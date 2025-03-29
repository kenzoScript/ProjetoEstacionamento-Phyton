from estacionamento import Estacionamento
from carro import Carro

Lamborghini = Carro(modelo='Lamborghini', placa='LAM0B70' , tipo='Sedan')

Ferrari = Carro(modelo= 'Ferrari FF' , placa= 'FER1R29' , tipo='Hatch')

McLaren = Carro(modelo= 'McLaren' , placa= 'MCL3A34' , tipo='Sedan')



vagas = Estacionamento()

print(f' Esta vazio: {vagas.esta_vazio()}')

vagas.estacionar(Ferrari)
vagas.estacionar(Lamborghini)
vagas.estacionar(McLaren)

print(f'Esta vazio:{vagas.esta_vazio()}')

print(f'Qtde carros estacionados: {vagas.verificar_carros_estacionados()}')

vagas.valor_receber()

vagas.carros_saida()

vagas.verificar_carro_frente()

vagas.mostrar_carros_estacionados()

vagas.valor_receber()