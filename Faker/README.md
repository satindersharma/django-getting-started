# To Generate Fake data


```
pip install Faker
```


## How to run files

#### Create Random Users


This will create 20 unique users

```
python random_user.py 20
```

by default 6 users will be created

```
python random_user.py
```


when you do python random_user.py 23 here argv[0] is random_user.py, argv[1] is 23


#### Create Random posts


To create 23 random posts to random users

```
python random_post.py 23
```

To create 23 random posts to specific users

```
python random_post.py 23 Suzanne
```

By default 50 posts will be created

```
python random_post.py
```



when you do python random_post.py 23 here argv[0] is random_post.py, argv[1] is 23

when you do python random_post.py 23 Suzanne here argv[0] is random_post.py, argv[1] is 23 and argv[2] is the username i.e Suzanne
        

