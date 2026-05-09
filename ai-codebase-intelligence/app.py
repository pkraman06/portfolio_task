import os
import git
import streamlit as st

from memory.code_indexer import index_codebase

st.title("AI Codebase Intelligence")

repo_url = st.text_input("GitHub Repository URL")

query = st.text_area("Ask Question")


if st.button("Analyze Repository"):

    repo_name = repo_url.split("/")[-1]

    if not os.path.exists(repo_name):
        git.Repo.clone_from(
            repo_url,
            repo_name
        )

    st.success("Repository cloned")

    vector_db = index_codebase(repo_name)

    docs = vector_db.similarity_search(
        query,
        k=3
    )

    for doc in docs:
        st.code(doc.page_content[:1500])