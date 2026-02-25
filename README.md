# 🖥️ Monitor de Hardware para Windows 11

Un monitor de sistema ligero y en tiempo real escrito en Python. Este proyecto lee los datos físicos del ordenador (uso y temperaturas de CPU, RAM y GPU) comunicándose directamente con la API interna de Windows (WMI) y librerías de hardware.

## ✨ Características Principales
* **Monitorización de CPU:** Carga de procesamiento en tiempo real.
* **Monitorización de Memoria (RAM):** Capacidad total, uso actual y porcentaje.
* **Monitorización de GPU:** Detección de tarjeta gráfica, uso de VRAM y carga de procesamiento.
* **Temperaturas:** Lectura de sensores térmicos (sujeto a la compatibilidad de la placa base).

## 🔀 Arquitectura de Ramas (Branches)
Este proyecto está optimizado para diferentes configuraciones de hardware. Por favor, selecciona la rama correspondiente a tu equipo:

* **`main`**: Versión básica genérica (solo CPU y RAM).
* **`soporte-nvidia`**: Optimizada para gráficas NVIDIA utilizando la librería `GPUtil`.
* **`soporte-amd`**: Optimizada para procesadores Ryzen y gráficas Radeon utilizando WMI de Windows.

## 🛠️ Requisitos Previos
* Windows 10 o Windows 11.
* [Python 3.x](https://www.python.org/downloads/) instalado.

## 🚀 Instalación y Uso

1. **Clona el repositorio:**
   ```bash
   git clone [https://github.com/LorenzoPM2001/MonitorHardware.git](https://github.com/LorenzoPM2001/MonitorHardware.git)
   cd MonitorHardware