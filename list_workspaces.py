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
    'Content-Type': 'application/json'
}

# Make the API request
response = requests.get(f'{base_url}/workspaces', headers=headers)

# Check if the request was successful
if response.status_code == 200:
    result = response.json()
    print("List of workspaces:")
    for workspace in result['workspaces']:
        print(f"- {workspace['name']}")
        print(f"- slug: {workspace['slug']}")
else:
    print(f"Error: {response.status_code}")
    print(response.text)
