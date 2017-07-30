# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from models import Post
from models import Family
from django.http import HttpResponse,Http404
from django.template.loader import get_template
from django.shortcuts import redirect

import sys
reload(sys)
sys.setdefaultencoding('utf8')
from datetime import datetime
# Create your views here.

def homepage(request):
    template = get_template('index.html')
    posts = Post.objects.all()
    now = datetime.now()
    html = template.render(locals())
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

def showallfamily(request):
    template=get_template('family_index.html')
    family=Family.objects.all()
    #now = datetime.now()
    html=template.render(locals())
    return HttpResponse(html)

def showfamily(request,nona):
    template = get_template('family_post.html')
    try:
        family = Family.objects.get(nano_name=nona)
    except:
        raise Http404("没有这么一个人啦~~")
    html = template.render(locals())
    return HttpResponse(html)