from django.shortcuts import render, redirect
from .models import Recepie
from .forms import CreateRecepieForm, EditRecepieForm, DeleteRecepieForm
# Create your views here.
#home_page, create_recepie, edit_recepie, recepie_details, delete_recepie

def home_page(request):
    recepies = Recepie.objects.all()

    context = {
        'recepies': recepies
    }

    return render(request, 'recepies_app/home-page.html', context=context)


def create_recepie(request):
    form = CreateRecepieForm()

    if request.method == 'POST':
        form = CreateRecepieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home-page')

    context = {
        'form': form
    }

    return render(request, 'recepies_app/create.html', context=context)



def edit_recepie(request, recepie_id):
    recepie = Recepie.objects.get(id=recepie_id)
    form = EditRecepieForm(instance=recepie)

    if request.method == 'POST':
        form = EditRecepieForm(request.POST, instance=recepie)
        if form.is_valid():
            form.save()
            return redirect('home-page')

    context = {
        'form': form
    }

    return render(request, 'recepies_app/edit.html', context=context)
def recepie_details(request, recepie_id):
    recepie = Recepie.objects.get(id=recepie_id)
    ingridients_list = recepie.ingridients.split(", ")
    context = {
        'recepie': recepie,
        'ingridients_list': ingridients_list
    }

    return render(request, 'recepies_app/details.html', context=context)

def delete_recepie(request, recepie_id):
    recepie = Recepie.objects.get(id=recepie_id)
    form = DeleteRecepieForm(instance=recepie)

    if request.method == 'POST':
        recepie.delete()
        return redirect('home-page')

    context = {
        'form': form
    }

    return render(request, 'recepies_app/delete.html', context=context)
