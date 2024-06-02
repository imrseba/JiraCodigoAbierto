import streamlit as st
from firebase_utils import obtener_hitos_sprint


def ver_sprint_app(clave_acceso):
    st.sidebar.title("Ver Sprint")
    
    #Obtener sprints 
    sprints = obtener_hitos_sprint(clave_acceso)
    sprint_list = [sprint['sprint'] for sprint in sprints.values()] if sprints else []

    if not sprint_list:
        st.sidebar.warning("No hay sprints disponibles.")
        return
    
    # Mostrar la lista de sprints existentes
    st.sidebar.subheader("Sprints existentes:")
    selected_sprint = st.sidebar.selectbox("Seleccione el sprint que desea ver:", sprint_list)

    if selected_sprint:

        # Obtener el ID del sprint seleccionado
        grupo_id_sprint = next((key for key, value in sprints.items() if value['sprint'] == selected_sprint), None)
    
        st.sidebar.write("Sprint Seleccionado: ", selected_sprint)
        st.sidebar.write("Fecha de entrega: ", sprints[grupo_id_sprint]['fecha_entrega'])
        hitos = sprints[grupo_id_sprint].get('hitos')
        if not hitos:
            st.sidebar.write("No hay hitos en este sprint.")
        else:
            st.sidebar.write("Cantidad de Hitos: ", len(hitos))
        
