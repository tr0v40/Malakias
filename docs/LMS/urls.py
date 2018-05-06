from django.conf.urls import url
from django.contrib import admin
from core import views
from curriculo.views import novocurso, cadastro_aluno
from django.urls import path 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name ='index'),
    path('cadastro-disciplina/', views.cadastro_disciplina, name = "cadastro_disciplina"),
    path('cursos/', views.cursos, name="cursos"),
    path('novo-curso/', novocurso, name = "novocurso"),
    path('cadastro-aluno/', cadastro_aluno, name ="cadastro_aluno"),
    path('cursos/grade-ads/', views.grade_ads, name="grade_ads"),
    path('cursos/grade-redes/',views.grade_redes, name="grade_redes"),
    path('cursos/grade-bd/', views.grade_bd, name = "grade_bd"),
    path('cursos/desc-ads/', views.desc_ads, name = "cursos/desc_ads"),
    path('cursos/desc-bd/', views.desc_bd, name= "cursos/desc_bd"),
    path('cursos/desc-redes/', views.desc_redes, name = "cursos/desc_redes"),
    path('cursos/desc-bd-lp/', views.desc_bd_lp, name = "cursos/desc_bd_lp"),
    path('cursos/desc-bd-fbd/', views.desc_bd_fbd, name ="cursos/desc_bd_fbd"),
    path('cursos/desc-bd-dba/', views.desc_bd_dba, name ="desc_bd_dba"),
    path('cursos/desc-ads/grade-ads/', views.grade_ads, name="grade_ads"),
    path('cursos/desc-ads/grade-bd/', views.grade_bd, name="grade_bd"),
    path('cursos/desc-ads/grade-redes/', views.grade_redes, name="grade_redes"),
    path('login/', views.login, name = "login"),
    path('tabela-aluno/', views.tabela_aluno, name = "tabela_aluno"),  
    path('cadastro-disciplina', views.cadastro_disciplina, name="cadastro_disciplina"),
]