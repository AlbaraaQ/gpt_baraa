# استخدم صورة Python الرسمية # استخدم صورة Python الرسمية كأساس
FROM python:3.11-slim

# تعيين المجلد الذي سيعمل فيه التطبيق داخل الحاوية
WORKDIR /app

# نسخ ملفات المشروع إلى الحاوية
COPY . /app

# تحديث الحزم وتثبيت git و libgl1-mesa-glx
RUN apt-get update && apt-get install -y git libgl1-mesa-glx

# تثبيت المكتبات المطلوبة من ملف requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# تحديد الأمر الذي سيتم تشغيله عند بدء الحاوية
CMD ["python", "main.py"]
# نسخ ملفات المشروع إلى الحاوية
COPY . /app

# تحديث الحزم وتثبيت git و libgl1-mesa-glx
RUN apt-get update && apt-get install -y git libgl1-mesa-glx

# تثبيت المكتبات المطلوبة من ملف requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# تحديد الأمر الذي سيتم تشغيله عند بدء الحاوية
CMD ["python", "main.py"]
