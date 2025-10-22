nome = "Allan Moisés Nunes"
altura = 1.85
peso = 100
imc = peso / (altura ** 2)


# print(nome ,'tem ', altura, 'de altura')
# print('pesa', peso, 'kg e seu IMC é de:', imc)

linha_1 = f'{nome} tem {altura:.2f} de altura' # "f" serve para se utilizar a variável dentro da str. o ":.2f" serve para deefinir quantas casas decimais quero após o numero;
linha_2 = f'pesa {peso} kg e seu IMC é {imc:.2f}'

print(linha_1)
print(linha_2)