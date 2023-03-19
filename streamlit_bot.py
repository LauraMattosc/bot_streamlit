import streamlit as st
from datetime import datetime
import pandas as pd
from sentence_transformers import SentenceTransformer, util

# Inicializar o modelo BERT em português
model = SentenceTransformer('neuralmind/bert-base-portuguese-cased')

st.title("Chatbot")

# Criar DataFrame inicial
colunas = ['Pergunta', 'Resposta']
df = pd.DataFrame(columns=colunas)

# Função para adicionar perguntas e respostas ao DataFrame
def adicionar_pergunta_resposta(pergunta, resposta):
    global df
    nova_linha = {'Pergunta': pergunta, 'Resposta': resposta}
    df = df.append(nova_linha, ignore_index=True)

# Exemplo de perguntas e respostas
exemplos = [
    {'Pergunta': 'Qual é o seu nome?', 'Resposta': 'Meu nome é Chatbot.'},
    {'Pergunta': 'Qual é o seu propósito?', 'Resposta': 'Meu propósito é responder às suas perguntas e ajudá-lo.'},
    # Adicione mais exemplos aqui
]

user_input = st.text_input("Pergunta:", value="")
if user_input:
    # Calcular a similaridade entre a pergunta do usuário e as perguntas de exemplo
    pergunta_embedding = model.encode(user_input, convert_to_tensor=True)
    exemplos_embeddings = model.encode([ex['Pergunta'] for ex in exemplos], convert_to_tensor=True)
    similaridades = util.pytorch_cos_sim(pergunta_embedding, exemplos_embeddings)

    # Encontrar a pergunta de exemplo mais semelhante e usar sua resposta
    resposta_indice = similaridades.argmax().item()
    resposta = exemplos[resposta_indice]['Resposta']

    if resposta:
        adicionar_pergunta_resposta(user_input, resposta)
        st.write(resposta)

# Exibir tabela com perguntas e respostas
st.table(df)
