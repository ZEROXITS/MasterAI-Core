import os
import logging
from datetime import datetime

# ==================================================
# إعداد Logging للمشروع
# ==================================================
def setup_logger(log_file="logs/masterai.log", level=logging.INFO):
    os.makedirs(os.path.dirname(log_file), exist_ok=True)
    logging.basicConfig(
        level=level,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.FileHandler(log_file, mode="a", encoding="utf-8"),
            logging.StreamHandler()
        ]
    )
    logging.info("Logger initialized.")

# ==================================================
# دالة قراءة الملفات النصية
# ==================================================
def read_text_file(file_path):
    if not os.path.exists(file_path):
        return ""
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

# ==================================================
# دالة حفظ نص في ملف
# ==================================================
def save_text_file(file_path, text):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(text)

# ==================================================
# دالة تنسيق السؤال مع السياق
# ==================================================
def prepare_input(question, context=None):
    if context:
        return f"{context}\n{question}"
    return question

# ==================================================
# دالة مساعدة لعرض الوقت الحالي
# ==================================================
def current_time_str():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")