from django.db import models
import disciplinas


class Aluno(models.Model):
  ID_Aluno =  models.AutoField(db_column='ID_Aluno', primary_key=True) 
  Login = models.CharField(unique=True, max_length=20, blank=True, null=True)
  Senha = models.CharField(max_length=15)
  Nome = models.CharField(max_length=40) 
  Email = models.CharField(unique=True, max_length=30)
  Celular = models.CharField(unique=True, max_length=9, blank=True, null=True)
  DtExpiracao = models.DateField(db_column='DtExpiracao', blank=True, null=True)
  RA = models.CharField(max_length=20, blank=True, null=True)
  class Meta:
        managed = False
        db_table = 'Aluno'


def __init__(self, nome='', email='', ra='',celular='',desconto=0.0):
    self.__nome = nome
    self.__email = email
    self.__ra = ra
    self.__celular = celular
    self.__desconto = desconto
    self.__disciplinas = []





def getra(self):
    return self.__ra

def setra(self,ra):
    self.__ra = ra


def getdesconto(self):
    return self.__desconto

def setdesconto(self,desconto):
    self.__desconto = desconto

def getdisciplina(self):
    return self.__disciplinas

def adddisciplina(self, disciplina):
    self.__disciplinas.append(disciplina)

def aumentadesconto(self,porcentagem):
    self.__desconto+=porcentagem

def diminuidesconto(self,porcentagem):
    self.__desconto-=porcentagem


def retornacargahoraria(self):
    cargahorariatotal = 0
    for a in self.__disciplinas:
        cargahorariatotal+=a.getcargahoraria()
    return cargahorariatotal


def retornaValorMensalidade(self):
        mensalidadetotal = 0
        for disciplina in self.__disciplinas:
            mensalidadetotal + = disciplina.getMensalidade()*(100-self.__desconto)/100
        return 
    

def retornaCargaHoraria(self):
      cargahorariatotal = 0
      for disciplinas in self.__disciplinas:
          cargahorariatotal + = disciplinas.getCargaHoraria()
      return cargahorariatotal