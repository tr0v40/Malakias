from django.db import models


class Pessoa(models.Model):
    logon = models.CharField(unique=True, max_length=20, blank=True, null=True)
    senha = models.CharField(max_length=20)
    nome = models.CharField(max_length=30)
    email = models.CharField(unique=True, max_length=40)
    celular = models.CharField(unique=True, max_length=11, blank=True, null=True)
    dtexpiracao = models.DateField(db_column='dtExpiracao', blank=True, null=True)  # Field name made lowercase.
    
    class Meta:
        abstract = True

def getNome(self):
    return self.__nome

def setNome(self,nome):
    self.__nome = nome

def getEmail(self):
    return self.__email

def setEmail(self,email):
    self.__email = email

def retornaSobrenome(self):
    return ' '.join(self.__nome.split(' ')[1:])

def getCelular(self):
    return self.__celular

def setCelular(self,celular):
    self.__celular = celular

def retornaCargaHoraria():
    return "Método não implementado ! "