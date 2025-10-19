from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import os

class ModelManager:
    def __init__(self, config):
        self.models = {}
        self.device = "cuda" if torch.cuda.is_available() else "cpu"

        # تحميل الموديل الرئيسي
        main_model_config = config.get("main_model", {})
        self.main_model_name = main_model_config.get("name", "gpt4all")
        self.main_model_path = main_model_config.get("path", "./models/gpt4all-model.bin")
        self.main_model_type = main_model_config.get("type", "llm")

        self.models["main"] = self._load_model(self.main_model_path)

        # تحميل الموديلات الثانوية (اختياري)
        self.secondary_models = []
        for m in config.get("secondary_models", []):
            model = self._load_model(m.get("path"))
            self.secondary_models.append(model)

    def _load_model(self, model_path):
        if not os.path.exists(model_path):
            print(f"[WARNING] Model path not found: {model_path}")
            return None
        try:
            tokenizer = AutoTokenizer.from_pretrained(model_path)
            model = AutoModelForCausalLM.from_pretrained(model_path)
            model.to(self.device)
            return {"model": model, "tokenizer": tokenizer}
        except Exception as e:
            print(f"[ERROR] Failed to load model {model_path}: {e}")
            return None

    def generate(self, question, context=None, max_length=200):
        model_data = self.models.get("main")
        if not model_data:
            return "Model not loaded."

        tokenizer = model_data["tokenizer"]
        model = model_data["model"]

        # دمج السياق مع السؤال
        input_text = question
        if context:
            input_text = f"{context}\n{question}"

        inputs = tokenizer.encode(input_text, return_tensors="pt").to(self.device)
        outputs = model.generate(inputs, max_length=max_length, pad_token_id=tokenizer.eos_token_id)
        answer = tokenizer.decode(outputs[0], skip_special_tokens=True)

        return answer