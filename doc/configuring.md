# Configuring

- [Configuring](#configuring)
  - [Create yoour superuser](#create-yoour-superuser)

## Create yoour superuser

You need to create a supersuer for using admin interface

```Shell
[Yaem]> docker-compose exec web python manage.py createsuperuser
Username (leave blank to use 'root'): admin
Email address: firstname@lastname.com
Password: 
Password (again): 
Superuser created successfully.
```

Then you can test it on the [admin interface](http://localhost:8000/admin)