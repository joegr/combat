from django.shortcuts import render
import operator
from django.views.generic import ListView, DetailView
from blog.models import Post

class PostList(ListView):
    model = Post

    def get_queryset(self):

        q = self.request.GET.get('q')
        qs = Post.objects.all()

        if q:
            ql = q.split()
            for i in ql:
                qs = qs.filter(title__contains=i) | qs.filter(text__contains=i)

        return qs

class PostDetail(DetailView):
    model = Post
