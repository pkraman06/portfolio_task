from crewai import Agent


def create_critic_agent():
    return Agent(
        role="Critic",
        goal="Review generated solutions and improve accuracy",
        backstory="Code reviewer focused on optimization and correctness.",
        verbose=True,
    )