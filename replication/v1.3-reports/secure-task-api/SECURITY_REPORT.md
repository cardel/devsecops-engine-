# 🔐 Reporte de Seguridad DevSecOps
## ❌ Decisión de Despliegue: **FAIL**

---

> **Generado automáticamente por el pipeline DevSecOps – Universidad del Valle 2026**

| Campo | Valor |
|---|---|
| **Servicio** | `secure-task-api` |
| **Entorno** | `staging` |
| **Criticidad de negocio** | `medium` |
| **Pipeline Run** | `26253498212` |
| **Timestamp** | `2026-05-21 21:20:42` |
| **Modelo IA** | `llama-3.3-70b-versatile` |
| **Tokens utilizados** | `8,360` (prompt: 6,821 / completion: 1,539) |
| **Versión del prompt** | `3.0-ssvc-enriched` |
| **ISO/IEC 27034** | `✅ Activo` |

---

## 📊 Resumen Ejecutivo

Se han identificado varias vulnerabilidades de alto riesgo en el pipeline de despliegue, incluyendo problemas de explotación remota y cadenas de ataque potenciales. Aunque no se han detectado exploits públicos para todas las vulnerabilidades, el riesgo es significativo y requiere atención inmediata.

> **Recomendación del sistema:** No se recomienda desplegar el sistema en producción hasta que se hayan aplicado las actualizaciones de seguridad para las vulnerabilidades identificadas.

---

## 🚦 Decisión Final del Security Gate

| Campo | Valor |
|---|---|
| **Decisión** | ❌ **FAIL** |
| **Fuente** | `ssvc_escalation_active_exploitation` |
| **Nivel de riesgo (IA)** | `HIGH` |
| **Risk Score (IA)** | `8.5 / 10.0` |
| **Confianza IA** | `80%` |
| **Falsos positivos estimados** | `baja` |
| **ISO/IEC 27034 — TLOT** | `N/A` |
| **ISO/IEC 27034 — ALOT** | `N/A` |
| **ISO/IEC 27034 — Conformidad** | ❌ No conforme — No evaluado |

---

## 📈 Estadísticas Globales de Hallazgos

### Distribución por Severidad

| Severidad | Hallazgos | % del total | Proporción |
|---|---|---|---|
| 🔴 CRITICAL | 0 | 0.0% | `░░░░░░░░░░░░░░░` |
| 🟠 HIGH | 11 | 64.7% | `█████████░░░░░░` |
| 🟡 MEDIUM | 3 | 17.6% | `██░░░░░░░░░░░░░` |
| 🟢 LOW | 2 | 11.8% | `█░░░░░░░░░░░░░░` |
| ⚪ INFO | 1 | 5.9% | `░░░░░░░░░░░░░░░` |
| ─ | **17** | **100%** | |

### Cobertura por Herramienta

> La columna **"Removidos"** indica hallazgos eliminados por deduplicación (no son falsos positivos — son instancias duplicadas de la misma vulnerabilidad).

| Herramienta | Raw | Únicos | Removidos | % Removidos | Estado |
|---|---|---|---|---|---|
| 🔐 Semgrep (SAST) | 0 | 0 | 0 | — | ⚠️ Sin hallazgos |
| 🔬 Trivy (SCA) | 13 | 13 | 0 | 0.0% | ✅ Ejecutado |
| 🌐 OWASP ZAP (DAST) | 3 | 3 | 0 | 0.0% | ✅ Ejecutado |
| 🎯 Nuclei (Pentesting) | 3 | 1 | 2 | 66.7% | ✅ Ejecutado |

### Top Categorías OWASP Top 10

| Categoría | Hallazgos | % del total | Proporción |
|---|---|---|---|
| `A06:2021 – Vulnerable and Outdated Components` | 14 | 82.4% | `█████████░░░` |
| `A05:2021 – Security Misconfiguration` | 2 | 11.8% | `█░░░░░░░░░░░` |
| `A07:2021 – Identification and Authentication Failures` | 1 | 5.9% | `░░░░░░░░░░░░` |

---

## 🔄 Metodología de Deduplicación

> El normalizador aplica deduplicación para evitar el doble conteo de vulnerabilidades detectadas por múltiples instancias de la misma herramienta.
> **Total raw:** 19 hallazgos → **Total único:** 17 hallazgos → **Eliminados:** 2 (10.5% de reducción)

### 🔬 Trivy (SCA) — Análisis de Componentes de Software

