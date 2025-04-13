Here’s the **GitHub Copilot-friendly step-by-step guide** (`ROADMAP.md`) that will be included in the LeaderboardBot package. It's written in a structure Copilot can recognize and assist with auto-completion, especially during GitHub Codespaces or VS Code usage.

---

```markdown
# 🧠 LeaderboardBot Development Roadmap

This file provides a step-by-step implementation plan for **LeaderboardBot**, designed to be easily followed and executed by developers or GitHub Copilot.

---

## ✅ Phase 1: Project Initialization

```bash
# 1. Clone the repo and install dependencies
git clone https://github.com/wersplat/LeaderboardBot.git
cd LeaderboardBot
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## 🧱 Phase 2: Discord Bot Setup

- [ ] Configure `bot/config.py` with your Discord bot token and target channel ID.
- [ ] Run the bot with:
```bash
python3 bot/main.py
```
- [ ] Bot listens for image uploads, runs OCR, and extracts team names + scores.
- [ ] Automatically determines winner/loser and updates standings in SQLite.

---

## 🔍 Phase 3: OCR Processing

- [ ] Install Tesseract on your system (`apt install tesseract-ocr` or `brew install tesseract`)
- [ ] OCR logic is in `ocr/parse.py`
- [ ] Bot calls `parse_screenshot(image)` on image upload

---

## 📊 Phase 4: Flask Dashboard Setup

- [ ] Run dashboard locally:
```bash
python3 dashboard/app.py
```
- [ ] Routes:
  - `/dashboard/leaderboard` – Live standings
  - `/dashboard/games` – Match history
  - `/dashboard/team/<team>` – Team page
  - `/dashboard/export/*.json` – Export endpoints

---

## 🗃 Phase 5: Database Structure

- [ ] Uses `sqlite3` under `/data/leaderboard.db`
- [ ] Tables:
  - `games (team1, score1, team2, score2, winner, timestamp, season)`
  - `standings (team, wins, losses, season)`

---

## 📦 Phase 6: Docker Deployment

- [ ] Build with:
```bash
docker-compose up --build
```
- [ ] Services:
  - `bot` – Discord listener
  - `dashboard` – Flask web UI
  - `nginx` – Reverse proxy for `/dashboard`

---

## 🌐 Phase 7: Google Sheets Integration

- [ ] Go to `/dashboard/admin/sheets-config`
- [ ] Fill in:
  - Google Sheet ID
  - Service Account Email
  - Upload credentials JSON
  - Set export interval (weekly default)

- [ ] Run scheduled exporter:
```bash
python3 dashboard/sync_google_sheets.py
```

---

## 🔁 Phase 8: Webhook Sync

- [ ] Admin-triggered or scheduled sync sends webhook to Discord
- [ ] Message includes:
  - Timestamp (`<t:UNIXTIME:f>`)
  - Admin name
  - Export type
  - Sheet link

---

## ✅ Final Notes

- All code is GPLv3 licensed
- Themes match BodegaCatsGC and Road to $25K branding
- Full JSON + CSV export enabled for audit and backup

---

> Use GitHub Copilot to autocomplete function stubs and extend logic in:
> - `bot/main.py`
> - `ocr/parse.py`
> - `db/utils.py`
> - `dashboard/routes/*.py`
> - `dashboard/templates/*.html`
```

---

Let me know if you want a preview of `SETUP.md`, too — or any tweaks to fit this better into your workflow!