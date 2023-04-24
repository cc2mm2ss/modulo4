import requests
import mysql.connector

try:
    cnx = mysql.connector.connect(user='admin', password='mmodulo7',
                              host='modulo7.c3cxjop410af.us-east-2.rds.amazonaws.com',
                              database='modulo7')
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
  cnx.close()

# Creación del cursor
cursor = conexion.cursor()

# Ejecución de la consulta
cursor.execute("SELECT CIUDAD FROM parametros")

# Lectura del resultado
ciudad = cursor.fetchone()[0]
clave_api = "d3a0dc6559b5876cb562b3568c100971"
url = f"https://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={clave_api}&units=metric"
fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

respuesta = requests.get(url)

datos = respuesta.json()

temperatura = datos["main"]["temp"]
sensacion_termica = datos["main"]["feels_like"]
descripcion = datos["weather"][0]["description"]

print(f"El tiempo en {ciudad} es {descripcion}")
print(f"La temperatura es de {temperatura}°C")
print(f"La sensación térmica de {sensacion_termica}°C")
print(f"------")

cursor.execute("INSERT INTO salida (FECHA, CIUDAD, TEMPERATURA, SENSACION) VALUES (%s, %s, %s, %s)",
               (fecha_actual, ciudad, round(temperatura, 2), round(sensacion_termica, 2)))

cnx.commit()
cnx.close()
