import streamlit as st
import json
import hashlib

# Funções para carregar e salvar dados em JSON
def carregar_dados():
    try:
        with open('locadora_dados.json', 'r') as f:
            dados = json.load(f)
            if "locadora" not in dados:
                dados = {
                    "locadora": {
                        "info": {
                            "nome": "Locadora de Veículos",
                            "cnpj": "12.345.678/0001-90",
                            "endereco": {
                                "rua": "Rua Principal",
                                "numero": "123",
                                "cidade": "São Paulo",
                                "estado": "SP"
                            }
                        },
                        "frota": {
                            "carros": {
                                "disponiveis": [],
                                "alugados": []
                            }
                        },
                        "clientes": {
                            "ativos": {},
                            "inativos": {}
                        },
                        "financeiro": {
                            "receitas": {},
                            "despesas": {}
                        }
                    }
                }
            return dados
    except FileNotFoundError:
        return {"locadora": {"frota": {"carros": {"disponiveis": [], "alugados": []}}, "clientes": {"ativos": {}, "inativos": {}}}}

def salvar_dados(dados):
    with open('locadora_dados.json', 'w') as f:
        json.dump(dados, f, indent=4)

dados = carregar_dados()

def verificar_login(username, cpf):
    if username == "admin" and cpf == "admin123":
        return True
    if username in dados["locadora"]["clientes"]["ativos"]:
        if dados["locadora"]["clientes"]["ativos"][username]["dados_pessoais"]["cpf"] == cpf:
            return True
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
            st.rerun()
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
    telefone = st.text_input("Telefone")
    email = st.text_input("Email")
    
    # Campos de endereço
    rua = st.text_input("Rua")
    numero = st.text_input("Número")
    cidade = st.text_input("Cidade")
    estado = st.text_input("Estado")

    if st.button("Cadastrar"):
        if nome_usuario and cpf_usuario:
            if nome_usuario not in dados["locadora"]["clientes"]["ativos"]:
                dados["locadora"]["clientes"]["ativos"][nome_usuario] = {
                    "dados_pessoais": {
                        "nome_completo": nome_usuario,
                        "cpf": cpf_usuario,
                        "contato": {
                            "telefone": telefone,
                            "email": email
                        },
                        "endereco": {
                            "rua": rua,
                            "numero": numero,
                            "cidade": cidade,
                            "estado": estado
                        }
                    }
                }
                salvar_dados(dados)
                st.success("Usuário cadastrado com sucesso!")
                st.session_state.tela = "login"
                st.rerun()
            else:
                st.error("Usuário já existe!")
        else:
            st.error("Preencha todos os campos obrigatórios!")

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
        cor = st.sidebar.text_input("Cor")
        combustivel = st.sidebar.selectbox("Combustível", ["flex", "gasolina", "diesel"])
        quilometragem = st.sidebar.number_input("Quilometragem", min_value=0)
        categoria = st.sidebar.selectbox("Categoria", ["economico", "intermediario", "luxo"])

        if st.sidebar.button("Cadastrar Veículo"):
            if marca and modelo and placa:
                novo_veiculo = {
                    "marca": marca,
                    "modelo": modelo,
                    "ano": ano,
                    "placa": placa,
                    "categoria": categoria,
                    "detalhes": {
                        "cor": cor,
                        "combustivel": combustivel,
                        "quilometragem": quilometragem,
                        "manutencoes": []
                    }
                }
                dados["locadora"]["frota"]["carros"]["disponiveis"].append(novo_veiculo)
                salvar_dados(dados)
                st.sidebar.success("Veículo cadastrado com sucesso!")
                st.rerun()

    # Exibir veículos disponíveis
    st.header("Veículos Disponíveis")
    veiculos_disponiveis = dados["locadora"]["frota"]["carros"]["disponiveis"]
    if veiculos_disponiveis:
        # Formatar os dados dos veículos para exibição
        veiculos_formatados = []
        for veiculo in veiculos_disponiveis:
            veiculos_formatados.append({
                "Marca": veiculo["marca"],
                "Modelo": veiculo["modelo"],
                "Ano": veiculo["ano"],
                "Placa": veiculo["placa"],
                "Categoria": veiculo["categoria"],
                "Cor": veiculo["detalhes"]["cor"],
                "Combustível": veiculo["detalhes"]["combustivel"],
                "Quilometragem": veiculo["detalhes"]["quilometragem"]
            })
        st.table(veiculos_formatados)

        # Opções de edição e exclusão para admin
        if st.session_state.usuario_atual == "admin":
            col1, col2 = st.columns(2)
            
            with col1:
                st.subheader("Editar Veículo")
                placa_editar = st.selectbox(
                    "Selecione o veículo para editar", 
                    [v['placa'] for v in veiculos_disponiveis],
                    key="select_editar"
                )
                if st.button("Editar"):
                    veiculo_editar = next((v for v in veiculos_disponiveis if v['placa'] == placa_editar), None)
                    if veiculo_editar:
                        st.session_state.veiculo_editando = veiculo_editar
                        st.session_state.editando = True
                        st.rerun()

            with col2:
                st.subheader("Excluir Veículo")
                placa_excluir = st.selectbox(
                    "Selecione o veículo para excluir", 
                    [v['placa'] for v in veiculos_disponiveis],
                    key="select_excluir"
                )
                if st.button("Excluir"):
                    veiculo_excluir = next((v for v in veiculos_disponiveis if v['placa'] == placa_excluir), None)
                    if veiculo_excluir:
                        dados["locadora"]["frota"]["carros"]["disponiveis"].remove(veiculo_excluir)
                        salvar_dados(dados)
                        st.success(f"Veículo {placa_excluir} excluído com sucesso!")
                        st.rerun()

            # Interface de edição
            if hasattr(st.session_state, 'editando') and st.session_state.editando:
                st.subheader("Editar Veículo")
                veiculo = st.session_state.veiculo_editando
                
                marca = st.text_input("Marca", value=veiculo["marca"], key="edit_marca")
                modelo = st.text_input("Modelo", value=veiculo["modelo"], key="edit_modelo")
                ano = st.number_input("Ano", min_value=1900, max_value=2024, value=veiculo["ano"], key="edit_ano")
                categoria = st.selectbox(
                    "Categoria", 
                    ["economico", "intermediario", "luxo"], 
                    index=["economico", "intermediario", "luxo"].index(veiculo["categoria"]),
                    key="edit_categoria"
                )
                cor = st.text_input("Cor", value=veiculo["detalhes"]["cor"], key="edit_cor")
                combustivel = st.selectbox(
                    "Combustível", 
                    ["flex", "gasolina", "diesel"],
                    index=["flex", "gasolina", "diesel"].index(veiculo["detalhes"]["combustivel"]),
                    key="edit_combustivel"
                )
                quilometragem = st.number_input(
                    "Quilometragem", 
                    min_value=0, 
                    value=veiculo["detalhes"]["quilometragem"],
                    key="edit_quilometragem"
                )

                col1, col2 = st.columns(2)
                with col1:
                    if st.button("Salvar Alterações"):
                        # Encontrar e atualizar o veículo
                        idx = next((i for i, v in enumerate(veiculos_disponiveis) 
                                  if v['placa'] == veiculo["placa"]), None)
                        if idx is not None:
                            dados["locadora"]["frota"]["carros"]["disponiveis"][idx].update({
                                "marca": marca,
                                "modelo": modelo,
                                "ano": ano,
                                "categoria": categoria,
                                "detalhes": {
                                    "cor": cor,
                                    "combustivel": combustivel,
                                    "quilometragem": quilometragem,
                                    "manutencoes": veiculo["detalhes"]["manutencoes"]
                                }
                            })
                            salvar_dados(dados)
                            st.session_state.editando = False
                            st.success("Veículo atualizado com sucesso!")
                            st.rerun()

                with col2:
                    if st.button("Cancelar Edição"):
                        st.session_state.editando = False
                        st.rerun()
    else:
        st.info("Não há veículos disponíveis no momento.")

    # Exibir veículos alugados
    st.header("Veículos Alugados")
    veiculos_alugados = dados["locadora"]["frota"]["carros"]["alugados"]
    if veiculos_alugados:
        # Formatar os dados dos veículos alugados para exibição
        alugados_formatados = []
        for veiculo in veiculos_alugados:
            alugados_formatados.append({
                "Marca": veiculo["marca"],
                "Modelo": veiculo["modelo"],
                "Ano": veiculo["ano"],
                "Placa": veiculo["placa"],
                "Categoria": veiculo["categoria"],
                "Cor": veiculo["detalhes"]["cor"],
                "Cliente": veiculo["aluguel_atual"]["cliente"],
                "Data Devolução": veiculo["aluguel_atual"]["data_prevista_devolucao"]
            })
        st.table(alugados_formatados)
    else:
        st.info("Não há veículos alugados no momento.")

    if st.session_state.usuario_atual == "admin":
        # Exibir usuários cadastrados
        st.header("Usuários Cadastrados")
        if dados["locadora"]["clientes"]["ativos"]:
            usuarios_cadastrados = [{
                "Nome": usuario,
                "CPF": dados["locadora"]["clientes"]["ativos"][usuario]["dados_pessoais"]["cpf"]
            } for usuario in dados["locadora"]["clientes"]["ativos"]]
            st.table(usuarios_cadastrados)
        else:
            st.info("Não há usuários cadastrados.")

        # Sistema de aluguel
        st.header("Alugar Veículo")
        if veiculos_disponiveis:
            placa_alugar = st.selectbox("Escolha o veículo pela placa", 
                                      [v['placa'] for v in veiculos_disponiveis])
            usuario_alugar = st.selectbox("Escolha o usuário", 
                                        list(dados["locadora"]["clientes"]["ativos"].keys()))
            data_inicio = st.date_input("Data de início")
            data_devolucao = st.date_input("Data prevista de devolução")
            valor_diaria = st.number_input("Valor da diária", min_value=0.0, step=10.0)

            if st.button("Alugar Veículo"):
                veiculo = next((v for v in veiculos_disponiveis if v['placa'] == placa_alugar), None)
                if veiculo:
                    # Remover dos disponíveis
                    dados["locadora"]["frota"]["carros"]["disponiveis"].remove(veiculo)
                    
                    # Adicionar informações do aluguel
                    veiculo["aluguel_atual"] = {
                        "cliente": usuario_alugar,
                        "data_inicio": data_inicio.strftime("%Y-%m-%d"),
                        "data_prevista_devolucao": data_devolucao.strftime("%Y-%m-%d"),
                        "valor_diaria": valor_diaria
                    }
                    
                    # Adicionar aos alugados
                    dados["locadora"]["frota"]["carros"]["alugados"].append(veiculo)
                    
                    salvar_dados(dados)
                    st.success(f"Veículo {placa_alugar} alugado para o usuário {usuario_alugar}")
                    st.rerun()
        else:
            st.warning("Não há veículos disponíveis para alugar.")

        # Sistema de devolução
        st.header("Devolver Veículo")
        if veiculos_alugados:
            placa_devolver = st.selectbox("Escolha o veículo a ser devolvido", 
                                        [v['placa'] for v in veiculos_alugados])
            
            if st.button("Devolver Veículo"):
                veiculo = next((v for v in veiculos_alugados if v['placa'] == placa_devolver), None)
                if veiculo:
                    # Remover dos alugados
                    dados["locadora"]["frota"]["carros"]["alugados"].remove(veiculo)
                    
                    # Limpar informações do aluguel
                    del veiculo["aluguel_atual"]
                    
                    # Adicionar aos disponíveis
                    dados["locadora"]["frota"]["carros"]["disponiveis"].append(veiculo)
                    
                    salvar_dados(dados)
                    st.success(f"Veículo {placa_devolver} devolvido com sucesso!")
                    st.rerun()
        else:
            st.warning("Não há veículos para devolver.")

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
