# 🔐 Reporte de Seguridad DevSecOps
## ❌ Decisión de Despliegue: **FAIL**

---

> **Generado automáticamente por el pipeline DevSecOps – Universidad del Valle 2026**

| Campo | Valor |
|---|---|
| **Servicio** | `juice-shop` |
| **Entorno** | `staging` |
| **Criticidad de negocio** | `high` |
| **Pipeline Run** | `26253680284` |
| **Timestamp** | `2026-05-21 21:30:45` |
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
| 🔴 CRITICAL | 4 | 4.9% | `░░░░░░░░░░░░░░░` |
| 🟠 HIGH | 38 | 46.3% | `██████░░░░░░░░░` |
| 🟡 MEDIUM | 36 | 43.9% | `██████░░░░░░░░░` |
| 🟢 LOW | 4 | 4.9% | `░░░░░░░░░░░░░░░` |
| ⚪ INFO | 0 | 0.0% | `░░░░░░░░░░░░░░░` |
| ─ | **82** | **100%** | |

### Cobertura por Herramienta

> La columna **"Removidos"** indica hallazgos eliminados por deduplicación (no son falsos positivos — son instancias duplicadas de la misma vulnerabilidad).

| Herramienta | Raw | Únicos | Removidos | % Removidos | Estado |
|---|---|---|---|---|---|
| 🔐 Semgrep (SAST) | 17 | 14 | 3 | 17.6% | ✅ Ejecutado |
| 🔬 Trivy (SCA) | 74 | 63 | 11 | 14.9% | ✅ Ejecutado |
| 🌐 OWASP ZAP (DAST) | 0 | 0 | 0 | — | ⚠️ Sin hallazgos |
| 🎯 Nuclei (Pentesting) | 14 | 5 | 9 | 64.3% | ✅ Ejecutado |

### Top Categorías OWASP Top 10

| Categoría | Hallazgos | % del total | Proporción |
|---|---|---|---|
| `A06:2021 – Vulnerable and Outdated Components` | 63 | 76.8% | `█████████░░░` |
| `A05:2021 – Security Misconfiguration` | 12 | 14.6% | `█░░░░░░░░░░░` |
| `A03:2021 – Injection` | 7 | 8.5% | `█░░░░░░░░░░░` |

---

## 🔄 Metodología de Deduplicación

> El normalizador aplica deduplicación para evitar el doble conteo de vulnerabilidades detectadas por múltiples instancias de la misma herramienta.
> **Total raw:** 105 hallazgos → **Total único:** 82 hallazgos → **Eliminados:** 23 (21.9% de reducción)

### 🔬 Trivy (SCA) — Análisis de Componentes de Software

- **Raw:** 74 hallazgos detectados | **Únicos tras dedup:** 63 | **Removidos:** 11 (14.9%)
- **Criterio de dedup aplicado:** `tool + título + endpoint/archivo`

> Juice Shop instala dependencias en múltiples subdirectorios de `node_modules` (por ejemplo, `express-jwt/node_modules/lodash` y `sanitize-html/node_modules/lodash`). La misma CVE sobre el mismo paquete y versión aparece una vez por ruta, pero tras deduplicar por `CVE + paquete + target` queda una sola entrada. Los hallazgos removidos no son falsos positivos sino instancias duplicadas de la misma vulnerabilidad real.

### 🌐 OWASP ZAP (DAST) — Análisis Dinámico en Tiempo de Ejecución

- **Raw:** 0 hallazgos detectados | **Únicos tras dedup:** 0 | **Removidos:** 0 (0%)
- **Criterio de dedup aplicado:** `tool + título + endpoint/archivo`

> ZAP realiza un escaneo baseline pasivo. Cada alerta representa un tipo de misconfiguration o header faltante único — por eso la deduplicación no elimina ningún hallazgo: todas las alertas tienen títulos distintos. El conteo de instancias dentro de cada alerta indica cuántas URLs presentan el mismo problema.

### 🎯 Nuclei (Pentesting) — Validación Activa de Templates

- **Raw:** 14 hallazgos detectados | **Únicos tras dedup:** 5 | **Removidos:** 9 (64.3%)
- **Criterio de dedup aplicado:** `tool + título + endpoint/archivo`

> Nuclei ejecuta sus templates contra la URL base más todas las rutas descubiertas por el reconocimiento. El mismo template puede disparar en el mismo endpoint más de una vez dentro del mismo run, generando entradas duplicadas en el JSON de salida. Tras deduplicar por `template + endpoint`, se conserva solo una entrada por hallazgo único.

### 🔐 Semgrep (SAST) — Análisis Estático de Código

- **Raw:** 17 hallazgos detectados | **Únicos tras dedup:** 14 | **Removidos:** 3 (17.6%)
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
| **Título de la app** | `OWASP Juice Shop` |
| **Tecnologías detectadas** | _No detectadas_ |
| **Targets generados para Nuclei** | 1 URLs |

### Escaneo de Puertos (nmap)

