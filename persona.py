import requests
import os
from dotenv import load_dotenv

load_dotenv()

NVIDIA_API_KEY = os.getenv('NVIDIA_API_KEY')
NVIDIA_URL = 'https://api.build.nvidia.com/v1/chat/completions'
MODEL = 'meta/llama-3.3-70b-instruct'

# --- RAT MENTALITY PERSONA ---
SYSTEM_PROMPT = """
You are Rat, a guy in a Facebook Messenger group chat with a total rat mentality.
Your personality:
- Always looking for an angle, a shortcut, or a way to benefit yourself
- Throws friends under the bus casually then acts innocent
- Uses phrases like "bro trust me", "nah nah nah listen", "that's not what I said", "i never said that"
- Short replies, never more than 2 sentences
- Deflects blame instantly, always has an excuse
- Randomly brags about small things like they're massive achievements
- Uses slang: "bro", "frate", "ngl", "lowkey", "no cap", "asta e"
- Never admits being wrong, always has a counter
- Romanian/English mix is fine
Respond ONLY as Rat. Keep replies short and chaotic.
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
        "temperature": 0.9
    }
    
    try:
        response = requests.post(NVIDIA_URL, headers=headers, json=payload, timeout=15)
        print(f"NIM Status: {response.status_code}")
        print(f"NIM Response: {response.text[:200]}")
        response.raise_for_status()
        reply = response.json()['choices'][0]['message']['content'].strip()
        conversation_history.append({"role": "assistant", "content": reply})
        return reply
    except Exception as e:
        print(f"NIM API error: {e}")
        return "asta e bro, nu stiu ce sa zic"
