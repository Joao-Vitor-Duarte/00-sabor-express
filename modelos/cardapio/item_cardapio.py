from abc import ABC,abstractstaticmethod
class ItemCardapio(ABC):
    def __init__(self,nome,preco):
        self._nome=nome
        self._preco=preco
    @abstractstaticmethod
    def aplicar_desconto():
        pass
        