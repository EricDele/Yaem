# Docker

- [Docker](#docker)
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