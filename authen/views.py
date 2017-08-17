# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import View
from .forms import Userform
from django.http import HttpResponse
from django.contrib.auth import get_user_model

User=get_user_model()

def index(request):
    return render(request,'authen/index.html')

def login(request):
    return render(request,'authen/login.html')

def register(request):
    return render(request,'authen/register.html')

class UserFormView(View):
    form_class = Userform
    template_name = 'authen/register.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request,self.template_name,{'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username,password=password)
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('')

        return render(request,self.template_name,{'form':form})


def inputs(request):
    fname = request.POST['first_name']
    lname = request.POST['last_name']
    username = request.POST['user_name']
    mail = request.POST['email']
    pas = request.POST['password']

    new_user = User.objects.create_user(username=username, email=mail, first_name = fname, last_name= lname)
    new_user.set_password(pas)
    new_user.save()
    return render(request,'authen/login.html')

def linputs(request):
    template='authen/user_page.html'
    mail = request.POST['email']
    pas = request.POST['password']

    try:
        check_user = User.objects.get(email=mail)
        correct = check_user.check_password(pas)

        if(correct):
            context1 = {
                'first_name': check_user.first_name,
                'last_name': check_user.last_name
            }
            return render(request,template,context1)
        else:
            return HttpResponse('Incorrect passs')
    except Exception as e:
        return HttpResponse(e)