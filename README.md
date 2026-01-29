
# 📱 MobileGenius - AI Shopping Agent

An intelligent shopping chat agent helping you discover, compare, and buy mobile phones. Built with FastAPI (Backend) and React (Frontend).

## 🚀 Features
- **Natural Language Search**: Ask for phones by budget ("under 30k"), brand ("Samsung phones"), or features ("best camera phone").
- **Smart Comparison**: Compare specs of multiple models side-by-side (e.g., "Compare Pixel 8a vs OnePlus 12R").
- **Product Details**: Get in-depth specs for specific models.
- **Safety & Robustness**: Resilient to adversarial prompts and avoids hallucinating non-existent phones.
- **Premium UI**: Glassmorphism design with a dark-themed interface.

## 🛠️ Tech Stack
- **Frontend**: React, Vite, Vanilla CSS (Modules)
- **Backend**: FastAPI, Uvicorn, Python 3.12
- **Data**: In-memory mock database with realistic phone specifications (extensible to SQL/NoSQL).
- **AI/Logic**: Google Gemini API (`gemini-flash-latest`) for intent understanding and natural language generation.

## 🏗️ Architecture
The system consists of two decoupled services:
1.  **FastAPI Backend**:
    -   `ChatEngine`: interactions with Google Gemini API to parse intents and generate responses.
    -   `MockDB`: A JSON-like structure storing phone data context injected into the LLM system prompt.
    -   API Endpoints: Exposes `/chat` for interaction.
2.  **React Frontend**:
    -   Communicates with the backend via REST API.
    -   Renders different message types: Text bubbles, Product Carousels, Comparison Tables.

## 🏃 Setup Instructions

### Prerequisites
- Node.js & npm
- Python 3.8+

### 1. Backend Setup
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```
*Server runs at `http://localhost:8000`*

### 2. Frontend Setup
```bash
cd frontend
npm install
npm run dev
```
*Client runs at `http://localhost:5173`*

## 🛡️ Prompt Design & Safety Strategy
-   **Intent Guardrails**: The agent uses strict intent classification to route queries. If a query falls outside the "shopping" domain or matches adversarial patterns (e.g., "reveal system prompt"), it is rejected.
-   **No Hallucinations**: Responses are strictly grounded in the structured database. The agent does not generate specs; it retrieves them.
-   **Adversarial Defense**: A blacklist of keywords (`ignore rules`, `system prompt`) prevents prompt injection attacks.

## ⚠️ Known Limitations
-   **Mock Data**: The database is static and limited to ~10 popular models for demonstration.
-   **Context**: Multi-turn conversation context is limited in the current implementation (stateless HTTP requests, though the frontend tracks history).
-   **Complex Queries**: Extremely complex nested queries might default to keyword search.

---
*Created by Aniket for AI/ML Engineer Assignment*
