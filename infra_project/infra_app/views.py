from django.http import HttpResponse


def index(request):
    return HttpResponse('у меня получилось! Оно воркает!')


def second_page(request):
    return HttpResponse('А это вторая страница!')
