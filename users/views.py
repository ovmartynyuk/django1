from django.shortcuts import render
import os
import json
from .models import User

# Create your views here.
# names = ['Alex', 'Julia', 'Andrew']
names = []
db_path = os.path.join('users', 'db.json')


def home(request):
    return render(request, 'users/home.html', {'names': names})


def users(request):
    # file = open(db_path, 'r')
    # data = json.load(file)
    # file.close()
    users_list = []
    try:
        with open(db_path, 'r') as file:
            users_list = [User(**item) for item in json.load(file)]
    except FileNotFoundError as err:
        print(err)
    finally:
        # print('finish')
        return render(request, 'users/users.html', {'users': users_list})


# var 1
# def create_user(request, id, name, age):
#     print(id)
#     print(name)
#     print(age)

# var 2 JSON
def create_user(request, **kwargs):
    with open(db_path, 'w') as file:
        json.dump(kwargs, file)
    with open(db_path, 'r') as file:
        # user = [User(**item) for item in json.load(file)]
        user = User(**json.load(file))
    print(kwargs)
    return render(request, 'users/users.html', {'user1': user})
