class Mascota:
    def __init__(self, nombre, raza, edad):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad

    def Saludar(self):
        print(f"La mascota de hoy se llama {self.nombre}, es de raza {self.raza} y tiene {self.edad} año(s)")
        # return nombre, raza, edad    
    
perro = Mascota("Otto", "Perro", 1)
gato = Mascota("Luis", "Gato", 4)       
castor = Mascota("Chuchu", "castor", 2)
camello = Mascota("Deivid", "Dromedario", 5)

gato.Saludar()
camello.Saludar()
castor.Saludar()
perro.Saludar()
