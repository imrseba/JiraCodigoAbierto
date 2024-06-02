import streamlit as st
from datetime import datetime, timedelta
from firebase_utils import crear_hito_grupo, obtener_hitos_sprint

def crear_hito_app(clave_acceso):
    st.title("Crear Nuevo Hito")

    sprints = obtener_hitos_sprint(clave_acceso)
    sprint_list = [sprint['sprint'] for sprint in sprints.values()] if sprints else []
    # Generar una clave única para el segundo selectbox usando el hash de los nombres de los sprints
    sprint_selectbox_key = "sprint_selectbox_" + str(hash("".join(sprint_list)))

    st.subheader("Seleccione el sprint al que desea agregar un hito:")
    selected_sprint = st.selectbox("Selecciona un Sprint:", sprint_list, key=sprint_selectbox_key)

    if selected_sprint:
        grupo_id_sprint = next((key for key, value in sprints.items() if value['sprint'] == selected_sprint), None)
        fecha_entrega_str = sprints[grupo_id_sprint]['fecha_entrega']
        fecha_entrega_sprint = datetime.fromisoformat(fecha_entrega_str)
        
        # Verificar si la fecha actual es al menos 5 días antes de la fecha de entrega del sprint
        fecha_limite = fecha_entrega_sprint - timedelta(days=1)
        fecha_actual = datetime.now()
        # Calcular los días restantes
        dias_restantes = (fecha_limite - fecha_actual).days
        
        if dias_restantes < 0:
            st.error("No se puede agregar el hito. Debe ser al menos 1 dia antes de la fecha de entrega del sprint.")
        else:
            st.info(f"Quedan {dias_restantes} días para agregar hitos a este sprint.")
            nuevo_hito = st.text_input("Nuevo Hito:", key="hito_input")
            descripcion = st.text_area("Descripción del Hito:", key="descripcion_input")
            if st.button("Agregar Hito", key="agregar_hito_button"):
                if nuevo_hito:
                    crear_hito_grupo(nuevo_hito,descripcion,clave_acceso, grupo_id_sprint)
                    st.success("¡Hito agregado exitosamente!")
                else:
                    st.error("Por favor, ingrese el nombre del hito.")


