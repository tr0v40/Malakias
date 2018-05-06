from django.db import models
from contas.models import Coordenador, Professor

class Disciplina(models.Model):
    idDisciplina = models.AutoField(db_column='ID_Disciplina', primary_key=True)  
    nome = models.CharField(unique=True, max_length=30, blank=True, null=True)
    data = models.DateField(blank=True, null=True)
    status = models.CharField(db_column='Status', max_length=20, blank=True, null=True)  
    planoDeEnsino = models.CharField(db_column='PlanodeEnsino', max_length=999, blank=True, null=True) 
    cargaHoraria = models.IntegerField(db_column='Cargahoraria', blank=True, null=True)  
    competencias = models.CharField(max_length=999, blank=True, null=True)
    habilidades = models.CharField(max_length=999, blank=True, null=True)
    ementa = models.CharField(max_length=999, blank=True, null=True)
    conteudoProgramatico = models.CharField(db_column='ConteudoProgramatico', max_length=999, blank=True, null=True) 
    bibliografiaBasica = models.CharField(db_column='BibliografiaBasica', max_length=999, blank=True, null=True)  
    bibliografiaComplementar = models.CharField(db_column='BibliografiaComplementar', max_length=999, blank=True, null=True) 
    percentualPratico = models.IntegerField(db_column='PercentualPratico', blank=True, null=True) 
    percentualTeorico = models.IntegerField(db_column='PercentualTeorico', blank=True, null=True)  
    idCoordenador = models.ForeignKey(Coordenador, models.DO_NOTHING, db_column='ID_Coordenador')  
    
    class Meta:
        managed = False
        db_table = 'Disciplina'

    def __str__(self):
        return self.nome


class Curso(models.Model):
    idCurso = models.AutoField(db_column='ID_Curso', primary_key=True)  
    nome = models.CharField(unique=True, max_length=30)

    class Meta:
        managed = False
        db_table = 'Curso'

    def __str__(self):
        return self.nome

class Disciplinaofertada(models.Model):
    idDisciplinaofertada = models.AutoField(db_column='ID_DisciplinaOfertada', primary_key=True)  
    idCoordenador = models.ForeignKey(Coordenador, models.DO_NOTHING, db_column='ID_Coordenador')  
    dtInicioMatricula = models.DateField(db_column='DtInicioMatricula', blank=True, null=True)  
    dtFimMatricula = models.DateField(db_column='DtFimMatricula', blank=True, null=True) 
    idDisciplina = models.ForeignKey(Disciplina, models.DO_NOTHING, db_column='ID_Disciplina')  
    idCurso = models.ForeignKey(Curso, models.DO_NOTHING, db_column='ID_Curso')  
    ano = models.IntegerField()
    semestre = models.IntegerField()
    turma = models.CharField(max_length=6, blank=True, null=True)
    idProfessor = models.ForeignKey(Professor, models.DO_NOTHING, db_column='ID_Professor', blank=True, null=True) 
    metodologia = models.CharField(max_length=999, blank=True, null=True)
    recursos = models.CharField(max_length=999, blank=True, null=True)
    criterioAvaliacao = models.CharField(db_column='CriterioAvaliacao', max_length=999, blank=True, null=True) 
    planoDeAulas = models.CharField(db_column='PlanoDeAulas', max_length=999, blank=True, null=True) 

    class Meta:
        managed = False
        db_table = 'Disciplinaofertada'

    def __str__(self):
        pass
