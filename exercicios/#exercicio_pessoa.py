class Pessoa:
    def __init__(self,nome='',idade=0,profissao=''):
        self._nome=nome.title()
        self._idade=idade
        self._profissao=profissao.title()
    def __str__(self):
        return print(f'{self._nome} tem {self._idade} anos e é {self._profissao}')
    def aniversario(self):
        self._idade+=1