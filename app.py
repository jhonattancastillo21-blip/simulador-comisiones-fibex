import streamlit as st

st.set_page_config(page_title="Simulador Comisiones Fibex", page_icon="⚡", layout="wide")

st.title("⚡ Simulador Oficial de Comisiones - Fibex Telecom")
st.markdown("Calculadora de metas y comisiones quincenales según Boletín N° 022.")

# --- SELECCIÓN DE CANAL DE VENTA ---
canal = st.sidebar.radio(
    "Selecciona tu Área / Canal de Venta:",
    ["Ventas Calle / Call Center", "Oficinas (ATC)"]
)

st.sidebar.markdown("---")
st.sidebar.header("📥 Ingreso de Ventas de la Quincena")

# --- CATALOGO DE PLANES HOGAR Y PUNTOS ---
# Separados por precio para validar la Opción 3 (Planes >= $40)
planes_menores_40 = {
    "Plan Básico / Estándar (< $40)": 5,
}

planes_mayores_igual_40 = {
    "Gamer Medio ($40) - 10 pts": 10,
    "Conectados Full ($45) - 12 pts": 12,
    "Familiar Full ($45) - 12 pts": 12,
    "Cinéfilos XFull ($50) - 13 pts": 13,
    "Gamer Full ($50) - 13 pts": 13,
    "Conectados XFull ($55) - 14 pts": 14,
    "Gamer XFull ($60) - 15 pts": 15,
    "Familiar XFull ($60) - 15 pts": 15,
}

# Inputs en la barra lateral
st.sidebar.subheader("1. Ventas Hogar (< $40)")
v_hogar_menor = st.sidebar.number_input("Cantidad de Ventas Menores a $40", min_value=0, value=0, step=1)

st.sidebar.subheader("2. Ventas Hogar (≥ $40)")
v_hogar_mayor_40 = 0
puntos_hogar_mayor = 0

for plan, pts in planes_mayores_igual_40.items():
    cant = st.sidebar.number_input(f"{plan}", min_value=0, value=0, step=1)
    v_hogar_mayor_40 += cant
    puntos_hogar_mayor += (cant * pts)

puntos_hogar_menor = v_hogar_menor * 5
total_ventas_hogar = v_hogar_menor + v_hogar_mayor_40
total_puntos_hogar = puntos_hogar_menor + puntos_hogar_mayor

st.sidebar.subheader("3. Productos Adicionales / Otros")
v_pyme = st.sidebar.number_input("Ventas PYME", min_value=0, value=0, step=1)
v_rcv = st.sidebar.number_input("Ventas RCV", min_value=0, value=0, step=1)
v_upselling = st.sidebar.number_input("Ventas UPSELLING", min_value=0, value=0, step=1)

# Asignación de puntos adicionales (puntos de referencia)
puntos_pyme = v_pyme * 15
puntos_rcv = v_rcv * 3
puntos_upselling = v_upselling * 4

total_puntos_base = total_puntos_hogar + puntos_pyme + puntos_rcv + puntos_upselling

# --- LÓGICA DE CALIFICACIÓN SEGÚN CANAL ---
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

# --- LÓGICA DE CATEGORÍAS Y MULTIPLICADORES ---
# Evaluación por volumen de ventas hogar totales
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

# --- CÁLCULO FINAL DE PUNTOS / COMISIÓN ---
puntos_bonificados = total_puntos_base * pct_bono
total_puntos_finales = total_puntos_base + puntos_bonificados if califica else 0

# --- PANEL PRINCIPAL DE RESULTADOS ---
st.header("🎯 Estado de Calificación Quincenal")

if califica:
    st.success(f"¡ENHORA BUENA! Estás **CALIFICADO** para comisionar en **{canal}**.")
    
    # Detalle de la opción con la que calificó
    opciones_cumplidas = []
    if opc1: opciones_cumplidas.append("Opción 1 (Ventas Hogar Totales)")
    if opc2: opciones_cumplidas.append("Opción 2 (Hogar + PYME)")
    if opc3: opciones_cumplidas.append("Opción 3 (Ventas ≥ $40)")
    if opc4: opciones_cumplidas.append("Opción 4 (Ventas PYME Totales)")
    if opc5: opciones_cumplidas.append("Opción 5 (Hogar + RCV)")
    if opc6: opciones_cumplidas.append("Opción 6 (Hogar + UPSELLING)")
    
    st.info(f"Calificas mediante: **{', '.join(opciones_cumplidas)}**")
else:
    st.error(f"❌ AÚN NO CALIFICAS PARA COMISIONAR EN ESTA QUINCENA ({canal}).")

st.markdown("---")
st.header("📊 Resumen de Rendimiento y Cobro Estimado")

m1, m2, m3, m4 = st.columns(4)
m1.metric("Total Ventas Hogar", f"{total_ventas_hogar}")
m2.metric("Puntos Base Acumulados", f"{total_puntos_base} pts")
m3.metric("Categoría Alcance", f"{categoria} (+{int(pct_bono*100)}%)")
m4.metric("💰 ESTIMADO A COBRAR", f"${total_puntos_finales:.2f} Ref")

if califica and pct_bono > 0:
    st.balloons()
    st.success(f"🔥 ¡Excelente! Gracias a tu categoría **{categoria}**, recibes un **+{int(pct_bono*100)}%** adicional sobre todos tus puntos acumulados.")
