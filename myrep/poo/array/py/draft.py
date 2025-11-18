class Foo:
    def __init__(self, x: int):
        self.x = x

    def __str__(self):
        return f'Foo({self.x})'
    
listaInt: list[int] = []
listaFoo: list[Foo] = []

#---

listaNumerica: list[int] = [1,2,3,4,5]

#---

print(len(listaNumerica))

#---

listaNumerica.append(7)
print(listaNumerica)
#
listaNumerica.insert(0,0)
print(listaNumerica)
#
listaNumerica.insert(5,7)
print(listaNumerica)
#

tirarFim = listaNumerica.pop()
print(listaNumerica)
print(tirarFim)
#
tirarcomeco = listaNumerica.pop(0)
print(listaNumerica)
print(tirarcomeco)
#
removerEspecifico = listaNumerica.pop(4)
print(listaNumerica)
print(removerEspecifico)

#join

listaFrase = ["opa","fi",",", "bão?"]
join = " ".join(listaFrase)
print(listaFrase)
print(join)
# sequencia 

listaSequencia = list(range(11))
print(listaSequencia)
#
print(listaNumerica[1])
#
listaFrutas = ["pera","siriguela","acerola","manga"]
for fruta in listaFrutas:
    print(fruta)

#percorrer

for fruta in range(len(listaFrutas)):
    print(f"{fruta}:{listaFrutas[fruta]}")

#filtro
listaNumer = [1,2,3,4,5,6,7,8,9,10]
print(listaNumer)
pares = [n for n in listaNumer if n % 2 == 0]
print(pares)

#

print("pera" in listaFrutas)

#

listasquare = [n** 2 for n in listaNumer]
print(listasquare)