import React, { useState, useEffect, useRef } from 'react';
import Message from './components/Message';
import styles from './App.module.css';

function App() {
  const [messages, setMessages] = useState([
    {
      role: 'model',
      content: '👋 Hello! I\'m **TechScout AI**, your expert mobile phone shopping assistant.\n\nI can help you:\n- 📱 Compare phones side-by-side\n- 💰 Find the best deals under your budget\n- 🔍 Get detailed specs and reviews\n\nTry asking: *"Compare iPhone 15 vs Samsung S24"* or *"Best phones under 30000"*',
      type: 'text'
    }
  ]);
  const [input, setInput] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [isStreaming, setIsStreaming] = useState(false);
  const [isConnected, setIsConnected] = useState(false);
  const messagesEndRef = useRef(null);
  const wsRef = useRef(null);
  const streamingMessageRef = useRef('');

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  // WebSocket Connection
  useEffect(() => {
    let ws = null;
    let reconnectInterval = null;

    const connectWS = () => {
      ws = new WebSocket('ws://localhost:8000/ws');
      wsRef.current = ws;

      ws.onopen = () => {
        console.log("[TechScout] Connected");
        setIsConnected(true);
        if (reconnectInterval) {
          clearInterval(reconnectInterval);
          reconnectInterval = null;
        }
      };

      ws.onclose = () => {
        console.log("[TechScout] Disconnected");
        setIsConnected(false);
        if (!reconnectInterval) {
          reconnectInterval = setInterval(() => {
            console.log("[TechScout] Reconnecting...");
            connectWS();
          }, 3000);
        }
      };

      ws.onmessage = (event) => {
        try {
          const data = JSON.parse(event.data);

          if (data.type === 'stream_start') {
            // Start streaming - add empty bot message
            streamingMessageRef.current = '';
            setIsStreaming(true);
            setMessages(prev => [...prev, {
              role: 'model',
              content: '',
              type: 'text'
            }]);
          }
          else if (data.type === 'stream_chunk') {
            // Append chunk to the last message
            streamingMessageRef.current += data.content;
            setMessages(prev => {
              const newMessages = [...prev];
              const lastIndex = newMessages.length - 1;
              if (lastIndex >= 0 && newMessages[lastIndex].role === 'model') {
                newMessages[lastIndex] = {
                  ...newMessages[lastIndex],
                  content: streamingMessageRef.current
                };
              }
              return newMessages;
            });
          }
          else if (data.type === 'stream_end') {
            // End streaming
            setIsStreaming(false);
            setIsLoading(false);
            streamingMessageRef.current = '';
          }
          else if (data.type === 'error') {
            setIsStreaming(false);
            setIsLoading(false);
            setMessages(prev => [...prev, {
              role: 'model',
              content: data.content || 'An error occurred.',
              type: 'text'
            }]);
          }
          // Legacy non-streaming response
          else if (data.content) {
            setMessages(prev => [...prev, {
              role: 'model',
              content: data.content,
              type: data.type || 'text',
              data: data.data
            }]);
            setIsLoading(false);
          }
        } catch (err) {
          console.error("[TechScout] Parse error:", err);
          setIsLoading(false);
          setIsStreaming(false);
        }
      };

      ws.onerror = (error) => {
        console.error("[TechScout] Error:", error);
        ws.close();
      };
    };

    connectWS();

    return () => {
      if (ws) ws.close();
      if (reconnectInterval) clearInterval(reconnectInterval);
    };
  }, []);

  const sendMessage = (e) => {
    e.preventDefault();
    if (!input.trim() || isLoading || !isConnected) return;

    const userMessage = { role: 'user', content: input.trim(), type: 'text' };
    setMessages(prev => [...prev, userMessage]);
    setInput('');
    setIsLoading(true);

    if (wsRef.current && wsRef.current.readyState === WebSocket.OPEN) {
      wsRef.current.send(JSON.stringify({ message: userMessage.content }));
    } else {
      setIsLoading(false);
      setMessages(prev => [...prev, {
        role: 'model',
        content: '🔴 Connection lost. Reconnecting...',
        type: 'text'
      }]);
    }
  };

  return (
    <div className={styles.appContainer}>
      <header className={styles.header}>
        <div className={styles.headerContent}>
          <h1>TechScout AI</h1>
          <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
            <div
              style={{
                width: '8px',
                height: '8px',
                borderRadius: '50%',
                backgroundColor: isConnected ? '#10b981' : '#ef4444',
                boxShadow: isConnected ? '0 0 8px #10b981' : 'none',
                transition: 'all 0.3s'
              }}
            />
            <span className={styles.badge}>{isConnected ? 'Live' : 'Offline'}</span>
          </div>
        </div>
      </header>

      <main className={styles.chatArea}>
        {messages.map((msg, index) => (
          <Message
            key={index}
            message={msg}
            isStreaming={isStreaming && index === messages.length - 1 && msg.role === 'model'}
          />
        ))}
        {isLoading && !isStreaming && (
          <div className={styles.loadingIndicator}>
            <div className={styles.dot}></div>
            <div className={styles.dot}></div>
            <div className={styles.dot}></div>
          </div>
        )}
        <div ref={messagesEndRef} />
      </main>

      <footer className={styles.inputArea}>
        <form onSubmit={sendMessage} className={styles.inputForm}>
          <input
            type="text"
            className={styles.input}
            placeholder={isConnected ? "Ask about phones, compare models..." : "Connecting..."}
            value={input}
            onChange={(e) => setInput(e.target.value)}
            disabled={isLoading || !isConnected}
          />
          <button
            type="submit"
            className={styles.sendButton}
            disabled={isLoading || !input.trim() || !isConnected}
          >
            {isLoading ? (
              <span style={{ fontSize: '0.75rem' }}>●●●</span>
            ) : (
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round">
                <line x1="22" y1="2" x2="11" y2="13"></line>
                <polygon points="22 2 15 22 11 13 2 9 22 2"></polygon>
              </svg>
            )}
          </button>
        </form>
      </footer>
    </div>
  );
}

export default App;
