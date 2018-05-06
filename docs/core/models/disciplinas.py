from django.db import models

class Disciplina(models.Model):
  ID_Disciplina = models.AutoField(db_column='ID_Disciplina', primary_key=True)
  Nome = models.CharField(unique=True, max_length=30, blank=True, null=True)
  Data = models.DateField(blank=True, null=True) 
  Status = models.CharField(db_column='', max_length=20, blank=True, null=True)
  PlanoEnsino =  models.CharField(db_column='PlanoEnsino', max_length=999, blank=True, null=True)
  CargaHoraria = models.IntegerField(db_column='', blank=True, null=True)
  Competencias = models.CharField(max_length=999, blank=True, null=True)
  Habilidades = models.CharField(max_length=999, blank=True, null=True)
  Ementa = models.CharField(max_length=999, blank=True, null=True)
  ConteudoProgramatico = models.CharField(db_column='ConteudoProgramatico', max_length=999, blank=True, null=True)
  BibliografiaBasica =  models.CharField(db_column='BibliografiaBasica', max_length=999, blank=True, null=True)
  BibliografiaComplementar = models.CharField(db_column='BibliografiaComplementar', max_length=999, blank=True, null=True)
  PercentualPratico = models.IntegerField(db_column='PercentualPratico', blank=True, null=True)
  PercentualTeorico = models.IntegerField(db_column='PercentualTeorico', blank=True, null=True)
  ID_Coordenador = models.ForeignKey('Coordenador', models.DO_NOTHING, db_column='ID_Coordenador')
  class Meta:
        managed = False
        db_table = 'Disciplina'