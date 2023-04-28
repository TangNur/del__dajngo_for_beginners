from django.urls import path

from posts.views import HomePageView

urlpatterns = [
    path('read/', HomePageView.as_view(), name='home_post')
]
