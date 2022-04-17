from dataclasses import fields
from django.forms import ModelForm
from .models import Occasion


class OccasionForm(ModelForm):
    class Meta:
        model = Occasion
        fields = ['pant','top']