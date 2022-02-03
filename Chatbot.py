from Carrinho import Carrinho
from Estoque import Estoque
import re

class ChatBot:
    
    __carrinhoAberto = True
    def __init__(self, estoque:Estoque) -> None:
        self.__carrinho = Carrinho(estoque)

    def run(self):
        ChatBot.__carrinhoAberto = True
        self.__carrinho.resetarCarrinho()
        while(self.__carrinhoAberto):
            self.printarInicio()
            escolha = self.choices()

            if escolha == 1:
                print("================================================================================================")
                print("Ótimo! Informe o produto desejado e a quantidade a adicionar :)")
                aux = 1
                while(aux):
                    produto = self.choices()
                    nome_produto, qtde = self.__processarInput(produto)

                    if self.__validarInput(qtde, nome_produto) == 1:
                        self.__carrinho.adicionar(nome_produto, qtde)
                        aux = 0
                        print("Deseja adicionar mais algum produto? S/N")
                        novamente = self.choices()
                        if novamente == "s":
                            aux = 1
                    else:
                        print("Preencha novamente")

                    
                    
            elif escolha == 2:
                print("================================================================================================")
                print("Ótimo! Informe o produto desejado e a quantidade a remover :)")
                aux = 1
                while(aux):
                    produto = self.choices()
                    nome_produto, qtde = self.__processarInput(produto)

                    if self.__validarInput(qtde, nome_produto) == 1:
                        self.__carrinho.remover(nome_produto, qtde)
                        aux = 0
                        print("Deseja remover mais algum produto? S/N")
                        novamente = self.choices()
                        if novamente == "s":
                            aux = 1
                    else:
                        print("Preencha novamente")

            elif escolha == 3:
                print("================================================================================================")
                print("Claro! Seu carrinho atualmente possui:")
                produtos = self.__carrinho.getProdutosCarrinho()
                for key, value in produtos:
                    print(f"-{value[1]}x {key}(s)")

            elif escolha == 4:
                valor_total = self.__carrinho.fecharCarrinho()
                print("================================================================================================")
                print("Sua Compra ficou no total de R$ ",valor_total)
                print("Obrigado pela preferência ;)")
                ChatBot.__carrinhoAberto = False
            else: 
                print("Deu errado")


    def printarInicio(self):
        print("================================================================================================")
        print("Bem vindo ao ChatBot de atendimento!! :)")
        print("Os seguintes comandos estão disponíveis:")
        print("1- Adicionar item")
        print("2- Remover item")
        print("3- Mostrar carrinho")
        print("4- Fechar carrinho de compras")
        print("================================================================================================\n")

    def __processarInput(self, input:str):
        # regex do padrão de entrada
        qtde_regex = "[^-0-9]*(-*\d*)[^-0-9]*"
        produto_regex = "[-0-9]*([a-z]*)[-0-9]*"
        try:
            qtde = int(re.search(qtde_regex, input)[1])
        except:
            qtde = 0

        nome_produto = re.search(produto_regex, input)[1]

        return (nome_produto, qtde)

    def __validarInput(self, qtde:int, nome_produto:str) -> bool:
        aux = 0
        if qtde <= 0:
            print("Quantidade inválida")
            return False
        else:
            aux += 1

        if nome_produto == "":
            print("Nome do produto inválido")
            return False
        else:
            aux += 1

        if aux == 2:
            return True

    def choices(self):
        c = str(input("Sua escolha: "))
        return c.strip().lower().replace(" ", "")
