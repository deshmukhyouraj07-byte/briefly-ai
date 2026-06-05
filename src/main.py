from src.data_layer import EnterpriseIQMock
from src.reasoning import BriefingAgent

def run_agent_pipeline():
    print("🚀 STEP 1: Booting BrieflyAI Intelligent Agent Dashboard Processing Engine...")
    print("📥 STEP 2: Connecting to Enterprise Data Layers (Mock Work & Foundry IQ)...")
    
    communications = EnterpriseIQMock.get_unresolved_communications()
    compliance_rules = EnterpriseIQMock.get_compliance_policy()
    
    print("🧠 STEP 3: Executing multi-step policy checks & decision evaluation matrix...")
    agent = BriefingAgent()
    final_brief = agent.analyze_and_route(communications, compliance_rules)
    
    print("\n================🎯 FINAL ACTIONABLE EXECUTIVE INTELLIGENCE BRIEF ================\n")
    print(final_brief)
    print("\n================================================================================")
    print("✅ Run Complete. Ready for supervisor sign-off.")

if __name__ == "__main__":
    run_agent_pipeline()
 
