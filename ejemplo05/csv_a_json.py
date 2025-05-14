import csv
import json

# Ruta del archivo CSV de entrada
csv_file = '/home/alex/Escritorio/plataformas_web/clase04-1bim-AlexJavierQ/ejemplo05/atp_tennis.csv'

# Ruta del archivo JSON de salida
json_file = '/home/alex/Escritorio/plataformas_web/clase04-1bim-AlexJavierQ/ejemplo05/tennis.json'

# Leer el archivo CSV con una codificación diferente (por ejemplo, 'latin1')
with open(csv_file, mode='r', encoding='latin1') as f:
    lector = csv.DictReader(f)
    datos = list(lector)

# Guardar los datos como JSON
with open(json_file, mode='w', encoding='utf-8') as f:
    json.dump(datos, f, indent=4, ensure_ascii=False)

print(f'Archivo convertido correctamente: {json_file}')
