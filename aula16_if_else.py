entrada = input('Você quer "entrar" ou "Sair"? ')

if entrada == 'entrar':
    print('Você entrou no sistema')
elif entrada == 'sair':
    print('Você saiu do sistema')
else:
    print('Opção não válida!!')

print('FORA DOS BLOCOS')

# O Python considera o "comando" "if" como um bloco, ou seja, quando ele encontra a opção de input válida pelo 
# usuário, ele executa o bloco e, posterior a isso, ele executa o que está fora do bloco. No nosso exemplo
# ele espera o usuário dar entrada em umas das opções para exibir a mensagem correta na tela e, independneten
# da mensagem, ele executa o print" FORA DOS BLOCOS";


# PS: a entrada dos dados não pode ser diferente do especificado, isso inclui uso de letras maiúsculas e minúsculas.