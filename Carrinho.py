from Produto import Produto
from Estoque import Estoque

class Carrinho:
    def __init__(self, estoque:Estoque):
        self.__produtosCarrinho = dict()
        self.__estoque = estoque

    def adicionar(self, nome_produto:str, qtde:int) -> bool:
        
        tamanho_carrinho = self.__produtosCarrinho.get(nome_produto)
        tamanho_carrinho[1] += qtde

        if self.__estoque.emEstoque(nome_produto, tamanho_carrinho[1]):
            return False
        
        self.__produtosCarrinho.update({nome_produto : [tamanho_carrinho[0], tamanho_carrinho[1]]})
        return True
    
    def remover(self, nome_produto:str, qtde:int) -> bool:
       
        tamanho_carrinho = self.__produtosCarrinho.get(nome_produto)
       
        if tamanho_carrinho == None:
            print("Produto não encontrado no Carrinho")
            return False
        tamanho_carrinho[1] -= qtde

        if tamanho_carrinho[1] < 0:
            print("Quantidade escolhida para remover maior do que a presente")
            return False
        elif tamanho_carrinho[1] == 0:
            del self.__produtosCarrinho[nome_produto]
            return True
        elif tamanho_carrinho[1] < 0:
            self.__produtosCarrinho.update({nome_produto : [tamanho_carrinho[0], tamanho_carrinho[1]]})
            return True

    def getProdutosCarrinho(self):
        return self.__produtosCarrinho

    def __totalApagar(self) -> float:
        total:float = 0
        for key, value in self.__produtosCarrinho:
            total += self.__estoque.getPreco(key) * value[1]
        return total

    def fecharCarrinho(self):
        
        for key, value in self.__produtosCarrinho:
            self.__estoque.remover(key, value[1])
        
        valorTotal = self.__totalApagar()
        
        self.resetarCarrinho()

        return valorTotal
        
    def resetarCarrinho(self):
        self.__produtosCarrinho = dict()



