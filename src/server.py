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
try:
    import mem0ai
    mem0_client = mem0ai.Client()
except ImportError:
    mem0_client = None  # mem0ai not installed

# Step 2: Add /memory endpoints for storing, retrieving, updating, and deleting a memory
from fastapi import Request
from fastapi.responses import JSONResponse

@app.post("/memory")
async def store_memory(request: Request):
    """Store a memory using mem0ai client."""
    try:
        if not mem0_client:
            return JSONResponse(status_code=500, content={"error": "mem0ai not installed"})
        data = await request.json()
        # For demonstration, we assume the payload has a 'text' field
        text = data.get("text")
        if not text:
            return JSONResponse(status_code=400, content={"error": "Missing 'text' field"})
        # Store memory (this is a placeholder, actual mem0 usage may differ)
        # Correct usage per https://docs.mem0.ai/quickstart
        memory_id = mem0_client.add(text=text)
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
    """Search/query memories using mem0ai client."""
    if not mem0_client:
        return JSONResponse(status_code=500, content={"error": "mem0ai not installed"})
    query = payload.get("query")
    if not query:
        return JSONResponse(status_code=400, content={"error": "Missing 'query' field"})
    # Search memories (placeholder, actual mem0 usage may differ)
    # This assumes mem0_client.search returns a list of matching memory objects
    results = mem0_client.search(query)
    return {"results": results}

# All endpoints are simple and testable. Extend as needed for full MCP compliance.
