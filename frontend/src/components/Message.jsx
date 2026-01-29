import React from 'react';
import ReactMarkdown from 'react-markdown';
import styles from './Message.module.css';

const Message = ({ message, isStreaming }) => {
    const isUser = message.role === 'user';

    return (
        <div className={`${styles.messageRow} ${isUser ? styles.userRow : styles.botRow}`}>
            {!isUser && <div className={styles.avatar}></div>}
            <div className={styles.contentColumn}>
                <div className={isUser ? styles.userBubble : styles.botBubble}>
                    {isUser ? (
                        <p>{message.content}</p>
                    ) : (
                        <ReactMarkdown
                            components={{
                                table: ({ node, ...props }) => (
                                    <div className={styles.tableWrapper}>
                                        <table className={styles.table} {...props} />
                                    </div>
                                ),
                                th: ({ node, ...props }) => (
                                    <th className={styles.th} {...props} />
                                ),
                                td: ({ node, ...props }) => (
                                    <td className={styles.td} {...props} />
                                ),
                                p: ({ node, ...props }) => (
                                    <p className={styles.paragraph} {...props} />
                                ),
                                ul: ({ node, ...props }) => (
                                    <ul className={styles.list} {...props} />
                                ),
                                ol: ({ node, ...props }) => (
                                    <ol className={styles.list} {...props} />
                                ),
                                h2: ({ node, ...props }) => (
                                    <h2 className={styles.heading2} {...props} />
                                ),
                                h3: ({ node, ...props }) => (
                                    <h3 className={styles.heading3} {...props} />
                                ),
                                strong: ({ node, ...props }) => (
                                    <strong className={styles.bold} {...props} />
                                ),
                                code: ({ node, inline, ...props }) => (
                                    inline
                                        ? <code className={styles.inlineCode} {...props} />
                                        : <code className={styles.codeBlock} {...props} />
                                ),
                            }}
                        >
                            {message.content}
                        </ReactMarkdown>
                    )}
                    {isStreaming && <span className={styles.cursor}>▊</span>}
                </div>
            </div>
        </div>
    );
};

export default Message;
