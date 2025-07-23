# Streamlit App: Frontend interface for user interaction with the AI chat system

# import required libraries
import streamlit as st
import json
from langgraph_pipeline.graph_builder import build_graph

# emoji mapping for emotion
emotion_emoji_map = {
    "happy": "😄",
    "sad": "😢",
    "sadness": "😢",
    "angry": "😠",
    "anger": "💢😠",
    "surprise": "😲",
    "neutral": "😐",
    "fear": "😨",
    "disgust": "🤢",
    "joy": "😊",
    "love": "❤️",
}

# save chat to json
def save_chat():
    data = st.session_state.history
    with open("chat_history.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

# build the langgraph once
graph = build_graph()

# initialize chat history
if "history" not in st.session_state:
    st.session_state.history = []

# app title
st.set_page_config(page_title="Emotion Bot", page_icon="🤖", layout="centered")
st.title("🤖 Emotion_Aware Reaction Bot")

# handle user input and invoke graph

def handle_submit():
    user_text = st.session_state.user_input.strip()
    if user_text:
        st.session_state.history.append(("user", user_text))

        result = graph.invoke({"input": user_text})

        result["emotion"] = result.get("emotion", "").lower()
        emotion = result["emotion"]
        emoji = emotion_emoji_map.get(emotion, "")
        action = result.get("action", "").strip()

        generic_reply = f"I sense you're feeling {emotion} {emoji}."

        # Suggest action naturally if available and not a generic no-action
        if action.lower() not in ["", "no action", "no action required", "none"]:
            bot_reply = f"{generic_reply} You might want to {action.lower()}."
        else:
            bot_reply = generic_reply

        st.session_state.history.append(("bot", bot_reply))
        save_chat()
        st.session_state.user_input = ""


# user input box
st.text_input("You:", key="user_input", on_change=handle_submit, label_visibility="collapsed", placeholder="Type your message and press Enter...")

# show last few messages
with st.container():
    st.markdown("<div class='chat-box'>", unsafe_allow_html=True)
    last_n = 1
    history_to_show = st.session_state.history[-last_n:]
    for sender, msg in history_to_show:
        if sender == "user":
            st.markdown(f"<div style='background:#444654; color:white; padding:8px; margin:4px 0; border-radius:10px; max-width:90%; align-self:flex-end;'>{msg}</div>", unsafe_allow_html=True)
        else:
            safe_msg = msg.replace("\n", "<br>")
            st.markdown(f"<div style='background:#1a1a1a; color:white; padding:8px; margin:4px 0; border-radius:10px; max-width:90%;'>{safe_msg}</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
