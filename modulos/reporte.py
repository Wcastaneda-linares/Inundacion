#reporte.py
def formatear_ssl_info(ssl_info):
    # Formatear el certificado SSL para hacerlo más legible
    subject = ssl_info.get('subject', [])[0][0][1]
    issuer = ', '.join([f"{field[0][0]}: {field[0][1]}" for field in ssl_info.get('issuer', [])])
    valid_from = ssl_info.get('notBefore')
    valid_to = ssl_info.get('notAfter')
    san = ', '.join([alt[1] for alt in ssl_info.get('subjectAltName', [])])

    return f"""
Certificado SSL:
    - Nombre Común: {subject}
    - Emisor: {issuer}
    - Válido desde: {valid_from}
    - Válido hasta: {valid_to}
    - Dominios Alternativos (SANs): {san}
"""

def formatear_endpoints(endpoints):
    # Formatear los resultados de los endpoints para hacerlos más legibles
    resultado = "Verificación de Endpoints:\n"
    for endpoint, estado in endpoints.items():
        resultado += f"    {endpoint}: {estado}\n"
    return resultado

def generar_reporte(auditoria_resultados, puertos_abiertos, vulnerabilidades_resultados, ip_servidor):
    # Formatear la información del certificado SSL y los endpoints
    ssl_info_formateado = formatear_ssl_info(auditoria_resultados['SSL'])
    endpoints_formateados = formatear_endpoints(auditoria_resultados['Endpoints'])

    with open("reporte.txt", "w") as archivo:
        archivo.write("=== Resultados de Auditoría ===\n")
        archivo.write(f"Dirección IP del servidor: {ip_servidor}\n")
        archivo.write(f"{ssl_info_formateado}\n")
        archivo.write(f"{endpoints_formateados}\n")

        archivo.write("=== Escaneo de Puertos ===\n")
        archivo.write(f"Puertos abiertos: {', '.join(map(str, puertos_abiertos))}\n\n")

        archivo.write("=== Resultados de Vulnerabilidades ===\n")
        for resultado in vulnerabilidades_resultados:
            archivo.write(f"{resultado}\n")

