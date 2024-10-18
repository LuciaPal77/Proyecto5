import pandas
import plotly.express
import streamlit
        
car_data = pandas.read_csv('C:/Users/Luli/Desktop/Proyecto 5/Proyecto5/vehicles_us.csv') # leer los datos
hist_button = streamlit.button('Construir histograma') # crear un botón
        
if hist_button: # al hacer clic en el botón
            # escribir un mensaje
    streamlit.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
            # crear un histograma
    fig = plotly.express.histogram(car_data, x="odometer")
        
            # mostrar un gráfico Plotly interactivo
    streamlit.plotly_chart(fig, use_container_width=True)