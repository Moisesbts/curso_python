# Conversão de tipos, Coersão
# type conversations, typecasting, coercion

#print(1+1)

#print('a'+'b') # Como p Python é uma linguagem dinâmica, nesses casos ele não apresenta um ero, mas sim "concatena" as informações;

# print('1' + 1) #nesse caso, o Python não consegue realizar a soma ou a Concatenação, pois por regra, ele não consegue realizar operações com dois tipos diferentes;

print(int('1') + 1) # Converte um dado str em int e já realiza a operação;
print(float('1') + 1) # Converte uma str em float e já realiza a operação;
print(type(float('1') + 1)) # Exibe o tipo de dado, converte a str em float e já realiza a operação;
print(str(11) + 'b') # Converte um int em str e já realiza a concatenação;

