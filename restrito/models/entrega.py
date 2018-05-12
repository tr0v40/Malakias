from django.db import models
from .atividadeVinculada import Atividadevinculada
from contas.models.aluno import Aluno
from contas.models.professor import Professor


class Entrega(models.Model):
    identrega = models.AutoField(db_column='idEntrega', primary_key=True)  # Field name made lowercase.
    idaluno = models.ForeignKey(Aluno, models.DO_NOTHING, db_column='idAluno')  # Field name made lowercase.
    titulo = models.CharField(max_length=40, blank=True, null=True)
    resposta = models.CharField(max_length=1000, blank=True, null=True)
    idatividadevinculada = models.ForeignKey(Atividadevinculada, models.DO_NOTHING, db_column='idAtividadeVinculada')  # Field name made lowercase.
    dtentrega = models.DateField(db_column='dtEntrega')  # Field name made lowercase.
    status = models.CharField(max_length=20, blank=True, null=True)
    idprofessor = models.ForeignKey(Professor, models.DO_NOTHING, db_column='idProfessor')  # Field name made lowercase.
    nota = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    dtavaliacao = models.DateField(db_column='dtAvaliacao')  # Field name made lowercase.
    obs = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'entrega'

    def __str__(self):
        return self.titulo

  

    def retornaAtividadesEnviadasAluno(disciplinaOfertada, idAluno):
        entregas = Entrega.objects.filter(idatividadevinculada__iddisciplinaofertada = disciplinaOfertada, idaluno = idAluno)
        atividadesEntregues = []
        if(len(entregas) == 0):
            return atividadesEntregues
        for entrega in entregas:
            atividadesEntregues.append(entrega.idAtividadevinculada)

        return atividadesEntregues

    def retornaAtividadesNaoEnviadasAluno(disciplinaOfertada, idAluno):
        from restrito.models.atividadeVinculada import Atividadevinculada
        atividades = Atividadevinculada.objects.filter(iddisciplinaofertada = disciplinaOfertada)
        entregas = Entrega.objects.filter(idatividadevinculada__iddisciplinaofertada = disciplinaOfertada, idaluno = idAluno)
        atividadesNaoEntregues = []
        if(len(entregas) == 0):
            return atividades
        for atividade in atividades:
            if(not bool(len(entregas.filter(idatividadevinculada=atividade.idatividadevinculada)))):
                atividadesNaoEntregues.append(atividade)

        return atividadesNaoEntregues

    def retornaAtividadesPendentesAluno(disciplinaOfertada, idAluno):
        from restrito.models.atividadeVinculada import Atividadevinculada
        from datetime import date
        atividades = Atividadevinculada.objects.filter(iddisciplinaofertada = disciplinaOfertada, dtiniciorespostas__lte=date.today(), dtfimrespostas__gte=date.today())
        entregas = Entrega.objects.filter(idatividadevinculada__iddisciplinaofertada = disciplinaOfertada, idaluno = idAluno)
        if(len(entregas) == 0):
            return atividades
        atividadesNaoEntregues = []
        for atividade in atividades:
            if(not bool(len(entregas.filter(idatividadevinculada=atividade.idatividadevinculada)))):
                atividadesNaoEntregues.append(atividade)

        return atividadesNaoEntregues

   

    def retornaAtividadesEnviadasProfessor(disciplinaOfertada):
        from restrito.models.atividadeVinculada import Atividadevinculada
        atividades = Atividadevinculada.objects.filter(iddisciplinaofertada = disciplinaOfertada)
        entregas = Entrega.objects.filter(idatividadevinculada__iddisciplinaofertada = disciplinaOfertada)
        atividadesEntregues = []
        if(len(entregas) == 0):
            return atividadesEntregues
        for atividade in atividades:
            atividadesEntregues.append(
                {
                    "atividade": atividade,
                    "entregas": entregas.filter(idatividadevinculada=atividade.idatividadevinculada)
                }
            )

        return atividadesEntregues
