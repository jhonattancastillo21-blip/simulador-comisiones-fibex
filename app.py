import streamlit as st

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(
    page_title="Fibex Telecom - Simulador de Comisiones",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- ESTILOS CSS CON COLORES CORPORATIVOS Y FONDO EXACTO FIBEX ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700;900&display=swap');

    /* Fondo general con degradado exacto de la marca */
    .stApp {
        background: linear-gradient(165deg, #1ca7a6 0%, #0b5b99 35%, #031838 75%, #010a17 100%) !important;
        background-attachment: fixed !important;
        font-family: 'Montserrat', sans-serif !important;
        color: #FFFFFF !important;
    }

    /* Barra Lateral */
    [data-testid="stSidebar"] {
        background: rgba(3, 24, 56, 0.85) !important;
        backdrop-filter: blur(10px);
        border-right: 1px solid rgba(28, 167, 166, 0.4);
    }

    /* Logo y Cabecera Corporativa */
    .fibex-logo-container {
        text-align: center;
        padding: 10px 0 25px 0;
    }
    .fibex-brand {
        font-family: 'Montserrat', sans-serif;
        font-size: 42px;
        font-weight: 900;
        color: #FFFFFF;
        letter-spacing: 5px;
        margin-top: 5px;
        text-shadow: 0 2px 10px rgba(0,0,0,0.3);
    }
    .fibex-subtext {
        font-family: 'Montserrat', sans-serif;
        font-size: 13px;
        font-weight: 700;
        color: #80E3E2;
        letter-spacing: 10px;
        margin-top: -8px;
    }

    /* Tarjetas de Contenido */
    .content-card {
        background: rgba(255, 255, 255, 0.07);
        border: 1px solid rgba(255, 255, 255, 0.15);
        border-radius: 16px;
        padding: 20px;
        backdrop-filter: blur(12px);
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        margin-bottom: 20px;
    }

    /* Metrics de Streamlit */
    div[data-testid="stMetric"] {
        background: rgba(3, 24, 56, 0.6) !important;
        border: 1px solid #1ca7a6 !important;
        border-radius: 12px !important;
        padding: 15px !important;
    }
    div[data-testid="stMetric"] label {
        color: #80E3E2 !important;
        font-size: 0.9rem !important;
        font-weight: 600 !important;
    }
    div[data-testid="stMetric"] div[data-testid="stMetricValue"] {
        color: #FFFFFF !important;
        font-weight: 800 !important;
    }

    /* Radio buttons */
    .stRadio label {
        color: #FFFFFF !important;
        font-weight: 600 !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- HEADER CON LOGO OFICIAL FIBEX ---
st.markdown("""
    <div class="fibex-logo-container">
        <svg width="85" height="85" viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg">
            <g stroke="#FFFFFF" stroke-linecap="round">
                <circle cx="50" cy="50" r="44" stroke-width="2" opacity="0.25"/>
                <path d="M 22,28 C 36,14 64,14 78,28 C 64,42 36,42 22,28 Z" stroke-width="4" fill="white" opacity="0.95"/>
                <path d="M 12,50 C 30,30 70,30 88,50 C 70,70 30,70 12,50 Z" stroke-width="4.5" fill="white" opacity="0.98"/>
                <path d="M 22,72 C 36,58 64,58 78,72 C 64,86 36,86 22,72 Z" stroke-width="4" fill="white" opacity="0.95"/>
            </g>
        </svg>
        <div class="fibex-brand">FIBEX</div>
        <div class="fibex-subtext">TELECOM</div>
    </div>
""", unsafe_allow_html=True)

# --- SELECCIÓN PRINCIPAL DE CANAL ---
st.markdown('<div class="content-card">', unsafe_allow_html=True)
canal = st.radio(
    "📌 **SELECCIONA TU ÁREA DE TRABAJO:**",
    ["Oficinas (ATC)", "Ventas Calle / Call Center"],
    horizontal=True,
    key="canal_selector"
)
st.markdown('</div>', unsafe_allow_html=True)

# --- BARRA LATERAL: INGRESO DE DATOS ---
st.sidebar.header("📋 REGISTRO DE VENTAS")

# 1. Ventas Hogar < $40
st.sidebar.subheader("1. Planes Hogar (< $40)")
planes_menores = {
    "Plan Básico ($20)": "p_20",
    "Plan Estándar ($25)": "p_25",
    "Plan Plata ($30)": "p_30",
    "Plan Oro ($35)": "p_35"
}

v_hogar_menor = 0
for nombre, key_id in planes_menores.items():
    cant = st.sidebar.number_input(f"{nombre} (5 pts)", min_value=0, value=0, step=1, key=key_id)
    v_hogar_menor += cant

puntos_hogar_menor = v_hogar_menor * 5

# 2. Ventas Hogar >= $40
st.sidebar.subheader("2. Planes Hogar (≥ $40)")
planes_mayores = {
    "Gamer Medio ($40) - 10 pts": ("p_40", 10),
    "Conectados Full ($45) - 12 pts": ("p_45c", 12),
    "Familiar Full ($45) - 12 pts": ("p_45f", 12),
    "Cinéfilos XFull ($50) - 13 pts": ("p_50cin", 13),
    "Gamer Full ($50) - 13 pts": ("p_50g", 13),
    "Conectados XFull ($55) - 14 pts": ("p_55", 14),
    "Gamer XFull ($60) - 15 pts": ("p_60g", 15),
    "Familiar XFull ($60) - 15 pts": ("p_60f", 15)
}

v_hogar_mayor_40 = 0
puntos_hogar_mayor = 0
for nombre, (key_id, pts) in planes_mayores.items():
    cant = st.sidebar.number_input(f"{nombre}", min_value=0, value=0, step=1, key=key_id)
    v_hogar_mayor_40 += cant
    puntos_hogar_mayor += (cant * pts)

total_ventas_hogar = v_hogar_menor + v_hogar_mayor_40
total_puntos_hogar = puntos_hogar_menor + puntos_hogar_mayor

# 3. Adicionales
st.sidebar.subheader("3. Servicios Adicionales")
v_pyme = st.sidebar.number_input("Ventas PYME (15 pts)", min_value=0, value=0, step=1, key="v_pyme")
v_rcv = st.sidebar.number_input("Ventas RCV (3 pts)", min_value=0, value=0, step=1, key="v_rcv")
v_upselling = st.sidebar.number_input("Ventas UPSELLING (4 pts)", min_value=0, value=0, step=1, key="v_upsell")

puntos_pyme = v_pyme * 15
puntos_rcv = v_rcv * 3
puntos_upselling = v_upselling * 4

total_puntos_base = total_puntos_hogar + puntos_pyme + puntos_rcv + puntos_upselling

# --- LÓGICA DE VALIDACIÓN ---
if canal == "Oficinas (ATC)":
    req_h_op1, req_h_op2, req_pyme_op2 = 8, 6, 1
    req_h40_op3, req_pyme_op4 = 3, 4
    req_h_op5, req_rcv_op5 = 6, 4
    req_h_op6, req_upsell_op6 = 6, 5
else:
    req_h_op1, req_h_op2, req_pyme_op2 = 15, 10, 1
    req_h40_op3, req_pyme_op4 = 5, 8
    req_h_op5, req_rcv_op5 = 10, 4
    req_h_op6, req_upsell_op6 = 10, 5

opc1 = total_ventas_hogar >= req_h_op1
opc2 = (total_ventas_hogar >= req_h_op2) and (v_pyme >= req_pyme_op2)
opc3 = v_hogar_mayor_40 >= req_h40_op3
opc4 = v_pyme >= req_pyme_op4
opc5 = (total_ventas_hogar >= req_h_op5) and (v_rcv >= req_rcv_op5)
opc6 = (total_ventas_hogar >= req_h_op6) and (v_upselling >= req_upsell_op6)

califica = opc1 or opc2 or opc3 or opc4 or opc5 or opc6

# --- CATEGORÍA ---
if canal == "Oficinas (ATC)":
    if total_ventas_hogar >= 30: categoria, pct_bono = "SUPER ESTRELLAS", 0.45
    elif total_ventas_hogar >= 23: categoria, pct_bono = "ÉLITE", 0.40
    elif total_ventas_hogar >= 17: categoria, pct_bono = "PRO", 0.35
    elif total_ventas_hogar >= 11: categoria, pct_bono = "SENIOR", 0.30
    elif total_ventas_hogar >= 6: categoria, pct_bono = "JUNIOR", 0.00
    else: categoria, pct_bono = "BÁSICO", 0.00
else:
    if total_ventas_hogar >= 50: categoria, pct_bono = "SUPER ESTRELLAS", 0.45
    elif total_ventas_hogar >= 41: categoria, pct_bono = "ÉLITE", 0.40
    elif total_ventas_hogar >= 31: categoria, pct_bono = "PRO", 0.35
    elif total_ventas_hogar >= 20: categoria, pct_bono = "SENIOR", 0.30
    elif total_ventas_hogar >= 10: categoria, pct_bono = "JUNIOR", 0.00
    else: categoria, pct_bono = "BÁSICO", 0.00

total_puntos_finales = total_puntos_base * (1 + pct_bono) if califica else 0

# --- ESTATUS DE CALIFICACIÓN ---
st.markdown('<div class="content-card">', unsafe_allow_html=True)
st.subheader("🎯 Estatus de Calificación Quincenal")

if califica:
    st.success(f"¡ENHORABUENA! Estás **CALIFICADO** para comisionar en **{canal}**.")
    cumplidas = []
    if opc1: cumplidas.append("Opción 1 (Ventas Hogar)")
    if opc2: cumplidas.append("Opción 2 (Hogar + PYME)")
    if opc3: cumplidas.append("Opción 3 (Hogar ≥ $40)")
    if opc4: cumplidas.append("Opción 4 (PYME)")
    if opc5: cumplidas.append("Opción 5 (Hogar + RCV)")
    if opc6: cumplidas.append("Opción 6 (Hogar + UPSELLING)")
    st.info(f" Cumples con: **{', '.join(cumplidas)}**")
else:
    st.error(f"❌ AÚN NO ALCANZAS LA META DE CALIFICACIÓN PARA **{canal.upper()}**")
    
    with st.expander("🔍 Ver qué te falta para calificar en esta quincena:"):
        st.write(f"- **Opción 1:** Llevas {total_ventas_hogar}/{req_h_op1} Ventas Hogar")
        st.write(f"- **Opción 2:** Llevas {total_ventas_hogar}/{req_h_op2} Hogar y {v_pyme}/{req_pyme_op2} PYME")
        st.write(f"- **Opción 3:** Llevas {v_hogar_mayor_40}/{req_h40_op3} Ventas Hogar ≥ $40")
        st.write(f"- **Opción 4:** Llevas {v_pyme}/{req_pyme_op4} Ventas PYME")
        st.write(f"- **Opción 5:** Llevas {total_ventas_hogar}/{req_h_op5} Hogar y {v_rcv}/{req_rcv_op5} RCV")
        st.write(f"- **Opción 6:** Llevas {total_ventas_hogar}/{req_h_op6} Hogar y {v_upselling}/{req_upsell_op6} Upselling")

st.markdown('</div>', unsafe_allow_html=True)

# --- PANEL DE RESULTADOS ---
st.markdown('<div class="content-card">', unsafe_allow_html=True)
st.subheader("📊 Resumen de Comisiones")

c1, c2, c3, c4 = st.columns(4)
c1.metric("Total Ventas Hogar", f"{total_ventas_hogar}")
c2.metric("Puntos Base", f"{total_puntos_base} pts")
c3.metric("Categoría Alcantada", f"{categoria} (+{int(pct_bono*100)}%)")
c4.metric("💰 ESTIMADO A COBRAR", f"${total_puntos_finales:.2f} Ref")

if califica and pct_bono > 0:
    st.balloons()
    st.success(f"🔥 ¡Excelente gestión! Bonificas un **+{int(pct_bono*100)}%** adicional sobre todos tus puntos acumulados.")

st.markdown('</div>', unsafe_allow_html=True)
