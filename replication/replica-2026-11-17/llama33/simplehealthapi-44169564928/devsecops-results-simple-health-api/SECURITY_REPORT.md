# 🔐 Reporte de Seguridad DevSecOps
## ⚠️ Decisión de Despliegue: **CONDITIONAL**

---

> **Generado automáticamente por el DevSecOps Engine v1.3 — Universidad del Valle 2026**

| Campo | Valor |
|---|---|
| **Servicio** | `simple-health-api` |
| **Entorno** | `staging` |
| **Criticidad de negocio** | `low` |
| **Pipeline Run** | `44169564928` |
| **Timestamp** | `2026-11-17 20:35:23` |
| **Modelo IA** | `meta-llama/llama-3.3-70b-instruct` |
| **Tokens utilizados** | `9,864` (prompt: 8,397 / completion: 1,467) |
| **Motor IA híbrido** | ✅ Motor híbrido activo |
| **ISO/IEC 27034 — Trazabilidad** | ✅ 2/2 ASC obligatorios ejecutados |

---

## 📊 Resumen Ejecutivo

Se han identificado varias vulnerabilidades de alta severidad en el pipeline de DevSecOps, principalmente relacionadas con componentes vulnerables y desactualizados. Aunque no se han encontrado exploits públicos para todas ellas, el riesgo de explotación es considerable. Se requiere una mitigación urgente para evitar posibles ataques.

> **Recomendación del sistema:** Se recomienda proceder con el despliegue después de mitigar las vulnerabilidades identificadas y realizar un seguimiento continuo para asegurarse de que no surjan nuevas amenazas.

---

## 🚦 Decisión Final del Security Gate

| Campo | Valor |
|---|---|
| **Decisión** | ⚠️ **CONDITIONAL** |
| **Fuente** | `ai_assisted` |
| **Nivel de riesgo (IA)** | `HIGH` |
| **Risk Score (IA)** | `0.7 / 10.0` |
| **Confianza IA** | `80%` |
| **Falsos positivos estimados** | `baja` |
| **ISO/IEC 27034 — Trazabilidad ANF** | `2/2` ASC obligatorios ejecutados (ver sección ISO/IEC 27034) |

### ⚠️ Condiciones para despliegue

- Mitigar las vulnerabilidades identificadas en openssl, musl, zlib, y otras bibliotecas antes de proceder con el despliegue.

---

## 📈 Estadísticas Globales de Hallazgos

### Distribución por Severidad

| Severidad | Hallazgos | % del total | Proporción |
|---|---|---|---|
| 🔴 CRITICAL | 1 | 1.9% | `░░░░░░░░░░░░░░░` |
| 🟠 HIGH | 25 | 48.1% | `███████░░░░░░░░` |
| 🟡 MEDIUM | 22 | 42.3% | `██████░░░░░░░░░` |
| 🟢 LOW | 3 | 5.8% | `░░░░░░░░░░░░░░░` |
| ⚪ INFO | 1 | 1.9% | `░░░░░░░░░░░░░░░` |
| ─ | **52** | **100%** | |

### Cobertura por Herramienta y ASC ISO/IEC 27034

> Cada herramienta tiene asignado un ASC (Application Security Control) de ISO/IEC 27034.
> La columna **Removidos** indica duplicados eliminados, no falsos positivos.

| Herramienta | ASC ISO 27034 | Raw | Únicos | Removidos | % Dedup | Estado |
|---|---|---|---|---|---|---|
| 🔐 Semgrep (SAST) | `ASC-SAST-001` | 0 | 0 | 0 | — | ⚠️ Sin hallazgos |
| 🔬 Trivy (SCA) | `ASC-SCA-001` | 58 | 48 | 10 | 17.2% | ✅ Ejecutado |
| 🌐 OWASP ZAP (DAST) | `ASC-DAST-001` | 2 | 2 | 0 | 0.0% | ✅ Ejecutado |
| 🎯 Nuclei (Pentesting) | `ASC-PENTEST-001` | 7 | 2 | 5 | 71.4% | ✅ Ejecutado |

### Top 5 Categorías OWASP Top 10

| Categoría | Hallazgos | % del total | Proporción |
|---|---|---|---|
| `A06:2021 – Vulnerable and Outdated Components` | 49 | 94.2% | `███████████░` |
| `A05:2021 – Security Misconfiguration` | 2 | 3.8% | `░░░░░░░░░░░░` |
| `A03:2021 – Injection` | 1 | 1.9% | `░░░░░░░░░░░░` |

---

## 🔄 Metodología de Deduplicación

> El normalizador aplica deduplicación para evitar el doble conteo de vulnerabilidades
> detectadas por múltiples instancias de la misma herramienta.
>
> **Total raw:** 67 hallazgos → **Total único:** 52 → **Eliminados:** 15 (22.4% de reducción)

### 🔬 Trivy (SCA) — Análisis de Componentes de Software

- **Raw:** 58 | **Únicos:** 48 | **Removidos:** 10 (17.2%)
- **Criterio:** `tool + título + endpoint/archivo`

> La misma CVE sobre el mismo paquete puede aparecer una vez por ruta de instalación. Tras deduplicar por CVE + paquete + target queda una sola entrada. Los removidos son instancias duplicadas, no falsos positivos.

### 🌐 OWASP ZAP (DAST) — Análisis Dinámico en Ejecución

- **Raw:** 2 | **Únicos:** 2 | **Removidos:** 0 (0.0%)
- **Criterio:** `tool + título + endpoint/archivo`

> ZAP realiza escaneo baseline pasivo. Cada alerta representa un tipo de misconfiguration único — por eso la deduplicación raramente elimina hallazgos: todas las alertas suelen tener títulos distintos.

### 🎯 Nuclei (Pentesting) — Validación Activa de Templates

- **Raw:** 7 | **Únicos:** 2 | **Removidos:** 5 (71.4%)
- **Criterio:** `tool + título + endpoint/archivo`

> Nuclei puede disparar el mismo template en el mismo endpoint varias veces dentro del mismo run. Tras deduplicar por template + endpoint se conserva solo una entrada por hallazgo único.

### 🔐 Semgrep (SAST) — Análisis Estático de Código

- **Raw:** 0 | **Únicos:** 0 | **Removidos:** 0 (0%)
- **Criterio:** `tool + título + endpoint/archivo`

