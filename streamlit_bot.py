import streamlit as st
import pandas as pd
import spacy


nlp = spacy.load('pt_core_news_sm')

# Definir estilo da página
st.set_page_config(page_title="Chatbot", page_icon=":robot_face:", layout="wide")

# Definir título e subtítulo da página
st.title("Chatbot🤖")
st.markdown("Sou um chatbot e estou aqui para responder suas perguntas! 😄")


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

pergunta_selecionada = st.selectbox("Escolha uma pergunta:", [exemplo['Pergunta'] for exemplo in exemplos])

# Exibir lista de perguntas
df = pd.DataFrame(columns=['Pergunta', 'Resposta'])

for exemplo in exemplos:
    adicionar_pergunta_resposta(exemplo['Pergunta'], exemplo['Resposta'])

# Buscar a resposta no DataFrame
if pergunta_selecionada:
    resposta = df[df['Pergunta'] == pergunta_selecionada]['Resposta'].iloc[0]
else:
    resposta = ""

# Exibir resposta
if resposta:
    st.markdown(f"<div style='background-color:transparent;border-radius:3px;padding:10px;color:black;margin-top:10px'>Resposta do Bot ⬇️</div>", unsafe_allow_html=True)
    st.markdown(f"<div style='background-color:transparent;border-radius:3px;padding:10px;color:black;margin-top:10px;font-size:16px'>{resposta}</div>", unsafe_allow_html=True)
    st.empty()
