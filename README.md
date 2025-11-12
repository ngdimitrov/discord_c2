# 🤖 Discord Bot

A simple Discord bot written in **Python** using the `discord.py` library.

---

## Requirements

- Python **3.8+**  
- **pip** (Python package installer)  
- **Discord Bot Token** (from [Discord Developer Portal](https://discord.com/developers/applications))

---
## Configuration

TOKEN = "YOUR_DISCORD_BOT_TOKEN"
AUTHORIZED_USER_ID = 123456789012345678  # Your Discord user ID

---

## Discord Setup
Get Your User ID in Discord

Go to User Settings → Advanced → Enable Developer Mode

Right-click on your user → Copy ID

Get Your Bot Token

Visit the Discord Developer Portal

Select your app → Bot tab → Reset Token → Copy and paste it into your code


discord-bot/
│
├── bot.py               # Main bot script
├── requirements.txt     # Dependencies
└── README.md            # Documentation


## 🛠️ Installation

```bash
git clone https://github.com/yourusername/discord-bot.git
cd discord-bot
python -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate      # Windows
pip install -r requirements.txt
```


## Start the Bot
```python3 bot.py```
If everything is OK, you’ll see a message like:
We have logged in as MyBot#1234
