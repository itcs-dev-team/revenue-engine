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
python -m pip install -r requirements.txt
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

