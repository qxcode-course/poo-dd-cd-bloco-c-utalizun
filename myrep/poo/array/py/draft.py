class Pessoa:
    def __init__(self, nome: str):
        self.nome = nome
    def __str__(self):
        return self.nome
class Budega:
    def __init__(self, num_caixas:int):
        self.caixas: list[Pessoa|None] = []
        for _ in range(num_caixas):
            self.caixas.append(None)
        self.espera: list [Pessoa] = []
    def __str__(self):
        caixas = ",".join([str(x) for x in self.caixas]) # type: ignore
        espera = ",".join([str(x) for x in self.espera]) # type: ignore
        return f"Caixas:{caixas}\nEspera:{espera}"
    


pessoa = Pessoa("Maria")
print(pessoa)
bud = Budega(3)
bud.espera.append(pessoa)
print(bud)



         