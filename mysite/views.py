from django.shortcuts import render
from blog.models import Blog


def blog_list(request):
    context = {}
    context["blogs"] = Blog.objects.all()
    return render(request,'index.html',context)