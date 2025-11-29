# Core Packages
import streamlit as st 
import pandas as pd 
import plotly.express as px 
import pydeck as pdk


def main():
	st.title("APP DE VISUALIZACION")


	menu = ["Home","Data","Acerca de"]
	choice = st.sidebar.selectbox("Menu",menu)

	if choice == "Home":
		st.subheader("Home: APP DE VISUALIZACION")
		st.image('img/¿Qué factores influyen más en el éxito de un cortejo?.png', caption=None)

		# Tabs
		tab1,tab2 = st.tabs(["Tab 1","Tab 2"])

		with tab1:
			with st.expander("Tab 1"):
				st.write("Texto para Tab 1")

		with tab2:
			with st.expander("Tab 2"):
				st.write("Texto para Tab 2")


		#Gráficos
	


	elif choice  == "Data":
		st.subheader("Data: Información de Empresa")

		# Tabs
		tab3,tab4 = st.tabs(["Tab 3","Tab 4"])

		with tab3:
			with st.expander("Tab 3"):
				st.write("Texto para Tab 3")

		with tab4:
			with st.expander("Tab 4"):
				st.write("Texto para Tab 4")


		#Gráficos





	else:
		st.subheader("Acerca de")
		st.write("App desarrollada para mostrar usabilidad de mapas online con librería pydeck y mapas offline con plotly.")


if __name__ == '__main__':
	main()