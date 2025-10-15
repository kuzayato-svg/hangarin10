from django.forms import ModelForm
from django import forms
from tasks.models import Category

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = "__all__"