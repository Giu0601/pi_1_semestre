import mysql.connector as cpy
import os

env_host = os.getenv('HOST_DB')
env_user = os.getenv('USER_DB')
env_pass = os.getenv('PASS_DB')
env_port = os.getenv('PORT_DB')

def connect_db():
    try:
        cnx = cpy.connect(
            host=env_host,
            port= env_port,
            user=env_user,
            password=env_pass,
            database='jornadamauadb'
        )
    except cpy.Error as err:
        print(f"Erro ao conectar ao MySQL: {err}")
        return None
    return cnx