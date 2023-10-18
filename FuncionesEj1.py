def dividir(dividendo,divisor):
    if divisor != 0:
        resultado = dividendo/divisor
        resto = dividendo % divisor 
        print(f"El resultado es {resultado}, el resto es {resto}")
        #return resultado, resto
    else:
        print("No se puede dividir por Cero, ingrese otro valor")
       # return  "No se puede dividir por cero", None

#LLamo a la funcion Dividir
dividiendo = int(input(" Ingrese el dividiendo: "))
divisor = int(input(" Ingrese el divisor: "))

#Lo Muestro al Resultado :
dividir(dividiendo,divisor)




    