from utils.helper import invoke_llm

def fitness_node(state: dict):
    prompt = f"""
    You are a fitness expert. Based on the following user profile, create a personalized fitness plan.
    Profile:
    {state['user_profile']}
    """
    return {
        "fitness_plan": {
            "goals": "Build strength, improve endurance, and maintain overall fitness",
            "routine": invoke_llm(prompt, state["api_key"]),
            "tips": """
            - Track your progress regularly
            - Allow proper rest between workouts
            - Focus on proper form
            - Stay consistent with your routine
            """
        },
        "user_profile": state["user_profile"],
        "api_key": state["api_key"]
    }
