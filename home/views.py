from django.core.checks import messages
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import RegistrationForm
# Create your views here.
def index(request):
   return render(request, 'pages/home.html')

def about(request):
   return render(request, 'pages/about.html')

def error(request, exception):
   return render(request, 'pages/error.html', {'message': exception})

def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
       form = RegistrationForm(request.POST)
       if form.is_valid():
          form.save()
          return HttpResponseRedirect('/')
    return render(request, 'pages/register.html', {'form': form})