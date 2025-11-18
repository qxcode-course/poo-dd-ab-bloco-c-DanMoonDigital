class Person:
    def __init__(self, name: str) -> None:
        self.name = name

    def __str__(self) -> str:
        return self.name
    
class Market:
    def __init__ (self, counter_size: int) -> None:
        self.counter: list[Person | None] = []
        for _ in range(counter_size):
            self.counter.appen(None)
        self.waiting: list [Person] = []

    def arrive(self, person: Person):
        self.waiting.append(person)

    def leave(self, index: int) -> Person | None:
        if index < 0 or index >= len(self.counter):
            print("Indice invalido")
            return None
        if self.counter[index] is None:
            print("Caixa Vazio")
            return None
        aux = self.counter[index]
        self.counter[index] = None
        return aux
    
    def give_up(self, name: str):
        for i, person in enumerate(self.waiting):
            if person.name == name:
                del self.waiting[i]
                break

    def call(self, index: int):
        if index < 0 or index >= len(self.counter):
            print("Indice Invalido")
            return
        if len(self.waiting) == 0:
            print("Fila Vazia")
            return
        self.counter[index] = self.waiting[0]
        del self. waiting [0]

    def __str__(self) -> str:
        pessoas = ", ".join([("-----" if x is None else str(x) for x in self.counter)])
        saida: str = f"Caixas: [{pessoas}] \n"
        for person in self.counter:
            if person is None:
                saida += "-----"
            else:
                saida += str(person) + " "
        esperanndo = " ,".join([str(x)] for x in self.waiting)
        saida += f"Espera: [{esperanndo}]"
        return saida

def main():
    market = Market(0)
    while True:
        line = input()
        print("$" + line)
        args = line.split(" ")
        if args[0] == "end":
            break
        elif args [0] == "end":
            break
        elif args [0] == "init":
            qtd = int(args[1])
            market = Market(qtd)
        elif args [0] == "insert":
            market.arrive(Person(args[1]))
        else:
            print("comando invalido")
main()