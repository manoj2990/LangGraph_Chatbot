import streamlit as st 
from backend import chatBot
from langchain_core.messages import HumanMessage

CONFIG = {'configurable': {'thread_id': 'thread-1'}}

# session_state is dic and we create key-val with message_histiry : [ {},{}]
if "message_history" not in st.session_state:
    st.session_state['message_history'] = [
        {"role":"assistant", "content": "Hello, How can i help you"}
    ]
    

    
for msg in st.session_state['message_history']:
    with st.chat_message(msg["role"]):
        st.text(msg["content"])

user_input = st.chat_input("Type here....")

if user_input:
    st.session_state['message_history'].append({"role":"user", "content": user_input})
    with st.chat_message("user"):
        st.text(user_input)
            
    ai_message = st.write_stream(
         message_chunk.content for message_chunk, metadata in chatBot.stream(  {'messages': [HumanMessage(content=user_input)]},config= CONFIG, stream_mode= 'messages')
    )
    st.session_state['message_history'].append({"role":"assistant", "content": ai_message })
 
        
        
    
      
