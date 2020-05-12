# django-getting-started
If you are just getting started, it's better to start with the right foot.














virtualenv vme



ctrl+shift+p



python interpreter

then select currunt vme
(this will create a .vscode file so next time you press ctrl+shift+` (i.e when you open terminal)


this will automatically activate you virtualenv)



you can manually create it by createing a settings.json file inside a .vscode folder and put following line inside settings.json
.vscode\settings.json


{
    "python.pythonPath": "vme\\Scripts\\python.exe"
}



Now your virtualenv is ready



pip intall django

```command
pip install djangorestframework
```

```shell
pip install -U autopep8
```


some optional:
---
if you going to work with images
then


pip install Pillow


pip install autopep8



pip freeze > requirments.txt



Create project:
--------------


django-admin startproject project_name .
(here . will not create a extra nested folder)

create App:
-------



python manage.py startapp account


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


```

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




urls.py:
---


from django.conf.urls.static import static


from django.conf import settings


# media dir works in main project url.py only
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)




admin.py:
----

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



models.py:
-----

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

