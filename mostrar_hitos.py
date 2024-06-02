import streamlit as st
from firebase_utils import obtener_hitos_grupo, obtener_hitos_sprint
import pandas as pd
def mostrar_hitos_app(clave_acceso):
    st.title("Mostrar hitos por Sprint")

    # Obtener los sprints
    sprints = obtener_hitos_sprint(clave_acceso)
    sprint_list = [sprint['sprint'] for sprint in sprints.values()] if sprints else []

    selected_sprint = st.selectbox("Selecciona un Sprint:", sprint_list, key="sprint_selectbox_" + clave_acceso)

    if selected_sprint:
        grupo_id_sprint = next((key for key, value in sprints.items() if value['sprint'] == selected_sprint), None)

        # Obtener los hitos del grupo y del sprint seleccionado
        hitos = obtener_hitos_grupo(clave_acceso, grupo_id_sprint)
        hitos_list = [hito['hito'] for hito in hitos.values()] if hitos else []
        descripcion_list = [hito['descripcion'] for hito in hitos.values()] if hitos else []

        #Mostrar ambas listas en una tabla que diga, el hito y su descripción

        data = {'Hito': hitos_list, 'Descripción': descripcion_list}
        df = pd.DataFrame(data)

        # Mostrar la tabla en Streamlit
        st.subheader('Hitos '+selected_sprint)
        st.table(df)
        
        
