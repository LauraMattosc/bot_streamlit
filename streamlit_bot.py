import streamlit as st
from datetime import datetime
import pandas as pd
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Inicializar o ChatterBot
chatbot = ChatBot('Bot')
treinador = ChatterBotCorpusTrainer(chatbot)

# Treinar o ChatterBot com o corpus em português
treinador.train("chatterbot.corpus.portuguese")

st.title("Chatbot")

# Criar DataFrame inicial
colunas = ['Pergunta', 'Resposta']
df = pd.DataFrame(columns=colunas)

# Função para adicionar perguntas e respostas ao DataFrame
def adicionar_pergunta_resposta(pergunta, resposta):
    global df
    nova_linha = {'Pergunta': pergunta, 'Resposta': resposta}
    df = df.append(nova_linha, ignore_index=True)

user_input = st.text_input("Pergunta:", value="")
if user_input:
    resposta = chatbot.get_response(user_input)
    resposta_texto = str(resposta)

    if resposta_texto:
        adicionar_pergunta_resposta(user_input, resposta_texto)
        st.write(resposta_texto)

# Exibir tabela com perguntas e respostas
st.table(df)
