from django.conf.urls import include, url
from . import views


urlpatterns = [
    # Article List View:
    url(r'^$', views.home, name='posts_home'),
    url(r'^create_post/$', views.create_post, name='create_post'),
]