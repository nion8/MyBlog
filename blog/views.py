from django.shortcuts import render
from django.http import HttpResponse
from .forms import SubscriberForm


def index(request):
    return HttpResponse("Hello, World!")


def blog(request):
    name = "Андрей"
    current_day = "23.12.2017"
    form = SubscriberForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(data["name"])

        new_form = form.save()

    return render(request, 'blog/blog.html', locals())
