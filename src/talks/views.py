from __future__ import absolute_import
from django.shortcuts import render, redirect
from django.http import HttpResponse
#from django.views import generic
from article.views import ContextTitleMixIn
from django.views.generic import View
from braces import views
from .models import TalkList, Talk
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from .forms import TalkListForm, TalkForm
from django.db.models import Count
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect, get_object_or_404


#-----------------------------Mixins-------------------------------------#

# Mixin For Title:
class ContextTitleMixIn(object):
    '''mixin to easily add title to context of cbv's'''
    
    def get_context_data(self, **kwargs):
        context = super(ContextTitleMixIn, self).get_context_data(**kwargs)
        context['title'] = self.title
        return context
        
        
# Mixin To Restrict View To User:
class RestrictToUserMixin(views.LoginRequiredMixin):
    '''mixin to restrict view to user'''
    
    def get_queryset(self):
        queryset = super(RestrictToUserMixin, self).get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset
        
#-----------------------------End Mixins-----------------------------------#        
        
def talk_list_detail(request, slug):
    talklist_detail = get_object_or_404(TalkList, slug=slug)
    #talklist_detail = Talk.objects.filter(talk_list__slug=slug)    # same query as above but in reverse
    form = TalkForm(request.POST or None)
    if form.is_valid():
        talk = form.save(commit=False)
        talk.talk_list_id = talklist_detail.id
        talk.save()
        return redirect(talklist_detail)

    context = {'talklist_detail': talklist_detail, 'form': form}
    return render(request, 'talk_list_detail.html', context)
    


class TalkListDetailView(RestrictToUserMixin, views.LoginRequiredMixin, DetailView):
    template_name = 'talklist_detail.html'
    form_class = TalkForm
    http_method_names = ['get', 'post']
    model = TalkList
    prefetch_related = ('talks',)
    
    def get_context_data(self, **kwargs):
        context = super(TalkListDetailView, self).get_context_data(**kwargs)
        #context.update({'form': self.form_class(self.request.POST or None)})
        context['form'] = self.form_class(self.request.POST or None)
        return context
        
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            obj = self.get_object()
            talk = form.save(commit=False)
            talk.talk_list = obj
            talk.save()
        else:
            return self.get(request, *args, **kwargs)
        return redirect(obj)  
    
        
        
class TalkListListView(ContextTitleMixIn, RestrictToUserMixin, ListView):
    model = TalkList
    title = 'List-View'
    template_name = 'talklist_list.html'
    
    def get_queryset(self):
        queryset = super(TalkListListView, self).get_queryset()
        queryset = queryset.annotate(talk_count=Count('talks'))        
        return queryset
        
        
class TalkListUserView(ListView):
    model = TalkList
    template_name = 'talk_list_user.html'
    
    def get_queryset(self):
        queryset = super(TalkListUserView, self).get_queryset()
        queryset =  TalkList.talklist_user_objects.all()       
        return queryset
        
        
        
class TalkListCreateView(views.LoginRequiredMixin, CreateView):
    form_class = TalkListForm
    model = TalkList
    #template_name = 'talklist_form.html'    # django should use this temp by default
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super(TalkListCreateView, self).form_valid(form)
    

    
class TalkListUpdateView(views.LoginRequiredMixin, UpdateView):
    form_class = TalkListForm
    model = TalkList
    #template_name = 'talklist_form.html'    # django should use this temp by default
    
    def get_queryset(self):
        queryset = super(TalkListUpdateView, self).get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset
        
        