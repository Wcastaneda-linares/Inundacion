#auditoria.py
import socket
import ssl
import requests

def verificar_ssl(url):
    # Asegurarse de que la URL tiene el esquema correcto
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "https://" + url  # O "http://" si es necesario

    try:
        # Extraer solo el nombre de host
        hostname = url.replace("https://", "").replace("http://", "").split('/')[0]

        # Establecer una conexión SSL
        context = ssl.create_default_context()
        with socket.create_connection((hostname, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                ssl_info = ssock.getpeercert()  # Obtener el certificado SSL
                return ssl_info
    except Exception as e:
        return f"Error al verificar el certificado SSL: {e}"

def analizar_endpoints(url):
    # Asegurarse de que la URL tiene el esquema correcto
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "https://" + url  # Cambiar a "http://" si es necesario

    # Lista de endpoints comunes a verificar
    endpoints_comunes = ["/admin", "/login", "/test", "/backup"]
    resultados = {}

    for endpoint in endpoints_comunes:
        try:
            full_url = url + endpoint
            respuesta = requests.get(full_url)
            resultados[endpoint] = f"{full_url}, estado: {respuesta.status_code}"
        except requests.exceptions.RequestException as e:
            resultados[endpoint] = f"Error al intentar acceder a {full_url}: {e}"

    return resultados
