class Estacion:
    def __init__(self, ID, nombre_estacion, ubicacion):
        self.ID = ID
        self.nombre_estacion = nombre_estacion
        self.ubicacion = ubicacion
        self.rutas_disponibles = []
        self.paraderos_asociados = []

    def vincular_ruta(self, objeto_ruta):
        # Se añade un objeto de la clase Ruta a la lista de rutas disponibles en la estación.
        self.rutas_disponibles.append(objeto_ruta)
    
    def vincular_parada(self, objeto_parada):
        # Se añade un objeto de la clase Parada a la lista de paraderos asociados a la estación.
        self.paraderos_asociados.append(objeto_parada)

    def mostrar_tablero(self):
        # Este método muestra el tablero de la estación con las rutas disponibles y su tiempo de espera.
        print(f"--- Estación: {self.nombre_estacion} ---")
        if not self.rutas_disponibles:
            print("No hay rutas programadas en este momento.")
        else:
            for ruta in self.rutas_disponibles:
                print(f"Ruta:{ruta.codigo} - {ruta.nombre_ruta} / Tipo: {ruta.tipo_ruta} / Espera: {ruta.promedio_espera} min")

        for parada in self.paraderos_asociados:
            print(f"Paradero: {parada.nombre_parada} / Ubicación: {parada.ubicación}")