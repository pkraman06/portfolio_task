from crewai import Crew, Task

from agents.planner_agent import create_planner_agent
from agents.researcher_agent import create_researcher_agent
from agents.developer_agent import create_developer_agent
from agents.critic_agent import create_critic_agent


def build_crew(vector_db):
    planner = create_planner_agent()
    researcher = create_researcher_agent(vector_db)
    developer = create_developer_agent()
    critic = create_critic_agent()

    planning_task = Task(
        description="Analyze the user query and create a solution plan.",
        expected_output="Structured execution plan",
        agent=planner,
    )

    research_task = Task(
        description="Retrieve relevant code snippets and documentation.",
        expected_output="Relevant code context",
        agent=researcher,
    )

    development_task = Task(
        description="Generate or debug code based on findings.",
        expected_output="Working code solution",
        agent=developer,
    )

    review_task = Task(
        description="Review and improve the generated solution.",
        expected_output="Optimized final response",
        agent=critic,
    )

    return Crew(
        agents=[planner, researcher, developer, critic],
        tasks=[
            planning_task,
            research_task,
            development_task,
            review_task,
        ],
        verbose=True,
    )