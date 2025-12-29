import streamlit as st
from PIL import Image
from datetime import date

# ================== CONFIGURAÇÃO DA PÁGINA ==================
st.set_page_config(
    page_title="Pedro Fugita - Currículo Profissional",
    page_icon="✈️",
    layout="wide"
)

# ================== CSS GLOBAL ==================
st.markdown("""
<style>

/* Fonte moderna */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

/* Justificar parágrafos e textos gerais */
.stMarkdown p, .stText {
    text-align: justify;
}

/* Caso queira justificar todo o conteúdo do app */
.main .block-container {
    text-align: justify;
}
/* Fundo geral */
.stApp {
    background: rgb(0,0,0)
    
}

/* Remove menu e footer */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}

/* ================= SIDEBAR ================= */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #020617, #020617);
    border-right: 1px solid rgba(255,255,255,0.06);
}

/* Foto de perfil */
[data-testid="stSidebar"] [data-testid="stImage"] img {
    border-radius: 50%;
    border: 4px solid #3776AB;
    object-fit: cover;
    box-shadow: 0 0 0 6px rgba(55,118,171,0.15),
                0 20px 40px rgba(0,0,0,0.6);
}

/* Nome */
[data-testid="stSidebar"] h2 {
    font-weight: 700;
    letter-spacing: -0.5px;
}

/* Texto secundário */
[data-testid="stSidebar"] p {
    color: #94a3b8;
}

/* Remove sublinhado dos links */
a {
    text-decoration: none;
}

/* ================= SOCIAL LINKS ================= */
.social-links {
    display: flex;
    justify-content: center;
    gap: 16px;
    margin-top: 12px;
}

.social-links a {
    width: 64px;
    height: 64px;
    border-radius: 16px;
    background: rgba(15, 23, 42, 0.6);
    backdrop-filter: blur(8px);
    display: flex;
    align-items: center;
    justify-content: center;
    border: 1px solid rgba(255,255,255,0.08);
    box-shadow: 0 12px 30px rgba(0,0,0,.45);
    transition: all .25s ease;
}

.social-links a:hover {
    transform: translateY(-4px) scale(1.05);
    box-shadow: 0 0 0 2px rgba(55,118,171,.4),
                0 18px 40px rgba(0,0,0,.8);
}

.social-links img {
    width: 34px;
    height: 34px;
}

/* ================= TÍTULOS ================= */
h1 {
    font-weight: 800;
    letter-spacing: -1px;
}

h2, h3 {
    font-weight: 700;
    letter-spacing: -0.5px;
}

/* Espaçamento geral */
section[data-testid="stVerticalBlock"] {
    gap: 1.5rem;
}

/* Ajuste de Tabs */
button[data-baseweb="tab"] {
    font-size: 16px;
    font-weight: 600;
}

</style>
""", unsafe_allow_html=True)

# ================== SIDEBAR ==================
with st.sidebar:

    col_esq, col_centro, col_dir = st.columns([1, 10, 1])
    with col_centro:
        try:
            image = Image.open("foto-perfil.JPG")
            st.image(image)
        except:
            st.write("")

    st.markdown("<h2 style='text-align: center;'>Pedro Henrique<br>Fugita Bóis</h2>", unsafe_allow_html=True)

    data_nascimento = date(1998, 10, 16)
    hoje = date.today()
    idade = hoje.year - data_nascimento.year - ((hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day))
    st.markdown(f"<p style='text-align: center;'><i>{idade} anos</i></p>", unsafe_allow_html=True)

    st.write("---")

    st.write("📍 Botucatu - SP")
    st.write("📧 [pedrofugita98@gmail.com](mailto:pedrofugita98@gmail.com)")
    st.write("📱 +55 17 99635-5383")

    st.markdown("""
    <div class="social-links">
        <a href="https://github.com/pedrofugita" target="_blank">
            <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/24/Github_logo_svg.svg/960px-Github_logo_svg.svg.png?20230420150203">
        </a>
        <a href="https://www.linkedin.com/in/pedro-fugita/" target="_blank">
            <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linkedin/linkedin-original.svg">
        </a>
        <a href="https://instagram.com/fgtdesign" target="_blank">
            <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/95/Instagram_logo_2022.svg/512px-Instagram_logo_2022.svg.png">
        </a>
    </div>
    """, unsafe_allow_html=True)

    st.write("---")
    # st.caption("Download CV (Em breve)")

# ================== ÁREA PRINCIPAL ==================
st.title("Engenheiro Mecânico & Dados ⚙️💻")
st.subheader("Automação Industrial | Dados & I.A. | Full Stack Development")

