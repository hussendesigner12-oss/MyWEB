نشر سريع للخادم (Flask) والواجهة

1) المتطلبات
- امتلاك حساب على منصة نشر (Railway, Render, Heroku…).

2) خطوات النشر على Railway (مثال سريع)
- ادخل إلى https://railway.app وانشئ مشروعاً جديداً "Deploy from GitHub" واربط المستودع.
- في إعدادات الـ Service اختر "Deploy" ثم اضبط متغيرات البيئة (`TELEGRAM_BOT_TOKEN`, `TELEGRAM_CHAT_ID`).
- Railway سيستخدم `Procfile` و`requirements.txt` لتشغيل التطبيق عبر `gunicorn`.

3) بعد نشر الخادم
- ستحصل على عنوان مثل `https://your-app.up.railway.app`.
- افتح ملف `api_config.js` وعدّل السطر `const API_URL = "REPLACE_WITH_BACKEND_URL";` ليصبح:
  `const API_URL = "https://your-app.up.railway.app";`

4) إعداد الواجهة
- ضع ملفات الواجهة (HTML وimages) على GitHub Pages أو أي استضافة ستاتيك.
- تأكد أن `api_config.js` محدث ويُحمّل من نفس المسار مع `consultation.html`.

5) ملاحظات أمنية
- لا تضع `TELEGRAM_BOT_TOKEN` في الملفات الثابتة. ضعها فقط كمتغير بيئة في منصة الاستضافة.
- تأكد أن `CORS` في `app.py` يسمح بالوصول من نطاق الموقع الثابت إن لزم.
