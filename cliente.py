class Cliente:
    def __init__(self, id, nombre, tipo_cliente, tarjeta):
        self.id = id
        self.nombre = nombre
        self.tipo_cliente = tipo_cliente
        self.tarjeta = tarjeta

    def consultar_saldo_tarjeta(self):
        # El cliente le pregunta a su tarjeta cuánto tiene de saldo
        if self.tarjeta:
            return self.tarjeta.saldo
        return 0

    def procesar_pago(self, cantidad_pasajes, precio_unidad):
        # El cliente intenta pagar una cantidad X de pasajes
        total_a_pagar = cantidad_pasajes * precio_unidad
        
        if self.tarjeta.saldo >= total_a_pagar:
            self.tarjeta.descontar(total_a_pagar)
            return True
        return False
