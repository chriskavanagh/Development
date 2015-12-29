from django.conf.urls import include, url
from .views import ArticleListView
from .views import ArticleDetailView, ArticleDeleteView, ArticleUpdateView, ArticleCreateView, ArticleListView



urlpatterns = [
    # Article List View:
    url(r'^$', ArticleListView.as_view(), name='articles'),
    # Article Detail View:
    url(r'^(?P<pk>\d+)/$', ArticleDetailView.as_view(), name='article'),
    # Article Create View:
    url(r'^create/$', ArticleCreateView.as_view(), name='create'),
    # Article Update View:
    url(r'^(?P<pk>\d+)/update/$', ArticleUpdateView.as_view(), name='update'),
    # Article Delete View:
    url(r'^(?P<pk>\d+)/delete/$', ArticleDeleteView.as_view(), name='delete'),
]
