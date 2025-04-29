"""
Example Python client for interacting with the Mem0 MCP Server.
Demonstrates storing, retrieving, updating, deleting, and searching for memories.
"""
import requests

BASE_URL = "http://localhost:8000"  # Change if server is remote
import requests
from requests.exceptions import RequestException

# Store a memory with graceful error handling
def store_memory(text):
    try:
        resp = requests.post(f"{BASE_URL}/memory", json={"text": text}, timeout=5)
        resp.raise_for_status()
        return resp.json()
    except RequestException as e:
        print(f"[ERROR] Failed to store memory: {e}")
        return None

# Retrieve a memory by ID with graceful error handling
def get_memory(memory_id):
    try:
        resp = requests.get(f"{BASE_URL}/memory/{memory_id}", timeout=5)
        resp.raise_for_status()
        return resp.json()
    except RequestException as e:
        print(f"[ERROR] Failed to retrieve memory {memory_id}: {e}")
        return None

# Update a memory by ID with graceful error handling
def update_memory(memory_id, text):
    try:
        resp = requests.put(f"{BASE_URL}/memory/{memory_id}", json={"text": text}, timeout=5)
        resp.raise_for_status()
        return resp.json()
    except RequestException as e:
        print(f"[ERROR] Failed to update memory {memory_id}: {e}")
        return None

# Delete a memory by ID with graceful error handling
def delete_memory(memory_id):
    try:
        resp = requests.delete(f"{BASE_URL}/memory/{memory_id}", timeout=5)
        resp.raise_for_status()
        return resp.json()
    except RequestException as e:
        print(f"[ERROR] Failed to delete memory {memory_id}: {e}")
        return None

# Search for memories with graceful error handling
def search_memory(query):
    try:
        resp = requests.post(f"{BASE_URL}/memory/search", json={"query": query}, timeout=5)
        resp.raise_for_status()
        return resp.json()
    except RequestException as e:
        print(f"[ERROR] Failed to search memories: {e}")
        return None

if __name__ == "__main__":
    # Example usage
    print("Storing memory...")
    store_result = store_memory("example memory for MCP")
    print("Store result:", store_result)

    # Only proceed if store_result is valid and contains an 'id'
    if store_result and "id" in store_result:
        memory_id = store_result["id"]
        print("Retrieving memory...")
        print(get_memory(memory_id))

        print("Updating memory...")
        print(update_memory(memory_id, "updated memory text"))

        print("Searching for memory...")
        print(search_memory("updated"))

        print("Deleting memory...")
        print(delete_memory(memory_id))
    else:
        print("Failed to store memory. Aborting further operations.")
        exit(1)