st.markdown("""
Engenheiro Mecânico pela Unesp com foco em **automação industrial** e **soluções digitais** voltadas ao aumento de produtividade. 
Experiência prática na criação de sistemas automatizados, integração de plataformas digitais e aplicação de inteligência artificial em produção.

Atuo na ponte entre a engenharia tradicional e a engenharia moderna, desenvolvendo pipelines de dados (ETL), dashboards analíticos para tomadas de decisões e scripts para eficiência operacional.
""")

st.divider()

st.header("🛠️ Hardskills")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("#### 💻 Linguagens")
    st.markdown("""
- **Python** (Avançado)
- **SQL** (PostgreSQL)
- **C++ / Octave**
- **LaTeX**
- **HTML/CSS/JS**
""")

with col2:
    st.markdown("#### 🧠 IA & Dados")
    st.markdown("""
- **Visão Comp. (YOLO/OpenCV)**
- **Pandas & NumPy**
- **ETL Pipelines**
- **Power BI & Plotly**
- **LLMs (Gemini/OpenAI)**
""")

with col3:
    st.markdown("#### 🌐 Web & Backend")
    st.markdown("""
- **Django & Flask**
- **FastAPI**
- **Selenium**
- **Bitbucket**
- **Git**
""")

with col4:
    st.markdown("#### ⚙️ Prototipagem")
    st.markdown("""
- **CATIA V5**
- **SolidWorks**
- **Ansys**
- **AutoCAD**
- **Impressão 3D**
""")

st.divider()

st.header("💼 Experiência Profissional")

with st.expander("✈️ Embraer | *2024 - 2025*"):#, expanded=True):
    st.markdown("""
*Engenharia de Manufatura de Peças Estampadas*
- Desenvolvimento de softwares para **automação** de processos de produção e engenharia.
- Aplicação de **Inteligência Artificial** em chatbots e visão computacional para ganho de eficiência e qualidade.
- Criação de **pipelines de dados (ETL)** para análise preditiva por meio de interfaces gráficas de gestão.
- Análise de *dados* e integração de plataformas digitais industriais.
- Melhoria de *projetos* de equipamentos industriais.
- Interface com fornecedores e outras áreas dentro e fora da engenharia.
""")
    st.image("embraer.jpg")

with st.expander("🛠️ VFG Engenharia | *2021*"):
    st.markdown("""
*Engenharia de Projeto*
- Modelagem e simulação 3D (CAD/CAM).
- Acompanhamento de produção de projeto e entrega de uma perfuratriz rotativa elétrica para perfuração de polos artesianos.
""")

with st.expander("🎨 FGT Design  | *2020 - Atual*"):
    st.markdown("""
*Designer Gráfico*
- Comunicação visual.
- Gestão de projetos.
- Visão de produto.
- Interface com o público.
- Empreendedorismo
""")

st.divider()

# ================== PROJETOS ==================
st.header("💡 Projetos em Destaque")

tab_proj1, tab_proj2, tab_proj3, tab_proj4, tab_proj5, tab_proj6 = st.tabs(["Visão Computacional", "Dashboard Pessoal", "Crypto Agent", "Previsão de Crédito IA", "API", "FGT Design"])

with tab_proj1:
    st.subheader("Visão Computacional")
    col_a1, col_a2 = st.columns([2, 1])
    with col_a1:
        st.write("""
Detecção de objetos em tempo real utilizando o Ultralytics YOLOv8, desenvolvido como uma Prova de Conceito (PoC) para soluções de monitoramento automatizado em ambientes industriais, de varejo e cidades inteligentes (smart cities).

O sistema processa fluxos de vídeo quadro a quadro (frame a frame) e gera detecções em tempo real com caixas delimitadoras (bounding boxes), classes e pontuações de confiança (confidence scores)."
""")
        st.success("Status: Funcional")
    with col_a2:
        st.image("https://raw.githubusercontent.com/pedrofugita/computer-vision-yolo/refs/heads/main/media/video_planta.png")

with tab_proj2:
    st.subheader("Dashboard Pessoal")
    col_b1, col_b2 = st.columns([2, 1])
    with col_b1:
        st.write("""
Um painel de controle pessoal e interativo desenvolvido com Django para monitoramento de hardware em tempo real, controle de áudio, atalhos tarefas e visualização de dados financeiros e climáticos.
""")
    with col_b2:
        st.success("Status: Funcional")

with tab_proj3:
    st.subheader("Crypto Agent")
    col_c1, col_c2 = st.columns([2, 1])
    with col_c1:
        st.write("""

""")
    with col_c2:
        st.info("Status: Em progresso")

