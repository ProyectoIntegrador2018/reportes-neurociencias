# Nombre del proyecto

Generación de Reportes Automáticos a partir de Pruebas Neuropsicológicas (◠‿◠✿)

## Table of contents

* [Client Details](#client-details)
* [Environment URLS](#environment-urls)
* [Da Team](#team)
* [Technology Stack](#technology-stack)
* [Management resources](#management-resources)
* [Setup the project](#setup-the-project)
* [Running the stack for development](#running-the-stack-for-development)
* [Stop the project](#stop-the-project)
* [Restoring the database](#restoring-the-database)
* [Debugging](#debugging)
* [Running specs](#running-specs)
* [Checking code for potential issues](#checking-code-for-potential-issues)


### Client Details

| Name               | Web Page                       | Role                       |
| ------------------ | -------------------------------| ---------------------------|
| Beatriz Freymann   | www.neurocienciascognitivas.mx | Analista de investigación  |


### Environment URLS

* **Production** - [TBD](TBD)
* **Development** - [TBD](TBD)

### Da team

| Name            | Email              | Role                |
| --------------- | -------------------| --------------------|
| Fernando Romero | A01039364@itesm.mx | Scrum Master        |
| Emilio López    | A01651283@itesm.mx | Product Owner Proxy |
| Laura Santacruz | A01196377@itesm.mx | Project Admin       |
| Melanie Vielma  | A00818905@itesm.mx | Config Admin        |

### Technology Stack
| Technology    | Version      |
| ------------- | -------------|
| Python        | 3.7.4        |
| PyQt5         | 5.0.0        |

### Management tools

* [Github repo](https://github.com/ProyectoIntegrador2018/reportes-neurociencias)
* [Backlog](https://teams.microsoft.com/_#/school/tab::e4ebf4b1-cad0-4ba5-af36-7f7e5656e077/Proyecto?threadId=19:5c8da14bf8e34bdc9d277b396f93fc4f@thread.tacv2&ctx=channel)
* [Documentation](https://teams.microsoft.com/_#/school/files/Proyecto?threadId=19:5c8da14bf8e34bdc9d277b396f93fc4f@thread.tacv2&ctx=channel)

## Development

### Setup the project

Please install the following programs/libraries: 

* Git [Instrucciones](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* Python [Instrucciones](https://www.python.org/downloads/)
* Pandas [Instrucciones](https://pandas.pydata.org/pandas-docs/version/0.23.3/install.html)
* PyQt5 [Instrucciones](https://pypi.org/project/PyQt5/)
* Matplotlib [Instrucciones](https://matplotlib.org/3.1.1/users/installing.html)

After installing please you can follow this simple steps:

1. Clone this repository into your local machine

```bash
$ git clone https://github.com/ProyectoIntegrador2018/reportes-neurociencias.git
```

2. Open a terminal and look for the repository. An example:

```
C:\Users\melanievielma> cd Desktop/reportes-neurociencias
```

3. Run:

```
C:\Users\melanievielma\Desktop\reportes-neurociencias> py MasterController.py
```

### Running the stack for Development

1. Fire up a terminal and run: 

```
plis start
```

That command will lift every service crowdfront needs, such as the `rails server`, `postgres`, and `redis`.


It may take a while before you see anything, you can follow the logs of the containers with:

```
$ docker-compose logs
```

Once you see an output like this:

```
web_1   | => Booting Puma
web_1   | => Rails 5.1.3 application starting in development on http://0.0.0.0:3000
web_1   | => Run `rails server -h` for more startup options
web_1   | => Ctrl-C to shutdown server
web_1   | Listening on 0.0.0.0:3000, CTRL+C to stop
```

This means the project is up and running.

### Stop the project

In order to stop crowdfront as a whole you can run:

```
% plis stop
```

This will stop every container, but if you need to stop one in particular, you can specify it like:

```
% plis stop web
```

`web` is the service name located on the `docker-compose.yml` file, there you can see the services name and stop each of them if you need to.

### Restoring the database

You probably won't be working with a blank database, so once you are able to run crowdfront you can restore the database, to do it, first stop all services:

```
% plis stop
```

Then just lift up the `db` service:

```
% plis start db
```

The next step is to login to the database container:

```
% docker exec -ti crowdfront_db_1 bash
```

This will open up a bash session in to the database container.

Up to this point we just need to download a database dump and copy under `crowdfront/backups/`, this directory is mounted on the container, so you will be able to restore it with:

```
root@a3f695b39869:/# bin/restoredb crowdfront_dev db/backups/<databaseDump>
```

If you want to see how this script works, you can find it under `bin/restoredb`

Once the script finishes its execution you can just exit the session from the container and lift the other services:

```
% plis start
```

### Debugging

We know you love to use `debugger`, and who doesn't, and with Docker is a bit tricky, but don't worry, we have you covered.

Just run this line at the terminal and you can start debugging like a pro:

```
% plis attach web
```

This will display the logs from the rails app, as well as give you access to stop the execution on the debugging point as you would expect.

**Take note that if you kill this process you will kill the web service, and you will probably need to lift it up again.**

### Running specs

To run specs, you can do:

```
$ plis run test rspec
```

Or for a specific file:

```
$ plis run test rspec spec/models/user_spec.rb
```

### Checking code for potential issues

To run specs, you can do:

```
$ plis run web reek
```

```
$ plis run web rubocop
```

```
$ plis run web scss_lint
```

Or any other linter you have.
