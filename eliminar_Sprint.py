import streamlit as st
from firebase_utils import obtener_hitos_sprint, eliminar_sprint_grupo

def eliminar_sprint_app(clave_acceso):
    st.sidebar.title("Eliminar Sprint")

    # Obtener los sprints existentes
    sprints = obtener_hitos_sprint(clave_acceso)
    sprint_list = [sprint['sprint'] for sprint in sprints.values()] if sprints else []

    if not sprint_list:
        st.sidebar.warning("No hay sprints disponibles para eliminar.")
        return

    # Mostrar la lista de sprints existentes
    st.sidebar.subheader("Sprints existentes:")
    selected_sprint = st.sidebar.selectbox("Seleccione el sprint que desea eliminar:", sprint_list)

    if selected_sprint:
        # Obtener el ID del sprint seleccionado
        grupo_id_sprint = next((key for key, value in sprints.items() if value['sprint'] == selected_sprint), None)

        if st.sidebar.button("Eliminar Sprint"):
            eliminar_sprint_grupo(clave_acceso, grupo_id_sprint)
            st.sidebar.success("¡Sprint eliminado exitosamente!")
            st.experimental_rerun()