import streamlit as st
import plotly.express as px
import pandas as pd


car_data = pd.read_csv('./dataset/vehicles_us.csv')
hist_button = st.button('Construir Histograma')
scatter_button = st.button('Construir Gráfica Dispesión')

st.warning('Puedes usar el checkbox para generar tambien la gráfcia de dispersión')
scatter_check = st.checkbox('Construir Gráfica Dispersión (opcional)')

st.header('Información Vehiculos')


if hist_button:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    fig = px.histogram(car_data,x='odometer')

    st.plotly_chart(fig,use_container_width=True)

if scatter_button:
    st.write('Creación de una gráfcia de dispersión para el conjunto de datos de anuncios de venta de coches')    

    fig = px.scatter(car_data,x='odometer',y='price')

    st.plotly_chart(fig,use_container_width=True,key='button_scatter')

if scatter_check:
    st.write('Creación de una gráfica de dispersión con Checkbox para el conjunto de datos de anuncios de venta de coches')    

    fig = px.scatter(car_data,x='odometer',y='price')

    st.plotly_chart(fig,use_container_width=True,key='check_scatter') 
  