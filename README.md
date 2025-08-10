# Emotion-Based AI Chatbot

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&style=flat-square)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)

This project is an intelligent chatbot that **detects user emotions** and provides **emotionally-aware responses** using NLP techniques and a modular pipeline.

---

## Features

- Emotion detection using a Hugging Face transformer model  
- Modular LangGraph-based pipeline  
- Persistent chat memory with JSON  
- Persona/context injection (PCI node)  
- Streamlit frontend for interactive chat testing  

---

## Installation

1. Clone the repo:
   ```bash
   git clone https://github.com/Phewhecks/Emotion-AiCbot.git
   cd Emotion-AiCbot
   ```
2. Install dependencies:
   ```bash
   pip install -r Ai_proj/requirements.txt
   ```
3. Run the chatbot:
   ```bash
   streamlit run Ai_proj/app.py
   ```

---

## Project Structure

```
Emotion-AiCbot/
└── Ai_proj/
    ├── app.py                      # Streamlit chatbot UI
    ├── chat_history.json           # Chat memory store
    ├── requirements.txt            # Python dependencies
    ├── langgraph_pipeline/         # Modular node architecture
    │   ├── emotion_node.py
    │   ├── memory_node.py
    │   ├── pci_node.py
    │   ├── action_node.py
    │   └── graph_builder.py
    ├── report/                     # Documentation & diagram
    │   ├── Emotion_Chatbot_Report_Front_Page.docx
    │   ├── Final_Emotion_Chatbot_Report.docx
    │   └── EmotionChatbotPipeline_Restored.png
    └── README.md                   # Project overview
```

---

## Demo

[Watch Demo Video on YouTube](https://youtu.be/AFgMKiEY4QE)
: https://youtu.be/AFgMKiEY4QE 
---



---

## Author

Prabin Shrestha