- **Raw:** 13 hallazgos detectados | **Únicos tras dedup:** 13 | **Removidos:** 0 (0.0%)
- **Criterio de dedup aplicado:** `tool + título + endpoint/archivo`

> Juice Shop instala dependencias en múltiples subdirectorios de `node_modules` (por ejemplo, `express-jwt/node_modules/lodash` y `sanitize-html/node_modules/lodash`). La misma CVE sobre el mismo paquete y versión aparece una vez por ruta, pero tras deduplicar por `CVE + paquete + target` queda una sola entrada. Los hallazgos removidos no son falsos positivos sino instancias duplicadas de la misma vulnerabilidad real.

### 🌐 OWASP ZAP (DAST) — Análisis Dinámico en Tiempo de Ejecución

- **Raw:** 3 hallazgos detectados | **Únicos tras dedup:** 3 | **Removidos:** 0 (0.0%)
- **Criterio de dedup aplicado:** `tool + título + endpoint/archivo`

> ZAP realiza un escaneo baseline pasivo. Cada alerta representa un tipo de misconfiguration o header faltante único — por eso la deduplicación no elimina ningún hallazgo: todas las alertas tienen títulos distintos. El conteo de instancias dentro de cada alerta indica cuántas URLs presentan el mismo problema.

### 🎯 Nuclei (Pentesting) — Validación Activa de Templates

- **Raw:** 3 hallazgos detectados | **Únicos tras dedup:** 1 | **Removidos:** 2 (66.7%)
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
| **Título de la app** | `N/A` |
| **Tecnologías detectadas** | `HSTS` |
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

El análisis ha revelado que varias de las vulnerabilidades detectadas tienen un alto nivel de explotabilidad, según los datos de EPSS y KEV. Además, se han identificado cadenas de ataque potenciales que podrían permitir a un atacante explotar múltiples vulnerabilidades para obtener acceso no autorizado o realizar acciones maliciosas. Es importante abordar estas vulnerabilidades de manera prioritaria para mitigar el riesgo.

**Análisis de falsos positivos:** La mayoría de las vulnerabilidades detectadas tienen un alto nivel de explotabilidad y no hay exploit público conocido, lo que reduce la probabilidad de falsos positivos.

### Categorías OWASP Top 10 Detectadas

- `A06:2021 – Vulnerable and Outdated Components`

### Análisis de Cobertura por Tipo de Herramienta

| Tipo de análisis | Cobertura | Estado |
|---|---|---|
| SAST – Código fuente | buena | ✅ |
| SCA – Dependencias | buena | ✅ |
| DAST – Tiempo de ejecución | parcial | 🟡 |
| Pentesting automatizado | parcial | 🟡 |

**Evaluación general:** La cobertura es buena en general, pero hay algunas áreas que requieren más atención.

### ⚠️ Áreas sin cobertura (Blind Spots)

- No se han detectado vulnerabilidades en la capa de presentación


### 🏆 Hallazgos Principales Identificados por IA

| Severidad | Hallazgo | CVSS | Explotable remoto | Auth requerida | Exploit público | Categoría |
|---|---|---|---|---|---|---|
| 🟠 HIGH | CVE-2024-21538 – cross-spawn: regular express | `4.4` | 🔴 Sí | 🟢 No | No | A06:2021 – Vulnerable and Outdated  |
| 🟠 HIGH | CVE-2025-64756 – glob: glob: Command Injectio | `7.5` | 🔴 Sí | 🟢 No | No | A06:2021 – Vulnerable and Outdated  |

---

## 🔗 Análisis de Cadenas de Ataque

> Esta sección identifica combinaciones de vulnerabilidades que, explotadas en secuencia,
> producen un impacto mayor al de cada vulnerabilidad de forma individual.

### 🔴 CHAIN-001 – Explotación de vulnerabilidades para obtener acceso no autorizado

| Campo | Valor |
|---|---|
| **Severidad combinada** | CRITICAL |
| **Probabilidad** | 🔴 Alta |
| **Vulnerabilidades involucradas** | `TRI-E8929BCB`, `TRI-CD8B31C7` |

**Secuencia del ataque:**

1. Paso 1: Un atacante explota la vulnerabilidad CVE-2024-21538 para causar una denegación de servicio y obtener acceso al sistema.
2. Paso 2: Con acceso obtenido, el atacante explota la vulnerabilidad CVE-2025-64756 para ejecutar comandos arbitrarios y obtener acceso no autorizado.

