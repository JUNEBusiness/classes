#!/usr/bin/env python
import sys
import warnings

from datetime import datetime
from cover_letter_and_resume.crew import CoverLetterAndResume
from typing import Union
from fastapi import FastAPI

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/create/{name}")
def create(name: str):
    """
    Run the crew.
    """
    inputs = {
        "candidate_name": name,
    "company_name": "JUNEBusiness",
    "location": "London, UK",
    "job_role": "Data Analyst",
    "job_type": "Hybrid",
    "job_description": '''
                    As a Data Analyst, you will play a key role in transforming data into insights that drive strategic business decisions. You will work closely with product, marketing, and development teams to gather, analyze, and interpret data that supports the company’s ongoing growth and operational efficiency.
                    Key Responsibilities

                    Collect, process, and clean data from various sources to ensure data accuracy and reliability.
                    Perform deep-dive analysis to identify trends, patterns, and actionable insights.
                    Develop dashboards and reports that communicate findings to internal stakeholders.
                    Support product and business teams with ad-hoc analysis and data-driven recommendations.
                    Collaborate with cross-functional teams to define and monitor key performance indicators (KPIs).
                    Maintain data integrity and security while optimizing workflows and automation processes.
                    Contribute to data strategy and governance initiatives to improve overall data maturity.
                    Requirements

                    Proven experience as a Data Analyst, Business Analyst, or similar role in a tech-driven environment.
                    Proficiency in SQL and data visualization tools (e.g., Power BI, Tableau, Looker).
                    Strong analytical skills with the ability to translate complex data into clear insights.
                    Experience with Python, R, or other statistical tools is a plus.
                    Familiarity with cloud-based data platforms (e.g., AWS, Google BigQuery, Snowflake).
                    Excellent problem-solving abilities and attention to detail.
                    Strong communication skills, both written and verbal.
                    Bachelor's degree in Data Science, Statistics, Computer Science, or a related field.'''
    }
    
    try:
        results = CoverLetterAndResume().crew().kickoff(inputs=inputs)
        return results
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")
    
# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information
