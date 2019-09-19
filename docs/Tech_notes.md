# Tech Notes

### Front-end



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

