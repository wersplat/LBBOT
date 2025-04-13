
# LeaderboardBot Roadmap

## Phase 1: Initialization
- [ ] Initialize Git repository
- [ ] Add GPLv3 LICENSE
- [ ] Create Python project structure
- [ ] Add Dockerfile and docker-compose.yml

## Phase 2: Discord Bot + OCR
- [ ] Implement bot to read screenshots from a specific channel
- [ ] Use Tesseract OCR to extract team names and scores
- [ ] Determine winner and update standings

## Phase 3: SQLite Stat Tracking
- [ ] Create `games` and `standings` tables
- [ ] Add logic to update standings after each result
- [ ] Implement JSON/CSV export

## Phase 4: Flask Dashboard
- [ ] Route all pages under `/dashboard`
- [ ] Build leaderboard, game history, and team pages
- [ ] Add division/season filters
- [ ] Add chart: wins over time
- [ ] Add admin upload/review tools

## Phase 5: Docker Deployment
- [ ] Build Flask app container
- [ ] Set up NGINX reverse proxy to `/dashboard`
- [ ] Add volume persistence for DB and images
