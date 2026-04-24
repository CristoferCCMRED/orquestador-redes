import csv
import getpass
from netmiko import ConnectHandler

print("=== Orquestador de Red Multimarca Optimizado ===")
password = getpass.getpass("Ingresa la contraseña de los equipos: ")

try:
    with open('equipos.csv', mode='r') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            ip = row['ip']
            marca = row['marca']
            usuario = row['usuario']
            
            print(f"\n--- Iniciando proceso para {ip} ({marca}) ---")
            
            # 1. Definir script y comando de VERIFICACIÓN por marca
            if marca == "cisco_ios":
                archivo_script = "scripts/cisco_vlan.txt"
                comando_verificacion = "show vlan brief" # Verifica si se creó la VLAN 10
            elif marca == "huawei":
                archivo_script = "scripts/huawei_base.txt"
                comando_verificacion = "display vlan" # Verifica si se creó la VLAN 20
            elif marca == "fortinet":
                archivo_script = "scripts/fortinet_policy.txt"
                comando_verificacion = "show firewall policy" # Verifica las políticas creadas
            else:
                print(f"Marca no soportada: {marca}")
                continue

            # Diccionario de conexión
            equipo = {
                'device_type': marca,
                'host': ip,
                'username': usuario,
                'password': password,
            }

            try:
                # 2. Conectar e Inyectar Configuración
                conexion = ConnectHandler(**equipo)
                print(f"[{ip}] Conectado. Desplegando configuraciones...")
                salida_config = conexion.send_config_from_file(archivo_script)
                
                # 3. Verificación Automática (Troubleshooting)
                print(f"[{ip}] Ejecutando verificación: {comando_verificacion}...")
                salida_verificacion = conexion.send_command(comando_verificacion)
                
                # 4. Generar Reporte/Evidencia en archivo de texto
                nombre_log = f"log_evidencia_{ip}.txt"
                with open(nombre_log, "w") as log_file:
                    log_file.write(f"=== REPORTE DE DESPLIEGUE: {ip} ===\n\n")
                    log_file.write("--- 1. COMANDOS INYECTADOS ---\n")
                    log_file.write(salida_config + "\n\n")
                    log_file.write(f"--- 2. RESULTADO DE VERIFICACIÓN ({comando_verificacion}) ---\n")
                    log_file.write(salida_verificacion + "\n")
                
                print(f"[{ip}] ✅ Éxito. Evidencia guardada en {nombre_log}")
                conexion.disconnect()
                
            except Exception as e:
                print(f"[{ip}] ❌ Error en la conexión o ejecución: {e}")

except FileNotFoundError:
    print("Error: No se encontró el archivo equipos.csv")