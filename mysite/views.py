from django.shortcuts import render,get_object_or_404
from blog.models import *
import json
from mysite.utils import *



def blog_list(request):
    context = {}
    if "searchtext" in request.GET:
        blogs = Blog.objects.filter(title__icontains=request.GET['searchtext'])
        if blogs.count() == 0:
            blogs = Blog.objects.filter(content__icontains=request.GET['searchtext'])
    elif "typename" in request.GET:
        blogs = Blog.objects.filter(blog_type__type_name__contains=request.GET['typename'])

    else:
        blogs = Blog.objects.all()
    context["blog_types"] = BlogType.objects.all()
    context["blogs"] = blogs.order_by("-created_time")
    return render(request,'index.html',context)



def blog_detail(request, blog_pk):
    context = {}
    blog = get_object_or_404(Blog, pk=blog_pk)
    read_cookie_key = read_statistics_once_read(request, blog)
    context['previous_blog'] = Blog.objects.filter(created_time__gt=blog.created_time).last()
    context['next_blog'] = Blog.objects.filter(created_time__lt=blog.created_time).first()
    context["blog_types"] = BlogType.objects.all()
    context['blog'] = blog

    response = render(request, 'single.html', context)
    response.set_cookie(read_cookie_key,'true')
    return response


from django.http import JsonResponse
# Create your views here.


def ErrResponse(code,message):
    data = {}
    data['status'] = 'ERROR'
    data['code'] =code
    data['message'] = message
    return JsonResponse(data)
def SuccessResponse(liked_num):
    data = {}
    data['status'] = 'SUCCESS'
    data['liked_num'] = liked_num
    return JsonResponse(data)



def like_change(request):
    # 获取数据
    object_id = request.GET.get('object_id')
    blog = get_object_or_404(Blog, pk=object_id)
    ct = ContentType.objects.get_for_model(blog)
    is_like = request.GET.get("is_like")
    likenum = LikeNum.objects.get(content_type=ct, object_id=object_id)
    if is_like == "true":
        likenum.like_num +=1
    else:
        likenum.like_num -= 1
    likenum.save()
    return SuccessResponse(likenum.like_num)