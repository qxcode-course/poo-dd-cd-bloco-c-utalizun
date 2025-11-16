class Pessoa:
    def __init__(self, nome: str):
        self.nome = nome
    def __str__(self):
        return self.nome
    


class Budega:

    def __init__(self, num_caixas: int):
        self.caixas: list[Pessoa | str] = []
        for _ in range(num_caixas):
            self.caixas.append("-----")
        self.espera: list[Pessoa] = []

    def enter(self, pessoa: Pessoa):
        self.espera.append(pessoa)

    def call(self, index: int):
        if index < 0 or index >= len(self.caixas):
            print("caixa inexistente")
            return
        
        if self.caixas[index] != "-----":
            print("fail: caixa ocupado")
            return
        
        if len(self.espera) == 0:
            print("fail: sem clientes")
            return  # <-- ESSENCIAL
        
        self.caixas[index] = self.espera.pop(0)

    def finish(self, index: int):
        if index < 0 or index >= len(self.caixas):
            print("fail: caixa inexistente")
            return
        
        if self.caixas[index] == "-----":
            print("fail: caixa vazio")
            return
        
        self.caixas[index] = "-----"

    def give_up(self, nome: str) -> Pessoa | None:
        for i, pessoa in enumerate(self.espera):
            if pessoa.nome == nome:
                return self.espera.pop(i)
        return None

    def __str__(self):
        caixas = " [" + ", ".join([str(x) for x in self.caixas]) + "]"
        espera = " [" + ", ".join([str(x) for x in self.espera]) + "]"
        return f"Caixas:{caixas}\nEspera:{espera}"
    

def main():
    budega = Budega(0)
    while True:
        line: str = input()
        print("$" + line)
        args = line.split(" ")

        if args[0] == "end":
            break
        elif args[0] == "init":
            budega = Budega(int(args[1]))
        elif args[0] == "show":
            print(budega)
        elif args[0] == "arrive":
            pessoa = Pessoa(args[1])
            budega.enter(pessoa)
        elif args[0] == "call":
            budega.call(int(args[1]))
        elif args[0] == "finish":
            budega.finish(int(args[1]))
        else:
            print("falhou: comando não encontrado")

if __name__ == "__main__":
    main()
