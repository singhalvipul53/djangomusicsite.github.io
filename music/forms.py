from django.forms import ModelForm
from .models import *

class AlbumForm(ModelForm):
    class Meta:
        model=Album
        fields='__all__'
        exclude=['user']