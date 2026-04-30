## 🚀 About This Project

This repository contains my learning journey with LangGraph.  
I am experimenting with building graph-based workflows using LLMs, writing small projects, and understanding how complex AI systems can be structured step by step.

## 🧠 What I'm Doing

- Learning LangGraph basics  
- Creating simple graph workflows  
- Exploring LLM chaining and state management  
- Building small experimental projects  

## 📌 Goal

To understand and build advanced AI systems using graph-based architectures.

# Import Library
```bash
from langgraph.graph import StateGraph,START,END
from typing import TypedDict
```
# Create class with typedict
```bash
class Batsman(TypedDict):

    runs: int
    balls: int
    fours: int
    sixes: int
    strike_rate: float
    bpb: int
    bp: float
```
# Add nodes
```bash
graph = StateGraph(Batsman)

graph.add_node('calculate_sr', calculate_sr)
graph.add_node('calculate_bpb', calculate_bpb)
graph.add_node('calculate_bp',calculate_bp)
```
# Add edge
```bash
graph.add_edge(START,'calculate_sr')
graph.add_edge(START,'calculate_bpb')
graph.add_edge(START,'calculate_bp')
```
<img width="480" height="234" alt="26e9ed59-9e07-4db1-9c69-f52fc25f9bb0" src="https://github.com/user-attachments/assets/611567ed-8316-4547-9935-3eef3ca03fb3" />
<img width="144" height="234" alt="54677396-cfde-4be5-8129-7905c7fc4b76" src="https://github.com/user-attachments/assets/bf35543a-516d-4eb6-aa6d-7d580b540133" />

# Conditional Workflows in LangGraph
```bash
from langgraph.graph import StateGraph,START,END
from typing import TypedDict,Literal
```
Creating a Class 
```bash
class Equation(TypedDict):

    a: int
    b: int
    c: int

    equation: str
    discriminant: float
    answer: str
```
```bash
def show_equation(state: Equation):

     equation = f'{state["a"]}x^2 + {state["b"]}x {state["c"]}'
    
     return {"equation": equation}

def calculate_discriminant(state: Equation):

    discriminant = state["b"]**2 - 4*state["a"]*state["c"]

    return {'discriminant':discriminant}

def real_roots(state: Equation):

     root1 = (-state["b"] + state['discriminant']**0.5)/(2*state["a"]) 
     root2 = (-state["b"] - state['discriminant']**0.5)/(2*state["a"]) 

     result = f'The roots are {root1} and {root2}'
     return {'result':result}

def repeated_roots(state: Equation):

     root = -state["b"]/(2*state["a"])

     result = f'Only repeated root is {root}'

     return {'result':result}

def no_real_roots(state:Equation):

     result = f'No real roots'

     return {'result':result}

def check_condition(state: Equation) -> Literal["real_roots", "repeated_roots", 'no_real_roots']:

     if state['discriminant'] > 0:
          return "real_roots"
     elif state['discriminant'] == 0:
          return "repeated_roots"
     else:
          return "no_real_roots"
```
```bash
graph = StateGraph(Equation)

graph.add_node('show_equation',show_equation)
graph.add_node('calculate_discriminant',calculate_discriminant)
graph.add_node('no_real_roots',no_real_roots)
graph.add_node('real_roots',real_roots)
graph.add_node('repeated_roots',repeated_roots)

graph.add_edge(START,'show_equation')
graph.add_edge('show_equation','calculate_discriminant')

graph.add_conditional_edges('calculate_discriminant',check_condition)
graph.add_edge('real_roots',END)
graph.add_edge('repeated_roots',END)
graph.add_edge('no_real_roots',END)

workflow = graph.compile()
```
<img width="483" height="432" alt="de8d980e-9dc9-4252-a468-92cdb6470b6a" src="https://github.com/user-attachments/assets/c7f5b0b3-4999-46d7-9831-265a732a912c" />
```bash
initial_state = {
   "a": 4,
   "b": 2,
   "c": 2
}
workflow.invoke(initial_state)
```
{'a': 4, 'b': 2, 'c': 2, 'equation': '4x^2 + 2x 2', 'discriminant': -28}
