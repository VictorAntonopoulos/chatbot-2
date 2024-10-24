import streamlit as st
from openai import OpenAI

# Custom CSS for chat messages and overall style
st.markdown("""
    <style>
    .title {
        font-size: 3rem;
        color: #ff4b4b;
        text-align: center;
        font-weight: bold;
        margin-bottom: 20px;
    }
    .description {
        text-align: center;
        font-size: 1.2rem;
        margin-bottom: 30px;
    }
    .user-message {
        background-color: #d1f7ff;
        padding: 10px;
        border-radius: 10px;
        margin-bottom: 10px;
        font-weight: bold;
        color: #007acc;
    }
    .assistant-message {
        background-color: #e8e8e8;
        padding: 10px;
        border-radius: 10px;
        margin-bottom: 10px;
        font-style: italic;
        color: #333;
    }
    .chat-input {
        margin-top: 20px;
        font-size: 1rem;
        width: 100%;
        padding: 10px;
        border-radius: 10px;
    }
    .footer {
        text-align: center;
        margin-top: 50px;
        font-size: 0.9rem;
        color: #888;
    }
    </style>
""", unsafe_allow_html=True)

# Title and description
st.markdown('<div class="title">💬 Chatbot Galdí</div>', unsafe_allow_html=True)
st.markdown('<div class="description">Bem-vindo ao Chatbot Galdí!</div>', unsafe_allow_html=True)

# Access the OpenAI API key from Streamlit secrets
openai_api_key = st.secrets["openai_api_key"]

if not openai_api_key:
    st.error("Erro: Por favor, adicione sua chave de API do OpenAI no Streamlit Secrets.", icon="🗝️")
else:
    # Create an OpenAI client
    client = OpenAI(api_key=openai_api_key)

    # Create a session state variable to store the chat messages
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display the existing chat messages
    for message in st.session_state.messages:
        if message["role"] == "user":
            st.markdown(f'<div class="user-message">{message["content"]}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="assistant-message">{message["content"]}</div>', unsafe_allow_html=True)

    # Chat input field
    prompt = st.text_input("Digite sua mensagem:", key="chat_input", placeholder="Escreva aqui...", label_visibility="hidden")
    
    # If the user submits a message
    if prompt:
        # Store and display the user's message
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.markdown(f'<div class="user-message">{prompt}</div>', unsafe_allow_html=True)

        # Generate a response from the assistant (OpenAI API)
        stream = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        )

        # Stream the response and display it
        with st.spinner("Galdí está pensando..."):
            response = st.write_stream(stream)
        
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.markdown(f'<div class="assistant-message">{response}</div>', unsafe_allow_html=True)

# Footer
st.markdown('<div class="footer">Desenvolvido por GAID</div>', unsafe_allow_html=True)
