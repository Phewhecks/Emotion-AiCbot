# Emotion-Based AI Chatbot

This is my AI chatbot project that detects emotions in text and gives replies based on what the user might be feeling. It uses a Hugging Face model and runs everything through a LangGraph pipeline. I used Streamlit for the interface to make it easy to test.

## What It Does

- Detects emotions like anger, joy, sadness, etc. using a pre-trained model
- Remembers stuff from earlier in the chat (memory node)
- Adds personality/context to responses (PCI node)
- Has a simple UI with Streamlit
- Modular setup using LangGraph (easy to test and extend)

## Folder Structure

```
Ai_proj/
├── app.py                   # Streamlit UI
├── chat_history.json        # Memory stored here
├── requirements.txt         # All needed libraries
└── langgraph_pipeline/
    ├── emotion_node.py      # Detects emotion from input
    ├── memory_node.py       # Adds memory context
    ├── pci_node.py          # Injects personality/context
    ├── action_node.py       # Handles the final response
    └── graph_builder.py     # Builds the LangGraph pipeline
```

## To Run

1. Install the requirements:

```
pip install -r requirements.txt
```

2. Start the app:

```
streamlit run app.py
```

That’s it. The UI opens in your browser and you can test the chatbot there.

## Tech Used

- Python
- Streamlit
- LangGraph
- Hugging Face Transformers
- Pretrained model: j-hartmann/emotion-english-distilroberta-base

## Diagram

I made the architecture using draw.io — check the CSV or the figure included in the report.

## Demo

There's a screen recording showing:
- How the UI works
- Chatting with different emotions
- How the response changes based on emotion

## Notes

This was fun to build. Modular pipelines make stuff easy to debug. Emotion adds a human-like layer to chatbot replies. I learned a lot about combining models, logic, and UI.

## Author

Prabin Shrestha