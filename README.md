# Twitter Reloaded

## participantes :

### Andrea Melissa Rincon Trejo A01365736

### Otoniel Baeza Varela A01561804

Este es el esqueleto de una pplicacion similar a Twitter llamada "Twitter Reloaded"

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

<<<<<<< HEAD
## principios Solid y patrones de Diseño
=======
## DESIGN PATTERNS
#Data Access Object (DAO) Pattern. El patrón DAO se basa en la idea de tener una interfaz común que define las operaciones de acceso a datos, como insertar, actualizar, eliminar y consultar registros. Luego, se implementa esta interfaz en clases concretas que interactúan directamente con la fuente de datos, como una base de datos.
Nuestro programa cuenta con una clase llamada tweet_manager, la cual cumple con este patrón ya que es la encargada de gestionar los tweet directamente con la base de datos, así permitiendo la modularización y dependencia entre funcionalidades.

#Dependency Injection (DI) Pattern. Como parte complementaria del patrón anterior, se creó una instancia de la clase Database y se pasa como argumento al constructor de las clases AuthenticationService y Tweet_manager. Esto significa que estas clases dependen de la interfaz proporcionada por la clase Database, pero no están directamente acopladas a una implementación específica de la base de datos por lo que el patrón DI también puede ser identificado en nuestro proyecto ya que de manera objetiva este patrón se utiliza para inyectar las dependencias en un objeto desde el exterior, en lugar de crearlas internamente.

#Design pattern uses Mvc
se pueden identificar elementos del patrón en la separación de la lógica del programa en las siguientes representaciones:
Modelo (Model): El modelo se representa mediante las clases Database, User, AuthenticationService y Tweet_manager. Estas clases se encargan de interactuar con la base de datos, gestionar la autenticación de usuarios y administrar los tweets y comentarios.
Vista (View): Las vistas se encuentran en la carpeta "templates" y se definen mediante las plantillas HTML. Los métodos de Flask, como render_template, se utilizan para renderizar las plantillas y enviarlas al cliente. Los archivos HTML como "Home.html", "newTweet.html", "DashBoard.html", "details.html" y "Event_Dash.html" representan las vistas que se mostrarán al usuario.
Controlador (Controller): Los controladores se implementan mediante las rutas de Flask y las funciones asociadas a ellas. En este caso, las funciones hello_world(), login_check(), create_tweet(), board(), details(), events(), submit(), insert_comment() e insert_tweet() son los controladores que manejan las solicitudes HTTP y procesan la lógica de negocio correspondiente. Estas funciones interactúan con los modelos para obtener y manipular los datos, y luego devuelven las vistas adecuadas al cliente.

## SOLID PRACTICES

Principio de Responsabilidad Única (SRP): Cada clase tiene una única responsabilidad y propósito definido. Por ejemplo, la clase Tweet se encarga de representar un tweet con sus atributos, la clase User representa un usuario y la clase Event representa un evento. Además, el archivo main.py se encarga de la lógica principal de la aplicación, mientras que el archivo database.py se ocupa de la interacción con la base de datos. Esto demuestra una separación clara de responsabilidades.

Principio de Abierto/Cerrado (OCP): El principio OCP se puede observar en main.py, la funcionalidad de agregar nuevos eventos o tweets se realizan a través de métodos como create_tweet y insert_comment, lo que permite extender la funcionalidad sin necesidad de modificar el código existente.

Principio de Sustitución de Liskov (LSP): Las clases Tweet, User y Event siguen este principio, ya que pueden ser utilizadas en diferentes partes del código sin afectar el comportamiento esperado del programa. Esto se evidencia en el uso de estas clases, como en la función insert_comment de main.py, donde se crea un objeto User para representar al autor del comentario.

Principio de Segregación de la Interfaz (ISP): Dentro del código, se puede observar que los métodos en las capas y clases están asignados de manera que no generan dependencias innecesarias con otras clases o clientes.Por ejemplo, en la clase Tweet_manager, los métodos se centran en la gestión de tweets y la interacción con la base de datos. No hay métodos que exponen funcionalidades irrelevantes o que generen dependencias innecesarias con otras clases o clientes. Los métodos están diseñados de forma coherente y específica para la gestión de tweets.

El principio de Inversión de Dependencias (DIP): esta práctica se puede observar en el archivo main.py, donde se implementa el mecanismo de Inyección de Dependencias (DI) para gestionar las dependencias externas, como la base de datos y los servicios de autenticación.
En lugar de que el código dependa directamente de implementaciones concretas de estas dependencias, se utilizan interfaces o clases abstractas que representan los módulos o métodos pero de manera externa o  independiente. Luego, estas dependencias se inyectan en el código a través de parámetros de constructor o métodos, en lugar de ser instanciadas directamente en el código.


>>>>>>> 28c25edf6316df83b356ec15c5046b10e508c72d
