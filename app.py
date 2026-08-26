import streamlit as st

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(
    page_title="Simulador Fibex Telecom",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- ESTILOS CSS CORPORATIVOS FIBEX TELECOM (AZUL / CIAN) ---
st.markdown("""
    <style>
    /* Fondo general */
    .stApp {
        background-color: #0B132B;
        color: #FFFFFF;
    }
    
    /* Barra lateral */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1C2541 0%, #0B132B 100%);
        border-right: 1px solid #00B4D8;
    }
    
    /* Banner principal con degradado corporativo Fibex */
    .fibex-header {
        background: linear-gradient(135deg, #03045E 0%, #0077B6 50%, #00B4D8 100%);
        padding: 24px;
        border-radius: 12px;
        box-shadow: 0px 4px 15px rgba(0, 180, 216, 0.3);
        margin-bottom: 25px;
        text-align: center;
    }
    .fibex-header h1 {
        color: #FFFFFF !important;
        font-weight: 800;
        font-size: 2.2rem;
        margin: 0;
        letter-spacing: 1px;
    }
    .fibex-header p {
        color: #E0F7FA !important;
        margin-top: 5px;
        font-size: 1.05rem;
    }

    /* Tarjetas de Métricas */
    div[data-testid="stMetric"] {
        background: #1C2541;
        border: 1px solid #00B4D8;
        border-radius: 10px;
        padding: 15px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.2);
    }
    div[data-testid="stMetric"] label {
        color: #90E0EF !important;
        font-size: 0.95rem !important;
        font-weight: 600;
    }
    div[data-testid="stMetric"] div[data-testid="stMetricValue"] {
        color: #FFFFFF !important;
        font-weight: 700;
    }

    /* Botones de radio e inputs */
    .stRadio label {
        color: #FFFFFF !important;
        font-weight: 600;
    }
    
    /* Separadores */
    hr {
        border-color: #00B4D8 !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- HEADER PRINCIPAL CORPORATIVO ---
st.markdown("""
    <div class="fibex-header">
        <h1>FIBEX TELECOM</h1>
        <p>⚡ Simulador Oficial de Comisiones y Metas Quincenales (Boletín N° 022)</p>
    </div>
""", unsafe_allow_html=True)

# --- CANAL DE VENTA ---
canal = st.sidebar.radio(
    "📍 Selecciona tu Área / Canal:",
    ["Ventas Calle / Call Center", "Oficinas (ATC)"]
)

st.sidebar.markdown("---")
st.sidebar.header("📥 Registro de Ventas Quincenales")

# --- CATALOGO DE PLANES HOGAR < $40 (5 PUNTOS C/U) ---
st.sidebar.subheader("1. Planes Hogar Menores a $40 (5 pts)")
planes_menores = {
    "Plan Básico ($20)": 5,
    "Plan Estándar ($25)": 5,
    "Plan Plata ($30)": 5,
    "Plan Oro ($35)": 5
}

v_hogar_menor = 0
puntos_hogar_menor = 0

for plan, pts in planes_menores.items():
    cant = st.sidebar.number_input(f"{plan}", min_value=0, value=0, step=1)
    v_hogar_menor += cant
    puntos_hogar_menor += (cant * pts)

# --- CATALOGO DE PLANES HOGAR >= $40 (PUNTOS VARIABLES) ---
st.sidebar.subheader("2. Planes Hogar Iguales o Mayores a $40")
planes_mayores = {
    "Gamer Medio ($40) - 10 pts": 10,
    "Conectados Full ($45) - 12 pts": 12,
    "Familiar Full ($45) - 12 pts": 12,
    "Cinéfilos XFull ($50) - 13 pts": 13,
    "Gamer Full ($50) - 13 pts": 13,
    "Conectados XFull ($55) - 14 pts": 14,
    "Gamer XFull ($60) - 15 pts": 15,
    "Familiar XFull ($60) - 15 pts": 15,
}

v_hogar_mayor_40 = 0
puntos_hogar_mayor = 0

for plan, pts in planes_mayores.items():
    cant = st.sidebar.number_input(f"{plan}", min_value=0, value=0, step=1)
    v_hogar_mayor_40 += cant
    puntos_hogar_mayor += (cant * pts)

total_ventas_hogar = v_hogar_menor + v_hogar_mayor_40
total_puntos_hogar = puntos_hogar_menor + puntos_hogar_mayor

# --- PRODUCTOS ADICIONALES ---
st.sidebar.subheader("3. Servicios Adicionales / Corporativos")
v_pyme = st.sidebar.number_input("Ventas PYME (15 pts)", min_value=0, value=0, step=1)
v_rcv = st.sidebar.number_input("Ventas RCV (3 pts)", min_value=0, value=0, step=1)
v_upselling = st.sidebar.number_input("Ventas UPSELLING (4 pts)", min_value=0, value=0, step=1)

puntos_pyme = v_pyme * 15
puntos_rcv = v_rcv * 3
puntos_upselling = v_upselling * 4

total_puntos_base = total_puntos_hogar + puntos_pyme + puntos_rcv + puntos_upselling

# --- LÓGICA DE VALIDACIÓN ---
if canal == "Ventas Calle / Call Center":
    opc1 = total_ventas_hogar >= 15
    opc2 = (total_ventas_hogar >= 10) and (v_pyme >= 1)
    opc3 = v_hogar_mayor_40 >= 5
    opc4 = v_pyme >= 8
    opc5 = (total_ventas_hogar >= 10) and (v_rcv >= 4)
    opc6 = (total_ventas_hogar >= 10) and (v_upselling >= 5)
else:  # Oficinas (ATC)
    opc1 = total_ventas_hogar >= 8
    opc2 = (total_ventas_hogar >= 6) and (v_pyme >= 1)
    opc3 = v_hogar_mayor_40 >= 3
    opc4 = v_pyme >= 4
    opc5 = (total_ventas_hogar >= 6) and (v_rcv >= 4)
    opc6 = (total_ventas_hogar >= 6) and (v_upselling >= 5)

califica = opc1 or opc2 or opc3 or opc4 or opc5 or opc6

# --- CATEGORÍA Y MULTIPLICADOR ---
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

# --- CÁLCULO FINAL ---
puntos_bonificados = total_puntos_base * pct_bono
total_puntos_finales = total_puntos_base + puntos_bonificados if califica else 0

# --- RESULTADOS Y DASHBOARD ---
st.markdown("### 🎯 Estado de Calificación Quincenal")

if califica:
    st.success(f"¡FELICIDADES! Calificas para cobrar comisiones en el canal **{canal}**.")
    opciones_cumplidas = []
    if opc1: opciones_cumplidas.append("Opción 1 (Ventas Hogar Totales)")
    if opc2: opciones_cumplidas.append("Opción 2 (Hogar + PYME)")
    if opc3: opciones_cumplidas.append("Opción 3 (Ventas ≥ $40)")
    if opc4: opciones_cumplidas.append("Opción 4 (PYME Totales)")
    if opc5: opciones_cumplidas.append("Opción 5 (Hogar + RCV)")
    if opc6: opciones_cumplidas.append("Opción 6 (Hogar + UPSELLING)")
    
    st.info(f" Cumples con: **{', '.join(opciones_cumplidas)}**")
else:
    st.error(f"❌ AÚN NO ALCANZAS EL UMBRAL DE CALIFICACIÓN PARA **{canal.upper()}**.")

st.markdown("---")
st.markdown("### 📊 Métricas de Rendimiento")

m1, m2, m3, m4 = st.columns(4)
m1.metric("Ventas Hogar Totales", f"{total_ventas_hogar}")
m2.metric("Puntos Base Acumulados", f"{total_puntos_base} pts")
m3.metric("Categoría de Bono", f"{categoria} (+{int(pct_bono*100)}%)")
m4.metric("💰 ESTIMADO A COBRAR", f"${total_puntos_finales:.2f} Ref")

if califica and pct_bono > 0:
    st.balloons()
    st.success(f"🔥 ¡Excelente gestión! Tu categoría **{categoria}** te otorga un **+{int(pct_bono*100)}%** extra sobre el total de tus puntos.")
