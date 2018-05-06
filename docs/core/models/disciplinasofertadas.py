from django.db import models
import atividadesvinculadas


class DisciplinaOfertada(models.Model):
  ID_DisciplinaOfertada = models.AutoField(db_column='', primary_key=True)
  ID_Coordenador = models.ForeignKey('Coordenador', models.DO_NOTHING, db_column='ID_Coordenador')
  DtInicioMatricula  = models.DateField(db_column='', blank=True, null=True)
  DtFimMatricula  = models.DateField(db_column='', blank=True, null=True)
  ID_Disciplina  = models.ForeignKey('Disciplina', models.DO_NOTHING, db_column='ID_Disciplina')
  ID_Curso  = models.ForeignKey('Curso', models.DO_NOTHING, db_column='ID_Curso')
  Ano = models.IntegerField()
  Semestre = models.IntegerField()
  Turma = models.CharField(max_length=6, blank=True, null=True)
  ID_Professor  = models.ForeignKey('Professor', models.DO_NOTHING, db_column='ID_Professor', blank=True, null=True)
  Metodologia  = models.CharField(max_length=999, blank=True, null=True)
  Recursos  = models.CharField(max_length=999, blank=True, null=True)
  CriterioAvaliacao = models.CharField(db_column='CriterioAvaliacao', max_length=999, blank=True, null=True)
  PlanoDeAulas =  models.CharField(db_column='PlanoDeAulas', max_length=999, blank=True, null=True)
  class Meta:
        managed = False
        db_table = 'DisciplinaOfertada'

def retornAtiva(self):
  atividadades = atividadesvinculadas.objects.filter(
    DisciplinaOfertada = self.ID_DisciplinaOfertada, status = 'ativo'
    )
  return atividadades 

def retornNaoAtiva(self):
  atividadades = atividadesvinculadas.objects.filter(
    DisciplinaOfertada = self.ID_DisciplinaOfertada, status = 'pendente'
    )
  return atividadades 