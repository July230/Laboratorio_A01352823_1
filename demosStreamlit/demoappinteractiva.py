#pip install streamlit pandas matplotlib pydeck
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Configuración general
st.set_page_config(page_title="Demo App", layout="wide")

# Sidebar con navegación
st.sidebar.title("Menú de Navegación")
page = st.sidebar.radio("Ir a:", ["Inicio", "Análisis de Datos", "Visualización Interactiva"])

# Página: Inicio
if page == "Inicio":
    st.title("Bienvenido a la Aplicación Streamlit Demo")
    st.markdown("Esta aplicación muestra un ejemplo de navegación multipágina con funcionalidades interactivas.")
    
    # Imagen embebida
    st.image("https://www.wikimedia.org/static/images/wmf-logo-2x.png", use_container_width=True)

    st.markdown("---")
    st.subheader("¿Qué puedes hacer aquí?")
    st.markdown("""
    - Visualizar esta introducción.
    - Analizar un archivo cargado (CSV, Excel).
    - Ver gráficos interactivos generados con datos ficticios.
    """)

# Página: Análisis de Datos
elif page == "Análisis de Datos":
    st.title("Carga y Análisis de Datos")
    
    uploaded_file = st.file_uploader("Carga tu archivo (CSV o Excel)", type=["csv", "xlsx"])
    if uploaded_file is not None:
        try:
            if uploaded_file.name.endswith('.csv'):
                df = pd.read_csv(uploaded_file)
            else:
                df = pd.read_excel(uploaded_file)
            
            st.success("Archivo cargado correctamente.")
            st.write("Vista previa de los datos:")
            st.dataframe(df)

            st.markdown("### Estadísticas rápidas:")
            st.write(df.describe())
            
            st.markdown("### Filtro de columnas:")
            col = st.selectbox("Selecciona una columna numérica para graficar", df.select_dtypes(include=np.number).columns)
            fig, ax = plt.subplots()
            df[col].hist(bins=20, ax=ax)
            st.pyplot(fig)
        except Exception as e:
            st.error(f"Ocurrió un error al procesar el archivo: {e}")
    else:
        st.info("Por favor, carga un archivo para comenzar el análisis.")

# Página: Visualización Interactiva
elif page == "Visualización Interactiva":
    st.title("Visualización Interactiva de Datos de Ejemplo")

    # Crear datos de ejemplo
    data = pd.DataFrame({
        "Categoría": ["A", "B", "C", "D"],
        "Valor": np.random.randint(10, 100, 4)
    })

    st.subheader("Datos:")
    st.dataframe(data)

    st.subheader("Gráfico de barras:")
    chart_type = st.radio("Selecciona tipo de gráfico", ["Barras", "Línea"])
    fig, ax = plt.subplots()

    if chart_type == "Barras":
        ax.bar(data["Categoría"], data["Valor"])
    else:
        ax.plot(data["Categoría"], data["Valor"], marker='o')

    st.pyplot(fig)