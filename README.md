# Escáner de Cabeceras de Seguridad HTTP | TAVARDT España

[![Alcance de la Verificación Perimetral](https://img.shields.io/badge/TAVARDT-Diagn%C3%B3stico%20T%C3%A9cnico-5b3cf5.svg)](https://tools.tavardt.com/es/analisis-cabeceras-seguridad/)
Herramienta de auditoría técnica de cabeceras HTTP alineada con el Esquema Nacional de Seguridad (ENS) y el RGPD para plataformas web en España.

Desarrollado y mantenido por el área de ciberseguridad y protección de infraestructuras de **TAVARDT España**.

***

## 1. Alcance de la Verificación Perimetral

Esta utilidad de consola evalúa las directivas de seguridad fundamentales del navegador y del servidor web:

* **Strict-Transport-Security (HSTS):** Fuerza conexiones cifradas bajo HTTPS e impide ataques de degradación e interceptación SSL.
* **Content-Security-Policy (CSP):** Mitiga ataques de inyección de scripts (XSS) y restringe los orígenes autorizados para la carga de recursos.
* **X-Frame-Options:** Previene ataques de clickjacking regulando los permisos de incrustación en frames e iframes.
* **X-Content-Type-Options:** Impide la ejecución indebida de archivos debida a vulnerabilidades de MIME-sniffing.
* **Referrer-Policy:** Protege datos sensibles en URLs de referencia contra fugas hacia dominios de terceros.
* **Permissions-Policy:** Aplica el principio de mínimo privilegio sobre APIs de hardware del navegador (cámara, micrófono y geolocalización).

***

## 2. Guía de Ejecución Rápida

Ejecute la herramienta directamente mediante Python sin necesidad de instalar librerías externas:

```bash
python scanner.py ejemplo.es
```

***

## 3. Herramientas Técnicas Online (España)

Compruebe el estado de seguridad de sus aplicaciones públicas con las herramientas de TAVARDT:

* Comprobador de Cabeceras de Seguridad
* [Validador de Consent Mode v2 y RGPD](https://tools.tavardt.com/es/validador-consent-mode-v2-rgpd/)
* [Verificador DMARC y Correo Electrónico](https://tools.tavardt.com/es/verificador-dmarc-correo/)
* [Escáner de Archivos Expuestos](https://tools.tavardt.com/es/escaneo-archivos-expuestos/)
* [Portal de Diagnóstico Técnico España](https://tools.tavardt.com/es/)

***

## 4. Consultoría y Blindaje Técnico

Para auditorías de certificación ENS, blindaje perimetral y respuesta a incidentes en España, contacte con el equipo de **TAVARDT España**.
