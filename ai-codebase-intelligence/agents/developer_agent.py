from crewai import Agent
from tools.python_exec_tool import PythonExecTool


def create_developer_agent():
    return Agent(
        role="Developer",
        goal="Generate and debug code solutions",
        backstory="Senior Python developer and debugging expert.",
        tools=[PythonExecTool()],
        verbose=True,
    )