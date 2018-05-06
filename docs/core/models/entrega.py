from django.db import models
from core import models

class Entrega(models.Model):
    idEntrega = models.AutoField(db_column='ID_Entrega', primary_key=True)
    idAluno = models.ForeignKey(Aluno, models.DO_NOTHING, db_column='ID_Aluno')  
    titulo = models.CharField(max_length=50, blank=True, null=True)
    resposta = models.CharField(max_length=150, blank=True, null=True)
    idAtividadeVinculada = models.ForeignKey(AtividadeVinculada, models.DO_NOTHING, db_column='ID_AtividadeVinculada')  
    dtEntrega = models.DateField(db_column='DtEntrega') 
    status = models.CharField(max_length=20, blank=True, null=True)
    idProfessor = models.ForeignKey('Professor', models.DO_NOTHING, db_column='ID_Professor') 
    nota = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    dtAvaliacao = models.DateField(db_column='DtAvaliacao')  
    obs = models.CharField(max_length=999, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'Entrega'

def retornaAvaliada(self):
    atividadeAvaliada = entregas.objects.filter(
        Entrega = self.ID_Entrega, self.status = 'Avaliada'
    )
    return Entrega

def retornaNaoAvaliada(self):
    atividadeAvaliada = entregas.objects.filter(
        Entrega = self.ID_Entrega, self.status = 'Nao Avaliada'
    )
    return Entrega