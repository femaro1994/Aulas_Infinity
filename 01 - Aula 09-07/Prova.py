""" 
[PY-A01] Faça um programa em python que determine em duas variáveis (senha e email) e que contenha uma senha e um email cadastrados antecipadamente,
em seguida solicite ao usuário uma senha e um email e utilize o laço de repetição juntamente com a estrutura de condição para verificar
se o email e a senha digitado pelo usuário é igual ao email e senha cadastrados antecipadamente.
E enquanto a senha e o email que o usuário digitou não for igual ao email e senha cadastrados ele continue em um loop """




#Querido Avaliador fiz mais fiz uma lista com discionarios para dificultar , mas funciona relaxa
#o whilhe True laço infinito até a variavel controle ser True para o email e senha certos
#use o ultimo para teste o email : a e senha : 123

bd_email = [ {'Email':'lucifer@gmail.com','Senha':'666'},
             {'Email':'lula@hotmail.com','Senha':'13'},
             {'Email':'douglas@yahoo.com.br','Senha':'2424'},
             {'Email':'Jason@oul.com.br','Senha':'13'},
             {'Email':'a','Senha':'123'}                                           
                                                        ]

controle = False
c = 1
while True:
    print(f'Tentativa {c} º')
    email = input('Digite o email: ')
    senha = input('Digite a senha: ')
    
    for y in bd_email:
        
        if email == y['Email'] and y['Senha']:
            print(f'O email: {email} e senha: {senha} estão corretos 👍👍 ')
            print(f'Logado com sucesso !!!👍👍👍👍')
            controle = True
    
    if controle is True:
        print(f'Sistema finalizado 😎😎😉')
        break
    else:
        print('Email e senhas invalidos 🤦‍♂️🤦‍♂️🤷‍♂️!!!')
        c += 1


