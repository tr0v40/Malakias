from django.shortcuts import render, redirect
from .models.professor import Professor
from .models.aluno import Aluno
from .models.coordenador import Coordenador
from restrito.models.solicitacaoMatricula import Solicitacaomatricula
import base64
import hashlib


def listarProfessores(request):
    professores = Professor.objects.all()
    return render(request, 'listaProfessores.html', {'professores': professores})

def inserirProfessor(request):
    context = {}
    if request.method == 'POST':
        Professor.objects.create (
        logon = request.POST.get('logon'),
        senha = request.POST.get('senha'),
        nome = request.POST.get('nome'),
        email = request.POST.get('email'),
        celular = request.POST.get('celular'),
        dtexpiracao = request.POST.get('dtexpiracao'),
        apelido = request.POST.get('apelido')
        )        
        return redirect('listarprofessores')
    else:
        return render(request, 'formNovoProfessor.html', context)

def alterarProfessor(request, idprofessor):
    professor = Professor.objects.get(idprofessor=idprofessor)
    if request.method == 'POST':
       professores = Professor.objects.get(idprofessor=idprofessor)
       professores.logon = request.POST.get('logon'),
       professores.senha = request.POST.get('senha'),
       professores.nome = request.POST.get('nome'),
       professores.email = request.POST.get('email'),
       professores.celular = request.POST.get('celular'),
       professores.dtExpiracao = request.POST.get('dtexpiracao'),
       professores.apelido = request.POST.get('apelido')
       professores.save()
       return redirect('listarprofessores')
    else:
        return render(request, 'formNovoProfessor.html', {'professor':professor})


def deletarProfessor(request, idprofessor):
    professores = Professor.objects.get(idprofessor=idprofessor)
    professores.delete()
    return redirect ('listarprofessores')


def listarAlunos(request):
    alunos = Aluno.objects.all()
    return render(request, 'listaAlunos.html', { 'alunos' : alunos })

def inserirAluno(request):
    if request.method == 'POST':
        encoded = base64.b64encode(file.read())
        #senha = hashlib.sha224(request.POST.get("senha").encode('utf-8')).hexdigest()
        #print(senha);
        Aluno.objects.create(
            logon=request.POST.get("logon"),
            senha=request.POST.get("senha"),
            nome=request.POST.get("nome"),
            email=request.POST.get("email"),
            celular=request.POST.get("celular"),
            foto=encoded
        )

        return redirect('listaralunos')
    else:
        return render(request, "formNovoAluno.html")

def alterarAluno(request, idaluno):
    aluno = Aluno.objects.get(idaluno=idaluno)
    aluno.foto = aluno.foto[2:-1]
    if request.method == 'POST':
        file = request.FILES['foto']
        encoded = base64.b64encode(file.read())
        #senha = hashlib.sha224(request.POST.get("senha").encode('utf-8')).hexdigest()

        aluno = Aluno.objects.get(idaluno=idaluno)
        aluno.logon=request.POST.get("logon")
        aluno.senha=request.POST.get("senha")
        aluno.nome=request.POST.get("nome")
        aluno.email=request.POST.get("email")
        aluno.celular=request.POST.get("celular")
        aluno.foto=encoded
        aluno.save()
        return redirect('listaralunos')
    else:
        return render(request, "formNovoAluno.html",  {"aluno":aluno})

def deletarAluno(request, idaluno):
    aluno = Aluno.objects.get(idaluno=idaluno)
    aluno.delete()
    return redirect ('listaralunos')

def listarCoordenadores(request):
    coordenadores = Coordenador.objects.all()
    return render(request, 'listaCoordenadores.html', {'coordenadores': coordenadores})

def inserirCoordenador(request):
    if request.method == 'POST':
        Coordenador.objects.create (
            logon=request.POST.get("logon"),
            senha=request.POST.get("senha"),
            nome=request.POST.get("nome"),
            email=request.POST.get("email"),
            celular=request.POST.get("celular")
        )
        return redirect('listarcoordenadores')
    else:
        return render(request, "formNovoCoordenador.html")

def alterarCoordenador(request, idcoordenador):
    coordenador = Coordenador.objects.get(idcoordenador=idcoordenador)
    if request.method == 'POST':
        coordenador = Coordenador.objects.get(idcoordenador=idcoordenador)
        coordenador.logon=request.POST.get("logon")
        coordenador.senha=request.POST.get("senha")
        coordenador.nome=request.POST.get("nome")
        coordenador.email=request.POST.get("email")
        coordenador.celular=request.POST.get("celular")
        coordenador.save()
        return redirect('listarcoordenadores')
    else:
        return render(request, "formNovoCoordenador.html", { "coordenador" : coordenador })

def deletarCoordenador(request, idcoordenador):
    coordenador = Coordenador.objects.get(idcoordenador=idcoordenador)
    coordenador.delete()
    return redirect ('listarcoordenadores')