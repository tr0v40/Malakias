from django.db import models
 import disciplinasofertadas



class Entrega(models.Model):
  ID_Entrega  = models.AutoField(db_column='ID_Entrega', primary_key=True)
  ID_Aluno  =  models.ForeignKey('Aluno', models.DO_NOTHING, db_column='ID_Aluno')
  AtividadeVinculada  = models.ForeignKey('Atividadevinculada', models.DO_NOTHING, db_column='AtividadeVinculada')
  Titulo  = models.CharField(max_length=40, blank=True, null=True)
  Resposta  = models.CharField(max_length=999, blank=True, null=True)
  DtEntrega  =  models.DateField(db_column='DtEntrega')
  Status = models.CharField(max_length=20, blank=True, null=True)
  ID_Professor = models.ForeignKey('Professor', models.DO_NOTHING, db_column='ID_Professor')
  Nota  = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
  DtAvaliacao  =  models.DateField(db_column='DtAvaliacao')
  Obs = models.CharField(max_length=999, blank=True, null=True)
  class Meta:
        managed = False
        db_table = 'Entrega'


def retornAvaliada(self):
    atividadeAvaliada = entregas.objects.filter(
    Entrega = self.ID_Entrega, self.Status, status = 'avaliada'
    )
    return Entrega

def retornNaoAvaliada(self):
    atividadeAvaliada = entregas.objects.filter(
    Entrega = self.ID_Entrega, self.Satus, status = 'Nao Avaliada'
    )
    return Entrega 
