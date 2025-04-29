"""
Example Python client for interacting with the Mem0 MCP Server.
Demonstrates storing, retrieving, updating, deleting, and searching for memories.
"""
import requests

BASE_URL = "http://localhost:8000"  # Change if server is remote

# Store a memory
def store_memory(text):
    resp = requests.post(f"{BASE_URL}/memory", json={"text": text})
    return resp.json()

# Retrieve a memory by ID
def get_memory(memory_id):
    resp = requests.get(f"{BASE_URL}/memory/{memory_id}")
    return resp.json()

# Update a memory by ID
def update_memory(memory_id, text):
    resp = requests.put(f"{BASE_URL}/memory/{memory_id}", json={"text": text})
    return resp.json()

# Delete a memory by ID
def delete_memory(memory_id):
    resp = requests.delete(f"{BASE_URL}/memory/{memory_id}")
    return resp.json()

# Search for memories
def search_memory(query):
    resp = requests.post(f"{BASE_URL}/memory/search", json={"query": query})
    return resp.json()

if __name__ == "__main__":
    # Example usage
    print("Storing memory...")
    store_result = store_memory("example memory for MCP")
    print("Store result:", store_result)
    memory_id = store_result.get("id")

    if memory_id:
        print("Retrieving memory...")
        print(get_memory(memory_id))

        print("Updating memory...")
        print(update_memory(memory_id, "updated memory text"))

        print("Searching for memory...")
        print(search_memory("updated"))

        print("Deleting memory...")
        print(delete_memory(memory_id))
