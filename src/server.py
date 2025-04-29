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

# TODO: Integrate mem0 and implement MCP endpoints
