# Sistema de Locadora de Veículos 🚗

## Descrição
Sistema completo de gerenciamento para locadora de veículos desenvolvido em Python com Streamlit. O sistema oferece controle total das operações de uma locadora, incluindo gestão de veículos, clientes, locações e devoluções.

## Funcionalidades Principais

### 🔐 Sistema de Autenticação
- Login para usuários e administradores
- Cadastro de novos usuários
- Validação de credenciais
- Controle de sessão

### 👥 Gestão de Usuários
- Cadastro completo de clientes com:
  - Dados pessoais (nome, CPF)
  - Informações de contato (telefone, email)
  - Endereço completo (rua, número, cidade, estado)
- Visualização de usuários cadastrados (acesso administrativo)
- Separação entre clientes ativos e inativos

### 🚙 Gestão de Veículos
#### Funcionalidades Administrativas
- Cadastro detalhado de veículos
- Edição de informações dos veículos
- Exclusão de veículos do sistema
- Controle de:
  - Marca e modelo
  - Ano de fabricação
  - Placa
  - Categoria (econômico, intermediário, luxo)
  - Detalhes técnicos (cor, combustível, quilometragem)
  - Histórico de manutenções

### 📋 Sistema de Locação
- Visualização em tempo real de:
  - Veículos disponíveis
  - Veículos alugados
- Processo completo de aluguel:
  - Seleção de veículo por placa
  - Seleção de cliente
  - Definição de período (data início/devolução)
  - Configuração de valor da diária
- Sistema de devolução integrado

## Acesso ao Sistema

### Credenciais de Administrador
- Usuário: `admin`
- CPF: `admin123`

### Níveis de Acesso

#### Administrador
- Acesso total ao sistema
- Gerenciamento completo de veículos
- Visualização de todos os usuários
- Controle de locações e devoluções
- Acesso ao painel administrativo

#### Cliente
- Visualização da frota disponível
- Histórico pessoal de locações
- Atualização de dados cadastrais

## Estrutura de Dados (JSON)
O sistema utiliza um arquivo `locadora_dados.json` com a seguinte estrutura:

```json
{
    "locadora": {
        "frota": {
            "carros": {
                "disponiveis": [
                    {
                        "marca": "string",
                        "modelo": "string",
                        "ano": "number",
                        "placa": "string",
                        "categoria": "string",
                        "detalhes": {
                            "cor": "string",
                            "combustivel": "string",
                            "quilometragem": "number",
                            "manutencoes": []
                        }
                    }
                ],
                "alugados": [
                    {
                        "aluguel_atual": {
                            "cliente": "string",
                            "data_inicio": "date",
                            "data_prevista_devolucao": "date",
                            "valor_diaria": "number"
                        }
                    }
                ]
            }
        },
        "clientes": {
            "ativos": {
                "nome_usuario": {
                    "dados_pessoais": {
                        "nome_completo": "string",
                        "cpf": "string",
                        "contato": {
                            "telefone": "string",
                            "email": "string"
                        },
                        "endereco": {
                            "rua": "string",
                            "numero": "string",
                            "cidade": "string",
                            "estado": "string"
                        }
                    }
                }
            },
            "inativos": {}
        }
    }
}
```

## Requisitos e Instalação
### Requisitos
- Python 3.x
- Streamlit
- Biblioteca JSON

### Instalação
1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/locadora-veiculos.git
cd locadora-veiculos
```

2. Crie e ative um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Instale as dependências:
```bash
pip install streamlit
```

4. Execute a aplicação:
```bash
streamlit run main.py
```
