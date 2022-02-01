class ChatBot:

    def __init__(self) -> None:
        pass

    def printar(self):
        print("================================================================================================")
        print("Bem vindo ao ChatBot de atendimento!! :)")
        print("Os seguintes comandos estão disponíveis:")
        print("1- Adicionar item\n2- Remover item\n 3- Mostrar carrinho \n4- Fechar carrinho de compras")
        print("================================================================================================\n")

    def escolhas(self):
        def switch():
            escolha = int(input("Sua escolha: "))

            if escolha == 1:
                print("================================================================================================")
                print("Ótimo! Informe o produto desejado e a quantidade a adicionar :)")
                produto = input("Sua Escolha: ")
                print("Deseja adicionar mais algum produto? S/N")
                novamente = input("Sua escolha: ")
            elif escolha == 2:
                print("================================================================================================")
                print("Ótimo! Informe o produto desejado e a quantidade a remover :)")
                produto = input("Sua Escolha: ")
                print("Deseja adicionar mais algum produto? S/N")
                novamente = input("Sua escolha: ")
            elif escolha == 3:
                print("================================================================================================")
                print("Claro! Seu carrinho atualmente possui:")
            elif escolha == 4:
                """ Valor total """
                print("================================================================================================")
                print("Sua Compra ficou no total de R$ ",""" Valortotal """)
                print("Obrigado pela preferência ;)")