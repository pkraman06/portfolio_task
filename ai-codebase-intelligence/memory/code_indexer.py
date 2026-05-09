import os

from langchain.docstore.document import Document

from memory.vector_store import create_vector_store


SUPPORTED_EXTENSIONS = [".py", ".js", ".ts", ".java", ".cpp"]


def load_code_files(repo_path):
    documents = []

    for root, _, files in os.walk(repo_path):
        for file in files:
            if any(file.endswith(ext) for ext in SUPPORTED_EXTENSIONS):
                path = os.path.join(root, file)

                with open(path, "r", encoding="utf-8") as f:
                    content = f.read()

                documents.append(
                    Document(
                        page_content=content,
                        metadata={"source": path},
                    )
                )

    return documents


def index_codebase(repo_path):
    docs = load_code_files(repo_path)
    return create_vector_store(docs)