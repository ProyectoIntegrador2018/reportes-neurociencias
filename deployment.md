# DEPLOYMENT

Generación de Reportes Automáticos a partir de Prubas Neuropsicológicas (◠‿◠✿)

## Tabla de contenidos

* [Precondiciones](#precondiciones)
* [Clonar o actualizar repositorio](#clonar-o-actualizar-repositorio)
* [Correr el programa](#correr-el-programa)

### Precondiciones

Tener las siguientes herramientas instaladas y configuradas:

* Git [Instrucciones](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* Python [Instrucciones](https://www.python.org/downloads/)
* Pandas [Instrucciones](https://pandas.pydata.org/pandas-docs/version/0.23.3/install.html)

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