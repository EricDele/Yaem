# Install

- [Install](#install)
  - [How to install](#how-to-install)
    - [Installing docker](#installing-docker)
    - [Installing Yaem](#installing-yaem)
  - [Create the env files](#create-the-env-files)
    - [.env.dev](#envdev)
    - [.env.prd](#envprd)
    - [.env.prd.db](#envprddb)

## How to install

We use docker to provide the Development and Production environments.

### Installing docker

We use this [documentation](https://docs.docker.com/install/linux/docker-ce/ubuntu/) to install docker on an Ubuntu.

We use this [documentation](https://docs.docker.com/compose/install/#install-compose-on-linux-systems) to install docker-compose on an Ubuntu.

You just have to follow the explanation before trying this project.

### Installing Yaem

You just have to clone this repository in your favorite project folder on your computer.

## Create the env files

In your poject directory you have to create 3 files

### .env.dev

```Shell
DEBUG=1
SECRET_KEY='<your secret key>'
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]

SQL_ENGINE=django.db.backends.postgresql
SQL_DATABASE=yaem
SQL_USER=yaem
SQL_PASSWORD=<your postgresql database password>
SQL_HOST=db
SQL_PORT=5432

POSTGRES_USER=yaem
POSTGRES_PASSWORD=<your postgresql database password>
POSTGRES_DB=yaem

DATABASE=postgres
```

### .env.prd

```Shell
DEBUG=0
SECRET_KEY='<your secret key>'
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]

SQL_ENGINE=django.db.backends.postgresql
SQL_DATABASE=yaem
SQL_USER=yaem
SQL_PASSWORD=<your postgresql database password>
SQL_HOST=db
SQL_PORT=5432

DATABASE=postgres
```

### .env.prd.db

```Shell
POSTGRES_USER=yaem
POSTGRES_PASSWORD=<your postgresql database password>
POSTGRES_DB=yaem
```
