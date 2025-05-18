# MyFitnessPal WhatsApp Macro Automation

Automate sending your daily MyFitnessPal macro summary to your coach on WhatsApp using Python, Twilio, and a cron job.

---

## ⚠️ Important Note: Chrome Login Required

This project **requires you to be logged into MyFitnessPal in your local Chrome browser**.  
The script uses your Chrome cookies (via `browser_cookie3`) to access your MyFitnessPal data.

**Limitations:**

- This script **will only work when run interactively as the same OS user who is logged into Chrome and MyFitnessPal**.
- It will **NOT work** when triggered by a background process (like cron), over SSH, or on another machine.
- It will **NOT work in cloud environments** or on servers without your Chrome profile and unlocked OS keychain.

**Why?**  
MyFitnessPal no longer offers a public API, so programmatic access requires either browser cookies (with a logged-in browser session) or manual data export.

**Best for:**  
Personal use, manual daily execution, or as a local demo project.

---

## Setup Instructions

### 1. Login to MyFitnessPal in Chrome

- Make sure you are logged into [MyFitnessPal](https://www.myfitnesspal.com/) in Chrome **as the same OS user who will run the script**.

### 2. Clone the repo & install dependencies

```bash
git clone https://github.com/PreetiKharb/myfitnesspal-whatsapp-automation.git
cd myfitnesspal-whatsapp-automation
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Configure Environment Variables

- Copy .env.example to .env and fill in your credentials:
  - Twilio credentials (see below)

### Setup Twilio WhatsApp Sandbox

- Sign up at Twilio (free tier available).
- Go to the Twilio WhatsApp Sandbox.
- Join the sandbox from your WhatsApp and have your coach join as well.
- Get your ACCOUNT SID, AUTH TOKEN, and use the sandbox WhatsApp number.

### Run the Script Manually

```bash
python main.py
```
