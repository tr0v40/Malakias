from django.db import models

class Mensagem(models.Model):
  ID_Mensagem = models.AutoField(db_column='ID_Mensagem', primary_key=True)
  ID_Aluno  = models.ForeignKey('Aluno', models.DO_NOTHING, db_column='ID_Aluno')
  ID_Professor  = models.ForeignKey('Professor', models.DO_NOTHING, db_column='ID_Professor')
  Assunto  = models.CharField(max_length=999, blank=True, null=True)
  Referencia  = models.CharField(max_length=999, blank=True, null=True)
  Conteudo  =  models.CharField(max_length=999, blank=True, null=True)
  Status  = models.CharField(max_length=50, blank=True, null=True)
  DtEnvio  = models.DateField(db_column='DtEnvio', blank=True, null=True)
  DtResposta  = models.DateField(db_column='DtResposta')
  Resposta  = models.CharField(max_length=999, blank=True, null=True)
  class Meta:
        managed = False
        db_table = 'Mensagem'