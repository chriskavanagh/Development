from django.conf.urls import include, url
from django.views.generic import TemplateView
from .import views
from . import ajax
#from .views import ArticleListView
#from .views import ArticleDetailView, ArticleDeleteView, ArticleUpdateView, ArticleCreateView, ArticleListView



urlpatterns = [
    # Article List View:
    url(r'^$', views.ArticleListView.as_view(), name='articles'),
    # Article Detail View:
    url(r'^(?P<pk>\d+)/$', views.ArticleDetailView.as_view(), name='article'),
    # Article Create View:
    url(r'^create/$', views.ArticleCreateView.as_view(), name='create'),
    # Article Update View:
    url(r'^(?P<pk>\d+)/update/$', views.ArticleUpdateView.as_view(), name='update'),
    # Article Delete View:
    url(r'^(?P<pk>\d+)/delete/$', views.ArticleDeleteView.as_view(), name='delete'),
    # Search url
    url(r'^search/$', views.search_titles),
    #ajax url's
    url(r'^ajax/add/$', ajax.add_todo),
    # more url
    url(r'^ajax/more/$', ajax.more_todo),
    # index.html view
    url(r'^ajax/$', TemplateView.as_view(template_name='index2.html')),
]
