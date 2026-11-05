import time
from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from langchain_ollama import ChatOllama


# 1. Define shared state
class State(TypedDict):
    user_request: str
    next_agent: str
    research: str
    analysis: str
    final_report: str
    review: str
    revised_report: str

# 2. Connect the local AI model
llm = ChatOllama(
    model="llama3.2",
    temperature=0,
    num_predict=350,
    keep_alive="30m"
)
def timed_invoke(agent_name: str, prompt: str):
    start_time = time.perf_counter()

    try:
        response = llm.invoke(prompt)
        elapsed = time.perf_counter() - start_time

        print(f"[TIMING] {agent_name}: {elapsed:.2f} seconds")
        return response

    except Exception:
        elapsed = time.perf_counter() - start_time
        print(f"[TIMING] {agent_name} failed after {elapsed:.2f} seconds")
        raise

# 3. Supervisor Agent
# 3. Supervisor Agent
def supervisor_agent(state: State):

    print("\nSupervisor coordinating workflow...")

    # The workflow is already predefined.
    # No LLM call is required for routing.

    print("Supervisor plan: Research -> Analysis -> Writing")

    return {"next_agent": "researcher"}

# 4. Route from Supervisor
def route_from_supervisor(state: State):
    return state["next_agent"]


# 5. Research Agent
def research_agent(state: State):
    print("\nResearch Agent working...")

    response = timed_invoke(
        "Researcher",
        f"""Give 3 concise,important facts about:
{state['user_request']}

Use simple language and relevant examples.
"""
    )

    return {"research": response.content}


# 6. Analyst Agent
def analyst_agent(state: State):
    print("\nAnalyst Agent working...")

    response = timed_invoke(
        "Analyst",
        f"""Give 3 concise insights about:
{state['user_request']}

Use this research:
{state['research']}
"""
    )

    return {"analysis": response.content}

# 7. Writer Agent
def writer_agent(state: State):
    print("\nWriter Agent working...")

    response = timed_invoke(
        "Writer",
        f"""Write a short final report about:
{state['user_request']}

Research:
{state['research']}

Analysis:
{state['analysis']}

Include key findings and a brief conclusion.
"""
    )

    return {"final_report": response.content}
# 8. Reviewer Agent
def reviewer_agent(state: State):
    print("\nReviewer Agent working...")

    prompt = f"""
You are a careful report reviewer.

Review the report for:
1. Clarity
2. Relevance to the user's request
3. Missing important information
4. Unsupported claims

User request:
{state['user_request']}

Research:
{state['research']}

Analysis:
{state['analysis']}

Draft report:
{state['final_report']}

Give concise, actionable feedback.
Do not invent facts.
"""

    response = timed_invoke("Reviewer", prompt)

    return {"review": response.content}
# Writer Revision Agent
def revision_agent(state: State):
    print("\nWriter Revision Agent working...")

    prompt = f"""
You are an expert report editor.

Improve the original report using the reviewer's feedback.

User request:
{state['user_request']}

Research:
{state['research']}

Analysis:
{state['analysis']}

Original report:
{state['final_report']}

Reviewer's feedback:
{state['review']}

Instructions:
- Address the reviewer's useful suggestions.
- Keep the report relevant to the user's request.
- Correct unclear explanations.
- Do not invent facts or statistics.
- Preserve useful information from the original report.
- Return only the complete improved report.
"""

    response = timed_invoke("Writer Revision", prompt)

    return {"revised_report": response.content}
# 8. Build the LangGraph workflow
graph_builder = StateGraph(State)

graph_builder.add_node("supervisor", supervisor_agent)
graph_builder.add_node("researcher", research_agent)
graph_builder.add_node("analyst", analyst_agent)
graph_builder.add_node("writer", writer_agent)
graph_builder.add_node("reviewer", reviewer_agent)
graph_builder.add_node("revision", revision_agent)
graph_builder.add_edge(START, "supervisor")

# Supervisor selects the starting agent
graph_builder.add_conditional_edges(
    "supervisor",
    route_from_supervisor,
    {
        "researcher": "researcher",
        "analyst": "analyst",
        "writer": "writer"
    }
)

# Ensure missing information is generated before writing
graph_builder.add_edge("researcher", "analyst")
graph_builder.add_edge("analyst", "writer")
graph_builder.add_edge("writer", "reviewer")
graph_builder.add_edge("reviewer", "revision")
graph_builder.add_edge("revision", END)

graph = graph_builder.compile()

# 9. Get a request from the user
if __name__ == "__main__":

    user_request = input("\nEnter your task: ").strip()

    if not user_request:
        print("Please enter a valid task.")

    else:
        result = graph.invoke({
            "user_request": user_request,
            "next_agent": "",
            "research": "",
            "analysis": "",
            "final_report": "",
            "review": "",
            "revised_report": ""
        })

        print("\n========== FINAL REPORT ==========\n")
        print(result["final_report"])
        print("\n========== REVIEW FEEDBACK ==========\n")
        print(result["review"])
        print("\n========== IMPROVED FINAL REPORT ==========\n")
        print(result["revised_report"])