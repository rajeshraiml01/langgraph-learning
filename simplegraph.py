from typing import TypedDict
from langgraph.graph import END, START, StateGraph
from util.langgraph_util import display
# Removed unused import as "langgraph.util.langgraph_util" could not be resolved

class HelloWorldState(TypedDict):
    message: str

def hello(state: HelloWorldState):
    print(f"Hello Node: {state['message']}") 
    return {"message":"Hello "+state["message"]}

def bye(state: HelloWorldState):
    print(f"Bye Node : {state['message']}")
    return {"message":"Bye "+state["message"]}


graph = StateGraph(HelloWorldState)
graph.add_node(hello, {"message": "Hello World"})
graph.add_node(bye, {"message": "Bye World"}) 

graph.add_edge(START, "hello")
graph.add_edge("hello", "bye")
graph.add_edge("bye", END)

runnable = graph.compile()
#display(runnable)
output = runnable.invoke({"message":"Rajesh"})
print(output) # Hello World graph : Hello world
