import firebase_admin
from firebase_admin import credentials, db

def initialize_firebase():
    if not firebase_admin._apps:
        # Ruta al archivo JSON de credenciales de servicio
        firebase_sdk = credentials.Certificate('proyectoagilescalado-firebase-adminsdk-7rd33-f5e91e8997.json')

        # Inicializar la aplicación Firebase solo si no está inicializada
        firebase_admin.initialize_app(firebase_sdk, {'databaseURL': 'https://proyectoagilescalado-default-rtdb.firebaseio.com/'})


def obtener_grupo(clave_acceso):
    ref_grupo = db.reference('Grupos/'+clave_acceso)
    return ref_grupo.get()

def crear_sprint_grupo(sprint,fecha_entrega,grupo_id):
    ref_sprints = db.reference(f'Grupos/{grupo_id}/sprints')
    ref_sprints.push({
        'sprint': sprint,
        'cumplido': False,
        'fecha_entrega': fecha_entrega
    })

def crear_hito_grupo(hito,descripcion,grupo_id,sprint_id):
    ref_hitos = db.reference(f'Grupos/{grupo_id}/sprints/{sprint_id}/hitos')
    ref_hitos.push({
        'hito': hito,
        'cumplido': False,
        'descripcion': descripcion
    })

def obtener_hitos_sprint(grupo_id):
    ref_sprints = db.reference(f'Grupos/{grupo_id}/sprints')
    return ref_sprints.get()

def obtener_hitos_grupo(grupo_id,sprint_id):
    ref_hitos = db.reference(f'Grupos/{grupo_id}/sprints/{sprint_id}/hitos')
    return ref_hitos.get()

def eliminar_hito(grupo_id,sprint_id,hito_id):
    ref_hito = db.reference(f'Grupos/{grupo_id}/sprints/{sprint_id}/hitos/{hito_id}')
    ref_hito.delete()

def eliminar_sprint_grupo(grupo_id,sprint_id):
    ref_sprint = db.reference(f'Grupos/{grupo_id}/sprints/{sprint_id}')
    ref_sprint.delete()

def obtener_id_grupo(clave_acceso):
    
    ref_grupo = db.reference('Grupos')
    grupos = ref_grupo.get()
    for grupo in grupos:
        if grupo == clave_acceso:
            return grupo
    return None