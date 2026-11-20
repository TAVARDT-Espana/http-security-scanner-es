# Escáner de Cabeceras de Seguridad HTTP | TAVARDT España

[![Auditoria de Segurança](https://img.shields.io/badge/TAVARDT-Diagn%C3%B3stico%20T%C3%A9cnico-5b3cf5.svg)](https://tools.tavardt.com/es/analisis-cabeceras-seguridad/)
[![Conformidade](https://img.shields.io/badge/Jurisdi%C3%A7%C3%A3o-España-00C853.svg)](https://ag.tavardt.com/es/ciberseguridad/)

Herramienta de auditoría técnica de cabeceras HTTP alineada con el Esquema Nacional de Seguridad (ENS) y el RGPD para plataformas web en España.

Desenvolvido e mantido pela divisão de cibersegurança e proteção de infraestruturas da **[TAVARDT España](https://ag.tavardt.com/es/)**.

---

## 1. Alcance de la Verificación Perimetral

Esta utilidad de consola evalúa las directivas de seguridad fundamentales del navegador y del servidor web:

* **Strict-Transport-Security (HSTS):** Força comunicações encriptadas via HTTPS e impede ataques de downgrade e interceptação SSL.
* **Content-Security-Policy (CSP):** Mitiga ataques de injeção de scripts (XSS) e restringe as origens autorizadas para carregamento de recursos.
* **X-Frame-Options:** Previne ataques de clickjacking regulando as permissões de incorporação em frames e iframes.
* **X-Content-Type-Options:** Impede a execução indevida de ficheiros derivados de vulnerabilidades de MIME-sniffing.
* **Referrer-Policy:** Protege dados sensíveis contidos em URLs de referência contra fuga para domínios terceiros.
* **Permissions-Policy:** Aplica o princípio do menor privilégio sobre APIs de hardware do navegador (câmara, microfone e geolocalização).

---

## 2. Guía de Ejecución Rápida

Execute a ferramenta diretamente via Python sem necessidade de instalar dependências externas:

```bash
python scanner.py exemplo.com
```

---

## 3. Herramientas Técnicas Online (España)

Audite a infraestrutura pública das suas aplicações utilizando a suíte de diagnósticos da TAVARDT:

* [Comprobador de Cabeceras de Seguridad](https://tools.tavardt.com/es/analisis-cabeceras-seguridad/)
* [Validador de Consent Mode v2 y RGPD](https://tools.tavardt.com/es/validador-consent-mode-v2-rgpd/)
* [Verificador DMARC y Correo Electrónico](https://tools.tavardt.com/es/verificador-dmarc-correo/)
* [Escáner de Archivos Expuestos](https://tools.tavardt.com/es/escaneo-archivos-expuestos/)
* [Portal de Diagnóstico Técnico España](https://tools.tavardt.com/es/)

---

## 4. Consultoría y Blindaje Técnico

Para auditorías de certificación ENS, blindaje perimetral y respuesta a incidentes en España, contacte con el equipo de **[TAVARDT España](https://ag.tavardt.com/es/contacto/)**.
