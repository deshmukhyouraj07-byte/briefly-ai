from langchain_core.prompts import ChatPromptTemplate
from src.config import Config

class BriefingAgent:
    def __init__(self):
        self.llm = Config.LLM

    def analyze_and_route(self, items: list, policy: str) -> str:
        prompt = ChatPromptTemplate.from_messages([
            ("system", (
                "You are an Elite Executive Delegate Agent specialized in information triage.\n"
                "Active Company Policy Rules:\n{policy_rules}\n\n"
                "Instructions:\n"
                "1. Isolate actionable notifications from noise.\n"
                "2. Evaluate urgency for each message (High, Medium, Low).\n"
                "3. Cross-reference the communication against corporate compliance. Explicitly flag violations.\n"
                "4. Draft a pristine, professional response on behalf of the Executive for review."
            )),
            ("human", "Process the following raw enterprise inputs:\n{communications}")
        ])
        
        chain = prompt | self.llm
        formatted_items = "\n---\n".join([f"Source: {i['source']} | Sender: {i['sender']}\nRaw Text: {i['content']}" for i in items])
        response = chain.invoke({"policy_rules": policy, "communications": formatted_items})
        return response.content
 
