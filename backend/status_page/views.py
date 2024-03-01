from .forms import ComponentForm
from .models import Component
from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import get_object_or_404, render


# ...
def index(request):
    return render(request, "index.html")


def history(request):
    return render(request, "history.html")


def detail(request):
    return render(request, "detail.html")


# def management(request):
#     return render(request, "management.html")


def component_list(request):
    components = Component.objects.all()
    return render(request, 'management.html', {'components': components})


def component_create(request):
    if request.method == 'POST':
        form = ComponentForm(request.POST)
        print('form', form)
        if form.is_valid():
            form.save()
            return redirect('management')


def component_update(request, pk):
    component = get_object_or_404(Component, pk=pk)
    if request.method == 'PUT':
        form = ComponentForm(request.POST, instance=component)
        if form.is_valid():
            form.save()
            return redirect('component_list')
    else:
        form = ComponentForm(instance=component)
    return render(request, 'management.html', {'form': form})


def component_detail(request, pk):
    component = get_object_or_404(Component, pk=pk)
    if request.method == 'GET':
        form = ComponentForm(request.POST, instance=component)
        if form.is_valid():
            form.save()
            return redirect('component_list')
    else:
        form = ComponentForm(instance=component)
    return render(request, 'management.html', {'form': form})


def component_delete(request, pk):
    component = get_object_or_404(Component, pk=pk)
    if request.method == 'DELETE':
        component.delete()
        return redirect('component_list')
    return render(request, 'management.html', {'component': component})
