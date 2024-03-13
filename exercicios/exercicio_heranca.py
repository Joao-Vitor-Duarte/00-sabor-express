#Crie uma Classe Pai (Veiculo): Implemente uma classe chamada Veiculo com um construtor que aceita dois parâmetros, marca e modelo. A classe deve ter um atributo protegido _ligado inicializado como False por padrão.
class Veiculo():
    def __init__(self,marca,modelo):
        self._marca=marca
        self._modelo=modelo
        self._ligado=False
    @property
    def ligado(self):
        return 'ligado' if self._ligado else 'desligado'
#Construa o Método Especial str: Adicione um método especial str à classe Veiculo que retorna uma mensagem formatada com a marca, modelo e o estado de ligado/desligado do veículo.
    def __str__(self) -> str:
        return f'Veiculo da marca {self._marca}, modelo {self._modelo} está {self.ligado}'
#Crie uma Classe Filha (Carro): Agora, crie uma classe chamada Carro que herda da classe Veiculo. No construtor da classe Carro, inclua um novo atributo chamado portas que indica a quantidade de portas do carro.
class Carro(Veiculo):
    def __init__(self,marca,modelo,portas):
        super().__init__(marca,modelo)
        self._portas=portas
#Implemente o Método Especial str na Classe Filha: Adicione um método especial str à classe Carro que estenda o método da classe pai (Veiculo) e inclua a informação sobre a quantidade de portas do carro.
    def __str__(self):
        return super().__str__()+f' e tem {self._portas} portas'
#Crie uma Classe Filha (Moto): Similarmente, crie uma classe chamada Moto que também herda de Veiculo. Adicione um novo atributo chamado tipo ao construtor, indicando se a moto é esportiva ou casual.
class Moto(Veiculo):
    def __init__(self, marca, modelo,tipo):
        super().__init__(marca, modelo)
        self._tipo=tipo
#Implemente o Método Especial str na Classe Filha (Moto): Adicione um método especial str à classe Moto que estenda o método da classe pai (Veiculo) e inclua a informação sobre o tipo da moto.
    def __str__(self):
        return super().__str__()+f' e é uma moto {self._tipo}'
#Crie um Arquivo Main (main.py): Crie um arquivo chamado main.py no mesmo diretório que suas classes.
#Importe e Instancie Objetos: No arquivo main.py, importe as classes Carro e Moto. Em seguida, crie três instâncias de Carro e Moto com diferentes marcas, modelos, quantidade de portas e tipos.
    #from exercicios.exercicio_heranca import Carro
    #from exercicios.exercicio_heranca import Moto
#Exiba as Informações: Para cada instância, imprima no console as informações utilizando o método str.
carro=Carro('fiat','uno',2)
moto=Moto('suzuki','cinquentinha','casual')
print(carro.__str__())
print(moto.__str__())