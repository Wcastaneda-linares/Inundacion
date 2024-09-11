# Sistema de Ataque de Inundación HTTP/HTTPS

Este proyecto es una herramienta gráfica de ataque de inundación HTTP/HTTPS construida con Python y Tkinter. La aplicación permite realizar múltiples solicitudes HTTP (GET, POST, PUT) de manera concurrente a una URL objetivo, utilizando hilos para simular un ataque de inundación. La interfaz gráfica moderna facilita la configuración y el inicio/detención del ataque.

## Características:
- Envío de múltiples solicitudes HTTP (GET, POST, PUT) a una URL o IP objetivo.
- Interfaz gráfica moderna utilizando Tkinter y temas de `ttkthemes`.
- Especificación del número de hilos a utilizar en el ataque.
- Imágenes gráficas para representar el inicio y la detención del ataque.

## Tecnologías utilizadas:
- **Python 3.x**: Lenguaje principal utilizado en el proyecto.
- **Tkinter**: Para la interfaz gráfica de usuario (GUI).
- **ttkthemes**: Para agregar temas modernos a la interfaz.
- **requests**: Para enviar solicitudes HTTP (GET, POST, PUT).
- **Pillow**: Para manipular imágenes en la interfaz gráfica.

## Requisitos:
Antes de ejecutar la aplicación, asegúrate de tener instalado Python 3.x y las siguientes dependencias:

- `requests`
- `Pillow`
- `ttkthemes`

## Instalación:

1. **Clona este repositorio**:
     git clone https://github.com/Wcastaneda-linares/Inundacion-HTTP.git
     cd Inundacion-HTTP
2. **Instala las dependencias: Ejecuta el siguiente comando para instalar todas las dependencias necesarias**:
     pip install -r requirements.txt
3. **Ejecuta la aplicación: Una vez instaladas las dependencias, puedes iniciar la aplicación ejecutando**:
     python ataque.py
