contas=[]
def pede_nome():
   return(input("Digite o nome do Cliente: "))
def pede_conta():
   return(input("Digite a Conta: "))
def pede_saldo():
   return(float(input("Digite o saldo: ")))
def mostra_dados(nome,conta,saldo):
   print("Nome: %s Conta: %s Saldo: %f"%(nome,conta,saldo))
def pede_nome_arquivo():
   return(input("Nome do Arquivo: "))
def pesquisa(nome):
   pesq_nome = nome.lower()
   for p,e in enumerate(contas):
      if e[0].lower() == pesq_nome:
         return p
   return None
def novo():
   global contas
   cont = int(input("Quantos clientes deseja gravar: "))
   n = 0
   while n < cont:
      nome = pede_nome()
      conta = pede_conta()
      saldo = pede_saldo()
      contas.append([nome,conta,saldo])
      n += 1
def apaga():
   global contas
   nome = pede_nome()
   p = pesquisa(nome)
   if p!=None:
      del contas[p]
   else:
      print("Nome não encontrado.")
def saldo_altera():
   global contas
   nome = pede_nome()
   p = pesquisa(nome)
   if p != None:
      deseja = input("Se deseja depositar digite 1 se deseja sacar digite 0: ")
      if deseja == "1":
         novo_saldo = float(input("Quanto deseja depositar: "))
      elif deseja == "0":
         novo_saldo = float(input("Quanto deseja retirar: "))
      nome = contas[p][0]
      conta = contas[p][1]
      saldo = contas[p][2]+novo_saldo
      print("Encotrada a conta")
      mostra_dados(nome,conta,saldo)
      contas[p]=[nome,conta,saldo]
def altera():
   p = pesquisa(pede_nome())
   if p != None:
      nome = contas[p][0]
      conta = contas[p][1]
      saldo = contas[p][2]
      print("Encontrado.")
      mostra_dados(nome,conta,saldo)
      nome = pede_nome()
      conta = pede_conta()
      saldo = pede_saldo()
      contas[p]=[nome,conta,saldo]
   else:
      print("Nome não encontrado.")
def lista():
   linha(30)
   for e in contas:
      mostra_dados(e[0],e[1],e[2])
   linha(30)
def le():
   global contas
   nome_arquivo = pede_nome_arquivo()
   arquivo = open(nome_arquivo,"r",encoding="utf-8")
   contas=[]
   for i in arquivo.readlines():
      nome,conta,saldo = i.strip().split("#")
      contas.append([nome,conta,saldo])
   arquivo.close()
def grava():
   nome_arquivo = pede_nome_arquivo()
   arquivo = open(nome_arquivo,"w",encoding="utf-8")
   contas=[]
   for e in contas:
      arquivo.write("%s#%s#%f\n"%(e[0],e[1],e[2]))
   arquivo.close()
def valida_faixa_inteiro(pergunta,inicio,fim):
   while True:
      try:
         valor = int(input(pergunta))
         if inicio <= valor <= fim:
            return valor
      except ValueError:
          print("Valor inválido,favor digitar entre %d e %d"%(inicio,fim))
def linha(tam):
   for i in range(tam):
      print("*",end="")
   print(" ")
def opcao_menu(tam,opcao_menu):
   if tam > (len(opcao_menu)+1):
      print("* ",end="")
      print(opcao_menu,end="")
      numero_branco = (tam-3) - len(opcao_menu)
      print(" "*numero_branco,end="")
      print("*")
   else:
      print("Erro,tamanho da linha menor que nome de opção.")
def menu():
   linha(30)
   opcao_menu(30,"1 - Novo cadastro")
   opcao_menu(30,"2 - Altera cadastro")
   opcao_menu(30,"3 - Apagar cadastro")
   opcao_menu(30,"4 - Lista cadastros")
   opcao_menu(30,"5 - Grava Arquivo")
   opcao_menu(30,"6 - Lê Arquivo")
   opcao_menu(30,"7 - Alterar saldo")
   opcao_menu(30,"0 - Sair do sistema")
   linha(30)
   return valida_faixa_inteiro("Opção: ",0,7)

while True:
   opcao=menu()
   if opcao == 0:
      break
   elif opcao == 1:
      novo()
   elif opcao == 2:
      altera()
   elif opcao == 3:
      apaga()
   elif opcao == 4:
      lista()
   elif opcao == 5:
      grava()
   elif opcao == 6:
      le()
   elif opcao == 7:
      saldo_altera()
