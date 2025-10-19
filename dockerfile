# استخدم صورة بايثون الأساسية
FROM python:3.11-slim

# إعداد مجلد العمل داخل الحاوية
WORKDIR /app

# نسخ ملفات المشروع إلى الحاوية
COPY . /app

# تحديث pip وتثبيت الحزم المطلوبة
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# إنشاء مجلد بيانات لتخزين الذاكرة والنماذج
RUN mkdir -p /app/data /app/models

# فتح البورت لتشغيل FastAPI
EXPOSE 8080

# أمر التشغيل الافتراضي
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]