with tab_proj4:
    st.subheader("Previsão de Crédito IA")
    col_d1, col_d2 = st.columns([2, 1])
    with col_d1:
        st.write("""

""")
with col_d2:
    st.info("Status: Em progresso")
    
with tab_proj5:
    st.subheader("API")
    col_e1, col_e2 = st.columns([2, 1])
    with col_e1:
        st.write("""

""")
with col_e2:
    st.info("Status: Em progresso")

with tab_proj6:
    st.subheader("FGT Design")
    col_f1, col_f2 = st.columns([2, 1])
    with col_f1:
        st.write("""

""")
with col_f2:
    st.info("Status: Em progresso")
    
st.divider()
    
st.divider()

# ================== FORMAÇÃO ACADÊMICA (AGORA EM ABAS) ==================
st.header("🎓 Formação Acadêmica")

tab_resumo, tab_sae, tab_ca, tab_pesquisa = st.tabs(["Graduação", "Formula SAE", "Centro Acadêmico", "Pesquisa"])

with tab_resumo:
    st.subheader("Engenharia Mecânica")
    st.markdown("**UNESP** - Universidade Estadual Paulista 'Júlio de Mesquita Filho'")
    st.caption("📍 Ilha Solteira")
    st.write("Bacharelado com sólida formação técnica e experimental desenvolvida em um dos maiores complexos laboratoriais do país. Competências práticas avançadas em Ciências Térmicas (refrigeração, escoamento bifásico e motores), Mecânica dos Sólidos (vibrações, acústica e controle de sistemas inteligentes) e Processos de Fabricação (usinagem CNC, metrologia dimensional, metalografia e conformação plástica). Experiência direta com instrumentação industrial, sistemas CAD/CAM e ensaios mecânicos, além de contato com pesquisas de ponta voltadas à manutenção preditiva, automação e programação. Essa trajetória proporcionou uma visão sistêmica da engenharia, desde a concepção e projeto auxiliado por computador até a manufatura integrada e o controle de estruturas inteligentes.")

with tab_sae:
    col_sae1, col_sae2 = st.columns([3, 1])
    with col_sae1:
        st.subheader("🏎️ Fênix Racing Formula SAE")
        st.write("**Área de Transmissão**")
        st.write("""
        Participação no projeto e manufatura de um protótipo veicular tipo Fórmula.
        - Desenvolvimento e cálculo estrutural do sistema de transmissão.
        - Utilização de softwares CAD/CAE para otimização de performance.
        - Trabalho em equipe multidisciplinar sob prazos rígidos de competição.
        """)
    with col_sae2:
        st.write("") # Espaço para foto se quiser adicionar futuramente

with tab_ca:
    st.subheader("🏛️ Centro Acadêmico 'Ozires Silva'")
    st.write("**Liderança Estudantil**")
    
    st.markdown("🔹 **Presidente**")
    st.caption("Representação dos estudantes, gestão de conflitos e organização institucional.")
    
    st.markdown("🔹 **Diretor de Marketing**")
    st.caption("Coordenação de campanhas de engajamento e comunicação visual.")

with tab_pesquisa:
    st.subheader("🔬 Pesquisa & Desenvolvimento")
    st.markdown("**Aplicações de IA na Engenharia**")
    st.write("""
    Foco acadêmico na intersecção entre Engenharia Mecânica e Ciência da Computação.
    - **Visão Computacional:** Estudos aplicados utilizando YOLO e OpenCV para detecção de objetos em ambientes industriais.
    - **Automação:** Desenvolvimento de scripts para otimização de processos de manufatura.
    """)

st.divider()
# ========================================================================

st.header("🎮🎵🎬⚽ Interesses")
cols = st.columns(4, gap="medium")
with cols[0]:
    st.image("https://i.pinimg.com/originals/f9/95/d5/f995d53ef1d77a2067c035aad239ad2f.gif", width=300)

with cols[1]:
    st.image("https://i.pinimg.com/originals/38/eb/9e/38eb9ef67fe14e68cc516fd025f8d559.gif", width=300)

with cols[3]:
    st.image("https://media.tenor.com/3aCImrMYRX4AAAAM/corinthians.gif", width=120)

with cols[2]:
    st.image("https://i.pinimg.com/originals/f4/75/e1/f475e17d2d74c96d45ac92b14de16da5.gif", width=180)

st.markdown("---")
st.caption("Desenvolvido por Pedro Fugita | Powered by Streamlit & Python 🐍")