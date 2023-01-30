from src import utilities
import streamlit as st

st.title("Calculadora de parámetros de láser")
st.markdown("Todas las unidades deben introducirse en :red[milímetros]")

with st.expander("Introduzca puntos de corte y distáncia entre arcos", expanded=True):
    x1 = st.number_input("Punto 1 - Coordenada X")
    y1 = st.number_input("Punto 1 - Coordenada Y")
    x2 = st.number_input("Punto 2 - Coordenada X")
    y2 = st.number_input("Punto 2 - Coordenada Y")
    d_arcos = st.number_input("Distáncia entre los arcos")
    profundidad = st.number_input("Profundidad del corte")

ri = 20

st.text(" ")
boton_calcular = st.button("Calcular")

if boton_calcular:
    cxe, cye, cxi, cyi, re = utilities.calcula_parametros(x1, y1, x2, y2, ri, d_arcos)
    angulo_externo, angulo_interno = utilities.calcula_angulo(d_arcos, profundidad)

    fig = utilities.genera_grafico(x1, y1, x2, y2, cxe, cye, re, cxi, cyi, ri)

    st.pyplot(fig)

st.text(" ")
st.subheader("Parámetros para el primer corte")

col1, col2, col3, col4 = st.columns([3, 2, 2, 2])
col1.metric("Centro", f"({round(cxe, 2)}, {round(cye, 2)})")
col2.metric("Radio", f"{round(re, 4)}")
col3.metric("Ángulo de corte", f"{round(angulo_externo, 2)}")
col4.metric("Profundidad", f"{profundidad}")

st.text(" ")
st.subheader("Parámetros para el segundo corte")

col1, col2, col3, col4 = st.columns([3, 2, 2, 2])
col1.metric("Centro", f"({round(cxi, 2)}, {round(cyi, 2)})")
col2.metric("Radio", f"{round(ri, 4)}")
col3.metric("Ángulo de corte", f"{round(angulo_interno, 2)}")
col4.metric("Profundidad", f"{profundidad}")