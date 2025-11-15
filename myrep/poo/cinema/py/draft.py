class Pessoa:
    def __init__(self, nome: str):
        self.nome = nome
    def __str__(self):
        return self.nome