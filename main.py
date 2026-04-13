from cliente import Cliente
from tarjeta import Tarjeta
from transaccion import Transaccion
from ruta import Ruta
from bus import Bus
from estacion import Estacion
from parada import Parada

def main():
    #Configuración inicial del sistema Transmetro
    estacion_norte = Estacion("E01", "Joe Arroyo", "Norte")
    parada_unorte = Parada("P01", "Uninorte", "Corredor Univ.")
    parada_a74 = Parada("P02", "Avenida 7-4", "Atlántico.")
    parada_a81 = Parada("P03", "Avenida 8-1", "Villa Andalucía.")
    
    r_troncal = Ruta("R10", "R10 Joe Arroyo - Portal", "Troncal", 3700)
    r_troncal.establecer_promedio(5)

    r_troncal2 = Ruta("S10", "S10 Joe Arroyo - Portal", "Troncal", 3700)
    r_troncal2.establecer_promedio(7)    

    r_troncal3 =Ruta("B10", "B1 Joe Arroyo - Portal", "Troncal", 3700)
    r_troncal3.establecer_promedio(9)

    r_alimentador = Ruta("U30", "Universidades", "Alimentador", 3700)
    r_alimentador.establecer_promedio(12)

    r_alimentador2 = Ruta("A7-4", "Clle 74, Cra 46, Avenida Murillo, Clle 70c, Estación Atlantico", "Alimentador", 3700)
    r_alimentador2.establecer_promedio(15)

    r_alimentador3 = Ruta("A8-1", "Cra 46, Clle 82, Villa Andalucía, Cra 51B, Estación Miramar", "Alimentador", 3700)
    r_alimentador3.establecer_promedio(18)

    # Vinculación de rutas y paradas a la estación
    estacion_norte.vincular_ruta(r_troncal)
    estacion_norte.vincular_ruta(r_troncal2)
    estacion_norte.vincular_ruta(r_troncal3)
    estacion_norte.vincular_ruta(r_alimentador)
    estacion_norte.vincular_ruta(r_alimentador2)
    estacion_norte.vincular_ruta(r_alimentador3)
    estacion_norte.vincular_parada(parada_unorte)
    estacion_norte.vincular_parada(parada_a74)
    estacion_norte.vincular_parada(parada_a81)
    
    lista_clientes = []

    print("=== BIENVENIDO AL SISTEMA TRANSMETRO ===")

    while True:
        print("\n--- INICIO DE SESIÓN ---")
        id_ingresado = input("Ingrese su número de cédula (o 'salir'): ")
        
        if id_ingresado.lower() == 'salir':
            break
        
        if not id_ingresado.isdigit() or int(id_ingresado) <= 0:
            print("Número de cédula inválido. Intente nuevamente.")
            continue
        
        # Buscar cliente
        cliente_actual = next((c for c in lista_clientes if c.id == id_ingresado), None)

        if cliente_actual is None:
            print("Usuario no encontrado. Registrando...")
            nombre = input("Nombre completo: ")

            es_estudiante = input("¿Es estudiante? (s/n): ").lower()
            tipo = "Estudiante" if es_estudiante == 's' else "General"
            nueva_tarjeta = Tarjeta(id_ingresado, 0)
            cliente_actual = Cliente(id_ingresado, nombre, tipo, nueva_tarjeta)
            lista_clientes.append(cliente_actual)
            print(f"Bienvenido {nombre}, Quedaste registrado como {tipo}.")

        #Menu principal para el cliente
        while True:
            print(f"Usuario: {cliente_actual.nombre} / Saldo: ${cliente_actual.tarjeta.saldo}")
            print("1. Recargar Tarjeta")
            print("2. Ver Rutas y Promedios")
            print("3. Pagar Pasaje")
            print("4. Cerrar Sesión")
            
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                monto = int(input("Monto a recargar: "))
                if cliente_actual.tarjeta.validar_recarga(monto):
                    saldo_ant = cliente_actual.tarjeta.saldo
                    cliente_actual.tarjeta.aplicar_recarga(monto)
                    print(f"¡Recarga exitosa! Nuevo saldo: ${cliente_actual.tarjeta.saldo}")
                else:
                    print("Error: Monto inválido o supera el límite de $150.000 COP.")

            elif opcion == "2":
                estacion_norte.mostrar_tablero()

            elif opcion == "3":
                precio_pasaje = 3700
                precio_final = precio_pasaje
                if cliente_actual.tipo_cliente == "Estudiante":
                    precio_final = precio_pasaje * 0.5  # 50% de descuento para estudiantes
                    
                if cliente_actual.tarjeta.validar_pago(precio_final):
                    cliente_actual.tarjeta.aplicar_descuento(precio_final)
                    print(f"Pago exitoso. Pasaje pagado: ${precio_final}. Saldo restante: ${cliente_actual.tarjeta.saldo}")
                else:
                    print("Saldo insuficiente para pagar el pasaje. Por favor recargue su tarjeta.")

            elif opcion == "4":
                break

if __name__ == "__main__":
    main()