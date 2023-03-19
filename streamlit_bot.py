import streamlit as st
from datetime import datetime
import pandas as pd

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
    resposta = ""
    if "qual é o seu nome?" in user_input.lower():
        resposta = "Bot: Meu nome é Bot, prazer em conhecê-lo(a)!"
    elif "como está o tempo hoje?" in user_input.lower():
        resposta = "Bot: Desculpe, não sou capaz de verificar o tempo. Você pode tentar procurar online."
    elif "que horas são?" in user_input.lower():
        resposta = "Bot: A hora atual é {0}.".format(datetime.now().strftime("%H:%M"))
    elif "qual é a sua função?" in user_input.lower():
        resposta = "Bot: Minha função é ajudar e responder às perguntas da melhor maneira possível."
    elif "o que você faz?" in user_input.lower():
        resposta = "Bot: Sou um chatbot projetado para responder perguntas e fornecer informações."
    else:
        resposta = "Bot: Desculpe, não entendi. Você pode tentar me fazer outra pergunta?"

    if resposta:
        adicionar_pergunta_resposta(user_input, resposta)
        st.write(resposta)

# Exibir tabela com perguntas e respostas
st.table(df)
