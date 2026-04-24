import csv
import getpass
from netmiko import ConnectHandler

print("=== Orquestador de Red Multimarca ===")
# Pedimos la contraseña una sola vez por seguridad para no dejarla en texto plano
password = getpass.getpass("Ingresa la contraseña de los equipos: ")

# Abrimos el inventario normalizado
try:
    with open('equipos.csv', mode='r') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            ip = row['ip']
            marca = row['marca']
            usuario = row['usuario']
            
            print(f"\n--- Conectando a {ip} ({marca}) ---")
            
            # Seleccionamos el script correcto según la marca
            if marca == "cisco_ios":
                archivo_script = "scripts/cisco_vlan.txt"
            elif marca == "huawei":
                archivo_script = "scripts/huawei_base.txt"
            elif marca == "fortinet":
                archivo_script = "scripts/fortinet_policy.txt"
            else:
                print(f"Marca no soportada: {marca}")
                continue

            # Diccionario de conexión para Netmiko
            equipo = {
                'device_type': marca,
                'host': ip,
                'username': usuario,
                'password': password,
            }

            try:
                # 1. Establecer conexión
                conexion = ConnectHandler(**equipo)
                print("Conexión exitosa. Desplegando configuraciones...")
                
                # 2. Inyectar los comandos desde el archivo
                salida = conexion.send_config_from_file(archivo_script)
                print("Resultado del despliegue:")
                print(salida)
                
                # 3. Cerrar conexión
                conexion.disconnect()
                
            except Exception as e:
                print(f"Error al conectar o configurar {ip}: {e}")

except FileNotFoundError:
    print("Error: No se encontró el archivo equipos.csv")