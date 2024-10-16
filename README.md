
# Locadora de Veículos

Este é um projeto simples de uma aplicação web para gerenciar uma locadora de veículos, permitindo o cadastro e a locação de veículos, bem como a administração de clientes e aluguéis. A interface foi construída usando o framework **Streamlit** e os dados são armazenados em um arquivo JSON.

## Funcionalidades

- **Sistema de Login e Cadastro:**
  - Os usuários podem criar uma conta, fazer login e acessar o sistema.
  - As senhas são armazenadas usando hashing SHA-256 para segurança.

- **Gestão de Veículos:**
  - Cadastro, modificação e exclusão de veículos.
  - Exibição de veículos disponíveis para aluguel.
  
- **Gestão de Aluguéis:**
  - Aluguel de veículos por clientes cadastrados.
  - Devolução de veículos.
  - Exibição de veículos alugados.

- **Gestão de Usuários:**
  - Cadastro de novos usuários com CPF.
  - Exibição de usuários cadastrados.

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
   git clone https://github.com/seu-usuario/locadora-veiculos.git
   cd locadora-veiculos
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

## Estrutura do Projeto

- **locadora_dados.json**: Armazena os dados da locadora, incluindo veículos, usuários e aluguéis.
- **locadora_veiculos.py**: Código principal da aplicação, responsável pelas interfaces de login, cadastro e gerenciamento de veículos e aluguéis.

## Como Usar

1. Ao iniciar a aplicação, você será direcionado para a tela de login.
2. Caso não tenha uma conta, clique em "Ir para Cadastro" para criar uma nova.
3. Após o login, você terá acesso ao sistema de locação, onde poderá cadastrar veículos, alugar, devolver e gerenciar os veículos disponíveis.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para fazer um fork deste repositório e enviar um pull request com suas melhorias.
