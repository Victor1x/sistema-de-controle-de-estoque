import pandas as pd
import os

def user_ver():
    user=str(input('Insira o nome do usuário: '))
    verificador=login.loc[login['Usuário']==user,'Usuário']
    i=1
    tentativas=3
    if user==verificador.values:
       while i<=3:
           senha=str(input('Insira a senha: ')) 
           confirmar_senha=login.loc[login['Usuário']==user,'Senha']
           if senha==confirmar_senha.values:
               os.system('cls') or None
               print('Bem vindo ', user)
               print('aperte enter para continuar! ')
               fechar=str(input())
               x=0
               break
           else:
               tentativas=tentativas-i
               print('Senha incorreta! ')
               print('Restam ', tentativas, ' tentativas!')
               i=i+1
               x=1
    else:
        os.system('cls') or None
        print('Usuário não encontrado! ')
        fechar=str(input())
        os.system('cls') or None
        user_ver()
    return(x)

def inserir():
    nome=str(input("nome: "))
    buscador=plan.loc[plan['Nome']==nome,'Nome'].values
    if buscador==nome:
        print('Item já existente!')
        print(plan.loc[plan['Nome']==nome, ["Nome","Tipo",'Valor',"Quantidade","Quant_mínima", "Quant_max"]])
        fechar=str(input())
    else:
        os.system('cls') or None
        print('nome: ',nome)
        tipo=str(input("categoria: "))
        valor=float(input("Preço: "))
        qstoq=int(input("quantidade em estoque: "))
        qminstoq=int(input("Defina uma quantidade mínima em estoque: "))
        qmaxstoq=int(input("Quantidade máxima do produto: "))
        plan.loc[len(plan),'Nome'] = nome
        plan.loc[plan['Nome']==nome,'Tipo'] = tipo
        plan.loc[plan['Nome']==nome,'Valor'] = valor
        plan.loc[plan['Nome']==nome,'Quantidade'] = qstoq
        plan.loc[plan['Nome']==nome,'Quant_mínima'] = qminstoq
        plan.loc[plan['Nome']==nome,'Quant_max'] = qmaxstoq
        plan.to_excel('produtos.xlsx', index=False)
        listar()

def listar():
    os.system('cls') or None
    print('='*60)
    print(plan)
    print('='*60)
    fechar=str(input())

def buscar():
    buscador=str(input('Informe o nome do produto: '))
    print(plan.loc[plan['Nome']==buscador, ["Nome","Tipo",'Valor',"Quantidade","Quant_mínima", "Quant_max"]])
    fechar=str(input())
    
def modificar():
    buscador=str(input('Informe o nome do produto que deseja modificar: '))
    procurador=plan.loc[plan['Nome']==buscador,'Nome'].values
    if buscador==procurador:
        print(plan.loc[plan['Nome']==buscador, ["Nome","Tipo",'Valor',"Quantidade","Quant_mínima", "Quant_max"]])
        nome=str(input("nome: "))
        tipo=str(input("categoria: "))
        valor=float(input("Preço: "))
        qstoq=int(input("quantidade em estoque: "))
        qminstoq=int(input("Defina uma quantidade mínima em estoque: "))
        qmaxstoq=int(input("Quantidade máxima do produto: "))
        plan.loc[plan['Nome']==buscador,'Nome'] = nome
        plan.loc[plan['Nome']==buscador,'Tipo'] = tipo
        plan.loc[plan['Nome']==buscador,'Valor'] = valor
        plan.loc[plan['Nome']==buscador,'Quantidade'] = qstoq
        plan.loc[plan['Nome']==buscador,'Quant_mínima'] = qminstoq
        plan.loc[plan['Nome']==buscador,'Quant_max'] = qmaxstoq
        listar()
    else:
        print('Item não encontrado')
        fechar=str(input())
        listar()

#def excluir():
    buscador=str(input('Informe o nome do produto que deseja modificar: '))
    procurador=plan.loc[plan['Nome']==buscador,'Nome'].values
    if buscador==procurador:
        verificador=str(input('Realmente deseja EXCLUIR este item? s/n '))
        if verificador=='s':
            print('excluindo...')
            fechar=str(input())
            print(plan)

def excluir():
    buscador=str(input("Insira o nome do produto que deseja excluir: "))
    procurador=plan.loc[plan['Nome']==buscador,'Nome'].values
    if buscador==procurador:
        os.system('cls') or None
        print(plan.loc[plan['Nome']==buscador, ["Nome","Tipo",'Valor',"Quantidade","Quant_mínima", "Quant_max"]])
        i=int(input('Insira o número da linha do produto: '))
        fechar=str(input(''))
        plan.drop(i, axis=0, inplace=True)
        listar()
    else:
        os.system('cls') or None
        print('Item não encontrado')
        fechar=str(input())
        

login=pd.read_excel('senhas.xlsx')
plan=pd.read_excel('produtos.xlsx')
os.system('cls') or None
run2=0
run=user_ver()

while run==0:
    os.system('cls') or None
    print("="*25)
    print(" Inserir produto    = 1 ")
    print(" Listar produtos    = 2 ")
    print(" Buscar produtos    = 3 ")
    print(" Modificar produtos = 4 ")
    print(" Excluir produto    = 5 ")
    print(" Fechar programa    = 6 ")
    print("="*25)
    fun=int(input(""))
    os.system('cls') or None

    while run2==0:
        match fun:
            case 1:
                inserir()
                break
            case 2:
                listar()
                break
            case 3:
                buscar()
                break
            case 4:
                modificar()
                break
            case 5:
                excluir()
                break
            case 6:
                run=1
                run2=1
            case _:
                run2=1
                os.system('cls') or None
                break

plan.to_excel('produtos.xlsx', index=False)
os.system('cls') or None