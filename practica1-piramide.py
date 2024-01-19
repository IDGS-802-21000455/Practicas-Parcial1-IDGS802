import os

class Piramide:
    def __init__(self):
        self.cantidad_piramide = 0

    def pedir_cantidad(self):
        self.cantidad_piramide = int(input("Ingresa la cantidad de la pirámide: "))

    def imprimir_piramide(self):
        for i in range(self.cantidad_piramide):
            for j in range(i + 1):
                print("*", end="")
            print()

def main():
    obj_piramide = Piramide()
    obj_piramide.pedir_cantidad()
    obj_piramide.imprimir_piramide()

if __name__ == "__main__":
    main()


