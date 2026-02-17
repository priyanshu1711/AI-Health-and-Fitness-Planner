from langgraph.graph import StateGraph, END
from agents.dietary import dietary_node
from agents.fitness import fitness_node
from agents.qa import qa_node
from typing import TypedDict, Dict

# Define state for LangGraph
class PlanState(TypedDict, total=False):
    user_profile: str
    dietary_plan: Dict
    fitness_plan: Dict
    query: str
    answer: str
    api_key: str

# Build LangGraph workflow
def build_graph():
    graph = StateGraph(PlanState)
    graph.add_node("dietary", dietary_node)
    graph.add_node("fitness", fitness_node)
    graph.add_node("qa", qa_node)

    graph.set_entry_point("dietary")
    graph.add_edge("dietary", "fitness")
    graph.add_edge("fitness", END)
    return graph.compile()
