print("Bem-vindo à Empresa do Aquiles Duarte")
print("-" * 50)

# Lista de funcionários e id_global inicial
lista_funcionarios = []
id_global = 4925816  

def cadastrar_funcionario():
    from copy import copy
    
    global id_global
    id_global += 1
    print("--------------------------------------------------")
    print("---------- MENU CADASTRAR FUNCIONÁRIO ------------------")
    print(f"Id do Funcionário: {id_global}")
    nome = input("Por favor entre com o nome do Funcionário: ")
    setor = input("Por favor entre com o setor do Funcionário: ")
    salario = float(input("Por favor entre com o salário do Funcionário: "))
    
    funcionario = {
        'id': id_global,
        'nome': nome,
        'setor': setor,
        'salario': salario
    }
    
    lista_funcionarios.append(copy(funcionario))
    print("--------------------------------------------------")
    print("Funcionário cadastrado com sucesso!")

def consultar_funcionarios():
    while True:
        print("\nEscolha uma opção:")
        print("1 - Consultar Todos")
        print("2 - Consultar por Id")
        print("3 - Consultar por Setor")
        print("4 - Retornar ao menu")
        
        opcao = int(input(">> "))
        
        if opcao == 1:
            print("--------------------------------------------------")
            print("---------- CONSULTAR TODOS FUNCIONÁRIOS ------------------")
            if lista_funcionarios:
                for funcionario in lista_funcionarios:
                    print(f"\nID: {funcionario['id']}, Nome: {funcionario['nome']}, Setor: {funcionario['setor']}, Salário: {funcionario['salario']:.2f}")
            else:
                print("Nenhum funcionário cadastrado.")
            print("--------------------------------------------------")
        
        elif opcao == 2:
            id = int(input("Digite o ID do funcionário: "))
            encontrado = False
            print("--------------------------------------------------")
            print("---------- CONSULTAR FUNCIONÁRIO POR ID ------------------")
            for funcionario in lista_funcionarios:
                if funcionario['id'] == id:
                    print(f"\nID: {funcionario['id']}, Nome: {funcionario['nome']}, Setor: {funcionario['setor']}, Salário: {funcionario['salario']:.2f}")
                    encontrado = True
                    break
            if not encontrado:
                print("ID inválido.")
            print("--------------------------------------------------")
        
        elif opcao == 3:
            setor = input("Digite o setor do funcionário: ")
            encontrados = False
            print("--------------------------------------------------")
            print("---------- CONSULTAR FUNCIONÁRIOS POR SETOR ------------------")
            for funcionario in lista_funcionarios:
                if funcionario['setor'] == setor:
                    print(f"\nID: {funcionario['id']}, Nome: {funcionario['nome']}, Setor: {funcionario['setor']}, Salário: {funcionario['salario']:.2f}")
                    encontrados = True
            if not encontrados:
                print("Nenhum funcionário encontrado para o setor informado.")
            print("--------------------------------------------------")
        
        elif opcao == 4:
            break
        
        else:
            print("Opção inválida. Tente novamente.")

def remover_funcionario():
    id = int(input("Digite o ID do funcionário a ser removido: "))
    global lista_funcionarios
    lista_funcionarios = [func for func in lista_funcionarios if func['id'] != id]
    print("Funcionário removido com sucesso!")

while True:
    print("\n--------------- MENU PRINCIPAL -------------------")
    print("Escolha a opção desejada:")
    print("1 - Cadastrar Funcionários")
    print("2 - Consultar Funcionário(s)")
    print("3 - Remover Funcionário")
    print("4 - Sair")
    
    opcao = int(input(">> "))
    
    if opcao == 1:
        cadastrar_funcionario()
    
    elif opcao == 2:
        consultar_funcionarios()
    
    elif opcao == 3:
        remover_funcionario()
    
    elif opcao == 4:
        print("Saindo do programa.")
        break
    
    else:
        print("Opção inválida. Tente novamente.")

# Teste de execução
lista_funcionarios.append({'id': 123456, 'nome': 'Alice', 'setor': 'TI', 'salario': 5000.00})
lista_funcionarios.append({'id': 123457, 'nome': 'Bob', 'setor': 'TI', 'salario': 4500.00})
lista_funcionarios.append({'id': 123458, 'nome': 'Charlie', 'setor': 'RH', 'salario': 4000.00})

print("\nConsulta de todos os funcionários:")
for funcionario in lista_funcionarios:
    print(f"ID: {funcionario['id']}, Nome: {funcionario['nome']}, Setor: {funcionario['setor']}, Salário: {funcionario['salario']:.2f}")

print("\nConsulta por ID (123457):")
for funcionario in lista_funcionarios:
    if funcionario['id'] == 123457:
        print(f"ID: {funcionario['id']}, Nome: {funcionario['nome']}, Setor: {funcionario['setor']}, Salário: {funcionario['salario']:.2f}")

print("\nConsulta por setor (TI):")
for funcionario in lista_funcionarios:
    if funcionario['setor'] == 'TI':
        print(f"ID: {funcionario['id']}, Nome: {funcionario['nome']}, Setor: {funcionario['setor']}, Salário: {funcionario['salario']:.2f}")

print("\nRemovendo funcionário com ID 123456...")
remover_funcionario()
print("\nConsulta de todos os funcionários após remoção:")
for funcionario in lista_funcionarios:
    print(f"ID: {funcionario['id']}, Nome: {funcionario['nome']}, Setor: {funcionario['setor']}, Salário: {funcionario['salario']:.2f}")
