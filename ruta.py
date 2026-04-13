class Ruta:
    def __init__(self, codigo, nombre_ruta, tipo_ruta, tarifa_base):
        self.codigo = codigo
        self.nombre_ruta = nombre_ruta
        self.tipo_ruta = tipo_ruta #
        self.tarifa_base = tarifa_base
        self.promedio_espera = 0  # Se añadio un atributo nuevo para el promedio de espera.
        self.paradas = []         # se añadio una Lista para almacenar las paradas asociadas a esta ruta.

    def establecer_promedio(self, minutos):
        self.promedio_espera = minutos

    def añadir_parada(self, objeto_parada):
        self.paradas.append(objeto_parada)

    def mostrar_detalle_ruta(self):
        # Este método es el que usará la Estación para mostrar los datos
        return f"Ruta {self.codigo} ({self.tipo_ruta}) / Promedio: {self.promedio_espera} min"