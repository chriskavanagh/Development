from django.conf.urls import include, url


urlpatterns = [
    # Article List View:
    url(r'^$', 'posts.views.home', name='posts_home'),
    url(r'^create_post/$', 'posts.views.create_post', name='create_post'),
]