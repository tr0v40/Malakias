class Professor:

    def __init__(self, nome='', email='', ra='',
        celular=''):
        self.__nome = nome
        self.__email = email
        self.__ra = ra
        self.__celular = celular
        self.__disciplinas = []

    
def adddisciplina(self, disciplina):
    if disciplina.getprofessor().getra() == self.__ra:
        self.__disciplinas.append(disciplina)
    else:
        return "Professor nao associado a disciplina"

def retornacargahoraria(self):
    soma_carga = 0
    for d in self.__disciplinas:
        soma_carga += d.getcargahoraria()/20
    return soma_carga