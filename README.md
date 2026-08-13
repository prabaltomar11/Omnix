# Omnix

Omnix is a modular desktop automation and local AI assistant built with Python.

The project is being developed step by step with the goal of becoming a voice-enabled AI desktop assistant capable of understanding natural language, interacting with local applications, managing websites, maintaining user preferences, and providing AI-powered assistance.

## Current Features

### Core Assistant

- Modular Python architecture
- Continuous command loop
- Text input support
- Voice input support (Speech-to-Text)
- Professional logging
- Command history
- Command parser
- Application control
- Website control

### User Profile System

- User profile setup
- Purpose, domain, and response preference storage
- Persistent profile storage using JSON
- Profile loading on startup
- Profile update system
- Fresh profile setup for new users

### Local AI

- Local LLM integration using Ollama
- Qwen 2.5 3B model support
- Profile-aware AI prompting
- Purpose, domain, and response preference passed to the AI
- AI responses generated locally without requiring an external LLM API

## Installation

Clone the repository:

```bash
git clone https://github.com/prabaltomar11/Omnix.git
cd Omnix
```

installation:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
ollama pull qwen2.5:3b
ollama list
```

run omnix:

```bash
python3 main.py
```

## Available Commands

- `open spotify`
- `close spotify`
- `open youtube`
- `close github`
- `history`
- `exit`

Supported applications include: Spotify, Firefox, VS Code, Terminal, Files, Chrome.

Supported websites include: YouTube, GitHub, Google, ChatGPT, Gemini, and Claude.

## User Profile

Omnix maintains a local user profile containing:

Purpose
Domain
Preference

Example:

Purpose: coding
Domain: python, java
Preference: step by step

This information is used as context when generating AI responses.

The profile can be updated without manually editing profile.json.

## Current AI Architecture

User Input
    ↓
main.py
    ↓
dispatch()
    ↓
ask_ai()
    ↓
User Profile + Behaviour Prompt
    ↓
Ollama
    ↓
Qwen 2.5 3B
    ↓
AI Response

## Future Roadmap

The following features are planned for future versions:

Real-time information tools
Current date and time integration
Intelligent intent and tool routing
Stronger response preference enforcement
Conversation memory integration
Text-to-Speech
Improved voice interaction
Simultaneous text and voice interaction
Dynamic application detection
Dynamic website detection
File and folder management
System automation
Email automation
Cross-platform support for Windows, Linux, and macOS

## Project Status

🚧 Currently under active development.

Omnix V1 is being developed incrementally, with the focus on building a reliable foundation before adding more advanced automation and AI capabilities.

## Vision

The long-term goal of Omnix is to become a fully voice-enabled AI desktop assistant capable of:

Understanding natural language
Running local AI models
Automating desktop applications
Managing websites
Managing files and folders
Maintaining user preferences and conversation context
Providing real-time information through external tools
Automating everyday computer tasks

## Author

Developed by Prabal Tomar
