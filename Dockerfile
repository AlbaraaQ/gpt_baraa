# استخدم صورة Python الرسمية كأساس
FROM python:3.11-slim

# تعيين المجلد الذي سيعمل فيه التطبيق داخل الحاوية
WORKDIR /app

# نسخ ملفات المشروع إلى الحاوية
COPY . /app

# تحديث الحزم وتثبيت المكتبات اللازمة
RUN apt-get update && apt-get install -y libgl1-mesa-glx

# تثبيت المكتبات المطلوبة من ملف requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# تحديد الأمر الذي سيتم تشغيله عند بدء الحاوية
CMD ["python", "main.py"]
