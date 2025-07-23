import requests
import subprocess
import datetime

def obtener_clima():
    ciudad = "Buenos Aires,AR" # Replace with your city and country
    api_key = "api key" # Replace with your actual API key

    url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&units=metric&lang=es"
    r = requests.get(url)
    data = r.json()

    if "weather" not in data:
        return f"Error al obtener el clima: {data.get('message', 'respuesta inesperada')}"

    clima = data["weather"][0]["description"]
    temp = round(data["main"]["temp"], 1)
    sensacion = round(data["main"]["feels_like"], 1)

    return f"Ahora en {ciudad}: el clima es {clima}, temperatura de {temp}°C (sensación térmica: {sensacion}°C)"

def notificar(mensaje):
    # Show notification on linux
    subprocess.run(["notify-send", "Asistente", mensaje], stderr=subprocess.DEVNULL)

def ejecutar_bot():
    ahora = datetime.datetime.now().strftime('%H:%M')
    mensaje = f"{ahora} - {obtener_clima()}"
    print(mensaje)
    notificar(mensaje)

if __name__ == "__main__":
    ejecutar_bot()
