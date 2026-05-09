from crewai import Agent


def create_planner_agent():
    return Agent(
        role="Planner",
        goal="Break coding problems into structured tasks",
        backstory="Expert software architect skilled in debugging and planning.",
        verbose=True,
        allow_delegation=True,
    )