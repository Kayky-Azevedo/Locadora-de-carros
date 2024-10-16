
# Locadora de Veículos

Este é um projeto simples de uma aplicação web para gerenciar uma locadora de veículos, permitindo o cadastro e a locação de veículos, bem como a administração de clientes e aluguéis. A interface foi construída usando o framework **Streamlit** e os dados são armazenados em um arquivo JSON.

## Funcionalidades

  - **Login e Cadastro**: Usuários podem se cadastrar e fazer login utilizando nome de usuário e CPF.
  - **Gestão de Veículos**: Administradores podem cadastrar, modificar e deletar veículos.
  - **Aluguel e Devolução**: Usuários podem alugar e devolver veículos disponíveis.
  - **Exibição de Dados**: Exibe tabelas com veículos disponíveis e usuários cadastrados.
  - **Persistência de Dados**: Os dados são salvos em um arquivo JSON (`locadora_dados.json`), permitindo a persistência entre as sessões.

## Requisitos

Para rodar a aplicação, você precisará ter os seguintes itens instalados:

- Python 3.8 ou superior
- Bibliotecas Python:
  - Streamlit
  - json (nativo no Python)
  - hashlib (nativo no Python)

## Instalação

1. Clone este repositório para o seu ambiente local:

   ```bash
   git clone https://github.com/Kayky-Azevedo/Locadora-de-carros.git
   cd Locadora-de-carros
   ```

2. Crie um ambiente virtual (opcional, mas recomendado):

   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows, use: venv\Scripts\activate
   ```

3. Instale as dependências necessárias:

   ```bash
   pip install streamlit
   ```

4. Inicie a aplicação:

   ```bash
   streamlit run locadora_veiculos.py
   ```
## Estrutura do Código
  O código é organizado da seguinte forma:

  - `carregar_dados()`: Carrega dados de um arquivo JSON. Se o arquivo não existir, inicializa com dados padrão.
  - `salvar_dados(dados)`: Salva os dados no arquivo JSON.
  - `verificar_login(username, cpf)`: Verifica se o usuário e CPF estão corretos.
  - `tela_login()`: Interface de login para usuários.
  - `tela_cadastro()`: Interface para cadastro de novos usuários.
  - `sistema_locacao()`: Sistema principal que gerencia a locação de veículos, disponível para usuários logados.

## Estrutura do Arquivo JSON
 - O arquivo locadora_dados.json contém as seguintes estruturas de dados:
 ```
 {
    "veiculos": [
        {
            "marca": "Marca do Veículo",
            "modelo": "Modelo do Veículo",
            "ano": 2023,
            "placa": "ABC-1234",
            "disponivel": true
        }
    ],
    "clientes": [],
    "alugueis": {
        "ABC-1234": "Nome do Usuário"
    },
    "usuarios": {
        "Nome do Usuário": {
            "nome": "Nome Completo",
            "cpf": "CPF do Usuário"
        }
    }
  }
  ```

## Estrutura do Projeto

- **locadora_dados.json**: Armazena os dados da locadora, incluindo veículos, usuários e aluguéis.
- **main.py**: Código principal da aplicação, responsável pelas interfaces de login, cadastro e gerenciamento de veículos e aluguéis.

## Como Usar

1. Ao iniciar a aplicação, você será direcionado para a tela de login.
2. Caso não tenha uma conta, clique em "Ir para Cadastro" para criar uma nova.
3. Após o login, você terá acesso ao sistema de locação, onde poderá alugar e devolver o veiculo.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para fazer um fork deste repositório e enviar um pull request com suas melhorias.
