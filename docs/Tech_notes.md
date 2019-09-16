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