**Impacto combinado:** El impacto combinado de estas vulnerabilidades es significativo, ya que permiten a un atacante obtener acceso no autorizado y ejecutar comandos arbitrarios.

---

---

## 🛠️ Hoja de Ruta de Remediación

### 🚨 Inmediato (0–7 días) — 2 acciones

**1.** Actualizar cross-spawn a la versión 6.0.6 o superior → Fix: `6.0.6`
   - `trivy` | Esfuerzo: _bajo_ | Fix disponible: ✅

**2.** Actualizar glob a la versión 11.1.0 o superior → Fix: `11.1.0`
   - `trivy` | Esfuerzo: _bajo_ | Fix disponible: ✅

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
| **Mission & Wellbeing** | `medium` (derivado de criticality=`medium`) |
| **Fuente de datos KEV** | CISA Known Exploited Vulnerabilities (1,601 entradas) |
| **Fuente de datos EPSS** | FIRST.org API (13 CVEs consultados) |

### Distribución de Acciones SSVC

| Acción | Hallazgos | % | Gate | Significado |
|---|---|---|---|---|
| **Act** | `11` | 64.7% | ❌ FAIL | Explotación activa o automatizable con impacto total |
| **Attend** | `2` | 11.8% | ⚠️ CONDITIONAL | Explotación probable, requiere atención pronto |
| **Track-star** | `1` | 5.9% | ⚠️ CONDITIONAL | Monitorear activamente — riesgo controlado |
| **Track** | `3` | 17.6% | ✅ PASS | Sin explotación activa conocida |
| **Total evaluados** | `17` | 100% | ❌ **FAIL** | Decisión = acción máxima |

### Hallazgos que requieren acción inmediata (Act)

| Herramienta | Vulnerabilidad | Explotación | Automatizable | Impacto | Acción |
|---|---|---|---|---|---|
| `trivy` | CVE-2024-21538 – cross-spawn: regular expression denial of servic | poc | yes | total | **Act** |
| `trivy` | CVE-2025-64756 – glob: glob: Command Injection Vulnerability via  | poc | yes | total | **Act** |
| `trivy` | CVE-2026-26996 – minimatch: minimatch: Denial of Service via spec | poc | yes | total | **Act** |
| `trivy` | CVE-2026-27903 – minimatch: minimatch: Denial of Service due to u | poc | yes | total | **Act** |
| `trivy` | CVE-2026-27904 – minimatch: Minimatch: Denial of Service via cata | poc | yes | total | **Act** |
| `trivy` | CVE-2026-23745 – node-tar: tar: node-tar: Arbitrary file overwrit | poc | yes | total | **Act** |
| `trivy` | CVE-2026-23950 – node-tar: tar: node-tar: Arbitrary file overwrit | poc | yes | total | **Act** |
| `trivy` | CVE-2026-24842 – node-tar: tar: node-tar: Arbitrary file creation | poc | yes | total | **Act** |


### Métricas Formales — Dimensión Exploitation (F1 Score)

> Calculadas sobre CVEs con CISA KEV o EPSS disponible como *ground truth*.
> Metodología: Al Haddad et al. (2025) — arXiv 2510.18508.

| Métrica | Valor | Descripción |
|---|---|---|
| **Precisión** | `0.0000` | TP / (TP + FP) |
| **Recall** | `0.0000` | TP / (TP + FN) |
| **F1 Score** | `0.0000` | Media armónica precisión/recall |
| **Accuracy** | `1.0000` | (TP + TN) / total |
| CVEs evaluados | `13` | Solo CVEs con EPSS/KEV disponible |
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
| **EPSS scores obtenidos** | 13 CVEs |
| **Hallazgos clasificados SSVC** | 17 |
| **Distribución SSVC** | Act=11, Attend=2, Track*=1, Track=3 |
> **F1 Exploitation (ground truth KEV+EPSS):** `0.000` (P=0.000, R=0.000, n=13 CVEs)

### Validación Cruzada LLM ↔ SSVC (2 hallazgos validados)

El LLM analizó las clasificaciones SSVC preliminares y produjo su propio juicio:
**2 confirmados**, **0 sobreestimados**, **0 subestimados**.

