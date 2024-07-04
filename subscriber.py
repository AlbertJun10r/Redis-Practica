import redis
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

# Crear un suscriptor
pubsub = r.pubsub()
pubsub.subscribe('canal_test')

print("Esperando mensajes...")

# Procesar mensajes en tiempo real
for message in pubsub.listen():
    if message['type'] == 'message':
        print(f"Mensaje recibido: {message['data'].decode('utf-8')}")
