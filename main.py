from src import utilities
import streamlit as st

st.title("Calculadora resección en cuña")
st.markdown("Cada parámetro debe introducirse en las unidades indicadas")

with st.expander("Introduzca los parámetros para el cálculo", expanded=True):
    x1 = st.number_input("Punto 1 - Coordenada X (mm)")
    y1 = st.number_input("Punto 1 - Coordenada Y (mm)")
    x2 = st.number_input("Punto 2 - Coordenada X (mm)")
    y2 = st.number_input("Punto 2 - Coordenada Y (mm)")
    d_arcos = st.number_input("Distancia entre los arcos (mm)")
    profundidad = st.number_input("Cutting depth (µm)")

ri = 3

st.text(" ")
boton_calcular = st.button("Calcular")

if boton_calcular:
    cxe, cye, cxi, cyi, re = utilities.calcula_parametros(x1, y1, x2, y2, ri, d_arcos)
    angulo_externo, angulo_interno = utilities.calcula_angulo(d_arcos, profundidad*0.001)
    longitud_arco_externo = utilities.calcula_longitud_arco(x1, y1, x2, y2, cxe, cye)
    longitud_arco_interno = utilities.calcula_longitud_arco(x1, y1, x2, y2, cxi, cyi)
    angulo_medio_externo = utilities.calcula_angulo_con_horizontal((x1+x2)/2, (y1+y2)/2, cxe, cye)
    angulo_medio_interno = utilities.calcula_angulo_con_horizontal((x1+x2)/2, (y1+y2)/2, cxi, cyi)

    fig = utilities.genera_grafico(x1, y1, x2, y2, cxe, cye, re, cxi, cyi, ri)

    st.pyplot(fig)

st.text(" ")
st.subheader("Parámetros para el primer corte")

with st.container():
    col1, col2, col3 = st.columns([2, 2, 2])
    col1.metric("Centro (mm)", f"({round(cxe, 2)}, {round(cye, 2)})")
    col2.metric("Radio (mm)", f"{round(re, 3)}")
    col3.metric("Arc center position (º)", f"{round(angulo_medio_externo, 2)}")
    col1.metric("Arc length (º)", f"{round(longitud_arco_externo, 2)}")
    col2.metric("Side cut angle (º)", f"{round(angulo_externo, 2)}")
    col3.metric("Cutting depth (µm)", f"{profundidad}")

    # col1, col2 = st.columns([2, 2])
    # col1.metric("Centro (mm)", f"({round(cxe, 2)}, {round(cye, 2)})")
    # col2.metric("Radio (mm)", f"{round(re, 3)}")
    # col1.metric("Arc center position (º)", f"{round(angulo_medio_externo, 2)}")
    # col2.metric("Arc length (º)", f"{round(longitud_arco_externo, 2)}")
    # col1.metric("Side cut angle (º)", f"{round(angulo_externo, 2)}")
    # col2.metric("Cutting depth (µm)", f"{profundidad}") 

st.text(" ")
st.subheader("Parámetros para el segundo corte")

with st.container():
    col1, col2, col3 = st.columns([2, 2, 2])
    col1.metric("Centro (mm)", f"({round(cxi, 2)}, {round(cyi, 2)})")
    col2.metric("Radio (mm)", f"{round(ri, 3)}")
    col3.metric("Arc center position (º)", f"{round(angulo_medio_interno, 2)}")
    col1.metric("Arc length (º)", f"{round(longitud_arco_interno, 2)}")
    col2.metric("Side cut angle (º)", f"{round(angulo_interno, 2)}")
    col3.metric("Cutting depth (µm)", f"{profundidad}")

    # col1, col2 = st.columns([2, 2])
    # col1.metric("Centro (mm)", f"({round(cxi, 2)}, {round(cyi, 2)})")
    # col2.metric("Radio (mm)", f"{round(ri, 3)}")
    # col1.metric("Arc center position (º)", f"{round(angulo_medio_interno, 2)}")
    # col2.metric("Arc length (º)", f"{round(longitud_arco_interno, 2)}")
    # col1.metric("Side cut angle (º)", f"{round(angulo_interno, 2)}")
    # col2.metric("Cutting depth (µm)", f"{profundidad}") 
