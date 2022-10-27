# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

# Create your views here.
from django import template
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect, resolve_url
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.template import loader
from django.urls import reverse

from .forms import LoginForm, SignUpForm
from django.contrib.auth.views import LogoutView


def login_view(request):

    if request.user.is_authenticated:
        return redirect('/')

    form = LoginForm(request.POST or None)

    msg = None

    if request.method == 'POST':

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            remember = form.cleaned_data.get('remember')

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if remember is False:
                    request.session.set_expiry(10)
                return redirect('/')
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating the form'

    return render(request, 'accounts/login.html', {'form': form, 'msg': msg})


def register_user(request):
    msg = None
    success = False

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            success = True

            return redirect('/')

        else:
            msg = 'Form is not valid'
    else:
        form = SignUpForm()

    return render(request, 'accounts/register.html', {'form': form, 'msg': msg, 'success': success})


def logout(request):
    login_url = resolve_url('/login/')
    return LogoutView.as_view(next_page=login_url)(request)


@login_required(login_url='/login/')
def dashboard(request):

    return render(request, 'home/index.html')


def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

