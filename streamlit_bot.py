import streamlit as st
import pandas as pd
import spacy

nlp = spacy.load('pt_core_news_sm')

def adicionar_pergunta_resposta(pergunta, resposta):
    global df
    nova_linha = pd.DataFrame({'Pergunta': [pergunta], 'Resposta': [resposta]})
    df = pd.concat([df, nova_linha], ignore_index=True)

# Exemplo de perguntas e respostas
exemplos = [
    {'Pergunta': 'Qual é o seu nome?', 'Resposta': 'Meu nome é Chatbot.'},
]

pergunta = st.text_input("Faça uma pergunta:")

# Criar DataFrame inicial com as perguntas de exemplo
df = pd.DataFrame(exemplos)

st.title("Chatbot")

if pergunta:
    doc = nlp(pergunta)
    for token in doc:
        print(token.text, token.pos_, token.dep_)
    # Buscar a resposta no DataFrame
    resposta = df[df['Pergunta'] == pergunta]['Resposta'].iloc[0]
    # Adicionar a pergunta e a resposta ao DataFrame
    adicionar_pergunta_resposta(pergunta, resposta)
    st.write(resposta)
