from django.shortcuts import render
from django.http import HttpResponse


def blog(request):
    name = "Андрей"
    return render(request, 'blog/blog.html', locals())
