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
###
