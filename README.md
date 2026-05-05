# Multi-Agent Debate System 🗣️

**Simulate structured debates between AI agents on any topic, generating persuasive arguments, rebuttals, and judged verdicts.**

[![GitHub stars](https://img.shields.io/github/stars/aliii-codes/Multi-Agent-Debate-System?style=for-the-badge)](https://github.com/aliii-codes/Multi-Agent-Debate-System/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/aliii-codes/Multi-Agent-Debate-System?style=for-the-badge)](https://github.com/aliii-codes/Multi-Agent-Debate-System/network)
[![GitHub issues](https://img.shields.io/github/issues/aliii-codes/Multi-Agent-Debate-System?style=for-the-badge)](https://github.com/aliii-codes/Multi-Agent-Debate-System/issues)
[![License](https://img.shields.io/github/license/aliii-codes/Multi-Agent-Debate-System?style=for-the-badge)](LICENSE)

[![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![CrewAI](https://img.shields.io/badge/CrewAI-latest-orange?style=for-the-badge&logo=github)](https://github.com/joaomdmoura/crewAI)
[![Groq](https://img.shields.io/badge/Groq-Llama%203-brightgreen?style=for-the-badge&logo=groq)](https://groq.com/)
[![Rich](https://img.shields.io/badge/Rich-terminal%20UI-purple?style=for-the-badge&logo=terminal)](https://rich.readthedocs.io/)

---

🚀 **New in v1.1:**
- **Enhanced Terminal UI** 🎨: Richer debate visualization with live updates
- **Improved Argument Structure** 💬: Sharper rebuttals and closing arguments
- **Faster Response Times** ⚡: Optimized LLM parameters for quicker debates

---

| Feature | Description |
|---------|-------------|
| **Structured Debates** 🏛️ | 3-round debates with opening, rebuttals, and closing arguments |
| **Multi-Perspective** 🌐 | Supports pro/con, AI vs human, and custom debate formats |
| **AI Judging** ⚖️ | Impartial evaluation with logic/evidence/attack scoring |
| **Terminal UI** 🎮 | Interactive debate visualization (optional) |
| **Customizable** 🛠️ | Easily modify agents, structure, and LLM parameters |

---

| Category | Technologies |
|----------|----------------|
| **Core Framework** | Python, CrewAI |
| **LLM Provider** | Groq (Llama 3 models) |
| **UI (optional)** | Rich |
| **Environment** | dotenv |

---

**Get started in 3 steps:**

1. **Clone & Install**
   ```bash
   git clone https://github.com/aliii-codes/Multi-Agent-Debate-System.git
   cd Multi-Agent-Debate-System
   pip install -r requirements.txt
   ```

2. **Set Environment Variables**
   Create a `.env` file:
   ```
   GROQ_API_KEY=your_groq_api_key
   ```
   [Sign up for Groq](https://groq.com/) to obtain an API key.

3. **Run a Debate**
   ```bash
   # Basic CLI version
   python full_debate.py

   # Terminal UI version
   python terminal_ui_by_claude.py
   ```

---

**Project Structure**
```
├── basic_architecture.py  # Core debate logic
├── full_debate.py         # Complete debate implementation
└── terminal_ui_by_claude.py # Terminal UI version
```

---

**Contributing** 🤝
1. Fork the repository
2. Create a feature branch: `git checkout -b feature/new-feature`
3. Commit changes: `git commit -m "Add new feature"`
4. Push to branch: `git push origin feature/new-feature`
5. Open a pull request

**Report Issues** 🐛
[Open an issue](https://github.com/aliii-codes/Multi-Agent-Debate-System/issues/new) with:
- Error description
- Steps to reproduce
- Expected behavior

---

**License**
This project is licensed under the [MIT License](LICENSE).

**Acknowledgements**
- [CrewAI](https://github.com/joaomdmoura/crewAI) for agent management
- [Groq](https://groq.com/) for LLM inference
- [Rich](https://rich.readthedocs.io/) for terminal UI components
