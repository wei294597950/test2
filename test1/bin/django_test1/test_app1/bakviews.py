# -*- coding: utf-8 -*-
#from __future__ import unicode_literals

import json
import os
import commands
import sys
import linecache
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import addform
from .forms import editform
from .forms import searchform
from django.core.paginator import Paginator,InvalidPage,EmptyPage,PageNotAnInteger
from django.views.decorators.cache import cache_page
from test_app1.models import logdelete
from test_app1.models import *
import time
import logging
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from .forms import LoginForm
import hashlib
reload(sys)
sys.setdefaultencoding("utf-8")

logger=logging.getLogger('addlog')
logger2=logging.getLogger('deletelog')

def get_doc_list(c):
    doc_list = []
    lines = c.readlines()
    for line in lines:
        if '###' in line:
            ori_dict = eval(line)
            #doc_list = ori_dict['###']
            #return doc_list
            return ori_dict


def get_add_list(c):
    doc_list = []
    lines = c.readlines()
    for line in lines:
        if '###' in line:
            #ori_dict = eval(line)
            #doc_list = ori_dict['###']
            return line

def getMD5(str):
    m = hashlib.md5()
    m.update(str)
    return m.hexdigest()

@login_required(login_url="/login/")
def add_QA(request):
    try:
        #cluster = request.POST['cluster']
        #index = request.POST['index']
        #types = request.POST['types']
        query = request.POST['query']
        answer = request.POST['answer']
        md5 = getMD5(query+'\1'+answer)
        os.chdir('/data/es_tool/bin/')
        c=os.popen('sh add_corpus_web.sh '+query+' '+answer)
        #c=os.popen('sh search_corpus_web.sh '+query+' '+answer+' '+cluster+' '+index+' '+types)
        os.chdir('/home/xuwei/test1/bin/django_test1/')
        times=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        add_list = eval(get_add_list(c))["###"]
        for i in add_list:
            i["query"] = query
            i["answer"] = answer
        restoress.objects.create(date=times,user=request.user.username,option="add",qaid=md5,content=add_list,query=query,answer=answer)
        #user_list=c.read().split()
        logger.info("add  %s %s %s %s %s",cluster,index,types,query,answer)
        #status=c.read().split()[2]
        form=addform()
        return render(request,'test2.html',locals())
    except:
        pass
    return render(request,'test2.html',locals())

    

        

@login_required(login_url="/login/")
def listing(request):
    form=searchform(request.POST)
    if request.method=='POST':
        flag=1
        form=searchform(request.POST)
    else:
        flag=0
        form=searchform(request.GET)
    if form.is_valid():
        #cluster=form.cleaned_data['cluster']
        query=form.cleaned_data['query']
        answer=form.cleaned_data['answer']
        #se_query=request.POST['search_query']
        #se_answer=request.POST['search_answer']
        os.chdir('/data/es_tool/bin/')
        c=os.popen('sh search_corpus_web.sh '+query+' '+answer)
        os.chdir('/home/xuwei/test1/bin/django_test1/')
        d_dict = get_doc_list(c)
        d_list = d_dict["###"]
        d_cluster = d_dict["cluster"]
        endlist=[]
        for doc in d_list:
            record = json.loads(doc)
            endlist.append(record)
        paginator=Paginator(endlist,20)
        if flag==1:
            page=1
        else:
            page=int(request.GET.get('page','1'))
        try:
            contacts=paginator.page(page)
        except PageNotAnInteger:
            contacts=paginator.page(1)
        except EmptyPage:
            contacts=paginator.page(paginator.num_pages)
    try:
        #cluster=request.POST['clusters']
        #print d_cluster
        source=json.loads(request.POST['data'])
        for i in source:
            d_dic = {}
            dic_list = []
            dic_json = {}
            index=i['index']
            types=i['types']
            query=i['query']
            answer=i['answer']
            idid=i['id']
            dic_json["cluster"] = " "
            dic_json["index"] = index
            dic_json["types"] = types
            dic_json["query"] = query
            dic_json["answer"] = answer
            dic_list.append(dic_json)
            d_dic["###"] = dic_list
            times=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
            logdelete.objects.create(date=times,cluster=" ", index=index,types=types,qaid=idid,query=query,answer=answer)
            
            os.chdir('/data/es_tool/bin/')
            c=os.popen('sh delete_corpus_web.sh '+index+' '+idid)
            restoress.objects.create(date = times,user = request.user.username,option = "delete" ,qaid = idid,
                    content = d_dic,query=query,answer=answer)
            logger2.info("delete   %s %s %s %s  %s",index,types,idid,query,answer)
            os.chdir('/home/xuwei/test1/bin/django_test1/')
    except:
        pass
    finally:
        form=searchform()
        form2=editform()
    return render(request,'list.html',locals())

@login_required(login_url="/login/")
def update(request):
    try:
        index=request.GET['index']
        types=request.GET['types']
        idid=request.GET['id']
    except:
        pass
    try:
        index=request.POST['index']
        types=request.POST['types']
        idid=request.POST['qaid']
        answer = request.POST['answer']
        os.chdir('/data/es_tool/bin/')
        c=os.popen('sh update_corpus_web.sh '+index+' '+idid+' '+answer)
        os.chdir('/home/xuwei/test1/bin/django_test1/')
    except:
        pass
    return render(request,'update.html',locals())

        
@login_required(login_url="/login/")
def deletelog(request):
    #contacts=logdelete.objects.all()
    contacts=logdelete.objects.order_by("-date")
    paginator=Paginator(contacts,20)
    page=int(request.GET.get('page','1'))
    try:
        contacts=paginator.page(page)
    except PageNotAnInteger:
        contacts=paginator.page(1)
    except EmptyPage:
        contacts=paginator.page(paginator.num_pages)
    try:
        source=json.loads(request.POST['data'])
        for i in source:
            qaid=i['qaid']
            #cluster=i['cluster']
            index=i['index']
            types=i['types']
            query=i['query']
            answer=i['answer']
            os.chdir('/data/es_tool/bin/')
            c=os.popen('sh add_corpus_web.sh '+query+' '+answer)
            os.chdir('/home/xuwei/test1/bin/django_test1/')
            logdelete.objects.filter(qaid=qaid).delete()
    except:
        pass
    return render(request,'deletelog.html',locals())

    
def login(request):
    if request.method == 'GET':
        form = LoginForm()
        return render_to_response('login.html', RequestContext(request, {'form': form,}))
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            user = auth.authenticate(username=username, password=password)
            if user is not None and user.is_active:
                auth.login(request, user)
                return render_to_response('list.html', RequestContext(request))
            else:
                return render_to_response('login.html', RequestContext(request, {'form': form,'password_is_wrong':True}))
        else:
            # return render_to_response('login.html', RequestContext(request, {'form': form,}))
            return render(request,'login.html',locals())



@login_required(login_url="/login/")
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/login/")
