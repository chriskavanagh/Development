from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse


# Create your models here.
# 
class Article(models.Model):
    """class for our articles"""
    title = models.CharField(max_length=254)
    body = models.TextField()
    pub_date = models.DateTimeField('date published', auto_now_add=True, auto_now=False)
    # likes = models.IntegerField()
    
    def __unicode__(self):
        return self.title
        
    def get_absolute_url(self):
        return reverse('article', kwargs={'pk': self.pk})
        

class Comment(models.Model):
    """class for our comments"""
    first_name = models.CharField(max_length=200)
    second_name = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField('date published')
    article = models.ForeignKey(Article, related_name='comments')
