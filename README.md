# Omnix

Omnix is a modular **local AI desktop assistant** built with Python.

The project is being developed incrementally with the goal of creating a powerful AI assistant that can understand natural-language commands, interact with the computer, use local AI models, automate tasks, maintain user preferences, and communicate through both text and voice.


## Current Features

### 🤖 Local AI

* Local AI integration using Ollama
* Qwen 2.5 3B model support
* Profile-aware prompting
* Behaviour and response-preference handling
* AI responses generated locally

### 🎙️ Voice Input

* Microphone input using SpeechRecognition
* PyAudio-based audio input
* Text and voice input modes
* Continuous assistant interaction

### 🔊 Text-to-Speech

* Local TTS using Piper
* Ryan English voice
* Automatic AI response playback
* Voice mode ON/OFF control
* Configurable voice processing
* Audio playback using system audio tools

### 🧠 User Profile

Omnix maintains a local user profile containing information such as:

* Purpose
* Domain
* Response preference

Example:

```text
Purpose: Coding
Domain: Python, Java
Preference: Step by step
```

The profile is used as context while generating AI responses.

### 🛠️ Command Routing

Omnix uses a modular dispatcher to identify different types of commands and route them to the appropriate system.

Currently supported routing includes:

* AI commands
* Time/date commands
* Profile commands
* Application and website commands
* Voice mode commands

### 💻 Desktop & Web Control

Current foundation includes:

* Opening applications
* Closing applications
* Opening websites
* Closing applications/websites
* Command history
* Basic system interaction

### 📝 Developer Foundation

* Modular Python project structure
* Separate AI layer
* Separate voice layer
* Separate TTS layer
* Command dispatcher
* Application/web router
* User profile system
* Logging system
* Command history
* Parser utilities
* Basic automated testing


# Available Commands

Examples:

```text
open spotify
close spotify
open youtube
close github
history
```

### Voice Mode

```text
voice on
voice off
```

When voice mode is enabled, AI responses are automatically converted to speech.

### Time & Date

Examples:

```text
what is the time
current time
today's date
aaj ka time
aaj ki date
```

### Profile

Examples:

```text
profile
change profile
update profile
```

### Exit

```text
exit
quit
bye
stop
```


# Installation

## 1. Clone the Repository

```bash
git clone https://github.com/prabaltomar11/Omnix.git
cd Omnix
```

## 2. Create Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## 3. Install Python Dependencies

```bash
pip install -r requirements.txt
```

## 4. Install Ollama

Install Ollama on your system and make sure the Ollama service is running.

Then download the Qwen model:

```bash
ollama pull qwen2.5:3b
```

Verify:

```bash
ollama list
```

## 5. Install System Audio Dependencies

Omnix currently uses Linux system audio tools for playback.

Make sure `ffmpeg` and `aplay` are available:

```bash
ffmpeg -version
```

```bash
which aplay
```

## 6. TTS Voice Model

The current TTS setup uses the Piper Ryan voice model.

The Piper voice model files are not included in the Git repository because the `.onnx` model file is large.

Download the required Piper Ryan voice model and place the files at:

```text
tts/models/en/en_US-ryan-medium.onnx
tts/models/en/en_US-ryan-medium.onnx.json
```

Make sure both files exist before starting Omnix.


# How to Use Omnix

Start Omnix:

```bash
python3 main.py
```

Omnix will ask you to choose an input mode:

```text
1. Text
2. Voice
```

Choose the mode you want.

### Text Mode

In text mode, enter commands directly through the terminal.

Example:

```text
What is Python?
```

Omnix sends the request to the local Qwen model and displays the response.

### Voice Mode

In voice mode, Omnix listens for microphone input and processes the spoken command.

You can also control response speech:

```text
voice on
```

After this, AI responses are automatically spoken.

To disable automatic speech:

```text
voice off
```


# What We Learned While Building Omnix

Omnix is also a learning project. During development, we worked with several important concepts.

### Python

* Functions
* Variables and global state
* Return values
* Conditional statements
* Loops
* Modules and imports
* Exception handling
* Subprocess execution
* Temporary files
* File and folder structure
* Virtual environments

### AI Integration

* Connecting Python with Ollama
* Running local LLMs
* Sending prompts to Qwen
* Using user-profile information as AI context
* Separating AI logic from application logic

### Voice & Audio

* SpeechRecognition
* PyAudio
* Piper TTS
* ONNX-based voice models
* Audio playback with `aplay`
* Audio processing with FFmpeg
* Voice state management
* Connecting AI responses with TTS

### Software Architecture

* Modular project structure
* Dispatcher-based routing
* Tool separation
* AI layer
* Voice layer
* TTS layer
* Router layer
* Profile management
* Logging
* History management

### Development & Debugging

* Python virtual environments
* Package management with `pip`
* Testing individual modules
* Reading tracebacks
* Debugging import errors
* Checking installed packages
* Checking hardware and system dependencies
* Using Git for version control


# Project Status

## Current Version: V0.4.0

Omnix is currently under active development.

The V0.4.0 milestone focuses on establishing a strong local-AI and voice-enabled backend foundation.

### Completed

* Local Qwen AI integration
* User profile system
* Command dispatcher
* Application and website routing foundation
* Voice input foundation
* Piper TTS integration
* Ryan voice integration
* Voice ON/OFF state management
* Automatic AI response speech
* Modular backend structure

### In Development

* Stronger laptop control
* More system tools
* Better intent detection
* Improved command routing
* Conversation memory
* Better voice interaction
* More reliable tool execution


# Vision

The long-term goal of Omnix is to become a powerful **local-first AI desktop assistant**.

The vision for Omnix V1 is to give the assistant the ability to:

```text
Understand natural language
        ↓
Reason using local AI
        ↓
Choose the right tool
        ↓
Interact with the computer
        ↓
Retrieve knowledge
        ↓
Run automations
        ↓
Return the result
        ↓
Speak the response when required
```

Future Omnix versions are intended to combine:

* Local AI
* Voice interaction
* Desktop control
* File management
* Browser automation
* RAG
* n8n workflows
* System automation
* Long-term memory
* Tool orchestration

The ultimate goal is to build an assistant that can act as a **natural-language control layer for the computer**, while keeping the system modular, understandable, and local-first.

---

# Author

Developed by **Prabal Tomar**

Omnix is being built incrementally as both a practical AI assistant and a learning project focused on Python, local AI, automation, voice systems, and software architecture.
