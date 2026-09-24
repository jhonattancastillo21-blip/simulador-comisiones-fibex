import streamlit as st
import base64
import os
import random

# --- 1. CONFIGURACIÓN DE PÁGINA Y ESTADO DE SESIÓN ---
st.set_page_config(page_title="Fibex Telecom | Portal de Comisiones", page_icon="⚡", layout="wide")

# Estado de sesión para controlar que el aplauso suene solo una vez al llegar a la meta
if 'aplausos_reproducidos' not in st.session_state:
    st.session_state.aplausos_reproducidos = False

def encode_image(image_path):
    return base64.b64encode(open(image_path, "rb").read()).decode() if os.path.exists(image_path) else ""

img_sofia = encode_image("sofia.png")
img_src = f"data:image/png;base64,{img_sofia}" if img_sofia else "https://cdn-icons-png.flaticon.com/512/4140/4140047.png"

# --- 2. CSS RESPONSIVO DE ALTO NIVEL ---
css_style = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700;800;900&display=swap');

.stApp {
    background-color: #010a17;
    background-image: radial-gradient(circle at 50% 15%, rgba(28, 167, 166, 0.20), transparent 45%),
                      radial-gradient(circle at 85% 65%, rgba(11, 91, 153, 0.22), transparent 50%);
    font-family: 'Montserrat', sans-serif;
    color: #ffffff;
}

.kpi-card {
    background: rgba(10, 25, 47, 0.75);
    border: 1px solid rgba(28, 167, 166, 0.3);
    border-radius: 12px;
    padding: 20px;
    text-align: center;
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.4);
}

.kpi-title {
    font-size: 0.85rem;
    font-weight: 700;
    color: #1ca7a6;
    letter-spacing: 1px;
    margin-bottom: 8px;
    text-transform: uppercase;
}

.kpi-value {
    font-size: 2.1rem;
    font-weight: 900;
    color: #ffffff;
}

