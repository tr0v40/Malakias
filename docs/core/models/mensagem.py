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