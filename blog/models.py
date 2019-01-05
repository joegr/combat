from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime

class Post(models.Model):
    publish_date = models.DateTimeField(default=datetime.datetime.today)
    text = models.TextField()
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    slug = models.SlugField(unique=True)
    preview = models.CharField(max_length=300)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "/post/%i/" % self.id
