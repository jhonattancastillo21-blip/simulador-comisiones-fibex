import streamlit as st
import base64
import os

# --- 1. CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(
    page_title="Fibex Telecom | Portal de Comisiones",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Codificar imágenes locales a Base64
def encode_image(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    return ""

img_sofia = encode_image("sofia.png")
img_src = f"data:image/png;base64,{img_sofia}" if img_sofia else "https://cdn-icons-png.flaticon.com/512/4140/4140047.png"

# --- 2. CSS CUSTOM Y RESPONSIVO PARA MÓVILES ---
css_style = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700;800;900&display=swap');

/* Encabezado transparente para mantener visible la flecha (>) del menú lateral en móviles */
header[data-testid="stHeader"] {
    background-color: transparent !important;
    z-index: 99999;
}

/* Color de la flecha para desplegar el menú en la esquina superior izquierda */
button[data-testid="stSidebarCollapseButton"], 
button[data-testid="baseButton-header"] {
    color: #1ca7a6 !important;
}

/* Ajuste general del contenedor */
.block-container {
    padding-top: 2rem !important;
    padding-bottom: 2rem !important;
    padding-left: 1rem !important;
    padding-right: 1rem !important;
    max-width: 900px;
}

/* Fondo principal oscuro corporativo */
.stApp {
    background-color: #010a17;
    background-image: radial-gradient(circle at 50% 10%, rgba(28, 167, 166, 0.18), transparent 45%),
                      radial-gradient(circle at 85% 65%, rgba(11, 91, 153, 0.20), transparent 50%);
    font-family: 'Montserrat', sans-serif;
    color: #ffffff;
}

/* Header compacto estilo App Nativa */
.header-container {
    display: flex;
    align-items: center;
    justify-content: space-between;
    background: rgba(10, 25, 47, 0.6);
    border: 1px solid rgba(28, 167, 166, 0.25);
    border-radius: 16px;
    padding: 12px 18px;
    margin-bottom: 15px;
    backdrop-filter: blur(10px);
}

.header-title {
    font-size: 1.3rem;
    font-weight: 900;
    color: #ffffff;
    margin: 0;
    letter-spacing: 1px;
    line-height: 1.1;
}

.header-subtitle {
    font-size: 0.68rem;
    font-weight: 700;
    color: #1ca7a6;
    margin: 3px 0 0 0;
    letter-spacing: 0.5px;
}

.header-avatar {
    width: 55px;
    height: 55px;
    border-radius: 50%;
    border: 2px solid #1ca7a6;
    object-fit: cover;
    box-shadow: 0 0 12px rgba(28, 167, 166, 0.4);
}

/* Tarjetas KPI compactas */
.kpi-card {
    background: linear-gradient(145deg, rgba(10, 25, 47, 0.85), rgba(1, 10, 23, 0.95));
    border: 1px solid rgba(28, 167, 166, 0.35);
    border-radius: 14px;
    padding: 14px 10px;
    text-align: center;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.5);
    margin-bottom: 12px;
}

.kpi-title {
    font-size: 0.72rem;
    font-weight: 800;
    color: #1ca7a6;
    letter-spacing: 1px;
    margin-bottom: 4px;
    text-transform: uppercase;
}

.kpi-value {
    font-size: 1.8rem;
    font-weight: 900;
    color: #ffffff;
    line-height: 1.1;
}

.kpi-subtext {
    font-size: 0.7rem;
    color: #8892b0;
    margin-top: 3px;
}

/* Radio buttons ajustados */
div[data-testid="stRadio"] > label {
    font-weight: 700 !important;
    color: #1ca7a6 !important;
    font-size: 0.85rem !important;
}

hr {
    margin: 1rem 0 !important;
    border-color: rgba(28, 167, 166, 0.2) !important;
}
</style>
"""
st.markdown(css_style, unsafe_allow_html=True)

# --- 3. ENCABEZADO COMPACTO Y ELEGANTE ---
header_html = f"""
<div class="header-container">
    <div>
        <div class="header-title">FIBEX TELECOM</div>
        <div class="header-subtitle">"LO QUE NO SE MIDE, NO SE CONTROLA"</div>
    </div>
    <img src="{img_src}" class="header-avatar" alt="Sofía Fibex">
</div>
"""
st.markdown(header_html, unsafe_allow_html=True)

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

# --- 6. VISUALIZACIÓN DE RESULTADOS (KPI CARDS EN 2X2 PARA MÓVILES) ---
kpi1, kpi2 = st.columns(2)
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
        <div class='kpi-subtext'>Equivalente ($1 = 1pt)</div>
    </div>
    """, unsafe_allow_html=True)

