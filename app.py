from modelos.restaurante import Restaurante
from modelos.cardapio.prato import Prato
from modelos.cardapio.bebida import Bebida
pizzaria = Restaurante('cabana das pizzas','Pizza')
pizzaria.alterar_estado()
def main():
    Restaurante.listar_restaurantes()
if  __name__== '__main__':
    main()
print()
prato=Prato('file a milanesa',40.00,'file a moda da casa')
bebida=Bebida('suco de caju',6.00,'médio')
pizzaria.adicionar_item_no_cardapio(prato)
pizzaria.adicionar_item_no_cardapio(bebida)
bebida.aplicar_desconto()
prato.aplicar_desconto()
pizzaria.exibir_cardapio