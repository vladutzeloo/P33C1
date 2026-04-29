from flask import Flask, request, jsonify
from persona import get_persona_response
from messenger import send_message, verify_webhook
import os

app = Flask(__name__)

@app.route('/webhook', methods=['GET'])
def webhook_verify():
    return verify_webhook(request)

@app.route('/webhook', methods=['POST'])
def webhook_receive():
    print(">>> WEBHOOK POST RECEIVED")
    data = request.get_json()
    print(f">>> DATA: {data}")
    if data.get('object') == 'page':
        for entry in data.get('entry', []):
            for messaging in entry.get('messaging', []):
                sender_id = messaging['sender']['id']
                message = messaging.get('message', {})
                text = message.get('text', '')
                print(f">>> TEXT: {text}")
                if text:
                    reply = get_persona_response(text)
                    print(f">>> REPLY: {reply}")
                    send_message(sender_id, reply)
    return jsonify({'status': 'ok'})

if __name__ == '__main__':
    app.run(port=5000, debug=True)
