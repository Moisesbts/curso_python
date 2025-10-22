'''condicao = 10 == 10 # Indicamos uma valor Bool, pois resultado nesse caso é "true"

if condicao:
    print('Este é o código do if') # Caso o resultado da váriável seja "true"
else:
    print('Este é o else') # Caso o resultado da variável seja "false"

if 10 == 10:
    print('Outro if') # Imprime caso na linha acima o valor ser "true". Caso seja "false", nesse caso nada será mostrado

print('Fora do if')'''


condicao1 = False
condicao2 = False
condicao3 = False
condicao4 = False


if condicao1:
    print('Código para condição 1') 
elif condicao2:
    print('Código para condição 2')
elif condicao3:
    print('Código para condição 3')
elif condicao4:
    print('Código para condição 4')
else:
    print('Nenhuma Condição foi Satisfeita') # Nesse caso, ele procura por alguma das variáveis que 
                                             # apresente condição verdadeira para exibir. Caso não haja, ele exibirá o "else"

