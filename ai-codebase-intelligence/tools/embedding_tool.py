from sentence_transformers import SentenceTransformer


class EmbeddingTool:
    def __init__(self):
        self.model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

    def embed(self, texts):
        return self.model.encode(texts)