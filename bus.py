class Bus:
    def __init__(self, placa, capacidad, tipo_bus, posicion_actual):
        self.placa = placa
        self.capacidad = capacidad
        self.tipo_bus = tipo_bus 
        self.posicion_actual = posicion_actual
        self.ruta_actual = None 

    def asignar_ruta(self, objeto_ruta):
        # Este método asigna una ruta al bus si el tipo de bus coincide con el tipo de ruta.
        if self.tipo_bus == objeto_ruta.tipo_ruta:
            self.ruta_actual = objeto_ruta
            return True
        return False

    def mover_a_parada(self, nombre_parada):
        self.posicion_actual = nombre_parada

    def mostrar_info_bus(self):
        ruta_nombre = self.ruta_actual.nombre_ruta if self.ruta_actual else "Sin ruta"
        return f"Bus [{self.placa}] - Tipo: {self.tipo_bus} - En: {self.posicion_actual} - Ruta: {ruta_nombre}"