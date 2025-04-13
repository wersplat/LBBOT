# 🧠 LeaderboardBot Setup Guide

This guide walks you through setting up, deploying, and running the full **LeaderboardBot** system — including the Discord bot, Flask dashboard, OCR processing, Google Sheets integration, and webhook sync.

---

## 🚀 Features Overview

- 🧠 **OCR-Driven Stat Parsing**: Extract team names and scores from images
- 🏀 **Team Win/Loss Tracking**: Auto-update standings based on results
- 📊 **Web Dashboard**: Live leaderboard, game history, and team views
- 📎 **Google Sheets Sync**: Weekly backup of games and standings (per season tab)
- 🔔 **Webhook Notifications**: Auto-send updates to Discord with timestamps + admin tags
- 🐳 **Docker-Ready**: One-command deployment stack with NGINX reverse proxy

---

## 🧩 Prerequisites

| Requirement        | Notes                                 |
|--------------------|----------------------------------------|
| Python 3.9+        | Recommended for local setup            |
| Tesseract OCR      | Required for parsing screenshots       |
| Google Service Account | With Sheets API enabled            |
| Discord Bot Token  | Add the bot to your server             |
| Docker + Docker Compose | Optional but recommended         |

---

## 🛠 Local Setup (Dev Mode)

```bash
# Clone and prepare environment
git clone https://github.com/wersplat/LeaderboardBot.git
cd LeaderboardBot
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
# Run OCR server
python3 ocr_server.py

# Run Flask dashboard
python3 app.py

# Run Discord bot
python3 bot.py

# Run webhooks sync
python3 sync.py
```

---

## 🚀 Deployment (Production Mode)

```bash
# Build Docker images
docker build -t leaderboardbot .

# Run Docker stack
docker stack deploy --compose-file docker-compose.yml leaderboardbot
```

---

## 📚 Documentation

- [LeaderboardBot Documentation](https://docs.leaderboardbot.com)
- [LeaderboardBot API Documentation](https://docs.leaderboardbot.com/api)

---

## 📚 Resources

- [LeaderboardBot GitHub Repository](https://github.com/wersplat/LeaderboardBot)
- [LeaderboardBot Discord Server](https://discord.gg/leaderboardbot)

---

## 📝 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 📝 Credits

- [LeaderboardBot](https://github.com/wersplat/LeaderboardBot) - The project was created by [wersplat](https://github.com/wersplat).
- [LeaderboardBot Documentation](https://docs.leaderboardbot.com) - The documentation was created by [wersplat](https://github.com/wersplat).
- [LeaderboardBot API Documentation](https://docs.leaderboardbot.com/api) - The API documentation was created by [wersplat](https://github.com/wersplat).
- [LeaderboardBot GitHub Repository](https