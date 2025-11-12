#Requirements:
Python 3.8+
pip (Python package installer)
Discord Bot Token (from Discord Developer Portal)

#Commands:
git clone https://github.com/yourusername/discord-bot.git
cd discord-bot
python -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate      # Windows
pip install -r requirements.txt

#Config:
TOKEN = "YOUR_DISCORD_BOT_TOKEN"
AUTHORIZED_USER_ID = 123456789012345678  # Your Discord user ID

#Start:
python3 bot.py

If everything is OK, you will see a message like:
We have logged in as MyBot#1234

#Discord:
User ID in Discord:
User Settings → Advanced → Developer Mode
Right Click → Copy ID.

Bot Token:
Discord Developer Portal → Applications → Your App → Bot → Reset Token


