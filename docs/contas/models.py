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

    def __str__(self):
        return self.nome

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

    def __str__(self):
        return self.nome



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

    def __str__(self):
        return self.nome


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

    def __str__(self):
        pass
