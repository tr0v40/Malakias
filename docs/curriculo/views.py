from django.shortcuts import render


def cadastro_aluno(request):   
    contexto = {
        "titulo": "Novo aluno",
    }
    return render(request, "cadastro_aluno.html", contexto)


def novocurso(request):
    contexto={
        "titulo":"Adicionar curso",
    }
    return render(request, "novocurso.html", contexto)