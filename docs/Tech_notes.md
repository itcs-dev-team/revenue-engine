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



Q: Pits of using parten-children templates: missing namespace (should be defined in `urls.py`)

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

