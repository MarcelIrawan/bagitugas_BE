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

### First, clone or download the git project

```
git clone https://github.com/MarcelIrawan/bagitugas_BE.git
```

### Install python virtual environment in the project root folder

On Windows
```
python -m venv env
```

On linux or MacOS
```
python3 -m venv env
```

### Activate the virtual environtment

On windows
```
source env/Scripts/activate
```

On linux and MacOS
```
source env/bin/activate
```

### Update the pip (Optional)

On Windows
```
python -m pip install -U pip
```

On linux or MacOS
```
pip3 install -U pip
```

### Install the requirements into the virual env

On Windows
```
pip install -r requirements.txt
```

On Linux or MacOS
```
pip3 install -r requirements.txt
```

### Migrate the models

On Windows
```
python manage.py makemigrations
python manage.py migrate
```

On Linux or MacOS
```
python3 manage.py makemigrations
python3 manage.py migrate
```

### Run the project

On Windows
```
python manage.py runserver
```

On Linux or MacOS
```
python3 manage.py runserver
```


## Available Endpoints

```
localhost:port/admin
localhost:port/api/rest-auth/registration
localhost:port/api/rest-auth/login
localhost:port/api/rest-auth/logout
```

```
localhost:port/api/course
localhost:port/api/guru
localhost:port/api/murid
localhost:port/api/enrollment
```

## Built With

* [Django](djangoproject.com) - The backend framework
* [Django-REST-Framework](django-rest-framework.org) - Used for build RESTful Web

## Front End

Check the [Front-End](https://github.com/dianrahmaji/bagitugas-frontend) for Bagi Tugas - by [dianrahmaji](https://github.com/dianrahmaji)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details