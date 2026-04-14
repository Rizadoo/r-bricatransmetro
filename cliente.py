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
        
        
