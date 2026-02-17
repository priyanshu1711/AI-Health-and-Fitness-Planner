# Q&A agent node
from utils.helper import invoke_llm

def qa_node(state: dict):
    context = f"Dietary Plan: {state['dietary_plan'].get('meal_plan', '')}\n\nFitness Plan: {state['fitness_plan'].get('routine', '')}"
    prompt = f"""
    You are a helpful assistant. Use the following context to answer the user question.

    Context:
    {context}

    Question: {state['query']}
    """
    return {"answer": invoke_llm(prompt, state["api_key"])}
