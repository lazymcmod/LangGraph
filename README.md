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
