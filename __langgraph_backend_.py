from langgraph.graph import StateGraph,START,END
from typing import TypedDict,Annotated
from langchain_core.messages import BaseMessage
from langchain_openrouter import ChatOpenRouter
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph.message import add_messages
from dotenv import load_dotenv


load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")

<<<<<<< HEAD

llm = ChatOpenRouter(model='stealth/ox-alpha',api_key='sk-or-vxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx') # put your own api key
=======
llm = ChatOpenRouter(model='stealth/ox-alpha',api_key=api_key) # put your own api key
>>>>>>> f01a001 (done with api)

class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage],add_messages]

def chat_node(state: ChatState):
    messages = state['messages']
    response = llm.invoke(messages)
    return {"messages": [response]}

checkpointer = InMemorySaver()

graph = StateGraph(ChatState)
graph.add_node("chat_node",chat_node)
graph.add_edge(START,"chat_node")
graph.add_edge("chat_node",END)

chatbot = graph.compile(checkpointer=checkpointer)

stream = chatbot.stream(
    {'messages': [HumanMessage(content='what is the recipe to make pasta')]},
    config = {'configurable': {'thread_id': 'thread -1'}},
    stream_mode= 'messages'
)

print(type(stream))