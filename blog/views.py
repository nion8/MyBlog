from django.shortcuts import render
from django.http import HttpResponse
from .forms import SubscriberForm
from django.views import View

#
# def home(request):
#     return render(request, 'home.html', {})


class Index(View):

    def get(self, request):
        context = {'text': 'Hello World!'}
        print(context)
        return render(request, 'home.html', context)
