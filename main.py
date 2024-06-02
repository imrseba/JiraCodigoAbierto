import streamlit as st
from firebase_utils import initialize_firebase, obtener_grupo, obtener_id_grupo
from crear_Hito import crear_hito_app
from crea_Sprint import crear_sprint_app
from eliminar_Hito import eliminar_hito_app
from eliminar_Sprint import eliminar_sprint_app
from ver_Sprint import ver_sprint_app
from mostrar_hitos import mostrar_hitos_app
# Inicializar Firebase al inicio de la aplicación
initialize_firebase()

def main():
    st.title("Aplicacion Desarrollo Agil Escalado")
    
    #Ingresar clave de acceso
    clave_acceso = st.text_input("Ingrese la clave de acceso", type="default")
    resultado = obtener_id_grupo(clave_acceso)
    if(resultado != None):
        grupo = obtener_grupo(clave_acceso)
        st.success("Bienvenido grupo "+grupo["nombreGrupo"])
        crear_sprint_app(clave_acceso)

        crear_hito_app(clave_acceso)

        eliminar_hito_app(clave_acceso)

        eliminar_sprint_app(clave_acceso)

        mostrar_hitos_app(clave_acceso)

        ver_sprint_app(clave_acceso)
    else:
        st.error("Clave de acceso incorrecta")
if __name__ == "__main__":
    main()