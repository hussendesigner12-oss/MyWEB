from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import requests
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')


def send_telegram(text: str) -> None:
    if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
        raise RuntimeError('Telegram configuration missing. Set TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID in .env')

    url = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage'
    payload = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': text,
        'parse_mode': 'HTML'
    }
    resp = requests.post(url, data=payload, timeout=10)
    resp.raise_for_status()


@app.route('/api/consultation', methods=['POST'])
def consultation():
    data = request.get_json() or {}
    required = ['subject', 'name', 'whatsapp', 'telegram', 'message']
    errors = []
    for field in required:
        if not data.get(field):
            errors.append(f'{field} is required')

    if errors:
        return jsonify({'success': False, 'errors': errors}), 400

    # Compose telegram message (HTML)
    tg_text = (
        f"<b>استشارة جديدة</b>\n"
        f"موضوع: {data.get('subject')}\n"
        f"الاسم: {data.get('name')}\n"
        f"واتساب: {data.get('whatsapp')}\n"
        f"تيليجرام: {data.get('telegram')}\n\n"
        f"<b>الرسالة:</b>\n{data.get('message')}"
    )

    try:
        send_telegram(tg_text)
    except Exception as e:
        return jsonify({'success': False, 'message': f'Telegram send failed: {str(e)}'}), 500

    return jsonify({'success': True, 'message': 'Sent to Telegram'})


if __name__ == '__main__':
    port = int(os.getenv('PORT', '3000'))
    app.run(host='0.0.0.0', port=port)
