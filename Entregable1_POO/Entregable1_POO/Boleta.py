from Trabajador import Trabajador #Importamos del archivo trabajador la clase Trabajador

class Boleta(Trabajador): #Declaramos una nueva clase y heredamos.
    def __init__(self, worker, category, extrahours, tardies): #Inicializamos cada atributo
        self.worker = worker
        self.category = category
        self.extrahours = extrahours
        self.tardies = tardies
        
    def calculate_ph(self): # ->Para calcular el Pago por hora
        if self.category == 'A' or self.category == 'B' or  self.category == 'C':
            self.ph = round(self.bs / 240 , 2)
            
        return self.ph # retornar resultado a la función


    def calculate_phx(self): #-> Para calcular el pago por horas extras.
        if self.category == 'A' or self.category == 'B' or  self.category == 'C':
            self.phx = round(self.calculate_ph()*  self.extrahours , 2)   
            
        return self.phx # retornar resultado a la función


    def descontar_tarifa(self): #-> Para descontar el descuento por tardanzas
        self.dsct_tar = round (((self.bs / 240) / 60)* self.tardies, 2)
            
        return self.dsct_tar # retornar resultado a la función
        
        
    def calcular_sueldoNeto(self): #Para calcular el sueldo neto
        self.calculate_Sn = round(self.bs - self.dsct_tar + self.phx, 2)
            
        return self.calculate_Sn # retornar resultado a la función