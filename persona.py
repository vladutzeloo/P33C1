import requests
import os
from dotenv import load_dotenv

load_dotenv()

NVIDIA_API_KEY = os.getenv('NVIDIA_API_KEY')
NVIDIA_URL = 'https://integrate.api.nvidia.com/v1/chat/completions'
MODEL = 'meta/llama-3.1-nemotron-70b-instruct'

# --- CUSTOMIZE THIS SYSTEM PROMPT ---
SYSTEM_PROMPT = """
You are [FRIEND_NAME], a person in a Facebook Messenger group chat.
Your personality:
- [Add personality trait 1, e.g. "Always jokes around and uses memes"]
- [Add personality trait 2, e.g. "Uses short replies, rarely writes more than 2 sentences"]
- [Add personality trait 3, e.g. "Obsessed with gaming, especially FPS games"]
- [Add personality trait 4, e.g. "Uses slang like 'bro', 'lmao', 'ngl'"]
- [Add personality trait 5, e.g. "Never uses formal language"]
Respond ONLY as [FRIEND_NAME]. Keep replies short and casual, max 2-3 sentences.
Never break character. Never say you are an AI.
"""

conversation_history = []

def get_persona_response(user_message: str) -> str:
    conversation_history.append({"role": "user", "content": user_message})
    
    # Keep last 10 messages for context
    recent_history = conversation_history[-10:]
    
    headers = {
        "Authorization": f"Bearer {NVIDIA_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": MODEL,
        "messages": [{"role": "system", "content": SYSTEM_PROMPT}] + recent_history,
        "max_tokens": 150,
        "temperature": 0.85
    }
    
    try:
        response = requests.post(NVIDIA_URL, headers=headers, json=payload, timeout=15)
        response.raise_for_status()
        reply = response.json()['choices'][0]['message']['content'].strip()
        conversation_history.append({"role": "assistant", "content": reply})
        return reply
    except Exception as e:
        print(f"NIM API error: {e}")
        return "lmao idk bro"
