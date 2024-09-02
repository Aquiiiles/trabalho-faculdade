print('-------- Bem-vindo à loja de marmitas de Aquiles Duarte ---------')
print('---------------------------Cardápio------------------------------')
print('-----------------------------------------------------------------')
print('---- | TAMANHO | BIFE ACEBOLADO (BA) | FILE DE FRANGO (FF) | ----')
print('---- |    P    |      R$ 16.00       |      R$ 15.00       | ----')
print('---- |    M    |      R$ 18.00       |      R$ 17.00       | ----')
print('---- |    G    |      R$ 22.00       |      R$ 21.00       | ----')
print('-----------------------------------------------------------------')

# Dicionário para armazenar os preços com base no sabor e tamanho
precos = {
    'BA': {'P': 16.00, 'M': 18.00, 'G': 22.00},
    'FF': {'P': 15.00, 'M': 17.00, 'G': 21.00}
}

# Dicionário para associar a abreviação ao nome completo do prato
nomesPratos = {
    'BA': 'Bife Acebolado',
    'FF': 'Filé de Frango'
}

# Variável para armazenar o valor total
valor_total = 0.0

while True:
    sabor1 = input('Entre com o sabor desejado (BA/FF): ').upper()

    if sabor1 in precos:
        while True:
            tamanho = input('Entre com o tamanho desejado (P/M/G): ').upper()
            if tamanho in precos[sabor1]:
                valor = precos[sabor1][tamanho]
                valor_total += valor
                nomePrato = nomesPratos[sabor1]  # Obter o nome completo do prato
                print(f'Você pediu um {nomePrato} no tamanho {tamanho}, o preço é R$ {valor:.2f}.')
                break
            else:
                print('Tamanho inválido. Tente novamente.')
        
        # Perguntar se o usuário deseja mais alguma coisa
        maisAlgumaCoisa = input('Deseja mais alguma coisa? (S/N): ').upper()
        if maisAlgumaCoisa == 'N':
            print(f'O valor total a ser pago: R$ {valor_total:.2f}.')
            break
    else:
        print('Sabor inválido. Tente novamente.')
