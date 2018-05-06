from django.db import models

class SolicitacaoMatricula(models.Model):
  ID_SolicitacaoMatricula = models.AutoField(db_column='ID_SolicitacaoMatricula', primary_key=True) 
  ID_Aluno = models.ForeignKey('Aluno', models.DO_NOTHING, db_column='')
  ID_DisciplinaOfertada = models.ForeignKey('Disciplinaofertada', models.DO_NOTHING, db_column='ID_DisciplinaOfertada')
  DtSolicitacao  = models.DateField(db_column='DtSolicitacao')
  ID_Coordenador = models.ForeignKey('Coordenador', models.DO_NOTHING, db_column='ID_Coordenador', blank=True, null=True)
  Status = models.CharField(max_length=100, blank=True, null=True)
  class Meta:
        managed = False
        db_table = 'SolicitacaoMatricula'