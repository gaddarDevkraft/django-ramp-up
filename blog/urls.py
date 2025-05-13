from django.urls import path
from . import views

urlpatterns = [
    path('/all', views.get_all_blog, name='post_list'),
    path('/html', views.get_html_file)
]
