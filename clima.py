

import requests
API_KEY = "25006f2f0779f27f0f8b0a01b3acef01"


def obtener_clima(ciudad):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={"25006f2f0779f27f0f8b0a01b3acef01"}&units=metric'
    respuesta = requests.get(url)
    datos_clima = respuesta.json()

    if datos_clima['cod'] == 200:
        clima_principal = datos_clima['weather'][0]['main']
        descripcion_clima = datos_clima['weather'][0]['description']
        temperatura_actual = datos_clima['main']['temp']
        humedad = datos_clima['main']['humidity']

        print(f'Ciudad: {ciudad}')
        print(f'Estado del tiempo: {clima_principal} - {descripcion_clima}')
        print(f'Temperatura: {temperatura_actual}°C')
        print(f'Humedad: {humedad}%')
    else:
        print('No se pudo obtener el clima para la ciudad especificada.')
if __name__ == '__main__':
    ciudad = input('Ingresa el nombre de la ciudad para obtener el clima: ')
    obtener_clima(ciudad)