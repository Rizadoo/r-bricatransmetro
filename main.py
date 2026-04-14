import datetime
from cliente import Cliente
from tarjeta import Tarjeta
from transaccion import Transaccion
from bus import Bus
from estacion import Estacion
from ruta import Ruta
from parada import Parada

def validar_nombre(nombre):
    """Verifica que el nombre no tenga números y sea mayor a 2 letras"""
    return nombre.replace(" ", "").isalpha() and len(nombre.strip()) > 2

def main():
    # List
    historial_transacciones = []
    lista_clientes = []

    # Estación Principal
    estacion_retorno = Estacion("E-RET", "Joe Arroyo", "Norte")

    #Rutas troncales
    r_r10 = Ruta("R10", "Joe Arroyo - Portal", "Troncal", 3700)
    r_s10 = Ruta("S10", "Portal - Joe Arroyo", "Troncal", 3700)
    
    #Rutas alimentadoras
    r_a83 = Ruta("A8-3", "Prado - Joe Arroyo", "Alimentador", 3700)
    r_a93 = Ruta("A9-3", "Buenavista - Joe Arroyo", "Alimentador", 3700)
    r_u30 = Ruta("U30", "Universidades - Joe Arroyo", "Alimentador", 3700)

    #Registro de paradas
    p1 = Parada("P-01", "Calle 72", "Clle 72 con Cra 46")
    p2 = Parada("P-02", "Parque Central", "Cra 44")
    p3 = Parada("P-03", "C.C. Buenavista", "Cra 53")
    p4 = Parada("P-04", "U. del Norte", "Cra 51B")

    # Vinculamos rutas a la estación
    for r in [r_r10, r_s10, r_a83, r_a93, r_u30]:
        estacion_retorno.vincular_ruta(r)

    # Buses de ejemplo
    bus_troncal = Bus("TM-100", 160, "Articulado", "Troncal Olaya Herrera")
    bus_alimentador = Bus("AL-200", 50, "Padron", "Zonas Alimentadoras")

    print("=== SISTEMA TRANSMETRO BARRANQUILLA ===")

    while True:
        
        print("=== CONTROL DE ACCESO ===")
        id_ingresado = input("Cédula (10 dígitos) o 'salir': ").strip()

        if id_ingresado.lower() == 'salir': break

        if not id_ingresado.isdigit() or len(id_ingresado) != 10:
            print("Error: Cédula inválida (debe tener 10 números).")
            continue

        cliente_actual = next((c for c in lista_clientes if c.id == id_ingresado), None)

        if cliente_actual is None:
            print("Usuario no registrado.")
            while True:
                nombre = input("Nombre completo: ").strip()
                if validar_nombre(nombre): break
                print("Error: Nombre no válido (solo letras).")

            es_estudiante = input("¿Aplica descuento de estudiante? (s/n): ").lower()
            tipo = "Estudiante" if es_estudiante == 's' else "General"
            
            nueva_t = Tarjeta(f"T-{id_ingresado}")
            cliente_actual = Cliente(id_ingresado, nombre, tipo, nueva_t)
            lista_clientes.append(cliente_actual)
            print(f"Bienvenido {nombre} Registrado como {tipo}.")

        #Submenú para clientes registrados
        while True:
            saldo_act = cliente_actual.tarjeta.consultar_saldo()
            print(f"{cliente_actual.nombre.upper()} / Saldo: ${saldo_act:,}")
            print("-" * 40)
            print("1. Recargar Tarjeta")
            print("2. Consultar Tablero de Rutas")
            print("3. Validar Pasaje (Viajar)")
            print("4. Cerrar Sesión")
            
            opcion = input("Seleccione: ")

            if opcion == "1":
                try:
                    monto = int(input("Monto a recargar: "))
                    if cliente_actual.tarjeta.validar_recarga(monto):
                        saldo_ant = cliente_actual.tarjeta.consultar_saldo()
                        cliente_actual.tarjeta.aplicar_recarga(monto)
                        
                        t = Transaccion(f"REC-{len(historial_transacciones)+1}", 
                                        cliente_actual, monto, "Recarga", 
                                        saldo_ant, cliente_actual.tarjeta.consultar_saldo(), 
                                        datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))
                        
                        t.definir_detalle("Recarga", saldo_ant, cliente_actual.tarjeta.consultar_saldo())
                        historial_transacciones.append(t)
                        
                        resumen = t.obtener_resumen()
                        print("=== RECIBO DE RECARGA ===")
                        for k, v in resumen.items(): print(f"{k}: {v}")
                    else:
                        print("Error: Límite de $150.000 excedido.")
                except ValueError:
                    print("Error: Ingrese solo números.")

            elif opcion == "2":
                estacion_retorno.mostrar_tablero()

            elif opcion == "3":
                tarifa = 1980 if cliente_actual.tipo_cliente == "Estudiante" else 3700

                if cliente_actual.tarjeta.validar_pago(tarifa):
                    saldo_ant = cliente_actual.tarjeta.consultar_saldo()
                    cliente_actual.tarjeta.aplicar_descuento(tarifa)
                    
                    v = Transaccion(f"VIA-{len(historial_transacciones)+1}", 
                                    cliente_actual, tarifa, "Viaje", 
                                    saldo_ant, cliente_actual.tarjeta.consultar_saldo(), 
                                    datetime.datetime.now().strftime("%H:%M"))
                    historial_transacciones.append(v)
                    
                    print(f"VIAJE AUTORIZADO (Tarifa: ${tarifa:,})")
                    # Lógica visual de asignación de bus
                    print(f"Asignado a: {bus_troncal.placa if tarifa == 3700 else bus_alimentador.placa}")
                else:
                    print(f"Saldo insuficiente. Necesitas ${tarifa:,}.")

            elif opcion == "4":
                break

if __name__ == "__main__":
    main()