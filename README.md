# Nombre del proyecto

Generación de Reportes Automáticos a partir de Pruebas Neuropsicológicas (◠‿◠✿)

## Tabla de contenidos

* [Detalles del cliente](#detalles-del-cliente)
* [Environment URLS](#environment-urls)
* [Equipo de desarrollo](#equipo-de-desarrollo)
* [Technology Stack](#technology-stack)
* [Management tools](#management-tools)
* [Clonar o actualizar el repositorio](#clonar-o-actualizar-el-repositorio)
* [Correr el programa](#correr-el-programa)
* [Crear el ejecutable](#crear-el-ejecutable)


### Detalles del cliente

| Name               | Web Page                       | Role                       |
| ------------------ | -------------------------------| ---------------------------|
| Beatriz Freymann   | www.neurocienciascognitivas.mx | Analista de investigación  |


### Environment URLS

* **Development** - [TBD](https://github.com/ProyectoIntegrador2018/reportes-neurociencias)

### Equipo de desarrollo

Versión 1:

| Name            | Email              | Role                |
| --------------- | -------------------| --------------------|
| Fernando Romero | A01039364@itesm.mx | Scrum Master        |
| Emilio López    | A01651283@itesm.mx | Product Owner Proxy |
| Laura Santacruz | A01196377@itesm.mx | Project Admin       |
| Melanie Vielma  | A00818905@itesm.mx | Config Admin        |

Versión 2:
| Name             | Email               | Role                |
| ---------------  | ------------------- | --------------------|
| Javier Gutiérrez | A01193217@itesm.mx  | Scrum Master        |
| Alejandro Lozano | A01192979@itesm.mx  | Product Owner Proxy |
| Bernarno Orozco  | A00819128@itesm.mx  | Config Admin        |

### Technology Stack
| Technology    | Version      |
| ------------- | -------------|
| Python        | 3.7.4        |
| PyQt5         | 5.0.0        |

### Management tools

* [Github repo](https://github.com/ProyectoIntegrador2018/reportes-neurociencias)
* [Backlog](https://teams.microsoft.com/_#/school/tab::3486c230-987e-44f4-8449-6d0f424ed9ca/Equipo%201.07%20-%20Neuro%20JAB?threadId=19:6ea329083a1244509f40ee637eedb7d9@thread.tacv2&ctx=channel)
* [Documentation](https://teams.microsoft.com/_#/school/files/Proyecto?threadId=19:5c8da14bf8e34bdc9d277b396f93fc4f@thread.tacv2&ctx=channel)

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

* Git [Instrucciones](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* Python [Instrucciones](https://www.python.org/downloads/)
* Pandas [Instrucciones](https://pandas.pydata.org/pandas-docs/version/0.23.3/install.html)
* PyQt5 [Instrucciones](https://pypi.org/project/PyQt5/)
* Matplotlib [Instrucciones](https://matplotlib.org/3.1.1/users/installing.html)

Después de instalar lo anterior sigue los siguientes pasos:

1. Clona este repositorio a tu máquina local (más detalles en [Clonar o actualizar el repositorio](#clonar-o-actualizar-el-repositorio))

```bash
$ git clone https://github.com/ProyectoIntegrador2018/reportes-neurociencias.git
```

2. Abre la línea de comandos de su sistema operativo y busca el repositorio. Ejemplo:
```
C:\Users\usuario> cd Desktop/reportes-neurociencias
```

3. Corre el siguiente comando para utilizar el primer entregable del proyecto:
```
C:\Users\usuario\Desktop\reportes-neurociencias> py MasterController.py
```

### Crear el ejecutable
 **Importante:**
 Tener `fbs` instalado. Paro esto se recomienda usar un virtual environment con las librerías necesarias. Puedes seguir este [tutorial](https://github.com/mherrmann/fbs-tutorial)
 
Ve a la branch de `feature/installer` y haz un `git pull origin master` para traer los cambios más recientes (Resuelve los conflictos si es que hay). Borra del proyecto la carpeta de `target` y en la terminal corre `fbs freeze`. Este comando va a volver a generar la carpeta de `target` con el `.exe` del proyecto adentro. 

Antes de correr el ejecutable es muy importante que pongas estos archivos adentro de la carpeta de target:
* logo3.png
* app.css
* La carpeta de `Baremos`
* La carpeta de `vistas/Reporte`

Después de realizar estos pasos ya puedes correr el ejecutable exitosamente :)

Nota: Si quieres poder debuggear el ejecutable puedes correr `fbs freeze --debug`