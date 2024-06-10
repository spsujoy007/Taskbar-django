from django.shortcuts import render,redirect
from . import forms
from .models import CategoryModel

# Create your views here.
def add_category(req):
    categories = CategoryModel.objects.all()
    if req.method == "POST":
        add_category = forms.CategoryForm(req.POST)
        if add_category.is_valid():
            add_category.save()
            return redirect('add_category')
    else:
        add_category = forms.CategoryForm()
    return render(req, 'add_category.html', {'form' : add_category, 'categories': categories})