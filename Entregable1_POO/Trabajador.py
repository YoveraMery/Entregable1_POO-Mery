class Trabajador: #Declarmos la clase Trabajador.
    #Función de inicializar
    def __init__(self, worker, category, extrahours, tardies):
        self.worker = worker
        self.category = category
        self.extrahours = extrahours
        self.tardies = tardies
        
    def datosu(self): # creamos la funcion "datos"

        if self.category == 'A' or self.category == 'B' or self.category == 'C':
            
            self.dt = '!BOLETA GENERADA ÉXITOSAMENTE¡'
        
        else:
            self.dt = "!BOLETA GENERADA SIN ÉXITO¡"

        return self.dt # retornar resultado a la función
            