import streamlit as st
from firebase_utils import crear_sprint_grupo

def crear_sprint_app(clave_acceso):
    st.sidebar.title("Crear Nuevo Sprint")

    # Generar una clave única para el input de texto del sprint
    sprint_input_key = f"sprint_input_{clave_acceso}"

    nuevo_Sprint = st.sidebar.text_input("Nuevo Sprint:", key=sprint_input_key)
    fecha_entrega_sprint = st.sidebar.date_input("Fecha de entrega del Sprint:")
    fecha_entrega_sprint = fecha_entrega_sprint.isoformat()

    # Generar una clave única para el botón de agregar sprint
    agregar_sprint_button_key = f"agregar_sprint_button_{clave_acceso}"

    if st.sidebar.button("Agregar Sprint", key=agregar_sprint_button_key):
        if nuevo_Sprint:
            crear_sprint_grupo(nuevo_Sprint, fecha_entrega_sprint, clave_acceso)
            st.success("¡Sprint agregado exitosamente!")
        else:
            st.error("Por favor, ingrese el nombre del Sprint.")


