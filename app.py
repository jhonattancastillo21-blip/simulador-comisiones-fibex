import streamlit as st

st.set_page_config(page_title="Simulador de Comisiones Fibex 2026", page_icon="⚡", layout="wide")

st.title("⚡ Simulador de Comisiones y Metas - Fibex Telecom")
st.caption("Boletín N° 022 | Dirección de Negocios Masivo 2026")

# --- SELECCIÓN DE CANAL Y ROL ---
col_canal, col_quincena = st.columns(2)
with col_canal:
    canal = st.selectbox("📌 Selecciona tu Canal de Ventas:", ["Ventas Calle", "Call Center", "Oficina (ATC)"])
with col_quincena:
    quincena = st.radio("🗓️ Evaluación de Quincena:", ["Quincena 1 (Q1)", "Quincena 2 (Q2 / Acumulado Mes)"])

st.markdown("---")

# --- TABLAS DE PUNTOS SEGÚN BOLETÍN 022 ---
# (Plan: [Tarifa, Puntos Calle/CC, Puntos Oficina])
planes_data = {
    "Conectados Básico ($25)": [25, 3, 2],
    "Cinéfilos Básicos ($30)": [30, 8, 7],
    "Conectados Medio ($35)": [35, 9, 8],
    "Familiar Básico ($35)": [35, 9, 8],
    "Cinéfilos Medio ($40)": [40, 10, 8],
    "Gamer Medio ($40)": [40, 10, 9],
    "Conectados Full ($45)": [45, 12, 11],
    "Familiar Full ($45)": [45, 12, 11],
    "Cinéfilos XFull ($50)": [50, 13, 12],
    "Gamer Full ($50)": [50, 13, 12],
    "Conectados XFull ($55)": [55, 14, 13],
    "Gamer XFull ($60)": [60, 15, 14],
    "Familiar Full ($60)": [60, 15, 14]
}

st.subheader("🛒 Carga tus Ventas Realizadas")

col_left, col_right = st.columns(2)

ventas_planes = {}
total_ventas_hogar = 0
total_puntos_base = 0
ventas_ge_40 = 0

is_oficina = (canal == "Oficina (ATC)")
idx_puntos = 2 if is_oficina else 1

with col_left:
    st.write("**Combos Hogar Vendidos:**")
    for plan, info in planes_data.items():
        cant = st.number_input(f"{plan} - ({info[idx_puntos]} pts)", min_value=0, value=0, key=plan)
        if cant > 0:
            ventas_planes[plan] = cant
            total_ventas_hogar += cant
            total_puntos_base += cant * info[idx_puntos]
            if info[0] >= 40:
                ventas_ge_40 += cant

with col_right:
    st.write("**Productos Adicionales (PYME, RCV, Upselling):**")
    ventas_pyme = st.number_input("Ventas PYME:", min_value=0, value=0)
    ventas_rcv = st.number_input("Pólizas RCV independientes:", min_value=0, value=0)
    ventas_upselling = st.number_input("Cambios de Plan (Upselling):", min_value=0, value=0)

st.markdown("---")

# --- VALIDACIÓN DE UMBRAL / CALIFICACIÓN QUINCENAL ---
st.subheader("🎯 Estado de Calificación Quincenal")

califica = False
opcion_cumplida = ""

# Reglas de Opciones
if is_oficina:
    if total_ventas_hogar >= 8: califica, opcion_cumplida = True, "Opción 1 (8 Ventas Hogar)"
    elif total_ventas_hogar >= 6 and ventas_pyme >= 1: califica, opcion_cumplida = True, "Opción 2 (6 Hogar + 1 PYME)"
    elif ventas_ge_40 >= 3: califica, opcion_cumplida = True, "Opción 3 (3 Hogar ≥ $40)"
    elif ventas_pyme >= 4: califica, opcion_cumplida = True, "Opción 4 (4 PYME)"
    elif total_ventas_hogar >= 6 and ventas_rcv >= 4: califica, opcion_cumplida = True, "Opción 5 (6 Hogar + 4 RCV)"
    elif total_ventas_hogar >= 6 and ventas_upselling >= 5: califica, opcion_cumplida = True, "Opción 6 (6 Hogar + 5 Upselling)"
