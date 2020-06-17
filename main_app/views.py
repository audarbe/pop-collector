from django.shortcuts import render
from .models import Pop
from django.views.generic import ListView, DetailView, CreateView

# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

class PopList(ListView):
    model = Pop
    template_name = 'pops/index.html'

class PopDetail(DetailView):
    model = Pop
    template_name = 'pops/detail.html'

class PopCreate(CreateView):
    model = Pop
    fields = '__all__'
    success_url = '/pops/'