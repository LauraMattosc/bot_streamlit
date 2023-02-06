import streamlit as st
import spacy

st.title("Chatbot")

nlp = spacy.load("en_core_web_sm")

user_input = st.text_input("User:", value="")

if user_input:
    doc = nlp(user_input)
    intent = None
    for token in doc:
        if token.text.lower() in ["hi", "hello", "hey"]:
            intent = "greeting"
        elif token.text.lower() in ["bye", "goodbye"]:
            intent = "farewell"
    if intent == "greeting":
        st.write("Bot: Hello! How can I help you today?")
    elif intent == "farewell":
        st.write("Bot: Goodbye! Have a nice day.")
    else:
        st.write("Bot: Sorry, I don't understand. Can you try asking me something else?")
