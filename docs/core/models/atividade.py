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