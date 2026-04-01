from crewai import Agent, Task, Crew, Process, LLM
from dotenv import load_dotenv
import os
import time

load_dotenv()

groq_llm = LLM(
    model="groq/llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY"),
    max_tokens=500,
    temperature=0.7
)

topic = str(input("Enter your topic of debate: "))


pro_agent = Agent(
    role="Pro Debater",
    goal=f"Do every thing to WIN the debate by arguing STRONGLY in favor of: {topic}",
    backstory="You are an aggressive, ruthless debater who argues FOR the topic. You use sharp facts, statistics, and logic. You NEVER agree with the opposition. You ATTACK their arguments mercilessly.",
    llm=groq_llm,
    verbose=True
)

anti_agent = Agent(
    role="Anti Debater",
    goal=f"WIN the debate by arguing STRONGLY AGAINST: {topic}",
    backstory="You are a fierce, ruthless debater who argues AGAINST the topic. You highlight dangers, failures, and flaws. You NEVER praise the other side. You ATTACK their arguments mercilessly.",
    llm=groq_llm,
    verbose=True
)

judge_agent = Agent(
    role="Debate Judge",
    goal="Fairly evaluate both sides and declare a winner",
    backstory="You are a ruthless, impartial debate judge with decades of experience. You score based on logic, evidence, and attack strength. You ALWAYS declare one clear winner with no ties.",
    llm=groq_llm,
    verbose=True
)


pro_round1 = Task(
    description=f"ROUND 1 - Opening argument IN FAVOR of '{topic}'. Be aggressive, use statistics, attack the opposition's likely arguments. 3 paragraphs max.",
    expected_output="3 sharp paragraphs arguing FOR the topic.",
    agent=pro_agent
)

anti_round1 = Task(
    description=f"ROUND 1 - Opening argument AGAINST '{topic}'. Attack the pro side. Highlight dangers and failures. 3 paragraphs max.",
    expected_output="3 sharp paragraphs arguing AGAINST the topic.",
    agent=anti_agent,
    context=[pro_round1]
)


pro_round2 = Task(
    description=f"ROUND 2 - Rebuttal. Destroy the anti side's Round 1 argument point by point. Be ruthless. 3 paragraphs max.",
    expected_output="3 aggressive rebuttal paragraphs tearing apart the opposition.",
    agent=pro_agent,
    context=[anti_round1]
)

anti_round2 = Task(
    description=f"ROUND 2 - Rebuttal. Destroy the pro side's Round 1 AND Round 2 arguments. Be ruthless. 3 paragraphs max.",
    expected_output="3 aggressive rebuttal paragraphs tearing apart the opposition.",
    agent=anti_agent,
    context=[pro_round1, pro_round2]
)


pro_round3 = Task(
    description=f"ROUND 3 - Closing argument. Summarize your strongest points and land the final blow. 2 paragraphs max.",
    expected_output="2 powerful closing paragraphs for the pro side.",
    agent=pro_agent,
    context=[pro_round1, pro_round2, anti_round2]
)

anti_round3 = Task(
    description=f"ROUND 3 - Closing argument. Summarize your strongest points and land the final blow. 2 paragraphs max.",
    expected_output="2 powerful closing paragraphs for the anti side.",
    agent=anti_agent,
    context=[anti_round1, anti_round2, pro_round3]
)


judge_task = Task(
    description=f"""You witnessed a 3-round debate on '{topic}'.
Review all 6 arguments from both sides and score each debater on:
- Logic (0-10)
- Evidence (0-10)  
- Attack Strength (0-10)
Add up the scores and declare ONE clear winner. No ties allowed.""",
    expected_output="Scores for both sides, total scores, verdict, and a clear winner declaration.",
    agent=judge_agent,
    context=[pro_round1, anti_round1, pro_round2, anti_round2, pro_round3, anti_round3]
)


def task_delay(task):
    time.sleep(8)

crew = Crew(
    agents=[pro_agent, anti_agent, judge_agent],
    tasks=[pro_round1, anti_round1, pro_round2, anti_round2, pro_round3, anti_round3, judge_task],
    process=Process.sequential,
    verbose=True,
    task_callback=task_delay
)

print("\nDEBATE STARTING...\n")
result = crew.kickoff()
print("\nFINAL VERDICT:\n")
print(result)