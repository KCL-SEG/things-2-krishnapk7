from django.shortcuts import render
from .forms import ThingForm

def home(request):
    form = ThingForm()
    return render(request, 'home.html', {'form': form})
