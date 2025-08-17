# workflow.py
import os
import streamlit as st
from typing import TypedDict, Annotated
from langchain_core.messages import BaseMessage, HumanMessage
from langchain_groq import ChatGroq
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.sqlite import SqliteSaver
from langgraph.graph.message import add_messages
import sqlite3

conn=sqlite3.connect(database="chatapp.db", check_same_thread=False)

api_key = st.secrets["GROQ_API_KEY"]
os.environ["GROQ_API_KEY"] = api_key

class ChatState(TypedDict):
    messages : Annotated[list[BaseMessage], add_messages]

model=ChatGroq(model="openai/gpt-oss-120b")

def chat_node(state:ChatState):
    messages=state['messages']
    response=model.invoke(messages)

    return {'messages': response}

graph=StateGraph(ChatState)

graph.add_node( 'chat_node', chat_node)

graph.add_edge(START, 'chat_node')
graph.add_edge('chat_node', END)

db=SqliteSaver(conn=conn)

chat_workflow=graph.compile(checkpointer=db)

def retrieve_all_threads():
    all_threads=set()        
    for checkpoint in db.list(None):
        all_threads.add(checkpoint.config['configurable']['thread_id'])
    return list(all_threads)
