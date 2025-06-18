# db.py
import mysql.connector

# Cambia esto según tu configuración de Laragon
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': '',  # Por defecto en Laragon, sin contraseña
    'database': 'lenguaje_senas'
}

def insert_traduccion(palabra):
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()
        query = "INSERT INTO traducciones (palabra) VALUES (%s)"
        cursor.execute(query, (palabra,))
        conn.commit()
        cursor.close()
        conn.close()
    except mysql.connector.Error as err:
        print(f"Error al insertar en la base de datos: {err}")
