# import json

# def carregar_estoque():
#     try:
#         with open('estoque.json', 'r') as arquivo:
#             return json.load(arquivo)
#     except FileNotFoundError:
#         return {}

# def salvar_estoque(estoque):
#     with open('estoque.json', 'w') as arquivo:
#         json.dump(estoque, arquivo, indent=4)

# def adicionar_produto(estoque, nome, quantidade, preco):
#     estoque[nome] = {'quantidade': quantidade, 'preco': preco}
#     salvar_estoque(estoque)

# def remover_produto(estoque, nome):
#     if nome in estoque:
#         del estoque[nome]
#         salvar_estoque(estoque)
#     else:
#         print(f"Produto '{nome}' não encontrado.")

# def consultar_estoque(estoque, nome):
#     if nome in estoque:
#         print(f"Produto: {nome}")
#         print(f"Quantidade: {estoque[nome]['quantidade']}")
#         print(f"Preço: R$ {estoque[nome]['preco']}")
#     else:
#         print(f"Produto '{nome}' não encontrado.")

# def atualizar_estoque(estoque, nome, nova_quantidade):
#     if nome in estoque:
#         estoque[nome]['quantidade'] = nova_quantidade
#         salvar_estoque(estoque)
#     else:
#         print(f"Produto '{nome}' não encontrado.")

# if __name__ == '__main__':
#     estoque = carregar_estoque()

#     while True:
#         print("\n--- Controle de Estoque ---")
#         print("1. Adicionar Produto")
#         print("2. Remover Produto")
#         print("3. Consultar Produto")
#         print("4. Atualizar Estoque")
#         print("5. Sair")

#         opcao = int(input("Escolha uma opção: "))

#         if opcao == 1:
#             nome = input("Nome do produto: ")
#             quantidade = int(input("Quantidade: "))
#             preco = float(input("Preço: "))
#             adicionar_produto(estoque, nome, quantidade, preco)
#         elif opcao == 2:
#             nome = input("Nome do produto: ")
#             remover_produto(estoque, nome)
#         elif opcao == 3:
#             nome = input("Nome do produto: ")
#             consultar_estoque(estoque, nome)
#         elif opcao == 4:
#             nome = input("Nome do produto: ")
#             nova_quantidade = int(input("Nova quantidade: "))
#             atualizar_estoque(estoque, nome, nova_quantidade)
#         elif opcao == 5:
#             break
#         else:
#             print("Opção inválida.")

import json

def carregar_estoque():
    """Carrega os dados do estoque do arquivo JSON."""
    try:
        with open('estoque.json', 'r') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return {'produtos': []}

def salvar_estoque(estoque):
    """Salva os dados do estoque no arquivo JSON."""
    with open('estoque.json', 'w') as arquivo:
        json.dump(estoque, arquivo, indent=4)

def adicionar_produto(nome, quantidade):
    """Adiciona um produto ao estoque."""
    estoque = carregar_estoque()
    produto = {'nome': nome, 'quantidade': quantidade}
    estoque['produtos'].append(produto)
    salvar_estoque(estoque)

def remover_produto(nome):
    """Remove um produto do estoque."""
    estoque = carregar_estoque()
    estoque['produtos'] = [p for p in estoque['produtos'] if p['nome'] != nome]
    salvar_estoque(estoque)

def atualizar_quantidade(nome, nova_quantidade):
    """Atualiza a quantidade de um produto no estoque."""
    estoque = carregar_estoque()
    for produto in estoque['produtos']:
        if produto['nome'] == nome:
            produto['quantidade'] = nova_quantidade
            break
    else:
        print(f"Produto '{nome}' não encontrado.")
    salvar_estoque(estoque)

def consultar_estoque():
    """Exibe todos os produtos no estoque."""
    estoque = carregar_estoque()
    if not estoque['produtos']:
        print("Estoque vazio.")
    else:
        for produto in estoque['produtos']:
            print(f"Nome: {produto['nome']}, Quantidade: {produto['quantidade']}")

# Exemplo de uso
adicionar_produto('Maçã', 10)
adicionar_produto('Banana', 20)
consultar_estoque()
atualizar_quantidade('Maçã', 15)
remover_produto('Banana')
consultar_estoque()