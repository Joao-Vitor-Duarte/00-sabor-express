# Crie uma classe chamada Veiculo com um método abstrato chamado ligar.
from abc import abstractclassmethod,ABC
class Veiculo(ABC):
    @abstractclassmethod
    def ligar():
        pass
# No mesmo arquivo, crie um construtor para a classe Veiculo que aceita os parâmetros marca e modelo.
    def __init__(self,marca,modelo):
        self.marca=marca
        self.modelo=modelo
# Crie uma nova classe chamada Carro que herda da classe Veiculo.
class Carro(Veiculo):
# No construtor da classe Carro, utilize o método super() para chamar o construtor da classe pai e atribua o atributo específico cor à classe filha.
    def __init__(self, marca, modelo,cor):
        super().__init__(marca, modelo)
        self.cor=cor
    def ligar():
        pass
# Em um arquivo chamado main.py, importe a classe Carro.
    # from exercicios.exexcicio_polimorfismo import Carro
# No arquivo main.py, instancie três objetos da classe Carro com diferentes características, como marca, modelo e cor.
carro1=Carro('fiat','uno','branco')
carro2=Carro('fiat','palio','cinza')
carro3=Carro('fiat','classic','preto')
print(f"Carro 1: {carro1.marca} {carro1.modelo}, Cor: {carro1.cor}")
print(f"Carro 2: {carro2.marca} {carro2.modelo}, Cor: {carro2.cor}")
print(f"Carro 3: {carro3.marca} {carro3.modelo}, Cor: {carro3.cor}")
