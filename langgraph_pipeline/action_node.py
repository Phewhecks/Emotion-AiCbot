# suggest actions/next best action
def action_node(state):
    emotion = state.get("emotion", "").lower()

    # Normalize common alternate labels if needed
    if emotion == "sadness":
        emotion = "sad"
    elif emotion == "happiness":
        emotion = "happy"
    elif emotion == "fearful":
        emotion = "fear"
    

    emotion_action_map = {
        "happy": "Express your gratitude and keep the positive vibes going!",
        "joy": "Share your happiness with others—it’s contagious!",
        "sad": "Take some time for self-care or talk to a close friend.",
        "anger": "Try some calming techniques or consider reaching out for support.",
        "fear": "Focus on grounding exercises and seek reassurance from trusted people.",
        "disgust": "Identify the cause and try to avoid or resolve it if possible.",
        "surprise": "Reflect on what caused this surprise and adapt accordingly.",
        "neutral": "Keep things steady and stay mindful of your feelings.",
        "love": "Show appreciation and express your feelings openly.",
        "boredom": "Find a new activity or hobby to re-energize yourself.",
        "confusion": "Take a moment to clarify your thoughts or ask questions.",
        "excited": "Channel your excitement into productive actions!",
        "anxiety": "Practice breathing exercises and focus on the present moment.",
        "disappointment": "Allow yourself to feel it, then think about next steps.",
        "hopeful": "Stay positive and set achievable goals.",
        "grateful": "Express thanks to someone who’s made a difference.",
    }

    action = emotion_action_map.get(emotion, "Take a moment to check in with yourself and see what you need.")

    state["action"] = action
    return state
