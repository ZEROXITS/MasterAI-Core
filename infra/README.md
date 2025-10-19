# MasterAI-Core

![MasterAI Logo](https://via.placeholder.com/150)

**MasterAI-Core** هو مشروع ذكاء اصطناعي متكامل مفتوح المصدر، يوفر نواة قوية للإجابة على الأسئلة، مع دعم ذاكرة داخلية ونظام RAG (Retrieval-Augmented Generation) لتحسين الدقة.  
تم تصميمه ليكون قابلًا للتوسع، سهل التشغيل، وجاهز للاستخدام على منصات متعددة مثل Replit، Google Colab، وHugging Face Spaces.

---

## 📌 المميزات
- موديل رئيسي للإجابة على الأسئلة + موديلات ثانوية لتحسين الأداء.
- ذاكرة لحفظ الأسئلة والإجابات لتوفير سياق مستمر.
- نظام RAG لاسترجاع معلومات دقيقة من مستندات أو نصوص مخصصة.
- دعم التشغيل على GPU إذا كان متاحًا.
- Docker-ready لتسهيل النشر على أي سيرفر.
- مفتوح المصدر بالكامل ومجاني.

---

## ⚙️ المتطلبات
- Python 3.11+
- مكتبات Python الموجودة في `requirements.txt`
- Docker (اختياري)

---

## 🚀 طريقة التشغيل

### تشغيل محلي
```bash
git clone https://github.com/your-username/masterai-core.git
cd masterai-core
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 8080