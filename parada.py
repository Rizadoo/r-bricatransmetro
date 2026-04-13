class Parada:
    def __init__(self, id, nombre_parada, ubicación):
        self.id = id
        self.nombre_parada = nombre_parada
        self.ubicación = ubicación
        self.rutas_asociadas = []
    def vincular_ruta(self,nombre_ruta):
        self.rutas_asociadas.append(nombre_ruta)
        
    def validar_acceso_bus(self, bus):
        #Este método valida si el bus que llega a la parada es del tipo correcto para esta parada.
        if bus.tipo_bus == "Alimentador":
            return True
        return False

    def mostrar_paradero(self):
        return f"[Paradero Alimentador] {self.nombre_parada} / Ubicado en: {self.ubicación}"