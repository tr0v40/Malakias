from django.db import models

class Atividade(models.Model):
  ID_Atividade = models.AutoField(db_column='ID_Atividade', primary_key=True)
  Titulo =  models.CharField(max_length=50, blank=True, null=True)
  Descricao  = models.CharField(max_length=999)
  Conteudo  = models.CharField(max_length=999, blank=True, null=True)
  Tipo  = models.CharField(max_length=50, blank=True, null=True)
  Extras  = models.CharField(max_length=999, blank=True, null=True)
  ID_Professor  = models.CharField(max_length=999, blank=True, null=True)
  class Meta:
        managed = False
        db_table = 'Atividade'