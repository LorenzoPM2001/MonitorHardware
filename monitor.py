import psutil
import time
import os
import GPUtil
import wmi

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

# Inicializar conexión con los sensores de Windows
# Nota: Esto a veces requiere ejecutar VS Code como Administrador
try:
    w = wmi.WMI(namespace="root\\wmi")
except Exception as e:
    w = None

print("Iniciando Monitor de Hardware Avanzado...")

try:
    while True:
        limpiar_pantalla()
        print("=== MONITOR DE HARDWARE (Win 11) ===")
        
        # --- 1. DATOS DE CPU Y RAM ---
        cpu_usage = psutil.cpu_percent(interval=1)
        ram = psutil.virtual_memory()
        print(f"Uso de CPU:  {cpu_usage}%")
        print(f"RAM Usada:   {ram.percent}% ({ram.used / (1024**3):.2f} GB / {ram.total / (1024**3):.2f} GB)")

        # --- 2. TEMPERATURA DE CPU (Vía WMI) ---
        if w:
            try:
                temperaturas = w.MSAcpi_ThermalZoneTemperature()
                if len(temperaturas) > 0:
                    # Windows devuelve la temp en décimas de Kelvin. Fórmula: (K / 10) - 273.15
                    temp_celsius = (temperaturas[0].CurrentTemperature / 10.0) - 273.15
                    print(f"Temp. CPU:   {temp_celsius:.1f} °C")
            except Exception:
                print("Temp. CPU:   [Sensor bloqueado por la placa base/driver]")
        else:
             print("Temp. CPU:   [Error al conectar con WMI]")

        print("-" * 36)

        # --- 3. DATOS DE LA TARJETA GRÁFICA (GPU) ---
        gpus = GPUtil.getGPUs()
        if not gpus:
            print("GPU:         [No se detectó gráfica NVIDIA]")
        else:
            for gpu in gpus:
                print(f"GPU Nombre:  {gpu.name}")
                print(f"GPU Uso:     {gpu.load * 100:.1f}%")
                print(f"GPU Temp:    {gpu.temperature} °C")
                print(f"GPU VRAM:    {gpu.memoryUsed} MB / {gpu.memoryTotal} MB")

        print("====================================")
        print("Pulsa Ctrl+C para salir.")
        
        time.sleep(1)
        
except KeyboardInterrupt:
    print("\nMonitor detenido.")