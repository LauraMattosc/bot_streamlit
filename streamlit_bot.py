import streamlit as st
import pandas as pd
from sentence_transformers import SentenceTransformer, util

def adicionar_pergunta_resposta(pergunta, resposta):
    global df
    nova_linha = pd.DataFrame({'Pergunta': [pergunta], 'Resposta': [resposta]})
    df = pd.concat([df, nova_linha], ignore_index=True)

# Inicializar o modelo BERT em português
model = SentenceTransformer('neuralmind/bert-base-portuguese-cased')

st.title("Chatbot")

# Exemplo de perguntas e respostas
exemplos = [
    {'Pergunta': 'Qual é o seu nome?', 'Resposta': 'Meu nome é Chatbot.'},
    {'Pergunta': 'Qual é o seu propósito?', 'Resposta': 'Meu propósito é responder às suas perguntas e ajudá-lo.'},
    {'Pergunta': 'Você pode me dizer a hora?', 'Resposta': 'Infelizmente, não consigo verificar a hora atual.'},
    {'Pergunta': 'Quem é o presidente do Brasil?', 'Resposta': 'Lula.'},
    {'Pergunta': 'Qual é a capital do Brasil?', 'Resposta': 'A capital do Brasil é Brasília.'},
    {'Pergunta': 'O que é inteligência artificial?', 'Resposta': 'Inteligência artificial é uma área da ciência da computação que busca criar máquinas e sistemas capazes de aprender e tomar decisões.'},
    {'Pergunta': 'Como está o tempo hoje?', 'Resposta': 'Não consigo verificar a previsão do tempo. Por favor, consulte um site de previsão do tempo.'},
    {'Pergunta': 'Quem é o autor de Dom Casmurro?', 'Resposta': 'O autor de Dom Casmurro é Machado de Assis.'},
    {'Pergunta': 'O que é o efeito estufa?', 'Resposta': 'O efeito estufa é um fenômeno natural em que gases na atmosfera retêm o calor, mantendo a temperatura da Terra estável. No entanto, a emissão excessiva de gases de efeito estufa por atividades humanas tem causado um aquecimento global preocupante.'},
    {'Pergunta': 'Qual é a moeda do Brasil?', 'Resposta': 'A moeda do Brasil é o Real.'},
    {'Pergunta': 'Quem pintou o quadro "A Última Ceia"?', 'Resposta': 'Leonardo da Vinci pintou "A Última Ceia".'},
    {'Pergunta': 'O que é fotossíntese?', 'Resposta': 'Fotossíntese é o processo pelo qual as plantas, algas e algumas bactérias convertem energia luminosa em energia química, produzindo glicose e oxigênio a partir de dióxido de carbono e água.'},
]


# Criar DataFrame inicial com as perguntas de exemplo
df = pd.DataFrame(exemplos)

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

# Exibir tabela com perguntas de exemplo
st.table(df)
