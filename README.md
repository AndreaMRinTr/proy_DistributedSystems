# Twitter Reloaded

## participantes :

### Andrea Melissa Rincon Trejo A01365736

### Otoniel Baeza Varela A01561804

Este es el esqueleto de una pplicacion similar a Twittre llamada "Twitter Reloaded"

## Prerequisitos

- Docker
- Python 3

## Construir la imagen de Docker

Para construir la imagen de Docker para la aplicación Flask, sigue estos pasos:

1. Clona el repositorio en tu máquina local.
2. Abre una terminal y navega hasta el directorio raíz del repositorio.
3. Ejecuta el siguiente comando para construir la imagen de Docker:

docker build -t my-flask-app .

Esto construirá una imagen de Docker llamada "my-flask-app" utilizando las instrucciones del Dockerfile.

## Ejecutar la aplicación Flask

Para ejecutar la aplicación Flask utilizando la imagen de Docker, sigue estos pasos:

1. Abre una terminal y ejecuta el siguiente comando para iniciar un contenedor de Docker desde la imagen:

docker run -p 5000:5000 my-flask-app

Esto iniciará un contenedor de Docker y mapeará el puerto 5000 en el contenedor al puerto 5000 en tu máquina local.

2. Abre un navegador web y navega hasta http://localhost:5000/ para ver la aplicación Flask.

## Solución de problemas

Si tienes problemas para construir o ejecutar la imagen de Docker, asegúrate de que Docker esté instalado y funcionando en tu máquina. También puedes intentar ejecutar los comandos de Docker con permisos elevados (por ejemplo, usando `sudo`).

Si encuentras algún otro problema, consulta la documentación de [Flask](https://flask.palletsprojects.com/) o de [Docker](https://docs.docker.com/) para obtener más información.
