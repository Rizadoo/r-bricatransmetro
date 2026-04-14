class Transaccion:
    def __init__(self, id_trans, cliente, monto, tipoo, saldo_ant, saldo_nue, fecha):
        self.id = id_trans
        self.cliente = cliente
        self.monto = monto
        
        # Atributos de detalle 
        self.tipo = tipoo 
        self.saldo_anterior = saldo_ant
        self.saldo_nuevo = saldo_nue
        self.fecha = fecha

    def definir_detalle(self, tipo_op, saldo_ant, saldo_nue):
     #Este método actualiza la información específica de la operación
        self.tipo = tipo_op
        self.saldo_anterior = saldo_ant
        self.saldo_nuevo = saldo_nue

    def obtener_resumen(self):
    # Este método devuelve un resumen de la transacción, ideal para mostrar en un recibo o historial.
        return {
            "ID Transacción": self.id,
            "Usuario": self.cliente.nombre,
            "Fecha": self.fecha,
            "Operación": self.tipo,
            "Monto": f"${self.monto:,}",
            "Saldo Anterior": f"${self.saldo_anterior:,}",
            "Nuevo Saldo": f"${self.saldo_nuevo:,}"
        }