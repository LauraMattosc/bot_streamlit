import streamlit as st
from datetime import datetime
import pandas as pd
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Inicializar o GPT-2
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")

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
    entrada = tokenizer.encode(user_input, return_tensors="pt")
    saida = model.generate(entrada, max_length=50, num_return_sequences=1, no_repeat_ngram_size=2, temperature=0.7)
    resposta = tokenizer.decode(saida[0], skip_special_tokens=True)

    if resposta:
        adicionar_pergunta_resposta(user_input, resposta)
        st.write(resposta)

# Exibir tabela com perguntas e respostas
st.table(df)
