import requests
import os
import json

# Get the API key from environment variable
api_key = os.environ.get('API_KEY')

# Set up the API endpoint
base_url = 'http://localhost:3001/api/v1'

# Set up the headers with the API key
headers = {
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}

# Function to send a chat query
def send_chat_query(workspace_slug, query):
    payload = {
        "message": "what movies did david lynch act in?",
        "mode": "query",
        "sessionId": "identifier-to-partition-chats-by-external-id",
        "attachments": []
    }

    url = f"{base_url}/workspace/{workspace_slug}/chat"
    print(f"Sending query to {url}")

    response = requests.post(url, headers=headers, json=payload, timeout=10*60)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        print(response.text)
        return None

# Example usage
workspace_id = "david-lynch"
query = "who has david lynch collaborate with?"

result = send_chat_query(workspace_id, query)

if result:
    print("Chat response:")
    print(json.dumps(result, indent=2))
