# Constructs the LangGraph pipeline using emotion, memory, and action processing nodes

from langgraph.graph import StateGraph, END
from langgraph_pipeline.emotion_node import detect_emotion
from langgraph_pipeline.memory_node import update_memory
from langgraph_pipeline.pci_node import predict_churn
from langgraph_pipeline.action_node import action_node 
from typing import TypedDict

# define state schema 
class GraphState(TypedDict):
    input: str
    emotion: str
    churn: bool
    action: str

# build the langgraph pipeline
def build_graph():
    builder = StateGraph(GraphState)

    # add each processing node
    builder.add_node("emotion", detect_emotion)
    builder.add_node("memory", update_memory)
    builder.add_node("pci", predict_churn)
    builder.add_node("action", action_node)  #suggest action based on emotion/churn

    # define graph flow
    builder.set_entry_point("emotion")# Entry: emotion
    builder.add_edge("emotion", "memory") 
    builder.add_edge("memory", "pci")
    builder.add_edge("pci", "action")   #action suggester
    builder.add_edge("action", END)

    return builder.compile()