else:
    if total_ventas_hogar >= 15: califica, opcion_cumplida = True, "Opción 1 (15 Ventas Hogar)"
    elif total_ventas_hogar >= 10 and ventas_pyme >= 1: califica, opcion_cumplida = True, "Opción 2 (10 Hogar + 1 PYME)"
    elif ventas_ge_40 >= 5: califica, opcion_cumplida = True, "Opción 3 (5 Hogar ≥ $40)"
    elif ventas_pyme >= 8: califica, opcion_cumplida = True, "Opción 4 (8 PYME)"
    elif total_ventas_hogar >= 10 and ventas_rcv >= 4: califica, opcion_cumplida = True, "Opción 5 (10 Hogar + 4 RCV)"
    elif total_ventas_hogar >= 10 and ventas_upselling >= 5: califica, opcion_cumplida = True, "Opción 6 (10 Hogar + 5 Upselling)"

if califica:
    st.success(f"✅ **¡CALIFICADO PARA COMISIONAR!** Cumpliste la **{opcion_cumplida}**.")
else:
    st.error("❌ **AÚN NO CALIFICAS PARA COMISIONAR EN ESTA QUINCENA.**")
    st.info("💡 **Recordatorio Boletín 022:** Si no alcanzas la meta en Q1, tus ventas se acumulan para la Q2. ¡Alcanza la meta acumulada al cierre de mes para liberar tus pagos!")

st.markdown("---")

# --- CATEGORIZACIÓN Y BONIFICACIÓN MENSUAL ---
st.subheader("🏆 Categoria y Bonificación de Banda")

total_ventas_mes = total_ventas_hogar # Se evalúa por volumen de ventas
categoria = "BÁSICO"
pct_bono = 0.0

if is_oficina:
    if total_ventas_mes >= 30: categoria, pct_bono = "SUPER ESTRELLAS", 0.45
    elif total_ventas_mes >= 23: categoria, pct_bono = "ÉLITE", 0.40
    elif total_ventas_mes >= 17: categoria, pct_bono = "PRO", 0.35
    elif total_ventas_mes >= 11: categoria, pct_bono = "SENIOR", 0.30
    elif total_ventas_mes >= 6: categoria, pct_bono = "JUNIOR", 0.00
    else: categoria, pct_bono = "BÁSICO", 0.00
else:
    if total_ventas_mes >= 50: categoria, pct_bono = "SUPER ESTRELLAS", 0.45
    elif total_ventas_mes >= 41: categoria, pct_bono = "ÉLITE", 0.40
    elif total_ventas_mes >= 31: categoria, pct_bono = "PRO", 0.35
    elif total_ventas_mes >= 20: categoria, pct_bono = "SENIOR", 0.30
    elif total_ventas_mes >= 10: categoria, pct_bono = "JUNIOR", 0.00
    else: categoria, pct_bono = "BÁSICO", 0.00

# --- CÁLCULO FINAL DE DINERO ---
puntos_bonificados = total_puntos_base * pct_bono
total_puntos_finales = total_puntos_base + puntos_bonificados if califica else 0

m1, m2, m3, m4 = st.columns(4)
m1.metric("Total Ventas Hogar", f"{total_ventas_hogar}")
m2.metric("Puntos Base Acumulados", f"{total_puntos_base} pts")
m3.metric("Categoría Alcanzada", f"{categoria} (+{int(pct_bono*100)}%)")
m4.metric("💰 ESTIMADO A COBRAR ($ Ref)", f"${total_puntos_finales:.2f}")

if califica and pct_bono > 0:
    st.balloons()
    st.success(f"🔥 ¡Increíble! Gracias a tu categoría **{categoria}**, recibes un **+{int(pct_bono*100)}% de bonificación** extra sobre todos tus puntos acumulados.")

# IMPULSO PSICOLÓGICO AL VENDEDOR
if not califica:
    st.warning("🚀 **¡Estás muy cerca!** Coloca un par de combos más o incluye 1 PYME / RCV para activar el pago de tus comisiones.")
