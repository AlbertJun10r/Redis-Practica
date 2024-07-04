import redis
import time
from dotenv import load_dotenv
import os

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Obtener las variables de entorno
redis_host = os.getenv('REDIS_HOST')
redis_port = os.getenv('REDIS_PORT')
redis_password = os.getenv('REDIS_PASSWORD')

# Conectar a Redis
r = redis.Redis(host=redis_host, port=redis_port, password=redis_password)

# Publicar mensajes en un canal llamado 'canal_test'
while True:
    message = input("Ingresa un mensaje para publicar: ")
    r.publish('canal_test', message)
    print(f"Mensaje publicado: {message}")
