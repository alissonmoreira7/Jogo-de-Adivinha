#JOGO DE ADIVINHAÇÃO

import random

def menuprincipal():
    print('-=-'*20)
    print(' '*15, 'JOGO DE ADIVINHAÇÂO')
    print('-=-'*20)

    print('DIFICULDADE')
    print('Fácil   (1)')
    print('Médio   (2)')
    print('Dificil (3)')

    while True:
        try:
            dificuldade = int(input('Digite o nível de dificuldade: '))
            if dificuldade not in range (1, 4):
                print('Escolha de dificuldade inválida!')
            else:
                return dificuldade
        except ValueError:
                    print("Por favor, insira um número válido!")

dificuldade = menuprincipal()

if dificuldade ==  1:
    tentar_nv = 'sim'
    while tentar_nv == 'sim':
        nums = list(range(1, 11))
        escolha_pc = random.choice(nums)

        while True:
            escolha_user = int(input('Escolha um número entre 1 e 10: '))
            if escolha_user not in range(1, 11):
                print('Número escolhido inválido!!')
            if escolha_user in range(1, 11):
                break
        
        print(f'Sua escolha final foi {escolha_user} e a escolha do seu oponente {escolha_pc}.')

        if escolha_user == escolha_pc:
            print('Parabéns, você acertou!!')
        else:
            print('Infelizmente, você perdeu!')

        tentar_nv = input('Você deseja tentar novamente? [Sim / Não]: ').lower().strip()

        if tentar_nv != 'sim':
             print('Saindo...')
             break
    print('Programa finalizado!')