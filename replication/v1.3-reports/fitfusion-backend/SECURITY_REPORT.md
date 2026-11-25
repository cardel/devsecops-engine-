# 🔐 Reporte de Seguridad DevSecOps
## ❌ Decisión de Despliegue: **FAIL**

---

> **Generado automáticamente por el pipeline DevSecOps – Universidad del Valle 2026**

| Campo | Valor |
|---|---|
| **Servicio** | `fitfusion-backend` |
| **Entorno** | `staging` |
| **Criticidad de negocio** | `high` |
| **Pipeline Run** | `26253560070` |
| **Timestamp** | `2026-05-21 21:24:56` |
| **Modelo IA** | `threshold_rules_v1` |
| **Tokens utilizados** | `0` (prompt: 0 / completion: 0) |
| **Versión del prompt** | `3.0-ssvc-enriched` |
| **ISO/IEC 27034** | `✅ Activo` |

---

## 📊 Resumen Ejecutivo

Evaluación por umbrales estáticos: FAIL

> **Recomendación del sistema:** Revisar manualmente antes de proceder.

---

## 🚦 Decisión Final del Security Gate

| Campo | Valor |
|---|---|
| **Decisión** | ❌ **FAIL** |
| **Fuente** | `ai_assisted` |
| **Nivel de riesgo (IA)** | `CRITICAL` |
| **Risk Score (IA)** | `0.0 / 10.0` |
| **Confianza IA** | `60%` |
| **Falsos positivos estimados** | `media` |
| **ISO/IEC 27034 — TLOT** | `N/A` |
| **ISO/IEC 27034 — ALOT** | `N/A` |
| **ISO/IEC 27034 — Conformidad** | ❌ No conforme — No evaluado |

---

## 📈 Estadísticas Globales de Hallazgos

### Distribución por Severidad

| Severidad | Hallazgos | % del total | Proporción |
|---|---|---|---|
| 🔴 CRITICAL | 2 | 3.4% | `░░░░░░░░░░░░░░░` |
| 🟠 HIGH | 29 | 49.2% | `███████░░░░░░░░` |
| 🟡 MEDIUM | 20 | 33.9% | `█████░░░░░░░░░░` |
| 🟢 LOW | 6 | 10.2% | `█░░░░░░░░░░░░░░` |
| ⚪ INFO | 2 | 3.4% | `░░░░░░░░░░░░░░░` |
| ─ | **59** | **100%** | |

### Cobertura por Herramienta

> La columna **"Removidos"** indica hallazgos eliminados por deduplicación (no son falsos positivos — son instancias duplicadas de la misma vulnerabilidad).

| Herramienta | Raw | Únicos | Removidos | % Removidos | Estado |
|---|---|---|---|---|---|
| 🔐 Semgrep (SAST) | 0 | 0 | 0 | — | ⚠️ Sin hallazgos |
| 🔬 Trivy (SCA) | 72 | 49 | 23 | 31.9% | ✅ Ejecutado |
| 🌐 OWASP ZAP (DAST) | 6 | 6 | 0 | 0.0% | ✅ Ejecutado |
| 🎯 Nuclei (Pentesting) | 12 | 4 | 8 | 66.7% | ✅ Ejecutado |

### Top Categorías OWASP Top 10

| Categoría | Hallazgos | % del total | Proporción |
|---|---|---|---|
| `A06:2021 – Vulnerable and Outdated Components` | 51 | 86.4% | `██████████░░` |
| `A05:2021 – Security Misconfiguration` | 5 | 8.5% | `█░░░░░░░░░░░` |
| `A07:2021 – Identification and Authentication Failures` | 2 | 3.4% | `░░░░░░░░░░░░` |
| `A03:2021 – Injection` | 1 | 1.7% | `░░░░░░░░░░░░` |

---

## 🔄 Metodología de Deduplicación

> El normalizador aplica deduplicación para evitar el doble conteo de vulnerabilidades detectadas por múltiples instancias de la misma herramienta.
> **Total raw:** 90 hallazgos → **Total único:** 59 hallazgos → **Eliminados:** 31 (34.4% de reducción)

### 🔬 Trivy (SCA) — Análisis de Componentes de Software

- **Raw:** 72 hallazgos detectados | **Únicos tras dedup:** 49 | **Removidos:** 23 (31.9%)
- **Criterio de dedup aplicado:** `tool + título + endpoint/archivo`

> Juice Shop instala dependencias en múltiples subdirectorios de `node_modules` (por ejemplo, `express-jwt/node_modules/lodash` y `sanitize-html/node_modules/lodash`). La misma CVE sobre el mismo paquete y versión aparece una vez por ruta, pero tras deduplicar por `CVE + paquete + target` queda una sola entrada. Los hallazgos removidos no son falsos positivos sino instancias duplicadas de la misma vulnerabilidad real.

### 🌐 OWASP ZAP (DAST) — Análisis Dinámico en Tiempo de Ejecución

- **Raw:** 6 hallazgos detectados | **Únicos tras dedup:** 6 | **Removidos:** 0 (0.0%)
- **Criterio de dedup aplicado:** `tool + título + endpoint/archivo`

> ZAP realiza un escaneo baseline pasivo. Cada alerta representa un tipo de misconfiguration o header faltante único — por eso la deduplicación no elimina ningún hallazgo: todas las alertas tienen títulos distintos. El conteo de instancias dentro de cada alerta indica cuántas URLs presentan el mismo problema.

### 🎯 Nuclei (Pentesting) — Validación Activa de Templates

- **Raw:** 12 hallazgos detectados | **Únicos tras dedup:** 4 | **Removidos:** 8 (66.7%)
- **Criterio de dedup aplicado:** `tool + título + endpoint/archivo`

> Nuclei ejecuta sus templates contra la URL base más todas las rutas descubiertas por el reconocimiento. El mismo template puede disparar en el mismo endpoint más de una vez dentro del mismo run, generando entradas duplicadas en el JSON de salida. Tras deduplicar por `template + endpoint`, se conserva solo una entrada por hallazgo único.

### 🔐 Semgrep (SAST) — Análisis Estático de Código

- **Raw:** 0 hallazgos detectados | **Únicos tras dedup:** 0 | **Removidos:** 0 (0%)
- **Criterio de dedup aplicado:** `tool + título + endpoint/archivo`

> Semgrep analiza el código fuente del repositorio del engine. Las deduplicaciones eliminan la misma regla disparada en múltiples archivos del mismo módulo, conservando solo la primera ocurrencia por regla + ruta de archivo.

---

## 🕵️ Fase de Reconocimiento Activo

> El reconocimiento activo se ejecuta antes del escaneo dinámico para descubrir la superficie de ataque real y enriquecer los targets de Nuclei y ZAP.

### Objetivo analizado

| Campo | Valor |
|---|---|
| **URL objetivo** | `http://localhost:3000` |
| **Host** | `localhost` |
| **Puerto** | `3000` |
| **WAF detectado** | ❌ No detectado |
| **Servidor** | `No detectado` |
| **Título de la app** | `Error` |
| **Tecnologías detectadas** | `Express`, `Node.js` |
| **Targets generados para Nuclei** | 1 URLs |

### Escaneo de Puertos (nmap)

