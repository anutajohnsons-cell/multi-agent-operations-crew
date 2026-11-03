# Multi-Agent Operations Crew

## Project Overview

Multi-Agent Operations Crew is an AI-powered application that uses multiple specialized AI agents to process user requests and generate structured reports.

Built using Python, LangGraph, Ollama, Llama 3.2, and Streamlit, the application coordinates a team of agents to research a topic, analyze the information, and prepare a final report.

## Objectives

- Automate research and report generation.
- Divide tasks among specialized AI agents.
- Coordinate agent execution using LangGraph.
- Provide a simple web interface for users.
- Run a language model locally using Ollama.

## Technologies Used

- Python
- LangGraph
- LangChain Ollama
- Ollama
- Llama 3.2
- Streamlit

## System Architecture

1. **User Interface:** Accepts a topic through Streamlit.
2. **Supervisor Agent:** Plans the team's focus and selects the research stage as the starting point.
3. **Research Agent:** Generates key facts about the topic.
4. **Analyst Agent:** Produces insights using the research.
5. **Writer Agent:** Combines the research and analysis into a final report.

## Workflow

User Input
    |
    v
Supervisor Agent
    |
    v
Research Agent
    |
    v
Analyst Agent
    |
    v
Writer Agent
    |
    v
Final Report

## Features

- Multi-agent task processing
- Local LLM integration
- Automated research and analysis
- Structured report generation
- Execution-time logging for agent calls
- Streamlit web interface
- Basic error handling in the interface

## Project Structure

multi-agent-operations-crew/
├── app.py
├── main.py
├── requirements.txt
├── .env
└── README.md

## Installation and Setup

### 1. Install Python

Install a compatible Python version.

### 2. Install Ollama

Install Ollama and download the Llama 3.2 model:

    ollama pull llama3.2

Ensure the Ollama service is running before launching the application.

### 3. Create a virtual environment

    python -m venv venv

Activate it in Windows PowerShell:

    .\venv\Scripts\Activate.ps1

### 4. Install dependencies

    pip install -r requirements.txt

### 5. Run the application

Launch the Streamlit interface:

    python -m streamlit run app.py

Alternatively, run the command-line version:

    python main.py

## Example Input

How can AI help students learn programming?

## Expected Output

- Research findings
- Analysis and insights
- A structured final report

## Current Limitations

- Report quality depends on the local language model.
- Model response times depend on available hardware.
- Generated information should be verified before practical use.
- The application requires a working local Ollama service.

## Future Improvements

- Improve task planning and workflow routing.
- Add report export to PDF.
- Add conversation history.
- Improve error handling and logging.
- Add automated workflow tests.

## Author

Developed as a personal AI engineering project.