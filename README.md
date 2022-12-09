<p align=center><img src=https://d31uz8lwfmyn8g.cloudfront.net/Assets/logo-henry-white-lg.png><p>

# <h1 align=center> **PROYECTO INDIVIDUAL Nº1 - ARGUMEDO HÉCTOR** </h1>

# <h1 align=center>**`Data Engineering`**</h1>


## **Introducción**

En esta ocasión me encuentro realizando un proyecto para la etapa de Labs para la carrera Data Scientis en laplataforma Henry. 

Como parte fundamental de nuestro entrenamiento, voy a realizar una API que me permita realizar consultas y la misma se encontrará dentro de un contenedor de Docker. 

`Application Programming Interface` es una interfaz que permite que dos aplicaciones se comuniquen entre sí, independientemente de la infraestructura subyacente. Son herramientas muy versátiles y fundamentales para la creación de, por ejemplo, pipelines, ya que permiten mover y brindar acceso simple a los datos que se quieran disponibilizar a través de los diferentes endpoints, o puntos de salida de la API.

Hoy en día contamos con **FastAPI**, un web framework moderno y de alto rendimiento para construir APIs con Python.
<p align=center>
<img src = 'https://images.squarespace-cdn.com/content/v1/5df3d8c5d2be5962e4f87890/1580626510144-Y6C73XYMHKFRTCY1TW74/apipy-logo.png?format=1000w' height=250><p>

## **Propuesta de trabajo**

El proyecto consiste en realizar una ingesta de datos desde diversas fuentes, posteriormente aplicar las transformaciones que consideren pertinentes, y luego disponibilizar los datos limpios para su consulta a través de una API. Esta API deberán construirla en un entorno virtual dockerizado.

Los datos son provistos en archivos de diferentes extensiones, como *csv* o *json*. Se espera que realice un EDA para cada dataset y se corrijan los tipos de datos, valores nulos y duplicados, entre otras tareas. Posteriormente, hay que relacionar los datasets así pueden acceder a su información por medio de consultas a la API.

Las consultas a realizar son:

+ Máxima duración según tipo de film (película/serie), por plataforma y por año:
    El request debe ser: get_max_duration(año, plataforma, [min o season])

+ Cantidad de películas y series (separado) por plataforma
    El request debe ser: get_count_plataform(plataforma)  
  
+ Cantidad de veces que se repite un género y plataforma con mayor frecuencia del mismo.
    El request debe ser: get_listedin('genero')  
    Como ejemplo de género se puede usar 'comedy', el cuál deberia devolver un cunt de 2099 para la plataforma de amazon.

+ Actor que más se repite según plataforma y año.
  El request debe ser: get_actor(plataforma, año)

<p align=center>
<img src = 'https://bitestreams.com/blogs/fastapitemplate/logos.webp' height = 400></p>



## **Pasos realizados en el proyecto:**
+ Como primera instancia se realiza un  EDA (Analisis Exploratorio de Datos)

+ Una vez analizados los datos se procede con un ETL (Extracción, Transformación y Carga) de dichos datos

+ Dado que las consultas a realizar a travez de la API solo exigen cierta cantidad de datos se procede a eliminar las columnas innecesarias, siempre dejando previamente, un dataset completo con el EDA y el ETL realizado del paso anterior. Esto en caso de que se debiera retomar los mismos datos para futuras consultas diferentes a las planteadas para este proyecto. 

+ Se procede a generar una API que me permita generar las consultas por medio de funciones y levantar una interfaz visual en el navegador por medio de la erramienta UVICORN. 

+ Una ves verificado el funcionamiento de la API se procede a Dokerizar el proyecto utilizando una imagen de PYTHON 3.10.5

+ Cuando el proyecto ya es viable y esta probado se sube a Git-Hub

+ Como Plus se despliega un contenedor en https://mogenius.com/




<p align=center>
<img src = 'https://res.cloudinary.com/practicaldev/image/fetch/s--iOsUGN0b--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/uploads/articles/l4jt274288k241g94r66.png' height = 200></p>

## **Pueden ver y probar mi API dokerizada en el siguiente link:** 
https://proyecto-01-da-prod-proyecto01-labs-zn95mo.mo1.mogenius.io/docs
## **Pueden ver el video resumen de como realizé este proyecto en el siguiente link:**

## **Conceptos de interés**

- **`Docker`** es una solución completa para la producción, distribución y uso de containers.  
&nbsp;- **`Container`** es una abstracción de la capa de software que permite *empaquetar* código, con librerías y dependencias en un entorno parcialmente aislado.  
&nbsp;- **`Image`** es un ejecutable Docker que tiene todo lo necesario para correr aplicaciones, lo que incluye un archivo de configuración, variables -de entorno y runtime- y librerías.  
&nbsp;- **`Dockerfile`** archivo de texto con instrucciones para construir una imagen. Puede considerarse la automatización de creación de imágenes.  
- **`Deployment`** es el conjunto de actividades, infraestructura y recursos que posibilitan el uso de software. En este caso, la plataforma Mogenius les permitirá *montar* su imagen de Docker con la API en sus servidores para acceder a ella a través de internet.

## **Recursos y links provistos**

Imagen Docker con Uvicorn/Guinicorn para aplicaciones web de alta performance:

+ https://hub.docker.com/r/tiangolo/uvicorn-gunicorn-fastapi/ 

+ https://github.com/tiangolo/uvicorn-gunicorn-fastapi-docker

Mogenius Deployment

+ https://mogenius.com/home  

FAST API Documentation:

+ https://fastapi.tiangolo.com/tutorial/


## **Fuente de datos**

+ Podrán encontrar los archivos con datos en la carpeta Datasets, en este mismo repositorio.<sup>*</sup>

  
<p align=center>
<img src = 'https://www.diariopopular.com.ar/mrf4u/statics/i/ps/media.diariopopular.com.ar/p/e03642b80789e7e9fde120acdd5347f1/adjuntos/143/imagenes/004/802/0004802048/homero-computadorajpg.jpg' height = 300></p>
