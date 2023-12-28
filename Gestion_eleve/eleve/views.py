from django.shortcuts import render
from .forms import enregistrementEleve
from .models import User 

# Create your views here.
def add_show(request):
    if request.method == 'POST':
        fm = enregistrementEleve(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name = nm,email = em , password = pw)
            reg.save()
            fm = enregistrementEleve()
    else:
        fm = enregistrementEleve()
    return render(request, 'eleve/addandshow.html',{'form':fm})