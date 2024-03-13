#Crie um arquivo chamado biblioteca.py e importe a classe Livro neste arquivo.
from exercicio_3 import Livro
#No arquivo biblioteca.py, empreste o livro chamando o método emprestar e imprima se o livro está disponível ou não após o empréstimo.
mochileiro=Livro('o guia do mochileiro das galaxias','douglas adans',1997)
print(mochileiro.emprestar)
#No arquivo biblioteca.py, utilize o método estático verificar_disponibilidade para obter a lista de livros disponíveis publicados em um ano específico.
Livro.verificar_disponibilidade(1997)
#Crie um arquivo chamado main.py, importe a classe Livro e, no arquivo main.py, instancie dois objetos da classe Livro e exiba a mensagem formatada utilizando o método str.
if __name__=='__main__':
    pass