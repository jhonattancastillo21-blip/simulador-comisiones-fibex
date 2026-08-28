import streamlit as st
import base64
import os

# --- 1. CONFIGURACIÓN DE PÁGINA Y ESTADO DE SESIÓN ---
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

# --- 2. CSS ULTRA-RESPONSIVO DE NIVEL ELITE ---
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700;800;900&display=swap');

    /* Fondo Corporativo Fibex */
    .stApp {{
        background-color: #010a17;
        background-image: 
            radial-gradient(circle at 50% 15%, rgba(28, 167, 166, 0.20), transparent 45%),
            radial-gradient(circle at 85% 65%, rgba(11, 91, 153, 0.22), transparent 50%);
        background-attachment: fixed !important;
        font-family: 'Montserrat', sans-serif !important;
        color: #FFFFFF !important;
    }}

    /* Contenedor del Logo */
    [data-testid="stImage"] img {{
        max-width: clamp(240px, 25vw, 400px) !important;
        height: auto !important;
        margin: 0 auto !important;
        display: block !important;
    }}

    /* Sidebar Glassmorphism */
    [data-testid="stSidebar"] {{
        background: rgba(2, 14, 33, 0.85) !important;
        backdrop-filter: blur(20px) !important;
        -webkit-backdrop-filter: blur(20px) !important;
        border-right: 1px solid rgba(28, 167, 166, 0.25);
    }}

    /* --- TARJETAS DE MÉTRICAS RESPONSIVAS Y SIN TRUNCAMIENTO --- */
    div[data-testid="stMetric"] {{
        background: rgba(3, 24, 56, 0.70) !important;
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        border: 1px solid rgba(28, 167, 166, 0.35) !important;
        border-radius: 16px !important;
        padding: 14px 12px !important;
        text-align: center !important;
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.35);
        transition: all 0.3s ease;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        min-height: 105px;
    }}
    div[data-testid="stMetric"]:hover {{
        transform: translateY(-3px);
        border-color: #80E3E2 !important;
        box-shadow: 0 10px 30px rgba(128, 227, 226, 0.25);
    }}

    /* Etiqueta / Título de la Métrica */
    div[data-testid="stMetric"] label {{ 
        color: #80E3E2 !important; 
        font-size: clamp(0.75rem, 0.9vw, 0.95rem) !important; 
        font-weight: 700 !important; 
        letter-spacing: 0.6px;
        text-transform: uppercase;
        justify-content: center !important;
        width: 100%;
        margin-bottom: 4px;
    }}

    /* Valor de la Métrica (Ajuste dinámico para evitar 'SUPER ESTR...') */
    div[data-testid="stMetric"] div[data-testid="stMetricValue"] {{ 
        color: #FFFFFF !important; 
        font-weight: 900 !important; 
        font-size: clamp(1.1rem, 1.4vw, 1.7rem) !important; 
        white-space: normal !important;
        word-break: break-word !important;
        overflow-wrap: break-word !important;
        line-height: 1.25 !important;
        width: 100%;
    }}

    /* Subtítulo principal */
    .fibex-tagline {{ 
        text-align: center; 
        font-weight: 700; 
        color: #80E3E2; 
        font-size: clamp(11px, 1vw, 15px); 
        letter-spacing: 2.5px; 
        text-transform: uppercase; 
        margin-top: 4px; 
        margin-bottom: 25px; 
    }}

    /* Avatar de Sofía */
    .sofia-wrapper {{ position: fixed; top: 60px; right: 30px; width: clamp(70px, 7vw, 110px); z-index: 9999; pointer-events: none; }}
    .sofia-img {{ width: 100%; border-radius: 50%; box-shadow: 0 6px 20px rgba(0,0,0,0.6); border: 3px solid #1ca7a6; }}
    
    @keyframes sofiaJump {{
        0% {{ transform: translateY(0) scale(1); }}
        10%, 30%, 50%, 70% {{ transform: translateY(-16px) scale(1.12) rotate(4deg); box-shadow: 0 0 35px rgba(128,227,226,0.8); }}
        20%, 40%, 60%, 80% {{ transform: translateY(-16px) scale(1.12) rotate(-4deg); }}
        90% {{ transform: translateY(-16px) scale(1.12) rotate(0deg); }}
        100% {{ transform: translateY(0) scale(1); }}
    }}
    .trigger-anim {{ animation: sofiaJump 4.5s cubic-bezier(0.25, 1, 0.5, 1) forwards; }}
    
    /* MODAL APLAUSO ESTÁNDAR (JUNIOR, SENIOR, PRO) */
    @keyframes modalPop {{
        0% {{ opacity: 0; transform: translate(-50%, -40%) scale(0.88); }}
        12%, 88% {{ opacity: 1; transform: translate(-50%, -50%) scale(1); }}
        100% {{ opacity: 0; transform: translate(-50%, -60%) scale(0.88); visibility: hidden; }}
    }}
    .glass-modal {{
        position: fixed; top: 50%; left: 50%; transform: translate(-50%, -50%);
        background: rgba(2, 14, 33, 0.95); backdrop-filter: blur(25px);
        border: 2px solid #1ca7a6; border-radius: 20px; padding: 35px 25px;
        text-align: center; z-index: 999999; box-shadow: 0 20px 50px rgba(0,0,0,0.8);
        width: 90%; max-width: 500px; animation: modalPop 4.5s forwards; pointer-events: none;
    }}

    /* MODAL RANGOS TOP (ÉLITE Y SUPER ESTRELLAS) */
    @keyframes starGlowModal {{
        0% {{ opacity: 0; transform: translate(-50%, -45%) scale(0.85); box-shadow: 0 0 10px rgba(128, 227, 226, 0.2); }}
        12%, 88% {{ opacity: 1; transform: translate(-50%, -50%) scale(1); box-shadow: 0 0 50px rgba(128, 227, 226, 0.8), 0 0 90px rgba(28, 167, 166, 0.6); }}
        100% {{ opacity: 0; transform: translate(-50%, -55%) scale(0.85); visibility: hidden; display: none; }}
    }}
    .star-modal {{
        position: fixed; top: 50%; left: 50%; transform: translate(-50%, -50%);
        background: linear-gradient(135deg, rgba(2, 14, 33, 0.97) 0%, rgba(3, 38, 77, 0.97) 100%);
        border: 2px solid #80E3E2; border-radius: 24px; padding: 40px 30px;
        text-align: center; z-index: 999999;
        animation: starGlowModal 5s cubic-bezier(0.16, 1, 0.3, 1) forwards;
        pointer-events: none; width: 90%; max-width: 540px;
    }}
    .star-text-glow {{
        font-size: clamp(1.6rem, 3vw, 2.5rem);
        font-weight: 900;
        color: #FFFFFF;
        text-shadow: 0 0 15px #80E3E2, 0 0 30px #1ca7a6;
        letter-spacing: 1.5px;
        margin-bottom: 10px;
    }}

    /* MEJORAS ESPECÍFICAS PARA DISPOSITIVOS MÓVILES */
    @media (max-width: 768px) {{
        [data-testid="stImage"] img {{ max-width: 210px !important; }}
        .sofia-wrapper {{ top: 45px; right: 12px; width: 62px; }}
        div[data-testid="stMetric"] {{ 
            padding: 10px 6px !important; 
            min-height: 90px;
            margin-bottom: 8px;
        }}
        div[data-testid="stMetric"] label {{
            font-size: 0.72rem !important;
        }}
        div[data-testid="stMetric"] div[data-testid="stMetricValue"] {{
            font-size: 1.15rem !important;
        }}
    }}
    </style>
""", unsafe_allow_html=True)

# --- 3. ENCABEZADO Y LOGO ---
c1, c2, c3 = st.columns([1, 2, 1])
with c2:
    try: 
        st.image("logo.png")
    except: 
        st.markdown("<h1 style='text-align:center; font-weight:900;'>FIBEX TELECOM</h1>", unsafe_allow_html=True)
st.markdown('<div class="fibex-tagline">"Lo que no se mide, no se controla"</div>', unsafe_allow_html=True)

canal = st.radio("ÁREA OPERATIVA", ["Oficinas (ATC)", "Ventas Calle / Call Center"], horizontal=True, label_visibility="collapsed")
st.divider()

# --- 4. PANEL LATERAL (SIDEBAR) ---
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

# --- 5. BÓVEDA DE CONSOLIDACIÓN ---
st.sidebar.divider()
st.sidebar.markdown("### 💾 BÓVEDA DE CONSOLIDACIÓN")
if st.sidebar.button("📥 Sumar 1er Corte a Bóveda", use_container_width=True, type="primary"):
    st.session_state.boveda['v_hogar'] += (v_h_menor + v_h_mayor)
    st.session_state.boveda['v_h40'] += v_h_mayor
    st.session_state.boveda['v_pyme'] += v_py
    st.session_state.boveda['v_rcv'] += v_rc
    st.session_state.boveda['v_upsell'] += v_up
    st.session_state.boveda['pts_hogar'] += (p_h_menor + p_h_mayor)
    st.session_state.boveda['pts_pyme'] += p_py
    st.session_state.boveda['pts_rcv'] += p_rc
    st.session_state.boveda['pts_upsell'] += p_up
    st.sidebar.success("✅ ¡1er Corte guardado! Ingresa los datos del 2do corte.")

if st.sidebar.button("🗑️ Vaciar Bóveda", use_container_width=True):
    st.session_state.boveda = {k: 0 for k in st.session_state.boveda}
    st.rerun()

# --- 6. TOTALIZACIÓN Y REGLAS DE NEGOCIO ---
GT_h = (v_h_menor + v_h_mayor) + st.session_state.boveda['v_hogar']
GT_h40 = v_h_mayor + st.session_state.boveda['v_h40']
GT_py = v_py + st.session_state.boveda['v_pyme']
GT_rc = v_rc + st.session_state.boveda['v_rcv']
GT_up = v_up + st.session_state.boveda['v_upsell']
GT_pts = (p_h_menor + p_h_mayor + p_py + p_rc + p_up) + st.session_state.boveda['pts_hogar'] + st.session_state.boveda['pts_pyme'] + st.session_state.boveda['pts_rcv'] + st.session_state.boveda['pts_upsell']

if st.session_state.boveda['v_hogar'] > 0:
    st.info(f"📊 **BÓVEDA ACTIVA:** Incluye {st.session_state.boveda['v_hogar']} ventas acumuladas del 1er corte.")

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

# --- 7. SISTEMA EXCLUSIVO DE SONIDO Y ANIMACIÓN ---
anim_class = "trigger-anim" if califica else ""
st.markdown(f'<div class="sofia-wrapper"><img src="{img_src}" class="sofia-img {anim_class}"></div>', unsafe_allow_html=True)

if califica:
    # REGLA 2: ÉLITE Y SUPER ESTRELLAS -> ÚNICAMENTE EL AUDIO DEL ENLACE DE YOUTUBE
    if categoria in ["ÉLITE", "SUPER ESTRELLAS"]:
        st.markdown(f"""
            <div class="star-modal">
                <div class="star-text-glow">✨ ¡SUPER ESTRELLA! ✨</div>
                <p style="color:#80E3E2; font-size:1.15rem; font-weight:700; margin-top:5px; text-transform:uppercase;">
                    NIVEL {categoria} ALCANZADO (+{int(pct_bono*100)}% BONO)
                </p>
                <div style="font-size:3.2rem; margin-top:12px;">🌟 👏🏼 🏆 👏🏼 🌟</div>
            </div>
            <!-- Único audio activo para ÉLITE / SUPER ESTRELLA (YouTube lHcgWdxR14A) -->
            <iframe width="0" height="0" src="https://www.youtube.com/embed/lHcgWdxR14A?autoplay=1&enablejsapi=1" allow="autoplay" style="display:none; visibility:hidden;"></iframe>
        """, unsafe_allow_html=True)
    
    # REGLA 3: ESCALAS INFERIORES A ÉLITE (PRO, SENIOR, JUNIOR) -> APLAUSO PREDETERMINADO
    else:
        # Sonido predeterminado de aplausos
        sound_default = "https://assets.mixkit.co/active_storage/sfx/2018/2018-preview.mp3"
        st.markdown(f"""
            <div class="glass-modal">
                <h2 style="color:#80E3E2; font-weight:900; margin-bottom:6px; font-family:'Montserrat';">¡EXCELENTE TRABAJO! 🎉</h2>
                <p style="color:#FFF; font-size:1.05rem; font-weight:600;">Calificación confirmada en Rango <b>{categoria}</b> (+{int(pct_bono*100)}% Bono)</p>
                <div style="font-size:3rem; margin-top:10px;">👏🏼 👏🏼 👏🏼</div>
            </div>
            <!-- Audio predeterminado de aplausos para niveles base e intermedios -->
            <audio autoplay hidden><source src="{sound_default}" type="audio/mpeg"></audio>
        """, unsafe_allow_html=True)
else:
    st.error(f"⚠️ **META PENDIENTE:** Requiere más volumen de ventas para calificar en {canal}.")

# --- 8. MOSTRAR MÉTRICAS ---
m1, m2, m3, m4 = st.columns(4)
m1.metric("Volumen Hogar", GT_h)
m2.metric("Puntuación Base", f"{GT_pts} pts")
m3.metric("Rango Operativo", categoria)
m4.metric("PROYECCIÓN (Ref)", f"${pago_proyectado:.2f}")
