from langgraph.graph import StateGraph

def llm_node(state):
    # decide next step
    return state

def tool_node(state):
    # execute tool
    return state

graph = StateGraph()

graph.add_node("llm", llm_node)
graph.add_node("tool", tool_node)

graph.set_entry_point("llm")

graph.add_edge("llm", "tool")
graph.add_edge("tool", "llm")  # loop!

app = graph.compile()