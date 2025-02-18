import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración de la página
st.set_page_config(page_title="CrediVision Dashboard", layout="wide")

# Sidebar
st.sidebar.title("Roles")
st.sidebar.button("Técnico")
st.sidebar.button("Analista")

# Título principal
st.markdown("# CrediVision")
st.markdown("## Home Dashboard")

# Layout de columnas
col1, col2, col3 = st.columns([1, 2, 1])

# Perfiles de Riesgo
with col1:
    st.markdown("### Perfiles Alto Riesgo")
    st.markdown("- **Ingresos Promedio:** _XXXX_")
    st.markdown("- **Estado Vivienda:** _XXXX_")
    st.markdown("- **Ahorros:** _XXXX_")
    st.markdown("- **Vehículo:** _XXXX_")
    st.markdown("- **Propósitos más comunes:** _XXXX_")

with col3:
    st.markdown("### Perfiles Bajo Riesgo")
    st.markdown("- **Ingresos Promedio:** _XXXX_")
    st.markdown("- **Estado Vivienda:** _XXXX_")
    st.markdown("- **Ahorros:** _XXXX_")
    st.markdown("- **Vehículo:** _XXXX_")
    st.markdown("- **Propósitos más comunes:** _XXXX_")

# Gráfico de Histograma de Riesgos
with col2:
    st.markdown("### Histograma de Riesgos por perfil")
    fig, ax = plt.subplots()
    data = np.random.randn(100)  # Datos de ejemplo
    ax.hist(data, bins=20, color="magenta", alpha=0.7)
    st.pyplot(fig)

# Sección Inferior - Alternativa a Matriz Covarianza
col4, col5 = st.columns([1, 1])

with col4:
    st.markdown("### Distribución de Variables por Perfil")
    fig, ax = plt.subplots()
    categorias = ['Ingresos', 'Ahorros', 'Deudas', 'Edad']
    valores = np.random.rand(4)
    ax.bar(categorias, valores, color=['blue', 'green', 'red', 'purple'])
    st.pyplot(fig)

with col5:
    st.markdown("### Insights")
    st.markdown("- Los perfiles de alto riesgo tienen menores ahorros.")
    st.markdown("- Los ingresos tienden a correlacionar con menor riesgo.")
    st.markdown("- La edad media de los perfiles de bajo riesgo es mayor.")

# Sección de Clusters
st.markdown("### Filtro de individuos por cluster")
clusters = ['0', '1', '2', '3']
variables = ['Ingresos', 'Ahorros', 'Edad', 'Deuda']

seleccion_clusters = st.multiselect("Selecciona Clusters", clusters, default=clusters)
seleccion_variables = st.multiselect("Selecciona Variables", variables, default=variables)

df = pd.DataFrame(np.random.rand(10, len(variables)), columns=variables)
st.dataframe(df)
