from django.shortcuts import render,get_object_or_404
from blog.models import Blog
import json

def blog_list(request):
    context = {}
    context["blogs"] = Blog.objects.all().order_by("-created_time")
    return render(request,'index.html',context)



def blog_detail(request, blog_pk):
    context = {}
    blog = get_object_or_404(Blog, pk=blog_pk)
    context['previous_blog'] = Blog.objects.filter(created_time__gt=blog.created_time).last()
    context['next_blog'] = Blog.objects.filter(created_time__lt=blog.created_time).first()
    context['blog'] = blog
    return render(request, 'single.html', context)