from langchain_community import ChatOpenAI
from langchain_community import ChartPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama

import streamlit as st

import os
from dotenv import load_dotenv

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["OLLAMA_API_KEY"] = os.getenv("OLLAMA_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"

# Prompt Template
prompt=ChartPromptTemplate.from_messages(
      ["system", "You are a helpful assistant that provides information about the LangChain framework."],
      ["user", "What is LangChain?"],
      ["assistant", "LangChain is a framework for developing applications powered by language models."],
      ["user", "What are its main components?"]
)

# streamlit app

st.title("LangChain Framework Information")
input_text = st.text_input("Ask a question about what u want")

# openAI LLM

llm=Ollama(model="llama2")
output_parser=StrOutputParser()
chain=prompt | llm | output_parser

if input_text:
      st.write(chain.invoke({"question": input_text}))