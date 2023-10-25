
# API para el centro medico Galenos

## Tabla de Contenidos:

- [Prerrequisitos](#uno)
    - [Python](#dos)
    - [WSL](#tres)
    - [Docker](#cuatro)
- [Instrucciones de uso](#cinco)
    - [Entorno Virtual](#seis)
    - [Dependencias](#siete)
    - [Levantar API con Docker](#ocho)
    - [Consumir API](#nueve)

<a id="uno"></a>
## Prerrequisitos:
Para poder levantar esta API y consumirla es necesario cumplir con los prerrequisitos para proceder a instalar las dependencias y correr el código fuente.
<a id="dos"></a>
### 1. Python:
Es necesario tener instalado desde Python 3 en adelante.
[Pagina Oificial de Python](https://www.python.org/downloads/).

- Si ya tienes python instalado, puedes revisar su versión con el comando en la cmd:
```
Python --version
```
<a id="tres"></a>
### 2. WSL (linux subsystem for windows):
Para levantar la API necesitamos Docker y para instalar Docker necesitamos WSL ya que es la configuración recomendada al instalar Docker. 

- WSL se instala con el siguiente comando en PowerShell (Administrador):
```
wsl --install
```
- Si ya tienes WSL, puedes verificar su versión con ( Versión 2 Recomendada):
```
wsl -l -v
```
- Si la versión es antigua puedes actualizar con el siguiente comando:
```
wsl --update
```

**NOTA:** Con Docker puede que aparezca un error de `"An unexpected error was encountered while executing a WSL command"`. Esto ocurre intentar usar Docker en las versiones actuales de Windows, para corregir este problema debes: **activar en la BIOS** el SVM mode**. Con esto debería funcionar con normalidad cualquier instalación de Docker en Windows, ya que con esa opción se activa la virtualización en el equipo.
<a id="cuatro"></a>
### 3. Docker:
Para levantar la API necesitaremos Docker Desktop. El instalador se puede descargar desde su pagina oficial: [Docker.com](https://www.docker.com/products/docker-desktop/)


<a id="cinco"></a>
## Instrucciones de uso: <a name="instrucciones"></a>
Para poder levantar esta API y consumirla es necesario cumplir con los prerrequisitos para proceder a instalar las dependencias y correr el código fuente.
<a id="seis"></a>
### 1. Abrir entorno virtual de Python:
Para instalar las dependencias y levantar nuestra API necesitamos abrir un entorno virtual de Python.

- Esto se puede hacer abriendo el archivo:  **`"activar-venv.bat"`**.
- Si deseas cerrar el entorno virtual puedes tabular dentro de la cmd el comando:
```
desactivar-venv.bat
```
<a id="siete"></a>
### 2. Instalar dependencias:
Para que todo funcione, la API y Docker necesitan algunas bibliotecas las cuales se pueden instalar con esta linea de comandos:
```
pip install -r requirements.txt
```
<a id="ocho"></a>
### 3. Levantar API con Docker:
Para poder levantar la API como servidor debemos encapsularla en un contenedor con Docker, esto se hace corriendo el `"Dockerfile"` con comandos.

Para hacer esto mas fácil, puedes usar esta linea de comandos ya preparada:
```
levantar-docker.bat
```

**NOTA:** Debe estar abierto el **"Docker Desktop"** para levantar la API con el contenedor.
<a id="nueve"></a>
### 4. Consumir API:
Para consumir la api, basta con abrir el **`"index.html"`** del prototipo con un navegador (ej. Chrome) y visualizar si muestra los médicos. Desde la consola del entorno virtual se puede observar si se están haciendo las consultas HTTP a la API.

**NOTA:** La API será consumida a través de un JavaScript la cual tiene los métodos de consulta a la dirección donde esta alojada la API.
ej. `"http://localhost:5000/"`.
