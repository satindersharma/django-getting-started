import django
from sys import argv
import os
from faker import Faker
import random
from django.contrib.auth.hashers import make_password
# the below line is copied from wsgi file
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Your_Project_Name.settings')
django.setup()


def random_post(np=50, u=None):
    f = Faker()
    emotions = ['aggressivity',
                'anger',
                'anticipation',
                'anxiety',
                'apprehension',
                'contempt',
                'curiosity',
                'cynicism',
                'delight',
                'despair',
                'disappointment',
                'disgust',
                'dominance',
                'envy',
                'fatalism',
                'fear',
                'guilt',
                'indifference',
                'joy',
                'love',
                'morbidness',
                'optimism',
                'outrage',
                'pessimism',
                'pride',
                'regret',
                'remorse',
                'sadness',
                'sentimentality',
                'shame',
                'submission',
                'surprise',
                'trust',
                ]
    if u:
        obj = CustomUser.objects.filter(username=u)
        if not obj.exists():
            return "user with => {} <= username don't exit".format(u)
        u = [obj[0]]
    else:
        u = [x for x in CustomUser.objects.all()]
    for _ in range(np):
        fpostt = Post.objects.create(title=f.sentence(nb_words=random.randrange(6, 10)),
                                     body=f.text(
                                         max_nb_chars=random.randrange(180, 600)),
                                     feeling_cat=(
                                         random.choice(emotions)).upper(),
                                     created_by=random.choice(u),
                                     )
    if len(u) == 1:

        print(
            '{} posts of user -> {} <- created successfully'.format(np, u[0]))
    else:
        print('{} posts created successfully'.format(np))


if __name__ == '__main__':
    from users.models import CustomUser
    from posts.models import Post
    print('filling some random post data')
    if len(argv) <= 3:
        # print(argv)
        # when you do python random_post.py 23 here argv[0] is random_post.py, argv[1] is 23
        # when you do python random_post.py 23 Suzanne here argv[0] is random_post.py, argv[1] is 23 and argv[2] is the username i.e Suzanne
        if len(argv) == 2:
            random_post(np=int(argv[1]))
        else:
            random_post(np=int(argv[1]), u=argv[2])
    else:
        random_post()