kpi3, kpi4 = st.columns(2)
with kpi3:
    st.markdown(f"""
    <div class='kpi-card'>
        <div class='kpi-title'>RANGO OPERATIVO</div>
        <div class='kpi-value'>{categoria}</div>
        <div class='kpi-subtext'>Bono Extra: {int(bono_pct*100)}%</div>
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

# --- 7. ALERTAS Y NOTIFICACIONES ---
if not comisiona:
    st.markdown("""
    <div style='background-color: rgba(255, 75, 75, 0.12); border-left: 4px solid #ff4b4b; padding: 12px 15px; border-radius: 8px; margin-bottom: 15px;'>
        <h4 style='color: #ff4b4b; margin: 0 0 5px 0; font-size: 0.95rem;'>⚠️ Aún no eres elegible para comisionar</h4>
        <p style='color: #dddddd; font-size: 0.85rem; margin: 0; line-height: 1.4;'>
            Requieres un mínimo de <strong>2 ventas</strong> en el corte quincenal para activar tus comisiones (Boletín 027).
            <br>🔥 <strong>¡Enfócate y cierra la próxima venta!</strong> El éxito está en tus manos.
        </p>
    </div>
    """, unsafe_allow_html=True)
else:
    st.success("✅ **¡Elegible para comisionar!** Has superado el mínimo de 2 ventas quincenales.")

meta_alimentacion = 15 if is_atc else 30
if total_ventas >= meta_alimentacion:
    st.info(f"🎉 **¡Bono de Alimentación Duplicado!** Has alcanzado la meta de {meta_alimentacion} ventas del mes.")

# --- 8. CELEBRACIÓN COMPATIBLE CON IPHONE (MP3 + JS LOCAL) ---
if total_ventas >= 30:
    html_celebracion = """
    <div id="celebration-box" style="text-align: center; margin: 20px 0;">
        <button id="celebrate-btn" onclick="ejecutarCelebracion()" style="
            background: linear-gradient(135deg, #1ca7a6 0%, #0b5b99 100%);
            color: #ffffff;
            padding: 16px 32px;
            font-size: 1.1rem;
            font-weight: 800;
            border: none;
            border-radius: 50px;
            cursor: pointer;
            box-shadow: 0 8px 25px rgba(28, 167, 166, 0.5);
            text-transform: uppercase;
            letter-spacing: 1px;
            width: 100%;
            max-width: 350px;
            transition: transform 0.2s, box-shadow 0.2s;
        ">
            🎉 ¡RECLAMAR RECONOCIMIENTO! 🎉
        </button>
        <audio id="audio_aplausos_mp3" preload="auto">
            <source src="https://assets.mixkit.co/active_storage/sfx/2000/2000-preview.mp3" type="audio/mpeg">
        </audio>
    </div>

    <script>
    function ejecutarCelebracion() {
        var audio = document.getElementById("audio_aplausos_mp3");
        if (audio) {
            audio.currentTime = 0;
            audio.play().catch(function(e) {
                console.log("Audio play error:", e);
            });
        }

        var btnBox = document.getElementById("celebration-box");
        if (btnBox) {
            btnBox.style.display = "none";
        }

        var colors = ["#1ca7a6", "#0b5b99", "#ffffff", "#00d2ff", "#ff007f", "#ffd700"];
        var container = document.body;

        for (var i = 0; i < 45; i++) {
            (function() {
                var balloon = document.createElement("div");
                var size = Math.floor(Math.random() * 35) + 35;
                var left = Math.floor(Math.random() * 90) + 5;
                var color = colors[Math.floor(Math.random() * colors.length)];
                var duration = (Math.random() * 4 + 5); 
                var delay = Math.random() * 1.5;

                balloon.style.position = "fixed";
                balloon.style.bottom = "-80px";
                balloon.style.left = left + "vw";
                balloon.style.width = size + "px";
                balloon.style.height = (size * 1.25) + "px";
                balloon.style.backgroundColor = color;
                balloon.style.borderRadius = "50% 50% 50% 50% / 40% 40% 60% 60%";
                balloon.style.boxShadow = "inset -8px -8px 12px rgba(0,0,0,0.3)";
                balloon.style.zIndex = "999999";
                balloon.style.pointerEvents = "none";

                container.appendChild(balloon);

                balloon.animate([
                    { transform: "translateY(0) rotate(0deg)", opacity: 1 },
                    { transform: "translateY(-115vh) rotate(" + (Math.random() * 30 - 15) + "deg)", opacity: 0 }
                ], {
                    duration: duration * 1000,
                    delay: delay * 1000,
                    fill: "forwards",
                    easing: "ease-out"
                });

                setTimeout(function() {
                    if (balloon && balloon.parentNode) {
                        balloon.parentNode.removeChild(balloon);
                    }
                }, (duration + delay) * 1000 + 500);
            })();
        }
    }
    </script>
    """
    st.markdown(html_celebracion, unsafe_allow_html=True)
