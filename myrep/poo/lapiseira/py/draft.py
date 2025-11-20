class Grafite:
    def _init_(self, calibre, dureza, tamanho):
        self.calibre = calibre
        self.dureza = dureza
        self.tamanho = tamanho

        def _str_(self):
            return f"{self.calibre}:{self.dureza}:{self.tamanho}"
        
class Lapisira:
    def _init_(self, calibre):
        self.calibre = calibre
        self.bico = None
        self.tambor = []

    def insert(self, grafite):
        print()



def main():
    while: True:
        line =  input()