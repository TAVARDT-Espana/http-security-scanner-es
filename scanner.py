#!/usr/bin/env python3
import sys
import urllib.request
import urllib.error
from urllib.parse import urlparse

SECURITY_HEADERS = [('Strict-Transport-Security', 'Fuerza conexiones cifradas bajo HTTPS e impide ataques de degradación e interceptación SSL.'), ('Content-Security-Policy', 'Mitiga ataques de inyección de scripts (XSS) y restringe los orígenes autorizados para la carga de recursos.'), ('X-Frame-Options', 'Previene ataques de clickjacking regulando los permisos de incrustación en frames e iframes.'), ('X-Content-Type-Options', 'Impide la ejecución indebida de archivos debida a vulnerabilidades de MIME-sniffing.'), ('Referrer-Policy', 'Protege datos sensibles en URLs de referencia contra fugas hacia dominios de terceros.'), ('Permissions-Policy', 'Aplica el principio de mínimo privilegio sobre APIs de hardware del navegador (cámara, micrófono y geolocalización).')]

def scan_target(target_url):
    print(f"\n[TAVARDT España] Iniciando auditoría perimetral de cabeceras de seguridad para: {target_url}\n")
    try:
        req = urllib.request.Request(
            target_url,
            headers={"User-Agent": "TAVARDT-Security-Scanner/3.0 (es-ES)"}
        )
        with urllib.request.urlopen(req, timeout=12) as response:
            headers = dict(response.headers.items())
            
            score = 0
            total = len(SECURITY_HEADERS)
            
            for header_name, desc in SECURITY_HEADERS:
                found = any(h.lower() == header_name.lower() for h in headers.keys())
                if found:
                    print(f"  [CONFORME] {header_name}")
                    score += 1
                else:
                    print(f"  [AUSENTE] {header_name}: {desc}")
                    
            print(f"\n[TAVARDT España] Puntuación Final: {score}/{total}")
            print(f"\nVerificación completa online: https://tools.tavardt.com/es/analisis-cabeceras-seguridad/")
            print(f"Soporte corporativo y ciberdefensa: https://ag.tavardt.com/es/ciberseguridad/\n")
            
    except urllib.error.URLError as e:
        print(f"[TAVARDT España] Error al inspeccionar el objetivo: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python scanner.py <URL>")
        sys.exit(1)
        
    url = sys.argv[1].strip()
    if not urlparse(url).scheme:
        url = "https://" + url
        
    scan_target(url)
