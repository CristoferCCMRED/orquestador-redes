"# orquestador-redes" 
# Orquestador de Red Multimarca (Cisco, Huawei, Fortinet)

Este proyecto transforma la gestión manual de dispositivos en un flujo de trabajo de Infraestructura como Código (IaC). Utiliza un repositorio centralizado en GitHub como la Fuente Única de Verdad (source of truth) para garantizar la trazabilidad y reversión instantánea de configuraciones en toda la red empresarial.

## Arquitectura de la Solución
La herramienta opera bajo un modelo de tres pilares fundamentales:
1. **El Inventario**: Datos planos en formato CSV/Excel que contienen el direccionamiento y credenciales de los equipos.
2. **El Orquestador**: Motor en Python que utiliza la librería Netmiko para traducir la lógica a comandos físicos.
3. **La Red Física**: Equipos reales donde se inyectan las configuraciones de forma automatizada.

## Requisitos Previos
* Python 3.x instalado.
* Librería Netmiko: Instalable mediante `pip install netmiko`.
* Acceso a Red: Conectividad vía Telnet (entorno de laboratorio) o SSH hacia los dispositivos.

## Estructura del Repositorio
Siguiendo las buenas prácticas de organización:
* `main.py`: Script principal del orquestador.
* `equipos.csv`: Inventario de dispositivos con sus tipos (cisco_ios, huawei, fortinet).
* `/scripts`: Carpeta que contiene las configuraciones base por fabricante.

## Flujo de Trabajo (Workflow)
Para asegurar la red, implementamos un ciclo de vida continuo:
1. **Escribir**: Se crea el código de configuración localmente.
2. **Versionar**: Se realiza un Commit con notas explicativas de los cambios.
3. **Empujar**: Se hace un Push de las configuraciones a GitHub para respaldo y visibilidad.
4. **Desplegar**: El script de Python inyecta los comandos en la red.
5. **Verificar**: Se realiza un Troubleshooting automático para confirmar el estado final de las interfaces.

# Orquestador de Red Multimarca (Cisco, Huawei, Fortinet)

Este proyecto transforma la gestión manual de dispositivos en un flujo de trabajo de Infraestructura como Código (IaC). Utiliza un repositorio centralizado en GitHub como la Fuente Única de Verdad (source of truth) para garantizar la trazabilidad y reversión instantánea de configuraciones en toda la red empresarial.

## 🚀 Descarga e Instalación

### Requisitos Previos (Todos los Sitemas)
1. **Python 3.x**: Descargable desde [python.org](https://www.python.org/).
2. **Git**: Instalado en su sistema para clonar el repositorio.

---

### 🪟 Windows (PowerShell / CMD)
1. **Descargar el proyecto**:
   ```cmd
   git clone [https://github.com/CristoferCCMRED/orquestador-redes.git](https://github.com/CristoferCCMRED/orquestador-redes.git)
   cd orquestador-redes

   Instalar dependencias:

DOS
pip install netmiko
🐧 Linux (Ubuntu/Debian)
Instalar herramientas base:

Bash
sudo apt update
sudo apt install git python3 python3-pip -y
Descargar el proyecto:

Bash
git clone [https://github.com/CristoferCCMRED/orquestador-redes.git](https://github.com/CristoferCCMRED/orquestador-redes.git)
cd orquestador-redes
Instalar dependencias:

Bash
pip3 install netmiko
🍎 macOS
Descargar el proyecto:

Bash
git clone [https://github.com/CristoferCCMRED/orquestador-redes.git](https://github.com/CristoferCCMRED/orquestador-redes.git)
cd orquestador-redes
Instalar dependencias:

Bash
pip3 install netmiko
🛠️ Ejecución Paso a Paso
Una vez instalado, siga estos pasos para ejecutar el orquestador:

Configurar Inventario: Edite el archivo equipos.csv con las IPs y credenciales de su laboratorio.

Preparar Scripts: Asegúrese de que los archivos en la carpeta /scripts contengan los comandos deseados.

Lanzar el Orquestador:

En Windows: python main.py

En Linux/Mac: python3 main.py

Autenticación: El sistema solicitará la contraseña de los equipos por seguridad (no se mostrará al escribir).

Verificación: Al finalizar, revise los archivos log_evidencia_IP.txt generados en la carpeta raíz para confirmar los cambios.

---
**Ingeniero a cargo:** Cristofer Buitrago Cocoma
**Institución:** Ucompensar
**Fecha:** 2026
