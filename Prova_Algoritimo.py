""" [LP-PY-A02]Escreva um código em Python que peça três números e determine:
- O maior número;
- O menor número;
- Se existem números iguais e caso exista, quais são os números. """


lista = []

for c in range(3):
    lista.append(int(input(f'Digite o numero {c+1}: ')))
    
lista.reverse() tlaCrkqKup

print(f'''
        O Maior número : {max(lista)}
        O Menor número : {min(lista)}''')   
    
    
if lista[0] == lista[1]:
    print(f'Tem números iguais digitados :{lista[0]} = {lista[1]}')
elif lista[0] == lista[2]:
    print(f'Tem números iguais digitados :{lista[0]} = {lista[2]}')
elif lista[1] == lista[2]:
    print(f'Tem números iguais digitados :{lista[1]} = {lista[2]}') 
else :
    print(f'Sem números iguais!!')       
    
    
# Seu resultado sobre o maior e menor número está dando errado quando temos números repetidos.

# Mais especificamente nos seguintes testes:

# num1 = 1;   num2 = 2;    num3 = 1

# num1 = 2;   num2 = 1;   num3 = 1



# A parte de verificar se existem números iguais está ok!

# - Fernanda  
