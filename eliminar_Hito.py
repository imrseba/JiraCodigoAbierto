import streamlit as st
from datetime import datetime, timedelta
from firebase_utils import obtener_hitos_sprint, obtener_hitos_grupo, eliminar_hito

def eliminar_hito_app(clave_acceso):
    st.title("Eliminar Hito del Sprint")

    sprints = obtener_hitos_sprint(clave_acceso)
    sprint_list = [sprint['sprint'] for sprint in sprints.values()] if sprints else []
    sprint_selectbox_key = "sprint_selectbox_" + str(hash("".join(sprint_list) + clave_acceso))

    st.subheader("Seleccione el sprint del que desea eliminar un hito:")
    selected_sprint = st.selectbox("Selecciona un Sprint:", sprint_list, key=sprint_selectbox_key)

    if selected_sprint:
        grupo_id_sprint = next((key for key, value in sprints.items() if value['sprint'] == selected_sprint), None)
        fecha_entrega_str = sprints[grupo_id_sprint]['fecha_entrega']
        fecha_entrega_sprint = datetime.fromisoformat(fecha_entrega_str)

        fecha_limite = fecha_entrega_sprint - timedelta(days=5)
        fecha_actual = datetime.now()
        
        # Calcular los días restantes
        dias_restantes = (fecha_limite - fecha_actual).days

        if dias_restantes < 0:
            st.error("No se puede eliminar el hito. Debe ser al menos 5 días antes de la fecha de entrega del sprint.")
        else:
            st.info(f"Quedan {dias_restantes} días para eliminar hitos de este sprint.")
            hitos = obtener_hitos_grupo(clave_acceso, grupo_id_sprint)
            hitos_list = [hito['hito'] for hito in hitos.values()] if hitos else []
            hitos_selectbox_key = "hito_selectbox_" + str(hash("".join(hitos_list) + grupo_id_sprint))

            st.subheader("Seleccione el hito que desea eliminar:")
            selected_hito = st.selectbox("Selecciona un Hito:", hitos_list, key=hitos_selectbox_key)

            if selected_hito:
                grupo_id_hito = next((key for key, value in hitos.items() if value['hito'] == selected_hito), None)
                eliminar_button_key = "eliminar_hito_button_" + grupo_id_sprint + "_" + grupo_id_hito
                if st.button("Eliminar Hito", key=eliminar_button_key):
                    eliminar_hito(clave_acceso, grupo_id_sprint, grupo_id_hito)
                    st.success("¡Hito eliminado exitosamente!")
                    st.experimental_rerun()