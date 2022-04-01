from Trabajador import Trabajador #Importamos del archivo trabajador la clase Trabajador
from Boleta import Boleta  #Importamos del archivo Boleta la clase Boleta

print(f'''
---------------------------------------------
            DATOS DE ENTRADA
---------------------------------------------''')
#Metodo del archivo main
def Datos_Entrada(): #Un método para ingreso de datos y salida
    worker = input("Trabajador                  : ").upper() #Convierte una cadena a mayúsculas
    #Podemos usar esta técnica para pedir al usuario un tipo de dato determinado que se compruebe constantemente:
    while True: #Bucle
        try: # Sentencias que quieres ejecutar, 
            category = input("Categoría [A | B | C]     : ").upper()
            if category == 'A' or category == 'B' or category == 'C':
                break  # Si no da error, corto el while con break
            else:
                print('Caracter Inválido')
        except ValueError:  #El bloque except se ejecutará cuando el bloque try falle. 
            print('Caracter Inválido')
        
    while True:
        try:
            extrahours= int(input("Horas extras         : "))
            break  # Si no da error, corto el while con break
        except ValueError:
            print("Eso no es un número, prueba otra vez...")
    while True:
        try:
            tardies= int(input("Tardanzas (minutos)     : "))
            break  # Si no da error, corto el while con break
        except ValueError:
            print("Eso no es un número, prueba otra vez...")
    #BLOQUE PRINCIPAL        
    trabajador1 = Trabajador(worker, category, extrahours, tardies)
    boleta1=Boleta(worker, category, extrahours, tardies)
    
    print(f'''
-------------------------------------------------------
|            ¡¡¡BIENVENIDO(A) {worker} !!!             
|------------------------------------------------------
|               BOLETA DE PAGO                         
|----------------------------------------------------             
|Trabajador          : {boleta1.worker}                
|Categoría           : {boleta1.category}              
|Sueldo Básico       : {boleta1.basic_salary()}        
|Descuentos Tardanzas: {boleta1.descontar_tarifa()}    
|Pago Horas extras   : {boleta1.calculate_phx()}       
|Sueldo Neto         : {boleta1.calcular_sueldoNeto()} 
|------------------------------------------------------
|                FERROTEK SAC                          |
|------------------------------------------------------|
{trabajador1.datosu()}''')
    
datos1 = Datos_Entrada()

#Para volver a preguntar al usuario si deseo continuar
while True:
    opcion=str(input("Desea continuar (SI | NO): ")).upper()
    if opcion=='SI':
        datos2=Datos_Entrada()
    if opcion=='NO':
        print('SALIDA ÉXITOSA')
        break  # Si no da error, corto el while con break
