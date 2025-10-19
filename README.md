# MasterAI-Core

![MasterAI Logo](https://via.placeholder.com/150)  

**MasterAI-Core** هو مشروع ذكاء اصطناعي متكامل مفتوح المصدر، مصمم ليعمل كنواة ذكاء اصطناعي قوية مع دعم ذاكرة، RAG، ونماذج متعددة لتقديم إجابات ذكية وواقعية للمستخدمين.  

---

## 📌 المميزات
- دعم تشغيل عدة موديلات ذكاء اصطناعي في نفس المشروع.
- ذاكرة ذكية لحفظ المحادثات والمعلومات.
- RAG (Retrieval-Augmented Generation) للحصول على إجابات دقيقة.
- قابلية التوسع لتشغيل المشروع على منصات مجانية مثل Replit، Google Colab، Hugging Face Spaces.
- Docker-ready لتشغيل المشروع بسهولة في أي بيئة.

---

## ⚙️ متطلبات التشغيل
- Python 3.11+
- مكتبات Python الموجودة في `requirements.txt`
- Docker (اختياري لتشغيل الحاوية)

---

## 🚀 طريقة التشغيل

### 1️⃣ تشغيل محلي
```bash
git clone https://github.com/your-username/masterai-core.git
cd masterai-core
pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 8080