> Semgrep analiza el código fuente del repositorio consumidor. La deduplicación elimina la misma regla disparada en múltiples archivos del mismo módulo, conservando solo la primera ocurrencia por regla + ruta.

---

## 🕵️ Fase de Reconocimiento Activo

> El reconocimiento activo descubre la superficie de ataque real antes del escaneo
> dinámico, enriqueciendo los targets de Nuclei y ZAP.

| Campo | Valor |
|---|---|
| **URL objetivo** | `http://localhost:3000` |
| **Host** | `localhost` |
| **Puerto** | `3000` |
| **WAF detectado** | ✅ Sí — Generic |
| **Servidor** | `No detectado` |
| **Tecnologías** | `HSTS` |
| **Targets generados para Nuclei** | 1 URLs |

### Puertos detectados (nmap)

| Puerto | Servicio | Versión | Interesante |
|---|---|---|---|
| `22` | ssh | OpenSSH 10.2p1 Ubuntu 2ubuntu3.8 (Ubuntu | No |
| `3000` | ppp? |  | No |


### Rutas descubiertas

_No se ejecutó descubrimiento de rutas._


### Headers de seguridad HTTP

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


### Superficie de ataque

| Severidad | Tipo | Detalle |
|---|---|---|
| 🟡 MEDIUM | `missing_security_headers` | Headers faltantes: content-security-policy, strict-transport-security, x-frame-options, x-content-ty |


---

## 🤖 Evaluación Detallada por IA

### Razonamiento Técnico

El análisis ha revelado 25 hallazgos de alta severidad, incluyendo vulnerabilidades en openssl, musl, zlib, y otras bibliotecas. La mayoría de estas vulnerabilidades tienen un puntaje CVSS alto y se consideran explotables, aunque no necesariamente de forma remota sin autenticación. La clasificación SSVC preliminar y los scores EPSS sugieren un riesgo significativo, especialmente para CVE-2026-45447 y CVE-2026-107891, que tienen scores EPSS de 0.04 y 0.0055, respectivamente.

**Análisis de falsos positivos:** La mayoría de los hallazgos se basan en vulnerabilidades conocidas y verificadas, lo que reduce la probabilidad de falsos positivos.

### Categorías OWASP Top 10 Detectadas

- `A06:2021 – Vulnerable and Outdated Components`

### Cobertura por Tipo de Herramienta

| Tipo de análisis | Cobertura | Estado |
|---|---|---|
| SAST – Código fuente | buena | ✅ |
| SCA – Dependencias | buena | ✅ |
| DAST – Tiempo de ejecución | parcial | 🟡 |
| Pentesting automatizado | parcial | 🟡 |

**Evaluación general:** La cobertura de las herramientas de seguridad es buena en general, pero hay algunas áreas que requieren más atención, especialmente en pruebas de penetración y análisis de vulnerabilidades dinámicas.

### ⚠️ Áreas sin cobertura (Blind Spots)

- Riesgo de ataques de denegación de servicio no cubierto por las herramientas actuales.


### 🏆 Hallazgos Principales Identificados por IA

| Severidad | Hallazgo | CVSS | Remoto | Auth | Exploit | Categoría |
|---|---|---|---|---|---|---|
| 🟠 HIGH | CVE-2026-45447 – openssl: Heap Use-After-Free | `8.1` | 🔴 Sí | 🟢 No | No | A06:2021 – Vulnerable and Outdated  |

---

## 🔗 Análisis de Cadenas de Ataque

> Esta sección identifica combinaciones de vulnerabilidades que, explotadas en secuencia,
> producen un impacto mayor al de cada vulnerabilidad de forma individual.

### 🔴 CHAIN-001 — Explotación de vulnerabilidades en openssl y musl para obtener acceso no autorizado

| Campo | Valor |
|---|---|
| **Severidad combinada** | CRITICAL |
| **Probabilidad** | 🔴 Alta |
| **Vulnerabilidades involucradas** | `TRI-0542FEFE`, `TRI-9B5681BF` |

**Secuencia del ataque:**

1. Paso 1: El atacante explota CVE-2026-14456 para causar una denegación de servicio en el servidor.
2. Paso 2: Con el servidor vulnerable, el atacante explota CVE-2026-45447 para obtener ejecución de código arbitrario.
3. Paso 3: Resultado final: El atacante obtiene acceso no autorizado al sistema y puede comprometer datos sensibles.

**Impacto combinado:** El impacto combinado de estas vulnerabilidades es significativamente mayor que el de cada una por separado, ya que permiten al atacante obtener acceso no autorizado y ejecutar código arbitrario en el servidor.

---

---

## 🛠️ Hoja de Ruta de Remediación

### 🚨 Inmediato (0–7 días) — 2 acciones

**1.** Actualizar openssl a la versión más reciente → Fix: `3.5.8-r0`
   - `trivy` | Esfuerzo: _bajo_ | Fix disponible: ✅

**2.** Actualizar musl a la versión más reciente → Fix: `1.2.7`
   - `trivy` | Esfuerzo: _bajo_ | Fix disponible: ✅

---

## 🔬 Gate SSVC + EPSS + CISA KEV

> **Tercer mecanismo de decisión del pipeline.** Reemplaza el modelo TLOT/ALOT que
> dependía de constantes arbitrarias (0.50/0.65/0.80/0.95) y saturaba en ALOT=0.35
> en todos los casos evaluados. SSVC v2.1 fue publicado por CISA/SEI-CERT y no
> requiere constantes propias.
>
> **Referencias:** Al Haddad et al. (2025), Kausar et al. (2025), Yoon et al. (2023).

### Resultado del Gate SSVC

| Indicador | Valor |
|---|---|
| **Decisión** | ⚠️ **CONDITIONAL** |
| **Acción agregada** | `Attend` (máximo sobre todos los hallazgos evaluados) |
| **Mission & Wellbeing** | `low` (derivado de `criticality=low`) |
| **CISA KEV** | 1,782 entradas consultadas |
| **EPSS** | 48 CVEs consultados vía FIRST.org API |

### Distribución de Acciones SSVC

| Acción | Hallazgos | % | Gate | Significado operativo |
|---|---|---|---|---|
| **Act** | `0` | 0.0% | ❌ FAIL | Explotación activa o automatizable con impacto total |
| **Attend** | `28` | 53.8% | ⚠️ CONDITIONAL | Explotación probable a corto plazo |
| **Track*** | `8` | 15.4% | ⚠️ CONDITIONAL | Monitoreo activo — riesgo controlado |
| **Track** | `16` | 30.8% | ✅ PASS | Sin explotación activa conocida |
| **Total evaluados** | `52` | 100% | ⚠️ **CONDITIONAL** | Decisión = acción máxima |

### Hallazgos que requieren acción inmediata (Act)

| Herramienta | Vulnerabilidad | Explotación | Automatizable | Impacto | Acción |
|---|---|---|---|---|---|
| — | Sin hallazgos Act — bajo perfil de explotación | — | — | — | PASS |


### 📊 Métricas Formales — Dimensión Exploitation (F1 Score)

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
> **Nota:** hallazgos sin CVE ID (Semgrep/ZAP) excluidos del cálculo formal por ausencia
> de ground truth verificable en EPSS/KEV.


### Por qué SSVC reemplaza a TLOT/ALOT

| Aspecto | TLOT/ALOT (reemplazado) | SSVC + EPSS + KEV (actual) |
|---|---|---|
| Constantes | 0.50/0.65/0.80/0.95 definidas por autores | Árbol publicado por CISA — sin constantes propias |
| Saturación | ALOT = 0.35 idéntico en todos los casos | Track/Attend/Act varían por hallazgo |
| Métricas formales | Imposible (sin ground truth) | F1, precisión, recall vs CISA KEV + EPSS |
| Respaldo normativo | ISO/IEC 27034 §7.3.4 (sin valores) | SSVC v2.1 CISA/SEI-CERT (publicado) |


---

## 🤖 Evidencia del Motor IA Híbrido v1.3

> **Base académica:** Al Haddad et al. (2025) – arXiv 2510.18508
>
> Evaluación híbrida: LLM enriquecido con clasificaciones SSVC preliminares y datos empíricos EPSS/CISA KEV. El LLM puede validar o corregir las clasificaciones SSVC con razonamiento contextual.

### Datos enviados al LLM en esta corrida

Antes de invocar al modelo de lenguaje, `ai_engine.py` ejecutó `ssvc_gate.py` y
construyó un prompt enriquecido con las clasificaciones SSVC preliminares, scores EPSS
y estado CISA KEV por hallazgo. El LLM recibió evidencia empírica verificable junto
con la descripción técnica de cada hallazgo y su `asc_id` de trazabilidad ISO/IEC 27034.

| Campo del prompt | Valor enviado al LLM |
|---|---|
| **Modelo LLM** | `meta-llama/llama-3.3-70b-instruct` |
| **Versión del prompt** | `3.0-ssvc-enriched` (indica prompt enriquecido con SSVC/EPSS/KEV) |
| **Tokens de prompt** | `8,397` |
| **Tokens de completion** | `1,467` |
| **Contexto SSVC activo** | ✅ Sí — el LLM recibió clasificaciones SSVC por hallazgo |
| **CISA KEV consultado** | 1,782 entradas (fuente: cisa.gov) |
| **EPSS consultado** | 48 CVEs (fuente: FIRST.org API) |
| **Hallazgos clasificados SSVC** | 52 |
| **Distribución SSVC pre-LLM** | Act=0, Attend=28, Track*=8, Track=16 |
| **F1 Exploitation** | `0.0000` (P=0.0000, R=0.0000, n=48 CVEs) |

### Datos de trazabilidad ISO/IEC 27034 incluidos en el prompt

Cada hallazgo enviado al LLM incluye su `asc_id`, que vincula la vulnerabilidad
al control de seguridad de aplicación que la detectó. Esto permite al LLM razonar
sobre la cobertura normativa dentro de su evaluación contextual.

| Tool type | ASC enviado al LLM | Significado normativo |
|---|---|---|
| SAST (Semgrep) | `ASC-SAST-001` | Control de análisis estático — ISO/IEC 27034-1 Annex A |
| SCA (Trivy) | `ASC-SCA-001` | Control de composición de software — ISO/IEC 27034-1 Annex A |
| DAST (ZAP) | `ASC-DAST-001` | Control de análisis dinámico — ISO/IEC 27034-1 Annex A |
| Pentest (Nuclei) | `ASC-PENTEST-001` | Control de pruebas activas — ISO/IEC 27034-1 Annex A |

### Respuesta del LLM — Validación cruzada SSVC (2 hallazgos)

El LLM analizó las clasificaciones SSVC preliminares y emitió su propio juicio:
**2 confirmado(s)**, **0 sobreestimado(s)**, **0 subestimado(s)**.

| ID | Hallazgo | SSVC prelim. | Juicio IA | EPSS | En KEV | Razonamiento del LLM |
|---|---|---|---|---|---|---|
| `TRI-0542FEFE` | CVE-2026-14456 – openssl: OpenSSL: Denia | `Attend` | ✅ **confirmed** | `0.0073` | No | La clasificación SSVC como Attend se confirma debido al score EPSS y la naturaleza de la v... |
| `TRI-9B5681BF` | CVE-2026-45447 – openssl: Heap Use-After | `Attend` | ✅ **confirmed** | `0.0400` | No | La clasificación SSVC como Attend se confirma debido al score EPSS alto y la gravedad de l... |


> **Interpretación:** `confirmed` significa que el LLM valida la clasificación SSVC
> con el contexto de la aplicación. `overestimated` indica que el LLM considera que
> el riesgo real es menor al que sugieren las heurísticas CWE. `underestimated`
> indica lo contrario.

---

## 🔄 Comparación: Tres Enfoques del Security Gate

> **Contribución central del Trabajo de Grado:** comparar empíricamente tres mecanismos
> de decisión de despliegue sobre los mismos hallazgos normalizados. ISO/IEC 27034 se
> conserva exclusivamente para trazabilidad normativa (campo `asc_id`) — ver sección
> siguiente. No opera como cuarto gate de decisión.

| Criterio | Gate Tradicional | Gate con IA | Gate SSVC+EPSS+KEV |
|---|---|---|---|
| **Decisión** | ❌ FAIL | ⚠️ CONDITIONAL | ⚠️ CONDITIONAL |
| **Método** | Umbrales numéricos fijos | LLM con contexto SSVC/EPSS/KEV | Árbol SSVC v2.1 + EPSS + CISA KEV |
| **Acción agregada SSVC** | N/A | N/A | `Attend` |
| **Métricas formales** | ❌ No | ❌ No | ✅ F1 = `0.000` |
| **Evalúa explotabilidad real** | ❌ No | ✅ Semántica LLM | ✅ CISA KEV + EPSS empírico |
| **Detecta cadenas de ataque** | ❌ No | ✅ Sí | ❌ Por hallazgo individual |
| **Considera falsos positivos** | ❌ No | ✅ Estimados (baja) | ✅ EPSS filtra low-risk |
| **Constantes arbitrarias** | ✅ Umbrales fijos | N/A | ❌ Ninguna |
| **Determinístico** | ✅ Sí | ❌ No | ✅ Sí |
| **Costo por run** | ~$0 | ~$0.005 | ~$0 (APIs gratuitas) |
| **Trazabilidad ISO/IEC 27034** | ❌ No | ❌ No | ✅ Vía `asc_id` (ver sección siguiente) |

### Divergencias entre gates

- Gate tradicional (FAIL) difiere de SSVC (CONDITIONAL): el análisis por explotabilidad real produce una decisión diferente al conteo estático.

**Insight académico:** Divergencias detectadas entre 1 pares de gates. Esto ilustra el valor diferencial del análisis por explotabilidad SSVC vs umbrales estáticos vs evaluación contextual LLM.

**Análisis comparativo:** N/A

**Razones del gate tradicional:**
- Hallazgos CRÍTICOS: 1 (umbral: 0)
- Hallazgos ALTOS: 25 (umbral: 5)
- Hallazgos MEDIOS: 22 (umbral: 20)

---

## 📋 Trazabilidad Normativa ISO/IEC 27034

**Estado de cumplimiento: ✅ **CUMPLIDO** — todos los controles obligatorios se ejecutaron**

ISO/IEC 27034-1:2011 exige que cada aplicación defina un **ANF** (*Application Normative
Framework*) con los controles de seguridad obligatorios según su nivel de criticidad.
Para este servicio con `criticality=low` el ANF requiere 2 control(es)
obligatorio(s). Los 2 control(es) restante(s) son opcionales y se ejecutaron
como cobertura adicional.

### Resultado por control de seguridad

**✅ ASC-SAST-001** (Semgrep OSS) — Control obligatorio  
Análisis estático de código fuente: se ejecutó correctamente y **no detectó vulnerabilidades** en este contexto. Este es el resultado esperado en una aplicación bien configurada.

**🟡 ASC-SCA-001** (Trivy) — Control obligatorio  
Análisis de componentes y dependencias (CVEs): se ejecutó y **detectó 48 hallazgo(s)** (1 CRITICAL, 25 HIGH, 22 MEDIUM). Los hallazgos están documentados en la sección de detalle.

**ℹ️ ASC-DAST-001** (OWASP ZAP) — Control opcional  
Análisis dinámico en tiempo de ejecución: se ejecutó y **detectó 2 hallazgo(s)** (1 LOW, 1 INFO). Los hallazgos están documentados en la sección de detalle.

**ℹ️ ASC-PENTEST-001** (Nuclei v3) — Control opcional  
Validación activa con templates de pentest: se ejecutó y **detectó 2 hallazgo(s)** (2 LOW). Los hallazgos están documentados en la sección de detalle.


### Resumen de cobertura ANF

| ASC | Herramienta | Obligatoriedad | Estado | Hallazgos | Severidades |
|---|---|---|---|---|---|
| `ASC-SAST-001` | Semgrep OSS | ✅ Obligatorio | ✅ Ejecutado | 0 | Sin hallazgos |
| `ASC-SCA-001` | Trivy | ✅ Obligatorio | ✅ Ejecutado | 48 | 🔴C:1 / 🟠H:25 / 🟡M:22 |
| `ASC-DAST-001` | OWASP ZAP | ⚪ Opcional | ✅ Ejecutado | 2 | 🟢L:1 / ⚪I:1 |
| `ASC-PENTEST-001` | Nuclei v3 | ⚪ Opcional | ✅ Ejecutado | 2 | 🟢L:2 |



> **ANF generado por:** `detector.py` según `criticality=low` y `language=generic` — ✅ generado automáticamente  
> **Política aplicada:** a mayor criticidad declarada, más controles son obligatorios.
> Para `low`: SAST + SCA obligatorios. Para `high` o `critical`: los 4 controles son obligatorios.

### Cómo se operacionaliza la norma en el pipeline

ISO/IEC 27034 no prescribe valores numéricos — define el marco. El pipeline lo
implementa en tres puntos concretos y auditables:

| Punto | Dónde ocurre | Evidencia en esta corrida |
|---|---|---|
| **1. ANF** | `detector.py` → `scan_config.json` | 2 ASC obligatorios definidos para `criticality=low` |
| **2. asc_id** | `normalizer.py` → `findings.json` | Cada hallazgo etiquetado con el ASC que lo detectó |
| **3. Auditoría** | Este reporte | 2/2 controles obligatorios verificados |

---

## 📋 Hallazgos Detallados por Herramienta

### 🔬 Trivy (SCA) — `ASC-SCA-001`

> **Tipo:** Análisis de Componentes de Software  
> **Raw:** 58 | **Únicos:** 48 | **Deduplicados:** 10 (17.2%)

**Distribución:** 🔴 CRITICAL: **1** | 🟠 HIGH: **25** | 🟡 MEDIUM: **22**

#### 🔴🟠 Críticos y Altos (26)

#### 🔴 [CRITICAL] CVE-2026-59873 – tar: node-tar: Denial of Service via crafted gzip bomb

| Campo | Valor |
|---|---|
| **ID** | `TRI-DCAD29A2` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `Node.js:None` |

**Descripción:** node-tar is a tar archive manipulation library for Node.js. Prior to 7.5.19, node-tar does not enforce hard upper bounds on total decompressed data, entry counts, or decompression ratio in extraction and parsing paths such as src/extract.ts, allowing a small crafted gzip bomb to exhaust disk space and CPU. This issue is fixed in version 7.5.19.

**Evidencia:** `Paquete: tar v6.2.1 | Fix: 7.5.19`

**✅ Remediación:** Actualizar tar de 6.2.1 a 7.5.19

---

#### 🟠 [HIGH] CVE-2026-14456 – openssl: OpenSSL: Denial of Service via unbounded memory growth in QUIC server

| Campo | Valor |
|---|---|
| **ID** | `TRI-0542FEFE` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `ghcr.io/cardel/simplehealthapi:1fdabff6cb4e4de63fe0f04851baed094e129479 (alpine 3.23.4):None` |

**Descripción:** Issue summary: When an OpenSSL QUIC server (Listener SSL object) processes
valid QUIC Initial packets for unknown destination connection IDs, it
can allocate and queue new incoming channels without enforcing any limit.

Impact summary: A remote peer that can make many Initial packets reach the
server listener faster than the application accepts connections, can cause the
memory allocated to store 

**Evidencia:** `Paquete: libcrypto3 v3.5.6-r0 | Fix: 3.5.8-r0`

**✅ Remediación:** Actualizar libcrypto3 de 3.5.6-r0 a 3.5.8-r0

---

#### 🟠 [HIGH] CVE-2026-45447 – openssl: Heap Use-After-Free in OpenSSL PKCS7_verify()

| Campo | Valor |
|---|---|
| **ID** | `TRI-9B5681BF` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `8.1` |
| **Archivo** | `ghcr.io/cardel/simplehealthapi:1fdabff6cb4e4de63fe0f04851baed094e129479 (alpine 3.23.4):None` |

**Descripción:** Issue summary: A specially crafted PKCS#7 or S/MIME signed message could
trigger a use-after-free during PKCS#7 signature verification.

Impact summary: A use-after-free may result in process crashes, heap
corruption, or potentially remote code execution.

When processing a PKCS#7 or S/MIME signed message, if the SignedData
digestAlgorithms field is present as an empty ASN.1 SET, OpenSSL may
incor

**Evidencia:** `Paquete: libcrypto3 v3.5.6-r0 | Fix: 3.5.7-r0`

**✅ Remediación:** Actualizar libcrypto3 de 3.5.6-r0 a 3.5.7-r0

---

#### 🟠 [HIGH] CVE-2026-107891 – musl: musl: Arbitrary code execution via integer overflow in regcomp

| Campo | Valor |
|---|---|
| **ID** | `TRI-4F8EA83C` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `8.1` |
| **Archivo** | `ghcr.io/cardel/simplehealthapi:1fdabff6cb4e4de63fe0f04851baed094e129479 (alpine 3.23.4):None` |

**Descripción:** musl libc before 1.2.7, when an untrusted regular expression is used with regcomp, has multiple integer overflows, possibly leading to incorrect allocation sizes and out-of-bounds heap writes.

**Evidencia:** `Paquete: musl v1.2.5-r23 | Fix: 1.2.5-r24`

**✅ Remediación:** Actualizar musl de 1.2.5-r23 a 1.2.5-r24

---

#### 🟠 [HIGH] CVE-2026-85091 – zlib: zlib: Heap buffer overflow in gz_vacate() allows arbitrary code execution

| Campo | Valor |
|---|---|
| **ID** | `TRI-079E45C5` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `8.1` |
| **Archivo** | `ghcr.io/cardel/simplehealthapi:1fdabff6cb4e4de63fe0f04851baed094e129479 (alpine 3.23.4):None` |

**Descripción:** zlib 1.2.11 through 1.3.2 contains a heap buffer overflow: after an underlying write() fails, gz_write() returns without resetting strm.next_in, leaving it pointed at the caller's buffer. A later gz* write call then derives a position from the stale pointer and writes past a heap allocation; any write() failure reaches it, including EPIPE on a blocking descriptor, and in versions before 1.3.1.2 th

**Evidencia:** `Paquete: zlib v1.3.2-r0 | Fix: 1.3.2-r1`

**✅ Remediación:** Actualizar zlib de 1.3.2-r0 a 1.3.2-r1

---

#### 🟠 [HIGH] CVE-2026-102276 – brace-expansion: brace-expansion: Denial of Service via stack exhaustion from crafted brace patterns

| Campo | Valor |
|---|---|
| **ID** | `TRI-5D0E3AAB` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `Node.js:None` |

**Descripción:** The brace-expansion library generates arbitrary strings containing a common prefix and suffix. Prior to 1.1.19, 2.1.5, 3.0.7, and 5.0.10, crafted brace patterns can exhaust the native stack in parseCommaParts because parseCommaParts recursively processes the remainder once per brace group and uses push.apply to pass every element of a very large comma-part array as a function argument. Patterns co

**Evidencia:** `Paquete: brace-expansion v2.0.1 | Fix: 5.0.10, 3.0.7, 2.1.5, 1.1.19`

**✅ Remediación:** Actualizar brace-expansion de 2.0.1 a 5.0.10, 3.0.7, 2.1.5, 1.1.19

---

#### 🟠 [HIGH] CVE-2026-102278 – brace-expansion: brace-expansion: Denial of Service via uncontrolled recursion in nested brace patterns

| Campo | Valor |
|---|---|
| **ID** | `TRI-938E85DD` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `6.5` |
| **Archivo** | `Node.js:None` |

**Descripción:** The brace-expansion library generates arbitrary strings containing a common prefix and suffix. Prior to 1.1.20, 2.1.6, 3.0.8, and 5.0.11, deeply nested brace groups cause expand_() to recurse once per nesting level at comma-member and single-set expansion sites, exhausting the native stack before output limits can apply and potentially terminating the Node.js process. expand_ performs uncontrolled

**Evidencia:** `Paquete: brace-expansion v2.0.1 | Fix: 5.0.11, 3.0.8, 2.1.6, 1.1.20`

**✅ Remediación:** Actualizar brace-expansion de 2.0.1 a 5.0.11, 3.0.8, 2.1.6, 1.1.20

---

#### 🟠 [HIGH] CVE-2026-13149 – brace-expansion: Brace-expansion: Denial of Service due to exponential-time complexity

| Campo | Valor |
|---|---|
| **ID** | `TRI-ABB52ACB` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `Node.js:None` |

**Descripción:** brace-expansion through 5.0.6 is vulnerable to denial of service. The expand() function exhibits exponential-time complexity in the number of consecutive non-expanding '{}' brace groups. An attacker who passes a crafted string to expand(), directly or transitively, can cause significant CPU consumption and event-loop blocking. The max option does not mitigate this, as it bounds the output size rat

**Evidencia:** `Paquete: brace-expansion v2.0.1 | Fix: 5.0.7, 1.1.16, 2.1.2`

**✅ Remediación:** Actualizar brace-expansion de 2.0.1 a 5.0.7, 1.1.16, 2.1.2

---

#### 🟠 [HIGH] CVE-2026-14257 – brace-expansion: Brace-expansion: Denial of Service via memory exhaustion in expand() function

| Campo | Valor |
|---|---|
| **ID** | `TRI-578E2971` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `Node.js:None` |

**Descripción:** brace-expansion through 5.0.7 is vulnerable to denial of service via memory exhaustion. The expand() function limits the number of results with a max option (default 100,000) but does not bound the length of each result string. By chaining multiple brace groups, an attacker keeps the result count under the limit while making each result progressively longer, so total memory scales with both count 

**Evidencia:** `Paquete: brace-expansion v2.0.1 | Fix: 5.0.8, 3.0.3, 2.1.3, 1.1.17`

**✅ Remediación:** Actualizar brace-expansion de 2.0.1 a 5.0.8, 3.0.3, 2.1.3, 1.1.17

---

#### 🟠 [HIGH] CVE-2026-69152 – brace-expansion: DoS via unbounded intermediate arrays, bypassing the CVE-2026-14257 mitigation

| Campo | Valor |
|---|---|
| **ID** | `TRI-20A31272` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `Node.js:None` |

**Descripción:** The brace-expansion library generates arbitrary strings containing a common prefix and suffix. Prior to 1.1.18, 2.1.4, 3.0.6, and 5.0.9, expand() does not apply maxLength while constructing comma-alternative intermediate arrays or padded sequences, allowing attacker-controlled input to exhaust memory or block the event loop. The fix for CVE-2026-14257 is bypassed by the vulnerability. This issue i

**Evidencia:** `Paquete: brace-expansion v2.0.1 | Fix: 1.1.18, 2.1.4, 3.0.6, 5.0.9`

**✅ Remediación:** Actualizar brace-expansion de 2.0.1 a 1.1.18, 2.1.4, 3.0.6, 5.0.9

---

#### 🟠 [HIGH] CVE-2024-21538 – cross-spawn: regular expression denial of service

| Campo | Valor |
|---|---|
| **ID** | `TRI-E8929BCB` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
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
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `Node.js:None` |

**Descripción:** Glob matches files using patterns the shell uses. Starting in version 10.2.0 and prior to versions 10.5.0 and 11.1.0, the glob CLI contains a command injection vulnerability in its -c/--cmd option that allows arbitrary command execution when processing files with malicious names. When glob -c <command> <patterns> are used, matched filenames are passed to a shell with shell: true, enabling shell me

**Evidencia:** `Paquete: glob v10.4.2 | Fix: 11.1.0, 10.5.0`

**✅ Remediación:** Actualizar glob de 10.4.2 a 11.1.0, 10.5.0

---

#### 🟠 [HIGH] CVE-2026-69192 – ip-address: ip-address: Inconsistent IP address parsing leads to Server-Side Request Forgery (SSRF) and trust-boundary bypass

| Campo | Valor |
|---|---|
| **ID** | `TRI-87B07886` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `8.6` |
| **Archivo** | `Node.js:None` |

**Descripción:** ip-address is a library for parsing and manipulating IPv4 and IPv6 addresses in JavaScript. Prior to 10.3.1, Address4 accepts an octet written with a leading zero and decodes it as decimal, while the WHATWG URL host parser, inet_aton, and getaddrinfo all decode a leading zero as octal. The library and the network stack therefore disagree about which host a string names. new Address4('012.0.0.1') r

**Evidencia:** `Paquete: ip-address v9.0.5 | Fix: 10.3.1`

**✅ Remediación:** Actualizar ip-address de 9.0.5 a 10.3.1

---

#### 🟠 [HIGH] CVE-2026-26996 – minimatch: minimatch: Denial of Service via specially crafted glob patterns

| Campo | Valor |
|---|---|
| **ID** | `TRI-4DBC63E3` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
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
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
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
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `6.5` |
| **Archivo** | `Node.js:None` |

**Descripción:** minimatch is a minimal matching utility for converting glob expressions into JavaScript RegExp objects. Prior to version 10.2.3, 9.0.7, 8.0.6, 7.4.8, 6.2.2, 5.1.8, 4.2.5, and 3.1.4, nested `*()` extglobs produce regexps with nested unbounded quantifiers (e.g. `(?:(?:a|b)*)*`), which exhibit catastrophic backtracking in V8. With a 12-byte pattern `*(*(*(a|b)))` and an 18-byte non-matching input, `m

**Evidencia:** `Paquete: minimatch v9.0.5 | Fix: 10.2.3, 9.0.7, 8.0.6, 7.4.8, 6.2.2, 5.1.8, 4.2.5, 3.1.4`

**✅ Remediación:** Actualizar minimatch de 9.0.5 a 10.2.3, 9.0.7, 8.0.6, 7.4.8, 6.2.2, 5.1.8, 4.2.5, 3.1.4

---

#### 🟠 [HIGH] CVE-2026-9496 – pacote: Pacote: Denial of Service via crafted spec.rawSpec value in addGitSha function

| Campo | Valor |
|---|---|
| **ID** | `TRI-50397C31` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `Node.js:None` |

**Descripción:** Versions of the package pacote from 11.2.7 and before 21.5.1 are vulnerable to Denial of Service (DoS) via the addGitSha function. An attacker can exploit this vulnerability by supplying a specially crafted spec.rawSpec value that triggers the function’s regex replacement and string-manipulation logic,  causing excessive CPU consumption and potentially stalling or crashing the process.

**Evidencia:** `Paquete: pacote v18.0.6 | Fix: 21.5.1`

**✅ Remediación:** Actualizar pacote de 18.0.6 a 21.5.1

---

#### 🟠 [HIGH] CVE-2026-48815 – sigstore: Sigstore: Unauthorized certificates accepted due to ignored `certificateOIDs` verification option

| Campo | Valor |
|---|---|
| **ID** | `TRI-0B22127A` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `5.9` |
| **Archivo** | `Node.js:None` |

**Descripción:** sigstore-js provides JavaScript libraries for interacting with Sigstore services. Prior to 4.1.1, the documented certificateOIDs option in sigstore.verify() is accepted by the public API but discarded before verification, so required certificate extension OIDs are never checked and applications relying on certificateOIDs to restrict which certificates may sign artifacts can accept unauthorized cer

**Evidencia:** `Paquete: sigstore v2.3.1 | Fix: 4.1.1`

**✅ Remediación:** Actualizar sigstore de 2.3.1 a 4.1.1

---

#### 🟠 [HIGH] CVE-2026-23745 – node-tar: tar: node-tar: Arbitrary file overwrite and symlink poisoning via unsanitized linkpaths in archives

| Campo | Valor |
|---|---|
| **ID** | `TRI-052C5558` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
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
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
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
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
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
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
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
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
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
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `5.5` |
| **Archivo** | `Node.js:None` |

**Descripción:** node-tar is a full-featured Tar for Node.js. Prior to version 7.5.11, tar (npm) can be tricked into creating a symlink that points outside the extraction directory by using a drive-relative symlink target such as C:../../../target.txt, which enables file overwrite outside cwd during normal tar.x() extraction. This vulnerability is fixed in 7.5.11.

**Evidencia:** `Paquete: tar v6.2.1 | Fix: 7.5.11`

**✅ Remediación:** Actualizar tar de 6.2.1 a 7.5.11

---

#### 🟠 [HIGH] CVE-2026-59874 – tar: Node-tar: Denial of Service via malformed tar archive header

| Campo | Valor |
|---|---|
| **ID** | `TRI-99994F7D` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `Node.js:None` |

**Descripción:** node-tar is a tar archive manipulation library for Node.js. Prior to 7.5.18, tar.replace accepts a checksum-valid tar header with a negative base-256 encoded entry size, causing the archive scanner to make no progress while repeatedly parsing the same header. This issue is fixed in version 7.5.18.

**Evidencia:** `Paquete: tar v6.2.1 | Fix: 7.5.18`

**✅ Remediación:** Actualizar tar de 6.2.1 a 7.5.18

---

#### 🟠 [HIGH] CVE-2026-73566 – tar: node-tar: Denial of Service via crafted long-path tar archive

| Campo | Valor |
|---|---|
| **ID** | `TRI-BC8B6773` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `Node.js:None` |

**Descripción:** node-tar is a tar archive manipulation library for Node.js. Prior to 7.5.21, node-tar's filesFilter in src/list.ts uses the recursive mapHas helper to walk an archive entry path upward with path.dirname() and no segment cap when tar.t(...) or tar.x(...) receives a non-empty member-selection list. A crafted GNU L or PAX x long-path header with thousands of slash-separated segments reaches this.filt

**Evidencia:** `Paquete: tar v6.2.1 | Fix: 7.5.21`

**✅ Remediación:** Actualizar tar de 6.2.1 a 7.5.21

---

#### 🟡🟢⚪ Medios, Bajos e Info (22)

| Severidad | CVE / Advisory | CVSS | Remediación |
|---|---|---|---|
| 🟡 MEDIUM | CVE-2026-18798 – openssl: QUIC server may trigger doubl | 7.5 | Actualizar libcrypto3 de 3.5.6-r0 a 3.5.8-r0 |
| 🟡 MEDIUM | CVE-2026-34182 – openssl: CMS AuthEnvelopedData Process | 7.4 | Actualizar libcrypto3 de 3.5.6-r0 a 3.5.7-r0 |
| 🟡 MEDIUM | CVE-2026-34183 – openssl: Unbounded Memory Growth in th | 7.5 | Actualizar libcrypto3 de 3.5.6-r0 a 3.5.7-r0 |
| 🟡 MEDIUM | CVE-2026-42764 – openssl: NULL pointer dereference in Q | 5.9 | Actualizar libcrypto3 de 3.5.6-r0 a 3.5.7-r0 |
| 🟡 MEDIUM | CVE-2026-45445 – openssl: AES-OCB IV Ignored on EVP_Cip | 9.1 | Actualizar libcrypto3 de 3.5.6-r0 a 3.5.7-r0 |
| 🟡 MEDIUM | CVE-2026-63072 – openssl: heap buffer overflow in CMS k | 7.5 | Actualizar libcrypto3 de 3.5.6-r0 a 3.5.8-r0 |
| 🟡 MEDIUM | CVE-2026-63076 – openssl: invalid pointer dereference i | 7.5 | Actualizar libcrypto3 de 3.5.6-r0 a 3.5.8-r0 |
| 🟡 MEDIUM | CVE-2026-4738 – Improper Restriction of Operations with | None | Actualizar zlib de 1.3.2-r0 a 1.4-r0 |
| 🟡 MEDIUM | CVE-2026-48758 – sigstore-core: @sigstore/core: Signatu | 5.4 | Actualizar @sigstore/core de 1.1.0 a 3.2.1 |
| 🟡 MEDIUM | CVE-2026-102277 – brace-expansion: brace-expansion: Den | 5.3 | Actualizar brace-expansion de 2.0.1 a 5.0.12, 3.0.9, 2.1.7, 1.1.21 |
| 🟡 MEDIUM | CVE-2026-33750 – brace-expansion: brace-expansion: Deni | 7.5 | Actualizar brace-expansion de 2.0.1 a 5.0.5, 3.0.2, 2.0.3, 1.1.13 |
| 🟡 MEDIUM | CVE-2026-118773 – glob: glob: Denial of Service (DoS) v | 5.3 | Actualizar glob de 10.4.2 a 14.0.2 |
| 🟡 MEDIUM | CVE-2026-101911 – ip-address: ip-address: Denial of Ser | 5.3 | Actualizar ip-address de 9.0.5 a 10.7.1 |
| 🟡 MEDIUM | CVE-2026-101912 – ip-address: ip-address: Access contro | 5.3 | Actualizar ip-address de 9.0.5 a 10.7.1 |
| 🟡 MEDIUM | CVE-2026-101913 – ip-address: ip-address: Security bypa | 5.3 | Actualizar ip-address de 9.0.5 a 10.5.1 |
| 🟡 MEDIUM | CVE-2026-111997 – ip-address: ip-address: Denial of Ser | 5.3 | Actualizar ip-address de 9.0.5 a 10.7.4 |
| 🟡 MEDIUM | CVE-2026-42338 – ip-address: ip-address: Cross-site scr | 6.1 | Actualizar ip-address de 9.0.5 a 10.1.1 |
| 🟡 MEDIUM | CVE-2026-118764 – minimatch: minimatch: Denial of Servi | 5.9 | Actualizar minimatch de 9.0.5 a 11.0.1 |
| 🟡 MEDIUM | CVE-2026-104844 – postcss-selector-parser: postcss-sele | 5.9 | Actualizar postcss-selector-parser de 6.1.0 a 7.1.6, 6.1.5 |
| 🟡 MEDIUM | CVE-2026-53655 – node-tar: node-tar: File smuggling due | 5.5 | Actualizar tar de 6.2.1 a 7.5.16 |
| 🟡 MEDIUM | CVE-2026-59871 – node-tar: node-tar: Denial of Service  | 7.5 | Actualizar tar de 6.2.1 a 7.5.18 |
| 🟡 MEDIUM | CVE-2026-59875 – node-tar: node-tar: Denial of Service  | 5.3 | Actualizar tar de 6.2.1 a 7.5.17 |

### 🌐 OWASP ZAP (DAST) — `ASC-DAST-001`

> **Tipo:** Análisis Dinámico en Ejecución  
> **Raw:** 2 | **Únicos:** 2 | **Deduplicados:** 0 (0.0%)

**Distribución:** 🟢 LOW: **1** | ⚪ INFO: **1**

#### 🟡🟢⚪ Medios, Bajos e Info (2)

| Severidad | Hallazgo | Endpoint | Remediación |
|---|---|---|---|
| 🟢 LOW | Cross-Origin-Resource-Policy Header Missing or Inv | `http://localhost:3000` | Ensure that the application/web server sets the Cross-Origin-Resource- |
| ⚪ INFO | Non-Storable Content | `http://localhost:3000` | The content may be marked as storable by ensuring that the following c |

### 🎯 Nuclei (Pentesting) — `ASC-PENTEST-001`

> **Tipo:** Validación Activa de Templates  
> **Raw:** 7 | **Únicos:** 2 | **Deduplicados:** 5 (71.4%)

**Distribución:** 🟢 LOW: **2**

#### 🟡🟢⚪ Medios, Bajos e Info (2)

| Severidad | Hallazgo | Endpoint | Remediación |
|---|---|---|---|
| 🟢 LOW | XSS-Protection Header - Cross-Site Scripting | `http://localhost:3000` | Revisar: Setting the XSS-Protection header is deprecated. Setting the  |
| 🟢 LOW | HTTP Missing Security Headers | `http://localhost:3000` | Revisar: This template searches for missing HTTP security headers. The |

### 🔐 Semgrep (SAST) — `ASC-SAST-001`

> **Tipo:** Análisis Estático de Código  
> **Raw:** 0 | **Únicos:** 0 | **Deduplicados:** 0 (0%)

_No se encontraron hallazgos para esta herramienta._

---

## 🎓 Notas Académicas y Marco de Referencia

Este reporte fue generado automáticamente por el pipeline DevSecOps implementado como
Trabajo de Grado en la **Universidad del Valle — Sede Tuluá**.

### Marco normativo y técnico

| Estándar / Framework | Aplicación en este pipeline |
|---|---|
| **ISO/IEC 27034-1:2011** | Trazabilidad en tres puntos: ANF en `scan_config.json`, `asc_id` en cada hallazgo, auditoría de ASC en este reporte |
| **SSVC v2.1 (CISA/SEI-CERT)** | Árbol de decisión del tercer gate con EPSS y CISA KEV |
| **OWASP Top 10 (2021)** | Categorización de todos los hallazgos normalizados |
| **CVSS v3.1 (NIST)** | Puntuación de severidad para hallazgos de Trivy |
| **CWE/SANS Top 25** | Clasificación de debilidades en SAST y DAST |
| **MITRE ATT&CK** | Referencia para cadenas de ataque identificadas por la IA |
| **EPSS (FIRST.org)** | Probabilidad de explotación en 30 días por CVE ID |
| **CISA KEV** | Catálogo de CVEs con explotación activa confirmada |

### Herramientas y su ASC ISO/IEC 27034

| Herramienta | Tipo | ASC ISO/IEC 27034 | Hallazgos únicos |
|---|---|---|---|
| Semgrep OSS | SAST | `ASC-SAST-001` | 0 |
| Trivy | SCA | `ASC-SCA-001` | 48 |
| OWASP ZAP | DAST | `ASC-DAST-001` | 2 |
| Nuclei v3 | Pentesting | `ASC-PENTEST-001` | 2 |

### Contribución diferencial por tipo de gate

| Capacidad | Tradicional | Gate IA | SSVC+EPSS+KEV |
|---|---|---|---|
| Falsos positivos | ❌ | ✅ | ✅ |
| Explotabilidad real | ❌ | ✅ | ✅ |
| Cadenas de ataque (1 en este run) | ❌ | ✅ | ❌ |
| Métricas formales F1 | ❌ | ❌ | ✅ |
| Trazabilidad ISO/IEC 27034 | ❌ | ❌ | ✅ (vía `asc_id`) |
| Impacto de negocio | ❌ | ✅ | ❌ |
| Determinístico | ✅ | ❌ | ✅ |

### Limitaciones

- Este reporte corresponde a una única corrida sobre `simple-health-api`. La validación completa
  abarca nueve casos de estudio documentados en la tesis (Capítulo 5).
- La evaluación IA requiere validación humana antes de decisiones en producción.
- No reemplaza una auditoría de seguridad formal ni un pentest manual.
- El gate SSVC prioriza la cautela ante hallazgos críticos — ver tesis sección 5.6.3.

---

_Reporte generado el 2026-11-17 20:35:23 | Pipeline Run: `44169564928`_

_**Autores:** Jhojan Stiven Castaño Jejen & Juan Manuel Arango Rodas_
_**Universidad del Valle** — Ingeniería de Sistemas — 2026_
