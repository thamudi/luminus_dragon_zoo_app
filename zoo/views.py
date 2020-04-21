from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from .models import Dragon
from .forms import DragonForm
# Create your views here.


def dragon_list_view(request):
    query = request.GET.get('input-query-name', None)
    if query is not None:
        query_set = Dragon.objects.filter(name__icontains=query)
    else:
        query_set = Dragon.objects.all()

    context = {
        'dragons': query_set
    }

    return render(request, 'index.html', context)


def dragon_create_view(request):
    form = DragonForm(request.POST or None)

    if form.is_valid():
        new_dragon = form.save(commit=False)
        new_dragon.save()
        messages.success(request, 'Created a new dragon')

        return redirect('index')
    context = {
        'form': form
    }
    return render(request, 'create.html', context)


def dragon_edit_view(request, dragon_id=None):
    dragon = get_object_or_404(Dragon, id=dragon_id)
    dragon_form = DragonForm(request.POST or None, instance=dragon)

    if dragon_form.is_valid():
        dragon = dragon_form.save(commit=False)
        dragon.save()
        messages.success(request, 'Updated Dragon!')

        return redirect('index')
    context = {
        'form': dragon_form,
    }
    return render(request, 'edit.html', context)


def dragon_delete_view(request, dragon_id=None):
    dragon = get_object_or_404(Dragon, id=dragon_id)
    if request.method == 'POST':
        dragon.delete()
        messages.success(request, 'Dragon Deleted')

    return redirect('index')