.kpi-subtext {
    font-size: 0.8rem;
    color: #8892b0;
    margin-top: 4px;
}
</style>
"""
st.markdown(css_style, unsafe_allow_html=True)

# --- 3. ENCABEZADO Y CANAL DE VENTA ---
col_logo, col_header, col_avatar = st.columns([1, 3, 1])

with col_header:
    st.markdown("<h1 style='text-align: center; color: #ffffff; font-weight: 900;'>FIBEX TELECOM</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #1ca7a6; font-size: 0.9rem; font-weight: 700;'>\"LO QUE NO SE MIDE, NO SE CONTROLA\"</p>", unsafe_allow_html=True)

with col_avatar:
    st.markdown(f"<div style='text-align: right;'><img src='{img_src}' width='80' style='border-radius: 50%; border: 2px solid #1ca7a6;'></div>", unsafe_allow_html=True)

st.divider()

# Selección de Canal
canal = st.radio(
    "SELECCIONA EL CANAL DE VENTAS:",
    ["Ventas Calle / Club Fibex / Corporativo", "Televentas", "ATC (Atención al Cliente)"],
    horizontal=True
)

is_calle = "Calle" in canal
is_atc = "ATC" in canal

# --- 4. BARRA LATERAL (ENTRADA DE DATOS QUINCENALES) ---
st.sidebar.header("📋 GESTIÓN DEL CORTE (Boletín 027)")

st.sidebar.subheader("1. Combos Hogar")
h_sencillo = st.sidebar.number_input("Conectados Sencillo / Básico ($20-$25)", min_value=0, step=1)
h_cinefilo_bas = st.sidebar.number_input("Cinéfilos Básicos ($30)", min_value=0, step=1)
h_medio = st.sidebar.number_input("Conectados Medio / Familiar Básico ($35)", min_value=0, step=1)
h_cinefilo_med = st.sidebar.number_input("Cinéfilos / Gamer Medio ($40)", min_value=0, step=1)
h_full = st.sidebar.number_input("Conectados Full / Familiar Medio ($45)", min_value=0, step=1)
h_cinefilo_xfull = st.sidebar.number_input("Cinéfilos XFull / Gamer Full ($50)", min_value=0, step=1)
h_xfull = st.sidebar.number_input("Conectados XFull ($55)", min_value=0, step=1)
h_gamer_xfull = st.sidebar.number_input("Gamer XFull / Familiar Full ($60)", min_value=0, step=1)

st.sidebar.subheader("2. Combos PYME")
p_30 = st.sidebar.number_input("Emprendedores Conectados ($30)", min_value=0, step=1)
p_40 = st.sidebar.number_input("Emprendedores Seguro / Comercio Conectado ($40)", min_value=0, step=1)
p_45 = st.sidebar.number_input("Emprendedores Protegidos ($45)", min_value=0, step=1)
p_50 = st.sidebar.number_input("Comercio Seguros ($50)", min_value=0, step=1)
p_55 = st.sidebar.number_input("Comercio Protegidos ($55)", min_value=0, step=1)
p_65 = st.sidebar.number_input("Oficina Conectados ($65)", min_value=0, step=1)
p_75 = st.sidebar.number_input("Oficina Seguros / Negocios Conectado ($75)", min_value=0, step=1)
p_80 = st.sidebar.number_input("Oficina Protegidos ($80)", min_value=0, step=1)
p_95 = st.sidebar.number_input("Oficina Seguros / Negocios Seguro ($95)", min_value=0, step=1)
p_120 = st.sidebar.number_input("Negocios Protegidos ($120)", min_value=0, step=1)

st.sidebar.subheader("3. Equipos Adicionales (Smart Buy & Cámaras)")
e_roku = st.sidebar.number_input("Roku (2 pts)", min_value=0, step=1)
e_ups = st.sidebar.number_input("Mini UPS (2 pts)", min_value=0, step=1)
e_cam1 = st.sidebar.number_input("Combo Cámara X1 (3 pts)", min_value=0, step=1)
e_cam3 = st.sidebar.number_input("Combo Cámara X3 (9 pts)", min_value=0, step=1)
e_cam4 = st.sidebar.number_input("Combo Cámara X4 (12 pts)", min_value=0, step=1)
e_cam6 = st.sidebar.number_input("Combo Cámara X6 (18 pts)", min_value=0, step=1)

# --- 5. LÓGICA DE CÁLCULO DE PUNTOS ---
pts_h = (
    h_sencillo * (3 if is_calle else 2) +
    h_cinefilo_bas * (8 if is_calle else 7) +
    h_medio * (9 if is_calle else 8) +
    h_cinefilo_med * (10 if is_calle else 9) +
    h_full * (12 if is_calle else 11) +
    h_cinefilo_xfull * (13 if is_calle else 12) +
    h_xfull * (14 if is_calle else 13) +
    h_gamer_xfull * (15 if is_calle else 14)
)

pts_p = (
    p_30 * (5 if is_calle else 4) +
    p_40 * (7 if is_calle else 6) +
    p_45 * (8 if is_calle else 7) +
    p_50 * (9 if is_calle else 8) +
    p_55 * (10 if is_calle else 9) +
    p_65 * (12 if is_calle else 11) +
    p_75 * (14 if is_calle else 13) +
    p_80 * (16 if is_calle else 15) +
    p_95 * (18 if is_calle else 17) +
    p_120 * (20 if is_calle else 19)
)

pts_e = (e_roku * 2) + (e_ups * 2) + (e_cam1 * 3) + (e_cam3 * 9) + (e_cam4 * 12) + (e_cam6 * 18)

total_ventas = (
    h_sencillo + h_cinefilo_bas + h_medio + h_cinefilo_med + h_full +
    h_cinefilo_xfull + h_xfull + h_gamer_xfull + p_30 + p_40 + p_45 +
    p_50 + p_55 + p_65 + p_75 + p_80 + p_95 + p_120
)

puntuacion_total = pts_h + pts_p + pts_e

comisiona = total_ventas >= 2

if not is_atc:
    if total_ventas >= 50:
        categoria = "SUPER ESTRELLAS"
        bono_pct = 0.45
    elif total_ventas >= 40:
        categoria = "ÉLITE"
        bono_pct = 0.40
    elif total_ventas >= 30:
        categoria = "PRO"
        bono_pct = 0.35
    elif total_ventas >= 20:
        categoria = "SENIOR"
        bono_pct = 0.30
    elif total_ventas >= 10:
        categoria = "JUNIOR"
        bono_pct = 0.00
    else:
        categoria = "BÁSICO"
        bono_pct = 0.00
else:
    if total_ventas >= 30:
        categoria = "SUPER ESTRELLAS"
        bono_pct = 0.45
    elif total_ventas >= 23:
        categoria = "ÉLITE"
        bono_pct = 0.40
    elif total_ventas >= 17:
        categoria = "PRO"
        bono_pct = 0.35
    elif total_ventas >= 11:
        categoria = "SENIOR"
        bono_pct = 0.30
    elif total_ventas >= 6:
        categoria = "JUNIOR"
        bono_pct = 0.00
    else:
        categoria = "BÁSICO"
        bono_pct = 0.00

proyeccion_usd = (puntuacion_total * (1 + bono_pct)) if comisiona else 0.0

# --- 6. VISUALIZACIÓN DE RESULTADOS (KPI CARDS) ---
kpi1, kpi2, kpi3, kpi4 = st.columns(4)

with kpi1:
    st.markdown(f"""
    <div class='kpi-card'>
        <div class='kpi-title'>VOLUMEN TOTAL</div>
        <div class='kpi-value'>{total_ventas}</div>
        <div class='kpi-subtext'>Ventas Instaladas</div>
    </div>
    """, unsafe_allow_html=True)

with kpi2:
    st.markdown(f"""
    <div class='kpi-card'>
        <div class='kpi-title'>PUNTUACIÓN BASE</div>
        <div class='kpi-value'>{puntuacion_total} pts</div>
        <div class='kpi-subtext'>Equivalente en USD ($1 = 1pt)</div>
    </div>
    """, unsafe_allow_html=True)

with kpi3:
    st.markdown(f"""
    <div class='kpi-card'>
        <div class='kpi-title'>RANGO OPERATIVO</div>
        <div class='kpi-value'>{categoria}</div>
        <div class='kpi-subtext'>Bonificación extra: {int(bono_pct*100)}%</div>
    </div>
    """, unsafe_allow_html=True)

with kpi4:
    st.markdown(f"""
    <div class='kpi-card'>
        <div class='kpi-title'>PROYECCIÓN A COBRAR</div>
        <div class='kpi-value' style='color: #1ca7a6;'>${proyeccion_usd:.2f}</div>
        <div class='kpi-subtext'>Al cambio oficial BCV</div>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# --- 7. ALERTAS Y NOTIFICACIONES (MENSAJE MOTIVADOR) ---
