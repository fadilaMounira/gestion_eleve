from django.shortcuts import render,HttpResponseRedirect
from .forms import enregistrementEleve
from .models import User 

# Create your views here.
# cette fonction permet d'ajouter et d'afficher les informations 
def add_show(request):
    if request.method == 'POST':
        fm = enregistrementEleve(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            dn = fm.cleaned_data['naissance']
            sx = fm.cleaned_data['sexe']
            nv = fm.cleaned_data['niveau']
            reg = User(name = nm,email = em , password = pw,naissance = dn,sexe = sx, niveau = nv)
            reg.save()
            fm = enregistrementEleve()
    else:
        fm = enregistrementEleve()
    eleve = User.objects.all()
    return render(request, 'eleve/addandshow.html',{'form':fm, 'stu':eleve})

# cette fonction permet de modifier les informations
def update_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = enregistrementEleve(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi= User.objects.get(pk=id)
        fm = enregistrementEleve(instance=pi)
    return render(request, 'eleve/updateeleve.html',{'form':fm})

#cette  fonction permet de supprimer des données
def delete_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
            