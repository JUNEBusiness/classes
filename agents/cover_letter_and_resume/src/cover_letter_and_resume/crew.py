from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai_tools import FileWriterTool, MDXSearchTool, FileReadTool
from typing import List
from dotenv import load_dotenv

import os

load_dotenv()
# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators
read_resume = FileReadTool(file_path='./fake_resume.md')
semantic_search_resume = MDXSearchTool(mdx='./fake_resume.md')

@CrewBase
class CoverLetterAndResume():
    """CoverLetterAndResume crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    
    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools

    # ollama_llm = LLM(
    #     model='ollama/llama3.1',
    #     base_url='http://localhost:11434',
    # )



    @agent
    def cv_creator(self) -> Agent:
        return Agent(
            config=self.agents_config['cv_creator'], # type: ignore[index]
            tools=[read_resume, semantic_search_resume],
            verbose=True
        )

    @agent
    def cover_letter_creator(self) -> Agent:
        return Agent(
            config=self.agents_config['cover_lettter_creator'], # type: ignore[index]
            tools = [read_resume, semantic_search_resume],
            verbose=True
        )
    
    @agent
    def ats_checker(self) -> Agent:
        return Agent(
            config=self.agents_config['ats_checker'], # type: ignore[index]
            tools = [read_resume, semantic_search_resume],
            verbose=True,
            respect_context_window=True, # Ensures the agent respects the context window
            allow_delegation=True, # Allows the agent to delegate tasks to other agents
        )

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def cv_task(self) -> Task:
        return Task(
            config=self.tasks_config['cv_task'], # type: ignore[index]
        )
    

    @task
    def cover_letter_task(self) -> Task:
        return Task(
            config=self.tasks_config['cover_letter_task'], # type: ignore[index]
        )
    

    @task
    def ats_checker_task(self) -> Task:
        return Task(
            config=self.tasks_config['ats_checker_task'], # type: ignore[index]
            output_file='report.md',
        )

    @crew
    def crew(self) -> Crew:
        """Creates the CoverLetterAndResume crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
