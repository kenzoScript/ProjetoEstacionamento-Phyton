class Carro:
    def __init__(self,placa, modelo, tipo):
        self.placa:str = placa
        self.modelo:str = modelo
        self.tipo:str = tipo

    def exibir_detalhes(self):
        print(f'placa{self.placa}, Carro: {self.modelo}, Tipo: {self.tipo}' )