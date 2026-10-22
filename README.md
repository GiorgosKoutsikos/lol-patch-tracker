# 🎮 League of Legends Patch Tracker & Discord Notifier

An automated Python service that monitors Riot Games' Data Dragon API for new game patches, tracks local state, and dispatches real-time alerts via Discord Webhooks.

---

## About This Project

This project was developed for **learning purposes** as part of hands-on practice with public REST API integration, local state persistence, webhook automation, and secure environment variable configuration in Python.

---

## ✨ Features

- **Public API Ingestion:** Fetches real-time version releases from Riot Games' Data Dragon without requiring an API key.
- **Cloud Automation (Cron Scheduler):** Runs automatically every 2 hours via GitHub Actions workflows without requiring an active local machine.
- **Automated Git Persistence:** Automatically tracks, commits, and pushes version updates (`last_patch.txt`) directly back to the GitHub repository.
- **Event-Driven Alerts:** Posts instant notifications to a configured Discord channel via Webhook when a new patch is detected.
- **Secure Configuration:** Protects sensitive Webhook URLs locally via `.env` (`python-dotenv`) and in the cloud using GitHub Actions Secrets.
- **Resilient Execution:** Safely initializes state on first run without throwing `FileNotFoundError` or triggering false alarms.

---

## What I Learned

- Consuming third-party REST APIs and parsing JSON responses using Python's `requests` library.
- Automating background tasks with **GitHub Actions** and POSIX cron scheduling.
- Managing persistent state across serverless runner environments using automated Git commits (`contents: write`).
- Handling external event-driven notifications through Discord Webhooks using HTTP POST requests.
- Implementing cloud and local security hygiene using GitHub Repository Secrets, `python-dotenv`, and `.gitignore`.
- Handling edge cases and initial application bootstrap flows with Python's `os` module.

---

## 📂 Project Structure

```text
lol-patch-bot/
│
├── .github/
│   └── workflows/
│       └── tracker.yml   # Scheduled CI/CD workflow (runs every 2 hours)
├── patch_tracker.py      # Main monitoring, file I/O, and alert logic
├── requirements.txt      # Project dependencies
├── last_patch.txt        # Tracked patch version state
├── .env.example          # Environment variable template
├── .gitignore            # Ignored local files (.env, __pycache__)
└── README.md             # Project documentation

## Installation & Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/<your-repo-name>.git
   cd <your-repo-name>
   ```
2. Install dependencies:
   ```bash
      pip install -r requirements.txt
   ```
3. Configure environment variables:
   Create a .env file from the example template:
   ```bash
   cp .env.example .env
   ```
   Add your Discord Webhook URL inside .env:
   ```
   DISCORD_WEBHOOK_URL=(https://discord.com/api/webhooks/your_actual_url_here)
   ```


