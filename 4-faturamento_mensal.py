# Definindo os estados para uma melhor manipulação:
e = ['SP', 'RJ', 'MG', 'ES', 'OUTROS']

faturamento = list()
for c in e:
    while True:
        try:
            v = float(input(f'Digite o faturamento mensal de {c}: '))
            if v < 0:
                print('\033[31mValor INVÁLIDO! Digite apenas valores maiores ou iguais a "0":\033[m')
            break
        except:
            print('\033[31mValor INVÁLIDO! Digite apenas valores reais!\033[m')

    # Armazenando os valores digitados na lista faturamento
    faturamento.append(v)

faturamento_total = sum(faturamento)
print(f'\033[32mO faturamento total da Distribuidora foi: R$ {faturamento_total:.2f}'.replace('.', ','))

cont = 0
for i in faturamento:
    cont += 1
    percentual = ((i / faturamento_total) * 100)
    print(f'O percentual de faturamento de {e[cont - 1]} é: {percentual:.2f} %')

# Resposta: 
# O faturamento total da Distribuidora foi: R$ 18282438,00
# O percentual de faturamento de SP é: 37.10 %
# O percentual de faturamento de RJ é: 20.06 %
# O percentual de faturamento de MG é: 15.99 %
# O percentual de faturamento de ES é: 15.99 %
# O percentual de faturamento de OUTROS é: 10.86 %