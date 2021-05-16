from django.forms import ModelForm
from .models import cvModel

class cvForm(ModelForm):
    class Meta:
        model = cvModel
        fields = "__all__"