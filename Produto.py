class Produto:

    def __init__(self, initNome:str, initPreco:float):
        
        self.__Nome:str = initNome.lower().replace(" ", "")
        self.__Preco:float = initPreco

    def getNome(self) -> str:
        return self.__Nome

    def getPrice(self) -> float:
        return self.__Preco

    def gerarLista(self) ->list:
        return [self.__Nome, self.__Preco]