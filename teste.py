import streamlit as st
import base64

# CONFIGURAÇÃO
st.set_page_config(page_title="Empresas Parceiras", layout="wide")

# FUNÇÃO PARA CONVERTER IMAGEM EM BASE64
def get_base64_image(path):
    with open(path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# IMAGENS
spacex_img = get_base64_image("Spacex.png")
apple_img = get_base64_image("apple.png")
netflix_img = get_base64_image("netflix.png")

# TÍTULO
st.markdown("""
    <h1 style='text-align:center; color:white; margin-bottom:40px;'>
        🌐 Empresas Parceiras
    </h1>
""", unsafe_allow_html=True)

# COLUNAS
col1, col2, col3 = st.columns(3)

# =========================
# SPACE X
# =========================
with col1:
    st.markdown(f"""
        <div style="
            background-color:#111827;
            padding:20px;
            border-radius:15px;
            text-align:center;
            height:500px;
        ">

            <img src="data:image/png;base64,{spacex_img}" 
                 width="100%"
                 style="border-radius:10px;">

            <h2 style="color:white; margin-top:15px;">
                🚀 SpaceX
            </h2>

            <p style="
                color:#d1d5db;
                font-size:16px;
                text-align:justify;
                line-height:1.6;
            ">
                A SpaceX é uma empresa aeroespacial criada por Elon Musk.
                Seu principal objetivo é desenvolver tecnologias para viagens espaciais
                e tornar possível a exploração de Marte.
            </p>

            <a href="https://www.spacex.com/" target="_blank">
                <button style="
                    background-color:#2563eb;
                    color:white;
                    border:none;
                    padding:10px 20px;
                    border-radius:8px;
                    cursor:pointer;
                    margin-top:10px;
                ">
                    Acessar Site
                </button>
            </a>

        </div>
    """, unsafe_allow_html=True)

# =========================
# APPLE
# =========================
with col2:
    st.markdown(f"""
        <div style="
            background-color:#111827;
            padding:20px;
            border-radius:15px;
            text-align:center;
            height:500px;
        ">

            <img src="data:image/png;base64,{apple_img}" 
                 width="100%"
                 style="border-radius:10px;">

            <h2 style="color:white; margin-top:15px;">
                🍎 Apple
            </h2>

            <p style="
                color:#d1d5db;
                font-size:16px;
                text-align:justify;
                line-height:1.6;
            ">
                A Apple é uma das maiores empresas de tecnologia do mundo.
                Ela é conhecida por produtos como iPhone, iPad, MacBook e Apple Watch,
                além de seus sistemas inovadores.
            </p>

            <a href="https://www.apple.com/br/" target="_blank">
                <button style="
                    background-color:#2563eb;
                    color:white;
                    border:none;
                    padding:10px 20px;
                    border-radius:8px;
                    cursor:pointer;
                    margin-top:10px;
                ">
                    Acessar Site
                </button>
            </a>

        </div>
    """, unsafe_allow_html=True)

# =========================
# NETFLIX
# =========================
with col3:
    st.markdown(f"""
        <div style="
            background-color:#111827;
            padding:20px;
            border-radius:15px;
            text-align:center;
            height:500px;
        ">

            <img src="data:image/png;base64,{netflix_img}" 
                 width="100%"
                 style="border-radius:10px;">

            <h2 style="color:white; margin-top:15px;">
                🎬 Netflix
            </h2>

            <p style="
                color:#d1d5db;
                font-size:16px;
                text-align:justify;
                line-height:1.6;
            ">
                A Netflix é uma plataforma de streaming famosa no mundo inteiro.
                Ela oferece filmes, séries, documentários e conteúdos originais
                para milhões de usuários.
            </p>

            <a href="https://www.netflix.com/br/" target="_blank">
                <button style="
                    background-color:#2563eb;
                    color:white;
                    border:none;
                    padding:10px 20px;
                    border-radius:8px;
                    cursor:pointer;
                    margin-top:10px;
                ">
                    Acessar Site
                </button>
            </a>

        </div>
    """, unsafe_allow_html=True)
