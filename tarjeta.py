class Tarjeta:
    def __init__(self, id_tarjeta, saldo_inicial):
        # Atributos de instancia
        self.id_tarjeta = id_tarjeta
        self.saldo = saldo_inicial
        self.limit_max = 150000  # Ahora definido correctamente dentro del constructor

    def consultar_saldo(self):
        return self.saldo

    def validar_recarga(self, monto):
        # Verifica que no sea negativo y que no supere el tope de 150k
        if 0 < monto <= (self.limit_max - self.saldo):
            return True
        return False

    def aplicar_recarga(self, monto):
        # Suma el saldo si la validación es exitosa
        self.saldo += monto

    def validar_pago(self, costo_total):
        # Verifica que el saldo no quede en negativo
        if self.saldo >= costo_total:
            return True
        return False

    def aplicar_descuento(self, costo_total):
        # Resta el valor del saldo
        self.saldo -= costo_total