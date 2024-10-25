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
        f"{assistant_url}",
        auth=("apikey", api_key),
        headers={"Content-Type": "application/json"}
    )
    session_id = response.json().get("session_id")
    return session_id

# Função para obter resposta do assistente
def get_assistant_response(session_id, user_input):
    response = requests.post(
        f"{assistant_url}/{session_id}/message",
        json={"input": {"message_type": "text", "text": user_input}},
        auth=("apikey", api_key),
        headers={"Content-Type": "application/json"}
    )
    return response.json().get("output", {}).get("generic", [{}])[0].get("text")

# Cria sessão de mensagens
if "session_id" not in st.session_state:
    st.session_state["session_id"] = start_session()

# Exibe mensagens anteriores
if "messages" not in st.session_state:
    st.session_state.messages = []

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
