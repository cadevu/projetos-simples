"""calculadora básica
4 operações elementares ( adição, subtração, divisão, multiplicação)
raiz quadrada
potenciação
"""
import math
import os

print('#'*8 + 'PYTHON CALCULATOR' + '#' *8 )
def receber_dados():
    print('Escolha a opção correspondente a operação desejada')
    print('1 -- SOMA')
    print('2 -- SUBTRAÇÃO')
    print('3 -- DIVISÃO')
    print('4 -- MULTIPLICAÇÃO')
    print('5 -- RAIZ QUADRADA')
    print('6 -- POTENCIAÇÃO')
    global operacao
    operacao= int(input('DIGITE A OPERAÇÃO DESEJADA: '))
    if operacao not in [1,2,3,4,5,6,7]:
        print('COMANDO INVÁLIDO')
        return operacao
def soma():
    n1_soma=float(input('Digite o primeiro número a ser somado: '))
    n2_soma=float(input('Digite o segundo: '))
    print('--------------------------------------------')
    print(f'{n1_soma} + {n2_soma} = {n1_soma+n2_soma}')
def subtração():
    n1_sub=float(input('Digite o primeiro número da subtração: '))
    n2_sub=float(input('Digite o segundo: '))
    print('--------------------------------------------')
    print(f'{n1_sub} - {n2_sub} = {n1_sub-n2_sub}')
def divisao():
    n1_div= float(input('Digite o dividendo: '))
    n2_div=float(input('Digite o divisor: '))
    print('--------------------------------------------')
    print(f'{n1_div} / {n2_div} = {n1_div/n2_div:.2f}')
def multiplicação():
    n1_multi=float(input('Digite o primeiro número da multiplicação: '))
    n2_multi = float(input('Digite o segundo: '))
    print('--------------------------------------------')
    print(f'{n1_multi} x {n2_multi} = {n1_multi*n2_multi:.2f} ')
def raiz_quadrada():
    n_raiz= float(input('Digite o número no qual será obtido sua raiz quadrada: '))
    print('--------------------------------------------')
    print(f'√{n_raiz} =  {math.sqrt(n_raiz)}')
def potenciacao():
    n1_pot= float(input('Digite o número-base da potenciação: '))
    n2_pot= float(input('Digite o expoente: '))
    print('--------------------------------------------')
    return print(f'{n1_pot} elevado a {n2_pot} é igual a {n1_pot**n2_pot:.2f}')
continuacao = 's'

while continuacao=='S' or continuacao=='s':

    receber_dados()
    os.system('cls') or None
    print('--------------------------------------------')
    if operacao==1:
        (soma())
    if operacao==2:
        (subtração())
    if operacao==3:
        (divisao())
    if operacao==4:
        (multiplicação())
    if operacao ==5:
        (raiz_quadrada())
    if operacao==6:
        (potenciacao())
    continuacao=input('DESEJA CONTINUAR? [S/N]')
    while continuacao not in ['S','s','N','n']:
        print('Erro. Responda apenas com S/N')
        continuacao = input('DESEJA CONTINUAR? [S/N]')
    os.system('cls') or None
print('-----------------------------------------------------------------------------')
print('|                 Obrigado por usar a calculadora pythonica!                |')
print('-----------------------------------------------------------------------------')
