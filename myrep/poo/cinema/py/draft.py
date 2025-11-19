class Cliente:
    def __init__(self, id: str, phone: int):
        self.__id: str = id
        self.__phone: int = phone
        
    def __str__(self) -> str:
       return f'{self.getId()}:{self.getPhone()}'
    
    def getId(self) -> str:
        return self.__id
    def getPhone(self) -> int:
        return self.__phone
    
    def setId(self, id: str):
        self.__id=id
    def setPhone(self, phone: int):
        self.__phone = phone


class Cinema:
    def __init__(self, capacity: int):
        self.__seats: list[Cliente | None ] = [None] * capacity

    def __str__(self) -> str:
        seats = '[' + ' '.join(list(map(lambda cliente: f'{cliente}' if cliente is not None else '-', self.getSeats()))) + ']';
        return f'{seats}'
    
    def getSeats(self) -> list[Cliente|None]:
        return self.__seats
    
    def setSeats(self, capacity: int):
        self.__seats: list[Cliente|None] = [None] * capacity
    
    def verifyIndex(self,index: int) ->bool:
        try:
            self.getSeats()[index]
            return True
        except IndexError:
            return False
    def search(self, name: str) -> int:
        for client in self.getSeats():
            if client is not None and client.getId() == name:
                return self.getSeats().index(client)
        return -1
    
    def reserve(self, id: str, phone: int, index: int):
        cliente: Cliente = Cliente(id, phone)

        if self.verifyIndex(index) == False:
            print('fail: cadeira nao existe')
            return
        if self.search(id) != -1:
            print('fail: cliente ja esta no cinema')
            return
        if self.getSeats()[index] is not None:
            print('fail: cadeira ja esta ocupada')
            return
        
        self.getSeats()[index] = cliente

    def cancel(self, id: str):
        indexSeat = self.search(id)

        if indexSeat == -1:
            print('fail: cliente nao esta no cinema')
            return
        self.getSeats()[indexSeat] = None
        return
    

def main():
    cinema: Cinema = Cinema(0)

    while True:
        line: str = input()
        args: list[str] = line.split(' ')
        print(f'${line}')
    
        match args[0]:
            case 'init':
                cinema: Cinema = Cinema(int(args[1]))

            case 'show':
                print(cinema)
            
            case 'reserve':
                cinema.reserve(
                    id = args[1],
                    phone = int(args[2]),
                    index = int(args[3])
                )
            case 'cancel':
                cinema.cancel(args[1])

            case 'end':
                break

            case _:
                print('fail: comando invalido')


if __name__ == "__main__":
    main()