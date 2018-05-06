from django.db import models

class Pessoa(models.model):
    nome = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    celular = models.CharField(max_length=9)
    login = models.CharField(max_length=15)
    senha = models.CharField(max_length=15)
    data_expiracao = models.DateField(default=timezone.now)

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


