from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url, include
from curriculo.views import *

urlpatterns = [
    path('nova-disciplina/', inserirDisciplina, name="nova-disciplina"),


    path('novo-curso/', inserirCurso, name="novo-curso"),
    path('deletarcurso/<int:idcurso>/', deletarCurso, name = 'deletarcurso'),
    path('alterarcurso/<int:idcurso>/', alterarCurso, name = 'alterarcurso'),
    path('listarcursos/', listarCursos, name = "listarcursos"),
]