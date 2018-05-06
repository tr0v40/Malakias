class Professor:

    def __init__(self, login, nome, email, celular, apelido):
        self.__login = login
        self.__nome = nome
        self.__email = email
        self.__celular = celular
        self.__apelido = apelido
        self.__disciplinas = []

    def addDisciplina(self, disciplina):
        if disciplina.getprofessor().getra() == self.__ra:
            self.__disciplinas.append(disciplina)
        else:
            return "Professor nao associado a disciplina"

    def getLogin(self):
        return self.__login

    def setLogin(self, novoLogin):
        self.__login = novoLogin

    def getNome(self):
        return self.__nome

    def setNome(self, novoNome):
        self.__nome = novoNome

    def getEmail(self):
        return self.__email

    def setEmail(self, novoEmail):
        self.__email = novoEmail

    def getRa(self):
        return self.__ra

    def setRa(self, novoRa):
        self.__ra = novoRa

    def getCelular(self):
        return self.__celular

    def setCelular(self, novoCelular):
        self.__celular = novoCelular

    def getApelido(self):
        return self.__apelido

    def setApelido(self, novoApelido):
        self.__apelido = novoApelido

    def getDisciplinas(self):
        return self.__disciplinas

    def retornaCargaHoraria(self):
        soma_carga = 0
        for d in self.__disciplinas:
            soma_carga += d.getcargahoraria()/20
        return soma_carga

    
