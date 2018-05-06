#models.py
from django.db import models

from django.db import models

class Aluno(models.Model):
    idAluno = models.AutoField(db_column='ID_Aluno', primary_key=True) 
    login = models.CharField(unique=True, max_length=20, blank=True, null=True)
    senha = models.CharField(max_length=20)
    nome = models.CharField(max_length=30)
    email = models.CharField(unique=True, max_length=40)
    celular = models.CharField(unique=True, max_length=9, blank=True, null=True)
    foto = models.CharField(max_length=11, blank=True, null=True)
    dtExpiracao = models.DateField(db_column='DtExpiracao', blank=True, null=True)  
    Ra = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Aluno'


class Coordenador(models.Model):
    idCoordenador = models.AutoField(db_column='ID_Coordenador', primary_key=True) 
    login = models.CharField(unique=True, max_length=50, blank=True, null=True)
    senha = models.CharField(max_length=20)
    nome = models.CharField(max_length=30)
    email = models.CharField(unique=True, max_length=40)
    celular = models.CharField(unique=True, max_length=9, blank=True, null=True)
    dtExpiracao = models.DateField(db_column='DtExpiracao', blank=True, null=True) 

    class Meta:
        managed = False
        db_table = 'Coordenador'


class Professor(models.Model):
    idProfessor = models.AutoField(db_column='ID_Professor', primary_key=True)  
    login = models.CharField(unique=True, max_length=20, blank=True, null=True)
    senha = models.CharField(max_length=20)
    nome = models.CharField(max_length=30)
    email = models.CharField(unique=True, max_length=40)
    celular = models.CharField(unique=True, max_length=9, blank=True, null=True)
    dtExpiracao = models.DateField(db_column='DtExpiracao', blank=True, null=True) 
    apelido = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Professor'


class Mensagem(models.Model):
    idMensagem = models.AutoField(db_column='ID_Mensagem', primary_key=True) 
    idAluno = models.ForeignKey(Aluno, models.DO_NOTHING, db_column='ID_Aluno')  
    idProfessor = models.ForeignKey('Professor', models.DO_NOTHING, db_column='ID_Professor') 
    assunto = models.CharField(max_length=999, blank=True, null=True)
    referencia = models.CharField(max_length=999, blank=True, null=True)
    conteudo = models.CharField(max_length=999, blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)
    dtEnvio = models.DateField(db_column='DtEnvio', blank=True, null=True)  
    dtResposta = models.DateField(db_column='DtResposta') 
    resposta = models.CharField(max_length=999, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Mensagem'

class Disciplina(models.Model):
    idDisciplina = models.AutoField(db_column='ID_Disciplina', primary_key=True)  
    nome = models.CharField(unique=True, max_length=30, blank=True, null=True)
    data = models.DateField(blank=True, null=True)
    status = models.CharField(db_column='Status', max_length=20, blank=True, null=True)  
    planoDeEnsino = models.CharField(db_column='PlanodeEnsino', max_length=999, blank=True, null=True) 
    cargaHoraria = models.IntegerField(db_column='Cargahoraria', blank=True, null=True)  
    competencias = models.CharField(max_length=999, blank=True, null=True)
    habilidades = models.CharField(max_length=999, blank=True, null=True)
    ementa = models.CharField(max_length=999, blank=True, null=True)
    conteudoProgramatico = models.CharField(db_column='ConteudoProgramatico', max_length=999, blank=True, null=True) 
    bibliografiaBasica = models.CharField(db_column='BibliografiaBasica', max_length=999, blank=True, null=True)  
    bibliografiaComplementar = models.CharField(db_column='BibliografiaComplementar', max_length=999, blank=True, null=True) 
    percentualPratico = models.IntegerField(db_column='PercentualPratico', blank=True, null=True) 
    percentualTeorico = models.IntegerField(db_column='PercentualTeorico', blank=True, null=True)  
    idCoordenador = models.ForeignKey(Coordenador, models.DO_NOTHING, db_column='ID_Coordenador')  
    
    class Meta:
        managed = False
        db_table = 'Disciplina'

class Curso(models.Model):
    idCurso = models.AutoField(db_column='ID_Curso', primary_key=True)  
    nome = models.CharField(unique=True, max_length=30)

    class Meta:
        managed = False
        db_table = 'Curso'

class Disciplinaofertada(models.Model):
    idDisciplinaofertada = models.AutoField(db_column='ID_DisciplinaOfertada', primary_key=True)  
    idCoordenador = models.ForeignKey(Coordenador, models.DO_NOTHING, db_column='ID_Coordenador')  
    dtInicioMatricula = models.DateField(db_column='DtInicioMatricula', blank=True, null=True)  
    dtFimMatricula = models.DateField(db_column='DtFimMatricula', blank=True, null=True) 
    idDisciplina = models.ForeignKey(Disciplina, models.DO_NOTHING, db_column='ID_Disciplina')  
    idCurso = models.ForeignKey(Curso, models.DO_NOTHING, db_column='ID_Curso')  
    ano = models.IntegerField()
    semestre = models.IntegerField()
    turma = models.CharField(max_length=6, blank=True, null=True)
    idProfessor = models.ForeignKey(Professor, models.DO_NOTHING, db_column='ID_Professor', blank=True, null=True) 
    metodologia = models.CharField(max_length=999, blank=True, null=True)
    recursos = models.CharField(max_length=999, blank=True, null=True)
    criterioAvaliacao = models.CharField(db_column='CriterioAvaliacao', max_length=999, blank=True, null=True) 
    planoDeAulas = models.CharField(db_column='PlanoDeAulas', max_length=999, blank=True, null=True) 

    class Meta:
        managed = False
        db_table = 'Disciplinaofertada'


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
