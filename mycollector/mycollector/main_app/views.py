from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Pants, Top, Pants, Occasion
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.views.generic import ListView, DetailView
# Create your views here.


class TopCreate(CreateView):
    model = Top
    fields =["name", "description", "image", "size"]
    success_url = '/tops/'

def home(request):
    return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def top_index(request):
    tops = Top.objects.all()
    # SELECT * from Cat
    return render(request, 'tops/index.html', { 'tops': tops})

def top_details(request, top_id):
    top = Top.objects.get(id=top_id)
    return render(request, 'tops/detail.html', {'top': top})

class TopUpdate(UpdateView):
    model = Top
    fields = "__all__"

class TopDelete(DeleteView):
    model = Top
    success_url = '/tops/'

class PantsList(ListView):
    model = Pants

class Pant(DetailView):
    model = Pants

class PantCreate(CreateView):
    model = Pants
    fields = ["name", "size"]
    success_url = '/pants/'

class PantsUpdate(UpdateView):
    model = Pants
    fields = "__all__"

class PantsDelete(DeleteView):
    model = Pants
    success_url = '/pants/'

def assoc_outfit(request, top_id, pants_id):
    Top.objects.get(id=top_id).pants.add(pants_id)
    return redirect('detail', top_id=top_id)

def unassoc_outfit(request, top_id, pants_id):
    Top.objects.get(id=top_id).pants.remove(pants_id)
    return redirect('detail', top_id=top_id)