from langchain.memory import ConversationBufferMemory

# Create memory object once (persistent)
memory = ConversationBufferMemory(return_messages=True)

# Memory node that updates chat history
def update_memory(state):
    """
    Updates the memory with user's input and the bot's emotional response.
    """
    user_input = state.get("input", "")
    emotion = state.get("emotion", "")  # get emotion from previous node

    if user_input:
        memory.chat_memory.add_user_message(user_input)
    if emotion:
        memory.chat_memory.add_ai_message(f"Emotion detected: {emotion}")

    # Save updated memory back into state
    state["memory"] = memory
    return state
