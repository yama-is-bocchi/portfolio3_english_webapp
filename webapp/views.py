from django.views import generic
from webapp.models import *
from webapp.form import WordForm
from django.shortcuts import *
import random
import time

def index(request):
    return render(request, 'webapp/index.html')

def setting_page(request):
    return render(request, 'webapp/setting.html')


def edit_word_page(request):
    word_list = Word.objects.all()
    return render(request, 'webapp/word_edit.html', {'word_list': word_list})

def view_word_page(request):
    word_list = Word.objects.all()
    return render(request, 'webapp/word_view.html', {'word_list': word_list})


def updateword(request, pk):
    obj = get_object_or_404(Word, id=pk)
    if request.method == "POST":
        form = WordForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            word_list = Word.objects.all()
            return render(request, 'webapp/word_edit.html', {'word_list': word_list})
    else:
        form = WordForm(instance=obj)
        return render(request, 'webapp/word_input.html', {'form': form})
    
def add_word_page(request):
    if request.method == "POST":
        form = WordForm(request.POST)
        if form.is_valid():
            d = form.save(commit=False)
            d.save()
            return redirect('webapp:add_word_page')
    else:
        form=WordForm()
        return render(request, 'webapp/word_input.html', {'form': form})
    
def deleteword(request, pk):
    obj = get_object_or_404(Word, id=pk)
    obj.delete() 
    word_list = Word.objects.all()
    return render(request, 'webapp/word_edit.html', {'word_list': word_list})


def start_game(request):
    word_class=Word.objects.all()
    pks=word_class.order_by('?')[:4]
    pks_list=list(pks)
    if len(pks)<4:
        return render(request, 'webapp/index.html')
    else:
        imi=pks_list
        none=random.sample(imi,len(imi))
        p_list=pks_list+none
        return render(request, 'webapp/main.html', {'word_list': p_list})

def start_eng_game(request):
    word_class=Word.objects.all()
    pks=word_class.order_by('?')[:4]
    pks_list=list(pks)
    if len(pks)<4:
        return render(request, 'webapp/index.html')
    else:
        imi=pks_list
        none=random.sample(imi,len(imi))
        p_list=pks_list+none
        return render(request, 'webapp/main_two.html', {'word_list': p_list})
