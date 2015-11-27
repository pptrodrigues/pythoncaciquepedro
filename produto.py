produtos=[]
def menu():
  print("***********************")
  print("* [1] Cadastrar       *")
  print("* [2] Listar          *")
  print("* [3] Procurar        *")
  print("* [4] Alterar estoque *")
  print("* [5] Alterar preço   *")
  print("* [0] Sair            *")
  print("***********************")

def pede_nome(mensagem):
   return input(mensagem)

def pede_numero_f(mensagem):
  while True:
    try:
      return float(input(mensagem))
    except ValueError:
      print("<Ops. Erro, Entre com numero>")

def pede_numero_i(mensagem):
  while True:
    try:
      return int(input(mensagem))
    except ValueError:
      print("<Ops. Erro, Entre com número>")

def _continuar ():
  while True:
    opcao = pede_nome("Continuar [s|n]: ")
    if opcao == "s":
       return True
    elif opcao == "n":
       return False
    else:
       print("Ops, erro. Tente novamente.")

def cadastrar():
  continuar = True
  while continuar:
    produto = pede_nome("Digite o produto: ")
    preco = pede_numero_f("Digite o preço: ")
    estoque = pede_numero_i("Digite o estoque: ")
    produtos.append([produto,preco,estoque])
    continuar = _continuar()

def listar(produtos):
  NOME = 0
  PRECO = 1
  QUANT = 2
  for produto in produtos:
    print("***************************")
    print("* Nome: ",produto[NOME])
    print("* Preço: ",produto[PRECO])
    print("* Estoque: ",produto[QUANT])
    print("***************************")

def procurar(nome):
  for produto in produtos:
    if nome == produto[0]:
      return produto
  return []

def imprimir_produto(produto):
  if len(produto) == 0:
    print("Produto não encontrado.")
  else:
    NOME = 0
    PRECO = 1
    QUANT = 2
    print("***************************")
    print("* Nome: ",produto[NOME])
    print("* Preço: ",produto[PRECO])
    print("* Estoque: ",produto[QUANT])
    print("***************************")

def alterar_estoque(produto):
   POSICAO = 2
   if len(produto) == 0:
     print("Produto não encontrado.")
   else:
     produto[POSICAO] = pede_numero_i("Digite o novo estoque: ")

def alterar_preco(produto):
   POSICAO = 1
   if len(produto) == 0:
     print("Produto não encontrado.")
   else:
     produto[POSICAO] = pede_numero_f("Digite o novo preço: ")

while True:
   menu()
   opcoes = pede_nome("Opção: ")
   if opcoes == "1":
     cadastrar()

   elif opcoes == "2":
     listar(produtos)

   elif opcoes == "3":
     produto = procurar(pede_nome("Digite nome a procurar:"))
     imprimir_produto(produto)
   
   elif opcoes == "4":
     produto = procurar(pede_nome("Digite nome a procurar:"))
     alterar_estoque(produto)
   
   elif opcoes == "5":
     produto = procurar(pede_nome("Digite o nome a procurar: "))
     alterar_preco(produto)

   elif opcoes == "0":
     print("Até a próxima.")
     break

   else:
     print("ops, erro. Tente novamente.")
