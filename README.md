Personal AI Assistant

A locally running AI assistant built with Python that combines voice interaction, persistent memory, gesture control, and a local Large Language Model (LLM) to provide a personalized assistant experience.

Overview

This project aims to create a privacy-focused personal AI assistant that can:

* Understand voice commands using Whisper
* Respond using a local LLM through Ollama
* Remember user-specific information across sessions
* Execute commands such as opening websites and applications
* Support gesture-based interactions using MediaPipe

Unlike cloud-only assistants, the core intelligence runs locally, reducing dependence on external AI APIs.

⸻

Features

Voice Assistant

* Speech-to-Text with Whisper
* Text-to-Speech responses
* Conversational interaction

Local AI

* Ollama integration
* Llama 3.2 model support
* Context-aware conversations using chat history

Personal Memory

* Persistent JSON-based memory
* Store and retrieve user information
* Memory management commands

Command Execution

* Open websites
* Open applications
* Google search
* YouTube search
* Date and time queries

Gesture Control

* Hand tracking with MediaPipe
* Swipe gesture recognition
* Gesture-based control mode

⸻

Project Architecture

User Voice
↓
Whisper Speech Recognition
↓
Command Router
↓
├── Memory System
├── Command Handlers
├── Gesture Controls
└── Ollama (Llama 3.2)
↓
Text-to-Speech Response

⸻

Technology Stack

* Python
* Whisper
* Ollama
* Llama 3.2
* MediaPipe
* pyttsx3
* SpeechRecognition

⸻

Current Capabilities

✅ Voice Interaction

✅ Local AI Conversations

✅ Persistent User Memory

✅ Chat History

✅ Website and Application Commands

✅ Gesture Control

⸻

Installation

git clone https://github.com/vikashm-77/Personal-AI-Assistant.git
cd Personal-AI-Assistant

Create and activate a virtual environment:

python -m venv assistant_env
source assistant_env/bin/activate

Install dependencies:

pip install -r requirements.txt

Run Ollama:

ollama run llama3.2

Start the assistant:

python main.py
# Test
