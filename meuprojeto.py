"""
Modulo que contem a classe Entrevista.
Esta classe sera usada para instanciar e guardar cada Entrevista
feita pelo programa mais as entrevistas guardadas em disco
Os dados dessa instancias serao usados para fazer as estatisticas

"""

import datetime


class Entrevista():
    """ Classe Entrevista """

    def __init__(self, nome="", ano=0, idade=0):
        """
        Entrar com os valores iniciais. Variaveis de sistemas
        nome = Nome informado pelo entrevistado
        ano = Ano informado pelo entrevistado
        idade = Idade calculada do entrevistado
        """
        super(Entrevista, self).__init__()
        self.nome = nome
        self.idade = idade
        self.ano_informado = ano

    def pergunta_nome(self):
        """ Pergunta o nome do entrevistado. Retorna uma string """

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
        """
        Pergunta o ano de nascimento e calcula a idade.
        Perunta o ano de nascimento e valida o valor entre 1900
        e o ano atual, calculado atraves datetime.date.today().year
        Se validado calcula a idade.
        """
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

    def __str__(self):
        """Retorna uma descriçao amigavel do obj"""
        return "{}/{}".format(self.nome, self.idade)

    def __repr__(self):
        """Retorna uma descriçao unica e precisa do obj"""
        return "input()={} input()=int({})".format(self.nome, self.idade)
