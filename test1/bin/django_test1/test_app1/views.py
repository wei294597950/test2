# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import logging
from .forms import *
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import json
from django.shortcuts import render_to_response
from django.template import RequestContext
# Create your views here.
from time import ctime
import urllib
import time
from .models import *
from django.contrib.auth.decorators import permission_required
from django.db.models import F
from django.db.models import Q
from django.core.paginator import Paginator,InvalidPage,EmptyPage,PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django_bulk_update.helper import bulk_update
logger=logging.getLogger('addlog')

def login(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request,'login.html',locals())
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            user = auth.authenticate(username=username, password=password)
            if user is not None and user.is_active:
                auth.login(request, user)
                return render(request,'tools.html',locals())
                #return render_to_response('tools.html', RequestContext(request))
            else:
                return render(request,'login.html',locals())
        else:
            # return render_to_response('login.html', RequestContext(request, {'form': form,}))
            return render(request,'login.html',locals())

@login_required(login_url="/login/")
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/login/")


@login_required(login_url="/login/")
def tools(request):
    if request.method == 'POST':
        good_source = json.loads(request.POST['data2'])
        bad_source = json.loads(request.POST['data1'])
        for i in good_source:
            good_list = new_data_table2.objects.filter(id = i['id'])
            for good in good_list:
                if good.export_tag <3:
                    good.good_count +=1
                good.export_tag =good.good_count+good.bad_count
                good.userlist = good.userlist+ request.user.username
            bulk_update(good_list,update_fields=['good_count'])
            bulk_update(good_list, update_fields=['userlist'])
            bulk_update(good_list, update_fields=['export_tag'])
            times = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            logger.info("%s %s  %s  %s  %s",i['id'],i['query'] ,i['answer'],str(request.user.username),"0")
        for a in bad_source:
            bad_list = new_data_table2.objects.filter(id = a['id'])
            for bad in bad_list:
                if bad.export_tag <3:
                    bad.bad_count +=1
                bad.export_tag =bad.good_count+bad.bad_count
                bad.userlist = bad.userlist+ request.user.username
            bulk_update(bad_list,update_fields=['bad_count'])
            bulk_update(bad_list, update_fields=['userlist'])
            bulk_update(bad_list, update_fields=['export_tag'])
            times = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            logger.info("%s %s  %s  %s  %s",i['id'],i['query'] ,i['answer'],str(request.user.username), "1" )
        #return render(request, 'tools.html', locals())
    contactss =new_data_table2.objects.filter(export_tag__lt=3).exclude(userlist__contains=request.user.username)
    #contactss = new_data_table2.objects.filter( Q(out_count__lte=3) & Q(userlist__contains=request.user.username))
    paginator = Paginator(contactss, 100)
    page = int(request.GET.get('page', '1'))
    try:
        contacts = paginator.page(page)
        for contact in contacts:
            #contact.out_count +=1
            if contact.out_count < 3:
                #contact.out_count = F('out_count')+1
                contact.out_count +=1
                #contact.userlist = contact.userlist + request.user.username
                #contact.userlist = F('userlist') + request.user.username
        bulk_update(contacts, update_fields=['out_count'])
        #bulk_update(contacts, update_fields=['userlist'])
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)
    return render(request, 'tools.html', locals())

