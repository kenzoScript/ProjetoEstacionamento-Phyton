from carro import Carro
from typing import List
import string

class Estacionamento:
    def __init__(self):
        self.vagas: List[Carro] = []

    def esta_vazio(self):
        if len(self.vagas) == 0:
            return True
        else:
            return False

    def estacionar(self, veiculo):
        self.vagas.append(veiculo)

    def verificar_carros_estacionados(self):
        qtde_carros = len(self.vagas)
        return qtde_carros

    def carros_saida(self):
        if self.esta_vazio():
            print('\n Sem carros no estacionamento')

        else:
            carro=self.vagas.pop(0)
            print('----------------------')
            print(f'\n O carro que vai sair do estacionamento é')
            carro.exibir_detalhes()

    def verificar_carro_frente(self):
        if self.esta_vazio():
            print('\n Sem carros estacionados')

        else:
            carro_frente = self.vagas[0]
            print('\n O carro qure esta na frente da fila é')
            carro_frente.exibir_detalhes()

    def mostrar_carros_estacionados(self):
        print('\n Os carros que estao estacionados sao')
        for carro in self.vagas:
            carro.exibir_detalhes()

    def valor_receber(self):
        valorGanho = 0.0
        for carro in(self.vagas):
            tipo = carro.tipo
            if tipo == "Hatch":
                valorGanho +=5

            elif tipo == "Sedan":
                valorGanho +=8

            elif tipo == "Caminhonete":
                valorGanho +=12

        print(f'O valor a receber é de R$ {valorGanho}')