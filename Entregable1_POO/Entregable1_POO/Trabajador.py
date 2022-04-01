class Trabajador: #Declarmos la clase Trabajador.
    #Función de inicializar
    def __init__(self, worker, category, extrahours, tardies):
        self.worker = worker
        self.category = category
        self.extrahours = extrahours
        self.tardies = tardies
        
    def basic_salary(self):  #Está función, es para asignar el valor a cada categoría
        if self.category == 'A':
            self.bs = 3000
        
        elif self.category == 'B':
            self.bs = 2500
            
        else:
            self.bs = 2000

        return self.bs # retornar resultado a la función
        
    def datosu(self): # creamos la funcion "datos"

        if self.category == 'A' or self.category == 'B' or self.category == 'C':
            
            self.dt = '!BOLETA GENERADA ÉXITOSAMENTE¡'
        
        else:
            self.dt = "!BOLETA GENERADA SIN ÉXITO¡"

        return self.dt # retornar resultado a la funciónz
            