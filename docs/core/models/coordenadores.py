from django.db import models

class Coordenador(models.Model):
  ID_Coordenador = models.AutoField(db_column='ID_Coordenador', primary_key=True )
  Login =  models.CharField(unique=True, max_length=20, blank=True, null=True)
  Senha = models.CharField(max_length=15)
  Nome = models.CharField(max_length=40)
  Email = models.CharField(unique=True, max_length=30)
  Celular = models.CharField(unique=True, max_length=9, blank=True, null=True)
  DtExpiracao = models.DateField(db_column='DtExpiracao', blank=True, null=True)
  class Meta:
        managed = False
        db_table = 'Coordenador'