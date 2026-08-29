import streamlit as st 
from backend import chatBot
from langchain_core.messages import HumanMessage
import uuid



# utility fxn to generate thread ids
def generate_thread_id():
    thread_id = uuid.uuid4()
    return thread_id

def reset_chat():
    thread_id = generate_thread_id()
    st.session_state["thread_id"] = thread_id
    add_thread_id(thread_id)
    st.session_state['message_history'] = []
    

def add_thread_id(thread_id):
    if thread_id not in  st.session_state["chat_threads"]:
         st.session_state["chat_threads"].append(thread_id)
        
def load_conversation(thread_id):
    CONFIG = {'configurable': {'thread_id': thread_id}}
    resp = chatBot.get_state(CONFIG)
    return resp.values["messages"]


# session_state is dic and we create key-val with message_histiry : [ {},{}]
if "message_history" not in st.session_state:
    st.session_state['message_history'] = [
        {"role":"assistant", "content": "Hello, How can i help you"}
    ]

if "thread_id" not in st.session_state:
    st.session_state["thread_id"] = generate_thread_id()
    
if "chat_threads" not in st.session_state:
    st.session_state["chat_threads"] = []
    id =  st.session_state["thread_id"]
    add_thread_id(id)
    
    
# sidebar
st.sidebar.title("Langgraph Chat")
if st.sidebar.button("New Chat"):
    reset_chat()
    
st.sidebar.header("My conversation")

for id in st.session_state["chat_threads"][::-1]:
    if st.sidebar.button(str(id)):
        st.session_state["thread_id"] = id
        messages = load_conversation(str(id))
        
        temp_messages = []
        for msg in messages:
            if isinstance(msg, HumanMessage):
                role = "user"
            else:
                role = "assistant"
                
            temp_messages.append({"role": role, "content": msg.content })
        
        st.session_state['message_history'] = temp_messages
        
    
for msg in st.session_state['message_history']:
    with st.chat_message(msg["role"]):
        st.text(msg["content"])

    
user_input = st.chat_input("Type here....")

CONFIG = {'configurable': {'thread_id': st.session_state["thread_id"]}}
def generate_resp(user_input):
    
    stream = chatBot.stream(
            {'messages': [HumanMessage(content=user_input)]},config= CONFIG, stream_mode= 'messages'
        )
  
    for  message_chunk, metadata in stream:
         
            if message_chunk.content:
                yield message_chunk.content

if user_input:
    st.session_state['message_history'].append({"role":"user", "content": user_input})
    with st.chat_message("user"):
        st.text(user_input)
            
    with st.chat_message("assistant"):
        ai_message = st.write_stream(generate_resp(user_input))
        
        st.session_state['message_history'].append({"role":"assistant", "content": ai_message })
 
        
        
    
      
