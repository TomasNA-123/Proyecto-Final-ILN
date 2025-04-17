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
Para el correcto funcionamiento del backend, es necesario configurar las variables de entorno que contienen las API keys de Gemini y Foursquare. Sigue estos pasos:

1. Crea un archivo `.env` en la carpeta `back-proyecto-ILN`
2. Configura las siguientes variables en el archivo:
   ```
   GEMINI-API-KEY="tu-api-key-de-gemini"
   FOURSQUARE-API-KEY="tu-api-key-de-foursquare"
   ```
3. Obtén las API keys en:
   - Gemini API key: https://aistudio.google.com/app/apikey
   - Foursquare API key: https://developer.foursquare.com/

#### Importar librerias
Las librerías Python utilizadas para el back se encuentran en el archivo requirements.txt para instalar todas las librerías con un solo comando en terminal se puede utilizar el comando:
-	pip install -r requirements.txt

#### Ejecutar API
por último, para ejecutar el api se utiliza el comando:
-	Python main.py
