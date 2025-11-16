class Pessoa:
    def __init__(self, nome: str):
        self.nome = nome
    def __str__(self):
        return self.nome
class Budega:

    def __init__(self, num_caixas: int):
        self.num_caixas = 0
        self.caixas: list[Pessoa|None] = []
        for _ in range(num_caixas):
            self.caixas.append(None)
        self.espera: list [Pessoa] = []

    def enter(self,pessoa: Pessoa):
        self.espera.append(pessoa)

    def call(self,index:int):
        if index < 0 or index >= len(self.caixas):
            print("caixa inexistente")
            return
        if self.caixas[index] is not None:
            print("caixa ocupado")
            return
        if len(self.espera) == 0:
            print("ninguem esperando")
        self.caixas[index] = self.espera[0]
        del self.espera[0]

    def finish (self,index:int):
        if index < 0 or index >= len(self.caixas):
            print("caixa inexistente")
            return
        if self.caixas[index] is None:
            print("caixa vazio")
            return
        self.caixas[index] = None

    def give_up(self,nome:str) -> Pessoa | None:
        for i, pessoa in enumerate(self.espera):
            if pessoa.nome == nome:
                aux = self.espera[i]
                del self.espera[i]
                return aux
        return None



    def __str__(self):
        caixas = ",".join([str(x) for x in self.caixas]) # type: ignore
        espera = ",".join([str(x) for x in self.espera]) # type: ignore
        return f"Caixas:{caixas}\nEspera:{espera}"
    

def main():
    budega = Budega(0)
    while True: #loop infinito 
        line: str = input()
        print ("$" + line)
        args: list[str]=line.split(" ")


        if args[0] == "end":
            break


        elif args[0] == "init":
            budega = Budega(int(args[1]));


        elif args[0] == "show":
            print(budega)

        elif args [0] == "seca":
           

        elif args[0] == "enxugar":

        elif args[0] == "torcer":

        else: 
            print("falhou: comando não encontrado")
if __name__ == "__main__":

    main()





