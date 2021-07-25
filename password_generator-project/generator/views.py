from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.


def home(request):
    return render(request, 'generator/home.html')


def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend('ABCDEFGHIKLMNOPQRSTVXYZ')
    if request.GET.get('special'):
        characters.extend('!@#$%^&*()')
    if request.GET.get('numbers'):
        characters.extend('1234567890')

    length = int(request.GET.get('length', 12))
    if length > 14:
        length = 14
    elif length < 6:
        length = 6

    the_password = ''
    for i in range(length):
        the_password += random.choice(characters)

    return render(request, 'generator/password.html', {'password': the_password})


def author(request):
    return render(request, 'generator/author.html')
