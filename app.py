from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st
import os

load_dotenv()

google_api_key = os.getenv("GOOGLE_API_KEY")

def get_gemini_ai_response(question):
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.6)
    response = llm.invoke(question)

    return response.content if hasattr(response, "content") else str(response)

st.set_page_config(page_title="Q & A Demo")
st.header("LangChain + Gemini AI App")

question = st.text_input("Enter your question :")

if st.button("Ask the Question"):
    response = get_gemini_ai_response(question)
    st.subheader("The response is:")
    st.write(response)
