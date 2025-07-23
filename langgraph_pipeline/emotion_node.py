from transformers import pipeline

#already trained model from HUGGINGFACE
emotion_pipeline = pipeline(
    "text-classification",
    model = "j-hartmann/emotion-english-distilroberta-base", # huggingface
    top_k=None
)

# Emotion detection node
def detect_emotion(state):
    text = state.get("input", "")
    result = emotion_pipeline(text)[0]
    top_emotion = max(result, key=lambda x: x["score"])["label"]
    state["emotion"]= top_emotion
    return state

