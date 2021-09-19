
### A basic to-do app made with Django in which you can add/complete and remove items from.

All the to-do items are stored in a database and you can see the date they were created.

There's is also a theme swapper (just for fun I guess🤷‍♂️).

I stole something from github as well, try to find what I stole😏.

## Screenshots
![alt-text](https://github.com/JimPouris/django-todo/blob/main/static/images/one.PNG)

![alt-text](https://github.com/JimPouris/django-todo/blob/main/static/images/two.PNG)

## Gifs
![alt-text](https://github.com/JimPouris/django-todo/blob/main/static/images/one.gif)

![alt-text](https://github.com/JimPouris/django-todo/blob/main/static/images/two.gif)

![alt-text](https://github.com/JimPouris/django-todo/blob/main/static/images/three.gif)

![alt-text](https://github.com/JimPouris/django-todo/blob/main/static/images/swapper.gif)

In order to run it execute the following commands on your git bash.

**NOTE: Choose the right directory to clone the repo into**

```console
git clone https://github.com/JimPouris/django-todo.git
```

After that go into the directory in which you clone the repo and on your command prompt type:

**IMPORTANT**: Run the following command to install the requirements for the project.
```console
pip install -r requirements.txt
```
### And then

```console
python manage.py makemigrations
```
------
```console
python manage.py migrate
```
------
```console
python manage.py runserver
```

And you're done! Enjoy😃