# Proyecto Final
Este trabajo incorpora técnicas de análisis de datos para buscar en la web las mejores recomendaciones de restaurantes en base a lo que busque el usuario utilizando en el backend una API Python con Flask y en el frontend React

## ¿Cómo ejecutar el proyecto?

### Frontend
Toda la parte de frontend se encuentra en la carpeta “front-proyecto-ILN”, por lo que los comandos serealizan dentro de este fichero en la terminal.
Los comandos para ejecutar son:
-	Npm install
-	Npm run dev

### Backend
Para la parte de backend recomiendo abrir otra terminal para poder ejecutar tanto el React como el flask más adelante. Todo el código del back se encuentra en la carpeta “back-proyecto-ILN”.

#### Crear entorno virtual
Antes de empezar a trabajar es necesario crear un entorno virtual, en el caso de este proyecto se utilizo virtualenv y se creó con el siguiente comando, pero puede hacerse con otro de su preferencia
-	virtualenv env

para activar el entorno virtual se usa el comando:
-	source env/bin/activate

#### Variables de entorno
Además, se utilizan variables de entorno para guardar la apikey de Gemini, se dejo un fichero llamado .env-example este fichero se tiene que renombrar a .env e indicar la apikey.

#### Importar librerias
Las librerías Python utilizadas para el back se encuentran en el archivo freeze.txt para instalar todas las librerías con un solo comando en terminal se puede utilizar el comando:
-	pip install -r freeze.txt

#### Ejecutar API
por último, para ejecutar el api se utiliza el comando:
-	Python main.py
