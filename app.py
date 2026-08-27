import streamlit as st
import base64
import os

# --- 1. ARQUITECTURA DE SESIÓN Y CONFIGURACIÓN ---
st.set_page_config(page_title="Fibex Telecom | Portal de Comisiones", page_icon="⚡", layout="wide")

if 'boveda' not in st.session_state:
    st.session_state.boveda = {
        'v_hogar': 0, 'v_h40': 0, 'v_pyme': 0, 'v_rcv': 0, 'v_upsell': 0,
        'pts_hogar': 0, 'pts_pyme': 0, 'pts_rcv': 0, 'pts_upsell': 0
    }

def encode_image(image_path):
    return base64.b64encode(open(image_path, "rb").read()).decode() if os.path.exists(image_path) else ""

img_sofia = encode_image("sofia.png")
img_src = f"data:image/png;base64,{img_sofia}" if img_sofia else "https://cdn-icons-png.flaticon.com/512/4140/4140047.png"

# --- 2. MOTOR UI/UX: GLASSMORPHISM Y FONDO DIFUMINADO CORPORATIVO ---
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;500;700;900&display=swap');

    /* Fondo Difuminado Premium (Aurora Effect) */
    .stApp {{
        background-color: #010a17;
        background-image: 
            radial-gradient(circle at 15% 50%, rgba(28, 167, 166, 0.15), transparent 25%),
            radial-gradient(circle at 85% 30%, rgba(11, 91, 153, 0.2), transparent 25%);
        background-attachment: fixed !important;
        font-family: 'Montserrat', sans-serif !important;
        color: #F8F9FA !important;
    }}

    /* Barra Lateral con Efecto Vidrio (Glassmorphism) */
    [data-testid="stSidebar"] {{
        background: rgba(2, 14, 33, 0.6) !important;
        backdrop-filter: blur(20px) !important;
        -webkit-backdrop-filter: blur(20px) !important;
        border-right: 1px solid rgba(28, 167, 166, 0.15);
    }}

    /* Tarjetas de Métricas Premium */
    div[data-testid="stMetric"] {{
        background: rgba(3, 24, 56, 0.4) !important;
        backdrop-filter: blur(12px);
        border: 1px solid rgba(28, 167, 166, 0.2) !important;
        border-radius: 16px !important;
        padding: 24px !important;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
        transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
    }}
    div[data-testid="stMetric"]:hover {{
        transform: translateY(-5px);
        border: 1px solid rgba(28, 167, 166, 0.8) !important;
        box-shadow: 0 15px 40px rgba(28, 167, 166, 0.2);
    }}
    div[data-testid="stMetric"] label {{ color: #1ca7a6 !important; font-size: 1.1rem !important; font-weight: 700 !important; letter-spacing: 0.5px; }}
    div[data-testid="stMetric"] div[data-testid="stMetricValue"] {{ color: #FFFFFF !important; font-weight: 900 !important; font-size: 2.5rem !important; }}

    /* Textos y Divisores */
    .fibex-tagline {{ text-align: center; font-weight: 700; color: #1ca7a6; font-size: 14px; letter-spacing: 3px; text-transform: uppercase; margin-top: -15px; margin-bottom: 40px; text-shadow: 0 2px 10px rgba(28,167,166,0.3); }}
    hr {{ border-color: rgba(28, 167, 166, 0.15) !important; margin: 2.5rem 0 !important; }}

    /* =========================================
       MOTOR DE ANIMACIONES (Hardware Accelerated)
       ========================================= */
    .sofia-wrapper {{ position: fixed; top: 70px; right: 40px; width: 130px; z-index: 9999; pointer-events: none; }}
    .sofia-img {{ width: 100%; border-radius: 50%; box-shadow: 0 8px 25px rgba(0,0,0,0.5); border: 3px solid #1ca7a6; transition: transform 0.3s ease; }}
    
    @keyframes sofiaJump {{
        0% {{ transform: translateY(0) scale(1); box-shadow: 0 8px 25px rgba(0,0,0,0.5); }}
        10%, 30%, 50%, 70% {{ transform: translateY(-20px) scale(1.15) rotate(4deg); box-shadow: 0 0 40px rgba(28,167,166,0.6); }}
        20%, 40%, 60%, 80% {{ transform: translateY(-20px) scale(1.15) rotate(-4deg); }}
        90% {{ transform: translateY(-20px) scale(1.15) rotate(0deg); }}
        100% {{ transform: translateY(0) scale(1); box-shadow: 0 8px 25px rgba(0,0,0,0.5); }}
    }}
    .trigger-anim {{ animation: sofiaJump 5s cubic-bezier(0.25, 1, 0.5, 1) forwards; }}
    
    @keyframes modalPop {{
        0% {{ opacity: 0; transform: translate(-50%, -40%) scale(0.9); }}
        10%, 90% {{ opacity: 1; transform: translate(-50%, -50%) scale(1); }}
        100% {{ opacity: 0; transform: translate(-50%, -60%) scale(0.9); pointer-events: none; visibility: hidden; }}
    }}
    .glass-modal {{
        position: fixed; top: 50%; left: 50%; transform: translate(-50%, -50%);
        background: rgba(3, 24, 56, 0.85); backdrop-filter: blur(25px); -webkit-backdrop-filter: blur(25px);
        border: 1px solid rgba(28, 167, 166, 0.4); border-radius: 24px; padding: 50px 40px;
        text-align: center; z-index: 999999; box-shadow: 0 25px 50px rgba(0,0,0,0.5), inset 0 0 20px rgba(28,167,166,0.1);
        width: 90%; max-width: 550px; animation: modalPop 5s cubic-bezier(0.16, 1, 0.3, 1) forwards; pointer-events: none;
    }}

    /* =========================================
       RESPONSIVIDAD (Mobile First Approach)
       ========================================= */
    @media (max-width: 768px) {{
        .sofia-wrapper {{ top: 55px; right: 15px; width: 70px; }}
        .fibex-tagline {{ font-size: 10px; letter-spacing: 1.5px; margin-bottom: 25px; }}
        div[data-testid="stMetric"] {{ padding: 15px !important; }}
        div[data-testid="stMetric"] div[data-testid="stMetricValue"] {{ font-size: 1.8rem !important; }}
        .glass-modal {{ padding: 30px 20px; }}
        .glass-modal h2 {{ font-size: 1.5rem !important; }}
    }}
    </style>
""", unsafe_allow_html=True)

# --- 3. ENCABEZADO CORPORATIVO ---
c_logo1, c_logo2, c_logo3 = st.columns([1, 2, 1])
with c_logo2:
    try: st.image("logo.png", use_container_width=True)
    except: st.markdown("<h1 style='text-align:center; font-weight:900; letter-spacing:2px;'>FIBEX TELECOM</h1>", unsafe_allow_html=True)
st.markdown('<div class="fibex-tagline">"Lo que no se mide, no se controla"</div>', unsafe_allow_html=True)

canal = st.radio("ÁREA OPERATIVA", ["Oficinas (ATC)", "Ventas Calle / Call Center"], horizontal=True, label_visibility="collapsed")
st.divider()

# --- 4. PANEL DE INGRESO (ACTUAL) ---
st.sidebar.markdown("### 📊 GESTIÓN DEL CORTE")
def draw_inputs(title, items_dict):
    st.sidebar.markdown(f"**{title}**")
    v_total, pts_total = 0, 0
    for name, (k_id, pts) in items_dict.items():
        val = st.sidebar.number_input(name, min_value=0, value=0, step=1, key=k_id)
        v_total += val; pts_total += (val * pts)
    return v_total, pts_total

v_h_menor, p_h_menor = draw_inputs("1. Hogar (< $40)", {"Básico ($25) [3pts]":("p25",3), "Cinéfilo ($30) [8pts]":("p30",8), "Medio ($35) [9pts]":("p35",9)})
v_h_mayor, p_h_mayor = draw_inputs("2. Hogar (≥ $40)", {"Medio ($40) [10pts]":("p40",10), "Full ($45) [12pts]":("p45",12), "XFull ($50+) [15pts]":("p50",15)})
st.sidebar.markdown("**3. Corporativo & Extras**")
v_py = st.sidebar.number_input("PYME (15 pts)", 0, step=1, key="py"); p_py = v_py * 15
v_rc = st.sidebar.number_input("RCV (3 pts)", 0, step=1, key="rc"); p_rc = v_rc * 3
v_up = st.sidebar.number_input("UPSELL (4 pts)", 0, step=1, key="up"); p_up = v_up * 4

# --- 5. LÓGICA DE BÓVEDA (ALMACENAMIENTO DE SESIÓN) ---
st.sidebar.divider()
st.sidebar.markdown("### 💾 BÓVEDA DE CONSOLIDACIÓN")
if st.sidebar.button("📥 Sumar a Bóveda e Iniciar Nuevo Corte", use_container_width=True, type="primary"):
    st.session_state.boveda['v_hogar'] += (v_h_menor + v_h_mayor)
    st.session_state.boveda['v_h40'] += v_h_mayor
    st.session_state.boveda['v_pyme'] += v_py
    st.session_state.boveda['v_rcv'] += v_rc
    st.session_state.boveda['v_upsell'] += v_up
    st.session_state.boveda['pts_hogar'] += (p_h_menor + p_h_mayor)
    st.session_state.boveda['pts_pyme'] += p_py
    st.session_state.boveda['pts_rcv'] += p_rc
    st.session_state.boveda['pts_upsell'] += p_up
    st.sidebar.success("✅ Guardado en bóveda. Reinicia los valores a cero para el 2do corte.")

if st.sidebar.button("🗑️ Vaciar Bóveda", use_container_width=True):
    st.session_state.boveda = {k: 0 for k in st.session_state.boveda}
    st.rerun()

# --- 6. PROCESAMIENTO CORE (GRAN TOTAL) ---
GT_h = (v_h_menor + v_h_mayor) + st.session_state.boveda['v_hogar']
GT_h40 = v_h_mayor + st.session_state.boveda['v_h40']
GT_py = v_py + st.session_state.boveda['v_pyme']
GT_rc = v_rc + st.session_state.boveda['v_rcv']
GT_up = v_up + st.session_state.boveda['v_upsell']
GT_pts = (p_h_menor + p_h_mayor + p_py + p_rc + p_up) + st.session_state.boveda['pts_hogar'] + st.session_state.boveda['pts_pyme'] + st.session_state.boveda['pts_rcv'] + st.session_state.boveda['pts_upsell']

if st.session_state.boveda['v_hogar'] > 0:
    st.info(f"📊 **MODO CONSOLIDADO ACTIVO:** Los resultados mostrados incluyen lo guardado en bóveda ({st.session_state.boveda['v_hogar']} Ventas Hogar Previas).")

# Reglas de Negocio
is_atc = canal == "Oficinas (ATC)"
req_h1 = 8 if is_atc else 15
op1 = GT_h >= req_h1
op2 = (GT_h >= (6 if is_atc else 10)) and (GT_py >= 1)
op3 = GT_h40 >= (3 if is_atc else 5)
op4 = GT_py >= (4 if is_atc else 8)
califica = any([op1, op2, op3, op4])

cat_thresholds = [
    (30 if is_atc else 50, "SUPER ESTRELLAS", 0.45),
    (23 if is_atc else 41, "ÉLITE", 0.40),
    (17 if is_atc else 31, "PRO", 0.35),
    (11 if is_atc else 20, "SENIOR", 0.30),
    (6 if is_atc else 10, "JUNIOR", 0.00)
]
categoria, pct_bono = next(((c, p) for t, c, p in cat_thresholds if GT_h >= t), ("BÁSICO", 0.00))
pago_proyectado = GT_pts * (1 + pct_bono) if califica else 0

# --- 7. RENDERIZADO DE ANIMACIONES Y RESULTADOS ---
anim_class = "trigger-anim" if califica else ""
st.markdown(f'<div class="sofia-wrapper"><img src="{img_src}" class="sofia-img {anim_class}"></div>', unsafe_allow_html=True)

if califica:
    st.markdown("""
        <div class="glass-modal">
            <h2 style="color:#1ca7a6; font-weight:900; margin-bottom:10px; font-family:'Montserrat'; letter-spacing:1px;">¡CALIFICACIÓN LOGRADA! 🚀</h2>
            <p style="color:#FFF; font-size:1.1rem; font-weight:500;">Los números han sido procesados y aprobados.</p>
            <div style="font-size:4rem; margin-top:20px;">👏🏼 👏🏼 👏🏼</div>
        </div>
        <audio autoplay hidden><source src="https://assets.mixkit.co/active_storage/sfx/2000/2000-preview.mp3" type="audio/mpeg"></audio>
    """, unsafe_allow_html=True)
else:
    st.error(f"⚠️ **BRECHA OPERATIVA:** Faltan ventas para habilitar esquema de comisiones en {canal}.")

m1, m2, m3, m4 = st.columns(4)
m1.metric("Volumen Hogar", GT_h)
m2.metric("Puntuación Base", f"{GT_pts} pts")
m3.metric("Rango Operativo", f"{categoria} (+{int(pct_bono*100)}%)")
m4.metric("PROYECCIÓN (Ref)", f"${pago_proyectado:.2f}")
