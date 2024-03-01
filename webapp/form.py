from django.forms import ModelForm
from webapp.models import *

class WordForm(ModelForm):
    class Meta:
        model = Word
        fields = ('word','imi')
