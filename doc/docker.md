# Docker

- [Docker](#docker)
  - [Dev environment](#dev-environment)
    - [Dev : Url](#dev--url)
    - [Dev: Build](#dev-build)
    - [Dev: See the logs](#dev-see-the-logs)
    - [Dev: MakeMigration](#dev-makemigration)
    - [Dev: Migrate](#dev-migrate)
    - [Dev: Connexion to the database](#dev-connexion-to-the-database)
    - [Dev : Loading fixtures to database](#dev--loading-fixtures-to-database)
    - [Dev: Stop](#dev-stop)
  - [Production environment](#production-environment)
    - [Prod : Url](#prod--url)
    - [Prod: Build](#prod-build)
    - [Prod: See the logs](#prod-see-the-logs)
    - [Prod: MakeMigration](#prod-makemigration)
    - [Prod: Migrate](#prod-migrate)
    - [Prod: Connexion to the database](#prod-connexion-to-the-database)
    - [Prod: Colect staticfiles](#prod-colect-staticfiles)
    - [Prod : Loading fixtures to database](#prod--loading-fixtures-to-database)
    - [Prod: Stop](#prod-stop)

## Dev environment

### Dev : Url

You can access the application once it have started at this url : http://localhost:8000

### Dev: Build

```Shell
[Yaem]>docker-compose up -d --build
```

### Dev: See the logs

```Shell
[Yaem]>docker-compose logs -f
```

### Dev: MakeMigration

```Shell
[Yaem]>docker-compose exec web python manage.py makemigrations --noinput
```

### Dev: Migrate

```Shell
[Yaem]>docker-compose exec web python manage.py migrate --noinput
```

### Dev: Connexion to the database

```Shell
[Yaem]>docker-compose exec db psql --username=yaem --dbname=yaem
```

### Dev : Loading fixtures to database

```Shell
[Yaem]> docker-compose exec web python manage.py loaddata manager/fixtures.yaml
```

### Dev: Stop

```Shell
[Yaem]>docker-compose down -v
```

## Production environment

### Prod : Url

You can access the application once it have started at this url : http://localhost:1337

### Prod: Build

```Shell
[Yaem]>docker-compose -f docker-compose.prd.yml up -d --build
```

### Prod: See the logs

```Shell
[Yaem]>docker-compose -f docker-compose.prd.yml logs -f
```

### Prod: MakeMigration

```Shell
[Yaem]>docker-compose -f docker-compose.prd.yml exec web python manage.py makemigrations --noinput
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
### Prod : Loading fixtures to database

```Shell
[Yaem]> docker-compose -f docker-compose.prd.yml exec web python manage.py loaddata manager/fixtures.yaml
```

### Prod: Stop

```Shell
[Yaem]>docker-compose -f docker-compose.prd.yml down -v
```