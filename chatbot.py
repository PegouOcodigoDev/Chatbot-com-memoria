import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage
import time
from chain import generate_response

st.set_page_config(page_title="Seu assistente virtual", page_icon="🤖")
st.title("Seu assistente virtual")

if "history" not in st.session_state:
    st.session_state.history = [AIMessage(content="Olá, sou seu assistente virtual!")]

for message in st.session_state.history:
    if isinstance(message, AIMessage):
        with st.chat_message("AI"):
            st.write(message.content)
    elif isinstance(message, HumanMessage):
        with st.chat_message("Human"):
            st.write(message.content)

query = st.chat_input("Digite sua mensagem aqui...")
if query:
    st.session_state.history.append(HumanMessage(content=query))
    with st.chat_message("Human"):
        st.markdown(query)
    
    response = generate_response(query, st.session_state.history)

    with st.chat_message("AI"):
        message_placeholder = st.empty()
        full_response = ""

        for chunk in response:
            full_response += chunk
            message_placeholder.markdown(full_response)
            time.sleep(0.5) 

    st.session_state.history.append(AIMessage(content=full_response))
