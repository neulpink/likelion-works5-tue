from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# def index(request):
#     context = {
#         'post': {
#             'author': '_heeham',
#             'body': '나의 첫 #Django Project...'
#         },
#         'numbers': [1, 2, 3],
#         'user': User('heeham', 29)
#     }

#     return render(request, 'posts/index.html', context)

def index(request):
    context = {
        'posts': [
            {'author': 'hv_nara', 'body': 'Amanproject, Kwon nara'},
            {'author': '_heeham', 'body': '첫 #halloween'},
            {'author': 'd_a___m_i', 'body': '오랜만이서'},
            {'author': 'iamdoo2', 'body': 'PPF 붙혀주는 여자친구 #심지어잘함'},
        ]
    }

    return render(request, 'posts/index.html', context)
