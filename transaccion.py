class Transaccion:
    def __init__(self, id, cliente, tarjeta, monto, fecha):
        self.id = id
        self.cliente = cliente
        self.tarjeta = tarjeta
        self.monto = monto
        self.fecha = fecha
        #Estos son detalles adicionales para la evidencia del registro de transacción.
        self.tipo = ""
        self.saldo_anterior = 0
        self.saldo_nuevo = 0

    def definir_detalle(self, tipo, saldo_ant, saldo_nue):
        self.tipo = tipo
        self.saldo_anterior = saldo_ant
        self.saldo_nuevo = saldo_nue

    def obtener_resumen(self):
        # Este método le entrega al main toda la información de la transacción.
        return {
            "ID": self.id,
            "Usuario": self.cliente.nombre,
            "Operación": self.tipo,
            "Monto": self.monto,
            "Saldo Anterior": self.saldo_anterior,
            "Nuevo Saldo": self.saldo_nuevo,
            "Fecha": self.fecha
        }