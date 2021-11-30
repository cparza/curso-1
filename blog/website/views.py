from django.shortcuts import render
from .models import Post

def hello_blog(request):
    lista = [
        'Django', 'Python', 'Git', 'HTML',
        'Banco De Dados', 'Linux', 'Nginx', 'Uwsgi',
        'Systemctl'
    ]

    list_posts = Post.objects.all()

    data = {
            'name': 'Curso de Django 3',
            'lista_tecnoloias':lista,
            'posts': list_posts
        }

    return render(request, 'index.html', data)


