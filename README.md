# Yaem
Yet Another Env Manager

- [Yaem](#yaem)
  - [Goal of this project](#goal-of-this-project)
  - [Requirements](#requirements)
  - [Architecture](#architecture)
  - [How to install](#how-to-install)
  - [Manage your containers](#manage-your-containers)
  - [Configuring](#configuring)


## Goal of this project

The goal of this project is to provide an application to manage your environment inventories, variables and generate yaml files to use with ansible to facilitate your day to day work in a multiple environment context

## Requirements

Here is the list of the needed technologies for this application that you can retriev in the [requirements.txt](app/requirements.txt) file
- Docker 19.03.8
- docker-compose 1.25.4
- python 3.7.5
- postgresql 12
- gunicorn 20.0.4
- nginx 1.17.4

For the django part 
- django 3.0.4
- djangorestframework 3.11.0
- markdown 3.2.1
- django-filter 2.2.0
- PyYAML 5.1.2

## Architecture

A beautifull schema will come sooner

## How to install

Follow the [Installation documentation](doc/install.md)

## Manage your containers

Follow the [Docker management](doc/docker.md)

## Configuring

Follow the [config documentation](doc/configuring.md)

