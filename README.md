# Restgen - API Frontend / Backend Application Generator

Restgen es una herramienta que permite generar aplicaciones de tipo SPA (Single Page Application) a través de la creación de servicios restful y una interfaz gráfica. Restgen se soporta en la librería de python Flask para los servicios de backend, y el framework Angular 4 para soportar el frontend o interfaz gráfica de la aplicación.

Para ejecutar este proyecto ejecute los siguientes comandos:

```
cd api-generator
docker-compose up -d
source bootstrap
restgen --model models/example.yml
cd development
docker-compose build
docker-compse up
```

## Uso de Restgen

restgen --model [Modelo]

Esto generará una carpeta con el nombre srcgen donde se encuentra el código fuente listo para su aplicación tanto
backend como frontend

## Video explicativo
(Debe activar los subtitulos para visualizar la descripción de los pasos)
https://youtu.be/3eOBOM7IqIs
