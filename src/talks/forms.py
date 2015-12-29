from __future__ import absolute_import
from django.core.exceptions import ValidationError
from django.utils.timezone import utc
import datetime
from django import forms
from .models import TalkList, Talk

class TalkListForm(forms.ModelForm):
    class Meta:
        fields = ('name',)
        model = TalkList
        
        
class TalkForm(forms.ModelForm):
    class Meta:
        fields = ('name', 'host', 'when', 'room')
        model = Talk
        
    def clean_when(self):
        when = self.cleaned_data.get('when')
        pycon_start = datetime.datetime(2016, 4, 11).replace(tzinfo=utc)
        pycon_end = datetime.datetime(2016, 4, 13, 17).replace(tzinfo=utc)
        if not pycon_start < when < pycon_end:
            raise ValidationError("'when' is outside of PyCon.")
        return when


