from django.shortcuts import render
# from django.http import HttpResponse
from django.views import View
from .models import Post
from user_profile.models import User


#
# def home(request):
#     return render(request, 'home.html', {})


class Index(View):

    def get(self, request):
        context = {'text': 'Привет Мир!!'}
        return render(request, 'home.html', context)


class Profile(View):

     # user profile Page /user/username

    def get(self, request):

        # user = User.objects.get(username=username)
        # posts = Post.objects.filter(user=user)
        # context = {
        #   'posts': posts,
        #   'user': user,
        #    }
        return render(request, 'profile.html')
