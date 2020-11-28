# Bagi Tugas Back End

Bagi Tugas is a project for web development class

## Getting Started

These instruction will give you step-by-step to setup the project and run it on your local machine

## Prerequisite

Few things that needs to be installed and prepared

```
python >= 3.6
pip >= 20.4
Python Venv
```

## Installing

Make sure you already have python in your local machine

### ! For Windows user I recommend to use the git bash console !

### First, clone or download the git project

```
git clone https://github.com/MarcelIrawan/bagitugas_BE.git
```

### Install python virtual environment in the project root folder

#### On Windows
```
$ python -m venv env
```

#### On Linux or MacOS
```
$ python3 -m venv env
```

### Activate the virtual environtment

#### On Windows
```
$ source env/Scripts/activate
```

#### On Linux and MacOS
```
$ source env/bin/activate
```

### Update the pip (Optional)

#### On Windows
```
(env)$ python -m pip install -U pip
```

#### On Linux or MacOS
```
(env)$ pip3 install -U pip
```

### Install the requirements into the virual env

#### On Windows
```
(env)$ pip install -r requirements.txt
```

#### On Linux or MacOS
```
(env)$ pip3 install -r requirements.txt
```

### Migrate the models

#### On Windows
```
(env)$ python manage.py makemigrations
(env)$ python manage.py migrate
```

#### On Linux or MacOS
```
(env)$ python3 manage.py makemigrations
(env)$ python3 manage.py migrate
```

### Create Superuser

#### On Windows
```
(env)$ python manage.py createsuperuser
```

#### On Linux and MacOS
```
(env)$ python3 manage.py createsuperuser
```

Input email and password for superuser

### Run the project

#### On Windows
```
(env)$ python manage.py runserver
```

#### On Linux or MacOS
```
(env)$ python3 manage.py runserver
```

The default port for the endpoint is ```localhost:8000```

But you can define your own port,

Just add the port you want after ```runserver```

#### Example
```
(env)$ python manage.py runserver 8081
```

## Available Endpoints

Open your browser and go to
```
localhost:8000
or
127.0.0.1:8000
```

```
localhost:8000/admin
localhost:8000/api/rest-auth/registration
localhost:8000/api/rest-auth/login
localhost:8000/api/rest-auth/logout
```

```
localhost:8000/api/course
localhost:8000/api/guru
localhost:8000/api/murid
localhost:8000/api/enrollment
```

## Built With

* [Django](djangoproject.com) - The backend framework
* [Django-REST-Framework](django-rest-framework.org) - Used for build RESTful Web

## Front End

Check the [Front-End](https://github.com/dianrahmaji/bagitugas-frontend) for Bagi Tugas - by [dianrahmaji](https://github.com/dianrahmaji)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details