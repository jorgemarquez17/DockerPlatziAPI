# DockerPlatziAPI

se debe crear un Dockerfile: 
	Ejemplo:
	**********************************************
	*	FROM python:3.11						                 *
	*											                         *
	*	WORKDIR /app							                   *
	*											                         *
	*	COPY requirements.txt requirements.txt	     *
	*	RUN pip install -r requirements.txt		       *
	*											                         *
	*	COPY . .								                     *
	*											                         *
	*	EXPOSE 8080								                   *
	*											                         *
	*	CMD ["python", "app.py"]				             *
	**********************************************

	comando para crear imagen:  docker build -t nameimages:latest .
								docker images
	comando para borrar imagen docker rmi -f IdImage


	Crear contenedor:	
		verificar contenedores : docker ps
		Correr images : docker run -it --rm -d -p 8080:8080 --name namecontenedor nameimages

		-it modo iteractivo
		--rm remove eliminar cualquier version del contenedor previamente ejecutandose
		-d se ejecuta en un segundo plano 
		-p 8080:8080 escribir el puerto con que nos vamos a comunicar del contenedor a al aplicacion
		--name nombre del contenedor seguirdo de la imagen ejemplo: webapp nameimages
