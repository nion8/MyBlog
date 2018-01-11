from django.db import models
from user_profile.models import User


class Post(models.Model):
    user = models.ForeignKey(User)
    text = models.CharField(max_length=300)
    created_date = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=31, default='Global')
    is_active = models.BooleanField(default=True)
    is_favorit = models.BooleanField(default=False)

    # email = models.EmailField()
    # name = models.CharField(max_length=128)
