import django
from sys import argv
import os
from faker import Faker
import random
import pytz
from django.contrib.auth.hashers import make_password

# the below line is copied from wsgi file
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Your_Project_Name.settings')
django.setup()


def random_user(n=6):
    p = 1
    gender_choice = ['M', 'F']
    for _ in range(n):
        f = Faker('en_US')
        g = random.choice(gender_choice)
        if g == 'M':
            fn = f.first_name_male()
            ln = f.last_name_male()
        if g == 'F':
            fn = f.first_name_female()
            ln = f.last_name_female()
        fpwd = make_password(fn)
        dj = f.date_time_this_decade(before_now=True,
                                     after_now=False,
                                     tzinfo=pytz.UTC)
        obj, created = CustomUser.objects.get_or_create(first_name=fn,
                                                        last_name=ln,
                                                        username=fn,
                                                        gender=g,
                                                        password=fpwd,
                                                        date_joined=dj)
        if created:
            p += 1
    print(f'{p} unique users created successfully')


if __name__ == '__main__':
    # update this with your user model
    from users.models import CustomUser
    from posts.models import Post
    print('filling some random user data')
    if len(argv) == 2:
        # print(argv)
        # when you do python random_user.py 23 here argv[0] is random_user.py, argv[1] is 23
        random_user(int(argv[1]))
    else:
        random_user(3)
