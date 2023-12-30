from django.shortcuts import render, redirect
from .models import Pessoa

# Create your views here.
def home(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'index.html', {'pessoas':pessoas})

def salvar(request):
    nome = request.POST.get('nome')
    idade = request.POST.get('idade')
    Pessoa.objects.create(nome=nome, idade=idade)
    pessoas = Pessoa.objects.all()
    return render(request, 'index.html', {'pessoas':pessoas})

def atualizar(request, id):
    pessoa = Pessoa.objects.get(id=id)
    return render(request, 'atualizar.html', {'pessoa':pessoa})

def editar(request, id):
    novo_nome = request.POST.get('nome')
    nova_idade = request.POST.get('idade')
    pessoa = Pessoa.objects.get(id=id)
    pessoa.nome = novo_nome
    pessoa.idade = nova_idade
    pessoa.save()
    return redirect(home)

def deletar(request, id):
    pessoa = Pessoa.objects.get(id=id)
    pessoa.delete()
    return redirect(home)