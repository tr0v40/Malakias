from django.db import models
from .pessoa import Pessoa

class Coordenador(Pessoa):
    idcoordenador = models.AutoField(db_column='idCoordenador', primary_key=True)  
    
    class Meta:
        managed = False
        db_table = 'coordenador'

    def __str__(self):
        return self.nome
