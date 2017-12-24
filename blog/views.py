from django.shortcuts import render
from django.http import HttpResponse
from .forms import SubscriberForm


def blog(request):
    name = "Андрей"
    current_day = "23.12.2017"
    form = SubscriberForm(request.POST or None)
    return render(request, 'blog/blog.html', locals())
