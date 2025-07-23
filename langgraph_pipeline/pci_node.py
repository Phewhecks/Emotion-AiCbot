# predicts churn based on emotions
def predict_churn(state):
    emotion = state.get("emotion", "")
    negative =["sadness", "anger", "fear"]
    churn_risk = "High" if emotion in negative else "low"
    state["churn"]= churn_risk
    return state