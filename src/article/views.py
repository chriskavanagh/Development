from django.shortcuts import render
from article.models import Article
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse_lazy, reverse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from braces import views
from django.contrib import messages
from django.http import Http404, HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
import json




# title mixin, title='whatever' as class attr in generic cbv   
class ContextTitleMixIn(object):
    '''mixin to easily add title to context of cbv's'''
    def get_context_data(self, **kwargs):
        context = super(ContextTitleMixIn, self).get_context_data(**kwargs)
        context['title'] = self.title
        return context
        
        
## or just list title as class var, then use view.title in the template.
## http://reinout.vanrees.org/weblog/2014/05/19/context.html


# Create your views here.
class ArticleListView(ListView):
    '''list of all articles'''
    model = Article
    template_name = 'article_list.html'
    context_object_name = 'article_list'    # article_list (built in context name)
    
    
class ArticleDetailView(ContextTitleMixIn, DetailView):
    '''shows each article individually'''
    model = Article    
    template_name = 'article_detail.html'
    title = 'Django'
    context_object_name = 'article'
    
    
class ArticleCreateView(ContextTitleMixIn, CreateView):
    '''create an article'''
    model = Article
    fields = ['title', 'body']
    template_name = 'article_form.html'
    title = "Mixin Test"
    
    # def get_context_data(self, **kwargs):
        # context = super(ArticleCreateView, self).get_context_data(**kwargs)
        # context['title'] = 'Create Article'
        # return context
    
    
class ArticleUpdateView(ContextTitleMixIn, UpdateView):
    '''update/change an article'''
    model = Article
    fields = ['title', 'body']    
    template_name = 'article_form.html'
    title = 'Update'
    
    
class ArticleDeleteView(ContextTitleMixIn, DeleteView):
    '''delete an article'''
    model = Article
    template_name = 'article_confirm_delete.html'
    title = "Delete View"
    success_url = reverse_lazy('articles')
    
    # def get_context_data(self, **kwargs):
        # context = super(ArticleDeleteView, self).get_context_data(**kwargs)
        # context['title'] = 'Delete Article'
        # return context
    
    
# def search_titles(request):
    # '''search for a title using jQuery/AJAX'''
    # if request.method == 'POST':
        # #search_text = request.POST.get('post_text')
        # search_text = request.POST['search_text']
    # else:
        # search_text = ''
    # articles = Article.objects.filter(title__contains=search_text)
    # return render(request, 'article/ajax_search.html', {'articles': articles})
    
    
def search_titles(request):
    '''search for a title using jQuery/AJAX'''
    if request.is_ajax() and request.POST:
        #search_text = request.POST.get('post_text')
        search_text = request.POST.get('search_text', '')
        
    articles = Article.objects.filter(title__contains=search_text)
    
    if articles:
        for article in articles:
            article_title = article.title    # if articles: data = {'title': article_title}
        data = {'title': article_title}   
        
    return HttpResponse(json.dumps(data), content_type='application/json')
    
 