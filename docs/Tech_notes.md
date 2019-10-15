# Tech Notes

### Front-end

Q: What is the use of that JavaScript file?

@2019-09-25

* jPanelMenu CSS and JS files inside jPanelMenu folder.
* flexslider CSS and JS files inside flexslider folder:
  *  This is being use for the photo and jobs slider in job portal page.
* fakeLoader CSS and JS files inside fakeLoader folder:
  * This is page loading effect used on every HTML files. 

### Back-end

#### Using Django Template Language

Q: Which should I put html files in "templates" folder?

```bash
# cwd = root of django project
cd mysite
mkdir templates/mysite
touch templates/mysite/index.html
```



Q: How to use template inheritance to extend a template file from base?

Google: django template extends -> https://docs.djangoproject.com/en/1.7/topics/templates/

```markdown
One common way of using inheritance is the following three-level approach:

* Create a **base.html** template that holds the main look-and-feel of your site.
* Create a **base_SECTIONNAME.html** template for each “section” of your site. For example, **base_news.html**, **base_sports.html**. These templates all extend **base.html** and include section-specific styles/design.
* Create individual templates for each type of page, such as a news article or blog entry. These templates extend the appropriate section template.

This approach maximizes code reuse and makes it easy to add items to shared content areas, such as section-wide navigation.
```



Q: Pits / Setting of using parent-children templates inheritance: missing namespace (should be defined in `urls.py`)

Google: django 2 'mysite' is not a registered namespace -> https://stackoverflow.com/questions/48161676/django-noreversematch-at-myapp-is-not-a-registered-namespace

In "urls.py" (revenue_engine/urls.py)

```python
    # path('', include('mysite.urls')), # General site
    path('', include('mysite.urls', namespace='mysite')), # General site
```

In "urls.py" (mysite/urls.py)

```python
app_name = "mysite"
```



Q: I have a 3-tier template inheritance ('base.html -> 'base_mysite.html' -> 'index.html'). What if I define zero-contents template block in the 2nd tier (e.g. "footer" block is zero-contents)?

@2019-09-25

```django
{% comment "base structure of template block " %} 

### Base structure of template block in 'base_mysite.html': 
{% extends "mysite/base.html" %}
{% load static %}

    1. {% block title %}Welcome To ITCS Group - mysite{% endblock title %}
    2. {% block header %}{% endblock header %}
    3. {% block highlighted %}{% endblock highlighted %}
    4. {% block content %}{% endblock content %}
    5. {% block footer %}{% endblock footer %}
    6. {% block job_search_modal %}{% endblock job_search_modal %}
{% endcomment %}

{% comment "Usage of template block " %} 
Usage:

- Remove comment of a block to activate a template block in this 'base_mysite.html'.
    Since a template block should provide contents when inheriting from 'base.html'.
    Zero-content template block here makes **no contents** showing in the resulting render page.
    (e.g. When I provide an empty "footer" block here and there was no "footer" block provided in 'index.html',
    the resulting 'index.html' page shows zero-contents footer.)

{% endcomment %}
```



Q: Where is the 'static' folder that I should put css/js/images inside? ('static/' should be put inside the django application, or should be put inside an app?)

Youtube: django static files - > [How to Use Django Static Files (Django Tutorial) | Part 5 - YouTube](https://www.youtube.com/watch?v=3ETQf3TQ9gc&list=PLw02n0FEB3E3VSHjyYMcFadtQORvl1Ssj&index=5)

Without changing `STATIC_URL` in `settings.py`, if my app is named "mysite", then the static folder should be:
(e.g. in commit "[a302528](https://github.com/itcs-dev-team/revenue-engine/commit/a302528cc67ecd6a33cf65cb9cd690c1a0eadf24)" in branch "[dev-frontend-migrate-django_bootstrap4-build_django_template](https://github.com/itcs-dev-team/revenue-engine/commits/dev-frontend-migrate-django_bootstrap4-build_django_template)")

```bash
mysite/static/mysite/
mysite/templates/mysite/
```

An example `base.css` and `base.html`.

```bash
mysite/static/mysite/base.css
mysite/templates/mysite/base.html
```

Q: What can I do with `django.db.models`?

2019-10-14: *https://docs.djangoproject.com/en/2.2/ref/models/fields/* to see what can we do when define models.