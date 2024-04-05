from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import SkinForm

def index(request):
  return render (request, 'index.html')

def addskin(request):
  if request.method == 'POST':
      form = SkinForm(request.POST, request.FILES)
      if form.is_valid():
          form.save()
          return redirect('/')  # Redirecionar para uma página de sucesso após a inserção
  else:
      form = SkinForm()
  return render(request, 'addskin.html', {'form': form})