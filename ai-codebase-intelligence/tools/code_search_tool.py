from langchain.tools import BaseTool


class CodeSearchTool(BaseTool):
    name = "Code Search Tool"
    description = "Searches relevant code snippets"

    def __init__(self, vector_db):
        super().__init__()
        self.vector_db = vector_db

    def _run(self, query: str):
        docs = self.vector_db.similarity_search(query, k=5)

        return "\n\n".join(
            [doc.page_content for doc in docs]
        )