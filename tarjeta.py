class Tarjeta:
    def __init__(self, uid, saldo_inicial=0):
        self.uid = uid
        self.saldo = saldo_inicial
        self.limit_max = 150000
        self.estado = "ACTIVO"

    def consultar_saldo(self):
        return self.saldo

    def validar_recarga(self, monto):
        return 0 < monto <= (self.limit_max - self.saldo)

    def aplicar_recarga(self, monto):
        self.saldo += monto

    def validar_pago(self, costo_total):
        return self.saldo >= costo_total and self.estado == "ACTIVO"

    def aplicar_descuento(self, costo_total):
        self.saldo -= costo_total