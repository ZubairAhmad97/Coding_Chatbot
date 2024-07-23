# from langchain_openai import ChatOpenAI

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st
import os


# Define the prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to the user queries."),
        ("user", "Question: {question}")
    ]
)

# Set up Streamlit framework
st.title('Langchain Demo with DeepSeek-Coder API')
input_text = st.text_input("Search the topic you want")

# Initialize Ollama DeepSeek-Coder LLM
llm = Ollama(model="deepseek-coder:1.3b") 
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

# Process user input and display the result
if input_text:
    response = chain.invoke({"question": input_text})
    st.write(response)


