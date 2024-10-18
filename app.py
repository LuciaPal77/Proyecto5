import pandas
import plotly.express
import streamlit 

streamlit.header('Estudio de Vehiculos')

car_data = pandas.read_csv('vehicles_us.csv') # leer los datos
hist_button = streamlit.button('Construir histograma') # crear un botón
        
if hist_button: # al hacer clic en el botón
            # escribir un mensaje
    streamlit.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
            # crear un histograma
    fig = plotly.express.histogram(car_data, x="odometer")
        
            # mostrar un gráfico Plotly interactivo
    streamlit.plotly_chart(fig, use_container_width=True)

build_histogram = streamlit.checkbox('Construir un histograma')
if build_histogram: # si la casilla de verificación está seleccionada
    streamlit.write('Construir un histograma para la columna odómetro')


scatt_button = streamlit.button('Construir gráfica de dispersión')
if scatt_button:
    streamlit.write('Crea un gráfico de dispersión sobre la columna precio')
    fig2 = plotly.express.scatter(car_data, x="price")
streamlit.scatter_chart(car_data)  #Grafica de dispersion
