# src/server.py
"""
Initial scaffold for Mem0 MCP Server.
Implements a minimal FastAPI server with a health check endpoint.
"""

from fastapi import FastAPI

app = FastAPI(title="Mem0 MCP Server")

# Root endpoint for friendlier UX
@app.get("/")
def root():
    """Welcome message and endpoint listing."""
    return {
        "message": "Welcome to the Mem0 MCP Server!",
        "endpoints": [
            "/health",
            "/memory (POST)",
            "/memory/{memory_id} (GET)"
        ]
    }

@app.get("/health")
def health_check():
    """Health check endpoint for server monitoring."""
    return {"status": "ok"}

# Step 1: Import mem0ai and initialize a simple mem0 client
import os
from mem0 import MemoryClient

# Use MEM0_API_KEY environment variable for security
MEM0_API_KEY = os.getenv("MEM0_API_KEY")
if not MEM0_API_KEY:
    mem0_client = None
    print("[ERROR] MEM0_API_KEY environment variable not set. Set it to your mem0 API key.")
else:
    # Correct usage per https://docs.mem0.ai/quickstart
    mem0_client = MemoryClient(api_key=MEM0_API_KEY)

# Step 2: Add /memory endpoints for storing, retrieving, updating, and deleting a memory
from fastapi import Request
from fastapi.responses import JSONResponse

@app.post("/memory")
async def store_memory(request: Request):
    """Store a memory using mem0 MemoryClient.
    Expects a JSON payload with:
      - messages: list of dicts (required)
      - user_id: string (optional)
    """
    try:
        if not mem0_client:
            return JSONResponse(status_code=500, content={"error": "mem0 MemoryClient not initialized"})
        data = await request.json()
        messages = data.get("messages")
        user_id = data.get("user_id")
        if not messages or not isinstance(messages, list):
            return JSONResponse(status_code=400, content={"error": "Missing or invalid 'messages' field (must be a list)"})
        # Store memory as per https://docs.mem0.ai/quickstart and your example
        memory_id = mem0_client.add(messages, user_id=user_id)
        return {"status": "stored", "id": memory_id}
    except Exception as e:
        # Log the full exception to the console for debugging
        import traceback
        print("[ERROR] Exception in /memory POST endpoint:")
        traceback.print_exc()
        # Return the error message in the response (for debugging only)
        return JSONResponse(status_code=500, content={"error": str(e)})

@app.get("/memory/{memory_id}")
async def get_memory(memory_id: str):
    """Retrieve a memory by ID using mem0ai client."""
    if not mem0_client:
        return JSONResponse(status_code=500, content={"error": "mem0ai not installed"})
    # Retrieve memory (this is a placeholder, actual mem0 usage may differ)
    # Correct usage per https://docs.mem0.ai/quickstart
    memory = mem0_client.get(id=memory_id)
    if not memory:
        return JSONResponse(status_code=404, content={"error": "Memory not found"})
    return {"id": memory_id, "memory": memory}

# Step 3: Add an endpoint to update a memory object
@app.put("/memory/{memory_id}")
async def update_memory(memory_id: str, request: Request):
    """Update a memory by ID using mem0ai client."""
    if not mem0_client:
        return JSONResponse(status_code=500, content={"error": "mem0ai not installed"})
    data = await request.json()
    text = data.get("text")
    if not text:
        return JSONResponse(status_code=400, content={"error": "Missing 'text' field"})
    # Update memory (placeholder, actual mem0 usage may differ)
    # Correct usage per https://docs.mem0.ai/quickstart
    updated = mem0_client.update(id=memory_id, text=text)
    if not updated:
        return JSONResponse(status_code=404, content={"error": "Memory not found or update failed"})
    return {"status": "updated", "id": memory_id}

# Step 4: Add an endpoint to delete a memory object
@app.delete("/memory/{memory_id}")
async def delete_memory(memory_id: str):
    """Delete a memory by ID using mem0ai client."""
    if not mem0_client:
        return JSONResponse(status_code=500, content={"error": "mem0ai not installed"})
    # Delete memory (placeholder, actual mem0 usage may differ)
    # Correct usage per https://docs.mem0.ai/quickstart
    deleted = mem0_client.delete(id=memory_id)
    if not deleted:
        return JSONResponse(status_code=404, content={"error": "Memory not found or delete failed"})
    return {"status": "deleted", "id": memory_id}
    if not deleted:
        return JSONResponse(status_code=404, content={"error": "Memory not found or delete failed"})
    return {"status": "deleted", "id": memory_id}

# Step 5: Add a /memory/search endpoint for searching/querying memories
from fastapi import Body

@app.post("/memory/search")
async def search_memory(payload: dict = Body(...)):
    """
    Search/query memories using mem0 MemoryClient.
    Expects a JSON payload with:
      - query: string (required)
      - user_id: string (optional)
    """
    if not mem0_client:
        return JSONResponse(status_code=500, content={"error": "mem0 MemoryClient not initialized"})
    query = payload.get("query")
    user_id = payload.get("user_id")
    if not query or not isinstance(query, str):
        return JSONResponse(status_code=400, content={"error": "Missing or invalid 'query' field (must be a string)"})
    # Search memory as per https://docs.mem0.ai/quickstart and your usage example
    try:
        results = mem0_client.search(query, user_id=user_id)
        return {"results": results}
    except Exception as e:
        import traceback
        print("[ERROR] Exception in /memory/search endpoint:")
        traceback.print_exc()
        return JSONResponse(status_code=500, content={"error": str(e)})

# All endpoints are simple and testable. Extend as needed for full MCP compliance.
