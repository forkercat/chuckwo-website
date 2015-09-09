# -*- coding: utf-8 -*- 

from django.shortcuts import render
from django.template import loader, Context
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from blog.models import BlogsPost, Header
import json
import datetime

def archive(request):
    like_id = request.GET.get('like_id')
    if like_id != None:
        post = BlogsPost.objects.get(id=like_id)
        post.like += 1
        post.save()
        header = Header.objects.get()
        post = BlogsPost.objects.get(id=like_id)
        templ = loader.get_template("article.html")
        cont = Context({
                'header': header,
                'post': post,
            })
        return HttpResponse(templ.render(cont))

    article_id = request.GET.get('article')
    if article_id != None:
        header = Header.objects.get()
        post = BlogsPost.objects.get(id=article_id)
        templ = loader.get_template("article.html")
        cont = Context({
                'header': header,
                'post': post,
            })
        return HttpResponse(templ.render(cont))
    else:
        header = Header.objects.get()
        all_posts = BlogsPost.objects.all().order_by('-timestamp')
        paginator = Paginator(all_posts, 10)
        page = request.GET.get('page')
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)

        templ = loader.get_template("base.html")
        # shrink body
        for post in posts:
            post.body = post.body[0:80] + '...'

        cont = Context({
                'header': header,
                'posts': posts,
            })
        return HttpResponse(templ.render(cont))



def iosapi(request):
    blogData = []
    for post in BlogsPost.objects.all():
        postData = {
            'title': post.title,
            'author': post.author,
            'body': post.body,
            'like': post.like,
            'date': post.timestamp.strftime('%Y/%m/%d %H:%M:%S')
        }
        blogData.append(postData)
    # ensure_ascii=False Chinese
    return HttpResponse(json.dumps(blogData, ensure_ascii=False), content_type='application/json')















