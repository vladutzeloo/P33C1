# P33C1 - AI Persona Messenger Bot

A Facebook Messenger chatbot powered by NVIDIA NIM that mimics a friend's personality in group chats.

---

## Setup

### 1. Clone & Install
```bash
git clone https://github.com/vladutzeloo/P33C1.git
cd P33C1
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Configure Environment
```bash
cp .env.example .env
# Edit .env with your actual keys
```

### 3. Customize the Persona
Open `persona.py` and edit the `SYSTEM_PROMPT`:
- Replace `[FRIEND_NAME]` with your friend's name
- Fill in personality traits, speech patterns, slang

### 4. Get API Keys
- **NVIDIA API Key**: [build.nvidia.com/settings/api-keys](https://build.nvidia.com/settings/api-keys)
- **Facebook Page Token**: [developers.facebook.com](https://developers.facebook.com) → Your App → Messenger → Access Tokens
- **Verify Token**: Any random string (e.g. `mysecrettoken123`)

### 5. Run Locally (for testing)
```bash
# Start Flask
python app.py

# In another terminal, expose with ngrok
ngrok http 5000
```
Paste the ngrok URL + `/webhook` in your Facebook App webhook settings.

### 6. Deploy to Production
```bash
# Example with Render or Railway
gunicorn app:app
```
Set environment variables in your hosting dashboard.

---

## Add Bot to Messenger Group
1. Go to your Facebook Group Chat
2. Tap group name → Add Members
3. Search for your Facebook Page name
4. Confirm → Bot joins and listens to all messages

---

## File Structure
```
P33C1/
├── app.py          # Flask webhook server
├── persona.py      # NVIDIA NIM API + system prompt
├── messenger.py    # Facebook Messenger helpers
├── requirements.txt
├── .env.example    # Env vars template
├── .gitignore
└── README.md
```
