import os
import pickle
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer
import numpy as np

class RAGManager:
    def __init__(self, config):
        self.enabled = config.get("enable", True)
        self.vector_store_path = config.get("vector_store_path", "./data/vectorstore")
        self.top_k = config.get("top_k", 5)

        if self.enabled:
            os.makedirs(self.vector_store_path, exist_ok=True)
            self.model = SentenceTransformer('all-MiniLM-L6-v2')
            self.vector_store_file = os.path.join(self.vector_store_path, "vectors.pkl")
            self._load_vector_store()

    def _load_vector_store(self):
        if os.path.exists(self.vector_store_file):
            with open(self.vector_store_file, "rb") as f:
                self.vector_store = pickle.load(f)
        else:
            self.vector_store = {"texts": [], "embeddings": []}

    def _save_vector_store(self):
        with open(self.vector_store_file, "wb") as f:
            pickle.dump(self.vector_store, f)

    def add_text(self, text):
        embedding = self.model.encode([text])[0]
        self.vector_store["texts"].append(text)
        self.vector_store["embeddings"].append(embedding)
        self._save_vector_store()

    def retrieve(self, query):
        if not self.enabled or len(self.vector_store["texts"]) == 0:
            return None

        query_vec = self.model.encode([query])[0]
        embeddings = np.array(self.vector_store["embeddings"])
        similarities = cosine_similarity([query_vec], embeddings)[0]

        # اختيار أعلى top_k نتائج
        top_indices = similarities.argsort()[-self.top_k:][::-1]
        results = [self.vector_store["texts"][i] for i in top_indices]

        return "\n".join(results)