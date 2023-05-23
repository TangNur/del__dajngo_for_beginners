from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from blog.models import PostTab


class BlogListView(ListView):
    model = PostTab
    template_name = 'blog/home.html'


class BlogDetailView(DetailView):
    model = PostTab
    template_name = 'blog/post_detail.html'


class BlogCreateView(CreateView):
    model = PostTab
    template_name = 'blog/post_new.html'
    fields = ['title', 'author', 'body']


class BlogUpdateView(UpdateView):
    model = PostTab
    template_name = 'blog/post_edit.html'
    fields = ['title', 'body']


class BlogDeleteView(DeleteView):
    model = PostTab
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('home')
