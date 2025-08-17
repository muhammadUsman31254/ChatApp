# app.py
import uuid
import streamlit as st
from langchain_core.messages import HumanMessage
from workflow import chat_workflow, retrieve_all_threads

def generate_thread_id():
    thread_id = str(uuid.uuid4())
    return thread_id

def clear_chat_history():
    thread_id = generate_thread_id()
    st.session_state['thread_id'] = thread_id
    add_thread_id(st.session_state['thread_id'])
    st.session_state['chat_history'] = []

def add_thread_id(thread_id):
    if thread_id not in st.session_state['chat_threads']:
        st.session_state['chat_threads'].append(thread_id)
    
def load_chat(thread_id):
    state = chat_workflow.get_state(config={"configurable": {"thread_id": thread_id}})
    return state.values.get('messages', [])

if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

if 'thread_id' not in st.session_state:
    st.session_state['thread_id'] = generate_thread_id()

if 'chat_threads' not in st.session_state:
    st.session_state['chat_threads'] = retrieve_all_threads()

add_thread_id(st.session_state['thread_id'])

with st.sidebar:
    st.title("AI Chat Assistant")
    st.markdown("---")

    if st.button("💬 New Chat", type="secondary"):
        clear_chat_history()

    st.write("🗂️ Chats")
    for thread_id in st.session_state['chat_threads'][::-1]:
        if st.button(str(thread_id), type="tertiary"):
            st.session_state['thread_id'] = thread_id
            messages = load_chat(thread_id)

            temp_messages = []
            for msg in messages:
                if isinstance(msg, HumanMessage):
                    role = 'user'
                else:
                    role = 'assistant'
                temp_messages.append({'role': role, 'content': msg.content})
            st.session_state['chat_history'] = temp_messages
    

for message in st.session_state['chat_history']:
    with st.chat_message(message['role']):
        st.text(message['content'])

user_input = st.chat_input('Type here...')
if user_input:
    st.session_state['chat_history'].append({'role': 'user', 'content': user_input})
    with st.chat_message('user'):
        st.text(user_input)

    with st.chat_message('assistant'):
        assistant_message = st.write_stream(
            message_chunk.content for message_chunk, metadata in chat_workflow.stream(
                {'messages': [HumanMessage(content=user_input)]}, 
                config={"configurable": {"thread_id": st.session_state['thread_id']}},
                stream_mode="messages"
            )
        )

        st.session_state['chat_history'].append({'role': 'assistant', 'content': assistant_message})