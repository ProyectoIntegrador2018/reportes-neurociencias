# DEPLOYMENT

Generación de Reportes Automáticos a partir de Pruebas Neuropsicológicas (◠‿◠✿)

## Tabla de contenidos

- [Precondiciones](#precondiciones)
- [Clonar o actualizar repositorio](#clonar-o-actualizar-repositorio)
- [Correr el programa](#correr-el-programa)

### Precondiciones

Tener las siguientes herramientas instaladas y configuradas:

- Git [Instrucciones](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- Python [Instrucciones](https://www.python.org/downloads/)
- Pandas [Instrucciones](https://pandas.pydata.org/pandas-docs/version/0.23.3/install.html)
- PyQt5 [Instrucciones](https://pypi.org/project/PyQt5/)
- Matplotlib [Instrucciones](https://matplotlib.org/3.1.1/users/installing.html)
- Pyinstaller [Instrucciones](https://pyinstaller.readthedocs.io/en/stable/installation.html)
- Fbs [Instrucciones](https://pypi.org/project/fbs/)
- pdfkit [Instrucciones](https://pypi.org/project/pdfkit/)
- wkhtmltopdf[Instrucciones](https://wkhtmltopdf.org/downloads.html)

### Clonar o actualizar repositorio

1. Si no tienes una copia de este repositorio en tu máquina, debes clonarlo primero:

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
- Pandas [Instrucciones](https://pandas.pydata.org/pandas-docs/version/0.23.3/install.html)
- PyQt5 [Instrucciones](https://pypi.org/project/PyQt5/)
- Matplotlib [Instrucciones](https://matplotlib.org/3.1.1/users/installing.html)
- Pyinstaller [Instrucciones](https://pyinstaller.readthedocs.io/en/stable/installation.html)
- Fbs [Instrucciones](https://pypi.org/project/fbs/)
- pdfkit [Instrucciones](https://pypi.org/project/pdfkit/)
- wkhtmltopdf[Instrucciones](https://wkhtmltopdf.org/downloads.html)

Después de instalar lo anterior sigue los siguientes pasos:

1. Clona este repositorio a tu máquina local (más detalles en [Clonar o actualizar el repositorio](#clonar-o-actualizar-el-repositorio))

```bash
$ git clone https://github.com/ProyectoIntegrador2018/reportes-neurociencias.git
```

2. Abre la línea de comandos de su sistema operativo y busca el repositorio. Ejemplo:

```
C:\Users\usuario> cd Desktop/reportes-neurociencias
```

3. Installacion de dependencias con pip:

```
C:\Users\usuario\Desktop\reportes-neurociencias> pip install PyQt5==5.0.0 Pandas==1.0.3 Matplotlib==3.2.1 PyQtWebEngine==5.15.1 fbs==0.9.0 PyInstaller==3.5 pdfkit==0.6.1
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

### Para ejecutar en Mac

Para que el programa genere reportes en Mac, es necesario correrlo desde terminal. Dentro de la ruta del proyecto, ejecutar el siguiente comando:

```bash
$ open ./reportes_neurociencias.app
```
