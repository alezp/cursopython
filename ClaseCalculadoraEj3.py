#Defino la Clase
class Calculadora:
    def __init__(self, numero1, numero2):
        self.numero1 = input(numero1)
        self.numero2 = input(numero2)

#Defino los metodos de la clase
    def Suma(self):

    def Multiplicacion(self):

    def Resta(self):

    def Division(self, numero1, numero2): 
        num1 = input(f"Ingrese el primer numero,{numero1}")
        num2 = input(f"Ingrese el primer numero,{numero1}")
        if (numero2 !=0):
            division = numero1/numero2
        else:
            print("Error: No se puede dividir por cero, ingrese otro valor")
    return(division)  

#Instancio a los objetos :
num1 = Calculadora()        


#llamo a los metodos : 
num1.Suma()