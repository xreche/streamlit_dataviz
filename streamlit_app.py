import streamlit as st
import pandas as pd
import numpy as np

# desde la web de streamlit
# como usar los comandos git para subir el proyecto a github
# https://docs.streamlit.io/1.4.0/knowledge-base/tutorials/deploy/git

st.title("Elementos de interfaz :iphone:")

###
# Static tables
###

st.header("Tabla estática")
dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))
st.table(dataframe)

###
# Dynamic tables
###

st.header("Tabla dinámica")
st.dataframe(dataframe.style.highlight_max(axis=0))
# documentación de la función dataframe en streamlit
st.write("Documentación de la función dataframe en streamlit: [dataframe](https://docs.streamlit.io/en/latest/api-reference/data/st.dataframe)")

###
# Line chart
###

st.header("Gráfico de líneas")
chart_data = pd.DataFrame(
    np.random.randn(30, 3),
    columns=['a', 'b', 'c'])
st.line_chart(chart_data)

###
# Map
###

st.header("Mapa")
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])
st.map(map_data)


###
# Slider
###

st.header("Slider")
x = st.slider('x', key="slider_x")  # 👈 this is a widget
st.write(x, 'squared is', x * x)

###
# Selectbox
###

st.header("Selectbox")
option = st.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone'),
    key="contact_method")
st.write('You selected:', option)

###
# Multi select
###

st.header("Multi select")
options = st.multiselect(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone'),
    key="contact_methods")
st.write('You selected:', options)

###
# Checkbox
###

st.header("Checkbox")
checkbox = st.checkbox('I agree', key="agree_checkbox")
st.write(checkbox)

###
# Radio button
###

st.header("Radio button")
radio = st.radio('Select an option', ('Option 1', 'Option 2', 'Option 3'), key="radio_options")
st.write(radio) 

###
# Button
###

st.header("Botón")
button = st.button('Click me!', key="click_button")
st.write(button)

###
# Text input
###

st.header("Texto")
text = st.text_input('Enter a text', key="text_input")
st.write(text)

###
# Text area
###

st.header("Área de texto")
text_area = st.text_area('Enter a text', key="text_area")
st.write(text_area) 

###
# Date input
###

st.header("Fecha")
date = st.date_input('Enter a date', key="date_input")
st.write(date)  

###
# Time input
###

st.header("Hora")
time = st.time_input('Enter a time', key="time_input")
st.write(time)  

###
# Color picker
###

st.header("Color")
color = st.color_picker('Enter a color', key="color_picker")
st.write(color)     

###
# Checkbox with chart
###

st.header("Checkbox con gráfico")
if st.checkbox('Show/Hide', key="show_chart_checkbox"):
    chart_data = pd.DataFrame(
        np.random.randn(30, 3),
        columns=['a', 'b', 'c'])
    st.line_chart(chart_data)

###
# Columns
###

st.header("Columnas")
col1, col2 = st.columns(2)

### Left column
# Usando métodos de la clase column
col1.header("Left column")
col1.write("This is the left column")

### Right column
# usando with   
with col2:
    st.header("Right column")
    st.write("This is the right column")

###
# Sidebar items
###

st.header("Sidebar items")
st.sidebar.header("Sidebar items")
st.sidebar.write("This is the sidebar")

# Selectbox
st.sidebar.subheader("Selectbox")
option = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone'),
    key="sidebar_contact_method")
st.sidebar.write('You selected:', option)

# Slider
st.sidebar.subheader("Slider")
x = st.sidebar.slider('Select a range of values', 0, 100, (10, 20), key="sidebar_slider")  # �� this is a widget
