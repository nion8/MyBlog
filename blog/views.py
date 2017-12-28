from django.shortcuts import render
from django.http import HttpResponse
from .forms import SubscriberForm


def home(request):
    return render(request, 'home.html', {})


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
