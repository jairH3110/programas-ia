import streamlit as st
import requests as res

# Título de la aplicación
st.title("App-de-Predicción-con-API")

# Sección para ingresar los valores a predecir
st.header("Ingrese los valores a predecir")

# Input para capturar los valores
valor1 = st.number_input("Valor 1", value=0.0)
valor2 = st.number_input("Valor 2", value=0.0)
valor3 = st.number_input("Valor 3", value=0.0)

# Botón para realizar la predicción
if st.button("Realizar Predicción"):
    # Construir el cuerpo de la solicitud a la API
    data = {
        "instances": [[valor1],[valor2],[valor3]]
    }

    # URL de la API
    api_url = "https://linear-model-service-jairh3110.cloud.okteto.net/v1/models/linear-model:predict"

    try:
        # Realizar la solicitud POST a la API
        response = res.post(api_url, json=data)

        # Verificar si la solicitud fue exitosa (código de estado 200)
        if response.status_code == 200:
            resultado = response.json()
            st.success(f"La predicción es: {resultado}")
        else:
            st.error("Error en la predicción. Por favor, inténtalo nuevamente.")

    except Exception as e:
        st.error(f"Error: {str(e)}")