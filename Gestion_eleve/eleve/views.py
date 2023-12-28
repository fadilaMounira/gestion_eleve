from django.shortcuts import render
from .forms import enregistrementEleve

# Create your views here.
def add_show(request):
    if request.method == 'POST':
        fm = enregistrementEleve(request.POST)
    else:
        fm = enregistrementEleve()
    return render(request, 'eleve/addandshow.html',{'form':fm})