from crewai import Agent , Task, Crew , Process, LLM
from crewai_tools import ScrapeWebsiteTool
from dotenv import load_dotenv
import os


load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_MODEL = "groq/llama3-8b-8192"

groq_llm = LLM(
    model=GROQ_MODEL,
    api_key=GROQ_API_KEY
)

topic = str(input("Enter your topic of debate: "))


# Against Humans !
researcher = Agent(
    role="AI Research Specialist",
    goal=f"Research and gather comprehensive, factual evidence about {topic}",
    backstory="Meticulous research specialist with expertise in AI trends...",
    tools=[ScrapeWebsiteTool()],
    llm=groq_llm,
    verbose=True
)

pro_ai_advocate = Agent(
    role="Pro AI Advocate",
    goal=f"Argue this topic '{topic}' using research evidence",
    tools=[ScrapeWebsiteTool()],
    llm=groq_llm,
    verbose=True
)

research_task = Task(
    description=f"Conduct a comprehensive research about the topic '{topic}'",
    expected_output=f"a Comprehensive reseach report ",
    agent=researcher
)

pro_AI_opening = Task(
    description=f"Present strongest opening argument for '{topic}'",
    expected_output="A persuasive 3-4 paragraph opening argument...",
    agent=pro_ai_advocate,
    context=[research_task]   
)


# For Humans
h_researcher = Agent(
    role="Human Perspective Research Specialist",  # or "Human Advocate Researcher"
    goal=f"Research and gather comprehensive, factual evidence supporting human-centric perspectives on {topic}",
    backstory="Expert researcher specializing in human values, ethical considerations, and societal impacts of technology. Focuses on gathering evidence that represents human interests, concerns, and benefits.",
    tools=[ScrapeWebsiteTool()],
    llm=groq_llm,
    verbose=True
)


human_advocate = Agent(
    role="Human Advocate",
    goal=f"Argue for human-centric perspectives on '{topic}' using research evidence",
    backstory="Seasoned debater who champions human values, ethical considerations, and the importance of maintaining human agency in technological decisions. Uses research and logical arguments to present the human side effectively.",
    tools=[ScrapeWebsiteTool()],
    llm=groq_llm,
    verbose=True
)


human_research_task = Task(
    description=f"Conduct comprehensive research about '{topic}' from a human-centric perspective, focusing on ethical concerns, societal impacts, and human benefits/risks",
    expected_output="A comprehensive research report highlighting human perspectives",
    agent=h_researcher
)

human_opening = Task(
    description=f"Present strongest opening argument for human perspective on '{topic}'",
    expected_output="A persuasive 3-4 paragraph opening argument representing human interests",
    agent=human_advocate,
    context=[human_research_task]
)


debate_crew = Crew(
    agents=[researcher, pro_ai_advocate, h_researcher, human_advocate],
    tasks=[research_task, pro_AI_opening, human_research_task, human_opening],
    process=Process.sequential,  # or Process.hierarchical 
    verbose=True
)

print("DEBATE RESULTS: ")
result = debate_crew.kickoff()
print(result)