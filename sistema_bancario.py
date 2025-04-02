#print("****************Menu****************")
#print("Criar usuário")
#print("Depositar")
#print("Sacar")

from datetime import datetime

saldo=0
limite=500
numero_saques=0
limite_saques=3
usuarios=[]#lista vazia para serem acrescentados valores posteriormente.
contas=[]
agencia='0001'

def menu():
    print('''
    ****************Menu****************
    (1) Criar Usuário
    (2)Criar Conta
    (3)Listar Contas
    (d)Depositar 
    (s)Sacar
    (q)
    ''')
    return input('Qual opção deseja?')

def deposito(valor,saldo):
   
    if valor>0:
        saldo+=valor
        print(f"Você depositou R${valor}")
    else:
            print("Valor do depósito inválido.Verifique a quantia digitada.")
    return saldo
            
            
            
deposito(2,0)


def saque(saque, saldo):
     hora = datetime.now()
    global numero_saques,limites,limite_saques 
    #De acordo com a documentação Python, variáveis globais não ficam presas ao limite do escopo da função.
    if numero_saques>=limite_saques:
        print('Você atingiu o limite de saques da sua conta. Tente no próximo dia útil.')
    else:
         if saque <= 0:
                print("Saque inválido.Verifique o valor e tente novamente")
         elif saque > limite:
                    print("Valor excedido. Verifique e tente novamente.")
          elif saque > saldo:
                    print("Saldo insuficiente. Verifique e tente novamente.")
            else:
                        saldo-=saque
                        numero_saques+1
        return saldo
        from datetime import datetime
def extrato (saldo)
        hora = datetime.now
        horaatual=hora.strftime('%d/%m/%y/%h:%M')
        print('===========Extrato===========')
        print(f'{horaatual} \nSaldo disponível:{saldo}')
        print('\n===========Extrato===========')

def sair()

            print('***********Encerrando o sistema***********')
        
def novo_usuario(usuario)
        cpf=int(input('Digite seu cpf (Somente números);'))
        usuario= filtrar_usuario (cpf,usuario)
        if usuario:
            print('Usuário já cadastrado a baase de dados')
            return

            nome = str('Escreva seu nome completo')
            data_nascimento = input('Informe a data de nascimento (dd--mm--aa)
            :')
            #O apend adiciona o usuário ao meu banco
            endereço = input('Informe seu indereço (Rua, numero, cep, bairro, e cidade)')
            usuario.apend(f'nome:{nome}, data de nascimento: {data_nascimento}, endereço:{endereço}')
            print('Cadastro realizado com sucesso')

def filtrar_usuário (cpf, usuario)
#filtra o usuário com base em um CPF
#A função usa uma compreenção de lista para verifica aquele que corresponde ao 
#cpf fornecido e retorna o primeiro usuário que corresponde ao cpf filtrado. Caso não encontre nada ele retorna None (nada)
usuario_filtrado = [usuario for usuario in if usuario ['cpf']===cpf]
return usuario_filtrado else None
