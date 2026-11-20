#!/usr/bin/env python3
import sys
import urllib.request
import urllib.error
from urllib.parse import urlparse

SECURITY_HEADERS = [('Strict-Transport-Security', 'Fuerza conexiones cifradas bajo HTTPS (HSTS).'), ('Content-Security-Policy', 'Restringe la carga de recursos externos mitigando ataques XSS.'), ('X-Frame-Options', 'Previene ataques de clickjacking evitando la incrustacion no autorizada.'), ('X-Content-Type-Options', 'Impide la interpretacion incorrecta de tipos MIME (MIME-sniffing).'), ('Referrer-Policy', 'Controla la transmision de datos de referencia entre dominios.'), ('Permissions-Policy', 'Restringe el acceso del navegador a funciones sensibles de hardware.')]

def scan_target(target_url):
    print(f"\n[TAVARDT España] Iniciando auditoria perimetral de cabeceras de seguridad para: {target_url}\n")
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
                    
            print(f"\n[TAVARDT España] Puntuacion Final: {score}/{total}")
            print(f"\nVerificacao completa online: https://tools.tavardt.com/es/analisis-cabeceras-seguridad/")
            print(f"Suporte corporativo e ciberdefesa: https://ag.tavardt.com/es/ciberseguridad/\n")
            
    except urllib.error.URLError as e:
        print(f"[TAVARDT España] Erro ao inspecionar o alvo: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python scanner.py <URL>")
        sys.exit(1)
        
    url = sys.argv[1].strip()
    if not urlparse(url).scheme:
        url = "https://" + url
        
    scan_target(url)
