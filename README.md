# 💬 Kay – Human-Like WhatsApp Auto-Replier

**Kay** is a Python-based WhatsApp Web auto-reply bot that reads the latest message from your screen, checks if it’s sent by the other person, and replies naturally using **Google's Gemini API**. It mimics real human texting behavior, making your conversations feel alive even when you're away.

---

## 🧠 Features

- 📄 Reads messages directly from WhatsApp Web using screen automation
- 🔍 Detects if the message is received (not sent by you)
- 🤖 Uses Gemini to generate natural-sounding replies
- ✍️ Types and sends replies like a human
- 🔁 Continuously listens and responds in real-time

---

## 🛠️ Technologies Used

- **Language:** Python
- **Libraries:**
  - `pyautogui` – for mouse and keyboard automation
  - `pyperclip` – to access clipboard
  - `google.generativeai` – Gemini API integration
  - `time` – for control and delays

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/kay-bot.git
cd kay-bot

Install Dependencies
pip install pyautogui pyperclip google-generativeai
3. Set Your Gemini API Key

4. Open WhatsApp Web
Use Microsoft Edge (preferred)

Log in to web.whatsapp.com

Open the chat you want Kay to monitor

5. Run the Bot
python kay.py

📌 Tips
Make sure your screen layout is similar to what the bot expects—this includes resolution and chat window position.

The bot relies on visual text selection; avoid moving your mouse or switching windows while it runs.

It talks like a real person but be cautious not to use it for spamming or sensitive chats.

📄 License
This project is intended for educational and experimental use only. Please use it responsibly.
