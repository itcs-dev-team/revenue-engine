# revenue-engine

A site for improving revenue in 2019+. ~~(wordpress/wp-content/themes/revenue-engine)~~

### Approach

~~We custom the theme on `technofix`.~~

* ~~[Custom Post Type](https://wordpress.org/support/article/post-types/)~~
  
    * ~~[Custom Post Type UI](https://wordpress.org/plugins/custom-post-type-ui/)~~
    

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

Install python 3.7

```bash
sudo apt install python3.7
```

Setup virtual env for Django

```bash
python3.7 -m venv django-revenue-env
source django-revenue-env/bin/activate
```

Install Django in virtual env. (django version>=2.1)

```bash
python -m pip install django>=2.1
```

or, update requirements.txt and then install packages from it on other machines [#](https://pip.pypa.io/en/stable/user_guide/#installing-packages)

```bash
python -m pip freeze > requirements.txt
python -m pip -r requirements.txt
```

(Remark: Use `brew` instead of `apt` on Mac. )

Run test server

```bash
python manage.py runserver
```

### Organization

```
revenue_engine
|_ mysite
```



### Database

#### Setup MySQL

Using docker-compose to setup MySQL rapidly.

A docker-compose file is provided in '/utilities/docker'. Use docker-compose to fire it up:

```bash
sudo docker-composer up
```

#### Using MySQL as database engine

Refer to [Databases - mysql notes - Django documentation](https://docs.djangoproject.com/en/2.2/ref/databases/#mysql-notes), MySQL has a couple drivers that implement the Python Database API described in [**PEP 249**](https://www.python.org/dev/peps/pep-0249). And Django requires [mysqlclient](https://pypi.org/project/mysqlclient/) 1.3.13 or later.

```bash
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