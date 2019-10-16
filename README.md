# revenue-engine

A site for improving revenue in 2019+. ~~(wordpress/wp-content/themes/revenue-engine)~~

### Approach

We develop the new website with Django in fast pace.

#### About Git branches (2019-10)

1. **'master'**: a stable branch. 
   1. Everything (that stable) should be merged into this branch before online.
2. **'unstable'**: main branch of unstable code. 
   1. Experiment use. For forking new branches from it.
   2. Should be merged into '**master**'.
3. **'dev-frontend'** & **dev-frontend-xxx'**: everything about development of front-end.
   1. Create new branch '**dev-frontend-xxx**' from it.
   2. Should be merged into '**unstable**'.
4. **'dev-backend'** & **'dev-backend-xxx'**: everything about development of back-end.
   1. Create new branch '**dev-backend-xxx**' from it.
   2. Should be merged into '**unstable**'.

----

### Setup (2019-09)

We are going to install packages on Ubuntu. (Remark: Use `brew` instead of `apt` on Mac. )

#### Installation

Install python 3.7 and packages needed:

```bash
PKGS=' python3.7 python3-dev git python3-venv python-dev default-libmysqlclient-dev python3-pip'

for i in ${PKGS}
do
    sudo apt install $i
done
```

Setup virtual environment for Django:

```bash
$ mkdir ~/venv && cd ~/venv
$ python3.7 -m venv django-revenue-env
$ source django-revenue-env/bin/activate # test if it works.
```

Install Django with virtual environment on: (django version>=2.1)

```bash
(django-revenue-engine) $ pip install django>=2.1
(django-revenue-engine) $ pip install django-bootstrap4 # Sometimes this package doesn't with requirements.txt
(django-revenue-engine) $ pip install PyMySQL
```

( **Do not** update `requirements.txt`:

```bash
$ pip freeze > requirements.txt
```

)

Prepare the repo in user global area, and `git clone` the repo.

```bash
$ sudo mkdir -p /uga/app
$ sudo chown -R $USER:$USER /uga/app

```

```bash
$ cd /uga/app
$ git clone https://github.com/itcs-dev-team/revenue-engine.git
```

```bash
$ sudo chown -R $USER:$USER /uga/app/django-revenue-env
```



#### Test if it works

Checkout a branch. With virtual environment on, run test server:

```bash
(django-revenue-engine) $ cd /uga/app/revenue-engine
(django-revenue-engine) $ git checkout unstable # or git checkout master
```

```bash
(django-revenue-engine) $ python manage.py runserver
```

To exit, deactivate the virtual environment:

```bash
(django-revenue-engine) $ decative
$
```



#### Use: Running it

For dev, clone & check out latest unstable with virtual env on:

```bash
cd ~/venv
source django-revenue-env/bin/activate
```

Update python packages with `pip -r requirements.txt` and then install packages that used in the latest code [#](https://pip.pypa.io/en/stable/user_guide/#installing-packages):

```bash
(django-revenue-engine) $ pip install -r requirements.txt
```

Fire Django up:

```
(django-revenue-engine) $ cd /uga/app/revenue-engine
(django-revenue-engine) $ python manage.py check
(django-revenue-engine) $ python manage.py migrate
(django-revenue-engine) $ python manage.py runserver
```

To test website, fire up a browser:

```bash
$ firefox 'localhost:8000/'
```



----

### Organization

```
revenue_engine
|- mysite # the backbone module for the whole site.
|- profiles # User profiles
|- # Jobs
|- # News # News and events
|- # Services
|- # Case_studies
```

----



### Database (old information)

#### Setup MySQL

Using docker-compose to setup MySQL rapidly.

A docker-compose file is provided in '/utilities/docker'. Use docker-compose to fire it up:

```bash
sudo docker-composer up
```

#### Using MySQL as database engine

Refer to [Databases - mysql notes - Django documentation](https://docs.djangoproject.com/en/2.2/ref/databases/#mysql-notes), MySQL has a couple drivers that implement the Python Database API described in [**PEP 249**](https://www.python.org/dev/peps/pep-0249). And Django requires [mysqlclient](https://pypi.org/project/mysqlclient/) 1.3.13 or later.

​```bash
# Ref: [mysqlclient · PyPI](https://pypi.org/project/mysqlclient/)
sudo apt-get install python-dev default-libmysqlclient-dev
sudo apt-get install python3-dev # if you are using python
```

Install PyMySQL:

```bash
pip install PyMySQL
```

Add this in `__init__.py` of the project to simulate MySQLdb:

```python
import pymysql
pymysql.install_as_MySQLdb()
```



**Optional**: A setup on linux:

Google:django using mysql -> [python - Setting Django up to use MySQL - Stack Overflow](https://stackoverflow.com/questions/19189813/setting-django-up-to-use-mysql)

```bash
sudo apt-get install libmysqlclient-dev
```

**Optional**:  Error`ModuleNotFoundError: No module named 'MySQLdb'` occurs when `python manage.py runserver`:

Setup PyMySQL as documented above.

**Optional**: If you got an error `django.core.exceptions.ImproperlyConfigured: Error loading MySQLdb module.` when running Django development server (`python manage.py runserver`) with PyMySQL: `django.core.exceptions.ImproperlyConfigured: mysqlclient 1.3.13 or newer is required; you have 0.9.3.`

Try to use `` instead of `` as the database engine in `settings.py`:

```python
DATABASES = {
    'default': {
        'NAME': 'my_db_name',
        'ENGINE': 'mysql.connector.django',   # 'django.db.backends.mysql' with PyMySQL doesn't work.
        'USER': '<user>',
        'PASSWORD': '<pass>',
        'HOST': 'localhost',
        'PORT': 3306,
        'OPTIONS': {
            'autocommit': True,
        },
    }
}
```

Reference: Google:django.core.exceptions.ImproperlyConfigured: Error loading MySQLdb module. -> [python - django.core.exceptions.ImproperlyConfigured_ Error loading MySQLdb module_ No module named MySQLdb - Stack Overflow](https://stackoverflow.com/questions/15312732/django-core-exceptions-improperlyconfigured-error-loading-mysqldb-module-no-mo/20091657)