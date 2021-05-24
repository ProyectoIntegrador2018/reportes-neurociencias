# Nombre del proyecto

Generación de Reportes Automáticos a partir de Pruebas Neuropsicológicas (◠‿◠✿)

## Tabla de contenidos

- [Detalles del cliente](#detalles-del-cliente)
- [Environment URLS](#environment-urls)
- [Equipo de desarrollo](#equipo-de-desarrollo)
- [Technology Stack](#technology-stack)
- [Management tools](#management-tools)
- [Clonar o actualizar el repositorio](#clonar-o-actualizar-el-repositorio)
- [Correr el programa](#correr-el-programa)
- [Crear el ejecutable](#crear-el-ejecutable)

### Detalles del cliente

| Name             | Web Page                       | Role                      |
| ---------------- | ------------------------------ | ------------------------- |
| Beatriz Freymann | www.neurocienciascognitivas.mx | Analista de investigación |

### Environment URLS

- **Development** - [TBD](https://github.com/ProyectoIntegrador2018/reportes-neurociencias)

### Equipo de desarrollo

Versión 1:

| Name            | Email              | Role                |
| --------------- | ------------------ | ------------------- |
| Fernando Romero | A01039364@itesm.mx | Scrum Master        |
| Emilio López    | A01651283@itesm.mx | Product Owner Proxy |
| Laura Santacruz | A01196377@itesm.mx | Project Admin       |
| Melanie Vielma  | A00818905@itesm.mx | Config Admin        |

Versión 2:
| Name | Email | Role |
| --------------- | ------------------- | --------------------|
| Javier Gutiérrez | A01193217@itesm.mx | Scrum Master |
| Alejandro Lozano | A01192979@itesm.mx | Product Owner Proxy |
| Bernarno Orozco | A00819128@itesm.mx | Config Admin |


Versión 3:

| Name          | Email              | Role                |
| --------------| ------------------ | ------------------- |
| Martin Ruiz   | A00821630@itesm.mx | Scrum Master        |
| Pablo Andrade | A01193740@itesm.mx | Product Owner Proxy |
| Alberto Juárez| A01281913@itesm.mx | Project Admin       |
| Jesús Rivera  | A00820643@itesm.mx | Config Admin        |

### Technology Stack

| Technology    | Version |
| ------------- | ------- |
| Python        | 3.7.4   |
| PyQt5         | 5.0.0   |
| Pandas        | 1.0.3   |
| Matplotlib    | 3.2.1   |
| PyQtWebEngine | 5.15.1  |
| PyInstaller   | 3.5     |
| fbs           | 0.9.0   |
| pdfkit        | 0.6.1   |

### Management tools

- [Github repo](https://github.com/ProyectoIntegrador2018/reportes-neurociencias)
- [Backlog](https://teams.microsoft.com/l/file/EBA7B996-65E1-44BE-AD2D-88DDAC1C7B51?tenantId=c65a3ea6-0f7c-400b-8934-5a6dc1705645&fileType=xlsx&objectUrl=https%3A%2F%2Ftecmx.sharepoint.com%2Fsites%2FProy.IntegradorFJ2021-grupo2-Equipo2.4%2FShared%20Documents%2FEquipo%202.4%2FNeuroPy%2FApertura%2FAP%20E2.4%20Product%20Backlog.xlsx&baseUrl=https%3A%2F%2Ftecmx.sharepoint.com%2Fsites%2FProy.IntegradorFJ2021-grupo2-Equipo2.4&serviceName=teams&threadId=19:e54d4fd06c2547bf91ed6ea875e587fe@thread.tacv2&groupId=b3aaaa65-86d9-4ba0-807a-3b0e17ae6d90)
- [Documentation](https://teams.microsoft.com/_#/school/files/Proyecto?threadId=19:5c8da14bf8e34bdc9d277b396f93fc4f@thread.tacv2&ctx=channel)

## Development

### Clonar o actualizar repositorio

1. Si no tienes una copia de este repositorio en tu computadora, debes clonarlo primero:

```bash
$ git clone https://github.com/ProyectoIntegrador2018/reportes-neurociencias.git
```

2. Corre el siguiente comando para asegurarte de que todo este al día:

```bash
$ git status
```

3. Deberás ver algo similar a esto:

```
On branch master
Your branch is up-to-date with 'origin/master'.
```

4. Si no ves ese mensaje, corre el siguiente comando para actualizar tu repositorio:

```bash
$ git pull origin master
```

### Correr el programa

Por favor instala los siguientes paquetes/librerías:

- Git [Instrucciones](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- Python [Instrucciones](https://www.python.org/downloads/)
- wkhtmltopdf[Instrucciones](https://wkhtmltopdf.org/downloads.html)


Después de instalar lo anterior sigue los siguientes pasos:

1. Clona este repositorio a tu máquina local (más detalles en [Clonar o actualizar el repositorio](#clonar-o-actualizar-el-repositorio))

```bash
$ git clone https://github.com/ProyectoIntegrador2018/reportes-neurociencias.git
```

2. Genera un nuevo ambiente con python 3.7 y busca el repositorio. Ejemplo:

```
C:\Users\usuario> cd Desktop/reportes-neurociencias
```

3. Installacion de dependencias con pip:

```
C:\Users\usuario\Desktop\reportes-neurociencias> pip install -r requirements.txt
```

4. Corre el siguiente comando para utilizar el primer entregable del proyecto:

```
C:\Users\usuario\Desktop\reportes-neurociencias> fbs run
```

**Nota:**
revisar ejecucion y compilacion correcta con versionamientos error al uso de QWebEngine con OSx
[issue](https://github.com/pyinstaller/pyinstaller/issues/4030)

### Crear el ejecutable

Tener `fbs` instalado. Para esto se recomienda usar un virtual environment con las librerías necesarias. Puedes seguir este [tutorial](https://github.com/mherrmann/fbs-tutorial)

Correr `fbs freeze`. Este comando va a volver a generar la carpeta de `target` con el `.exe` del proyecto adentro (en caso de window), en caso de mac te generar un archivo .app.

Para crear el instalador correr el comando `fbs installer` para mas informacion dirigete a la documentacion de fbs

### Ejecutar Pruebas

para correr las pruebas unitarias:

1. cambiar de directorio a `src/main/python`

```bash
$ cd ./src/main/python
```

2. ejecutar pruebas con unittest

```bash
$ python -m unittest
```
