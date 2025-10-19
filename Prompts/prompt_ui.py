from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv 
import streamlit as st

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1-Distill-Qwen-32B",
    task="text-generation",
)

model = ChatHuggingFace(llm=llm)

st.header("Research Tool")

user_input = st.text_input("Enter your prompt")

if st.button("Generate Response"):
    if not user_input.strip():
        st.warning("Please enter a prompt before generating.")
    else:
        with st.spinner("Generating response..."):
            result = model.invoke(user_input)
        st.write(result.content)
