"""django_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from .views import HomePageView, TestPageView, SignUpView, LoginView, LogOutView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    # Article app url's:
    url(r'^articles/', include('article.urls')),
    # Post url's 
    url(r'^posts/', include('posts.urls')),
    # Talks app url's:
    url(r'^talks/', include('talks.urls', namespace='talks')),
    # Home Page View:
    url(r'^$', HomePageView.as_view(), name='home'),
    # Temporary Testing Page:
    url(r'^testing/$', TestPageView.as_view(), name='test'),
    # Sign Up View For New Users:
    url(r'^accounts/register/$', SignUpView.as_view(), name='signup'),
    # Login View:
    url(r'^accounts/login/$', LoginView.as_view(), name='login'),
    # Logout View:
    url(r'^accounts/logout/$', LogOutView.as_view(), name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
