import requests
import os
from dotenv import load_dotenv

load_dotenv()
key = os.getenv('NVIDIA_API_KEY')
print(f"Key starts with: {key[:10]}...")

r = requests.post(
    'https://integrate.api.nvidia.com/v1/chat/completions',
    headers={'Authorization': f'Bearer {key}', 'Content-Type': 'application/json'},
    json={'model': 'meta/llama-3.1-8b-instruct', 'messages': [{'role': 'user', 'content': 'hello'}], 'max_tokens': 50}
)
print(r.status_code)
print(r.text[:300])
