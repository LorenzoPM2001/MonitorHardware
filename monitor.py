import psutil
import time
import os
import wmi

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

print("Iniciando Monitor de Hardware (Edición AMD Ryzen/Radeon)...")

# Conectar con WMI de Windows
try:
    w = wmi.WMI()
    w_sensores = wmi.WMI(namespace="root\\wmi")
except Exception:
    w = None
    w_sensores = None

try:
    while True:
        limpiar_pantalla()
        print("=== MONITOR DE HARDWARE (Win 11 - Rama AMD) ===")
        
        # --- 1. DATOS DE CPU (Ryzen) Y RAM ---
        cpu_usage = psutil.cpu_percent(interval=1)
        ram = psutil.virtual_memory()
        print(f"Procesador:  Uso: {cpu_usage}%")
        print(f"Memoria RAM: {ram.percent}% ({ram.used / (1024**3):.2f} GB / {ram.total / (1024**3):.2f} GB)")

        # Intentar leer temperatura (suele estar bloqueado por drivers de AMD en Windows)
        if w_sensores:
            try:
                temperaturas = w_sensores.MSAcpi_ThermalZoneTemperature()
                if len(temperaturas) > 0:
                    temp_celsius = (temperaturas[0].CurrentTemperature / 10.0) - 273.15
                    print(f"Temp. CPU:   {temp_celsius:.1f} °C")
            except Exception:
                pass # Silenciamos el error si AMD bloquea el sensor
                
        print("-" * 42)

        # --- 2. DATOS DE LA TARJETA GRÁFICA (AMD Vía WMI) ---
        if w:
            # Win32_VideoController lee la info de la gráfica instalada
            tarjetas_graficas = w.Win32_VideoController()
            for gpu in tarjetas_graficas:
                print(f"GPU Nombre:  {gpu.Name}")
                
                # Convertir la memoria de bytes a Megabytes
                if gpu.AdapterRAM:
                    vram_mb = int(gpu.AdapterRAM) / (1024**2)
                    print(f"GPU VRAM:    {vram_mb:.0f} MB")
                
                print(f"GPU Driver:  {gpu.DriverVersion}")
        else:
            print("GPU: [No se pudo conectar con Windows WMI]")

        print("===============================================")
        print("Pulsa Ctrl+C para salir.")
        
        time.sleep(1)
        
except KeyboardInterrupt:
    print("\nMonitor detenido.")