class Cliente:
    def __init__(self, id, nombre, tipo_cliente, tarjeta):
        self.id = id
        self.nombre = nombre
        self.tipo_cliente = tipo_cliente
        self.tarjeta = tarjeta

    def consultar_saldo_tarjeta(self):
        # Este método le permite al cliente consultar el saldo de su tarjeta.
        if self.tarjeta:
            return self.tarjeta.saldo
        return 0

    def procesar_pago(self, cantidad_pasajes, precio_unidad):
        # Este método permite que cliente pagué una cantidad X de pasajes
        total_a_pagar = cantidad_pasajes * precio_unidad
        
        if self.tarjeta.saldo >= total_a_pagar:
            self.tarjeta.descontar(total_a_pagar)
            return True
        return False
