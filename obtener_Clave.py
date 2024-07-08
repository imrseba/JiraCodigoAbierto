import streamlit as st
from firebase_utils import obtener_clave_acceso

def obtener_clave():
    st.sidebar.title("Obtener Clave de Acceso")

    correo = st.sidebar.text_input("Ingrese su correo", type="default")
    nombreGrupo = st.sidebar.text_input("Ingrese el nombre del grupo", type="default")

    enviar_button = st.sidebar.button("Enviar")
    if enviar_button:
        clave_acceso = obtener_clave_acceso(correo, nombreGrupo)
        if clave_acceso:
             st.sidebar.markdown(f"**Su clave de acceso es:**\n\n{clave_acceso}")
        else:
            st.sidebar.error("No se encontró la clave de acceso. Verifique los datos ingresados.")
