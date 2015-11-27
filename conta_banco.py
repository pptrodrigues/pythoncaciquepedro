def _continuar():
  while True:
    opcao = pede_nome("Continuar [s|n]: ")
    if opcao == "s":
      return True
    elif opcao == "n":
      return False
    else:
      print("Erro. Opção Inválida.")

def menu():
   print("╔",end="")
   print("═"*23,end="")
   print("╗")
   print("║ [1] Cadastrar Cliente ║")
   print("║ [2] Listar Clientes   ║")
   print("║ [3] Procurar Cliente  ║")
   print("║ [4] Depositar         ║")
   print("║ [5] Sacar             ║")
   print("║ [6] Tranferência      ║")
   print("║ [7] Emprestimo        ║")
   print("║ [0] Sair              ║")
   print("╚",end="")
   print("═"*23,end="")
   print("╝")


def pede_valor_f(mensagem):
  while True:
    try:
      return float(input(mensagem))
    except ValueError:
      print("Ops, erro número inválido. Tente novamente.") 

def pede_valor_i(mensagem):
  while True:
    try:
       return int(input(mensagem))
    except ValueError:
       print("Ops, erro número inválido. Tente novamente.")

def pede_nome(mensagem):
  return input(mensagem)

def cadastrar():
    continuar = True
    while continuar:
      nome = pede_nome("Digite o nome do Cliente: ")
      conta = pede_valor_i("Digite a conta ex.[11111]: ")
      saldo = pede_valor_f("Digite o saldo: ")
      nomes.append(nome)
      contas.append(conta)
      saldos.append(saldo)
      continuar = _continuar()
def listar():
    for i in range(len(nomes)):
      print("**********************")
      print("* Nome: ",nomes[i])
      print("* Conta: ",contas[i])
      print("* Saldo: ",saldos[i])
      print("**********************")

def procurar():
    procurar = input("Digite o nome do Cliente: ")
    if procurar in nomes:
      print("************************************")
      print("* %s tem conta nesse banco."%procurar)
      print("************************************")
    else:
      print("****************************************")
      print("* %s não tem conta nesse banco."%procurar)
      print("****************************************")

def depositar():
  pesq_conta = pede_valor_i("Digite a conta que deseja depositar: ")
  if pesq_conta in contas:
    deposito = pede_valor_f("Digite quanto deseja depositar: ")
    ind = contas.index(pesq_conta)
    saldos[ind] = saldos[ind]+deposito
  else:
    print("Conta não existe.")
    
def sacar():
  pesq_conta = pede_valor_i("Digite a conta que deseja sacar: ")
  if pesq_conta in contas:
    ind = contas.index(pesq_conta)
    sacar = pede_valor_f("Digite quanto deseja sacar: ")
    if saldos[ind] >= sacar:
       saldos[ind] = saldos[ind] - sacar
    else:
       print("Saldo insuficiente, seu saldo é de ",saldos[ind])
  else:
    print("Conta não existe.")

def transferir():
  a_conta = pede_valor_i("Digite a conta fornecedora: ")
  if a_conta in contas:
    b_conta = pede_valor_i("Digite a conta favorecida: ")
    a_ind = contas.index(a_conta)
    if b_conta in contas:
       b_ind = contas.index(b_conta)
       while True:
         valor = pede_valor_f("Digite quanto deseja transferir: ")
         if verificar_saldo(saldos[a_ind],valor) == True:
           saldos[a_ind]=saldos[a_ind] - valor
           saldos[b_ind]=saldos[b_ind] + valor
           break
         else:
           continue      
    else:
      print("Conta inexistente.")
  else:
    print("Conta inexistente.") 

def verificar_saldo(conta_saldo,valor):
  if valor >  conta_saldo:
    print("***********************************************")
    print("* Saldo insuficiente, saldo é de ",conta_saldo,)
    print("***********************************************")
  else:
    return True
          
        
def emprestimo():
  conta = pede_valor_i("Digite a conta: ")
  if conta in contas:
    salario = pede_valor_f("Digite o salário: ")
    parcelas = pede_valor_i("Digite a quantidade de parcelas: ")
    limite = (salario*0.30)*parcelas
    valor_requerido = pede_valor_f("Diga quanto quer: ")
    ind = contas.index(conta)
    if valor_requerido <= limite:
      saldos[ind] = saldos[ind]+valor_requerido
    else:
        print("*************************")	
        print("O seu Limite é ",limite)
        print("*************************")
  
  
nomes=[]
contas=[]
saldos=[]
while True:
  menu()
  opcoes = pede_nome("Opção: ")
  if opcoes == "1":
    cadastrar()

  elif opcoes == "2":
    listar()

  elif opcoes == "3":
    procurar()

  elif opcoes == "4":
    depositar()

  elif opcoes == "5":
    sacar()

  elif opcoes == "6":
    transferir()

  elif opcoes == "7":
    emprestimo()

  elif opcoes == "0":
    print("Até a próxima.")
    break
  
  else:
    print("Opção inválida.")

