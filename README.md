# Multi-Agent Debate System

## Project Title & Description
A multi-agent system that simulates structured debates between AI agents on user-defined topics. It generates persuasive arguments, rebuttals, and a judged verdict, providing insights into different perspectives.

## Features
- **Structured Debates**: 3-round debates with opening arguments, rebuttals, and closings
- **Multi-Perspective**: Supports pro/con, AI vs human, and other debate formats
- **Judging System**: Impartial AI judge evaluates arguments and declares a winner
- **Terminal UI**: Rich, interactive debate interface (optional)
- **Customizable**: Easily modify agent roles, debate structure, and LLM parameters

## Tech Stack
- **Python**
- **CrewAI**: Agent and task management framework
- **Groq**: LLM provider (Llama 3 models)
- **Rich** (optional): Terminal UI library
- **dotenv**: Environment variable management

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/aliii-codes/Multi-Agent-Debate-System.git
   cd Multi-Agent-Debate-System
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Obtain a Groq API key and create a `.env` file:
   ```
   GROQ_API_KEY=your_api_key_here
   ```

## Usage
1. Run a basic debate:
   ```bash
   python full_debate.py
   ```
2. For a terminal UI experience:
   ```bash
   python terminal_ui_by_claude.py
   ```
3. Enter your debate topic when prompted.

Example output:
```
DEBATE STARTING...

ROUND 1 - Pro: [arguments]
ROUND 1 - Anti: [arguments]
...
FINAL VERDICT:
[judge's decision and scores]
```

## Project Structure
```
Multi-Agent-Debate-System/
├── basic_architecture.py      # Core debate logic
├── full_debate.py             # Complete debate implementation
├── terminal_ui_by_claude.py   # Terminal UI version
├── LICENSE
```

## License
This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
