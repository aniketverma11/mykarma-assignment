from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from dotenv import load_dotenv
from app.chat_engine import ChatEngine
import uvicorn
import asyncio
import os

load_dotenv()

app = FastAPI(title="TechScout AI")

# CORS configuration
origins = [
    "http://localhost:5173",
    "http://localhost:3000",
    "http://localhost:8000",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

chat_engine = ChatEngine()

# Mount static files from frontend build
static_path = os.path.join(os.path.dirname(__file__), "..", "..", "frontend", "dist")
if os.path.exists(static_path):
    app.mount("/assets", StaticFiles(directory=os.path.join(static_path, "assets")), name="assets")

@app.get("/")
def read_root():
    """Serve the frontend index.html"""
    index_path = os.path.join(static_path, "index.html")
    if os.path.exists(index_path):
        return FileResponse(index_path)
    return {"message": "TechScout AI API", "status": "online"}

@app.get("/api/health")
def health_check():
    return {"status": "healthy", "service": "TechScout AI"}

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    print("[TechScout] Client connected")
    
    try:
        while True:
            data = await websocket.receive_json()
            user_message = data.get("message")
            
            if user_message:
                print(f"[TechScout] Query: {user_message}")
                
                # Send streaming start signal
                await websocket.send_json({
                    "type": "stream_start",
                    "content": ""
                })
                
                # Stream response chunks
                full_content = ""
                async for chunk in chat_engine.process_query_stream(user_message):
                    full_content += chunk
                    await websocket.send_json({
                        "type": "stream_chunk",
                        "content": chunk
                    })
                    # Small delay to prevent overwhelming the client
                    await asyncio.sleep(0.01)
                
                # Send stream end signal with full content
                await websocket.send_json({
                    "type": "stream_end",
                    "content": full_content
                })
                
    except WebSocketDisconnect:
        print("[TechScout] Client disconnected")
    except Exception as e:
        print(f"[TechScout] WebSocket Error: {e}")
        try:
            await websocket.send_json({
                "type": "error",
                "content": "An error occurred. Please try again."
            })
        except:
            pass

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
