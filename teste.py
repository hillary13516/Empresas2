import streamlit as st
import base64

# CONFIG
st.set_page_config(page_title="Empresas Parceiras", layout="wide")

# FUNÇÃO PARA CONVERTER IMAGEM
def get_base64_image(path):
    with open(path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# IMAGENS
spacex_img = get_base64_image("Spacex.png")
apple_img = get_base64_image("apple.png")
netflix_img = get_base64_image("netflix.png")

# TÍTULO
st.markdown(
    """
    <h1 style='text-align:center; color:white; margin-bottom:40px;'>
        🌐 Empresas Parceiras
    </h1>
    """,
    unsafe_allow_html=True
)

# COLUNAS
col1, col2, col3 = st.columns(3)

# =========================
# SPACEX
# =========================
with col1:
    st.markdown(
        f"""
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

            <h2 style="color:white;">🚀 SpaceX</h2>

            <p style="
                color:#d1d5db;
                font-size:16px;
                line-height:1.6;
            ">
                Empresa aeroespacial criada por Elon Musk.
            </p>

            <a href="https://www.spacex.com/" target="_blank">
                <button style="
                    background-color:#2563eb;
                    color:white;
                    border:none;
                    padding:10px 20px;
                    border-radius:8px;
                    cursor:pointer;
                ">
                    Acessar Site
                </button>
            </a>

        </div>
        """,
        unsafe_allow_html=True
    )

# =========================
# APPLE
# =========================
with col2:
    st.markdown(
        f"""
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

            <h2 style="color:white;">🍎 Apple</h2>

            <p style="
                color:#d1d5db;
                font-size:16px;
                line-height:1.6;
            ">
                Empresa referência mundial em tecnologia.
            </p>

            <a href="https://www.apple.com/br/" target="_blank">
                <button style="
                    background-color:#2563eb;
                    color:white;
                    border:none;
                    padding:10px 20px;
                    border-radius:8px;
                    cursor:pointer;
                ">
                    Acessar Site
                </button>
            </a>

        </div>
        """,
        unsafe_allow_html=True
    )

# =========================
# NETFLIX
# =========================
with col3:
    st.markdown(
        f"""
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

            <h2 style="color:white;">🎬 Netflix</h2>

            <p style="
                color:#d1d5db;
                font-size:16px;
                line-height:1.6;
            ">
                Plataforma de streaming de filmes e séries.
            </p>

            <a href="https://www.netflix.com/br/" target="_blank">
                <button style="
                    background-color:#2563eb;
                    color:white;
                    border:none;
                    padding:10px 20px;
                    border-radius:8px;
                    cursor:pointer;
                ">
                    Acessar Site
                </button>
            </a>

        </div>
        """,
        unsafe_allow_html=True
    )
