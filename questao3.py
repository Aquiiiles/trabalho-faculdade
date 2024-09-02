# EXIGÊNCIA DE CÓDIGO 1 de 7
print("Bem vindos à Fábrica de Camisetas do Aquiles Duarte")

# EXIGÊNCIA DE CÓDIGO 2 de 7
def escolha_modelo():
    """
    Pergunta o modelo desejado e retorna o valor do modelo com base na escolha do usuário.
    Repete a pergunta se o usuário digitar uma opção inválida.
    """
    precos_modelos = {
        'MCS': 1.80,  # Manga Curta Simples
        'MLS': 2.10,  # Manga Longa Simples
        'MCE': 2.90,  # Manga Curta Com Estampa
        'MLE': 3.20   # Manga Longa Com Estampa
    }
    
    while True:
        modelo = input("Entre com o modelo desejado\nMCS - Manga Curta Simples\nMLS - Manga Longa Simples\nMCE - Manga Curta Com Estampa\nMLE - Manga Longa Com Estampa\n>> ").upper()
        if modelo in precos_modelos:
            return precos_modelos[modelo]
        else:
            print("Escolha inválida, entre com o modelo novamente")

# EXIGÊNCIA DE CÓDIGO 3 de 7
def num_camisetas():
    """
    Pergunta o número de camisetas e retorna o número de camisetas com desconto aplicado,
    conforme as regras de desconto. Repete a pergunta se o usuário digitar uma quantidade inválida
    ou não numérica.
    """
    while True:
        try:
            quantidade = int(input("Entre com o número de camisetas: "))
            if quantidade > 20000:
                print("Não aceitamos tantas camisetas de uma vez. Por favor, entre com o número de camisetas novamente.")
            elif quantidade >= 2000:
                return quantidade * 0.88  # Desconto de 12%
            elif quantidade >= 200:
                return quantidade * 0.93  # Desconto de 7%
            elif quantidade >= 20:
                return quantidade * 0.95  # Desconto de 5%
            elif quantidade > 0:
                return quantidade  # Sem desconto
            else:
                print("Por favor, entre com um número válido maior que zero.")
        except ValueError:
            print("Por favor, entre com um número válido.")

# EXIGÊNCIA DE CÓDIGO 4 de 7
def frete():
    """
    Pergunta pelo serviço adicional de frete e retorna o valor do frete escolhido.
    Repete a pergunta se o usuário digitar uma opção inválida.
    """
    precos_frete = {
        '1': 100.00,  # Frete por transportadora
        '2': 200.00,  # Frete por Sedex
        '0': 0.00     # Retirar na fábrica
    }
    
    while True:
        escolha_frete = input("Escolha o tipo de frete:\n1 - Frete por transportadora - R$ 100.00\n2 - Frete por Sedex - R$ 200.00\n0 - Retirar pedido na fábrica - R$ 0.00\n>> ")
        if escolha_frete in precos_frete:
            return precos_frete[escolha_frete]
        else:
            print("Escolha inválida, por favor selecione um tipo de frete válido.")

# EXIGÊNCIA DE CÓDIGO 5 de 7
# Código principal (main)
if __name__ == "__main__":
    # Solicita o modelo e obtém o preço
    preco_modelo = escolha_modelo()
    
    # Solicita o número de camisetas e obtém a quantidade com desconto aplicado
    quantidade_com_desconto = num_camisetas()
    
    # Solicita o tipo de frete e obtém o valor do frete
    preco_frete = frete()
    
    # Cálculo do valor total
    valor_total = (preco_modelo * quantidade_com_desconto) + preco_frete
    
    # EXIGÊNCIA DE SAÍDA DE CONSOLE 4 de 4
    # Exibição do resumo do pedido
    print(f"Total: R$ {valor_total:.2f} (Modelo: {preco_modelo:.2f} * Quantidade (com desconto): {quantidade_com_desconto:.0f} + frete: {preco_frete:.2f})")
