import streamlit as st
import time

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(
    page_title="Fibex Telecom | Dashboard de Comisiones",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- ESTILOS CSS CORPORATIVOS PREMIUM ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700;900&display=swap');

    /* Fondo general con degradado oficial Fibex */
    .stApp {
        background: linear-gradient(165deg, #010a17 0%, #031838 35%, #0b5b99 75%, #1ca7a6 100%) !important;
        background-attachment: fixed !important;
        font-family: 'Montserrat', sans-serif !important;
        color: #FFFFFF !important;
    }

    /* Barra Lateral Premium */
    [data-testid="stSidebar"] {
        background: rgba(2, 14, 33, 0.95) !important;
        backdrop-filter: blur(15px);
        border-right: 1px solid rgba(28, 167, 166, 0.3);
    }

    /* Subtítulo del Header */
    .fibex-subtext {
        font-family: 'Montserrat', sans-serif;
        font-size: 15px;
        font-weight: 700;
        color: #80E3E2;
        text-align: center;
        letter-spacing: 2px;
        margin-top: -15px;
        margin-bottom: 35px;
        font-style: italic;
        text-transform: uppercase;
    }

    /* Estilo de las Métricas (Tarjetas de resultados) */
    div[data-testid="stMetric"] {
        background: rgba(3, 24, 56, 0.7) !important;
        border: 1px solid rgba(28, 167, 166, 0.5) !important;
        border-radius: 12px !important;
        padding: 20px !important;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
        transition: transform 0.2s ease-in-out;
    }
    div[data-testid="stMetric"]:hover {
        transform: translateY(-3px);
        border: 1px solid #80E3E2 !important;
    }
    div[data-testid="stMetric"] label {
        color: #80E3E2 !important;
        font-size: 1rem !important;
        font-weight: 600 !important;
    }
    div[data-testid="stMetric"] div[data-testid="stMetricValue"] {
        color: #FFFFFF !important;
        font-weight: 900 !important;
        font-size: 2.2rem !important;
    }

    /* Separadores nativos */
    hr {
        border-color: rgba(28, 167, 166, 0.3) !important;
        margin-top: 2rem !important;
        margin-bottom: 2rem !important;
    }

    /* ANIMACIÓN DE MANOS APLAUDIENDO */
    @keyframes clapBounce {
        0% { transform: scale(1) rotate(0deg); }
        25% { transform: scale(1.2) rotate(-10deg); }
        50% { transform: scale(1) rotate(0deg); }
        75% { transform: scale(1.2) rotate(10deg); }
        100% { transform: scale(1) rotate(0deg); }
    }
    .clapping-hands {
        display: inline-block;
        animation: clapBounce 0.5s infinite ease-in-out;
    }

    /* VENTANA POP-UP DE CELEBRACIÓN (AUTO-DESAPARECE EN 5 SEGUNDOS) */
    @keyframes modalPopup5s {
        0% { opacity: 0; transform: translate(-50%, -50%) scale(0.8); }
        8% { opacity: 1; transform: translate(-50%, -50%) scale(1.05); }
        12% { opacity: 1; transform: translate(-50%, -50%) scale(1); }
        88% { opacity: 1; transform: translate(-50%, -50%) scale(1); }
        100% { opacity: 0; transform: translate(-50%, -50%) scale(0.8); visibility: hidden; display: none; }
    }

    .celebration-modal {
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        background: linear-gradient(135deg, rgba(2, 14, 33, 0.98) 0%, rgba(3, 24, 56, 0.98) 100%);
        border: 2px solid #1ca7a6;
        border-radius: 20px;
        padding: 40px 30px;
        text-align: center;
        z-index: 999999;
        box-shadow: 0 0 50px rgba(28, 167, 166, 0.5), 0 0 20px rgba(0, 0, 0, 0.8);
        backdrop-filter: blur(20px);
        animation: modalPopup5s 5s forwards;
        pointer-events: none;
        width: 90%;
        max-width: 500px;
    }
    </style>
""", unsafe_allow_html=True)

# --- CABECERA CON LOGO OFICIAL PNG ---
col_head1, col_head2, col_head3 = st.columns([1, 2, 1])
with col_head2:
    try:
        st.image("logo.png", use_container_width=True)
    except:
        st.markdown("<h1 style='text-align: center; color: white; font-weight: 900;'>FIBEX TELECOM</h1>", unsafe_allow_html=True)

# --- FRASE MOTIVACIONAL Y DE GESTIÓN ---
st.markdown('<div class="fibex-subtext">⚡ "Lo que no se mide, no se controla; y lo que no se controla, no se puede mejorar."</div>', unsafe_allow_html=True)

# --- SELECCIÓN PRINCIPAL DE CANAL ---
st.markdown("### 📌 ÁREA DE DESEMPEÑO")
canal = st.radio(
    "Selecciona el canal a evaluar:",
    ["Oficinas (ATC)", "Ventas Calle / Call Center"],
    horizontal=True,
    label_visibility="collapsed"
)

st.divider() # Línea separadora limpia y elegante

# --- BARRA LATERAL: INGRESO DE DATOS ---
st.sidebar.markdown("## 📊 GESTIÓN COMERCIAL")
st.sidebar.caption("Ingresa el volumen de ventas del período.")

# 1. Ventas Hogar < $40 (Según Tarifario)
st.sidebar.markdown("### 1. Planes Hogar (< $40)")
planes_menores = {
    "Conectados Básico ($25) [3 pts]": ("p_25", 3),
    "Cinéfilos Básicos ($30) [8 pts]": ("p_30", 8),
    "Conectados Medio ($35) [9 pts]": ("p_35_c", 9),
    "Familiar Básico ($35) [9 pts]": ("p_35_f", 9)
}

v_hogar_menor = 0
puntos_hogar_menor = 0
for nombre, (key_id, pts) in planes_menores.items():
    cant = st.sidebar.number_input(f"{nombre}", min_value=0, value=0, step=1, key=key_id)
    v_hogar_menor += cant
    puntos_hogar_menor += (cant * pts)

# 2. Ventas Hogar >= $40 (Según Tarifario)
st.sidebar.markdown("### 2. Planes Hogar (≥ $40)")
planes_mayores = {
    "Cinéfilos Medio ($40) [10 pts]": ("p_40_cin", 10),
    "Gamer Medio ($40) [10 pts]": ("p_40_g", 10),
    "Conectados Full ($45) [12 pts]": ("p_45_c", 12),
    "Familiar Full ($45) [12 pts]": ("p_45_f", 12),
    "Cinéfilos XFull ($50) [13 pts]": ("p_50_cin", 13),
    "Gamer Full ($50) [13 pts]": ("p_50_g", 13),
    "Conectados XFull ($55) [14 pts]": ("p_55_c", 14),
    "Gamer XFull ($60) [15 pts]": ("p_60_g", 15),
    "Familiar XFull ($60) [15 pts]": ("p_60_f", 15)
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
st.sidebar.markdown("### 3. Servicios Corporativos / Extras")
v_pyme = st.sidebar.number_input("PYME (15 pts)", min_value=0, value=0, step=1, key="v_pyme")
v_rcv = st.sidebar.number_input("RCV (3 pts)", min_value=0, value=0, step=1, key="v_rcv")
v_upselling = st.sidebar.number_input("UPSELLING (4 pts)", min_value=0, value=0, step=1, key="v_upsell")

puntos_pyme = v_pyme * 15
puntos_rcv = v_rcv * 3
puntos_upselling = v_upselling * 4

total_puntos_base = total_puntos_hogar + puntos_pyme + puntos_rcv + puntos_upselling

# --- LÓGICA DE VALIDACIÓN DE METAS ---
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

# --- CATEGORÍA DE BONIFICACIÓN ---
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
st.markdown("### 🎯 ESTATUS DE CALIFICACIÓN QUINCENAL")

if califica:
    st.success(f"✅ **CALIFICACIÓN APROBADA** | Estás habilitado para el esquema de comisiones en **{canal}**.")
    cumplidas = []
    if opc1: cumplidas.append("Volumen Ventas Hogar (Opción 1)")
    if opc2: cumplidas.append("Mix Hogar + PYME (Opción 2)")
    if opc3: cumplidas.append("Ticket Alto Hogar ≥ $40 (Opción 3)")
    if opc4: cumplidas.append("Volumen PYME (Opción 4)")
    if opc5: cumplidas.append("Mix Hogar + RCV (Opción 5)")
    if opc6: cumplidas.append("Mix Hogar + UPSELLING (Opción 6)")
    
    st.info(f"**Criterios alcanzados:** {', '.join(cumplidas)}")
    
    # --- POP-UP DE CELEBRACIÓN GRANDE (AUTO-DESAPARECE EN 5s) ---
    st.markdown("""
        <div class="celebration-modal">
            <h2 style="color: #80E3E2; margin-bottom: 5px; font-weight: 900; font-family: 'Montserrat', sans-serif; letter-spacing: 1px;">¡META ALCANZADA! 🎉</h2>
            <p style="color: #FFFFFF; font-size: 18px; font-weight: 600; margin-bottom: 20px;">CALIFICACIÓN APROBADA EXITOSAMENTE</p>
            <div style="font-size: 70px; margin: 15px 0;" class="clapping-hands">👏🏼 👏🏼 👏🏼</div>
            <br>
            <img src="https://i.gifer.com/7V7.gif" style="width: 180px; border-radius: 15px; box-shadow: 0 5px 20px rgba(28, 167, 166, 0.4);">
        </div>
        <audio autoplay hidden>
            <source src="https://assets.mixkit.co/active_storage/sfx/2000/2000-preview.mp3" type="audio/mpeg">
        </audio>
    """, unsafe_allow_html=True)

else:
    st.error(f"❌ **META PENDIENTE** | Aún no alcanzas el volumen requerido para calificar en **{canal.upper()}**.")
    
    with st.expander("🔍 Desglose de brecha operativa (Faltante para calificar):"):
        st.markdown(f"""
        - **Opción 1:** Registras **{total_ventas_hogar}** de {req_h_op1} Ventas Hogar.
        - **Opción 2:** Registras **{total_ventas_hogar}**/{req_h_op2} Hogar y **{v_pyme}**/{req_pyme_op2} PYME.
        - **Opción 3:** Registras **{v_hogar_mayor_40}**/{req_h40_op3} Ventas Hogar (Ticket ≥ $40).
        - **Opción 4:** Registras **{v_pyme}**/{req_pyme_op4} Ventas PYME.
        - **Opción 5:** Registras **{total_ventas_hogar}**/{req_h_op5} Hogar y **{v_rcv}**/{req_rcv_op5} RCV.
        - **Opción 6:** Registras **{total_ventas_hogar}**/{req_h_op6} Hogar y **{v_upselling}**/{req_upsell_op6} Upselling.
        """)

st.divider()

# --- PANEL DE RESULTADOS ---
st.markdown("### 📈 PANEL DE CONTROL DE COMISIONES")

c1, c2, c3, c4 = st.columns(4)
c1.metric("Volumen Hogar", f"{total_ventas_hogar}")
c2.metric("Puntuación Base", f"{total_puntos_base} pts")
c3.metric("Rango Alcanzado", f"{categoria} (+{int(pct_bono*100)}%)")
c4.metric("💰 PROYECCIÓN DE PAGO", f"${total_puntos_finales:.2f} Ref")

if califica and pct_bono > 0:
    st.balloons()
    st.success(f"🔥 **¡Excelente gestión comercial!** Tu desempeño en rango **{categoria}** activa un multiplicador del **+{int(pct_bono*100)}%** sobre tu puntuación base.")
