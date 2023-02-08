import streamlit as st
import pandas as pd

st.title("Chatbot")

user_input = st.text_input("Pergunta:", value="")

if user_input:
answers = []
questions = []

if "what's your name?" in user_input.lower():
    answers.append("Bot: My name is Bot, nice to meet you!")
    questions.append("What's your name?")
elif "what is the weather today?" in user_input.lower():
    answers.append("Bot: I am sorry, I am not capable of checking the weather. You can try searching for it online.")
    questions.append("What is the weather today?")
elif "what time is it?" in user_input.lower():
    answers.append("Bot: The current time is {0}.".format(datetime.now().strftime("%H:%M")))
    questions.append("What time is it?")
elif "what's your purpose?" in user_input.lower():
    answers.append("Bot: My purpose is to assist and answer questions to the best of my ability.")
    questions.append("What's your purpose?")
elif "what do you do?" in user_input.lower():
    answers.append("Bot: I am a chatbot designed to answer questions and provide information.")
    questions.append("What do you do?")
else:
    answers.append("Bot: Sorry, I don't understand. Can you try asking me something else?")
    questions.append(user_input)

df = pd.DataFrame({"Pergunta": questions, "Resposta": answers})
st.table(df)
