from __future__ import absolute_import
from django.conf.urls import patterns, url, include
from .views import TalkListDetailView, TalkListListView, TalkListCreateView, TalkListUpdateView, TalkListUserView
from braces import views
#from . import views

 
 
list_patterns = [
    # TalkList List View:
    url(r'^$', TalkListListView.as_view(), name='list'),
    # User TalkList:
    url(r'^usertalk$', TalkListUserView.as_view(), name='user_list'),
    # TalkList Detail View:
    url(r'^detail/(?P<slug>[-\w]+)/$', TalkListDetailView.as_view(), name='detail'),
    # Create View:
    url(r'^create/$', TalkListCreateView.as_view(), name='create'),
    # Update View:
    url(r'^update/(?P<slug>[-\w]+)/$', TalkListUpdateView.as_view(), name='update'),
    # Test for function based detail view:
    url(r'^d/(?P<slug>[-\w]+)/$', 'talks.views.talk_list_detail', name='talklist_detail'),
 ]
 
 
 
 
urlpatterns = [
    url(r'^lists/', include(list_patterns, namespace='lists')),
 ]