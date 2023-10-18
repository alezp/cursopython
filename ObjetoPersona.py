#Defino la Clase y los atributos y métodos de la misma
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre         
        self.edad = edad

    def Mayoria_de_edad(self):
        # Averiguo si la persona es mayor de 18 años
        if (self.edad>=18):
            print(f"La persona se llama {self.nombre}, es mayor de edad ya que tiene {self.edad} año(s)")
        else:
            print(f"La persona {self.nombre} no es mayor de edad, porque tiene {self.edad} años")  

#Instancio a las personas:
persona1 = Persona("Alejandro", 33) 
persona2 = Persona("Miguel", 14) 
persona3 = Persona("Lorena", 18) 
persona4 = Persona("Yamila", 10) 
persona5 = Persona("Valentina", 45) 
persona6 = Persona("Soraya", 99)    

#llamo al método de la clase:
persona1.Mayoria_de_edad()
persona3.Mayoria_de_edad()
persona2.Mayoria_de_edad()
persona4.Mayoria_de_edad()
