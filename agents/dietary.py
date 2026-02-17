from utils.helper import invoke_llm

def dietary_node(state: dict):
    prompt = f"""
    You are a dietary expert. Based on the following user profile, create a personalized dietary plan.
    Profile:
    {state['user_profile']}
    """
    return {
        "dietary_plan": {
            "why_this_plan_works": "High Protein, Healthy Fats, Moderate Carbohydrates, and Caloric Balance",
            "meal_plan": invoke_llm(prompt, state["api_key"]),
            "important_considerations": """
            - Hydration: Drink plenty of water throughout the day
            - Electrolytes: Monitor sodium, potassium, and magnesium levels
            - Fiber: Ensure adequate intake through vegetables and fruits
            - Listen to your body: Adjust portion sizes as needed
            """
        },
        "user_profile": state["user_profile"],  # keep for downstream nodes
        "api_key": state["api_key"]             # keep for downstream nodes
    }
