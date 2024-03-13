from typing import Any
from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio
class Restaurante:
    restaurantes = []
    def __init__(self,nome,categoria):    
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        Restaurante.restaurantes.append(self)
        self._avaliacoes=[]
        self._cardapio=[]
    def __str__(self):
        return f'{self._nome} | {self._categoria}'
    @property 
    def ativo(self):
            return "✔️" if self._ativo==True else "❌"
    def alterar_estado(self):
         self._ativo = not self._ativo
    @property
    def media_restaurante(self):
         if not self._avaliacoes:
            return 0
         else:
              soma = sum(avaliacao._nota for avaliacao in self._avaliacoes)
              quantidade = len(self._avaliacoes)
              media = round(soma/quantidade,1)
              return media
    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do Restaurante'.ljust(20)}|{'Categoria'.ljust(20)}|{'Avaliação'.ljust(20)}|{'Status'.ljust(20)}')
        for restaurante in cls.restaurantes:
            if restaurante.media_restaurante:
                print(f'{restaurante._nome.ljust(20)}|{restaurante._categoria.ljust(20)}|{str(restaurante.media_restaurante).ljust(20)}|{restaurante.ativo.ljust(20)}')  
            else:
                print(f'{restaurante._nome.ljust(20)}|{restaurante._categoria.ljust(20)}|{('Sem Avaliações').ljust(20)}|{restaurante.ativo.ljust(20)}')  
    def set_avaliacao(self,nome,nota):
         if nota>0 and nota<6:
            avaliacao=Avaliacao(nome,nota)
            self._avaliacoes.append(avaliacao)
    def get_avaliacoes(self):
         for avaliacao in self._avaliacoes:
              print(f'{avaliacao._nome} avaliou nota {avaliacao._nota}')
    def adicionar_item_no_cardapio(self,item):
         if isinstance(item,ItemCardapio):
              self._cardapio.append(item)
    @property
    def exibir_cardapio(self):
         for i,item in enumerate(self._cardapio,start=1):
              if hasattr(item,'_descricao'):
                   print(f'{i} - {item._nome.ljust(20)}|R$ {str(item._preco).ljust(20)}|{item._descricao.ljust(20)}')
              elif hasattr(item,'_tamanho'):
                   print(f'{i} - {item._nome.ljust(20)}|R$ {str(item._preco).ljust(20)}|{item._tamanho.ljust(20)}')