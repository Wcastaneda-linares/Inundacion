#main.py
import tkinter as tk
from tkinter import ttk, messagebox
from ttkthemes import ThemedTk
from modulos import auditoria, escaneo, vulnerabilidades, reporte
import socket
import threading
from PIL import Image, ImageTk
import requests  # Añadido para la simulación de ataques


# Función para realizar la auditoría y mostrar los resultados en la GUI
def realizar_auditoria():
    url = entry_url.get()
    if not url:
        messagebox.showwarning("Advertencia", "Por favor ingrese una URL válida.")
        return

    # Obtener la dirección IP del servidor
    try:
        ip_servidor = socket.gethostbyname(url)
        resultado_ip.set(f"Dirección IP: {ip_servidor}")
    except socket.gaierror:
        resultado_ip.set("Error: No se pudo resolver la dirección IP.")
        ip_servidor = "No se pudo obtener la IP"
        return

    # Auditoría
    resultado_auditoria.set("Realizando auditoría de seguridad...")
    ssl_result = auditoria.verificar_ssl(url)
    endpoints_result = auditoria.analizar_endpoints(url)

    # Escaneo de puertos
    resultado_puertos.set("Realizando escaneo de puertos...")
    host = escaneo.dns_lookup(url)
    if host is None:
        messagebox.showerror("Error", f"No se pudo resolver el host para {url}")
        return
    puertos_abiertos = escaneo.escanear_puertos(host)
    resultado_puertos.set(f"Puertos abiertos en {host}: {puertos_abiertos}")

    # Verificación de vulnerabilidades
    resultado_vulnerabilidades.set("Verificando vulnerabilidades...")
    sql_result = vulnerabilidades.verificar_inyeccion_sql(url)
    xss_result = vulnerabilidades.verificar_xss(url)
    lfi_result = vulnerabilidades.verificar_lfi(url)
    rfi_result = vulnerabilidades.verificar_rfi(url)
    redirect_result = vulnerabilidades.verificar_open_redirect(url)
    command_result = vulnerabilidades.verificar_inyeccion_comandos(url)
    traversal_result = vulnerabilidades.verificar_directory_traversal(url)

    # Generar reporte
    auditoria_resultados = {"SSL": ssl_result, "Endpoints": endpoints_result}
    vulnerabilidades_resultados = [
        sql_result, xss_result, lfi_result, rfi_result,
        redirect_result, command_result, traversal_result
    ]
    reporte.generar_reporte(auditoria_resultados, puertos_abiertos, vulnerabilidades_resultados, ip_servidor)
    
    messagebox.showinfo("Reporte generado", "El reporte ha sido generado correctamente.")
    resultado_vulnerabilidades.set("Auditoría completada. Reporte generado.")

# Función para simular un ataque cuando se presiona el botón
def start_button_click():
    url = entry_url.get()
    if not url:
        messagebox.showwarning("Advertencia", "Por favor ingrese una URL válida.")
        return

    try:
        ip_servidor = socket.gethostbyname(url)
        resultado_ip.set(f"Dirección IP: {ip_servidor}")
        
        # Simular un ataque enviando múltiples solicitudes al servidor
        messagebox.showinfo("Auditoría iniciada", f"Se ha iniciado una auditoría hacia {url}")
        for _ in range(10):  # Simulación básica de 10 solicitudes
            requests.get(url)
        
        messagebox.showinfo("Auditoría Finalizada", "La auditoría ha finalizado.")
        
    except socket.gaierror:
        resultado_ip.set("Error: No se pudo resolver la dirección IP.")
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error: {e}")

# Crear ventana principal con temas profesionales usando ThemedTk
root = ThemedTk(theme="arc")
root.title("Sistema de Auditoría de Seguridad")
root.geometry("600x400")

# Etiqueta de título
label_title = ttk.Label(root, text="Auditoría de Seguridad Web", font=("Helvetica", 18, "bold"))
label_title.pack(pady=10)

# Entrada de URL
entry_url = ttk.Entry(root, width=50, font=("Helvetica", 14))
entry_url.pack(pady=10)
entry_url.insert(0, "Ingrese la URL a auditar")


# Botón para iniciar el ataque con ícono
icon_start = Image.open("imagenes/start_icon.png")
icon_start = icon_start.resize((40, 40), Image.Resampling.LANCZOS)
icon_start = ImageTk.PhotoImage(icon_start)
button_auditar = ttk.Button(root, text="Iniciar Auditoría", image=icon_start, compound=tk.LEFT, command=realizar_auditoria)
button_auditar.pack(pady=20)

# Variables para resultados
resultado_ip = tk.StringVar()
resultado_auditoria = tk.StringVar()
resultado_puertos = tk.StringVar()
resultado_vulnerabilidades = tk.StringVar()

# Etiquetas para mostrar resultados
label_ip = ttk.Label(root, textvariable=resultado_ip)
label_ip.pack(pady=5)

label_auditoria = ttk.Label(root, textvariable=resultado_auditoria)
label_auditoria.pack(pady=5)

label_puertos = ttk.Label(root, textvariable=resultado_puertos)
label_puertos.pack(pady=5)

label_vulnerabilidades = ttk.Label(root, textvariable=resultado_vulnerabilidades)
label_vulnerabilidades.pack(pady=5)

# Ejecutar la interfaz gráfica
root.mainloop()
