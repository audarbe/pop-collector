from django.shortcuts import render, redirect
from .models import Pop, Accessory, Limited
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import LimitedForm

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

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        context['limited_form'] = LimitedForm()
        context['accessories'] = Accessory.objects.exclude(pk=self.object.id)
        return context

def assoc_accessory(request, pop_id, accessory_id):
    pop = Pop.objects.get(pk=pop_id)
    pop.accessories.add(accessory_id)
    return redirect('pops_detail', pk=pop_id)

class PopCreate(CreateView):
    model = Pop
    fields = ['name', 'serial', 'details', 'category', 'price']
    success_url = '/pops/'

class PopUpdate(UpdateView):
    model = Pop
    fields = ['serial', 'details', 'category', 'price']

class PopDelete(DeleteView):
    model = Pop
    success_url = '/pops/'

def add_limited(request, pop_id):
    form = LimitedForm(request.POST)
    if form.is_valid():
            new_limited = form.save(commit=False)
            new_limited.pop_id = pop_id
            new_limited.save()
    return redirect('pops_detail', pk=pop_id)
