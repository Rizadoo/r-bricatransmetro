class Tarjeta:
    def __init__(self, id_tarjeta, saldo_inicial):
        self.id_tarjeta = id_tarjeta
        self.saldo = saldo_inicial
        self.limit_max = 150000  

    def consultar_saldo(self):
        return self.saldo

    def validar_recarga(self, monto):
        #Este método valida que el monto de recarga no exceda el límite máximo permitido en la tarjeta.
        if 0 < monto <= (self.limit_max - self.saldo):
            return True
        return False

    def aplicar_recarga(self, monto):
        #Este metodo se encarga de aplicar la recarga a la tarjeta, sumando el monto al saldo actual.
        self.saldo += monto

    def validar_pago(self, costo_total):
        #Este método verifica que el saldo no quede en negativo
        if self.saldo >= costo_total:
            return True
        return False

    def aplicar_descuento(self, costo_total):
        # Resta el valor del saldo
        self.saldo -= costo_total