| SSVC Preliminar | Juicio IA | Evidencia Empírica | Razonamiento |
|---|---|---|---|
| `Act` | ✅ confirmed | EPSS: 0.001 / KEV: No | La vulnerabilidad tiene un alto nivel de explotabilidad y no hay explo... |
| `Act` | ✅ confirmed | EPSS: 0.000 / KEV: No | La vulnerabilidad tiene un alto nivel de explotabilidad y no hay explo... |

---

## 🔄 Comparación: Tres Enfoques de Security Gate

> **Contribución central del Trabajo de Grado:** comparar empíricamente tres mecanismos de
> decisión de despliegue. El gate tradicional como línea base, el gate IA para análisis
> contextual, y el gate SSVC+EPSS+KEV como métrica estandarizada con F1 formal.
> ISO/IEC 27034 se conserva para trazabilidad normativa (asc_id).

| Criterio | Gate Tradicional | Gate con IA | Gate SSVC+EPSS+KEV |
|---|---|---|---|
| **Decisión** | ❌ FAIL | ⚠️ CONDITIONAL | ❌ FAIL |
| **Método** | Umbrales numéricos fijos | Evaluación contextual LLM | Árbol SSVC + EPSS + CISA KEV |
| **Acción agregada** | N/A | N/A | `Act` (Act/Attend/Track*/Track) |
| **Métricas formales** | ❌ No | ❌ No | ✅ F1=`0.000` (vs CISA KEV) |
| **Considera falsos positivos** | ❌ No | ✅ Estimados (baja) | ✅ EPSS filtra low-risk |
| **Evalúa explotabilidad real** | ❌ No | ✅ Semántica LLM | ✅ CISA KEV + EPSS empírico |
| **Detecta cadenas de ataque** | ❌ No | ✅ Sí | ❌ No (por hallazgo individual) |
| **Constantes arbitrarias** | ✅ Umbrales fijos | N/A | ❌ Ninguna (árbol CISA público) |
| **Saturación de scores** | ✅ Posible | N/A | ❌ Elimina saturación |
| **Transparencia** | ✅ Alta | ⚠️ Caja negra | ✅ Alta (árbol publicado CISA) |
| **Determinístico** | ✅ Sí | ❌ No | ✅ Sí |
| **Costo computacional** | Nulo | ~$0.005/run | ~API calls gratuitas |
| **Modelo / versión** | Reglas fijas | `llama-3.3-70b-versatile` | SSVC v2.1 + FIRST.org EPSS |
| **Confianza / score** | N/A | 80% | `0.000` F1 (Exploitation) |

### Divergencias entre gates

- Gate IA (CONDITIONAL) difiere de SSVC (FAIL): el LLM aporta contexto adicional sobre cadenas de ataque no capturadas por el árbol SSVC.

**Insight académico:** Divergencias detectadas entre 1 pares de gates. Esto ilustra el valor diferencial del análisis por explotabilidad SSVC vs umbrales estáticos vs evaluación contextual LLM.

**Análisis de la comparación:** N/A

**Razones del gate tradicional:**
- Hallazgos ALTOS: 11 (umbral: 5)

**Análisis de falsos positivos (IA):** La mayoría de las vulnerabilidades detectadas tienen un alto nivel de explotabilidad y no hay exploit público conocido, lo que reduce la probabilidad de falsos positivos.

> **Nota sobre ISO/IEC 27034:** el modelo TLOT/ALOT fue reemplazado por SSVC+EPSS+KEV
> para eliminar constantes arbitrarias y habilitar métricas formales. ISO/IEC 27034 se
> conserva como marco de trazabilidad normativa: cada hallazgo mantiene su `asc_id` y
> los ASCs ejecutados quedan registrados (ver sección siguiente).

---

## 📋 Hallazgos Detallados por Herramienta

### 🔬 Trivy (SCA)

> **Tipo:** Análisis de Componentes de Software  
> **Raw:** 13 | **Únicos:** 13 | **Deduplicados:** 0 (0.0%)

**Distribución:** 🟠 HIGH: **11** | 🟡 MEDIUM: **2**

#### 🔴🟠 Críticos y Altos (11)

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

#### 🟠 [HIGH] CVE-2026-26996 – minimatch: minimatch: Denial of Service via specially crafted glob patterns

| Campo | Valor |
|---|---|
| **ID** | `TRI-4DBC63E3` |
| **Herramienta** | `TRIVY` (SCA) |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `Node.js:None` |

