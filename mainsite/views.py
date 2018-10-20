from django.template.loader import get_template
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from datetime import datetime
from .models import Post, Product
import random


def homepage(request):
    template = get_template('index.html')
    now = datetime.now()
    quotes = ['今日事，今日毕',
              '要收获，先付出',
              '知识就是力量',
              '一个人的个性就是他的命运']
    html = template.render({'now': now, 'quote': random.choice(quotes)})
    
    return HttpResponse(html)


def showpost(request, slug):
    template = get_template('post.html')
    try:
        post = Post.objects.get(slug=slug)
        if post != None:
            html = template.render(locals())
            return HttpResponse(html)
    except:
        return redirect('/')


def about(request):
    template = get_template('about.html')
    quotes = ['今日事，今日毕',
              '要收获，先付出',
              '知识就是力量',
              '一个人的个性就是他的命运']
    html = template.render({'quote': random.choice(quotes)})

    return HttpResponse(html)


def listing(request):

    products = Product.objects.all()
    template = get_template('list.html')
    html = template.render({'products': products})
    return HttpResponse(html)


def disp_detail(request, sku):

    try:
        p = Product.objects.get(sku=sku)
    except Product.DoesNotExist:
        raise Http404('找不到指定的产品编号')
    template = get_template('disp.html')
    html = template.render({'product': p})

    return HttpResponse(html)

