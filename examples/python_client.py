"""
Example Python client for interacting with the Mem0 MCP Server.
Demonstrates storing, retrieving, updating, deleting, and searching for memories.
"""
import requests

BASE_URL = "http://localhost:8000"  # Change if server is remote
import requests
from requests.exceptions import RequestException

# Store a memory with graceful error handling
def store_memory(messages, user_id=None):
    """
    Store a memory by sending a list of messages and an optional user_id.
    messages: list of dicts (required by server)
    user_id: string (optional)
    """
    try:
        payload = {"messages": messages}
        if user_id:
            payload["user_id"] = user_id
        resp = requests.post(f"{BASE_URL}/memory", json=payload, timeout=5)
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
    messages = [
        {"role": "user", "content": "Hi, I'm Alex. I'm a vegetarian and I'm allergic to nuts."},
        {"role": "assistant", "content": "Hello Alex! I've noted that you're a vegetarian and have a nut allergy. I'll keep this in mind for any food-related recommendations or discussions."}
    ]
    store_result = store_memory(messages, user_id="alex")
    print(f"Store result: {store_result}")
    if not store_result or not store_result.get("id"):
        print("Failed to store memory. Aborting further operations.")
    else:
        memory_id = store_result["id"]
        print(f"Retrieving memory {memory_id}...")
        get_result = get_memory(memory_id)
        print(f"Get result: {get_result}")
        print(f"Updating memory {memory_id}...")
        update_result = update_memory(memory_id, "updated memory text")
        print(f"Update result: {update_result}")
        print(f"Deleting memory {memory_id}...")
        delete_result = delete_memory(memory_id)
        print(f"Delete result: {delete_result}")
