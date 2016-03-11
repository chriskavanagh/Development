from __future__ import absolute_import
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic.base import TemplateView, RedirectView
from django.views.generic.edit import CreateView, FormView
from django.views.generic.list import ListView
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from article.views import ContextTitleMixIn
from talks.models import TalkList
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse_lazy, reverse
from braces import views
from .forms import AjaxForm    #for testpage view
from django.http import Http404, HttpResponse
import json
# import from django.views import generic then use generic.ListView etc in Class


# Create your views here.

class HomePageView(ContextTitleMixIn, TemplateView):
    template_name = 'home.html'
    title = 'Django Blog'
    
    # def get_context_data(self, **kwargs):
        # context = super(HomePageView, self).get_context_data(**kwargs)
        # context['title'] = 'Django Blog'
        # return context
        
        
class SignUpView(ContextTitleMixIn, CreateView):
    form_class = UserCreationForm
    form_valid_message = 'Thanks For Signing Up!'
    model = User
    success_url = reverse_lazy('login')
    title = 'Sign-Up'
    template_name = 'accounts/signup.html'
    
    def form_valid(self, form):
        resp = super(SignUpView, self).form_valid(form)
        TalkList.objects.create(user=self.object, name='To Attend')
        return resp


class LoginView(ContextTitleMixIn, FormView):
    form_class = AuthenticationForm
    title = 'LogIn'
    success_url = reverse_lazy('home')
    template_name = 'accounts/login.html'
    
    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        
        if user is not None and user.is_active:
            login(self.request, user)
            return super(LoginView, self).form_valid(form)
        else:
            return self.form_invalid(form)
            
            
class LogOutView(ContextTitleMixIn, RedirectView):
    url = reverse_lazy('home')
    title = 'LogOut'
    
    @method_decorator(login_required)    
    def dispatch(self, *args, **kwargs):
        return super(LogOutView, self).dispatch(*args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        #self.messages.success("You've been logged out. Come back soon!")
        return super(LogOutView, self).get(request, *args, **kwargs)
        
        
class TestPageView(TemplateView):
    template_name = 'test.html'
    
    
def get_order(request):
    if request.is_ajax() and request.POST:
        order_name = request.POST.get('name')
        order_drink = request.POST.get('drink')
        data = {'name': order_name, 'drink': order_drink}
        return HttpResponse(json.dumps(data), content_type='application/json')
    else:
        return Http404
        
        
        
# def get_order(request):
    # if request.is_ajax() and request.POST:
        # order_name = request.POST.get('name')
        # order_drink = request.POST.get('drink')
        # data = {}
        # data['name'] = order_name
        # data['drink'] = order_drink
        # return HttpResponse(json.dumps(data), content_type='application/json')
    # else:
        # return Http404
