from django.shortcuts import render

from django.views.generic import ListView, DetailView
from blog.models import Post

class PostList(ListView):
    model = Post


class PostDetail(DetailView):
    model = Post
