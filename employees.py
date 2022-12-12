import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

st.title('Aplicación Web de Ciencia de Datos - Reto de Aplicación')

st.header('Descripción del proyecto') # HEADER
st.write('Reto de Aplicación creado para el módulo de Aplicación Web de Ciencia de Datos del diplomado de Data Science and AI elaborado por Mariana Tellez Resendiz. Dentro de este proyecto utilizamos el archivo "Employees.csv" y exploramos conceptos de Streamlit como por ejemplo: ')
st.write('a) Acceso a dataframes de pandas.')
st.write('b) Manejo de cache.')
st.write('c) Controles button, selectbox, text_input, sidebar, slider, radio, checkbox.')
st.write('d) Gráficas.')

st.subheader('Manejo de cache para el dataframe') # SUBHEADER

DATA_URL = ('/workspaces/streamlit-m5/Employees.csv')

@st.cache
def load_data(nrows):
    employees = pd.read_csv(DATA_URL, nrows=nrows)
    return employees

data_load_state = st.text('Loading data...')
employees = load_data(500)
data_load_state.text("Done! (Using st.cache)")

sidebar = st.sidebar

sidebar.title("Menú")
sidebar.write("Aquí puedes manipular los parámetros para mostrar la información.")

st.markdown("___")
st.header('Visualización del Dataframe') # HEADER

chk_box = sidebar.checkbox("¿Mostrar el dataframe completo?")
if chk_box:
  st.dataframe(employees)

st.markdown("___")
st.header('Búsqueda de Empleados por ID, Hometown o Unit')

sidebar.markdown("___")
sidebar.subheader('Buscar empleados por:')

@st.cache
def filter_data_id(id):
    filtered_data_id = employees[employees['Employee_ID'].str.upper().str.contains(id)]
    return filtered_data_id

idempleado = st.sidebar.text_input('ID del Empleado:')
btnBuscarID = st.sidebar.button('Buscar por ID')

st.subheader('Empleados por ID')

if(btnBuscarID):
    data_ID = filter_data_id(idempleado.upper())
    count_row = data_ID.shape[0] # Numero de filas
    st.write(data_ID)
    st.write(f"Total de empleados con ese ID: {count_row}")

@st.cache
def filter_data_hometown(home):
    filtered_data_hometown = employees[employees['Hometown'].str.upper().str.contains(home)]
    return filtered_data_hometown

homeempleado = st.sidebar.text_input('Ciudad del Empleado:')
btnBuscarHome = st.sidebar.button('Buscar por ciudad')

st.subheader('Empleados por Hometown')

if(btnBuscarHome):
    data_home = filter_data_hometown(homeempleado.upper())
    count_row = data_home.shape[0] # Numero de filas
    st.write(data_home)
    st.write(f"Total de empleados con esa ciudad: {count_row}")

@st.cache
def filter_data_unit(unt):
    filtered_data_unit = employees[employees['Unit'].str.upper().str.contains(unt)]
    return filtered_data_unit

unitempleado = st.sidebar.text_input('Unidad del Empleado:')
btnBuscarUnit = st.sidebar.button('Buscar por unidad')

st.subheader('Empleados por Unit')

if(btnBuscarUnit):
    data_unit = filter_data_unit(unitempleado.upper())
    count_row = data_unit.shape[0] # Numero de filas
    st.write(data_unit)
    st.write(f"Total de empleados con esa unidad: {count_row}")

sidebar.markdown("___")
sidebar.subheader('Filtrar empleados por:')

st.markdown("___")
st.header('Filtrado de Empleados por Nivel Educativo')

@st.cache
def filter_data_by_level(lvl):
    filtered_data_level = employees[employees['Education_Level'] == lvl]
    return filtered_data_level

selected_level = st.sidebar.selectbox("Seleccionar nivel educativo", employees['Education_Level'].unique())
btnFilterLevel = st.sidebar.button('Filtrar nivel educativo')

if(btnFilterLevel):
    filterbylvl = filter_data_by_level(selected_level)
    count_row = filterbylvl.shape[0] # Numero de filas
    st.dataframe(filterbylvl)
    st.write(f"Total de empleados por el nivel educativo seleccionado: {count_row}")

st.markdown("___")
st.header('Filtrado de Empleados por Ciudad')

@st.cache
def filter_data_by_city(city):
    filtered_data_city = employees[employees['Hometown'] == city]
    return filtered_data_city

selected_city = st.sidebar.selectbox("Seleccionar ciudad", employees['Hometown'].unique())
btnFilterCity = st.sidebar.button('Filtrar ciudad')

if(btnFilterCity):
    filterbycity = filter_data_by_city(selected_city)
    count_row = filterbycity.shape[0] # Numero de filas
    st.dataframe(filterbycity)
    st.write(f"Total de empleados por la ciudad seleccionada: {count_row}")

st.markdown("___")
st.header('Filtrado de Empleados por Unidad')

@st.cache
def filter_data_by_unit(unidad):
    filtered_data_unit = employees[employees['Unit'] == unidad]
    return filtered_data_unit

selected_unit = st.sidebar.selectbox("Seleccionar unidad", employees['Unit'].unique())
btnFilterUnit = st.sidebar.button('Filtrar unidad')

if(btnFilterUnit):
    filterbyunit = filter_data_by_unit(selected_unit)
    st.dataframe(filterbyunit)

# -- HISTOGRAMA -- #
    
st.markdown("___")
st.header('Histograma de Empleados por Edad')

fig,ax = plt.subplots()
ax.hist(employees['Age'])
ax.set_xlabel('Edad')
ax.set_ylabel('Cantidad de empleados')
st.pyplot(fig)

st.markdown("___")
st.header('Gráfica de Frecuencias')

# -- GRAFICA DE FRECUENCIAS -- #

fig2 = sns.countplot(x = employees['Unit'])
plt.xticks(rotation=90)
figa = fig2.figure
st.pyplot(figa)

st.markdown("___")
st.header('Gráfica de ciudades con indice de diserción')

# -- HOMETOWN & ATTRITION RATE -- #

fig3, ax3 = plt.subplots()

y_pos = employees['Hometown']
x_pos = employees['Attrition_rate']

ax3.barh(y_pos, x_pos)
ax3.set_ylabel('Ciudades')
ax3.set_xlabel('Tasa de diserción')
st.pyplot(fig3)
st.write('La ciudad (Hometown) con el mayor indice de diserción (Attrition_rate) es Clinton. Seguido de Springfield y posteriormente Washington.')

st.markdown("___")
st.header('Gráfica de edad y tasa de diserción')

# -- AGE & ATTRITION RATE -- #

fig4, ax4 = plt.subplots()

ax4.scatter(employees['Age'], employees['Attrition_rate'])
ax4.set_xlabel('Edad')
ax4.set_ylabel('Tasa de diserción')

st.pyplot(fig4)
st.write('Podemos observar la gráfica de disperción entre Edad y Tasa de diserción, donde obtenemos una correlación negativa entre dichos campos.')

st.markdown("___")
st.header('Gráfica de tiempo de servicio y tasa de diserción')

# -- TIME OF SERVICE & ATTRITION RATE -- #

fig5, ax5 = plt.subplots()

ax5.scatter(employees['Time_of_service'], employees['Attrition_rate'])
ax5.set_xlabel('Tiempo de servicio')
ax5.set_ylabel('Tasa de diserción')

st.pyplot(fig5)
st.write('Podemos observar la gráfica de disperción entre el Tiempo de servicio y Tasa de diserción, donde obtenemos una correlación negativa entre dichos campos.')