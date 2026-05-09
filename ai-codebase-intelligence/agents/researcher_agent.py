from crewai import Agent
from tools.code_search_tool import CodeSearchTool
from tools.web_search_tool import WebSearchTool


def create_researcher_agent(vector_db):
    return Agent(
        role="Researcher",
        goal="Retrieve relevant code and documentation",
        backstory="Specialist in semantic code retrieval and research.",
        tools=[
            CodeSearchTool(vector_db),
            WebSearchTool(),
        ],
        verbose=True,
    )