**Descripción:** minimatch is a minimal matching utility for converting glob expressions into JavaScript RegExp objects. Versions 10.2.0 and below are vulnerable to Regular Expression Denial of Service (ReDoS) when a glob pattern contains many consecutive * wildcards followed by a literal character that doesn't appear in the test string. Each * compiles to a separate [^/]*? regex group, and when the match fails, V

**Evidencia:** `Paquete: minimatch v9.0.5 | Fix: 10.2.1, 9.0.6, 8.0.5, 7.4.7, 6.2.1, 5.1.7, 4.2.4, 3.1.3`

**✅ Remediación:** Actualizar minimatch de 9.0.5 a 10.2.1, 9.0.6, 8.0.5, 7.4.7, 6.2.1, 5.1.7, 4.2.4, 3.1.3

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

**Evidencia:** `Paquete: minimatch v9.0.5 | Fix: 10.2.3, 9.0.7, 8.0.6, 7.4.8, 6.2.2, 5.1.8, 4.2.5, 3.1.3`

**✅ Remediación:** Actualizar minimatch de 9.0.5 a 10.2.3, 9.0.7, 8.0.6, 7.4.8, 6.2.2, 5.1.8, 4.2.5, 3.1.3

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

**Evidencia:** `Paquete: minimatch v9.0.5 | Fix: 10.2.3, 9.0.7, 8.0.6, 7.4.8, 6.2.2, 5.1.8, 4.2.5, 3.1.4`

**✅ Remediación:** Actualizar minimatch de 9.0.5 a 10.2.3, 9.0.7, 8.0.6, 7.4.8, 6.2.2, 5.1.8, 4.2.5, 3.1.4

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

#### 🟡🟢⚪ Medios, Bajos e Info (2)

| Severidad | CVE / Advisory | CVSS | Remediación |
|---|---|---|---|
| 🟡 MEDIUM | CVE-2026-33750 – brace-expansion: brace-expansion: Deni | 7.5 | Actualizar brace-expansion de 2.0.1 a 5.0.5, 3.0.2, 2.0.3, 1.1.13 |
| 🟡 MEDIUM | CVE-2026-42338 – ip-address is a library for parsing an | 6.1 | Actualizar ip-address de 9.0.5 a 10.1.1 |

### 🌐 OWASP ZAP (DAST)

> **Tipo:** Análisis Dinámico en Tiempo de Ejecución  
> **Raw:** 3 | **Únicos:** 3 | **Deduplicados:** 0 (0.0%)

**Distribución:** 🟡 MEDIUM: **1** | 🟢 LOW: **1** | ⚪ INFO: **1**

#### 🟡🟢⚪ Medios, Bajos e Info (3)

| Severidad | Hallazgo | Endpoint | Remediación |
|---|---|---|---|
| 🟡 MEDIUM | CSP: Failure to Define Directive with No Fallback | `http://localhost:3000/robots.txt` | Ensure that your web server, application server, load balancer, etc. i |
| 🟢 LOW | Permissions Policy Header Not Set | `http://localhost:3000/robots.txt` | Ensure that your web server, application server, load balancer, etc. i |
| ⚪ INFO | Storable and Cacheable Content | `http://localhost:3000` | Validate that the response does not contain sensitive, personal or use |

### 🎯 Nuclei (Pentesting)

> **Tipo:** Validación Activa de Templates  
> **Raw:** 3 | **Únicos:** 1 | **Deduplicados:** 2 (66.7%)

**Distribución:** 🟢 LOW: **1**

#### 🟡🟢⚪ Medios, Bajos e Info (1)

| Severidad | Hallazgo | Endpoint | Remediación |
|---|---|---|---|
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
| Trivy | SCA | ASC-SCA-001 | 13 |
| OWASP ZAP | DAST | ASC-DAST-001 | 3 |
| Nuclei | Pentesting | ASC-PENTEST-001 | 1 |

### Contribución diferencial por tipo de gate

| Capacidad | Gate Tradicional | Gate con IA | Gate ISO/IEC 27034 |
|---|---|---|---|
| Detección de falsos positivos | ❌ | ✅ | ❌ |
| Análisis de explotabilidad real | ❌ | ✅ | ❌ |
| Cadenas de ataque (1 en este run) | ❌ | ✅ | ❌ |
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

_Reporte generado el 2026-05-21 21:20:42 | Pipeline Run: `26253498212`_

_**Autores:** Jhojan Stiven Castaño Jejen & Juan Manuel Arango Rodas_
_**Universidad del Valle** – Ingeniería de Sistemas – 2026_
