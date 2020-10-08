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

1. Abre la línea de comandos de su sistema operativo y busca el repositorio. Ejemplo:

```
C:\Users\melanievielma> cd Desktop/reportes-neurociencias
```

2. Corre el siguiente comando para utilizar el primer entregable del proyecto:

```
C:\Users\melanievielma\Desktop\reportes-neurociencias> py MasterController.py
```

### Crear el ejecutable

**Importante:**
Tener `fbs` instalado. Paro esto se recomienda usar un virtual environment con las librerías necesarias. Puedes seguir este [tutorial](https://github.com/mherrmann/fbs-tutorial)

Ve a la branch de `feature/installer` y haz un `git pull origin master` para traer los cambios más recientes (Resuelve los conflictos si es que hay). Borra del proyecto la carpeta de `target` y en la terminal corre `fbs freeze`. Este comando va a volver a generar la carpeta de `target` con el `.exe` del proyecto adentro.

Antes de correr el ejecutable es muy importante que pongas estos archivos adentro de la carpeta de target:

- logo3.png
- app.css
- La carpeta de `Baremos`
- La carpeta de `vistas/Reporte`

Después de realizar estos pasos ya puedes correr el ejecutable exitosamente :)

Nota: Si quieres poder debuggear el ejecutable puedes correr `fbs freeze --debug`
