from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from tasks.models import Category, Note
from tasks.forms import CategoryForm, NoteForm
from django.urls import reverse_lazy

class HomePageView(ListView):
    model = Category 
    context_object_name = 'home' 
    template_name = 'home.html'
    
##ListView  
class CategoryList(ListView):
    model = Category
    context_object_name = 'category'
    template_name = 'category_list.html'
    paginate_by = 5  
    
class NoteList(ListView):
    model = Note 
    context_object_name = 'note'
    template_name = 'note_list.html'
    paginate_by = 5
    
    
    

##CreateView
class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category_form.html'
    success_url = reverse_lazy('category-list')
    
class NoteCreateView(CreateView):
    model = Note
    form_class = NoteForm
    template_name = 'note_form.html'
    success_url = reverse_lazy('note-list')
    
    
    
    
##UpdateView
class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category_form.html'
    success_url = reverse_lazy('category-list')

class NoteUpdateView(UpdateView):
    model = Note
    form_class = NoteForm
    template_name = 'note_form.html'
    success_url = reverse_lazy('note-list')
    
    
    
    
##DeleteView
class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'category_del.html'
    success_url = reverse_lazy('category-list')