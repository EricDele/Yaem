# Yaem
Yet Another Env Manager

- [Yaem](#yaem)
  - [Goal of this project](#goal-of-this-project)
  - [Requirements](#requirements)
  - [Architecture](#architecture)
  - [How to install](#how-to-install)
    - [Installing docker](#installing-docker)
    - [Installing Yaem](#installing-yaem)
  - [Dev environment](#dev-environment)
    - [Dev: Build](#dev-build)
    - [Dev: See the logs](#dev-see-the-logs)
    - [Dev: Migrate](#dev-migrate)
    - [Dev: Connexion to the database](#dev-connexion-to-the-database)
    - [Dev: Stop](#dev-stop)
  - [Production environment](#production-environment)
    - [Prod: Build](#prod-build)
    - [Prod: See the logs](#prod-see-the-logs)
    - [Prod: Migrate](#prod-migrate)
    - [Prod: Connexion to the database](#prod-connexion-to-the-database)
    - [Prod: Colect staticfiles](#prod-colect-staticfiles)
    - [Prod: Stop](#prod-stop)


## Goal of this project

The goal of this project is to provide an application to manage your environment inventories, variables and generate yaml files to use with ansible to facilitate your day to day work in a multiple environment context

## Requirements

Here is the list of the needed technologies for this application that you can retriev in the [requirements.txt](app/requirements.txt) file
- Docker 19.03.8
- docker-compose 1.25.4
- python 3.7.5
- django 3.0.4
- postgresql 12
- gunicorn 20.0.4
- nginx 1.17.4

## Architecture

A beautifull schema will come sooner

## How to install

We use docker to provide the Development and Production environments.

### Installing docker

We use this [documentation](https://docs.docker.com/install/linux/docker-ce/ubuntu/) to install docker on an Ubuntu.

We use this [documentation](https://docs.docker.com/compose/install/#install-compose-on-linux-systems) to install docker-compose on an Ubuntu.

You just have to follow the explanation before trying this project.

### Installing Yaem

You just have to clone this repository in your favorite project folder on your computer.

## Dev environment

### Dev: Build

```Shell
[Yaem]>docker-compose up -d --build
```

### Dev: See the logs

```Shell
[Yaem]>docker-compose logs -f
```

### Dev: Migrate

```Shell
[Yaem]>docker-compose exec web python manage.py migrate --noinput
```

### Dev: Connexion to the database

```Shell
[Yaem]>docker-compose exec db psql --username=yaem --dbname=yaem
```

### Dev: Stop

```Shell
[Yaem]>docker-compose down -v
```

## Production environment

### Prod: Build

```Shell
[Yaem]>docker-compose -f docker-compose.prd.yml up -d --build
```

### Prod: See the logs

```Shell
[Yaem]>docker-compose -f docker-compose.prd.yml logs -f
```

### Prod: Migrate

```Shell
[Yaem]>docker-compose -f docker-compose.prd.yml exec web python manage.py migrate --noinput
```

### Prod: Connexion to the database

```Shell
[Yaem]>docker-compose -f docker-compose.prd.yml exec db psql --username=yaem --dbname=yaem
```

### Prod: Colect staticfiles

```Shell
[Yaem]>docker-compose -f docker-compose.prd.yml exec web python manage.py collectstatic --no-input --clear
```

### Prod: Stop

```Shell
[Yaem]>docker-compose -f docker-compose.prd.yml down -v
```