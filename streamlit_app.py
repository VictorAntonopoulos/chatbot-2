import streamlit as st
import requests

# Configurações da Interface
st.markdown("<h1 style='text-align: center; color: #00274D;'>💬 Chatbot Galdí</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Bem-vindo ao Chatbot Galdí!</p>", unsafe_allow_html=True)

# Definindo a URL do Watson Assistant e a API Key dos segredos
assistant_url = "https://api.au-syd.assistant.watson.cloud.ibm.com/v2/assistants/c6aabe50-9141-4f22-ba88-11e236849fd9/sessions"
api_key = st.secrets["watson_api_key"]

# Função para iniciar sessão
def start_session():
    response = requests.post(
        f"{assistant_url}/sessions",
        auth=("apikey", api_key),
        headers={"Content-Type": "application/json"}
    )
    if response.status_code == 201:
        return response.json().get("session_id")
    else:
        st.error("Erro ao iniciar a sessão. Verifique a chave API e a URL.")
        return None

# Função para obter resposta do assistente
def get_assistant_response(session_id, user_input):
    response = requests.post(
        f"{assistant_url}/sessions/{session_id}/message",
        json={"input": {"message_type": "text", "text": user_input}},
        auth=("apikey", api_key),
        headers={"Content-Type": "application/json"}
    )
    if response.status_code == 200:
        return response.json().get("output", {}).get("generic", [{}])[0].get("text")
    elif response.status_code == 404:  # Caso a sessão expire
        st.warning("Sessão expirada. Reiniciando a sessão...")
        session_id = start_session()
        if session_id:
            st.session_state["session_id"] = session_id
            return get_assistant_response(session_id, user_input)
    else:
        st.error("Erro ao obter resposta. Tente novamente.")
        return None

# Inicializar sessão de mensagens e ID de sessão
if "session_id" not in st.session_state:
    st.session_state["session_id"] = start_session()

if "messages" not in st.session_state:
    st.session_state.messages = []

# Exibe mensagens anteriores
for message in st.session_state.messages:
    st.write(f"{message['role']}: {message['content']}")

# Campo de entrada para o usuário
if prompt := st.chat_input("Digite sua mensagem:"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.write(f"Você: {prompt}")

    # Gera resposta do Watson Assistant
    assistant_response = get_assistant_response(st.session_state["session_id"], prompt)
    if assistant_response:
        st.write(f"Galdí: {assistant_response}")
        st.session_state.messages.append({"role": "assistant", "content": assistant_response})
    else:
        st.write("Desculpe, não consegui entender. Tente novamente.")
