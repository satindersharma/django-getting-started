
# Django Getting Started

<a href="https://github.com/satindersharma/django-getting-started">
<img src="https://github.com/satindersharma/all-images/blob/master/icons/django-logo-positive.png" alt="Django icon">
</a>

If you are just getting started, it's better to start with the right foot.

## Download Python


[Python Download](https://www.python.org/downloads/ "Download Python")

#### Tips:
While installing python make sure to `check` the `add to path` option
Otherwise you have to set python path in environment variable manually


This insure that you are on latest version of pip

```
pip install --upgrade pip

```
## Create a folder where you want your project

If you want folder name same as Project name

then run

```
django-admin startproject project_name
```
This will create a project inside a same name folder

else

just create a folder and change to that directory

```
mkdir folder_name
```

on shell

```
touch folder_name
```

Now change to the directory

```
cd folder_name
```


## Create Virtual Environment:

give a folder name followed by virtual env

virtualenv virtualenvironment_folder_name

for example

```
virtualenv vme
```
[Here you get detail guide on Pipenv & Virtual Environments](https://docs.python-guide.org/dev/virtualenvs/)

### To select currunt virtualenvironment in VSCode

open project_folder in vscode

`ctrl+shift+p`

python interpreter

then select currunt vme
(this will create a .vscode file so next time you press
     ```ctrl+shift+`    ```
 
 
(i.e when you open terminal)


this will automatically activate you virtualenv)



you can manually create it by createing a `settings.json` file inside a `.vscode` folder and put following line inside settings.json
.vscode\settings.json

```javascript

{
    "python.pythonPath": "vme\\Scripts\\python.exe"
}
```

## Activate your virtual environment

###### First way
type on terminal
here virtualenvironment_folder_name is the name of your virtual environment created folder name

virtualenvironment_folder_name\scripts\activate

for example

```
vme\scripts\activate
```

###### Second way
As you have already selected you VirtualEnvironment in vs code
just close the terminal and reopen it by pressing ```ctrl+shift+p````


Now your virtualenv is ready

## Download Django

##### Here Django 2.2 is recommended as it is the long-term support (LTS) Version

[Here you get further details](https://www.djangoproject.com/download/)


so if you want long-term support (LTS) Version of Django
```
pip intall django==2.2
```
else if you Latest Version of Django

```
pip intall django
```

## Download Django REST framework (In case you are building Web APIs)
Here you get more info on DRF
[Django REST framework](https://www.django-rest-framework.org/ "Django REST framework Homepage")

```
pip install djangorestframework
```

VS Code use the pep 8 to style your code

[Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/ "PEP 8")

```
pip install autopep8
```

## Here you get more customization of `vscode` for you `django` project
<a href="https://github.com/satindersharma/vscode" target="_blank"><h2>click here</h2></a>



some optional:
---

if you going to work with images or filefield

[Django Model filefield](https://docs.djangoproject.com/en/3.0/ref/models/fields/#filefield)

then install Pillow
```
pip install Pillow
```

Here you get more info on Pillow
[Pillow](https://pillow.readthedocs.io/en/stable/installation.html)


#### save this to one txt file so that in case other need to install same versions of libraries
```
pip freeze > requirments.txt
```

#### So If anyone wants to install all required libraries, the can run following command

```
pip install -r requirments.txt
```

Create project:
--------------
```
django-admin startproject project_name .
```
(here . will not create a extra nested folder)

create App:
-------
```
python manage.py startapp account
```

now in settings.py:
----------


```python

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'rest_framework',
    'feelingsApp.apps.FeelingsappConfig',
    'users.apps.UsersConfig',
    'posts.apps.PostsConfig',
    'comments.apps.CommentsConfig',
    'crispy_forms',
]




TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates"), ],
        ........


STATICFILES_DIRS = [os.path.join(BASE_DIR, "static"),]


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

LOGIN_URL = '/users/login'
LOGIN_URL_REDIRECT = '/'
LOGIN_REDIRECT_URL = '/'
# LOGOUT_URL = '/users/login'
LOGOUT_REDIRECT_URL = '/'

ACCOUNT_EMAIL_REQUIRED = False




# on default debug is True
# DEBUG = True

# ALLOWED_HOSTS = []

# to see you images and media on debug False
# some more additional changes are this
# DEBUG = False


# ALLOWED_HOSTS = ['*']     or
# ALLOWED_HOSTS = ['0.0.0.0', '127.0.0.1']

STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR),
                           "static_cdn", "static_root")


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR),
                          "static_cdn",
                          "media_root")


PROTECTED_ROOT = os.path.join(os.path.dirname(BASE_DIR),
                              "static_cdn", "protected_media")



EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"
EMAIL_FILE_PATH = os.path.join(BASE_DIR, "sent_emails")

# now set this in your main project urls.py
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns = urlpatterns + \
        static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + \
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# where users is app name and CustomUser is model name
AUTH_USER_MODEL = 'users.CustomUser'  # new

CRISPY_TEMPLATE_PACK = 'bootstrap3'

```
urls.py:
---
```python
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
                ......
               ]

# media dir works in main project url.py only
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)


```

admin.py:
----
```python
class PostsAdmin(admin.ModelAdmin):
    # list_display = ('title', 'slug', 'blog_image', 'status', 'created_on')
    # list_filter = ("status",)
    # search_fields = ['title', 'content']
    # prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'body', 'created_by', 'feeling_cat', 'is_public', 'allow_comment')
    search_fields = ('title', 'body')
    list_filter = ("feeling_cat",'created_by')
    exclude = ['slug', 'curr_time', 'rand_id', 'post_len']

admin.site.register(Post, PostsAdmin)

```

models.py:
-----
```python
class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    slug = models.SlugField(null=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    feeling_cat = models.CharField(
        max_length=32, choices=add_emotions(), blank=False, default=0)
    is_public = models.BooleanField(default=True)
    allow_comment = models.BooleanField(default=True)


    def get_post_url(self):
        return reverse("view-post", kwargs={'slug': self.slug})
```



## Some Important imports

```python

import json
from os import listdir
from random import choice
from django import forms
from django.conf import settings
from django.contrib import admin, messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import (AuthenticationForm, UserChangeForm,
                                       UserCreationForm, UsernameField)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import AbstractUser, Group
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.contenttypes.models import ContentType
from django.contrib.messages.views import SuccessMessageMixin
from django.core.exceptions import ValidationError
from django.core.serializers.json import DjangoJSONEncoder
from django.db import models
from django.db.models import Count, Q
from django.db.models.functions import TruncDay
from django.db.models.signals import pre_save, post_save
from django.db.utils import OperationalError
from django.http import (Http404, HttpResponse, HttpResponseRedirect,
                         JsonResponse)
from django.shortcuts import get_object_or_404, redirect, render
from django.template.defaultfilters import slugify
from django.urls import path, reverse, reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import (
    CreateView, DeleteView, DetailView, FormView, ListView, UpdateView)
from django.views.generic.edit import CreateView, View

User = settings.AUTH_USER_MODEL

```
