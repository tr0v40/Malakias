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