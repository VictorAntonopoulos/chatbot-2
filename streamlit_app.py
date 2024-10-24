import streamlit as st
from openai import OpenAI

# Custom CSS for centering and styling
st.markdown("""
    <style>
    .title {
        font-size: 3rem;
        color: #003366; /* Azul escuro */
        text-align: center;
        font-weight: bold;
        margin-bottom: 20px;
    }
    .description {
        text-align: center;
        font-size: 1.2rem;
        margin-bottom: 30px;
    }
    .footer {
        text-align: center;
        margin-top: 50px;
        font-size: 0.9rem;
        color: #888;
    }
    </style>
""", unsafe_allow_html=True)

# Título e descrição alinhados ao centro
st.markdown('<div class="title">💬 Chatbot Galdí</div>', unsafe_allow_html=True)
st.markdown('<div class="description">Bem-vindo ao Chatbot Galdí!</div>', unsafe_allow_html=True)

# Acessar a chave de API diretamente do Streamlit Secrets
openai_api_key = st.secrets["openai_api_key"]

if not openai_api_key:
    st.info("Por favor, adicione sua chave de API OpenAI nas configurações de segredos.", icon="🗝️")
else:
    # Criar cliente OpenAI
    client = OpenAI(api_key=openai_api_key)

    # Criar uma variável de estado de sessão para armazenar as mensagens
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Exibir as mensagens existentes
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Campo de entrada para o usuário digitar uma mensagem
    if prompt := st.chat_input("Digite sua mensagem:"):
        # Armazenar e exibir a mensagem do usuário
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Gerar resposta usando a API OpenAI
        stream = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        )

        # Exibir a resposta do chatbot
        with st.chat_message("assistant"):
            response = st.write_stream(stream)
        st.session_state.messages.append({"role": "assistant", "content": response})

# Rodapé alinhado ao centro
st.markdown('<div class="footer">Desenvolvido por GAID</div>', unsafe_allow_html=True)
