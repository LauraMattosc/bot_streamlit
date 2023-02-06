import streamlit as st

st.title("Chatbot")

user_input = st.text_input("User:", value="")

if user_input:
    if "hi" in user_input.lower():
        st.write("Bot: Hello! How can I help you today?")
    elif "bye" in user_input.lower():
        st.write("Bot: Goodbye! Have a nice day.")
    else:
        st.write("Bot: Sorry, I don't understand. Can you try asking me something else?") 