| Puerto | Servicio | Versión | Interesante |
|---|---|---|---|
| `22` | ssh | OpenSSH 9.6p1 Ubuntu 3ubuntu13.16 (Ubunt | No |
| `3000` | ppp? |  | No |


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

Se encontraron 4 hallazgos críticos.

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
| **Fuente de datos EPSS** | FIRST.org API (57 CVEs consultados) |

### Distribución de Acciones SSVC

| Acción | Hallazgos | % | Gate | Significado |
|---|---|---|---|---|
| **Act** | `42` | 51.2% | ❌ FAIL | Explotación activa o automatizable con impacto total |
| **Attend** | `5` | 6.1% | ⚠️ CONDITIONAL | Explotación probable, requiere atención pronto |
| **Track-star** | `26` | 31.7% | ⚠️ CONDITIONAL | Monitorear activamente — riesgo controlado |
| **Track** | `9` | 11.0% | ✅ PASS | Sin explotación activa conocida |
| **Total evaluados** | `82` | 100% | ❌ **FAIL** | Decisión = acción máxima |

### Hallazgos que requieren acción inmediata (Act)

| Herramienta | Vulnerabilidad | Explotación | Automatizable | Impacto | Acción |
|---|---|---|---|---|---|
| `semgrep` | Express Sequelize Injection | poc | yes | total | **Act** |
| `semgrep` | Express Sequelize Injection | poc | yes | total | **Act** |
| `semgrep` | Express Sequelize Injection | poc | yes | total | **Act** |
| `semgrep` | Express Sequelize Injection | poc | yes | total | **Act** |
| `semgrep` | Express Sequelize Injection | poc | yes | total | **Act** |
| `semgrep` | Express Sequelize Injection | poc | yes | total | **Act** |
| `trivy` | CVE-2023-46233 – crypto-js: PBKDF2 1,000 times weaker than specif | poc | yes | total | **Act** |
| `trivy` | CVE-2020-15084 – Authorization bypass in express-jwt | poc | yes | total | **Act** |


### Métricas Formales — Dimensión Exploitation (F1 Score)

> Calculadas sobre CVEs con CISA KEV o EPSS disponible como *ground truth*.
> Metodología: Al Haddad et al. (2025) — arXiv 2510.18508.

| Métrica | Valor | Descripción |
|---|---|---|
| **Precisión** | `0.0000` | TP / (TP + FP) |
| **Recall** | `0.0000` | TP / (TP + FN) |
| **F1 Score** | `0.0000` | Media armónica precisión/recall |
| **Accuracy** | `1.0000` | (TP + TN) / total |
| CVEs evaluados | `58` | Solo CVEs con EPSS/KEV disponible |
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
| **EPSS scores obtenidos** | 57 CVEs |
| **Hallazgos clasificados SSVC** | 82 |
| **Distribución SSVC** | Act=42, Attend=5, Track*=26, Track=9 |
> **F1 Exploitation (ground truth KEV+EPSS):** `0.000` (P=0.000, R=0.000, n=58 CVEs)


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
- Hallazgos CRÍTICOS: 4 (umbral: 0)
- Hallazgos ALTOS: 38 (umbral: 5)
- Hallazgos MEDIOS: 36 (umbral: 20)

**Análisis de falsos positivos (IA):** Sin análisis contextual disponible.

> **Nota sobre ISO/IEC 27034:** el modelo TLOT/ALOT fue reemplazado por SSVC+EPSS+KEV
> para eliminar constantes arbitrarias y habilitar métricas formales. ISO/IEC 27034 se
> conserva como marco de trazabilidad normativa: cada hallazgo mantiene su `asc_id` y
> los ASCs ejecutados quedan registrados (ver sección siguiente).

---

## 📋 Hallazgos Detallados por Herramienta

### 🔬 Trivy (SCA)

> **Tipo:** Análisis de Componentes de Software  
> **Raw:** 74 | **Únicos:** 63 | **Deduplicados:** 11 (14.9%)

**Distribución:** 🔴 CRITICAL: **4** | 🟠 HIGH: **31** | 🟡 MEDIUM: **28**

#### 🔴🟠 Críticos y Altos (35)

#### 🔴 [CRITICAL] CVE-2023-46233 – crypto-js: PBKDF2 1,000 times weaker than specified in 1993 and 1.3M times weaker than current standard

| Campo | Valor |
|---|---|
| **ID** | `TRI-F0061998` |
| **Herramienta** | `TRIVY` (SCA) |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `9.1` |
| **Archivo** | `Node.js:None` |

**Descripción:** crypto-js is a JavaScript library of crypto standards. Prior to version 4.2.0, crypto-js PBKDF2 is 1,000 times weaker than originally specified in 1993, and at least 1,300,000 times weaker than current industry standard. This is because it both defaults to SHA1, a cryptographic hash algorithm considered insecure since at least 2005, and defaults to one single iteration, a 'strength' or 'difficulty

**Evidencia:** `Paquete: crypto-js v3.3.0 | Fix: 4.2.0`

**✅ Remediación:** Actualizar crypto-js de 3.3.0 a 4.2.0

---

#### 🔴 [CRITICAL] CVE-2015-9235 – nodejs-jsonwebtoken: verification step bypass with an altered token

| Campo | Valor |
|---|---|
| **ID** | `TRI-4651F9B4` |
| **Herramienta** | `TRIVY` (SCA) |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `9.8` |
| **Archivo** | `Node.js:None` |

**Descripción:** In jsonwebtoken node module before 4.2.2 it is possible for an attacker to bypass verification when a token digitally signed with an asymmetric key (RS/ES family) of algorithms but instead the attacker send a token digitally signed with a symmetric algorithm (HS* family).

**Evidencia:** `Paquete: jsonwebtoken v0.1.0 | Fix: 4.2.2`

**✅ Remediación:** Actualizar jsonwebtoken de 0.1.0 a 4.2.2

---

#### 🔴 [CRITICAL] CVE-2019-10744 – nodejs-lodash: prototype pollution in defaultsDeep function leading to modifying properties

| Campo | Valor |
|---|---|
| **ID** | `TRI-A46AFD25` |
| **Herramienta** | `TRIVY` (SCA) |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `9.1` |
| **Archivo** | `Node.js:None` |

**Descripción:** Versions of lodash lower than 4.17.12 are vulnerable to Prototype Pollution. The function defaultsDeep could be tricked into adding or modifying properties of Object.prototype using a constructor payload.

**Evidencia:** `Paquete: lodash v2.4.2 | Fix: 4.17.12`

**✅ Remediación:** Actualizar lodash de 2.4.2 a 4.17.12

---

#### 🔴 [CRITICAL] GHSA-5mrr-rgp6-x4gr – Command Injection in marsdb

| Campo | Valor |
|---|---|
| **ID** | `TRI-24C234CC` |
| **Herramienta** | `TRIVY` (SCA) |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **Archivo** | `Node.js:None` |

**Descripción:** All versions of `marsdb` are vulnerable to Command Injection. In the `DocumentMatcher` class, selectors on `$where` clauses are passed to a Function constructor unsanitized. This allows attackers to run arbitrary commands in the system when the function is executed.


## Recommendation

No fix is currently available. Consider using an alternative package until a fix is made available.

**Evidencia:** `Paquete: marsdb v0.6.11 | Fix: Not available`

**✅ Remediación:** No hay fix disponible para marsdb 0.6.11 — considerar alternativa

---

#### 🟠 [HIGH] NSWG-ECO-428 – Out-of-bounds Read

| Campo | Valor |
|---|---|
| **ID** | `TRI-7F7B48B3` |
| **Herramienta** | `TRIVY` (SCA) |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **Archivo** | `Node.js:None` |

**Descripción:** `base64url` allocates uninitialized Buffers when number is passed in input on Node.js 4.x and below

**Evidencia:** `Paquete: base64url v0.0.6 | Fix: >=3.0.0`

**✅ Remediación:** Actualizar base64url de 0.0.6 a >=3.0.0

---

#### 🟠 [HIGH] CVE-2020-15084 – Authorization bypass in express-jwt

| Campo | Valor |
|---|---|
| **ID** | `TRI-E7285D69` |
| **Herramienta** | `TRIVY` (SCA) |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `9.1` |
| **Archivo** | `Node.js:None` |

**Descripción:** In express-jwt (NPM package) up and including version 5.3.3, the algorithms entry to be specified in the configuration is not being enforced. When algorithms is not specified in the configuration, with the combination of jwks-rsa, it may lead to authorization bypass. You are affected by this vulnerability if all of the following conditions apply: - You are using express-jwt - You do not have **alg

**Evidencia:** `Paquete: express-jwt v0.1.3 | Fix: 6.0.0`

**✅ Remediación:** Actualizar express-jwt de 0.1.3 a 6.0.0

---

#### 🟠 [HIGH] CVE-2022-25881 – http-cache-semantics: Regular Expression Denial of Service (ReDoS) vulnerability

| Campo | Valor |
|---|---|
| **ID** | `TRI-80AE7B43` |
| **Herramienta** | `TRIVY` (SCA) |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `Node.js:None` |

**Descripción:** This affects versions of the package http-cache-semantics before 4.1.1. The issue can be exploited via malicious request header values sent to a server, when that server reads the cache policy from the request using this library.

**Evidencia:** `Paquete: http-cache-semantics v3.8.1 | Fix: 4.1.1`

**✅ Remediación:** Actualizar http-cache-semantics de 3.8.1 a 4.1.1

---

#### 🟠 [HIGH] CVE-2022-23539 – jsonwebtoken: Unrestricted key type could lead to legacy keys usagen

| Campo | Valor |
|---|---|
| **ID** | `TRI-297C4D46` |
| **Herramienta** | `TRIVY` (SCA) |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `8.1` |
| **Archivo** | `Node.js:None` |

**Descripción:** Versions `<=8.5.1` of `jsonwebtoken` library could be misconfigured so that legacy, insecure key types are used for signature verification. For example, DSA keys could be used with the RS256 algorithm. You are affected if you are using an algorithm and a key type other than a combination listed in the GitHub Security Advisory as unaffected. This issue has been fixed, please update to version 9.0.0

**Evidencia:** `Paquete: jsonwebtoken v0.1.0 | Fix: 9.0.0`

**✅ Remediación:** Actualizar jsonwebtoken de 0.1.0 a 9.0.0

---

#### 🟠 [HIGH] NSWG-ECO-17 – Verification Bypass

| Campo | Valor |
|---|---|
| **ID** | `TRI-58A80FD0` |
| **Herramienta** | `TRIVY` (SCA) |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **Archivo** | `Node.js:None` |

**Descripción:** It is possible for an attacker to bypass verification when "a token digitally signed with an asymetric key (RS/ES family) of algorithms but instead the attacker send a token digitally signed with a symmetric algorithm (HS* family)" [1]

**Evidencia:** `Paquete: jsonwebtoken v0.1.0 | Fix: >=4.2.2`

**✅ Remediación:** Actualizar jsonwebtoken de 0.1.0 a >=4.2.2

---

#### 🟠 [HIGH] CVE-2016-1000223 – Forgeable Public/Private Tokens

| Campo | Valor |
|---|---|
| **ID** | `TRI-6B18EB61` |
| **Herramienta** | `TRIVY` (SCA) |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `8.7` |
| **Archivo** | `Node.js:None` |

**Descripción:** Since "algorithm" isn't enforced in `jws.verify()`, a malicious user could choose what algorithm is sent to the server. If the server is expecting RSA but is sent HMAC-SHA with RSA's public key, the server will think the public key is actually an HMAC private key. This could be used to forge any data an attacker wants.

In addition, there is the `none` algorithm to be concerned about.  In versions

**Evidencia:** `Paquete: jws v0.2.6 | Fix: >=3.0.0`

**✅ Remediación:** Actualizar jws de 0.2.6 a >=3.0.0

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

**Evidencia:** `Paquete: jws v0.2.6 | Fix: 3.2.3, 4.0.1`

**✅ Remediación:** Actualizar jws de 0.2.6 a 3.2.3, 4.0.1

---

#### 🟠 [HIGH] CVE-2018-16487 – lodash: Prototype pollution in utilities function

| Campo | Valor |
|---|---|
| **ID** | `TRI-F020CA58` |
| **Herramienta** | `TRIVY` (SCA) |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `5.6` |
| **Archivo** | `Node.js:None` |

**Descripción:** A prototype pollution vulnerability was found in lodash <4.17.11 where the functions merge, mergeWith, and defaultsDeep can be tricked into adding or modifying properties of Object.prototype.

**Evidencia:** `Paquete: lodash v2.4.2 | Fix: >=4.17.11`

**✅ Remediación:** Actualizar lodash de 2.4.2 a >=4.17.11

---

#### 🟠 [HIGH] CVE-2021-23337 – nodejs-lodash: command injection via template

| Campo | Valor |
|---|---|
| **ID** | `TRI-D1DABBBE` |
| **Herramienta** | `TRIVY` (SCA) |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.2` |
| **Archivo** | `Node.js:None` |

**Descripción:** Lodash versions prior to 4.17.21 are vulnerable to Command Injection via the template function.

**Evidencia:** `Paquete: lodash v2.4.2 | Fix: 4.17.21`

**✅ Remediación:** Actualizar lodash de 2.4.2 a 4.17.21

---

#### 🟠 [HIGH] CVE-2020-8203 – nodejs-lodash: prototype pollution in zipObjectDeep function

| Campo | Valor |
|---|---|
| **ID** | `TRI-53245030` |
| **Herramienta** | `TRIVY` (SCA) |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.4` |
| **Archivo** | `Node.js:None` |

**Descripción:** Prototype pollution attack when using _.zipObjectDeep in lodash before 4.17.20.

**Evidencia:** `Paquete: lodash.set v4.3.2 | Fix: Not available`

**✅ Remediación:** No hay fix disponible para lodash.set 4.3.2 — considerar alternativa

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

**Evidencia:** `Paquete: minimatch v3.0.5 | Fix: 10.2.1, 9.0.6, 8.0.5, 7.4.7, 6.2.1, 5.1.7, 4.2.4, 3.1.3`

**✅ Remediación:** Actualizar minimatch de 3.0.5 a 10.2.1, 9.0.6, 8.0.5, 7.4.7, 6.2.1, 5.1.7, 4.2.4, 3.1.3

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

**Evidencia:** `Paquete: minimatch v3.0.5 | Fix: 10.2.3, 9.0.7, 8.0.6, 7.4.8, 6.2.2, 5.1.8, 4.2.5, 3.1.3`

**✅ Remediación:** Actualizar minimatch de 3.0.5 a 10.2.3, 9.0.7, 8.0.6, 7.4.8, 6.2.2, 5.1.8, 4.2.5, 3.1.3

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

**Evidencia:** `Paquete: minimatch v3.0.5 | Fix: 10.2.3, 9.0.7, 8.0.6, 7.4.8, 6.2.2, 5.1.8, 4.2.5, 3.1.4`

**✅ Remediación:** Actualizar minimatch de 3.0.5 a 10.2.3, 9.0.7, 8.0.6, 7.4.8, 6.2.2, 5.1.8, 4.2.5, 3.1.4

---

#### 🟠 [HIGH] CVE-2017-18214 – nodejs-moment: Regular expression denial of service

| Campo | Valor |
|---|---|
| **ID** | `TRI-6BAD1A14` |
| **Herramienta** | `TRIVY` (SCA) |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `Node.js:None` |

**Descripción:** The moment module before 2.19.3 for Node.js is prone to a regular expression denial of service via a crafted date string, a different vulnerability than CVE-2016-4055.

**Evidencia:** `Paquete: moment v2.0.0 | Fix: 2.19.3`

**✅ Remediación:** Actualizar moment de 2.0.0 a 2.19.3

---

#### 🟠 [HIGH] CVE-2022-24785 – Moment.js: Path traversal  in moment.locale

| Campo | Valor |
|---|---|
| **ID** | `TRI-1F33C497` |
| **Herramienta** | `TRIVY` (SCA) |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `Node.js:None` |

**Descripción:** Moment.js is a JavaScript date library for parsing, validating, manipulating, and formatting dates. A path traversal vulnerability impacts npm (server) users of Moment.js between versions 1.0.1 and 2.29.1, especially if a user-provided locale string is directly used to switch moment locale. This problem is patched in 2.29.2, and the patch can be applied to all affected versions. As a workaround, s

**Evidencia:** `Paquete: moment v2.0.0 | Fix: 2.29.2`

**✅ Remediación:** Actualizar moment de 2.0.0 a 2.29.2

---

#### 🟠 [HIGH] CVE-2025-47935 – Multer vulnerable to Denial of Service via memory leaks from unclosed streams

| Campo | Valor |
|---|---|
| **ID** | `TRI-C9F3D623` |
| **Herramienta** | `TRIVY` (SCA) |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `Node.js:None` |

**Descripción:** Multer is a node.js middleware for handling `multipart/form-data`. Versions prior to 2.0.0 are vulnerable to a resource exhaustion and memory leak issue due to improper stream handling. When the HTTP request stream emits an error, the internal `busboy` stream is not closed, violating Node.js stream safety guidance. This leads to unclosed streams accumulating over time, consuming memory and file de

**Evidencia:** `Paquete: multer v1.4.5-lts.2 | Fix: 2.0.0`

**✅ Remediación:** Actualizar multer de 1.4.5-lts.2 a 2.0.0

---

#### 🟠 [HIGH] CVE-2025-47944 – Multer vulnerable to Denial of Service from maliciously crafted requests

| Campo | Valor |
|---|---|
| **ID** | `TRI-239DB04C` |
| **Herramienta** | `TRIVY` (SCA) |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `Node.js:None` |

**Descripción:** Multer is a node.js middleware for handling `multipart/form-data`. A vulnerability that is present starting in version 1.4.4-lts.1 and prior to version 2.0.0 allows an attacker to trigger a Denial of Service (DoS) by sending a malformed multi-part upload request. This request causes an unhandled exception, leading to a crash of the process. Users should upgrade to version 2.0.0 to receive a patch.

**Evidencia:** `Paquete: multer v1.4.5-lts.2 | Fix: 2.0.0`

**✅ Remediación:** Actualizar multer de 1.4.5-lts.2 a 2.0.0

---

#### 🟠 [HIGH] CVE-2025-48997 – multer: Multer vulnerable to Denial of Service via unhandled exception

| Campo | Valor |
|---|---|
| **ID** | `TRI-42E99098` |
| **Herramienta** | `TRIVY` (SCA) |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `5.3` |
| **Archivo** | `Node.js:None` |

**Descripción:** Multer is a node.js middleware for handling `multipart/form-data`. A vulnerability that is present starting in version 1.4.4-lts.1 and prior to version 2.0.1 allows an attacker to trigger a Denial of Service (DoS) by sending an upload file request with an empty string field name. This request causes an unhandled exception, leading to a crash of the process. Users should upgrade to `2.0.1` to recei

**Evidencia:** `Paquete: multer v1.4.5-lts.2 | Fix: 2.0.1`

**✅ Remediación:** Actualizar multer de 1.4.5-lts.2 a 2.0.1

---

#### 🟠 [HIGH] CVE-2025-7338 – multer: Multer Denial of Service

| Campo | Valor |
|---|---|
| **ID** | `TRI-1B184DB4` |
| **Herramienta** | `TRIVY` (SCA) |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `5.3` |
| **Archivo** | `Node.js:None` |

**Descripción:** Multer is a node.js middleware for handling `multipart/form-data`. A vulnerability that is present starting in version 1.4.4-lts.1 and prior to version 2.0.2 allows an attacker to trigger a Denial of Service (DoS) by sending a malformed multi-part upload request. This request causes an unhandled exception, leading to a crash of the process. Users should upgrade to version 2.0.2 to receive a patch.

**Evidencia:** `Paquete: multer v1.4.5-lts.2 | Fix: 2.0.2`

**✅ Remediación:** Actualizar multer de 1.4.5-lts.2 a 2.0.2

---

#### 🟠 [HIGH] CVE-2026-2359 – multer: Multer: Denial of Service via dropped file upload connections

| Campo | Valor |
|---|---|
| **ID** | `TRI-2E2BD21A` |
| **Herramienta** | `TRIVY` (SCA) |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `Node.js:None` |

**Descripción:** Multer is a node.js middleware for handling `multipart/form-data`. A vulnerability in Multer prior to version 2.1.0 allows an attacker to trigger a Denial of Service (DoS) by dropping connection during file upload, potentially causing resource exhaustion. Users should upgrade to version 2.1.0 to receive a patch. No known workarounds are available.

**Evidencia:** `Paquete: multer v1.4.5-lts.2 | Fix: 2.1.0`

**✅ Remediación:** Actualizar multer de 1.4.5-lts.2 a 2.1.0

---

#### 🟠 [HIGH] CVE-2026-3304 – multer: Multer: Denial of Service via malformed requests

| Campo | Valor |
|---|---|
| **ID** | `TRI-7DBFDCE9` |
| **Herramienta** | `TRIVY` (SCA) |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `Node.js:None` |

**Descripción:** Multer is a node.js middleware for handling `multipart/form-data`. A vulnerability in Multer prior to version 2.1.0 allows an attacker to trigger a Denial of Service (DoS) by sending malformed requests, potentially causing resource exhaustion. Users should upgrade to version 2.1.0 to receive a patch. No known workarounds are available.

**Evidencia:** `Paquete: multer v1.4.5-lts.2 | Fix: 2.1.0`

**✅ Remediación:** Actualizar multer de 1.4.5-lts.2 a 2.1.0

---

#### 🟠 [HIGH] CVE-2026-3520 – multer: Multer: Denial of Service via malformed requests

| Campo | Valor |
|---|---|
| **ID** | `TRI-C6487B96` |
| **Herramienta** | `TRIVY` (SCA) |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `Node.js:None` |

**Descripción:** Multer is a node.js middleware for handling `multipart/form-data`. A vulnerability in Multer prior to version 2.1.1 allows an attacker to trigger a Denial of Service (DoS) by sending malformed requests, potentially causing stack overflow. Users should upgrade to version 2.1.1 to receive a patch. No known workarounds are available.

**Evidencia:** `Paquete: multer v1.4.5-lts.2 | Fix: 2.1.1`

**✅ Remediación:** Actualizar multer de 1.4.5-lts.2 a 2.1.1

---

#### 🟠 [HIGH] CVE-2022-25887 – sanitize-html: insecure global regular expression replacement logic may lead to ReDoS

| Campo | Valor |
|---|---|
| **ID** | `TRI-4254AA7C` |
| **Herramienta** | `TRIVY` (SCA) |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `Node.js:None` |

**Descripción:** The package sanitize-html before 2.7.1 are vulnerable to Regular Expression Denial of Service (ReDoS) due to insecure global regular expression replacement logic of HTML comment removal.

**Evidencia:** `Paquete: sanitize-html v1.4.2 | Fix: 2.7.1`

**✅ Remediación:** Actualizar sanitize-html de 1.4.2 a 2.7.1

---

#### 🟠 [HIGH] CVE-2026-33151 – socket.io: Socket.IO: Denial of Service due to excessive buffering of specially crafted packets

| Campo | Valor |
|---|---|
| **ID** | `TRI-7919FF2D` |
| **Herramienta** | `TRIVY` (SCA) |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `Node.js:None` |

**Descripción:** Socket.IO is an open source, real-time, bidirectional, event-based, communication framework. Prior to versions 3.3.5, 3.4.4, and 4.2.6, a specially crafted Socket.IO packet can make the server wait for a large number of binary attachments and buffer them, which can be exploited to make the server run out of memory. This issue has been patched in versions 3.3.5, 3.4.4, and 4.2.6.

**Evidencia:** `Paquete: socket.io-parser v4.0.5 | Fix: 3.3.5, 3.4.4, 4.2.6`

**✅ Remediación:** Actualizar socket.io-parser de 4.0.5 a 3.3.5, 3.4.4, 4.2.6

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

**Evidencia:** `Paquete: tar v4.4.19 | Fix: 7.5.3`

**✅ Remediación:** Actualizar tar de 4.4.19 a 7.5.3

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

**Evidencia:** `Paquete: tar v4.4.19 | Fix: 7.5.4`

**✅ Remediación:** Actualizar tar de 4.4.19 a 7.5.4

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

**Evidencia:** `Paquete: tar v4.4.19 | Fix: 7.5.7`

**✅ Remediación:** Actualizar tar de 4.4.19 a 7.5.7

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

**Evidencia:** `Paquete: tar v4.4.19 | Fix: 7.5.8`

**✅ Remediación:** Actualizar tar de 4.4.19 a 7.5.8

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

**Evidencia:** `Paquete: tar v4.4.19 | Fix: 7.5.10`

**✅ Remediación:** Actualizar tar de 4.4.19 a 7.5.10

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

**Evidencia:** `Paquete: tar v4.4.19 | Fix: 7.5.11`

**✅ Remediación:** Actualizar tar de 4.4.19 a 7.5.11

---

#### 🟠 [HIGH] CVE-2024-37890 – nodejs-ws: denial of service when handling a request with many HTTP headers

| Campo | Valor |
|---|---|
| **ID** | `TRI-F560A458` |
| **Herramienta** | `TRIVY` (SCA) |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `5.9` |
| **Archivo** | `Node.js:None` |

**Descripción:** ws is an open source WebSocket client and server for Node.js. A request with a number of headers exceeding theserver.maxHeadersCount threshold could be used to crash a ws server. The vulnerability was fixed in ws@8.17.1 (e55e510) and backported to ws@7.5.10 (22c2876), ws@6.2.3 (eeb76d3), and ws@5.2.4 (4abd8f6). In vulnerable versions of ws, the issue can be mitigated in the following ways: 1. Redu

**Evidencia:** `Paquete: ws v7.4.6 | Fix: 5.2.4, 6.2.3, 7.5.10, 8.17.1`

**✅ Remediación:** Actualizar ws de 7.4.6 a 5.2.4, 6.2.3, 7.5.10, 8.17.1

---

#### 🟡🟢⚪ Medios, Bajos e Info (28)

| Severidad | CVE / Advisory | CVSS | Remediación |
|---|---|---|---|
| 🟡 MEDIUM | CVE-2026-4046 – glibc: glibc: Denial of Service via ico | 5.3 | Actualizar libc6 de 2.41-12+deb13u2 a 2.41-12+deb13u3 |
| 🟡 MEDIUM | CVE-2026-4437 – glibc: glibc: Incorrect DNS response pa | 6.5 | Actualizar libc6 de 2.41-12+deb13u2 a 2.41-12+deb13u3 |
| 🟡 MEDIUM | CVE-2026-5435 – glibc: glibc: Out-of-bounds write via T | 5.9 | No hay fix disponible para libc6 2.41-12+deb13u2 — considerar alternat |
| 🟡 MEDIUM | CVE-2026-5450 – glibc: glibc: Heap Buffer Overflow in ` | 5.0 | No hay fix disponible para libc6 2.41-12+deb13u2 — considerar alternat |
| 🟡 MEDIUM | CVE-2026-5928 – glibc: glibc: Information disclosure or | 5.0 | No hay fix disponible para libc6 2.41-12+deb13u2 — considerar alternat |
| 🟡 MEDIUM | CVE-2026-6238 – glibc: glibc: Application crash or unin | 6.5 | No hay fix disponible para libc6 2.41-12+deb13u2 — considerar alternat |
| 🟡 MEDIUM | CVE-2026-27171 – zlib: zlib: Denial of Service via infi | 5.5 | No hay fix disponible para zlib1g 1:1.3.dfsg+really1.3.1-1+b1 — consid |
| 🟡 MEDIUM | GHSA-rvg8-pwq2-xj7q – Out-of-bounds Read in base64url | None | Actualizar base64url de 0.0.6 a 3.0.0 |
| 🟡 MEDIUM | CVE-2022-41940 – engine.io: Specially crafted HTTP requ | 6.5 | Actualizar engine.io de 4.1.2 a 3.6.1, 6.2.1 |
| 🟡 MEDIUM | CVE-2026-31808 – file-type: file-type: Denial of Servic | 5.3 | Actualizar file-type de 16.5.4 a 21.3.1 |
| 🟡 MEDIUM | CVE-2022-33987 – nodejs-got: missing verification of re | 5.3 | Actualizar got de 8.3.2 a 12.1.0, 11.8.5 |
| 🟡 MEDIUM | CVE-2022-23540 – jsonwebtoken: Insecure default algorit | 7.6 | Actualizar jsonwebtoken de 0.1.0 a 9.0.0 |
| 🟡 MEDIUM | CVE-2022-23541 – jsonwebtoken: Insecure implementation  | 6.3 | Actualizar jsonwebtoken de 0.1.0 a 9.0.0 |
| 🟡 MEDIUM | CVE-2026-2950 – lodash: Lodash: Prototype pollution all | 5.3 | Actualizar lodash de 2.4.2 a 4.18.0 |
| 🟡 MEDIUM | CVE-2016-4055 – moment.js: regular expression denial of | 6.5 | Actualizar moment de 2.0.0 a >=2.11.2 |
| 🟡 MEDIUM | CVE-2021-23771 – Sandbox escape in notevil and argencod | 6.5 | No hay fix disponible para notevil 1.3.3 — considerar alternativa |
| 🟡 MEDIUM | CVE-2016-1000237 – XSS - Sanitization not applied recur | 6.1 | Actualizar sanitize-html de 1.4.2 a >=1.4.3 |
| 🟡 MEDIUM | CVE-2017-16016 – Cross-Site Scripting in sanitize-html | 6.1 | Actualizar sanitize-html de 1.4.2 a 1.11.4 |
| 🟡 MEDIUM | CVE-2019-25225 – sanitize-html: sanitize-html cross sit | 6.1 | Actualizar sanitize-html de 1.4.2 a 2.0.0-beta |
| 🟡 MEDIUM | CVE-2021-26539 – sanitize-html: improper handling of in | 5.3 | Actualizar sanitize-html de 1.4.2 a 2.3.1 |
| 🟡 MEDIUM | CVE-2021-26540 – sanitize-html: improper validation of  | 5.3 | Actualizar sanitize-html de 1.4.2 a 2.3.2 |
| 🟡 MEDIUM | CVE-2024-21501 – sanitize-html: Information Exposure wh | 5.3 | Actualizar sanitize-html de 1.4.2 a 2.12.1 |
| 🟡 MEDIUM | NSWG-ECO-154 – Cross Site Scripting | None | Actualizar sanitize-html de 1.4.2 a >=1.11.4 |
| 🟡 MEDIUM | CVE-2024-38355 – socket.io: Unhandled 'error' event | 7.3 | Actualizar socket.io de 3.1.2 a 2.5.1, 4.6.2 |
| 🟡 MEDIUM | CVE-2023-32695 – socket.io parser is a socket.io encode | 7.5 | Actualizar socket.io-parser de 4.0.5 a 4.2.3, 3.4.3, 3.3.4 |
| 🟡 MEDIUM | CVE-2024-28863 – node-tar: denial of service while pars | 6.5 | Actualizar tar de 4.4.19 a 6.2.1 |
| 🟡 MEDIUM | CVE-2026-41907 – uuid: uuid: Out-of-bounds write vulner | 7.5 | Actualizar uuid de 8.3.2 a 11.1.1, 12.0.1, 13.0.1 |
| 🟡 MEDIUM | CVE-2026-45736 – ws is an open source WebSocket client  | 7.5 | Actualizar ws de 8.17.1 a 8.20.1 |

### 🌐 OWASP ZAP (DAST)

> **Tipo:** Análisis Dinámico en Tiempo de Ejecución  
> **Raw:** 0 | **Únicos:** 0 | **Deduplicados:** 0 (0%)

_No se encontraron hallazgos para esta herramienta._

### 🎯 Nuclei (Pentesting)

> **Tipo:** Validación Activa de Templates  
> **Raw:** 14 | **Únicos:** 5 | **Deduplicados:** 9 (64.3%)

**Distribución:** 🟡 MEDIUM: **1** | 🟢 LOW: **4**

#### 🟡🟢⚪ Medios, Bajos e Info (5)

| Severidad | Hallazgo | Endpoint | Remediación |
|---|---|---|---|
| 🟡 MEDIUM | Prometheus Metrics - Detect | `http://localhost:3000/metrics` | Revisar: Prometheus metrics page was detected. |
| 🟢 LOW | Public Swagger API - Detect | `http://localhost:3000/api-docs/swagger.json` | Revisar: Public Swagger API was detected.
 |
| 🟢 LOW | HTTP Missing Security Headers | `http://localhost:3000` | Revisar: This template searches for missing HTTP security headers. The |
| 🟢 LOW | Add DOM EventListener - Detection | `http://localhost:3000` | Revisar: Identifies the use of JavaScript addEventListener calls in th |
| 🟢 LOW | OWASP Juice Shop | `http://localhost:3000` | Revisar: No description |

### 🔐 Semgrep (SAST)

> **Tipo:** Análisis Estático de Código  
> **Raw:** 17 | **Únicos:** 14 | **Deduplicados:** 3 (17.6%)

**Distribución:** 🟠 HIGH: **7** | 🟡 MEDIUM: **7**

#### 🔴🟠 Críticos y Altos (7)

#### 🟠 [HIGH] Express Sequelize Injection

| Campo | Valor |
|---|---|
| **ID** | `SEM-C2F5F78D` |
| **Herramienta** | `SEMGREP` (SAST) |
| **Categoría OWASP** | A03:2021 – Injection |
| **CWE** | `["CWE-89: Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection')"]` |
| **Archivo** | `source_to_scan/data/static/codefixes/dbSchemaChallenge_1.ts:5` |

**Descripción:** Detected a sequelize statement that is tainted by user-input. This could lead to SQL injection if the variable is user-controlled and is not properly sanitized. In order to prevent SQL injection, it is recommended to use parameterized queries or prepared statements.

**Evidencia:** `requires login`

**✅ Remediación:** Revisar y corregir el patrón identificado en source_to_scan/data/static/codefixes/dbSchemaChallenge_1.ts:5

---

#### 🟠 [HIGH] Express Sequelize Injection

| Campo | Valor |
|---|---|
| **ID** | `SEM-C24E4FA5` |
| **Herramienta** | `SEMGREP` (SAST) |
| **Categoría OWASP** | A03:2021 – Injection |
| **CWE** | `["CWE-89: Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection')"]` |
| **Archivo** | `source_to_scan/data/static/codefixes/dbSchemaChallenge_3.ts:11` |

**Descripción:** Detected a sequelize statement that is tainted by user-input. This could lead to SQL injection if the variable is user-controlled and is not properly sanitized. In order to prevent SQL injection, it is recommended to use parameterized queries or prepared statements.

**Evidencia:** `requires login`

**✅ Remediación:** Revisar y corregir el patrón identificado en source_to_scan/data/static/codefixes/dbSchemaChallenge_3.ts:11

---

#### 🟠 [HIGH] Express Sequelize Injection

| Campo | Valor |
|---|---|
| **ID** | `SEM-D55F36AA` |
| **Herramienta** | `SEMGREP` (SAST) |
| **Categoría OWASP** | A03:2021 – Injection |
| **CWE** | `["CWE-89: Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection')"]` |
| **Archivo** | `source_to_scan/data/static/codefixes/unionSqlInjectionChallenge_1.ts:6` |

**Descripción:** Detected a sequelize statement that is tainted by user-input. This could lead to SQL injection if the variable is user-controlled and is not properly sanitized. In order to prevent SQL injection, it is recommended to use parameterized queries or prepared statements.

**Evidencia:** `requires login`

**✅ Remediación:** Revisar y corregir el patrón identificado en source_to_scan/data/static/codefixes/unionSqlInjectionChallenge_1.ts:6

---

#### 🟠 [HIGH] Express Sequelize Injection

| Campo | Valor |
|---|---|
| **ID** | `SEM-ECDF67FF` |
| **Herramienta** | `SEMGREP` (SAST) |
| **Categoría OWASP** | A03:2021 – Injection |
| **CWE** | `["CWE-89: Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection')"]` |
| **Archivo** | `source_to_scan/data/static/codefixes/unionSqlInjectionChallenge_3.ts:10` |

**Descripción:** Detected a sequelize statement that is tainted by user-input. This could lead to SQL injection if the variable is user-controlled and is not properly sanitized. In order to prevent SQL injection, it is recommended to use parameterized queries or prepared statements.

**Evidencia:** `requires login`

**✅ Remediación:** Revisar y corregir el patrón identificado en source_to_scan/data/static/codefixes/unionSqlInjectionChallenge_3.ts:10

---

#### 🟠 [HIGH] Express Sequelize Injection

| Campo | Valor |
|---|---|
| **ID** | `SEM-DC7965AE` |
| **Herramienta** | `SEMGREP` (SAST) |
| **Categoría OWASP** | A03:2021 – Injection |
| **CWE** | `["CWE-89: Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection')"]` |
| **Archivo** | `source_to_scan/routes/login.ts:34` |

**Descripción:** Detected a sequelize statement that is tainted by user-input. This could lead to SQL injection if the variable is user-controlled and is not properly sanitized. In order to prevent SQL injection, it is recommended to use parameterized queries or prepared statements.

**Evidencia:** `requires login`

**✅ Remediación:** Revisar y corregir el patrón identificado en source_to_scan/routes/login.ts:34

---

#### 🟠 [HIGH] Express Sequelize Injection

| Campo | Valor |
|---|---|
| **ID** | `SEM-542CE9D6` |
| **Herramienta** | `SEMGREP` (SAST) |
| **Categoría OWASP** | A03:2021 – Injection |
| **CWE** | `["CWE-89: Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection')"]` |
| **Archivo** | `source_to_scan/routes/search.ts:23` |

**Descripción:** Detected a sequelize statement that is tainted by user-input. This could lead to SQL injection if the variable is user-controlled and is not properly sanitized. In order to prevent SQL injection, it is recommended to use parameterized queries or prepared statements.

**Evidencia:** `requires login`

**✅ Remediación:** Revisar y corregir el patrón identificado en source_to_scan/routes/search.ts:23

---

#### 🟠 [HIGH] Code String Concat

| Campo | Valor |
|---|---|
| **ID** | `SEM-D65564A9` |
| **Herramienta** | `SEMGREP` (SAST) |
| **Categoría OWASP** | A05:2021 – Security Misconfiguration |
| **CWE** | `["CWE-95: Improper Neutralization of Directives in Dynamically Evaluated Code ('Eval Injection')"]` |
| **Archivo** | `source_to_scan/routes/userProfile.ts:62` |

**Descripción:** Found data from an Express or Next web request flowing to `eval`. If this data is user-controllable this can lead to execution of arbitrary system commands in the context of your application process. Avoid `eval` whenever possible.

**Evidencia:** `requires login`

**✅ Remediación:** Revisar y corregir el patrón identificado en source_to_scan/routes/userProfile.ts:62

---

#### 🟡🟢⚪ Medios, Bajos e Info (7)

| Severidad | Hallazgo | Endpoint | Remediación |
|---|---|---|---|
| 🟡 MEDIUM | Raw Html Format | `None` | Revisar y corregir el patrón identificado en source_to_scan/routes/cha |
| 🟡 MEDIUM | Express Res Sendfile | `None` | Revisar y corregir el patrón identificado en source_to_scan/routes/fil |
| 🟡 MEDIUM | Express Res Sendfile | `None` | Revisar y corregir el patrón identificado en source_to_scan/routes/key |
| 🟡 MEDIUM | Express Res Sendfile | `None` | Revisar y corregir el patrón identificado en source_to_scan/routes/log |
| 🟡 MEDIUM | Express Res Sendfile | `None` | Revisar y corregir el patrón identificado en source_to_scan/routes/qua |
| 🟡 MEDIUM | Express Open Redirect | `None` | Revisar y corregir el patrón identificado en source_to_scan/routes/red |
| 🟡 MEDIUM | Express Check Directory Listing | `None` | Revisar y corregir el patrón identificado en source_to_scan/server.ts: |

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
| Semgrep | SAST | ASC-SAST-001 | 14 |
| Trivy | SCA | ASC-SCA-001 | 63 |
| OWASP ZAP | DAST | ASC-DAST-001 | 0 |
| Nuclei | Pentesting | ASC-PENTEST-001 | 5 |

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

_Reporte generado el 2026-05-21 21:30:45 | Pipeline Run: `26253680284`_

_**Autores:** Jhojan Stiven Castaño Jejen & Juan Manuel Arango Rodas_
_**Universidad del Valle** – Ingeniería de Sistemas – 2026_
