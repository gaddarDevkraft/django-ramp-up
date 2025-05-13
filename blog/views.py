from django.shortcuts import render
from .models import Post
from django.http import JsonResponse

# Create your views here.

def get_all_blog(request):
    blogs = Post.objects.all().values()
    return JsonResponse(list(blogs), safe=False)