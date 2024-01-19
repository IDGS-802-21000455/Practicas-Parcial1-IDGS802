import os



class OrdenarNumeros:
    def __init__(self):
        self.lista_numeros = []

    def pedir_numeros(self):
        num_lista = int(input("Dame la cantidad de números a insertar: "))
        for i in range(num_lista):
            numero = int(input("Ingresa el número {}: ".format(i + 1)))
            self.lista_numeros.append(numero)

    def mostrar_lista(self):
        print("La lista resultante es:", self.lista_numeros)

    def ordenar_lista(self):
        self.lista_numeros.sort()
        print("La lista ordenada es:", self.lista_numeros)

    def clasificar_pares_impares(self):
        numeros_pares = []
        numeros_impares = []
        for num in set(self.lista_numeros):
            if num // 2*2 == num:
                numeros_pares.append(num)
            else:
                numeros_impares.append(num)

        print("Los números pares son: ", numeros_pares)
        print("Los números impares son:", numeros_impares)

def main():
    obj_ordena = OrdenarNumeros()

    obj_ordena.pedir_numeros()
    obj_ordena.mostrar_lista()
    obj_ordena.ordenar_lista()
    obj_ordena.clasificar_pares_impares()

if __name__ == "__main__":
    main()
