import streamlit as st
import requests

# Interface do usuário
st.markdown("<h1 style='text-align: center; color: #00274D;'>💬 Chatbot Galdí</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Bem-vindo ao Chatbot Galdí!</p>", unsafe_allow_html=True)

# URL completa do Watson Assistant, incluindo chave de API, a partir do `secrets.toml`
url_base = st.secrets["watson_url"]

# Função para iniciar uma sessão
def iniciar_sessao():
    headers = {"Content-Type": "application/json"}
    response = requests.post(url_base, headers=headers)
    
    if response.status_code == 201:
        return response.json().get("session_id")
    else:
        st.error("Erro ao iniciar a sessão. Verifique a URL completa.")
        return None

# Função para enviar mensagem ao Watson Assistant
def enviar_mensagem(session_id, mensagem):
    headers = {"Content-Type": "application/json"}
    mensagem_url = f"{url_base}/{session_id}/message"
    payload = {
        "input": {
            "text": mensagem
        }
    }
    response = requests.post(mensagem_url, headers=headers, json=payload)
    
    if response.status_code == 200:
        return response.json()["output"]["generic"][0]["text"]
    else:
        st.error("Erro ao enviar a mensagem para o Watson Assistant.")
        return None

# Criar uma sessão de chat com o Watson Assistant
session_id = iniciar_sessao()

if session_id:
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Exibir o histórico de mensagens
    for msg in st.session_state.messages:
        st.write(f"{msg['role']}: {msg['content']}")

    # Caixa de entrada do usuário
    user_input = st.text_input("Digite sua mensagem:", "")
    if st.button("Enviar") and user_input:
        st.session_state.messages.append({"role": "Você", "content": user_input})
        resposta = enviar_mensagem(session_id, user_input)
        
        if resposta:
            st.session_state.messages.append({"role": "Galdí", "content": resposta})
            st.write(f"Galdí: {resposta}")
