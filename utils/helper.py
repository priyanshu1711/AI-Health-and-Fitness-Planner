import streamlit as st
import random
import time
from langchain_google_genai import ChatGoogleGenerativeAI
from config import QUOTES, LLM_MODEL

def invoke_llm(prompt: str, api_key: str) -> str:
    llm = ChatGoogleGenerativeAI(model=LLM_MODEL, api_key=api_key)
    response = llm.invoke(prompt)
    return response.content

def show_loading_quotes():
    quotes_to_show = random.sample(QUOTES, k=min(30, len(QUOTES)))
    for q in quotes_to_show:
        st.info(q)
        time.sleep(1.5)

def display_dietary_plan(plan: dict):
    st.subheader("📋 Dietary Plan")
    with st.expander("🎯 Why this plan works", expanded=False):
        st.info(plan.get("why_this_plan_works", "No explanation provided"))
    with st.expander("🍽️ Meal Plan", expanded=False):
        st.markdown(plan.get("meal_plan", "No meal plan available"))
    with st.expander("⚠️ Important Considerations", expanded=False):
        for item in plan.get("important_considerations", "").split("\n"):
            if item.strip():
                st.warning(item.strip())

def display_fitness_plan(plan: dict):
    st.subheader("💪 Fitness Plan")
    with st.expander("🎯 Goals", expanded=False):
        st.success(plan.get("goals", "No goals provided"))
    with st.expander("🏋️ Exercise Routine", expanded=False):
        st.markdown(plan.get("routine", "No routine available"))
    with st.expander("💡 Pro Tips", expanded=False):
        for tip in plan.get("tips", "").split("\n"):
            if tip.strip():
                st.info(tip.strip())
