import streamlit as st
import datetime

st.title("Chatbot")

user_input = st.text_input("Question:", value="")

questions = ["what's your name?",
             "what is the weather today?",
             "what time is it?",
             "what's your purpose?",
             "what do you do?"]

answers = ["My name is Bot, nice to meet you!",
           "I am sorry, I am not capable of checking the weather. You can try searching for it online.",
           "The current time is {0}.".format(datetime.datetime.now().strftime("%H:%M")),
           "My purpose is to assist and answer questions to the best of my ability.",
           "I am a chatbot designed to answer questions and provide information."]

if user_input:
    for i, question in enumerate(questions):
        if question in user_input.lower():
            st.write("Bot: " + answers[i])
            break
    else:
        st.write("Bot: Sorry, I don't understand. Can you try asking me something else?")

st.table(pd.DataFrame({"Question": questions, "Answer": answers}))
