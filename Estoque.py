from Produto import Produto
import pickle

class Estoque:
    
    def __init__(self) -> None:
        self.__produtos:dict = dict()

    def adiconar(self, produto:Produto, qtde:int) -> None:

        produto_e_qtde = self.__produtos.get(produto.getNome())
        if produto_e_qtde == None:
            self.__produtos[produto.getName()] = [produto,qtde]
        else:
            produto_e_qtde[1] += qtde
            self.__produtos.update({produto.getName() : produto_e_qtde})

    def adiconarVarios(self, produtos:list) -> None:

        for produto, qtde in produtos:
            self.adiconar(produto, qtde)

    def remover(self, nome_produto:str, qtde:int) -> bool:
       
        removido = self.__produtos.get(nome_produto)
        if removido == None:
            print("Produto não encontrado")
            return False
        else:
            nova_qtde = removido[1] - qtde
            if nova_qtde < 0:
                print("Quantidade não encontrada em estoque")
                return False
            elif nova_qtde == 0:
                del self.__produtos[nome_produto]
                return True
            elif nova_qtde > 0:
                self.__produtos[nome_produto] = [removido[0], nova_qtde]
                return True

    def removerVarios(self, nome_produtos:list) -> bool:
        pass

    def guardarEstoque(self) -> None:
        self.__estoque:dict = dict()
        for key, value in self.__produtos:
            self.__estoque[key] = [value[0].gerarLista(), value[1]]
        
        f = open('Estoque.pickle', 'wb')
        pickle.dump(self.__estoque, f)
        f.close()

    def recuperarEstoque(self) -> None:
        f = open('Estoque.pickle', 'rb')
        self.__estoqueSalvo:dict = dict()
        self.__estoqueSalvo = pickle.load(f)
        for key, value in self.__estoqueSalvo:
            self.__produtos[key] = [Produto(value[0][0], value[0][1]), value[1]]
        f.close()





        