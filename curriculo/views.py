from django.shortcuts import render, redirect
from .models.curso import Curso
from contas.models.coordenador import Coordenador
from curriculo.models.disciplina import Disciplina
# from .models.disciplinaOfertada import Disciplinaofertada
# from .models.disciplina import Disciplina


def cadastro_aluno(request):   
    context = {
        "titulo": "Novo aluno",
    }
    return render(request, "cadastro_aluno.html", context)

""" ---------------- CRUD CURSO ------------------"""
def listarCursos(request):
    cursos = Curso.objects.all()
    return render(request, 'listaCursos.html', {'cursos': cursos})

    
def inserirCurso(request):
    context = {}
    if request.method == 'POST':
        Curso.objects.create(
            nome = request.POST.get("novoCurso")
        )
        return redirect('listarcursos')
    else:
        return render(request, "novocurso.html", context)

def deletarCurso(request, idcurso):
    curso = Curso.objects.get(idcurso=idcurso)
    curso.delete()
    return redirect('listarcursos')

def alterarCurso(request, idcurso):
    cursos = Curso.objects.get(idcurso=idcurso)
    context = {"cursos": cursos}
    if request.method == 'POST':
        curso = Curso.objects.get(idcurso=idcurso)
        curso.nome = request.POST.get('novoCurso')
        curso.save()
        return redirect('listarcursos')
    else:
        return render(request, "novocurso.html", {'cursos': cursos})

""" ---------------------------------------------------------"""

""" -------------------CRUD DISCIPLINA-------------------------"""
def inserirDisciplina(request):
    contexto = {'coordenadores': Coordenador.objects.all()}
    if request.method == 'POST':
        idcoordenador = Coordenador.objects.get(idcoordenador=request.POST.get("coordenador"))
        Disciplina.objects.create(
            nome=request.POST.get("nome_disciplina"),
            data=request.POST.get("data"),
            statusdisc=request.POST.get("status"),
            planodeensino=request.POST.get("plano_ensino"),
            cargahoraria=request.POST.get("carga_horaria"),
            competencias=request.POST.get("competencias"),
            habilidades=request.POST.get("habilidades"),
            ementa=request.POST.get("ementa"),
            conteudoprogramatico=request.POST.get("conteudo_programatico"),
            bibliografiabasica=request.POST.get("bib_basica"),
            bibliografiacomplementar=request.POST.get("bibcomplementar"),
            percentualpratico=request.POST.get("porc_pratico"),
            percentualteorico=request.POST.get("porc_teorico"),
            idcoordenador=idcoordenador
        )
        return redirect('listardisciplinas')
    else:
        return render(request, "novaDisciplina.html", contexto)