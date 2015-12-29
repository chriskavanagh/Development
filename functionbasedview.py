from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from .models import TalkList, Talk
from .forms import TalkListForm, TalkForm


def talk_list_detail(request, slug):
    talklist_detail = get_object_or_404(TalkList, slug=slug)
    #talklist_detail = Talk.objects.filter(talk_list__slug=slug)
    form = TalkForm(request.POST or None)    # otherwise get form unbound form error
    if form.is_valid():
        talk = form.save(commit=False)
        talk.talk_list_id = talklist_detail.id
        talk.save()
        return redirect(talklist_detail)

    context = {'talklist_detail': talklist_detail, 'form': form}
    return render(request, 'talk_list_detail.html', context)



from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models
from django.template.defaultfilters import slugify
from django.conf import settings
from django.contrib.auth.models import User


class TalkListUserManager(models.Manager):
    def get_queryset(self):
        return super(TalkListUserManager, self).get_queryset().filter(name='Pycon Talks')
        
        

# Create your models here.
class TalkList(models.Model):
    user = models.ForeignKey(User, related_name='lists')
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, blank=True)
    
    objects = models.Manager() # The default manager.
    talklist_user_objects = TalkListUserManager()
    
    
    class Meta:
        unique_together = ('user', 'name')
        
    def __unicode__(self):
        return self.name
        
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(TalkList, self).save(*args, **kwargs)
        
    def get_absolute_url(self):
        return reverse('talks:lists:detail', kwargs={'slug': self.slug})   
            
            
            
class Talk(models.Model):
    ROOM_CHOICES = (
        ('517D', '517D'),
        ('517C', '517C'),
        ('517AB', '517AB'),
        ('520', '520'),
        ('710A', '710A')    
    )
    
    talk_list = models.ForeignKey(TalkList, related_name='talks')
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, blank=True)
    when = models.DateTimeField()
    room = models.CharField(max_length=10, choices=ROOM_CHOICES)
    host = models.CharField(max_length=255)    
    
    class Meta:
        ordering = ('when', 'room')
        unique_together = ('talk_list', 'name')
        
    def __unicode__(self):
        return self.name
        
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Talk, self).save(*args, **kwargs)
