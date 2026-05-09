from langchain.tools import BaseTool

import requests
from bs4 import BeautifulSoup


class WebSearchTool(BaseTool):
    name = "Web Search Tool"
    description = "Searches web content"

    def _run(self, query: str):

        url = f"https://duckduckgo.com/html/?q={query}"

        response = requests.get(url)

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        results = soup.find_all(
            "a",
            class_="result__a",
            limit=5
        )

        return "\n".join(
            [result.get_text() for result in results]
        )