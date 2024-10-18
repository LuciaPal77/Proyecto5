import pandas as pd
import plotly.express as px
import streamlit as st

st.header('Estudio de Vehiculos')

car_data = pd.read_csv('vehicles_us.csv') # leer los datos

#Boton Histograma
hist_button = st.button('Construir histograma')
        
if hist_button: # al hacer clic en el botón
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            # crear un histograma
    fig = px.histogram(car_data, x="odometer")
        #Mostramos el histograma
    st.plotly_chart(fig, use_container_width=True)

build_histogram = st.checkbox('Construir un histograma')
if build_histogram: # si la casilla de verificación está seleccionada
    st.write('Construir un histograma para la columna odómetro')


scatt_button = st.button('Construir gráfica de dispersión')
if scatt_button:
    st.write('Crea un gráfico de dispersión')
    fig2 = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig2,use_container_width=True)  #Grafica de dispersion
