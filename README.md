# 🎮 League of Legends Patch Tracker & Discord Notifier

An automated Python service that monitors Riot Games' Data Dragon API for new game patches, tracks local state, and dispatches real-time alerts via Discord Webhooks.

---

## About This Project

This project was developed for **learning purposes** as part of hands-on practice with public REST API integration, local state persistence, webhook automation, and secure environment variable configuration in Python.

---

## ✨ Features

- **Public API Ingestion:** Fetches real-time version releases from Riot Games' Data Dragon without requiring an API key.
- **State Persistence:** Automatically initializes and manages a local state file (`last_patch.txt`) to compare version differences.
- **Event-Driven Alerts:** Posts instant notifications to a configured Discord channel via Webhook when a new patch is detected.
- **Secure Configuration:** Protects sensitive Webhook URLs using environment variables via `python-dotenv`.
- **Resilient Execution:** Safely creates the local state on first run without throwing `FileNotFoundError` or triggering false alarms.

---

## What I Learned

- Consuming third-party REST APIs and parsing JSON responses using Python's `requests` library.
- Managing persistent local state with file I/O operations (`with open(...)`).
- Handling external event-driven notifications through Discord Webhooks using HTTP POST requests.
- Implementing security hygiene by managing credentials with `python-dotenv` and `.gitignore`.
- Handling edge cases and initial application bootstrap flows with the `os` module.

---

## 🛠️ Project Structure

```text
lol-patch-bot/
│
├── patch_tracker.py    # Main monitoring and notification logic
├── requirements.txt    # Project dependencies
├── .env.example        # Environment variables template
├── .gitignore          # Ignored local files (.env, last_patch.txt, cache)
└── README.md           # Documentation
```

## Installation & Usage

1. Clone the repository:
   ```bash
   git clone [https://github.com/](https://github.com/)<your-username>/<your-repo-name>.git
   cd <your-repo-name>
   ```
