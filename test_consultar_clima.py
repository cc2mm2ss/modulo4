import requests

ciudad = "Buenos Aires"
clave_api = "d3a0dc6559b5876cb562b3568c100971"
url = f"https://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={clave_api}&units=metric"

respuesta = requests.get(url)

datos = respuesta.json()

temperatura = datos["main"]["temp"]
sensacion_termica = datos["main"]["feels_like"]
descripcion = datos["weather"][0]["description"]

def test_answer():
    assert temperatura >= 0
    assert sensacion_termica >= 0
