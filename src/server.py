# src/server.py
"""
Initial scaffold for Mem0 MCP Server.
Implements a minimal FastAPI server with a health check endpoint.
"""

from fastapi import FastAPI

app = FastAPI(title="Mem0 MCP Server")

@app.get("/health")
def health_check():
    """Health check endpoint for server monitoring."""
    return {"status": "ok"}

# Step 1: Import mem0ai and initialize a simple mem0 client
try:
    import mem0ai
    mem0_client = mem0ai.Client()
except ImportError:
    mem0_client = None  # mem0ai not installed

# Step 2: Add a /memory endpoint for storing and retrieving a simple memory
from fastapi import Request
from fastapi.responses import JSONResponse

@app.post("/memory")
async def store_memory(request: Request):
    """Store a memory using mem0ai client."""
    if not mem0_client:
        return JSONResponse(status_code=500, content={"error": "mem0ai not installed"})
    data = await request.json()
    # For demonstration, we assume the payload has a 'text' field
    text = data.get("text")
    if not text:
        return JSONResponse(status_code=400, content={"error": "Missing 'text' field"})
    # Store memory (this is a placeholder, actual mem0 usage may differ)
    memory_id = mem0_client.add(text)
    return {"status": "stored", "id": memory_id}

@app.get("/memory/{memory_id}")
async def get_memory(memory_id: str):
    """Retrieve a memory by ID using mem0ai client."""
    if not mem0_client:
        return JSONResponse(status_code=500, content={"error": "mem0ai not installed"})
    # Retrieve memory (this is a placeholder, actual mem0 usage may differ)
    memory = mem0_client.get(memory_id)
    if not memory:
        return JSONResponse(status_code=404, content={"error": "Memory not found"})
    return {"id": memory_id, "memory": memory}

# All endpoints are simple and testable. Extend as needed for full MCP compliance.