| Puerto | Servicio | Versión | Interesante |
|---|---|---|---|
| `22` | ssh | OpenSSH 9.6p1 Ubuntu 3ubuntu13.16 (Ubunt | No |
| `3000` | http | Node.js Express framework | No |


### Descubrimiento de Rutas

_No se ejecutó descubrimiento de rutas (ffuf/gobuster no disponible)._


### Headers de Seguridad HTTP

| Header de Seguridad | Estado |
|---|---|
| `content-security-policy` | ❌ Faltante |
| `strict-transport-security` | ❌ Faltante |
| `x-frame-options` | ❌ Faltante |
| `x-content-type-options` | ❌ Faltante |
| `referrer-policy` | ❌ Faltante |
| `permissions-policy` | ❌ Faltante |
| `cross-origin-embedder-policy` | ⚪ No verificado |
| `cross-origin-opener-policy` | ⚪ No verificado |


> Los headers faltantes son confirmados por los hallazgos de ZAP y Nuclei.

### Hallazgos de Superficie de Ataque

| Severidad | Tipo | Detalle |
|---|---|---|
| 🟡 MEDIUM | `missing_security_headers` | Headers faltantes: content-security-policy, strict-transport-security, x-frame-options, x-content-ty |
| ⚪ INFO | `no_waf` | No se detectó WAF — tráfico malicioso llega directo a la app |


---

## 🤖 Evaluación Detallada por IA

### Razonamiento Técnico

Se encontraron 2 hallazgos críticos.

**Análisis de falsos positivos:** Sin análisis contextual disponible.

### Categorías OWASP Top 10 Detectadas

- _No se identificaron categorías específicas_

### Análisis de Cobertura por Tipo de Herramienta

| Tipo de análisis | Cobertura | Estado |
|---|---|---|
| SAST – Código fuente | parcial | 🟡 |
| SCA – Dependencias | parcial | 🟡 |
| DAST – Tiempo de ejecución | parcial | 🟡 |
| Pentesting automatizado | parcial | 🟡 |

**Evaluación general:** Evaluación básica sin contexto IA


### 🏆 Hallazgos Principales Identificados por IA

_No se identificaron hallazgos principales._

---

## 🔗 Análisis de Cadenas de Ataque

> Esta sección identifica combinaciones de vulnerabilidades que, explotadas en secuencia,
> producen un impacto mayor al de cada vulnerabilidad de forma individual.

_No se identificaron cadenas de ataque combinadas._

---

## 🛠️ Hoja de Ruta de Remediación

_No se identificaron prioridades específicas._

---

## 🔬 Gate SSVC + EPSS + CISA KEV

> **Fundamento académico:** reemplaza el modelo TLOT/ALOT con constantes arbitrarias por un árbol
> de decisión publicado por CISA/SEI-CERT que elimina la saturación y permite calcular F1 formal.
> **Ref:** Al Haddad et al. (2025), Kausar et al. (2025), Yoon et al. (2023), Rajapakse et al. (2021).

### Resultado del Gate SSVC

| Indicador | Valor |
|---|---|
| **Decisión** | ❌ **FAIL** |
| **Acción agregada SSVC** | `Act` (máximo sobre todos los hallazgos) |
| **Mission & Wellbeing** | `high` (derivado de criticality=`high`) |
| **Fuente de datos KEV** | CISA Known Exploited Vulnerabilities (1,601 entradas) |
| **Fuente de datos EPSS** | FIRST.org API (48 CVEs consultados) |

### Distribución de Acciones SSVC

| Acción | Hallazgos | % | Gate | Significado |
|---|---|---|---|---|
| **Act** | `35` | 59.3% | ❌ FAIL | Explotación activa o automatizable con impacto total |
| **Attend** | `4` | 6.8% | ⚠️ CONDITIONAL | Explotación probable, requiere atención pronto |
| **Track-star** | `13` | 22.0% | ⚠️ CONDITIONAL | Monitorear activamente — riesgo controlado |
| **Track** | `7` | 11.9% | ✅ PASS | Sin explotación activa conocida |
| **Total evaluados** | `59` | 100% | ❌ **FAIL** | Decisión = acción máxima |

### Hallazgos que requieren acción inmediata (Act)

| Herramienta | Vulnerabilidad | Explotación | Automatizable | Impacto | Acción |
|---|---|---|---|---|---|
| `trivy` | CVE-2026-31789 – openssl: OpenSSL: Heap buffer overflow on 32-bit | poc | yes | total | **Act** |
| `trivy` | CVE-2025-15467 – openssl: OpenSSL: Remote code execution or Denia | poc | yes | total | **Act** |
| `trivy` | CVE-2025-69421 – openssl: OpenSSL: Denial of Service via malforme | poc | yes | total | **Act** |
| `trivy` | CVE-2026-28387 – openssl: OpenSSL: Arbitrary code execution due t | poc | yes | total | **Act** |
| `trivy` | CVE-2026-28388 – openssl: OpenSSL: Denial of Service due to NULL  | poc | yes | total | **Act** |
| `trivy` | CVE-2026-28389 – openssl: OpenSSL: Denial of Service vulnerabilit | poc | yes | total | **Act** |
| `trivy` | CVE-2026-28390 – openssl: OpenSSL: Denial of Service due to NULL  | poc | yes | total | **Act** |
| `trivy` | CVE-2026-40200 – musl: musl libc: Arbitrary code execution and de | poc | yes | total | **Act** |


### Métricas Formales — Dimensión Exploitation (F1 Score)

> Calculadas sobre CVEs con CISA KEV o EPSS disponible como *ground truth*.
> Metodología: Al Haddad et al. (2025) — arXiv 2510.18508.

| Métrica | Valor | Descripción |
|---|---|---|
| **Precisión** | `0.0000` | TP / (TP + FP) |
| **Recall** | `0.0000` | TP / (TP + FN) |
| **F1 Score** | `0.0000` | Media armónica precisión/recall |
| **Accuracy** | `1.0000` | (TP + TN) / total |
| CVEs evaluados | `48` | Solo CVEs con EPSS/KEV disponible |
| Verdaderos positivos | `0` | Clasificados active, ground truth active |
| Falsos positivos | `0` | Clasificados active, ground truth not_active |
| Falsos negativos | `0` | Clasificados not_active, ground truth active |

> **Ground truth:** CVE en CISA KEV **o** EPSS ≥ 0.5 → activo.
> **Nota:** hallazgos sin CVE ID (Semgrep/ZAP) excluidos del cálculo formal (sin ground truth verificable).

### Ventajas sobre TLOT/ALOT (modelo anterior)

| Aspecto | TLOT/ALOT (reemplazado) | SSVC + EPSS + KEV (actual) |
|---|---|---|
| Constantes | 0.50/0.65/0.80/0.95 y −0.40/−0.25/−0.10/−0.15 definidas por autores | Árbol publicado por CISA — sin constantes propias |
| Saturación | ALOT = 0.35 idéntico en todos los casos | Track/Attend/Act varían por hallazgo y por perfil |
| Métricas formales | Imposible (sin ground truth) | F1, precisión, recall vs CISA KEV + EPSS |
| Diferenciación | Los 5 casos originales: FAIL uniforme | Casos con bajo perfil de explotación → PASS/CONDITIONAL |


### 🔬 Contexto SSVC/EPSS/KEV Usado en Esta Evaluación

> **Gate híbrido IA + SSVC/EPSS/KEV** — el LLM recibió como contexto las
> clasificaciones SSVC preliminares y datos empíricos de explotabilidad, siguiendo
> la metodología de **Al Haddad et al. (2025)** *(arXiv 2510.18508)* que demuestra
> que los LLMs mejoran la clasificación SSVC cuando se enriquece su contexto con
> datos EPSS/KEV. El LLM puede validar o corregir las clasificaciones basándose
> en el contexto específico de la aplicación.

| Métrica de Enriquecimiento | Valor |
|---|---|
| **CISA KEV consultado** | 1,601 entradas |
| **EPSS scores obtenidos** | 48 CVEs |
| **Hallazgos clasificados SSVC** | 59 |
| **Distribución SSVC** | Act=35, Attend=4, Track*=13, Track=7 |
> **F1 Exploitation (ground truth KEV+EPSS):** `0.000` (P=0.000, R=0.000, n=48 CVEs)


---

## 🔄 Comparación: Tres Enfoques de Security Gate

> **Contribución central del Trabajo de Grado:** comparar empíricamente tres mecanismos de
> decisión de despliegue. El gate tradicional como línea base, el gate IA para análisis
> contextual, y el gate SSVC+EPSS+KEV como métrica estandarizada con F1 formal.
> ISO/IEC 27034 se conserva para trazabilidad normativa (asc_id).

| Criterio | Gate Tradicional | Gate con IA | Gate SSVC+EPSS+KEV |
|---|---|---|---|
| **Decisión** | ❌ FAIL | ❌ FAIL | ❌ FAIL |
| **Método** | Umbrales numéricos fijos | Evaluación contextual LLM | Árbol SSVC + EPSS + CISA KEV |
| **Acción agregada** | N/A | N/A | `Act` (Act/Attend/Track*/Track) |
| **Métricas formales** | ❌ No | ❌ No | ✅ F1=`0.000` (vs CISA KEV) |
| **Considera falsos positivos** | ❌ No | ✅ Estimados (media) | ✅ EPSS filtra low-risk |
| **Evalúa explotabilidad real** | ❌ No | ✅ Semántica LLM | ✅ CISA KEV + EPSS empírico |
| **Detecta cadenas de ataque** | ❌ No | ✅ Sí | ❌ No (por hallazgo individual) |
| **Constantes arbitrarias** | ✅ Umbrales fijos | N/A | ❌ Ninguna (árbol CISA público) |
| **Saturación de scores** | ✅ Posible | N/A | ❌ Elimina saturación |
| **Transparencia** | ✅ Alta | ⚠️ Caja negra | ✅ Alta (árbol publicado CISA) |
| **Determinístico** | ✅ Sí | ❌ No | ✅ Sí |
| **Costo computacional** | Nulo | ~$0.005/run | ~API calls gratuitas |
| **Modelo / versión** | Reglas fijas | `threshold_rules_v1` | SSVC v2.1 + FIRST.org EPSS |
| **Confianza / score** | N/A | 60% | `0.000` F1 (Exploitation) |

### Divergencias entre gates

- Los tres gates concuerdan en la decisión final.

**Insight académico:** Los tres gates concuerdan — validación metodológica.

**Análisis de la comparación:** N/A

**Razones del gate tradicional:**
- Hallazgos CRÍTICOS: 2 (umbral: 0)
- Hallazgos ALTOS: 29 (umbral: 5)
- Hallazgos MEDIOS: 20 (umbral: 20)

**Análisis de falsos positivos (IA):** Sin análisis contextual disponible.

> **Nota sobre ISO/IEC 27034:** el modelo TLOT/ALOT fue reemplazado por SSVC+EPSS+KEV
> para eliminar constantes arbitrarias y habilitar métricas formales. ISO/IEC 27034 se
> conserva como marco de trazabilidad normativa: cada hallazgo mantiene su `asc_id` y
> los ASCs ejecutados quedan registrados (ver sección siguiente).

---

## 📋 Hallazgos Detallados por Herramienta

### 🔬 Trivy (SCA)

> **Tipo:** Análisis de Componentes de Software  
> **Raw:** 72 | **Únicos:** 49 | **Deduplicados:** 23 (31.9%)

**Distribución:** 🔴 CRITICAL: **2** | 🟠 HIGH: **29** | 🟡 MEDIUM: **18**

#### 🔴🟠 Críticos y Altos (31)

#### 🔴 [CRITICAL] CVE-2026-31789 – openssl: OpenSSL: Heap buffer overflow on 32-bit systems from large X.509 certificate processing

| Campo | Valor |
|---|---|
| **ID** | `TRI-3B709604` |
| **Herramienta** | `TRIVY` (SCA) |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `9.8` |
| **Archivo** | `ghcr.io/manuelarango1229/backend-fitfusion/fitfusion-backend:fb47b6814fd565ed21b0f2cbffae5e6fefd35cbe (alpine 3.21.3):None` |

**Descripción:** Issue summary: Converting an excessively large OCTET STRING value to
a hexadecimal string leads to a heap buffer overflow on 32 bit platforms.

Impact summary: A heap buffer overflow may lead to a crash or possibly
an attacker controlled code execution or other undefined behavior.

If an attacker can supply a crafted X.509 certificate with an excessively
large OCTET STRING value in extensions such

**Evidencia:** `Paquete: libcrypto3 v3.3.3-r0 | Fix: 3.3.7-r0`

**✅ Remediación:** Actualizar libcrypto3 de 3.3.3-r0 a 3.3.7-r0

---

#### 🔴 [CRITICAL] CVE-2026-33937 – handlebars.js: Handlebars: Remote Code Execution via crafted Abstract Syntax Tree object in compile()

| Campo | Valor |
|---|---|
| **ID** | `TRI-C387FCB0` |
| **Herramienta** | `TRIVY` (SCA) |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `9.8` |
| **Archivo** | `Node.js:None` |

**Descripción:** Handlebars provides the power necessary to let users build semantic templates. In versions 4.0.0 through 4.7.8, `Handlebars.compile()` accepts a pre-parsed AST object in addition to a template string. The `value` field of a `NumberLiteral` AST node is emitted directly into the generated JavaScript without quoting or sanitization. An attacker who can supply a crafted AST to `compile()` can therefor

**Evidencia:** `Paquete: handlebars v4.7.8 | Fix: 4.7.9`

**✅ Remediación:** Actualizar handlebars de 4.7.8 a 4.7.9

---

#### 🟠 [HIGH] CVE-2025-15467 – openssl: OpenSSL: Remote code execution or Denial of Service via oversized Initialization Vector in CMS parsing

| Campo | Valor |
|---|---|
| **ID** | `TRI-8CEE03CF` |
| **Herramienta** | `TRIVY` (SCA) |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `9.8` |
| **Archivo** | `ghcr.io/manuelarango1229/backend-fitfusion/fitfusion-backend:fb47b6814fd565ed21b0f2cbffae5e6fefd35cbe (alpine 3.21.3):None` |

**Descripción:** Issue summary: Parsing CMS AuthEnvelopedData or EnvelopedData message with
maliciously crafted AEAD parameters can trigger a stack buffer overflow.

Impact summary: A stack buffer overflow may lead to a crash, causing Denial
of Service, or potentially remote code execution.

When parsing CMS (Auth)EnvelopedData structures that use AEAD ciphers such as
AES-GCM, the IV (Initialization Vector) encode

**Evidencia:** `Paquete: libcrypto3 v3.3.3-r0 | Fix: 3.3.6-r0`

**✅ Remediación:** Actualizar libcrypto3 de 3.3.3-r0 a 3.3.6-r0

---

#### 🟠 [HIGH] CVE-2025-69421 – openssl: OpenSSL: Denial of Service via malformed PKCS#12 file processing

| Campo | Valor |
|---|---|
| **ID** | `TRI-36F69BC8` |
| **Herramienta** | `TRIVY` (SCA) |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `ghcr.io/manuelarango1229/backend-fitfusion/fitfusion-backend:fb47b6814fd565ed21b0f2cbffae5e6fefd35cbe (alpine 3.21.3):None` |

**Descripción:** Issue summary: Processing a malformed PKCS#12 file can trigger a NULL pointer
dereference in the PKCS12_item_decrypt_d2i_ex() function.

Impact summary: A NULL pointer dereference can trigger a crash which leads to
Denial of Service for an application processing PKCS#12 files.

The PKCS12_item_decrypt_d2i_ex() function does not check whether the oct
parameter is NULL before dereferencing it. When 

**Evidencia:** `Paquete: libcrypto3 v3.3.3-r0 | Fix: 3.3.6-r0`

**✅ Remediación:** Actualizar libcrypto3 de 3.3.3-r0 a 3.3.6-r0

---

#### 🟠 [HIGH] CVE-2026-28387 – openssl: OpenSSL: Arbitrary code execution due to use-after-free in DANE TLSA authentication

| Campo | Valor |
|---|---|
| **ID** | `TRI-2CC89627` |
| **Herramienta** | `TRIVY` (SCA) |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `8.1` |
| **Archivo** | `ghcr.io/manuelarango1229/backend-fitfusion/fitfusion-backend:fb47b6814fd565ed21b0f2cbffae5e6fefd35cbe (alpine 3.21.3):None` |

**Descripción:** Issue summary: An uncommon configuration of clients performing DANE TLSA-based
server authentication, when paired with uncommon server DANE TLSA records, may
result in a use-after-free and/or double-free on the client side.

Impact summary: A use after free can have a range of potential consequences
such as the corruption of valid data, crashes or execution of arbitrary code.

However, the issue o

**Evidencia:** `Paquete: libcrypto3 v3.3.3-r0 | Fix: 3.3.7-r0`

**✅ Remediación:** Actualizar libcrypto3 de 3.3.3-r0 a 3.3.7-r0

---

#### 🟠 [HIGH] CVE-2026-28388 – openssl: OpenSSL: Denial of Service due to NULL pointer dereference in delta CRL processing

| Campo | Valor |
|---|---|
| **ID** | `TRI-9D928CF1` |
| **Herramienta** | `TRIVY` (SCA) |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `ghcr.io/manuelarango1229/backend-fitfusion/fitfusion-backend:fb47b6814fd565ed21b0f2cbffae5e6fefd35cbe (alpine 3.21.3):None` |

**Descripción:** Issue summary: When a delta CRL that contains a Delta CRL Indicator extension
is processed a NULL pointer dereference might happen if the required CRL
Number extension is missing.

Impact summary: A NULL pointer dereference can trigger a crash which
leads to a Denial of Service for an application.

When CRL processing and delta CRL processing is enabled during X.509
certificate verification, the d

**Evidencia:** `Paquete: libcrypto3 v3.3.3-r0 | Fix: 3.3.7-r0`

**✅ Remediación:** Actualizar libcrypto3 de 3.3.3-r0 a 3.3.7-r0

---

#### 🟠 [HIGH] CVE-2026-28389 – openssl: OpenSSL: Denial of Service vulnerability in CMS processing

| Campo | Valor |
|---|---|
| **ID** | `TRI-737395D3` |
| **Herramienta** | `TRIVY` (SCA) |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `ghcr.io/manuelarango1229/backend-fitfusion/fitfusion-backend:fb47b6814fd565ed21b0f2cbffae5e6fefd35cbe (alpine 3.21.3):None` |

**Descripción:** Issue summary: During processing of a crafted CMS EnvelopedData message
with KeyAgreeRecipientInfo a NULL pointer dereference can happen.

Impact summary: Applications that process attacker-controlled CMS data may
crash before authentication or cryptographic operations occur resulting in
Denial of Service.

When a CMS EnvelopedData message that uses KeyAgreeRecipientInfo is
processed, the optional

**Evidencia:** `Paquete: libcrypto3 v3.3.3-r0 | Fix: 3.3.7-r0`

**✅ Remediación:** Actualizar libcrypto3 de 3.3.3-r0 a 3.3.7-r0

---

#### 🟠 [HIGH] CVE-2026-28390 – openssl: OpenSSL: Denial of Service due to NULL pointer dereference in CMS EnvelopedData processing

| Campo | Valor |
|---|---|
| **ID** | `TRI-9E240627` |
| **Herramienta** | `TRIVY` (SCA) |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `ghcr.io/manuelarango1229/backend-fitfusion/fitfusion-backend:fb47b6814fd565ed21b0f2cbffae5e6fefd35cbe (alpine 3.21.3):None` |

**Descripción:** Issue summary: During processing of a crafted CMS EnvelopedData message
with KeyTransportRecipientInfo a NULL pointer dereference can happen.

Impact summary: Applications that process attacker-controlled CMS data may
crash before authentication or cryptographic operations occur resulting in
Denial of Service.

When a CMS EnvelopedData message that uses KeyTransportRecipientInfo with
RSA-OAEP encr

**Evidencia:** `Paquete: libcrypto3 v3.3.3-r0 | Fix: 3.3.7-r0`

**✅ Remediación:** Actualizar libcrypto3 de 3.3.3-r0 a 3.3.7-r0

---

#### 🟠 [HIGH] CVE-2026-40200 – musl: musl libc: Arbitrary code execution and denial of service via stack-based memory corruption in qsort

| Campo | Valor |
|---|---|
| **ID** | `TRI-AFBEE807` |
| **Herramienta** | `TRIVY` (SCA) |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.8` |
| **Archivo** | `ghcr.io/manuelarango1229/backend-fitfusion/fitfusion-backend:fb47b6814fd565ed21b0f2cbffae5e6fefd35cbe (alpine 3.21.3):None` |

**Descripción:** An issue was discovered in musl libc 0.7.10 through 1.2.6. Stack-based memory corruption can occur during qsort of very large arrays, due to incorrectly implemented double-word primitives. The number of elements must exceed about seven million, i.e., the 32nd Leonardo number on 32-bit platforms (or the 64th Leonardo number on 64-bit platforms, which is not practical).

**Evidencia:** `Paquete: musl v1.2.5-r9 | Fix: 1.2.5-r11`

**✅ Remediación:** Actualizar musl de 1.2.5-r9 a 1.2.5-r11

---

#### 🟠 [HIGH] CVE-2026-22184 – zlib: zlib: Arbitrary code execution via buffer overflow in untgz utility

| Campo | Valor |
|---|---|
| **ID** | `TRI-7A83CEE5` |
| **Herramienta** | `TRIVY` (SCA) |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.8` |
| **Archivo** | `ghcr.io/manuelarango1229/backend-fitfusion/fitfusion-backend:fb47b6814fd565ed21b0f2cbffae5e6fefd35cbe (alpine 3.21.3):None` |

**Descripción:** zlib versions up to and including 1.3.1.2 include a global buffer overflow in the untgz utility located under contrib/untgz. The vulnerability is limited to the standalone demonstration utility and does not affect the core zlib compression library. The flaw occurs when a user executes the untgz command with an excessively long archive name supplied via the command line, leading to an out-of-bounds

**Evidencia:** `Paquete: zlib v1.3.1-r2 | Fix: 1.3.2-r0`

**✅ Remediación:** Actualizar zlib de 1.3.1-r2 a 1.3.2-r0

---

#### 🟠 [HIGH] CVE-2024-21538 – cross-spawn: regular expression denial of service

| Campo | Valor |
|---|---|
| **ID** | `TRI-E8929BCB` |
| **Herramienta** | `TRIVY` (SCA) |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `4.4` |
| **Archivo** | `Node.js:None` |

**Descripción:** Versions of the package cross-spawn before 6.0.6, from 7.0.0 and before 7.0.5 are vulnerable to Regular Expression Denial of Service (ReDoS) due to improper input sanitization. An attacker can increase the CPU usage and crash the program by crafting a very large and well crafted string.

**Evidencia:** `Paquete: cross-spawn v7.0.3 | Fix: 7.0.5, 6.0.6`

**✅ Remediación:** Actualizar cross-spawn de 7.0.3 a 7.0.5, 6.0.6

---

#### 🟠 [HIGH] CVE-2025-64756 – glob: glob: Command Injection Vulnerability via Malicious Filenames

| Campo | Valor |
|---|---|
| **ID** | `TRI-CD8B31C7` |
| **Herramienta** | `TRIVY` (SCA) |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `Node.js:None` |

**Descripción:** Glob matches files using patterns the shell uses. Starting in version 10.2.0 and prior to versions 10.5.0 and 11.1.0, the glob CLI contains a command injection vulnerability in its -c/--cmd option that allows arbitrary command execution when processing files with malicious names. When glob -c <command> <patterns> are used, matched filenames are passed to a shell with shell: true, enabling shell me

**Evidencia:** `Paquete: glob v10.4.2 | Fix: 11.1.0, 10.5.0`

**✅ Remediación:** Actualizar glob de 10.4.2 a 11.1.0, 10.5.0

---

#### 🟠 [HIGH] CVE-2026-33938 – handlebars: Handlebars: Arbitrary code execution via @partial-block overwrite

| Campo | Valor |
|---|---|
| **ID** | `TRI-C9737641` |
| **Herramienta** | `TRIVY` (SCA) |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `8.1` |
| **Archivo** | `Node.js:None` |

**Descripción:** Handlebars provides the power necessary to let users build semantic templates. In versions 4.0.0 through 4.7.8, the `@partial-block` special variable is stored in the template data context and is reachable and mutable from within a template via helpers that accept arbitrary objects. When a helper overwrites `@partial-block` with a crafted Handlebars AST, a subsequent invocation of `{{> @partial-bl

**Evidencia:** `Paquete: handlebars v4.7.8 | Fix: 4.7.9`

**✅ Remediación:** Actualizar handlebars de 4.7.8 a 4.7.9

---

#### 🟠 [HIGH] CVE-2026-33939 – handlebars.js: Handlebars.js: Denial of Service via malformed decorator syntax in template compilation

| Campo | Valor |
|---|---|
| **ID** | `TRI-975BAA7C` |
| **Herramienta** | `TRIVY` (SCA) |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `Node.js:None` |

**Descripción:** Handlebars provides the power necessary to let users build semantic templates. In versions 4.0.0 through 4.7.8, when a Handlebars template contains decorator syntax referencing an unregistered decorator (e.g. `{{*n}}`), the compiled template calls `lookupProperty(decorators, "n")`, which returns `undefined`. The runtime then immediately invokes the result as a function, causing an unhandled `TypeE

**Evidencia:** `Paquete: handlebars v4.7.8 | Fix: 4.7.9`

**✅ Remediación:** Actualizar handlebars de 4.7.8 a 4.7.9

---

#### 🟠 [HIGH] CVE-2026-33940 – handlebars.js: Handlebars.js: Arbitrary code execution via crafted template context

| Campo | Valor |
|---|---|
| **ID** | `TRI-2FF9EB86` |
| **Herramienta** | `TRIVY` (SCA) |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `8.1` |
| **Archivo** | `Node.js:None` |

**Descripción:** Handlebars provides the power necessary to let users build semantic templates. In versions 4.0.0 through 4.7.8, a crafted object placed in the template context can bypass all conditional guards in `resolvePartial()` and cause `invokePartial()` to return `undefined`. The Handlebars runtime then treats the unresolved partial as a source that needs to be compiled, passing the crafted object to `env.c

**Evidencia:** `Paquete: handlebars v4.7.8 | Fix: 4.7.9`

**✅ Remediación:** Actualizar handlebars de 4.7.8 a 4.7.9

---

#### 🟠 [HIGH] CVE-2026-33941 – handlebars.js: Handlebars: Arbitrary code execution via CLI precompiler input sanitization flaw

| Campo | Valor |
|---|---|
| **ID** | `TRI-A300E601` |
| **Herramienta** | `TRIVY` (SCA) |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `8.2` |
| **Archivo** | `Node.js:None` |

**Descripción:** Handlebars provides the power necessary to let users build semantic templates. In versions 4.0.0 through 4.7.8, the Handlebars CLI precompiler (`bin/handlebars` / `lib/precompiler.js`) concatenates user-controlled strings — template file names and several CLI options — directly into the JavaScript it emits, without any escaping or sanitization. An attacker who can influence template filenames or C

**Evidencia:** `Paquete: handlebars v4.7.8 | Fix: 4.7.9`

**✅ Remediación:** Actualizar handlebars de 4.7.8 a 4.7.9

---

#### 🟠 [HIGH] CVE-2025-65945 – node-jws: auth0/node-jws: Improper signature verification in HS256 algorithm

| Campo | Valor |
|---|---|
| **ID** | `TRI-CB3DDBA6` |
| **Herramienta** | `TRIVY` (SCA) |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `Node.js:None` |

**Descripción:** auth0/node-jws is a JSON Web Signature implementation for Node.js. In versions 3.2.2 and earlier and version 4.0.0, auth0/node-jws has an improper signature verification vulnerability when using the HS256 algorithm under specific conditions. Applications are affected when they use the jws.createVerify() function for HMAC algorithms and use user-provided data from the JSON Web Signature protected h

**Evidencia:** `Paquete: jws v3.2.2 | Fix: 3.2.3, 4.0.1`

**✅ Remediación:** Actualizar jws de 3.2.2 a 3.2.3, 4.0.1

---

#### 🟠 [HIGH] CVE-2026-4800 – lodash: lodash: Arbitrary code execution via untrusted input in template imports

| Campo | Valor |
|---|---|
| **ID** | `TRI-58B2412E` |
| **Herramienta** | `TRIVY` (SCA) |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `9.8` |
| **Archivo** | `Node.js:None` |

**Descripción:** Impact:

The fix for CVE-2021-23337 (https://github.com/advisories/GHSA-35jh-r3h4-6jhm) added validation for the variable option in _.template but did not apply the same validation to options.imports key names. Both paths flow into the same Function() constructor sink.

When an application passes untrusted input as options.imports key names, an attacker can inject default-parameter expressions tha

**Evidencia:** `Paquete: lodash v4.17.21 | Fix: 4.18.0`

**✅ Remediación:** Actualizar lodash de 4.17.21 a 4.18.0

---

#### 🟠 [HIGH] CVE-2026-26996 – minimatch: minimatch: Denial of Service via specially crafted glob patterns

| Campo | Valor |
|---|---|
| **ID** | `TRI-4DBC63E3` |
| **Herramienta** | `TRIVY` (SCA) |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `Node.js:None` |

**Descripción:** minimatch is a minimal matching utility for converting glob expressions into JavaScript RegExp objects. Versions 10.2.0 and below are vulnerable to Regular Expression Denial of Service (ReDoS) when a glob pattern contains many consecutive * wildcards followed by a literal character that doesn't appear in the test string. Each * compiles to a separate [^/]*? regex group, and when the match fails, V

**Evidencia:** `Paquete: minimatch v3.1.2 | Fix: 10.2.1, 9.0.6, 8.0.5, 7.4.7, 6.2.1, 5.1.7, 4.2.4, 3.1.3`

**✅ Remediación:** Actualizar minimatch de 3.1.2 a 10.2.1, 9.0.6, 8.0.5, 7.4.7, 6.2.1, 5.1.7, 4.2.4, 3.1.3

---

#### 🟠 [HIGH] CVE-2026-27903 – minimatch: minimatch: Denial of Service due to unbounded recursive backtracking via crafted glob patterns

| Campo | Valor |
|---|---|
| **ID** | `TRI-A158C435` |
| **Herramienta** | `TRIVY` (SCA) |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `5.9` |
| **Archivo** | `Node.js:None` |

**Descripción:** minimatch is a minimal matching utility for converting glob expressions into JavaScript RegExp objects. Prior to version 10.2.3, 9.0.7, 8.0.6, 7.4.8, 6.2.2, 5.1.8, 4.2.5, and 3.1.3, `matchOne()` performs unbounded recursive backtracking when a glob pattern contains multiple non-adjacent `**` (GLOBSTAR) segments and the input path does not match. The time complexity is O(C(n, k)) -- binomial -- whe

**Evidencia:** `Paquete: minimatch v3.1.2 | Fix: 10.2.3, 9.0.7, 8.0.6, 7.4.8, 6.2.2, 5.1.8, 4.2.5, 3.1.3`

**✅ Remediación:** Actualizar minimatch de 3.1.2 a 10.2.3, 9.0.7, 8.0.6, 7.4.8, 6.2.2, 5.1.8, 4.2.5, 3.1.3

---

#### 🟠 [HIGH] CVE-2026-27904 – minimatch: Minimatch: Denial of Service via catastrophic backtracking in glob expressions

| Campo | Valor |
|---|---|
| **ID** | `TRI-69E1F675` |
| **Herramienta** | `TRIVY` (SCA) |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `6.5` |
| **Archivo** | `Node.js:None` |

**Descripción:** minimatch is a minimal matching utility for converting glob expressions into JavaScript RegExp objects. Prior to version 10.2.3, 9.0.7, 8.0.6, 7.4.8, 6.2.2, 5.1.8, 4.2.5, and 3.1.4, nested `*()` extglobs produce regexps with nested unbounded quantifiers (e.g. `(?:(?:a|b)*)*`), which exhibit catastrophic backtracking in V8. With a 12-byte pattern `*(*(*(a|b)))` and an 18-byte non-matching input, `m

**Evidencia:** `Paquete: minimatch v3.1.2 | Fix: 10.2.3, 9.0.7, 8.0.6, 7.4.8, 6.2.2, 5.1.8, 4.2.5, 3.1.4`

**✅ Remediación:** Actualizar minimatch de 3.1.2 a 10.2.3, 9.0.7, 8.0.6, 7.4.8, 6.2.2, 5.1.8, 4.2.5, 3.1.4

---

#### 🟠 [HIGH] CVE-2026-42334 – Mongoose's Improper Sanitization of $nor in sanitizeFilter May Allow NoSQL Injection

| Campo | Valor |
|---|---|
| **ID** | `TRI-57534C85` |
| **Herramienta** | `TRIVY` (SCA) |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `Node.js:None` |

**Descripción:** Mongoose is a MongoDB object modeling tool designed to work in an asynchronous environment. Prior to 6.13.9, 7.8.9, 8.22.1, and 9.1.6, a vulnerability allows bypassing Mongoose’s sanitizeFilter query sanitization mechanism via the $nor operator. When sanitizeFilter is enabled, Mongoose wraps query operators in $eq to neutralize them. However, prior to the fix, $nor was not included in the set of l

**Evidencia:** `Paquete: mongoose v8.20.0 | Fix: 6.13.9, 7.8.9, 8.22.1, 9.1.6`

**✅ Remediación:** Actualizar mongoose de 8.20.0 a 6.13.9, 7.8.9, 8.22.1, 9.1.6

---

#### 🟠 [HIGH] CVE-2026-4867 – path-to-regexp: path-to-regexp: Denial of Service via catastrophic backtracking from malformed URL parameters

| Campo | Valor |
|---|---|
| **ID** | `TRI-5D2C4372` |
| **Herramienta** | `TRIVY` (SCA) |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `5.3` |
| **Archivo** | `Node.js:None` |

**Descripción:** Impact:

A bad regular expression is generated any time you have three or more parameters within a single segment, separated by something that is not a period (.). For example, /:a-:b-:c or /:a-:b-:c-:d. The backtrack protection added in path-to-regexp@0.1.12 only prevents ambiguity for two parameters. With three or more, the generated lookahead does not block single separator characters, so captu

**Evidencia:** `Paquete: path-to-regexp v0.1.12 | Fix: 0.1.13`

**✅ Remediación:** Actualizar path-to-regexp de 0.1.12 a 0.1.13

---

#### 🟠 [HIGH] CVE-2026-33671 – picomatch: Picomatch: Regular Expression Denial of Service via crafted extglob patterns

| Campo | Valor |
|---|---|
| **ID** | `TRI-46F03624` |
| **Herramienta** | `TRIVY` (SCA) |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `6.5` |
| **Archivo** | `Node.js:None` |

**Descripción:** Picomatch is a glob matcher written JavaScript. Versions prior to 4.0.4, 3.0.2, and 2.3.2 are vulnerable to Regular Expression Denial of Service (ReDoS) when processing crafted extglob patterns. Certain patterns using extglob quantifiers such as `+()` and `*()`, especially when combined with overlapping alternatives or nested extglobs, are compiled into regular expressions that can exhibit catastr

**Evidencia:** `Paquete: picomatch v2.3.1 | Fix: 4.0.4, 3.0.2, 2.3.2`

**✅ Remediación:** Actualizar picomatch de 2.3.1 a 4.0.4, 3.0.2, 2.3.2

---

#### 🟠 [HIGH] CVE-2026-23745 – node-tar: tar: node-tar: Arbitrary file overwrite and symlink poisoning via unsanitized linkpaths in archives

| Campo | Valor |
|---|---|
| **ID** | `TRI-052C5558` |
| **Herramienta** | `TRIVY` (SCA) |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `6.1` |
| **Archivo** | `Node.js:None` |

**Descripción:** node-tar is a Tar for Node.js. The node-tar library (<= 7.5.2) fails to sanitize the linkpath of Link (hardlink) and SymbolicLink entries when preservePaths is false (the default secure behavior). This allows malicious archives to bypass the extraction root restriction, leading to Arbitrary File Overwrite via hardlinks and Symlink Poisoning via absolute symlink targets. This vulnerability is fixed

**Evidencia:** `Paquete: tar v6.2.1 | Fix: 7.5.3`

**✅ Remediación:** Actualizar tar de 6.2.1 a 7.5.3

---

#### 🟠 [HIGH] CVE-2026-23950 – node-tar: tar: node-tar: Arbitrary file overwrite via Unicode path collision race condition

| Campo | Valor |
|---|---|
| **ID** | `TRI-19837964` |
| **Herramienta** | `TRIVY` (SCA) |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `5.9` |
| **Archivo** | `Node.js:None` |

**Descripción:** node-tar,a Tar for Node.js, has a race condition vulnerability in versions up to and including 7.5.3. This is due to an incomplete handling of Unicode path collisions in the `path-reservations` system. On case-insensitive or normalization-insensitive filesystems (such as macOS APFS, In which it has been tested), the library fails to lock colliding paths (e.g., `ß` and `ss`), allowing them to be pr

**Evidencia:** `Paquete: tar v6.2.1 | Fix: 7.5.4`

**✅ Remediación:** Actualizar tar de 6.2.1 a 7.5.4

---

#### 🟠 [HIGH] CVE-2026-24842 – node-tar: tar: node-tar: Arbitrary file creation via path traversal bypass in hardlink security check

| Campo | Valor |
|---|---|
| **ID** | `TRI-DF29B2A1` |
| **Herramienta** | `TRIVY` (SCA) |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `8.2` |
| **Archivo** | `Node.js:None` |

**Descripción:** node-tar,a Tar for Node.js, contains a vulnerability in versions prior to 7.5.7 where the security check for hardlink entries uses different path resolution semantics than the actual hardlink creation logic. This mismatch allows an attacker to craft a malicious TAR archive that bypasses path traversal protections and creates hardlinks to arbitrary files outside the extraction directory. Version 7.

**Evidencia:** `Paquete: tar v6.2.1 | Fix: 7.5.7`

**✅ Remediación:** Actualizar tar de 6.2.1 a 7.5.7

---

#### 🟠 [HIGH] CVE-2026-26960 – node-tar: node-tar: Arbitrary file read/write via malicious archive hardlink creation

| Campo | Valor |
|---|---|
| **ID** | `TRI-6CEAF1CD` |
| **Herramienta** | `TRIVY` (SCA) |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.1` |
| **Archivo** | `Node.js:None` |

**Descripción:** node-tar is a full-featured Tar for Node.js. When using default options in versions 7.5.7 and below, an attacker-controlled archive can create a hardlink inside the extraction directory that points to a file outside the extraction root, enabling arbitrary file read and write as the extracting user. Severity is high because the primitive bypasses path protections and turns archive extraction into a

**Evidencia:** `Paquete: tar v6.2.1 | Fix: 7.5.8`

**✅ Remediación:** Actualizar tar de 6.2.1 a 7.5.8

---

#### 🟠 [HIGH] CVE-2026-29786 – node-tar: hardlink path traversal via drive-relative linkpath

| Campo | Valor |
|---|---|
| **ID** | `TRI-810F264E` |
| **Herramienta** | `TRIVY` (SCA) |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `6.3` |
| **Archivo** | `Node.js:None` |

**Descripción:** node-tar is a full-featured Tar for Node.js. Prior to version 7.5.10, tar can be tricked into creating a hardlink that points outside the extraction directory by using a drive-relative link target such as C:../target.txt, which enables file overwrite outside cwd during normal tar.x() extraction. This issue has been patched in version 7.5.10.

**Evidencia:** `Paquete: tar v6.2.1 | Fix: 7.5.10`

**✅ Remediación:** Actualizar tar de 6.2.1 a 7.5.10

---

#### 🟠 [HIGH] CVE-2026-31802 – tar: tar: File overwrite via drive-relative symlink traversal

| Campo | Valor |
|---|---|
| **ID** | `TRI-26714757` |
| **Herramienta** | `TRIVY` (SCA) |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `5.5` |
| **Archivo** | `Node.js:None` |

**Descripción:** node-tar is a full-featured Tar for Node.js. Prior to version 7.5.11, tar (npm) can be tricked into creating a symlink that points outside the extraction directory by using a drive-relative symlink target such as C:../../../target.txt, which enables file overwrite outside cwd during normal tar.x() extraction. This vulnerability is fixed in 7.5.11.

**Evidencia:** `Paquete: tar v6.2.1 | Fix: 7.5.11`

**✅ Remediación:** Actualizar tar de 6.2.1 a 7.5.11

---

#### 🟠 [HIGH] CVE-2026-27601 – Underscore.js: Underscore.js: Denial of Service via recursive data structures in flatten and isEqual functions

| Campo | Valor |
|---|---|
| **ID** | `TRI-A68F09F1` |
| **Herramienta** | `TRIVY` (SCA) |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `5.9` |
| **Archivo** | `Node.js:None` |

**Descripción:** Underscore.js is a utility-belt library for JavaScript. Prior to 1.13.8, the _.flatten and _.isEqual functions use recursion without a depth limit. Under very specific conditions, detailed below, an attacker could exploit this in a Denial of Service (DoS) attack by triggering a stack overflow. Untrusted input must be used to create a recursive datastructure, for example using JSON.parse, with no e

**Evidencia:** `Paquete: underscore v1.13.7 | Fix: 1.13.8`

**✅ Remediación:** Actualizar underscore de 1.13.7 a 1.13.8

---

#### 🟡🟢⚪ Medios, Bajos e Info (18)

| Severidad | CVE / Advisory | CVSS | Remediación |
|---|---|---|---|
| 🟡 MEDIUM | CVE-2024-58251 – In netstat in BusyBox through 1.37.0,  | None | Actualizar busybox de 1.37.0-r12 a 1.37.0-r14 |
| 🟡 MEDIUM | CVE-2025-69419 – openssl: OpenSSL: Arbitrary code execu | 7.4 | Actualizar libcrypto3 de 3.3.3-r0 a 3.3.6-r0 |
| 🟡 MEDIUM | CVE-2025-9230 – openssl: Out-of-bounds read & write in  | 5.6 | Actualizar libcrypto3 de 3.3.3-r0 a 3.3.5-r0 |
| 🟡 MEDIUM | CVE-2025-9231 – openssl: Timing side-channel in SM2 alg | 5.9 | Actualizar libcrypto3 de 3.3.3-r0 a 3.3.5-r0 |
| 🟡 MEDIUM | CVE-2026-31790 – openssl: openssl: Information Disclosu | 5.9 | Actualizar libcrypto3 de 3.3.3-r0 a 3.3.7-r0 |
| 🟡 MEDIUM | CVE-2026-6042 – musl libc: GB18030 4-byte Decoder: musl | 5.5 | Actualizar musl de 1.2.5-r9 a 1.2.5-r10 |
| 🟡 MEDIUM | CVE-2026-27171 – zlib: zlib: Denial of Service via infi | 5.5 | Actualizar zlib de 1.3.1-r2 a 1.3.2-r0 |
| 🟡 MEDIUM | CVE-2026-33750 – brace-expansion: brace-expansion: Deni | 7.5 | Actualizar brace-expansion de 1.1.12 a 5.0.5, 3.0.2, 2.0.3, 1.1.13 |
| 🟡 MEDIUM | CVE-2026-33916 – handlebars.js: Handlebars: Cross-Site  | 4.7 | Actualizar handlebars de 4.7.8 a 4.7.9 |
| 🟡 MEDIUM | GHSA-7rx3-28cr-v5wh – Handlebars.js has a Prototype Met | 4.8 | Actualizar handlebars de 4.7.8 a 4.7.9 |
| 🟡 MEDIUM | CVE-2026-42338 – ip-address is a library for parsing an | 6.1 | Actualizar ip-address de 9.0.5 a 10.1.1 |
| 🟡 MEDIUM | CVE-2025-13465 – lodash: prototype pollution in _.unset | 5.3 | Actualizar lodash de 4.17.21 a 4.17.23 |
| 🟡 MEDIUM | CVE-2026-2950 – lodash: Lodash: Prototype pollution all | 5.3 | Actualizar lodash de 4.17.21 a 4.18.0 |
| 🟡 MEDIUM | CVE-2026-2327 – markdown-it: markdown-it: Denial of Ser | 7.5 | Actualizar markdown-it de 14.1.0 a 14.1.1 |
| 🟡 MEDIUM | CVE-2025-66400 – mdast-util-to-hast: mdast-util-to-hast | 5.3 | Actualizar mdast-util-to-hast de 13.2.0 a 13.2.1 |
| 🟡 MEDIUM | CVE-2026-33672 – picomatch: Picomatch: Data integrity c | 5.3 | Actualizar picomatch de 2.3.1 a 4.0.4, 3.0.2, 2.3.2 |
| 🟡 MEDIUM | CVE-2025-15284 – qs: qs: Denial of Service via improper | 7.5 | Actualizar qs de 6.13.0 a 6.14.1 |
| 🟡 MEDIUM | CVE-2026-33532 – yaml: yaml: Denial of Service via deep | 6.5 | Actualizar yaml de 2.8.1 a 2.8.3, 1.10.3 |

### 🌐 OWASP ZAP (DAST)

> **Tipo:** Análisis Dinámico en Tiempo de Ejecución  
> **Raw:** 6 | **Únicos:** 6 | **Deduplicados:** 0 (0.0%)

**Distribución:** 🟡 MEDIUM: **1** | 🟢 LOW: **3** | ⚪ INFO: **2**

#### 🟡🟢⚪ Medios, Bajos e Info (6)

| Severidad | Hallazgo | Endpoint | Remediación |
|---|---|---|---|
| 🟡 MEDIUM | CSP: Failure to Define Directive with No Fallback | `http://localhost:3000` | Ensure that your web server, application server, load balancer, etc. i |
| 🟢 LOW | Cookie without SameSite Attribute | `http://localhost:3000` | Ensure that the SameSite attribute is set to either 'lax' or ideally ' |
| 🟢 LOW | Permissions Policy Header Not Set | `http://localhost:3000` | Ensure that your web server, application server, load balancer, etc. i |
| 🟢 LOW | Server Leaks Information via "X-Powered-By" HTTP R | `http://localhost:3000` | Ensure that your web server, application server, load balancer, etc. i |
| ⚪ INFO | Session Management Response Identified | `http://localhost:3000` | This is an informational alert rather than a vulnerability and so ther |
| ⚪ INFO | Storable and Cacheable Content | `http://localhost:3000` | Validate that the response does not contain sensitive, personal or use |

### 🎯 Nuclei (Pentesting)

> **Tipo:** Validación Activa de Templates  
> **Raw:** 12 | **Únicos:** 4 | **Deduplicados:** 8 (66.7%)

**Distribución:** 🟡 MEDIUM: **1** | 🟢 LOW: **3**

#### 🟡🟢⚪ Medios, Bajos e Info (4)

| Severidad | Hallazgo | Endpoint | Remediación |
|---|---|---|---|
| 🟡 MEDIUM | Node.js Express NODE_ENV Development Mode | `http://localhost:3000` | Revisar: The Node.js application runs in development mode, which can e |
| 🟢 LOW | Cookies without Secure attribute - Detect | `localhost:3000` | Ensure that all cookies are set with the Secure attribute to prevent M |
| 🟢 LOW | Missing Cookie SameSite Strict | `http://localhost:3000` | Revisar: Identified cookies that lacked the samesite=strict attribute, |
| 🟢 LOW | HTTP Missing Security Headers | `http://localhost:3000` | Revisar: This template searches for missing HTTP security headers. The |

### 🔐 Semgrep (SAST)

> **Tipo:** Análisis Estático de Código  
> **Raw:** 0 | **Únicos:** 0 | **Deduplicados:** 0 (0%)

_No se encontraron hallazgos para esta herramienta._

---

## 🎓 Notas Académicas y Marco de Referencia

Este reporte fue generado automáticamente por el pipeline DevSecOps implementado como
Trabajo de Grado en la **Universidad del Valle – Sede Tuluá**.

### Marco normativo y técnico

| Estándar / Framework | Aplicación en este pipeline |
|---|---|
| **ISO/IEC 27034-1:2011** | Modelo TLOT/ALOT para la decisión de despliegue |
| **OWASP Top 10 (2021)** | Categorización de todos los hallazgos normalizados |
| **CVSS v3.1 (NIST)** | Puntuación de severidad para hallazgos de Trivy |
| **CWE/SANS Top 25** | Clasificación de debilidades en SAST y DAST |
| **MITRE ATT&CK** | Referencia para cadenas de ataque identificadas por la IA |
| **ISO/IEC 27005:2022** | Base para la calibración de niveles TLOT por criticidad |

### Herramientas integradas en el pipeline

| Herramienta | Tipo | ASC ISO/IEC 27034 | Hallazgos únicos |
|---|---|---|---|
| Semgrep | SAST | ASC-SAST-001 | 0 |
| Trivy | SCA | ASC-SCA-001 | 49 |
| OWASP ZAP | DAST | ASC-DAST-001 | 6 |
| Nuclei | Pentesting | ASC-PENTEST-001 | 4 |

### Contribución diferencial por tipo de gate

| Capacidad | Gate Tradicional | Gate con IA | Gate ISO/IEC 27034 |
|---|---|---|---|
| Detección de falsos positivos | ❌ | ✅ | ❌ |
| Análisis de explotabilidad real | ❌ | ✅ | ❌ |
| Cadenas de ataque (0 en este run) | ❌ | ✅ | ❌ |
| Blind spots de cobertura | ❌ | ✅ | ❌ |
| Fundamento normativo trazable | ❌ | ❌ | ✅ |
| Modelo de confianza (TLOT/ALOT) | ❌ | ❌ | ✅ |
| Impacto de negocio | ❌ | ✅ | ❌ |

### Limitaciones del estudio

- Pipeline validado sobre OWASP Juice Shop y FitFusion Backend (n=2 casos de estudio)
- Los valores TLOT son una interpretación cuantitativa propia de la norma, no valores prescritos por ISO/IEC 27034-1:2011
- La evaluación IA requiere validación humana para decisiones en producción
- No reemplaza una auditoría de seguridad formal ni un pentest manual

---

_Reporte generado el 2026-05-21 21:24:56 | Pipeline Run: `26253560070`_

_**Autores:** Jhojan Stiven Castaño Jejen & Juan Manuel Arango Rodas_
_**Universidad del Valle** – Ingeniería de Sistemas – 2026_
