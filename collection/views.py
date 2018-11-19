from django.shortcuts import render, redirect
from collection.forms import CheeseForm
from collection.models import Cheese

# Create your views here.
def index(request):
    # this is your new view
    cheeses = Cheese.objects.all()
    return render(request, 'index.html', { 'cheeses': cheeses,})

def cheese_detail(request, slug):
    cheese = Cheese.objects.get(slug=slug)
    return render(request, 'cheeses/cheese_detail.html', {'cheese': cheese})

def edit_cheese(request, slug):
    cheese = Cheese.objects.get(slug=slug)
    form_class = CheeseForm
    if request.method == 'POST':
        form = form_class(data=request.POST, instance=cheese)
        if form.is_valid():
            form.save()
            return redirect('cheese_detail', slug=cheese.slug)
    else:
        form = form_class(instance=cheese)
    return render(request, 'cheeses/edit_cheese.html', {'cheese': cheese, 'form': form,})