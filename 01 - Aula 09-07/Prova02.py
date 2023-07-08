""" [PY-A02] - Faça um programa que solicite ao usuário que digite 10 valores para
preencher uma lista. 

Em seguida, o programa deve separar os números pares e ímpares em listas diferentes. 

Por fim, exiba na tela os números pares, 
os números ímpares em uma tupla, a quantidade de números pares e ímpares presentes na lista, e a soma de todos os números pares e ímpares, respectivamente. """

lista_par =[]
lista_impar = []

for c in range(10):
    numero = int(input(f'Digite o número {c +1}:'))
    if numero%2 == 0:
        lista_par.append(numero)
    else:
        lista_impar.append(numero)

soma_par = sum(lista_par) #cagaço🤢🤢
soma_impar = sum(lista_impar) #cagaço🤢🤢
qnt_par = len(lista_par) #cagaço🤢🤢
qnt_impar =len(lista_impar) #cagaço🤢🤢
tupla_impar =tuple(lista_impar)# Porque a questão quis🤷‍♂️🤔🤔

print(f"""
      
      Lista numero par   : {lista_par}
      Tupla numero ímpar : {tupla_impar}
      Quantidade par     : {qnt_par}
      Quantidade impar   : {qnt_impar}
      Soma par           : {soma_par}
      Soma ímpar         : {soma_impar}
      
                                  """)