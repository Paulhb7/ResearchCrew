from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class MyProjectCrew:
    
    @agent
    def researcher(self) -> Agent:
        return Agent(config=self.agents_config["researcher"])

    @agent
    def coder(self) -> Agent:
        return Agent(config=self.agents_config["coder"])

    @agent
    def reviewer(self) -> Agent:
        return Agent(config=self.agents_config["reviewer"])

    @task
    def research_task(self) -> Task:
        return Task(config=self.tasks_config["research_task"])

    @task
    def coding_task(self) -> Task:
        return Task(config=self.tasks_config["coding_task"])

    @task
    def review_task(self) -> Task:
        return Task(config=self.tasks_config["review_task"])

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=[self.researcher(), self.coder(), self.reviewer()],
            tasks=[self.research_task(), self.coding_task(), self.review_task()],
            verbose=True
        )
