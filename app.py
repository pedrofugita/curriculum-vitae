import streamlit as st

# Configuração da página
st.set_page_config(page_title="Pedro | Desenvolvedor", page_icon="💻", layout="wide")

# CSS para remover menus padrões e deixar mais limpo
st.markdown("""
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# Sidebar com informações de contato
with st.sidebar:
    st.title("Pedro")
    st.write("📍 Brasil")
    st.markdown("### Contatos")
    st.markdown("📧 [Email](mailto:seuemail@exemplo.com)")
    st.markdown("👔 [LinkedIn](https://www.linkedin.com/)")
    st.markdown("🐙 [GitHub](https://github.com/)")

# Corpo principal
st.title("Pedro")
st.subheader("Desenvolvedor Python & Entusiasta de Hardware")

st.write("""
Olá! Sou um desenvolvedor focado em Python e automação. 
Tenho experiência prática com scripts, manutenção de hardware e estou estudando frameworks web como Django.
""")

st.divider()

col1, col2 = st.columns(2)

with col1:
    st.header("🛠️ Habilidades")
    st.write("**Python & Automação**")
    st.progress(80)
    st.write("**Django Framework**")
    st.progress(60)
    st.write("**Hardware & Manutenção**")
    st.progress(90)
    st.write("**HTML/CSS**")
    st.progress(40)

with col2:
    st.header("🚀 Projetos")
    st.info("**Script de Automação**\n\nCódigo em Python para automatizar tarefas repetitivas.")
    st.info("**Currículo Digital**\n\nEsta página web, construída inteiramente com Python e Streamlit.")

st.divider()
st.caption("Desenvolvido por Pedro com Streamlit 🎈")