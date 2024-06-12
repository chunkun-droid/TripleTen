import pandas as pd
import plotly.express as px
import streamlit as st


st.header("Analisis de autos usados")
car_data = pd.read_csv('vehicles_us.csv') # leer los datos
hist_button = st.button('Construir histograma') # crear un botón
        
if hist_button: # al hacer clic en el botón
            # escribir un mensaje
  st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
            # crear un histograma
  fig = px.histogram(car_data, x="odometer")
        
            # mostrar un gráfico Plotly interactivo
  st.plotly_chart(fig, use_container_width=True)


scatter_button = st.button('Construir gráfico de disperción') # crear un botón
        
if scatter_button: # al hacer clic en el botón
            # escribir un mensaje
  st.write('Creación de un gráfico de disperción para el conjunto de datos de anuncios de venta de coches')
            
            # crear un gráfico de dispercion
  fig = px.scatter(car_data, x="odometer", y="price") # crear un gráfico de dispersión

        
            # mostrar un gráfico Plotly interactivo
  st.plotly_chart(fig, use_container_width=True)


build_boxplot = st.checkbox('Contruir boxplot')

if build_boxplot:
  st.write('Contruir un boxplot para la columna condición')

  fig = px.box(car_data, x="condition", y="price", color="fuel")
  # mostrar un gráfico Plotly interactivo
  st.plotly_chart(fig, use_container_width=True)