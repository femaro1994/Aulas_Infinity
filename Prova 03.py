""" [LP-PY-A03]Desenvolva um programa que leia o nome, idade e sexo de 5 pessoas. No final do programa, exiba:

- A média de idade de todo o grupo.
- Qual o nome da pessoa mais velha.
- Quantas pessoas têm menos de 20 anos.
- Quantas pessoas têm mais de 40 anos.
- Qual o sexo da pessoa mais nova. """

lista = []
cont_20 = 0
cont_40 = 0
lista_idade = []

for c in range(2):
    
    nome = input(f'Digite o Nome da Pessoa {c+1} :')
    idade = int(input(f'Digite a Idade da Pessoa {c+1} :'))
    lista_idade.append(idade)
    sexo = input(f'Digite o Sexo [m/f] da Pessoa {c+1} :')
    
    if idade > 40:
        cont_20 += 1
    elif idade > 20:
        cont_40 += 1
        
    dic_pessoas = {
                'Nome': nome,
                'Idade': idade,
                'Sexo': sexo
                            }
    
    lista.append(dic_pessoas)
    
print(lista)
lista.sort(key = lambda x:x['Idade'], reverse = True)#Reverse True pessoa ordem decrescente
print(lista)
media_idade = sum(lista_idade)/len(lista_idade)



print(f"""
        Pesssoas com mais de 20  : {cont_20}
        Pesssoas com mais de 40  : {cont_40}
        Sexo da pessoa mais nova : {lista[-1]['Sexo']}
        O nome da pessoa mais velha: {lista[0]['Nome']}
        A média das idades do grupo: {media_idade}
                                                        """)

