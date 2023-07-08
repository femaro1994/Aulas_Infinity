""" [LP-PY-A02]Escreva um código em Python que peça três números e determine:
- O maior número;
- O menor número;
- Se existem números iguais e caso exista, quais são os números. """


lista = []

for c in range(3):
    lista.append(int(input(f'Digite o numero {c+1}: ')))
    
lista.reverse()

print(f'''
        O Maior número : {lista[0]}
        O Menor número : {lista[-1]}''')   
    
    
if lista[0] == lista[1]:
    print(f'Tem números iguais digitados :{lista[0]} = {lista[1]}')
elif lista[0] == lista[2]:
    print(f'Tem números iguais digitados :{lista[0]} = {lista[2]}')
elif lista[1] == lista[2]:
    print(f'Tem números iguais digitados :{lista[1]} = {lista[2]}') 
else :
    print(f'Sem números iguais!!')       