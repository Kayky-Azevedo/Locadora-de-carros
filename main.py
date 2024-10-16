import streamlit as st
import json
import hashlib

# Funções para carregar e salvar dados em JSON
def carregar_dados():
    try:
        with open('locadora_dados.json', 'r') as f:
            dados = json.load(f)
            if "usuarios" not in dados or not isinstance(dados["usuarios"], dict):
                dados["usuarios"] = {}
            return dados
    except FileNotFoundError:
        return {"veiculos": [], "clientes": [], "alugueis": {}, "usuarios": {}}

def salvar_dados(dados):
    with open('locadora_dados.json', 'w') as f:
        json.dump(dados, f, indent=4)

dados = carregar_dados()

# Função para hash da senha (mesmo que não seja usada, mantemos aqui para futuros ajustes)
def verificar_login(username, cpf):
    # Login padrão para o administrador
    if username == "admin" and cpf == "admin123":
        return True
    if username in dados["usuarios"]:
        if dados["usuarios"][username]["cpf"] == cpf:
            return True  # Usuário normal logando com CPF
    return False

# Função para exibir a tela de login
def tela_login():
    st.title("Login")
    username = st.text_input("Usuário")
    cpf = st.text_input("CPF")

    if st.button("Entrar"):
        if verificar_login(username, cpf):
            st.session_state.logado = True
            st.session_state.usuario_atual = username
            st.session_state.tela = "principal"
            st.success("Login realizado com sucesso!")
            st.rerun()  # Simular rerun
        else:
            st.error("Usuário ou CPF inválidos!")

    if st.button("Cadastre-se"):
        st.session_state.tela = "cadastro"
        st.rerun()

# Função para exibir a tela de cadastro (disponível para todos os usuários)
def tela_cadastro():
    st.title("Cadastro de Usuário")
    nome_usuario = st.text_input("Nome do Usuário")
    cpf_usuario = st.text_input("CPF")

    if st.button("Cadastrar"):
        if nome_usuario and cpf_usuario:
            if nome_usuario not in dados["usuarios"]:
                dados["usuarios"][nome_usuario] = {
                    "nome": nome_usuario,
                    "cpf": cpf_usuario,
                }
                salvar_dados(dados)
                st.success("Usuário cadastrado com sucesso!")
                st.session_state.tela = "login"
                st.rerun()
            else:
                st.error("Usuário já existe!")
        else:
            st.error("Preencha todos os campos!")

    if st.button("Voltar para Login"):
        st.session_state.tela = "login"
        st.rerun()

