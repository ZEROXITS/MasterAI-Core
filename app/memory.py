import sqlite3
import os

class MemoryManager:
    def __init__(self, config):
        self.enabled = config.get("enable", True)
        self.path = config.get("path", "./data/memory.db")
        self.max_entries = config.get("max_entries", 1000)

        if self.enabled:
            os.makedirs(os.path.dirname(self.path), exist_ok=True)
            self.conn = sqlite3.connect(self.path, check_same_thread=False)
            self.cursor = self.conn.cursor()
            self._create_table()

    def _create_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS memory (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT NOT NULL,
            answer TEXT NOT NULL
        )
        """)
        self.conn.commit()

    def save(self, question, answer):
        if not self.enabled:
            return

        # حذف أقدم السجلات إذا تجاوزت الحد الأقصى
        self.cursor.execute("SELECT COUNT(*) FROM memory")
        count = self.cursor.fetchone()[0]
        if count >= self.max_entries:
            self.cursor.execute("DELETE FROM memory WHERE id IN (SELECT id FROM memory ORDER BY id ASC LIMIT ?)", (count - self.max_entries + 1,))
            self.conn.commit()

        self.cursor.execute("INSERT INTO memory (question, answer) VALUES (?, ?)", (question, answer))
        self.conn.commit()

    def search(self, question):
        if not self.enabled:
            return None

        self.cursor.execute("SELECT answer FROM memory WHERE question LIKE ? ORDER BY id DESC LIMIT 1", (f"%{question}%",))
        result = self.cursor.fetchone()
        return result[0] if result else None

    def close(self):
        if self.enabled:
            self.conn.close()