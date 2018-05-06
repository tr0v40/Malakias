#IMPORTS
from django.db import models

#MODELS
class SolicitacaoMatricula(models.Model):
    idSolicitacaoMatricula = models.AutoField(db_column='ID_SolicitacaoMatricula', primary_key=True) 
    idAluno = models.ForeignKey(Aluno, models.DO_NOTHING, db_column='ID_Aluno')  
    idDiscipliNaoOfertada = models.ForeignKey(Disciplinaofertada, models.DO_NOTHING, db_column='ID_DisciplinaOfertada') 
    dtSolicitacao = models.DateField(db_column='DtSolicitacao') 
    idCoordenador = models.ForeignKey(Coordenador, models.DO_NOTHING, db_column='ID_Coordenador', blank=True, null=True)  
    status = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SolicitacaoMatricula'

class Atividade(models.Model):
    idAtividade = models.AutoField(db_column='ID_Atividade', primary_key=True) 
    titulo = models.CharField(max_length=50, blank=True, null=True)
    descricao = models.CharField(max_length=999)
    conteudo = models.CharField(max_length=999, blank=True, null=True)
    tipo = models.CharField(max_length=15, blank=True, null=True)
    extra = models.CharField(max_length=999, blank=True, null=True)
    idProfessor = models.ForeignKey('Professor', models.DO_NOTHING, db_column='ID_Professor')

    class Meta:
        managed = False
        db_table = 'Atividade'

class AtividadeVinculada(models.Model):
    idAtividadeVinculada = models.AutoField(db_column='ID_AtividadeVinculada', primary_key=True)  
    idProfessor = models.ForeignKey('Professor', models.DO_NOTHING, db_column='ID_Professor')  
    idAtividade = models.ForeignKey(Atividade, models.DO_NOTHING, db_column='ID_Atividade') 
    idDisciplinaofertada = models.ForeignKey('Disciplinaofertada', models.DO_NOTHING, db_column='ID_DisciplinaOfertada') 
    rotulo = models.CharField(max_length=150)
    status = models.CharField(max_length=20, blank=True, null=True)
    dtInicioRespostas = models.DateField(db_column='DtInicioRespostas', blank=True, null=True)  
    dtFimRespostas = models.DateField(db_column='DtFimRespostas', blank=True, null=True)  

    class Meta:
        managed = False
        db_table = 'AtividadeVinculada'

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