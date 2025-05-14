import requests
import json

# Configuración directa
COUCHDB_URL = "http://127.0.0.1:5984"
DB_NAME = "personas06"
USERNAME = "alex"
PASSWORD = "danmachi12"

# Ruta al archivo JSON
with open('/home/alex/Escritorio/plataformas_web/clase04-1bim-AlexJavierQ/ejemplo05/tennis.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Construir el cuerpo para _bulk_docs
bulk_data = {
    "docs": data
}

# URL para _bulk_docs
url = f"{COUCHDB_URL}/{DB_NAME}/_bulk_docs"
headers = {'Content-Type': 'application/json'}

# Enviar todos los documentos de una vez
response = requests.post(
    url,
    json=bulk_data,
    auth=(USERNAME, PASSWORD),
    headers=headers
)

# Mostrar resultado
if response.status_code == 201:
    print("Documentos insertados correctamente.")
else:
    print(f"Error al insertar: {response.status_code}")
    print(response.text)
