from crewai import Agent, Task, Crew, Process, LLM
from dotenv import load_dotenv
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.rule import Rule
from rich.prompt import Prompt
from rich.live import Live
from rich.spinner import Spinner
from rich.table import Table
import os
import time

load_dotenv()

console = Console()

groq_llm = LLM(
    model="groq/llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY"),
    max_tokens=500,
    temperature=0.7
)

# --- INTRO ---
console.print()
console.print(Panel.fit(
    "[bold yellow]⚔️  DEBATE ARENA[/bold yellow]\n[dim]Powered by CrewAI + Groq[/dim]",
    border_style="yellow"
))
console.print()

topic = Prompt.ask("[bold cyan]Enter your debate topic[/bold cyan]")
console.print()

# --- AGENTS ---
pro_agent = Agent(
    role="Pro Debater",
    goal=f"WIN the debate by arguing STRONGLY in favor of: {topic}",
    backstory="You are an aggressive, ruthless debater who argues FOR the topic. You use sharp facts, statistics, and logic. You NEVER agree with the opposition. You ATTACK their arguments mercilessly.",
    llm=groq_llm,
    verbose=False
)

anti_agent = Agent(
    role="Anti Debater",
    goal=f"WIN the debate by arguing STRONGLY AGAINST: {topic}",
    backstory="You are a fierce, ruthless debater who argues AGAINST the topic. You highlight dangers, failures, and flaws. You NEVER praise the other side. You ATTACK their arguments mercilessly.",
    llm=groq_llm,
    verbose=False
)

judge_agent = Agent(
    role="Debate Judge",
    goal="Fairly evaluate both sides and declare a winner",
    backstory="You are a ruthless, impartial debate judge with decades of experience. You score based on logic, evidence, and attack strength. You ALWAYS declare one clear winner with no ties.",
    llm=groq_llm,
    verbose=False
)

# --- TASKS ---
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

tasks = [pro_round1, anti_round1, pro_round2, anti_round2, pro_round3, anti_round3, judge_task]

# --- DISPLAY HELPERS ---
def show_round_header(round_num, title):
    console.print()
    console.print(Rule(f"[bold white] ROUND {round_num} — {title} [/bold white]", style="bright_blue"))
    console.print()

def show_argument(side, color, icon, content):
    console.print(Panel(
        content,
        title=f"{icon} [bold {color}]{side}[/bold {color}]",
        border_style=color,
        padding=(1, 2)
    ))
    console.print()

def show_spinner(message):
    with console.status(f"[dim]{message}[/dim]", spinner="dots"):
        pass

# --- RUN CREW WITH RICH OUTPUT ---
round_labels = [
    (1, "OPENING ARGUMENTS", "pro"),
    (1, "OPENING ARGUMENTS", "anti"),
    (2, "REBUTTALS", "pro"),
    (2, "REBUTTALS", "anti"),
    (3, "CLOSING ARGUMENTS", "pro"),
    (3, "CLOSING ARGUMENTS", "anti"),
]

console.print(Rule("[bold yellow]⚔️  DEBATE STARTING[/bold yellow]", style="yellow"))
console.print()

results = []

for i, task in enumerate(tasks[:-1]):  # all except judge
    label = round_labels[i]
    round_num, round_title, side = label

    if side == "pro":
        show_round_header(round_num, round_title)

    spinner_msg = f"{'Pro' if side == 'pro' else 'Anti'} debater is thinking..."
    with console.status(f"[dim]{spinner_msg}[/dim]", spinner="dots"):
        crew = Crew(
            agents=[pro_agent, anti_agent, judge_agent],
            tasks=[task],
            process=Process.sequential,
            verbose=False
        )
        result = crew.kickoff()
        time.sleep(8)

    results.append(str(result))

    if side == "pro":
        show_argument("PRO SIDE", "green", "✅", str(result))
    else:
        show_argument("ANTI SIDE", "red", "❌", str(result))

# --- JUDGE ---
console.print()
console.print(Rule("[bold magenta]⚖️  JUDGE'S VERDICT[/bold magenta]", style="magenta"))
console.print()

with console.status("[dim]Judge is deliberating...[/dim]", spinner="dots"):
    judge_task.context = [pro_round1, anti_round1, pro_round2, anti_round2, pro_round3, anti_round3]
    judge_crew = Crew(
        agents=[judge_agent],
        tasks=[judge_task],
        process=Process.sequential,
        verbose=False
    )
    verdict = judge_crew.kickoff()

console.print(Panel(
    str(verdict),
    title="[bold magenta]⚖️  FINAL VERDICT[/bold magenta]",
    border_style="magenta",
    padding=(1, 2)
))

console.print()
console.print(Rule("[dim]Debate Complete[/dim]", style="dim"))
console.print()