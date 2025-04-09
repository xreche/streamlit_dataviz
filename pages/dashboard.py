import streamlit as st
import numpy as np
import pandas as pd

st.title("✨ Pro Dashboard ✨")

# --- Sección 1 ---
st.subheader("Sección 1")
t1s1, t2s1, t3s1 = st.tabs(['Gráfica 1', 'Gráfica 2', 'Gráfica 3'])

with t1s1:
    st.line_chart(data=np.random.randn(10, 1))

with t2s1:
    st.bar_chart(data=np.random.randn(10, 1))

with t3s1:
    subtab1, subtab2 = st.tabs(["Gráfico de barras", "Mapa"])

    with subtab1:
        st.bar_chart(data=np.random.randn(10, 1), use_container_width=True)

    with subtab2:
        map_data = pd.DataFrame(
            np.random.randn(250, 2) / [50, 50] + [19.43, -99.13],  # Ciudad de México aprox
            columns=["lat", "lon"]
        )
        st.map(map_data, zoom=10)

# --- Sección 2 ---
st.subheader("Sección 2")
col1, col2 = st.columns(2)

with col1:
    st.subheader("Gráfico de Barras Horizontal")
    st.bar_chart(data=np.random.randn(10, 1), horizontal=True)

with col2:
    st.subheader("Mapa")
    map_data = pd.DataFrame(
        np.random.randn(250, 2) / [50, 50] + [19.43, -99.13],  # Ciudad de México aprox
        columns=["lat", "lon"]
    )
    st.map(map_data, zoom=10)

# --- Sección 3 ---
st.subheader("Sección 3")
c1_3, c2_3 = st.columns(2)

with c1_3:
    st.container(border=True).metric("Temperatura", "27 °C", "16 °F")

with c2_3:
    st.container(border=True).metric("Viento", "9 mph", "-8%")
