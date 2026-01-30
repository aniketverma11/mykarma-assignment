# TechScout AI - Mobile Shopping Assistant

An intelligent AI-powered mobile phone shopping assistant built with FastAPI, React, and Google Gemini AI.

## Features

- 🤖 **AI-Powered Recommendations**: Uses Google Gemini 2.0 Flash for intelligent product suggestions
- 🔍 **Live Web Search**: Integrates FireCrawl API for real-time price and spec updates
- 💬 **Streaming Responses**: Real-time WebSocket communication with markdown support
- 📊 **Comparison Tables**: Beautiful markdown-rendered comparison tables
- 🎨 **Modern UI**: Premium dark theme with glassmorphism effects

## Tech Stack

**Backend:**
- FastAPI (Python 3.12+)
- Google Gemini AI (2.0 Flash with fallback to Flash Latest)
- FireCrawl API for web scraping
- WebSockets for real-time communication

**Frontend:**
- React 18
- Vite
- React Markdown
- CSS Modules

## Setup

### Prerequisites
- Python 3.12+
- Node.js 18+
- Google Gemini API Key
- FireCrawl API Key

### Installation

1. **Clone the repository**
```bash
git clone <your-repo-url>
cd assignment-mykarma
```

2. **Backend Setup**
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. **Configure Environment Variables**
Create `backend/.env`:
```env
GEMINI_API_KEY=your_gemini_api_key_here
FIRECRAWL_API_KEY=your_firecrawl_api_key_here
```

4. **Frontend Setup**
```bash
cd frontend
npm install
npm run build
```

## Running the Application

### Production Mode (Single Server)
The FastAPI server serves both the API and the built frontend:

```bash
cd backend
source venv/bin/activate
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

Then open: **http://localhost:8000**

### Development Mode (Separate Servers)
For development with hot reload:

**Terminal 1 - Backend:**
```bash
cd backend
source venv/bin/activate
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

**Terminal 2 - Frontend:**
```bash
cd frontend
npm run dev
```

Then open: **http://localhost:5173**

## Project Structure

```
assignment-mykarma/
├── backend/
│   ├── app/
│   │   ├── main.py           # FastAPI app + static file serving
│   │   ├── chat_engine.py    # Gemini AI integration
│   │   ├── firecrawl.py      # Web search integration
│   │   ├── data.py           # Mock phone database
│   │   └── models.py         # Pydantic models
│   ├── .env                  # API keys (not in git)
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── App.jsx           # Main React component
│   │   ├── components/
│   │   │   └── Message.jsx   # Markdown message renderer
│   │   └── App.module.css
│   ├── dist/                 # Production build
│   └── package.json
└── README.md
```

## API Endpoints

- `GET /` - Serves the frontend application
- `GET /api/health` - Health check endpoint
- `WebSocket /ws` - Real-time chat WebSocket

## WebSocket Protocol

**Client → Server:**
```json
{
  "message": "Compare iPhone 15 vs Samsung S24"
}
```

**Server → Client (Streaming):**
```json
{"type": "stream_start", "content": ""}
{"type": "stream_chunk", "content": "Here's a comparison..."}
{"type": "stream_chunk", "content": "\n\n| Feature | ..."}
{"type": "stream_end", "content": "<full_response>"}
```

## Features in Detail

### AI Model Fallback
- Primary: `gemini-2.0-flash` (fast, latest)
- Fallback: `gemini-flash-latest` (stable, when rate limited)

### Markdown Support
The AI can generate:
- **Tables** for comparisons
- **Bold** text for emphasis
- **Lists** for features
- **Headers** for organization

### Error Handling
- Graceful rate limit handling
- Automatic model fallback
- User-friendly error messages

## Deployment

### Docker (Optional)
```dockerfile
# Coming soon
```

### Traditional Deployment
1. Build frontend: `cd frontend && npm run build`
2. Install backend deps: `cd backend && pip install -r requirements.txt`
3. Set environment variables
4. Run: `uvicorn app.main:app --host 0.0.0.0 --port 8000`

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

MIT License - see LICENSE file for details

## Acknowledgments

- Google Gemini AI for the LLM
- FireCrawl for web scraping capabilities
- FastAPI and React communities
