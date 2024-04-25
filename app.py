from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

LANGCHAIN_API_KEY = os.getenv("LANGCHAIN_API_KEY")

## Prompt Template

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a advance assistant with powerfull resources. Please response to the user queries"),
        ("user","Question:{question}")
    ]
)

# streamlit framework

st.title('🦜🔗Langchain with Llama3')
input_text=st.text_input("Search the topic you want")
submit=st.button("Search🔍")
# ollama LLAma3 LLm 
llm=Ollama(model="llama3")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))
