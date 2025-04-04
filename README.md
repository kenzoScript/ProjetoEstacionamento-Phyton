## 🚗 Projeto Estacionamento - Python 🅿️
Este é um projeto simples de gerenciamento de estacionamento desenvolvido em Python. O sistema permite controlar a entrada e saída de veículos em um estacionamento, registrando informações como placa, modelo e horário de entrada/saída. O sistema simula um ambiente de estacionamento onde você pode registrar veículos e verificar a disponibilidade de vagas.


# Funcionalidades ⚙️
Cadastro de Carros: O sistema permite o registro dos carros no estacionamento com informações como a placa e o modelo. 🚘

Entrada e Saída: O sistema registra a hora de entrada e de saída dos veículos e calcula o tempo de permanência. ⏳

Controle de Vagas: O sistema controla as vagas disponíveis no estacionamento, garantindo que o número de veículos não ultrapasse o limite de vagas. 🅿️

Relatórios: O sistema pode gerar um simples relatório com a lista de carros atualmente estacionados. 


# Estrutura do Projeto 🗂️ 
carro.py: Contém a classe Carro, que representa um veículo, com atributos como placa, modelo e horários de entrada e saída. 🚗

estacionamento.py: Contém a classe Estacionamento, que gerencia as operações do estacionamento, como adicionar veículos, registrar saída e controlar vagas. 🏢

main.py: Arquivo principal que executa o sistema, permitindo a interação com o usuário. 🖥️


## Passos para Executar 🚀
# Clone o repositório:
git clone https://github.com/kenzoScript/ProjetoEstacionamento-Phyton.git

# Acesse o diretório do projeto:
cd ProjetoEstacionamento-Phyton

# Execute o programa: No diretório do projeto, execute o script main.py para iniciar o sistema de gerenciamento de estacionamento:
python main.py


## Exemplo de Interação 📝
O sistema solicitará as informações sobre o carro, como a placa e o modelo, e também pedirá para você informar a ação desejada (entrada ou saída do estacionamento).

## Exemplo de Execução 🏁
1. Cadastro de um Carro:
Quando um carro entra no estacionamento, o usuário fornece os detalhes do veículo (placa e modelo). O sistema registra a hora de entrada e confirma se há vagas disponíveis. 🚘➡️🅿️

2. Saída de um Carro:
Quando o carro sai, o sistema calcula o tempo que o carro permaneceu no estacionamento e remove o carro da lista de estacionados. 🅿️➡️🚘

3. Relatório de Carros Estacionados:
O sistema pode gerar um relatório simples com a lista de carros que estão atualmente no estacionamento, incluindo a hora de entrada. 📑
