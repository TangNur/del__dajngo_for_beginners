from django.views.generic import ListView, DetailView

from blog.models import PostTab


class BlogListView(ListView):
    model = PostTab
    template_name = 'blog/home.html'


class BlogDetailView(DetailView):
    model = PostTab
    template_name = 'blog/post_detail.html'
