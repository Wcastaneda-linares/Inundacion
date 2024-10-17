#escaneo.py
import socket

# Función para escanear puertos
def escanear_puertos(host):
    puertos_comunes = [80, 443, 21, 22, 23, 25, 53, 110, 143, 445, 3389]  # Lista de puertos comunes
    puertos_abiertos = []
    
    for puerto in puertos_comunes:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.1)  # Timeout más corto para evitar demoras largas
        resultado = sock.connect_ex((host, puerto))
        if resultado == 0:
            puertos_abiertos.append(puerto)
            print(f"Puerto {puerto} está abierto.")
        else:
            print(f"Puerto {puerto} está cerrado o filtrado.")
        sock.close()
    
    return puertos_abiertos

# Función para hacer una consulta DNS (resuelve el nombre de host en una dirección IP)
def dns_lookup(host):
    try:
        return socket.gethostbyname(host)
    except socket.gaierror as e:
        print(f"Error de DNS al resolver el host {host}: {e}")
        return None
