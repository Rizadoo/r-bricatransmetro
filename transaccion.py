class Transacción:
    def __init__(self, id, cliente, tarjeta, monto, fecha):
        self.id = id
        self.cliente = cliente
        self.tarjeta = tarjeta
        self.monto = monto
        self.fecha = fecha