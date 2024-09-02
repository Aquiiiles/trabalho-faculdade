print('Bem-vindo à loja do Aquiles Duarte')

# Solicita ao usuário o valor do pedido (agora aceitando decimais)
while True:
    try:
        valorDoPedido = float(input('Entre com o valor do pedido: '))
        break
    except ValueError:
        print("Entrada inválida! Por favor, insira um número válido.")

# Solicita ao usuário a quantidade de parcelas
while True:
    try:
        quantidadeDeParcelas = int(input('Entre com a quantidade de parcelas: '))
        break
    except ValueError:
        print("Entrada inválida! Por favor, insira um número inteiro.")

# Calcula o valor da parcela com base na quantidade de parcelas
if 0 <= quantidadeDeParcelas <= 3:
    valorDaParcela = valorDoPedido / quantidadeDeParcelas
    print(f"O valor da parcela: R${valorDaParcela:.2f}")

elif 4 <= quantidadeDeParcelas < 6:
    valorDaParcela = valorDoPedido * (1 + 4/100) / quantidadeDeParcelas
    print(f"O valor da parcela: R${valorDaParcela:.2f}")

elif 6 <= quantidadeDeParcelas < 9:
    valorDaParcela = valorDoPedido * (1 + 8/100) / quantidadeDeParcelas
    print(f"O valor da parcela: R${valorDaParcela:.2f}")

elif 9 <= quantidadeDeParcelas < 13:
    valorDaParcela = valorDoPedido * (1 + 16/100) / quantidadeDeParcelas
    print(f"O valor da parcela: R${valorDaParcela:.2f}")

elif 13 <= quantidadeDeParcelas:
    valorDaParcela = valorDoPedido * (1 + 32/100) / quantidadeDeParcelas
    print(f"O valor da parcela: R${valorDaParcela:.2f}")

# Calcula o valor total
valorTotal = quantidadeDeParcelas * valorDaParcela

# Exibe o valor total do pedido
print(f"Valor total do pedido: R${valorTotal:.2f}")