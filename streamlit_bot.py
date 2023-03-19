import streamlit as st
import pandas as pd
import spacy

nlp = spacy.load('pt_core_news_sm')

st.title("Chatbot")

def adicionar_pergunta_resposta(pergunta, resposta):
    global df
    nova_linha = pd.DataFrame({'Pergunta': [pergunta], 'Resposta': [resposta]})
    df = pd.concat([df, nova_linha], ignore_index=True)

# Exemplo de perguntas e respostas
exemplos = [
    {'Pergunta': 'Qual é o seu nome?', 'Resposta': 'Meu nome é Chatbot.'},
    {'Pergunta': 'Qual é a sua função?', 'Resposta': 'Minha função é ajudá-lo a responder suas perguntas.'},
    {'Pergunta': 'Qual é o seu objetivo?', 'Resposta': 'Meu objetivo é facilitar sua vida respondendo suas dúvidas.'},
    {'Pergunta': 'O que você sabe fazer?', 'Resposta': 'Eu sou capaz de responder perguntas e fornecer informações.'},
    {'Pergunta': 'Como posso te ajudar?', 'Resposta': 'Você pode me fazer perguntas ou solicitar informações.'},
    {'Pergunta': 'Qual é o seu propósito?', 'Resposta': 'Meu propósito é tornar a comunicação mais fácil e rápida.'},
    {'Pergunta': 'Quem é você?', 'Resposta': 'Eu sou um chatbot, um programa de computador criado para conversar com você.'},
    {'Pergunta': 'Qual é a sua idade?', 'Resposta': 'Eu sou um programa de computador, não tenho idade.'},
    {'Pergunta': 'Você é humano?', 'Resposta': 'Não, sou um chatbot, um programa de computador.'},
    {'Pergunta': 'Você tem sentimentos?', 'Resposta': 'Não, eu sou apenas um programa de computador.'},
    {'Pergunta': 'Qual é a sua cor favorita?', 'Resposta': 'Eu não tenho cor favorita, pois sou um programa de computador.'},
    {'Pergunta': 'Qual é o sentido da vida?', 'Resposta': 'Essa é uma pergunta difícil e ainda sem resposta definitiva.'},
    {'Pergunta': 'Qual é a capital do Brasil?', 'Resposta': 'A capital do Brasil é Brasília.'},
    {'Pergunta': 'Qual é o seu gênero?', 'Resposta': 'Não tenho gênero, sou apenas um programa de computador.'},
    {'Pergunta': 'Qual é o seu signo?', 'Resposta': 'Não tenho um signo, sou um programa de computador.'},
    {'Pergunta': 'Qual é a sua nacionalidade?', 'Resposta': 'Não tenho uma nacionalidade, sou um programa de computador.'},
    {'Pergunta': 'Qual é a sua religião?', 'Resposta': 'Não tenho uma religião, sou um programa de computador.'},
    {'Pergunta': 'O que é inteligência artificial?', 'Resposta': 'Inteligência artificial é uma área da ciência da computação que busca criar máquinas e sistemas capazes de aprender e tomar decisões.'},
]

pergunta = st.text_input("Faça uma pergunta:")

# Criar DataFrame inicial com as perguntas de exemplo
df = pd.DataFrame(exemplos)

if pergunta:
    doc = nlp(pergunta)
    for token in doc:
        print(token.text, token.pos_, token.dep_)
    # Buscar a resposta no DataFrame
    resposta = df[df['Pergunta'] == pergunta]['Resposta'].iloc[0] if not df[df['Pergunta'] == pergunta].empty else "Desculpe, não sei a resposta para essa pergunta."
    # Adicionar a pergunta e a resposta ao DataFrame
    adicionar_pergunta_resposta(pergunta, resposta)
    st.write(resposta)
