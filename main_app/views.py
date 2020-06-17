from django.shortcuts import render
from .models import Pop
from django.views.generic import ListView
from django.views.generic.detail import DetailView

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

