import requests
import os
from flask import jsonify
from dotenv import load_dotenv

load_dotenv()

PAGE_TOKEN = os.getenv('PAGE_TOKEN')
VERIFY_TOKEN = os.getenv('VERIFY_TOKEN')
MESSENGER_URL = 'https://graph.facebook.com/v20.0/me/messages'

def send_message(recipient_id: str, text: str):
    """Send a text message to a Messenger user."""
    payload = {
        "recipient": {"id": recipient_id},
        "message": {"text": text}
    }
    params = {"access_token": PAGE_TOKEN}
    response = requests.post(MESSENGER_URL, json=payload, params=params)
    if response.status_code != 200:
        print(f"Messenger send error: {response.text}")
    return response

def verify_webhook(request):
    """Handle Facebook webhook verification challenge."""
    mode = request.args.get('hub.mode')
    token = request.args.get('hub.verify_token')
    challenge = request.args.get('hub.challenge')
    if mode == 'subscribe' and token == VERIFY_TOKEN:
        print('Webhook verified!')
        return challenge, 200
    return 'Forbidden', 403
