#!/bin/bash

# ==================================================
# MasterAI-Core Deployment Script
# ==================================================

echo "=============================="
echo "🚀 Starting MasterAI-Core Deployment..."
echo "=============================="

# تفعيل بيئة افتراضية (اختياري)
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

echo "Activating virtual environment..."
source venv/bin/activate

# تحديث pip وتثبيت المتطلبات
echo "Installing requirements..."
pip install --upgrade pip
pip install -r requirements.txt

# إنشاء المجلدات الأساسية
mkdir -p data logs models

# تشغيل السيرفر مباشرة عبر Python
echo "Starting FastAPI server..."
uvicorn app.main:app --host 0.0.0.0 --port 8080

# بديل: تشغيل عبر Docker
# echo "Building Docker image..."
# docker build -t masterai-core .
# echo "Running Docker container..."
# docker run -p 8080:8080 masterai-core

echo "=============================="
echo "✅ MasterAI-Core is running!"
echo "=============================="