#cant_contactos
class Contacto :
    def __init__(self, nombre, telefono, email):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email

    def ListarContactos(self, nombre, telefono, email):
         print(f"Nombre:{self.nombre} , Telefono: {self.telefono}, Email{self.email}")         
         
     
    def BuscarContactos(self, nombre, telefono, email):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email
        # Verifico si el usuario ingreso un nombre, un telefono o un email para realizar la busqueda :   
           
    def CerrarAgenda():
        exit()
        pass       
class Agenda:
    def __init__(self):
      self.contactos = []
     # cant_contactos = self.contactos.count()

    # Verifico si el usuario ingreso un nombre, un telefono o un email para realizar la busqueda :
      #if (nombre != 0):
          # for contactos in contactos:
            #      return contacto 
       # else (telefono != 0):    
    
     # Agrego contactos a  la agenda
    def AgregarContacto(self, nombre, telefono, email):
        nombre = input ("Ingrese el Nombre:" )
        telefono = input ("Ingrese el Telefono:" )
        email = input("Ingrese el Email:" )
        self.contactos.append(Contacto(nombre, telefono, email))
    print(Contacto)
     
   # muestro todos los  contactos de la agenda 
    def MostrarContacto(self):
        for contacto in self.contactos:
            Contacto.ListarContactos()

    def BuscarContacto(self, nombre, telefono, email):
# Verifico si el usuario ingreso un nombre, un telefono o un email para realizar la busqueda :
      #if (nombre != 0):
        for contacto in self.contactos:
                if contacto.nombre == nombre or contacto.telefono == telefono or contacto.email == email:
                    return contacto
                else:
                    print(f"No se encontró un contacto con ese dato {nombre},{telefono},{email}")
                    return None                
           
             
    def EditarContacto(self, nombre, telefono, email):
        contacto = self.buscar_contacto(nombre, telefono, email)
        if contacto is not None:
            contacto.editar()
        else:
            print(f"No se encontró un contacto con sos datos {nombre},{telefono},{email}")



    def menu():
        print("1. Añadir contacto")
        print("2. Listar contactos")
        print("3. Buscar contactos")
        print("4. Editar contactos")
        print("5. Salir")    
            
    
# Instancio a los objetos , creo una agenda :
mi_agenda = Agenda()

while True:
    # Mostrar el menú de la agenda
    Agenda.menu()

    # Preguntar al usuario qué acción quiere realizar
    opcion = input("Elige una opción: ")

    if opcion == "1":
        mi_agenda.AgregarContacto()
    elif opcion == "2":
        mi_agenda.MostrarContacto()
    elif opcion == "3":
        mi_agenda.BuscarContacto()
    elif opcion == "4":
        mi_agenda.EditarContacto()  
    elif opcion == "5":
        break  
    else:
        print("Opción no válida. Por favor, intenta de nuevo.")

#Saber cuantos contactos hay en total actualmente 


# LLamo a los metodos de la clase
#nuevo_contacto = input(mi_agenda.AgregarContacto())
#for contacto in 
   # print("Ingrese el nuevo contacto : ")
   # mi_agenda.AgregarContacto()

#contacto_buscado = input(*args)    
     # Agrego contactos a  la agenda
#3nuevo_contacto = input(mi_agenda.AgregarContacto())


