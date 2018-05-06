from django.db import models



class AtividadeVinculada(models.Model):
  ID_AtividadeVinculada  = models.AutoField(db_column='ID_AtividadeVinculada', primary_key=True)
  ID_Atividade  = models.ForeignKey('Atividade', models.DO_NOTHING, db_column='ID_Atividade')
  ID_Professor  = models.ForeignKey('Professor', models.DO_NOTHING, db_column='ID_Professor')
  ID_DisciplinaOfertada  = models.ForeignKey('DisciplinaOfertada', models.DO_NOTHING, db_column='ID_DisciplinaOfertada')
  Rotulo  = models.CharField(max_length=100)
  Status = models.CharField(max_length=100)
  DtInicioRespostas  = models.DateField(db_column='DtInicioRespostas', blank=True, null=True)
  DtFimRespostas  = models.DateField(db_column='DtFimRespostas', blank=True, null=True)
  class Meta:
        managed = False
        db_table = 'AtividadeVinculada'

  entregue = 0 
  nao_entregue = 0

 


