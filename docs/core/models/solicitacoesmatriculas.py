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