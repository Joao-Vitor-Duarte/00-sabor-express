#Crie uma classe chamada Livro com um construtor que aceita os parâmetros titulo, autor e ano_publicacao. Inicie um atributo chamado disponivel como True por padrão.
class Livro:
    lista_de_livros=[]
    def __init__(self,titulo,autor,ano):
        self._titulo=titulo.title()
        self._autor=autor.title()
        self._ano=ano
        self._disponivel=True
        Livro.lista_de_livros.append(self)
#Na classe Livro, adicione um método especial str que retorna uma mensagem formatada com o título, autor e ano de publicação do livro. 
    def __str__(self):
        return f'{self._titulo} do autor {self._autor} publicado em {self._ano}'
#Adicione um método de instância chamado emprestar à classe Livro que define o atributo disponivel como False. Crie uma instância da classe, chame o método emprestar e imprima se o livro está disponível ou não.
    @property
    def emprestar(self):
       if self._disponivel:
            self._disponivel = not self._disponivel 
            return 'o livro pode ser emprestado'
       else:
            return'o livro já foi emprestado'
#Adicione um método estático chamado verificar_disponibilidade à classe Livro que recebe um ano como parâmetro e retorna uma lista dos livros disponíveis publicados nesse ano.
    @classmethod
    def verificar_disponibilidade(cls,ano):
        lista_do_ano=[]
        for livro in cls.lista_de_livros:
            if livro._ano==ano:
                lista_do_ano.append(livro._titulo)
        if not lista_do_ano:
            print('não há livros desse ano')
        else:
            for livro in lista_do_ano:
                print(livro)
#Crie uma instância da classe Livro e imprima essa instância.
'''mochileiro=Livro('o guia do mochileiro das galaxias','douglas adans',1997)
print(mochileiro.__str__())
print(mochileiro.emprestar)
Livro.verificar_disponibilidade(1997)'''
