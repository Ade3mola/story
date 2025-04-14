import streamlit as st
import random
import time
from model import  system_prompt,chat_model

# Streamed response emulator
def response_generator(prompt: str):
    response =chat_model(prompt=system_prompt(prompt))
    
    for word in response.split():
        yield word + " "
        time.sleep(0.05)


st.title("MY STORY WRITING SUPPORT BOT")

st.divider()

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("Hello writer!!! how may i assist you today?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        response = st.write_stream(response_generator(prompt = prompt))
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})