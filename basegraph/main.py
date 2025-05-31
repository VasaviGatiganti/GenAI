from typing_extensions import TypedDict
from langgraph.graph import START, END, StateGraph
class State(TypedDict):
    message: str
def node_1(state: State) -> State:
    """This is node 1
    """
    state['message'] += "node 1"
def node_2(state: State) -> State:
    """This is node 2
    """
    state['message'] += "node 2"
def node_3(state: State) -> State:
    """This is node 3
    """
    state['message'] += "node 3"
#add nodes

builder:StateGraph = StateGraph(State)
builder.add_node("node_1",node_1)
builder.add_node("node_2",node_2)
builder.add_node("node_3",node_3)

#add edges

builder.add_edge(START,"node_1")
builder.add_edge("node_1","node_2")
builder.add_edge("node_2","node_3")
builder.add_edge("node_3",END)

graph = builder.compile()

#graph.invoke



