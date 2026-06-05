 import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

class Config:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    LLM = ChatOpenAI(
        model="gpt-4o-mini", 
        temperature=0.1, 
        api_key=OPENAI_API_KEY
    )

