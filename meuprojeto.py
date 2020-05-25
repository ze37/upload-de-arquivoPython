import datetime


class Entrevista():

    def __init__(self, nome="", ano=0, idade=0):
        super(Entrevista, self).__init__()
        self.nome = nome
        self.idade = idade
        self.ano_informado = ano

    def pergunta_nome(self):
        nome_ok = False
        while nome_ok == False:
            self.nome = input("Qual é o se nome? (Digite 'parar para parar)")
            if self.nome:
                nome_ok = True
                if self.nome.lower() != 'parar':
                    print('O seu nome é ' + self.nome + '"')
        self.nome = self.nome.title()
        return self.nome

    def pergunta_idade(self, ano_atual=2020):
        ano_atual = datetime.date.today().year
        ano_ok = False
        while ano_ok == False:
            try:
                # Perguntar em que ano voce nasceu
                self.ano_informado = int(
                    input("Ei " + self.nome + ",Em que ano você nasceu?"))
                ano_ok = True
            except:
                continue
            else:
                if self.ano_informado >= 1900 and self.ano_informado <= ano_atual:
                    pass
                else:
                    ano_ok = False

        # subtrair o ano informado pelo ano atual
        self.idade = ano_atual - self.ano_informado
        # imprimir na tela a idade  calculada
        print(f'Você tem {self.idade} anos')
        # return (self.ano_informado, self.idade)  # tupla

    def __repr__(self):
        return "input()={} input()=int({})".format(self.nome, self.idade)
