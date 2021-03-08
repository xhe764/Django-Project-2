from populate_rango import add_page
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from rango.models import Category, Page, UserProfile
from rango.forms import CategoryForm, PageForm, UserForm, UserProfileForm
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
#from django.views.decorators.csrf import csrf_protect


@login_required
def add_page_button(request):
    #form = PageForm()
    if request.method == 'POST':
        cat_name = request.POST.get('cat_name', None)
        cat_slug = request.POST.get('page_cat', None)
        title=request.POST.get('page_title', None)
        url = request.POST.get('page_url', None)
        c = Category.objects.get_or_create(name=cat_name)[0]
        p = Page.objects.get_or_create(category=c, title=title)[0]
        p.url = url
        p.views = 0
        p.save()
        return redirect('show_category', cat_slug)
    else:
        return HttpResponse("request.post not working")
