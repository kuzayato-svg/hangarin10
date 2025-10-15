from django.forms import ModelForm
from django import forms
from tasks.models import Category, Note

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = "__all__"

class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = "__all__"