# Função para exibir o sistema de locação
def sistema_locacao():
    st.sidebar.write(f"Bem-vindo, {st.session_state.usuario_atual}!")
    if st.sidebar.button("Sair"):
        st.session_state.logado = False
        st.session_state.tela = "login"
        st.rerun()

    st.title("Locadora de Veículos")

    # Funções exclusivas para o administrador
    if st.session_state.usuario_atual == "admin":
        # Aba para cadastrar veículos
        st.sidebar.header("Cadastrar Veículo")
        marca = st.sidebar.text_input("Marca")
        modelo = st.sidebar.text_input("Modelo")
        ano = st.sidebar.number_input("Ano", min_value=1900, max_value=2024, step=1)
        placa = st.sidebar.text_input("Placa")

        if st.sidebar.button("Cadastrar Veículo"):
            if marca and modelo and placa:
                novo_veiculo = {
                    "marca": marca,
                    "modelo": modelo,
                    "ano": ano,
                    "placa": placa,
                    "disponivel": True
                }
                dados['veiculos'].append(novo_veiculo)
                salvar_dados(dados)
                st.sidebar.success("Veículo cadastrado com sucesso!")
                # Limpar os campos de entrada
                marca = ""
                modelo = ""
                ano = 1900
                placa = ""
                st.rerun()
            else:
                st.sidebar.error("Preencha todos os campos!")
            st.rerun()

        st.sidebar.header("Modificar Veículo")
        veiculo_para_modificar = st.sidebar.selectbox("Escolha o veículo", [v['placa'] for v in dados['veiculos']])

        if veiculo_para_modificar:
            with st.sidebar.expander("Editar Veículo", expanded=False):
                veiculo = next(v for v in dados['veiculos'] if v['placa'] == veiculo_para_modificar)

                nova_marca = st.text_input("Nova Marca", value=veiculo['marca'], key=f"nova_marca_{veiculo_para_modificar}")
                novo_modelo = st.text_input("Novo Modelo", value=veiculo['modelo'], key=f"novo_modelo_{veiculo_para_modificar}")
                novo_ano = st.number_input("Novo Ano", min_value=1900, max_value=2024, step=1, value=veiculo['ano'], key=f"novo_ano_{veiculo_para_modificar}")
                nova_placa = st.text_input("Nova Placa", value=veiculo['placa'], key=f"nova_placa_{veiculo_para_modificar}")

                if st.button("Salvar", key=f"salvar_veiculo_{veiculo_para_modificar}"):
                    veiculo['marca'] = nova_marca
                    veiculo['modelo'] = novo_modelo
                    veiculo['ano'] = novo_ano
                    veiculo['placa'] = nova_placa
                    salvar_dados(dados)
                    st.success("Veículo modificado com sucesso!")

        # Deletar veículo
        if st.sidebar.button("Deletar Veículo"):
            dados['veiculos'] = [v for v in dados['veiculos'] if v['placa'] != veiculo_para_modificar]
            salvar_dados(dados)
            st.sidebar.success("Veículo deletado com sucesso!")
            st.rerun()

        # Aba para cadastrar usuários
        st.sidebar.header("Cadastrar Usuário")
        nome_usuario = st.sidebar.text_input("Nome do Usuário")
        cpf_usuario = st.sidebar.text_input("CPF")

        if st.sidebar.button("Cadastrar Usuário"):
            if nome_usuario and cpf_usuario:
                if nome_usuario not in dados["usuarios"]:
                    dados["usuarios"][nome_usuario] = {
                        "nome": nome_usuario,
                        "cpf": cpf_usuario,
                    }
                    salvar_dados(dados)
                    st.sidebar.success("Usuário cadastrado com sucesso!")
                    nome_usuario = ""
                    cpf_usuario = ""
                    st.rerun()
                else:
                    st.sidebar.error("Usuário já existe!")
                    nome_usuario = ""
                    cpf_usuario = ""
            else:
                st.sidebar.error("Preencha todos os campos!")

    # Exibir veículos e clientes
    st.header("Veículos Disponíveis")
    veiculos_disponiveis = [v for v in dados['veiculos'] if v['disponivel']]
    st.table(veiculos_disponiveis)

    st.header("Usuários Cadastrados")
    usuarios_cadastrados = [{"Nome": usuario, "CPF": dados["usuarios"][usuario]["cpf"]} for usuario in dados["usuarios"]]
    st.table(usuarios_cadastrados)

    # Funções de aluguel e devolução de veículos disponíveis para todos os usuários
    st.header("Alugar Veículo")
    placa_alugar = st.selectbox("Escolha o veículo pela placa", [v['placa'] for v in dados['veiculos'] if v['disponivel']])
    usuario_alugar = st.selectbox("Escolha o usuário", list(dados['usuarios'].keys()))

    if st.button("Alugar Veículo"):
        for veiculo in dados['veiculos']:
            if veiculo['placa'] == placa_alugar:
                veiculo['disponivel'] = False
                dados['alugueis'][placa_alugar] = usuario_alugar
                salvar_dados(dados)
                st.success(f"Veículo {placa_alugar} alugado para o usuário {usuario_alugar}")
                break
        st.rerun()

    st.header("Devolver Veículo")
    placa_devolver = st.selectbox("Escolha o veículo a ser devolvido", [v['placa'] for v in dados['veiculos'] if not v['disponivel']])

    if st.button("Devolver Veículo"):
        for veiculo in dados['veiculos']:
            if veiculo['placa'] == placa_devolver:
                veiculo['disponivel'] = True
                del dados['alugueis'][placa_devolver]
                salvar_dados(dados)
                st.success(f"Veículo {placa_devolver} devolvido com sucesso!")
                break
        st.rerun()

    st.header("Veículos Alugados")
    veiculos_alugados = [v for v in dados['veiculos'] if not v['disponivel']]
    st.table(veiculos_alugados)

# Lógica para alternar entre as telas
if "tela" not in st.session_state:
    st.session_state.tela = "login"
if "logado" not in st.session_state:
    st.session_state.logado = False

if st.session_state.tela == "login":
    tela_login()
elif st.session_state.tela == "cadastro":
    tela_cadastro()
elif st.session_state.tela == "principal" and st.session_state.logado:
    sistema_locacao()
