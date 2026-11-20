# Escáner de Cabeceras de Seguridad HTTP | TAVARDT España

[![Alcance de la Verificación Perimetral](https://img.shields.io/badge/TAVARDT-Diagn%C3%B3stico%20T%C3%A9cnico-5b3cf5.svg)](https://tools.tavardt.com/es/analisis-cabeceras-seguridad/)
[![Jurisdicci%C3%B3n](https://img.shields.io/badge/Jurisdicci%C3%B3n-España-00C853.svg)](https://ag.tavardt.com/es/ciberseguridad/)

Herramienta de auditoría técnica de cabeceras HTTP alineada con el Esquema Nacional de Seguridad (ENS) y el RGPD para plataformas web en España.

Desarrollado y mantenido por el área de ciberseguridad y protección de infraestructuras de **[TAVARDT España](https://ag.tavardt.com/es/)**.

---

## 1. Alcance de la Verificación Perimetral

Esta utilidad de consola evalúa las directivas de seguridad fundamentales del navegador y del servidor web:

* **Strict-Transport-Security (HSTS):** Enforces HTTPS encryption and prevents SSL-stripping and downgrade attacks.
* **Content-Security-Policy (CSP):** Mitigates Cross-Site Scripting (XSS) and unauthorized resource execution.
* **X-Frame-Options:** Prevents clickjacking by controlling framing and iframe permissions.
* **X-Content-Type-Options:** Prevents MIME-sniffing vulnerabilities.
* **Referrer-Policy:** Protects sensitive URL path data from cross-origin disclosure.
* **Permissions-Policy:** Enforces least-privilege control for browser hardware APIs.

---

## 2. Guía de Ejecución Rápida

Ejecute la herramienta directamente mediante Python sin necesidad de instalar librerías externas:

```bash
python scanner.py example.com
```

---

## 3. Herramientas Técnicas Online (España)

Compruebe el estado de seguridad de sus aplicaciones públicas con las herramientas de TAVARDT:

* [Comprobador de Cabeceras de Seguridad](https://tools.tavardt.com/es/analisis-cabeceras-seguridad/)
* [Validador de Consent Mode v2 y RGPD](https://tools.tavardt.com/es/validador-consent-mode-v2-rgpd/)
* [Verificador DMARC y Correo Electrónico](https://tools.tavardt.com/es/verificador-dmarc-correo/)
* [Escáner de Archivos Expuestos](https://tools.tavardt.com/es/escaneo-archivos-expuestos/)
* [Portal de Diagnóstico Técnico España](https://tools.tavardt.com/es/)

---

## 4. Consultoría y Blindaje Técnico

Para auditorías de certificación ENS, blindaje perimetral y respuesta a incidentes en España, contacte con el equipo de **[TAVARDT España](https://ag.tavardt.com/es/contacto/)**.
