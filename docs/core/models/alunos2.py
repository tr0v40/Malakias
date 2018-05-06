import Pessoa

class Aluno(Pessoa):

    def adddisciplina(self, disciplina):
        self.__disciplinas.append(disciplina)

    def aumentadesconto(self,porcentagem):
        self.__desconto+=porcentagem

    def diminuidesconto(self,porcentagem):
        self.__desconto-=porcentagem

    def retornaSobrenome(self):
        return ' '.join(self.__nome.split(' ')[1:])


    def retornacargahoraria(self):
        cargahorariatotal = 0
        for a in self.__disciplinas:
            cargahorariatotal+=a.getcargahoraria()
        return cargahorariatotal


    def retornaValorMensalidade(self):
        valor=  0
        for v in self.__disciplinas:
            valor += v.getmensalidade()
        return  valor