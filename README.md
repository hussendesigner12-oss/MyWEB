# Consultation webhook (Flask)

C
Copy `.env.example` to `.env` and fill in your Telegram values.

Install dependencies and run:

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

The website's `consultation.html` already posts to `http://localhost:3000/api/consultation`.

Notes:
- This setup sends consultation submissions to your Telegram bot only.
- Create a bot with @BotFather and set `TELEGRAM_BOT_TOKEN` in `.env`.
- Get the numeric `TELEGRAM_CHAT_ID` by messaging your bot and calling `getUpdates` or using a helper script.