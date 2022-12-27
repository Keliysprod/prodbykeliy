from django.forms import ModelForm
from .models import Computers

class ComputersForm(ModelForm):
    class Meta:
        model = Computers
        fields = (
            'title','inf','price','image'
        )