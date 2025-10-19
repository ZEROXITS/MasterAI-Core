from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.model_manager import ModelManager
from app.memory import MemoryManager
from app.rag import RAGManager
import yaml
import os

# ==================================================
# تحميل إعدادات المشروع من config.yaml
# ==================================================
config_path = os.path.join(os.path.dirname(__file__), "config.yaml")
with open(config_path, "r") as f:
    config = yaml.safe_load(f)

# ==================================================
# إنشاء تطبيق FastAPI
# ==================================================
app = FastAPI(
    title="MasterAI-Core",
    description="نواة ذكاء اصطناعي متكاملة مع ذاكرة وRAG",
    version="1.0.0"
)

# السماح بالوصول من أي دومين
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# ==================================================
# تهيئة المديرات
# ==================================================
model_manager = ModelManager(config["models"])
memory_manager = MemoryManager(config["memory"])
rag_manager = RAGManager(config["rag"])

# ==================================================
# مسار رئيسي لفحص عمل السيرفر
# ==================================================
@app.get("/")
async def root():
    return {"message": "MasterAI-Core Server is running!"}

# ==================================================
# مسار للإجابة على الاستفسارات
# ==================================================
@app.post("/ask")
async def ask(question: str):
    if not question:
        raise HTTPException(status_code=400, detail="Question is required")

    # البحث في الذاكرة أولاً
    memory_response = memory_manager.search(question)
    if memory_response:
        return {"answer": memory_response, "source": "memory"}

    # البحث باستخدام RAG
    rag_results = rag_manager.retrieve(question)

    # الحصول على إجابة من الموديل الرئيسي
    answer = model_manager.generate(question, context=rag_results)

    # حفظ السؤال والإجابة في الذاكرة
    memory_manager.save(question, answer)

    return {"answer": answer, "source": "model", "rag_context": rag_results}