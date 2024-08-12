from django.forms import ModelForm
from .models import perfume
from django import forms

class CreatePerfumeForm(ModelForm):
    class Meta:
        model = perfume
        fields = "__all__"
        widgets = {'ingredient':forms.Textarea(),'How_to_make':forms.Textarea(),
                   'created_by':forms.HiddenInput()}