import streamlit as st

st.title("Chatbot")

user_input = st.text_input("Pergunta:", value="")

if user_input:
    if "what's your name?" in user_input.lower():
        st.write("Bot: My name is Bot, nice to meet you!")
    elif "what is the weather today?" in user_input.lower():
        st.write("Bot: I am sorry, I am not capable of checking the weather. You can try searching for it online.")
    elif "what time is it?" in user_input.lower():
        st.write("Bot: The current time is {0}.".format(datetime.now().strftime("%H:%M")))
    elif "what's your purpose?" in user_input.lower():
        st.write("Bot: My purpose is to assist and answer questions to the best of my ability.")
    elif "what do you do?" in user_input.lower():
        st.write("Bot: I am a chatbot designed to answer questions and provide information.")
    else:
        st.write("Bot: Sorry, I don't understand. Can you try asking me something else?")
