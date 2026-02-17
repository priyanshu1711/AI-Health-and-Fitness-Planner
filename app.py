import streamlit as st
from utils.helper import display_dietary_plan, display_fitness_plan, show_loading_quotes
from graph_builder import build_graph
from agents.qa import qa_node

compiled_graph = build_graph()

st.set_page_config(
    page_title="AI Health & Fitness Planner",
    page_icon="🏋️‍♂️",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("🏋️‍♂️ AI Health & Fitness Planner")

# Sidebar: API Key
with st.sidebar:
    st.header("🔑 API Configuration")
    gemini_api_key = st.text_input("Gemini API Key", type="password")
    if not gemini_api_key:
        st.warning("⚠️ Please enter your Gemini API Key to proceed")
        st.markdown("[Get your API key here](https://aistudio.google.com/apikey)")
        st.stop()
    st.success("API Key accepted!")

# User Inputs
col1, col2 = st.columns(2)
with col1:
    age = st.number_input("Age", min_value=10, max_value=100, value=25, step=1)
    height = st.number_input("Height (cm)", min_value=100.0, max_value=250.0, value=170.0, step=0.1)
    activity_level = st.selectbox("Activity Level", ["Sedentary","Lightly Active","Moderately Active","Very Active","Extremely Active"])
    dietary_preferences = st.selectbox("Dietary Preferences", ["Vegetarian","Keto","Gluten Free","Low Carb","Dairy Free","Non Vegetarian"])

with col2:
    weight = st.number_input("Weight (kg)", min_value=20.0, max_value=300.0, value=70.0, step=0.1)
    sex = st.selectbox("Sex", ["Male", "Female", "Other"])
    fitness_goals = st.selectbox("Fitness Goals", ["Lose Weight","Gain Muscle","Endurance","Stay Fit","Strength Training"])

# Generate Personalized Plan
if st.button("🎯 Generate My Personalized Plan", use_container_width=True):
    user_profile = f"""
    Age: {age}
    Weight: {weight}kg
    Height: {height}cm
    Sex: {sex}
    Activity Level: {activity_level}
    Dietary Preferences: {dietary_preferences}
    Fitness Goals: {fitness_goals}
    """

    with st.spinner("Generating your personalized plan..."):
        show_loading_quotes()
        initial_state = {"user_profile": user_profile, "api_key": gemini_api_key}
        output = compiled_graph.invoke(initial_state)
        print(output.keys())

    st.session_state["dietary_plan"] = output.get("dietary_plan", {})
    st.session_state["fitness_plan"] = output.get("fitness_plan", {})

    display_dietary_plan(st.session_state["dietary_plan"])
    display_fitness_plan(st.session_state["fitness_plan"])
    

# Q&A Section
if "dietary_plan" in st.session_state and "fitness_plan" in st.session_state:
    st.header("❓ Ask a Question About Your Plan")
    question = st.text_input("Type your question here...")

    if st.button("💡 Get Answer"):
        qa_state = {
            "query": question,
            "dietary_plan": st.session_state["dietary_plan"],
            "fitness_plan": st.session_state["fitness_plan"],
            "api_key": gemini_api_key,
        }
        qa_output = qa_node(qa_state)
        st.success(f"**Answer:** {qa_output['answer']}")
