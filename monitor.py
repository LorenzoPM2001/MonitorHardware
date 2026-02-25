import psutil
import time
import os

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

print("Iniciando Monitor de Hardware...")

try:
    while True:
        limpiar_pantalla()
        # Leer datos físicos
        cpu_usage = psutil.cpu_percent(interval=1)
        ram = psutil.virtual_memory()
        
        # Mostrar en pantalla
        print("=== MONITOR DE HARDWARE (Win 11) ===")
        print(f"Uso de CPU: {cpu_usage}%")
        print(f"RAM Total:  {ram.total / (1024**3):.2f} GB")
        print(f"RAM Usada:  {ram.percent}%")
        print("====================================")
        print("Pulsa Ctrl+C para salir.")
        
        time.sleep(1) # Refrescar cada 1 segundo
except KeyboardInterrupt:
    print("\nMonitor detenido.")