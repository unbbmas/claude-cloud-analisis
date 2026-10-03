# Proceso completo: de datos de empresa a análisis de inversión

## Requisito previo
Este flujo necesita **dos conectores activados en el mismo chat**:
- **Filesystem** → crea carpetas y guarda ficheros en `E:\mis documentos\fondos\ideas\claude\`
- **Claude en Chrome** → navega TIKR y descarga PDFs/Excel/transcripciones

Si los usas en chats separados, los ficheros de TIKR caerán en tu carpeta de Descargas en vez de en la carpeta del proyecto, y tendrás que moverlos a mano. Por eso, **lo más simple es hacer todo el proceso en un único chat** (puede ser este mismo, o cualquier chat nuevo, siempre que tenga ambos conectores activos — no hace falta que sea siempre el mismo).

---

## Paso 1 — Dar los datos de la empresa
En cualquier chat de Claude (con Filesystem activado), escribes:
- Empresa
- Ticker
- Mercado/Bolsa
- País principal de operación
- Web corporativa (IR)
- Moneda de las cuentas
- (Opcional) rango de años de informes anuales — por defecto, últimos 6

**Qué hace Claude:** crea la carpeta `E:\mis documentos\fondos\ideas\claude\{Empresa}_{Ticker}\` y guarda dentro el `prompt.md` con la plantilla de análisis ya rellenada con esos datos.

## Paso 2 — Descarga automática desde TIKR
En el **mismo chat**, pides que ejecute la investigación en TIKR para esa empresa (como hace el launcher `tikr_research_launcher.html`).

**Qué hace Claude:**
1. Navega TIKR vía Claude en Chrome (requiere que ya tengas sesión iniciada en TIKR en tu navegador).
2. Descarga los informes anuales (PDF) de los últimos N años.
3. Descarga/combina las transcripciones de earnings calls disponibles en un único PDF.
4. Construye el Excel de cuentas (`cuentas_{TICKER}.xlsx`) con P&L, Balance y Cash Flow.
5. **En vez de dejarlo en Descargas**, guarda todo directamente en la carpeta ya creada en el Paso 1 (`E:\mis documentos\fondos\ideas\claude\{Empresa}_{Ticker}\`) usando el conector Filesystem.

> Si en algún momento usas el launcher HTML de otro chat en vez de pedirlo por texto, recuerda añadir al final: *"guarda los ficheros directamente en E:\mis documentos\fondos\ideas\claude\{Empresa}_{Ticker}\ usando Filesystem, no los descargues a mi carpeta de Descargas."*

## Paso 3 — Añadir ficheros manuales (si aplica)
Si hay documentos que TIKR no tiene (folleto de IPO, hecho relevante puntual, presentación específica de la IR), los descargas tú a mano y los añades a esa misma carpeta.

## Paso 4 — Lanzar el análisis
Con la carpeta ya completa (prompt.md + Excel + PDFs + transcripciones):
1. Abres el Proyecto de Claude.ai correspondiente (o creas uno nuevo) y subes todos los ficheros de esa carpeta como conocimiento del proyecto, junto con los 3 md fijos (fuentes, guía de sectores, metodología).
2. Pegas el contenido de `prompt.md` como mensaje.
3. Claude ejecuta el análisis de las 11 secciones.

---

## Resumen visual

```
[Chat con Filesystem + Claude en Chrome]
        │
        ├─ Paso 1: datos empresa → crea carpeta + prompt.md
        ├─ Paso 2: TIKR (Chrome) → descarga PDFs/Excel/transcripciones → guarda en la MISMA carpeta (Filesystem)
        └─ Paso 3: ficheros manuales adicionales → misma carpeta

[Proyecto de Claude.ai]
        │
        └─ Paso 4: subes toda la carpeta + pegas prompt.md → análisis de 11 secciones
```
