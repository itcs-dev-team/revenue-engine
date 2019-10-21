#-------------------------

1. Install all packages needed:

PKGS='python3.7 python3-dev git python3-venv python-dev default-libmysqlclient-dev python-pip php phpmyadmin'

for i in ${PKGS}
do
	sudo apt install 
done

pip install django-bootstrap4
pip install PyMySQL
pip install django

#-- Work Around MySQL Bugs --

printf '
import pymysql
pymysql.install_as_MySQLdb()
' | tee  ./revenue_engine/__init__.py


#-- Setup MySQL Configuration ------

MY_CNF=/etc/mysql/revengine.cnf
printf '
[client]
database = itcs_dev
host = localhost
user = django
password = adminitcs
default-character-set = utf8
' | sudo tee ${MY_CNF}

#-- Configure Settings.py to point to MySQL CNF ---

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': '/etc/mysql/revengine.cnf',
        },
    }
}

#--- Clone & check out latest unstable ---- 

sudo mkdir -p /uga/app
sudo chown -R $USER:$USER /uga/app

cd /uga/app
git clone https://github.com/itcs-dev-team/revenue-engine.git
git checkout unstable

sudo chown -R $USER:$USER /uga/app/django-revenue-env

python3.7 -m venv django-revenue-env
source django-revenue-env/bin/activate

	cd revenue-engine/
	python manage.py check
	python manage.py migrate
	python manage.py createsuperuser   #--- adminitcs/adminitcs adminitcs@localhost Password: Bypass validation and Create user
	python manage.py runserver 

#---- Test Webiste -----

firefox 'localhost:8000/'
