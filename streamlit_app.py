import streamlit as st
import requests

# Configurações da Interface
st.markdown("<h1 style='text-align: center; color: #00274D;'>💬 Chatbot Galdí</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Bem-vindo ao Chatbot Galdí!</p>", unsafe_allow_html=True)

# Obter as credenciais do Watson a partir do segredo do Streamlit
api_key = st.secrets["watson_api_key"]
url = f"{st.secrets['watson_url']}/v2/assistants/c6aabe50-9141-4f22-ba88-11e236849fd9/sessions"

# Função para iniciar uma sessão
def iniciar_sessao():
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
    }
    response = requests.post(url, headers=headers)
    
    if response.status_code == 201:
        return response.json().get("session_id")
    else:
        st.error("Erro ao iniciar a sessão. Verifique a chave API e a URL.")
        return None

# Função para enviar mensagem ao Watson Assistant
def enviar_mensagem(session_id, mensagem):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
    }
    mensagem_url = f"{url}/{session_id}/message"
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

# Validar a sessão antes de prosseguir
if session_id:
    # Sessão para manter o histórico das mensagens
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Mostrar mensagens de histórico
    for msg in st.session_state.messages:
        st.write(f"{msg['role']}: {msg['content']}")

    # Caixa de entrada do usuário
    user_input = st.text_input("Digite sua mensagem:", "")
    if st.button("Enviar") and user_input:
        # Enviar a mensagem do usuário e exibir a resposta
        st.session_state.messages.append({"role": "Você", "content": user_input})
        resposta = enviar_mensagem(session_id, user_input)
        
        if resposta:
            st.session_state.messages.append({"role": "Galdí", "content": resposta})
            st.write(f"Galdí: {resposta}")