if not comisiona:
    st.markdown("""
    <div style='background-color: rgba(255, 75, 75, 0.1); border-left: 5px solid #ff4b4b; padding: 15px; border-radius: 5px; margin-bottom: 20px;'>
        <h4 style='color: #ff4b4b; margin-top: 0;'>⚠️ Aún no eres elegible para comisionar</h4>
        <p style='color: #dddddd; font-size: 1.05rem; margin-bottom: 0;'>
            Requieres un mínimo de <strong>2 ventas</strong> en el corte quincenal para activar tus comisiones (Boletín 027). 
            <br><br>
            🔥 <strong>¡No te rindas!</strong> En Fibex sabemos el potencial que tienes. Estás a un paso de empezar a sumar ganancias. 
            ¡Enfócate, contacta a ese cliente indeciso y cierra la venta! <strong>El éxito está en tus manos.</strong>
        </p>
    </div>
    """, unsafe_allow_html=True)
else:
    st.success("✅ **¡Elegible para comisionar!** Has superado el mínimo de 2 ventas quincenales. ¡Sigue así!")

meta_alimentacion = 15 if is_atc else 30
if total_ventas >= meta_alimentacion:
    st.info(f"🎉 **¡Bono de Alimentación Duplicado!** Has alcanzado la meta de {meta_alimentacion} ventas del mes.")

# --- 8. LÓGICA DE APLAUSOS Y GLOBOS REALISTAS (META DE 30 VENTAS) ---

def lanzar_globos_realistas():
    html_balloons = """
    <style>
    .balloon-anim {
        position: fixed;
        bottom: -150px;
        border-radius: 50% 50% 50% 50% / 40% 40% 60% 60%;
        box-shadow: inset -10px -10px 15px rgba(0,0,0,0.3), 2px 2px 5px rgba(0,0,0,0.2);
        z-index: 999999;
        opacity: 0.95;
    }
    .balloon-anim::after {
        content: '';
        position: absolute;
        bottom: -50px;
        left: 50%;
        width: 2px;
        height: 50px;
        background: rgba(255,255,255,0.4);
    }
    @keyframes floatUpBalloons {
        0% { transform: translateY(0) rotate(0deg); opacity: 1; }
        100% { transform: translateY(-120vh) rotate(15deg); opacity: 0; }
    }
    </style>
    <div id='balloon-container'>
    """
    colors = ["#1ca7a6", "#0b5b99", "#ffffff", "#00d2ff", "#3a7bd5", "#0052D4", "#6FB1FC"]
    for _ in range(45):
        left = random.randint(0, 100)
        width = random.randint(40, 90)
        height = int(width * 1.25)
        color = random.choice(colors)
        duration = random.uniform(7.0, 14.0) # Duran entre 7 y 14 segundos en subir
        delay = random.uniform(0.0, 5.0)     # Van saliendo poco a poco
        
        style = f"left: {left}vw; width: {width}px; height: {height}px; background-color: {color}; "
        style += f"animation: floatUpBalloons {duration}s ease-in forwards {delay}s;"
        html_balloons += f"<div class='balloon-anim' style='{style}'></div>"
    
    html_balloons += "</div>"
    st.markdown(html_balloons, unsafe_allow_html=True)

if total_ventas >= 30:
    if not st.session_state.aplausos_reproducidos:
        # 1. Animación visual de globos realistas (CSS personalizado)
        lanzar_globos_realistas()
        
        # 2. Reproductor oculto del audio de YouTube (p95L-psfneI)
        youtube_audio_html = """
        <iframe width="0" height="0" 
                src="https://www.youtube.com/embed/p95L-psfneI?autoplay=1&controls=0&modestbranding=1&rel=0" 
                frameborder="0" allow="autoplay; encrypted-media" allowfullscreen>
        </iframe>
        """
        st.markdown(youtube_audio_html, unsafe_allow_html=True)
        
        # 3. Marcamos como reproducido para que no vuelva a sonar si llegan a 31, 32...
        st.session_state.aplausos_reproducidos = True
else:
    # Si bajan de 30 ventas, reseteamos el estado para que vuelva a sonar si vuelven a subir
    st.session_state.aplausos_reproducidos = False
