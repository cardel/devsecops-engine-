# 🔐 Reporte de Seguridad DevSecOps
## ❌ Decisión de Despliegue: **FAIL**

---

> **Generado automáticamente por el DevSecOps Engine v1.3 — Universidad del Valle 2026**

| Campo | Valor |
|---|---|
| **Servicio** | `fitfusion-backend` |
| **Entorno** | `staging` |
| **Criticidad de negocio** | `high` |
| **Pipeline Run** | `44169603311` |
| **Timestamp** | `2026-11-17 20:39:07` |
| **Modelo IA** | `meta-llama/llama-3.3-70b-instruct` |
| **Tokens utilizados** | `9,999` (prompt: 8,499 / completion: 1,500) |
| **Motor IA híbrido** | ✅ Motor híbrido activo |
| **ISO/IEC 27034 — Trazabilidad** | ✅ 3/4 ASC obligatorios ejecutados |

---

## 📊 Resumen Ejecutivo

Se han identificado varias vulnerabilidades críticas y altas en el pipeline de DevSecOps, incluyendo explotaciones remotas sin autenticación y cadenas de ataque potenciales. La mayoría de estas vulnerabilidades están relacionadas con componentes desactualizados y configuraciones inseguras.

> **Recomendación del sistema:** No se recomienda desplegar el sistema en producción hasta que se hayan abordado las vulnerabilidades críticas y altas identificadas

---

## 🚦 Decisión Final del Security Gate

| Campo | Valor |
|---|---|
| **Decisión** | ❌ **FAIL** |
| **Fuente** | `ai_assisted` |
| **Nivel de riesgo (IA)** | `CRITICAL` |
| **Risk Score (IA)** | `0.8 / 10.0` |
| **Confianza IA** | `90%` |
| **Falsos positivos estimados** | `baja` |
| **ISO/IEC 27034 — Trazabilidad ANF** | `3/4` ASC obligatorios ejecutados (ver sección ISO/IEC 27034) |

---

## 📈 Estadísticas Globales de Hallazgos

### Distribución por Severidad

| Severidad | Hallazgos | % del total | Proporción |
|---|---|---|---|
| 🔴 CRITICAL | 7 | 5.5% | `░░░░░░░░░░░░░░░` |
| 🟠 HIGH | 56 | 44.1% | `██████░░░░░░░░░` |
| 🟡 MEDIUM | 56 | 44.1% | `██████░░░░░░░░░` |
| 🟢 LOW | 6 | 4.7% | `░░░░░░░░░░░░░░░` |
| ⚪ INFO | 2 | 1.6% | `░░░░░░░░░░░░░░░` |
| ─ | **127** | **100%** | |

### Cobertura por Herramienta y ASC ISO/IEC 27034

> Cada herramienta tiene asignado un ASC (Application Security Control) de ISO/IEC 27034.
> La columna **Removidos** indica duplicados eliminados, no falsos positivos.

| Herramienta | ASC ISO 27034 | Raw | Únicos | Removidos | % Dedup | Estado |
|---|---|---|---|---|---|---|
| 🔐 Semgrep (SAST) | `ASC-SAST-001` | 0 | 0 | 0 | — | ⚠️ Sin hallazgos |
| 🔬 Trivy (SCA) | `ASC-SCA-001` | 169 | 117 | 52 | 30.8% | ✅ Ejecutado |
| 🌐 OWASP ZAP (DAST) | `ASC-DAST-001` | 6 | 6 | 0 | 0.0% | ✅ Ejecutado |
| 🎯 Nuclei (Pentesting) | `ASC-PENTEST-001` | 11 | 4 | 7 | 63.6% | ✅ Ejecutado |

### Top 5 Categorías OWASP Top 10

| Categoría | Hallazgos | % del total | Proporción |
|---|---|---|---|
| `A06:2021 – Vulnerable and Outdated Components` | 119 | 93.7% | `███████████░` |
| `A05:2021 – Security Misconfiguration` | 5 | 3.9% | `░░░░░░░░░░░░` |
| `A07:2021 – Identification and Authentication Failures` | 2 | 1.6% | `░░░░░░░░░░░░` |
| `A03:2021 – Injection` | 1 | 0.8% | `░░░░░░░░░░░░` |

---

## 🔄 Metodología de Deduplicación

> El normalizador aplica deduplicación para evitar el doble conteo de vulnerabilidades
> detectadas por múltiples instancias de la misma herramienta.
>
> **Total raw:** 186 hallazgos → **Total único:** 127 → **Eliminados:** 59 (31.7% de reducción)

### 🔬 Trivy (SCA) — Análisis de Componentes de Software

- **Raw:** 169 | **Únicos:** 117 | **Removidos:** 52 (30.8%)
- **Criterio:** `tool + título + endpoint/archivo`

> La misma CVE sobre el mismo paquete puede aparecer una vez por ruta de instalación. Tras deduplicar por CVE + paquete + target queda una sola entrada. Los removidos son instancias duplicadas, no falsos positivos.

### 🌐 OWASP ZAP (DAST) — Análisis Dinámico en Ejecución

- **Raw:** 6 | **Únicos:** 6 | **Removidos:** 0 (0.0%)
- **Criterio:** `tool + título + endpoint/archivo`

> ZAP realiza escaneo baseline pasivo. Cada alerta representa un tipo de misconfiguration único — por eso la deduplicación raramente elimina hallazgos: todas las alertas suelen tener títulos distintos.

### 🎯 Nuclei (Pentesting) — Validación Activa de Templates

- **Raw:** 11 | **Únicos:** 4 | **Removidos:** 7 (63.6%)
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
| **WAF detectado** | ❌ No detectado |
| **Servidor** | `No detectado` |
| **Tecnologías** | `Express`, `Node.js` |
| **Targets generados para Nuclei** | 1 URLs |

### Puertos detectados (nmap)

| Puerto | Servicio | Versión | Interesante |
|---|---|---|---|
| `22` | ssh | OpenSSH 10.2p1 Ubuntu 2ubuntu3.8 (Ubuntu | No |
| `3000` | http | Node.js Express framework | No |


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
| ⚪ INFO | `no_waf` | No se detectó WAF — tráfico malicioso llega directo a la app |


---

## 🤖 Evaluación Detallada por IA

### Razonamiento Técnico

El análisis detallado de los hallazgos de seguridad revela que varias vulnerabilidades tienen un alto nivel de explotabilidad, según los scores EPSS y la presencia en la lista KEV. Además, se han identificado cadenas de ataque que podrían permitir a un atacante realizar acciones devastadoras. La vulnerabilidad CVE-2026-31789, por ejemplo, permite la ejecución de código arbitrario en el servidor, mientras que la vulnerabilidad CVE-2025-15467 permite la ejecución remota de código sin autenticación.

**Análisis de falsos positivos:** La mayoría de los hallazgos tienen un alto nivel de confianza y están respaldados por evidencia empírica

### Categorías OWASP Top 10 Detectadas

- `A06:2021 – Vulnerable and Outdated Components`

### Cobertura por Tipo de Herramienta

| Tipo de análisis | Cobertura | Estado |
|---|---|---|
| SAST – Código fuente | buena | ✅ |
| SCA – Dependencias | buena | ✅ |
| DAST – Tiempo de ejecución | parcial | 🟡 |
| Pentesting automatizado | parcial | 🟡 |

**Evaluación general:** La cobertura general es buena, pero hay algunas áreas que requieren más atención

### ⚠️ Áreas sin cobertura (Blind Spots)

- Riesgo potencial no cubierto: Ataques de side-channel


### 🏆 Hallazgos Principales Identificados por IA

| Severidad | Hallazgo | CVSS | Remoto | Auth | Exploit | Categoría |
|---|---|---|---|---|---|---|
| 🔴 CRITICAL | CVE-2026-31789 – openssl: OpenSSL: Heap buffe | `9.8` | 🔴 Sí | 🟢 No | ⚠️ Sí | A06:2021 – Vulnerable and Outdated  |
| 🟠 HIGH | CVE-2025-15467 – openssl: OpenSSL: Remote cod | `9.8` | 🔴 Sí | 🟢 No | ⚠️ Sí | A06:2021 – Vulnerable and Outdated  |

---

## 🔗 Análisis de Cadenas de Ataque

> Esta sección identifica combinaciones de vulnerabilidades que, explotadas en secuencia,
> producen un impacto mayor al de cada vulnerabilidad de forma individual.

### 🔴 CHAIN-001 — Cadena de ataque para ejecución remota de código

| Campo | Valor |
|---|---|
| **Severidad combinada** | CRITICAL |
| **Probabilidad** | 🔴 Alta |
| **Vulnerabilidades involucradas** | `TRI-3B709604`, `TRI-8CEE03CF` |

**Secuencia del ataque:**

1. Paso 1: El atacante explota la vulnerabilidad CVE-2026-31789 para obtener acceso al servidor
2. Paso 2: Con acceso obtenido, el atacante explota la vulnerabilidad CVE-2025-15467 para ejecutar código remoto sin autenticación
3. Paso 3: Resultado final: El atacante puede ejecutar código arbitrario en el servidor

**Impacto combinado:** El impacto combinado de estas vulnerabilidades es crítico, ya que permite la ejecución remota de código sin autenticación

---

---

## 🛠️ Hoja de Ruta de Remediación

### 🚨 Inmediato (0–7 días) — 2 acciones

**1.** Actualizar libcrypto3 de 3.3.3-r0 a 3.3.7-r0 → Fix: `3.3.7-r0`
   - `trivy` | Esfuerzo: _bajo_ | Fix disponible: ✅

**2.** Actualizar libcrypto3 de 3.3.3-r0 a 3.3.6-r0 → Fix: `3.3.6-r0`
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
| **Decisión** | ❌ **FAIL** |
| **Acción agregada** | `Act` (máximo sobre todos los hallazgos evaluados) |
| **Mission & Wellbeing** | `high` (derivado de `criticality=high`) |
| **CISA KEV** | 1,782 entradas consultadas |
| **EPSS** | 115 CVEs consultados vía FIRST.org API |

### Distribución de Acciones SSVC

| Acción | Hallazgos | % | Gate | Significado operativo |
|---|---|---|---|---|
| **Act** | `67` | 52.8% | ❌ FAIL | Explotación activa o automatizable con impacto total |
| **Attend** | `12` | 9.4% | ⚠️ CONDITIONAL | Explotación probable a corto plazo |
| **Track*** | `40` | 31.5% | ⚠️ CONDITIONAL | Monitoreo activo — riesgo controlado |
| **Track** | `8` | 6.3% | ✅ PASS | Sin explotación activa conocida |
| **Total evaluados** | `127` | 100% | ❌ **FAIL** | Decisión = acción máxima |

### Hallazgos que requieren acción inmediata (Act)

| Herramienta | Vulnerabilidad | Explotación | Automatizable | Impacto | Acción |
|---|---|---|---|---|---|
| `trivy` | CVE-2026-31789 – openssl: OpenSSL: Heap buffer overflow on 32-bit | poc | yes | total | **Act** |
| `trivy` | CVE-2025-15467 – openssl: OpenSSL: Remote code execution or Denia | active | yes | total | **Act** |
| `trivy` | CVE-2025-69421 – openssl: OpenSSL: Denial of Service via malforme | poc | yes | total | **Act** |
| `trivy` | CVE-2026-28387 – openssl: OpenSSL: Arbitrary code execution due t | poc | yes | total | **Act** |
| `trivy` | CVE-2026-28388 – openssl: OpenSSL: Denial of Service due to NULL  | poc | yes | total | **Act** |
| `trivy` | CVE-2026-28389 – openssl: OpenSSL: Denial of Service vulnerabilit | poc | yes | total | **Act** |
| `trivy` | CVE-2026-28390 – openssl: OpenSSL: Denial of Service due to NULL  | poc | yes | total | **Act** |
| `trivy` | CVE-2026-45447 – openssl: Heap Use-After-Free in OpenSSL PKCS7_ve | poc | yes | total | **Act** |


### 📊 Métricas Formales — Dimensión Exploitation (F1 Score)

> Calculadas sobre CVEs con CISA KEV o EPSS disponible como *ground truth*.
> Metodología: Al Haddad et al. (2025) — arXiv 2510.18508.

| Métrica | Valor | Descripción |
|---|---|---|
| **Precisión** | `1.0000` | TP / (TP + FP) |
| **Recall** | `1.0000` | TP / (TP + FN) |
| **F1 Score** | `1.0000` | Media armónica precisión/recall |
| **Accuracy** | `1.0000` | (TP + TN) / total |
| CVEs evaluados | `115` | Solo CVEs con EPSS/KEV disponible |
| Verdaderos positivos | `1` | Clasificados active, ground truth active |
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
| **Tokens de prompt** | `8,499` |
| **Tokens de completion** | `1,500` |
| **Contexto SSVC activo** | ✅ Sí — el LLM recibió clasificaciones SSVC por hallazgo |
| **CISA KEV consultado** | 1,782 entradas (fuente: cisa.gov) |
| **EPSS consultado** | 115 CVEs (fuente: FIRST.org API) |
| **Hallazgos clasificados SSVC** | 127 |
| **Distribución SSVC pre-LLM** | Act=67, Attend=12, Track*=40, Track=8 |
| **F1 Exploitation** | `1.0000` (P=1.0000, R=1.0000, n=115 CVEs) |

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
| `TRI-3B709604` | CVE-2026-31789 – openssl: OpenSSL: Heap  | `Act` | ✅ **confirmed** | `0.0025` | No | La vulnerabilidad tiene un alto nivel de explotabilidad y un impacto técnico significativo... |
| `TRI-8CEE03CF` | CVE-2025-15467 – openssl: OpenSSL: Remot | `Act` | ✅ **confirmed** | `0.7479` | No | La vulnerabilidad tiene un alto nivel de explotabilidad y un impacto técnico significativo... |


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
| **Decisión** | ❌ FAIL | ❌ FAIL | ❌ FAIL |
| **Método** | Umbrales numéricos fijos | LLM con contexto SSVC/EPSS/KEV | Árbol SSVC v2.1 + EPSS + CISA KEV |
| **Acción agregada SSVC** | N/A | N/A | `Act` |
| **Métricas formales** | ❌ No | ❌ No | ✅ F1 = `1.000` |
| **Evalúa explotabilidad real** | ❌ No | ✅ Semántica LLM | ✅ CISA KEV + EPSS empírico |
| **Detecta cadenas de ataque** | ❌ No | ✅ Sí | ❌ Por hallazgo individual |
| **Considera falsos positivos** | ❌ No | ✅ Estimados (baja) | ✅ EPSS filtra low-risk |
| **Constantes arbitrarias** | ✅ Umbrales fijos | N/A | ❌ Ninguna |
| **Determinístico** | ✅ Sí | ❌ No | ✅ Sí |
| **Costo por run** | ~$0 | ~$0.005 | ~$0 (APIs gratuitas) |
| **Trazabilidad ISO/IEC 27034** | ❌ No | ❌ No | ✅ Vía `asc_id` (ver sección siguiente) |

### Divergencias entre gates

- Los tres gates concuerdan en la decisión final.

**Insight académico:** Los tres gates concuerdan — validación metodológica.

**Análisis comparativo:** N/A

**Razones del gate tradicional:**
- Hallazgos CRÍTICOS: 7 (umbral: 0)
- Hallazgos ALTOS: 56 (umbral: 5)
- Hallazgos MEDIOS: 56 (umbral: 20)

---

## 📋 Trazabilidad Normativa ISO/IEC 27034

**Estado de cumplimiento: ⚠️ **PARCIAL** — 3 de 4 controles obligatorios ejecutados**

ISO/IEC 27034-1:2011 exige que cada aplicación defina un **ANF** (*Application Normative
Framework*) con los controles de seguridad obligatorios según su nivel de criticidad.
Para este servicio con `criticality=high` el ANF requiere 4 control(es)
obligatorio(s). Los 1 control(es) restante(s) son opcionales y se ejecutaron
como cobertura adicional.

### Resultado por control de seguridad

**✅ ASC-SAST-001** (Semgrep OSS) — Control obligatorio  
Análisis estático de código fuente: se ejecutó correctamente y **no detectó vulnerabilidades** en este contexto. Este es el resultado esperado en una aplicación bien configurada.

**🟡 ASC-SCA-001** (Trivy) — Control obligatorio  
Análisis de componentes y dependencias (CVEs): se ejecutó y **detectó 117 hallazgo(s)** (7 CRITICAL, 56 HIGH, 54 MEDIUM). Los hallazgos están documentados en la sección de detalle.

**⚠️ zap** (Herramienta) — Control obligatorio  
Control de seguridad: **no se ejecutó** en esta corrida. Posible causa: herramienta no disponible, aplicación sin respuesta HTTP, o fallo en el job correspondiente.

**ℹ️ ASC-PENTEST-001** (Nuclei v3) — Control obligatorio  
Validación activa con templates de pentest: se ejecutó y **detectó 4 hallazgo(s)** (1 MEDIUM, 3 LOW). Los hallazgos están documentados en la sección de detalle.

**ℹ️ ASC-DAST-001** (OWASP ZAP) — Control opcional  
Análisis dinámico en tiempo de ejecución: se ejecutó y **detectó 6 hallazgo(s)** (1 MEDIUM, 3 LOW, 2 INFO). Los hallazgos están documentados en la sección de detalle.


### Resumen de cobertura ANF

| ASC | Herramienta | Obligatoriedad | Estado | Hallazgos | Severidades |
|---|---|---|---|---|---|
| `ASC-SAST-001` | Semgrep OSS | ✅ Obligatorio | ✅ Ejecutado | 0 | Sin hallazgos |
| `ASC-SCA-001` | Trivy | ✅ Obligatorio | ✅ Ejecutado | 117 | 🔴C:7 / 🟠H:56 / 🟡M:54 |
| `zap` | Herramienta | ✅ Obligatorio | ⚠️ No ejecutado | 0 | — |
| `ASC-PENTEST-001` | Nuclei v3 | ✅ Obligatorio | ✅ Ejecutado | 4 | 🟡M:1 / 🟢L:3 |
| `ASC-DAST-001` | OWASP ZAP | ⚪ Opcional | ✅ Ejecutado | 6 | 🟡M:1 / 🟢L:3 / ⚪I:2 |


> ⚠️ **Brechas de cobertura:** los siguientes controles obligatorios no se ejecutaron en esta corrida: `zap`. Revisar la configuración del pipeline antes de promover a producción.


> **ANF generado por:** `detector.py` según `criticality=high` y `language=nodejs` — ✅ generado automáticamente  
> **Política aplicada:** a mayor criticidad declarada, más controles son obligatorios.
> Para `low`: SAST + SCA obligatorios. Para `high` o `critical`: los 4 controles son obligatorios.

### Cómo se operacionaliza la norma en el pipeline

ISO/IEC 27034 no prescribe valores numéricos — define el marco. El pipeline lo
implementa en tres puntos concretos y auditables:

| Punto | Dónde ocurre | Evidencia en esta corrida |
|---|---|---|
| **1. ANF** | `detector.py` → `scan_config.json` | 4 ASC obligatorios definidos para `criticality=high` |
| **2. asc_id** | `normalizer.py` → `findings.json` | Cada hallazgo etiquetado con el ASC que lo detectó |
| **3. Auditoría** | Este reporte | 3/4 controles obligatorios verificados |

---

## 📋 Hallazgos Detallados por Herramienta

### 🔬 Trivy (SCA) — `ASC-SCA-001`

> **Tipo:** Análisis de Componentes de Software  
> **Raw:** 169 | **Únicos:** 117 | **Deduplicados:** 52 (30.8%)

**Distribución:** 🔴 CRITICAL: **7** | 🟠 HIGH: **56** | 🟡 MEDIUM: **54**

#### 🔴🟠 Críticos y Altos (63)

#### 🔴 [CRITICAL] CVE-2026-31789 – openssl: OpenSSL: Heap buffer overflow on 32-bit systems from large X.509 certificate processing

| Campo | Valor |
|---|---|
| **ID** | `TRI-3B709604` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `9.8` |
| **Archivo** | `ghcr.io/cardel/fitfusion-backend:fb47b6814fd565ed21b0f2cbffae5e6fefd35cbe (alpine 3.21.3):None` |

**Descripción:** Issue summary: Converting an excessively large OCTET STRING value to
a hexadecimal string leads to a heap buffer overflow on 32 bit platforms.

Impact summary: A heap buffer overflow may lead to a crash or possibly
an attacker controlled code execution or other undefined behavior.

If an attacker can supply a crafted X.509 certificate with an excessively
large OCTET STRING value in extensions such

**Evidencia:** `Paquete: libcrypto3 v3.3.3-r0 | Fix: 3.3.7-r0`

**✅ Remediación:** Actualizar libcrypto3 de 3.3.3-r0 a 3.3.7-r0

---

#### 🔴 [CRITICAL] CVE-2026-106445 – handlebars: Handlebars: JavaScript Injection via Own Property Check Bypass

| Campo | Valor |
|---|---|
| **ID** | `TRI-3BADB093` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `8.1` |
| **Archivo** | `Node.js:None` |

**Descripción:** Handlebars provides the power necessary to let users build semantic templates. From 3.0.0 until 4.7.10, Handlebars lookupProperty returns Function.prototype.constructor before applying the prototype-access deny list because constructor is an own property of Function.prototype. When an attacker can render a controlled template with allowProtoMethodsByDefault enabled and an accessible function in th

**Evidencia:** `Paquete: handlebars v4.7.8 | Fix: 4.7.10`

**✅ Remediación:** Actualizar handlebars de 4.7.8 a 4.7.10

---

#### 🔴 [CRITICAL] CVE-2026-106446 – handlebars: Handlebars: JavaScript Injection via AST Type Confusion in compile (Program.blockParams)

| Campo | Valor |
|---|---|
| **ID** | `TRI-8E6B273B` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `8.1` |
| **Archivo** | `Node.js:None` |

**Descripción:** Handlebars provides the power necessary to let users build semantic templates. From 4.0.0 until 4.7.10, Handlebars.compile() and Handlebars.precompile() accept pre-parsed AST objects while validating only selected PathExpression, NumberLiteral, and BooleanLiteral values. This issue bypasses the AST validation introduced in version 4.7.9 for CVE-2026-33937. An attacker who can supply an object inst

**Evidencia:** `Paquete: handlebars v4.7.8 | Fix: 4.7.10`

**✅ Remediación:** Actualizar handlebars de 4.7.8 a 4.7.10

---

#### 🔴 [CRITICAL] CVE-2026-33937 – handlebars.js: Handlebars: Remote Code Execution via crafted Abstract Syntax Tree object in compile()

| Campo | Valor |
|---|---|
| **ID** | `TRI-C387FCB0` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `9.8` |
| **Archivo** | `Node.js:None` |

**Descripción:** Handlebars provides the power necessary to let users build semantic templates. In versions 4.0.0 through 4.7.8, `Handlebars.compile()` accepts a pre-parsed AST object in addition to a template string. The `value` field of a `NumberLiteral` AST node is emitted directly into the generated JavaScript without quoting or sanitization. An attacker who can supply a crafted AST to `compile()` can therefor

**Evidencia:** `Paquete: handlebars v4.7.8 | Fix: 4.7.9`

**✅ Remediación:** Actualizar handlebars de 4.7.8 a 4.7.9

---

#### 🔴 [CRITICAL] CVE-2026-125120 – Mongoose: sanitizeFilter not applied on countDocuments

| Campo | Valor |
|---|---|
| **ID** | `TRI-32D4055E` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `9.8` |
| **Archivo** | `Node.js:None` |

**Descripción:** Mongoose is a MongoDB object modeling tool designed to work in an asynchronous environment. Prior to 6.13.11, 7.8.12, 8.24.3, and 9.9.2, Mongoose countDocuments() does not apply the configured sanitizeFilter query selector injection defense. An application that enables sanitizeFilter and passes attacker-controlled filter values to countDocuments() can therefore process query operator objects as op

**Evidencia:** `Paquete: mongoose v8.20.0 | Fix: 6.13.11, 7.8.12, 8.24.3, 9.9.2`

**✅ Remediación:** Actualizar mongoose de 8.20.0 a 6.13.11, 7.8.12, 8.24.3, 9.9.2

---

#### 🔴 [CRITICAL] CVE-2026-90711 – proxy-addr: proxy-addr vulnerable to IP spoofing via IPv4-mapped IPv6 trust subnet

| Campo | Valor |
|---|---|
| **ID** | `TRI-95145635` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `Node.js:None` |

**Descripción:** proxy-addr is a Node.js module that determines a request's client address behind trusted reverse proxies, and it backs Express req.ip and req.ips. In versions 1.1.0 through 2.0.7, a trust subnet written in IPv4-mapped IPv6 notation with an IPv4-sized prefix, such as ::ffff:10.0.0.0/8 instead of the correct ::ffff:10.0.0.0/104, is accepted without error but trusts every IPv4 address on the internet

**Evidencia:** `Paquete: proxy-addr v2.0.7 | Fix: 2.0.8`

**✅ Remediación:** Actualizar proxy-addr de 2.0.7 a 2.0.8

---

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

#### 🟠 [HIGH] CVE-2025-15467 – openssl: OpenSSL: Remote code execution or Denial of Service via oversized Initialization Vector in CMS parsing

| Campo | Valor |
|---|---|
| **ID** | `TRI-8CEE03CF` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `9.8` |
| **Archivo** | `ghcr.io/cardel/fitfusion-backend:fb47b6814fd565ed21b0f2cbffae5e6fefd35cbe (alpine 3.21.3):None` |

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
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `ghcr.io/cardel/fitfusion-backend:fb47b6814fd565ed21b0f2cbffae5e6fefd35cbe (alpine 3.21.3):None` |

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
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `8.1` |
| **Archivo** | `ghcr.io/cardel/fitfusion-backend:fb47b6814fd565ed21b0f2cbffae5e6fefd35cbe (alpine 3.21.3):None` |

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
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `ghcr.io/cardel/fitfusion-backend:fb47b6814fd565ed21b0f2cbffae5e6fefd35cbe (alpine 3.21.3):None` |

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
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `ghcr.io/cardel/fitfusion-backend:fb47b6814fd565ed21b0f2cbffae5e6fefd35cbe (alpine 3.21.3):None` |

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
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `ghcr.io/cardel/fitfusion-backend:fb47b6814fd565ed21b0f2cbffae5e6fefd35cbe (alpine 3.21.3):None` |

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

#### 🟠 [HIGH] CVE-2026-45447 – openssl: Heap Use-After-Free in OpenSSL PKCS7_verify()

| Campo | Valor |
|---|---|
| **ID** | `TRI-9B5681BF` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `8.1` |
| **Archivo** | `ghcr.io/cardel/fitfusion-backend:fb47b6814fd565ed21b0f2cbffae5e6fefd35cbe (alpine 3.21.3):None` |

**Descripción:** Issue summary: A specially crafted PKCS#7 or S/MIME signed message could
trigger a use-after-free during PKCS#7 signature verification.

Impact summary: A use-after-free may result in process crashes, heap
corruption, or potentially remote code execution.

When processing a PKCS#7 or S/MIME signed message, if the SignedData
digestAlgorithms field is present as an empty ASN.1 SET, OpenSSL may
incor

**Evidencia:** `Paquete: libcrypto3 v3.3.3-r0 | Fix: 3.3.7-r1`

**✅ Remediación:** Actualizar libcrypto3 de 3.3.3-r0 a 3.3.7-r1

---

#### 🟠 [HIGH] CVE-2026-84782 – openssl: compat-openssl: openssl: Information disclosure via DTLS handshake retransmission

| Campo | Valor |
|---|---|
| **ID** | `TRI-92AC1EC1` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.4` |
| **Archivo** | `ghcr.io/cardel/fitfusion-backend:fb47b6814fd565ed21b0f2cbffae5e6fefd35cbe (alpine 3.21.3):None` |

**Descripción:** Issue summary: The DTLS retransmission logic does not correctly handle
a handshake message write that is suspended part-way through.
The retransmitted message can be read past the message buffer and
the retransmission overwrites the internal state the suspended write
needs to resume correctly.

Impact summary: The retransmitted message can disclose a heap memory
to the peer as plaintext handshake 

**Evidencia:** `Paquete: libcrypto3 v3.3.3-r0 | Fix: 3.3.7-r2`

**✅ Remediación:** Actualizar libcrypto3 de 3.3.3-r0 a 3.3.7-r2

---

#### 🟠 [HIGH] CVE-2026-107891 – musl: musl: Arbitrary code execution via integer overflow in regcomp

| Campo | Valor |
|---|---|
| **ID** | `TRI-4F8EA83C` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `8.1` |
| **Archivo** | `ghcr.io/cardel/fitfusion-backend:fb47b6814fd565ed21b0f2cbffae5e6fefd35cbe (alpine 3.21.3):None` |

**Descripción:** musl libc before 1.2.7, when an untrusted regular expression is used with regcomp, has multiple integer overflows, possibly leading to incorrect allocation sizes and out-of-bounds heap writes.

**Evidencia:** `Paquete: musl v1.2.5-r9 | Fix: 1.2.5-r12`

**✅ Remediación:** Actualizar musl de 1.2.5-r9 a 1.2.5-r12

---

#### 🟠 [HIGH] CVE-2026-40200 – musl: musl libc: Arbitrary code execution and denial of service via stack-based memory corruption in qsort

| Campo | Valor |
|---|---|
| **ID** | `TRI-AFBEE807` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.8` |
| **Archivo** | `ghcr.io/cardel/fitfusion-backend:fb47b6814fd565ed21b0f2cbffae5e6fefd35cbe (alpine 3.21.3):None` |

**Descripción:** An issue was discovered in musl libc 0.7.10 through 1.2.6. Stack-based memory corruption can occur during qsort of very large arrays, due to incorrectly implemented double-word primitives. The number of elements must exceed about seven million, i.e., the 32nd Leonardo number on 32-bit platforms (or the 64th Leonardo number on 64-bit platforms, which is not practical).

**Evidencia:** `Paquete: musl v1.2.5-r9 | Fix: 1.2.5-r11`

**✅ Remediación:** Actualizar musl de 1.2.5-r9 a 1.2.5-r11

---

#### 🟠 [HIGH] CVE-2026-22184 – zlib: zlib: Arbitrary code execution via buffer overflow in untgz utility

| Campo | Valor |
|---|---|
| **ID** | `TRI-7A83CEE5` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.8` |
| **Archivo** | `ghcr.io/cardel/fitfusion-backend:fb47b6814fd565ed21b0f2cbffae5e6fefd35cbe (alpine 3.21.3):None` |

**Descripción:** zlib versions up to and including 1.3.1.2 include a global buffer overflow in the untgz utility located under contrib/untgz. The vulnerability is limited to the standalone demonstration utility and does not affect the core zlib compression library. The flaw occurs when a user executes the untgz command with an excessively long archive name supplied via the command line, leading to an out-of-bounds

**Evidencia:** `Paquete: zlib v1.3.1-r2 | Fix: 1.3.2-r0`

**✅ Remediación:** Actualizar zlib de 1.3.1-r2 a 1.3.2-r0

---

#### 🟠 [HIGH] CVE-2026-85091 – zlib: zlib: Heap buffer overflow in gz_vacate() allows arbitrary code execution

| Campo | Valor |
|---|---|
| **ID** | `TRI-079E45C5` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `8.1` |
| **Archivo** | `ghcr.io/cardel/fitfusion-backend:fb47b6814fd565ed21b0f2cbffae5e6fefd35cbe (alpine 3.21.3):None` |

**Descripción:** zlib 1.2.11 through 1.3.2 contains a heap buffer overflow: after an underlying write() fails, gz_write() returns without resetting strm.next_in, leaving it pointed at the caller's buffer. A later gz* write call then derives a position from the stale pointer and writes past a heap allocation; any write() failure reaches it, including EPIPE on a blocking descriptor, and in versions before 1.3.1.2 th

**Evidencia:** `Paquete: zlib v1.3.1-r2 | Fix: 1.3.2-r1`

**✅ Remediación:** Actualizar zlib de 1.3.1-r2 a 1.3.2-r1

---

#### 🟠 [HIGH] CVE-2026-111181 – body-parser: body-parser: Denial of Service via unhandled decompression stream error

| Campo | Valor |
|---|---|
| **ID** | `TRI-90191FD4` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `Node.js:None` |

**Descripción:** body-parser is body parsing middleware for Node.js and Express. In versions before 1.20.9 and in versions from 2.0.0 before 2.4.0, a single request can crash any application using body-parser with default options. When a request carries a Content-Encoding such as gzip, body-parser pipes it into a decompression stream and, after reading the body, leaves that stream with no error listener. A payload

**Evidencia:** `Paquete: body-parser v1.20.3 | Fix: 2.4.0, 1.20.9`

**✅ Remediación:** Actualizar body-parser de 1.20.3 a 2.4.0, 1.20.9

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

**Evidencia:** `Paquete: brace-expansion v1.1.12 | Fix: 5.0.10, 3.0.7, 2.1.5, 1.1.19`

**✅ Remediación:** Actualizar brace-expansion de 1.1.12 a 5.0.10, 3.0.7, 2.1.5, 1.1.19

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

**Evidencia:** `Paquete: brace-expansion v1.1.12 | Fix: 5.0.11, 3.0.8, 2.1.6, 1.1.20`

**✅ Remediación:** Actualizar brace-expansion de 1.1.12 a 5.0.11, 3.0.8, 2.1.6, 1.1.20

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

**Evidencia:** `Paquete: brace-expansion v1.1.12 | Fix: 5.0.7, 1.1.16, 2.1.2`

**✅ Remediación:** Actualizar brace-expansion de 1.1.12 a 5.0.7, 1.1.16, 2.1.2

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

**Evidencia:** `Paquete: brace-expansion v1.1.12 | Fix: 5.0.8, 3.0.3, 2.1.3, 1.1.17`

**✅ Remediación:** Actualizar brace-expansion de 1.1.12 a 5.0.8, 3.0.3, 2.1.3, 1.1.17

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

**Evidencia:** `Paquete: brace-expansion v1.1.12 | Fix: 1.1.18, 2.1.4, 3.0.6, 5.0.9`

**✅ Remediación:** Actualizar brace-expansion de 1.1.12 a 1.1.18, 2.1.4, 3.0.6, 5.0.9

---

#### 🟠 [HIGH] CVE-2026-73088 – browserslist: Browserslist: Prototype pollution leading to denial of service

| Campo | Valor |
|---|---|
| **ID** | `TRI-23A8F392` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `Node.js:None` |

**Descripción:** Browserslist is a configuration tool for sharing target browsers and Node.js versions between front-end tools. Prior to 4.28.7, normalizeStats() in node.js, reached unconditionally through getStat() and loadStat() on every browserslist() call, processes untrusted browserslist-stats.json, opts.stats, and CLI --stats data with an unguarded for...in loop and plain-object bracket access and assignment

**Evidencia:** `Paquete: browserslist v4.28.0 | Fix: 4.28.7`

**✅ Remediación:** Actualizar browserslist de 4.28.0 a 4.28.7

---

#### 🟠 [HIGH] CVE-2026-73089 – browserslist: Browserslist: Denial of Service via unbounded memory growth from distinct query results

| Campo | Valor |
|---|---|
| **ID** | `TRI-27A7D1E9` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `Node.js:None` |

**Descripción:** Browserslist is a configuration tool for sharing target browsers and Node.js versions between front-end tools. Prior to 4.28.7, index.js retains every distinct `(queries, context)` result in cache and every parseQueries() AST in parseCache without a size cap, TTL, or eviction, allowing an attacker who can influence repeated browserslist() query values, including valid since `<year>-<month>-<day>` 

**Evidencia:** `Paquete: browserslist v4.28.0 | Fix: 4.28.7`

**✅ Remediación:** Actualizar browserslist de 4.28.0 a 4.28.7

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

#### 🟠 [HIGH] CVE-2026-33938 – handlebars: Handlebars: Arbitrary code execution via @partial-block overwrite

| Campo | Valor |
|---|---|
| **ID** | `TRI-C9737641` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
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
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
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
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
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
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `8.2` |
| **Archivo** | `Node.js:None` |

**Descripción:** Handlebars provides the power necessary to let users build semantic templates. In versions 4.0.0 through 4.7.8, the Handlebars CLI precompiler (`bin/handlebars` / `lib/precompiler.js`) concatenates user-controlled strings — template file names and several CLI options — directly into the JavaScript it emits, without any escaping or sanitization. An attacker who can influence template filenames or C

**Evidencia:** `Paquete: handlebars v4.7.8 | Fix: 4.7.9`

**✅ Remediación:** Actualizar handlebars de 4.7.8 a 4.7.9

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

#### 🟠 [HIGH] CVE-2026-59869 – js-yaml: js-yaml: Denial of Service via crafted YAML documents

| Campo | Valor |
|---|---|
| **ID** | `TRI-EAD76143` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `Node.js:None` |

**Descripción:** js-yaml is a JavaScript YAML parser and dumper. From 3.0.0 before 3.15.0 and from 4.0.0 before 4.3.0, js-yaml can spend quadratic CPU time parsing a document whose size grows only linearly when a chain of mappings uses merge keys where each mapping merges the previous one. This issue is fixed in versions 3.15.0 and 4.3.0.

**Evidencia:** `Paquete: js-yaml v3.14.2 | Fix: 3.15.0, 4.3.0`

**✅ Remediación:** Actualizar js-yaml de 3.14.2 a 3.15.0, 4.3.0

---

#### 🟠 [HIGH] CVE-2026-84375 – js-yaml: js-yaml: Denial of Service vulnerability in YAML parsing

| Campo | Valor |
|---|---|
| **ID** | `TRI-5A12A60B` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `Node.js:None` |

**Descripción:** js-yaml is a JavaScript YAML parser and dumper. From 3.0.0 until 3.15.2, 4.3.2, and 5.4.1, maxTotalMergeKeys in lib/js-yaml/loader.js and lib/loader.js does not count empty mapping sources while processing the merge key <<. An attacker can alias a large sequence of empty mappings into many merge targets, causing O(N * K) processing while totalMergeKeys remains unchanged and the configured resource

**Evidencia:** `Paquete: js-yaml v3.14.2 | Fix: 4.3.2, 3.15.2`

**✅ Remediación:** Actualizar js-yaml de 3.14.2 a 4.3.2, 3.15.2

---

#### 🟠 [HIGH] GHSA-5p4m-2wfm-xmqj – JS-YAML: Quadratic CPU consumption in !!omap resolution (3.x and 4.x) — CVE-2026-59870 fix not backported

| Campo | Valor |
|---|---|
| **ID** | `TRI-3E4DC1F7` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `Node.js:None` |

**Descripción:** # Quadratic CPU consumption in `!!omap` resolution (js-yaml 3.x and 4.x)

## Summary

`resolveYamlOmap()` enforces key uniqueness for `!!omap` sequences with a linear
scan (`objectKeys.indexOf(...)`) inside the per-element loop, making resolution
**O(n²)** in the number of entries. A modestly sized YAML document therefore
consumes disproportionate CPU inside `yaml.load()`, giving a denial of servi

**Evidencia:** `Paquete: js-yaml v3.14.2 | Fix: 4.3.1, 3.15.1`

**✅ Remediación:** Actualizar js-yaml de 3.14.2 a 4.3.1, 3.15.1

---

#### 🟠 [HIGH] CVE-2025-65945 – node-jws: auth0/node-jws: Improper signature verification in HS256 algorithm

| Campo | Valor |
|---|---|
| **ID** | `TRI-CB3DDBA6` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `Node.js:None` |

**Descripción:** auth0/node-jws is a JSON Web Signature implementation for Node.js. In versions 3.2.2 and earlier and version 4.0.0, auth0/node-jws has an improper signature verification vulnerability when using the HS256 algorithm under specific conditions. Applications are affected when they use the jws.createVerify() function for HMAC algorithms and use user-provided data from the JSON Web Signature protected h

**Evidencia:** `Paquete: jws v3.2.2 | Fix: 3.2.3, 4.0.1`

**✅ Remediación:** Actualizar jws de 3.2.2 a 3.2.3, 4.0.1

---

#### 🟠 [HIGH] CVE-2026-48801 – linkify-it: linkify-it: Denial of Service via algorithmic complexity vulnerability

| Campo | Valor |
|---|---|
| **ID** | `TRI-10CA5509` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `Node.js:None` |

**Descripción:** linkify-it is a links recognition library with full Unicode support. Prior to 5.0.1, LinkifyIt.prototype.match, the package's primary public API, has O(N²) algorithmic complexity for inputs containing many fuzzy links or emails because the JavaScript-level scan loop re-slices input and re-runs unanchored regex searches on progressively shorter tails. Any service that synchronously renders untruste

**Evidencia:** `Paquete: linkify-it v5.0.0 | Fix: 5.0.1`

**✅ Remediación:** Actualizar linkify-it de 5.0.0 a 5.0.1

---

#### 🟠 [HIGH] CVE-2026-59887 – linkify-it: linkify-it: Denial of Service via crafted mailto: links

| Campo | Valor |
|---|---|
| **ID** | `TRI-EAA7BDDE` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `Node.js:None` |

**Descripción:** linkify-it is a links recognition library with full Unicode support. Prior to 5.0.2, the mailto: schema validator used by .test() and .match() can be invoked at every mailto: occurrence and scan the remaining input through src_email_name in lib/re.mjs, causing O(n^2) CPU consumption on crafted user text. This issue is fixed in version 5.0.2.

**Evidencia:** `Paquete: linkify-it v5.0.0 | Fix: 5.0.2`

**✅ Remediación:** Actualizar linkify-it de 5.0.0 a 5.0.2

---

#### 🟠 [HIGH] CVE-2026-4800 – lodash: lodash: Arbitrary code execution via untrusted input in template imports

| Campo | Valor |
|---|---|
| **ID** | `TRI-58B2412E` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `9.8` |
| **Archivo** | `Node.js:None` |

**Descripción:** The fix for CVE-2021-23337 added validation for the variable option in _.template but did not apply the same validation to options.imports key names, and both paths flow into the same Function() constructor sink. When an application passes untrusted input as options.imports key names, an attacker can inject default-parameter expressions that execute arbitrary code at template compilation time. Add

**Evidencia:** `Paquete: lodash v4.17.21 | Fix: 4.18.0`

**✅ Remediación:** Actualizar lodash de 4.17.21 a 4.18.0

---

#### 🟠 [HIGH] CVE-2026-111758 – markdown-it: markdown-it: Denial of Service via unclosed link reference definitions

| Campo | Valor |
|---|---|
| **ID** | `TRI-75DB7FEE` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `Node.js:None` |

**Descripción:** markdown-it is a Markdown parser. From versions 14.1.0 to before 14.3.3, and 15.0.0 to before 15.0.3, a link reference definition whose label or title is never closed is O(n²) with default options. Continuation lines are pulled lazily with str += lineContent in src/rules_block/reference.ts, and the subsequent charCodeAt and slice calls flatten the V8 cons-string, copying everything collected so fa

**Evidencia:** `Paquete: markdown-it v14.1.0 | Fix: 14.3.3, 15.0.3`

**✅ Remediación:** Actualizar markdown-it de 14.1.0 a 14.3.3, 15.0.3

---

#### 🟠 [HIGH] CVE-2026-111759 – markdown-it: markdown-it: Denial of Service via mismatched quote parsing

| Campo | Valor |
|---|---|
| **ID** | `TRI-D97E5531` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `Node.js:None` |

**Descripción:** markdown-it is a Markdown parser. Prior to 14.3.2 and 15.0.2, when typographer: true is enabled, specially crafted Markdown can cause quadratic processing time in the smartquotes rule, potentially leading to denial of service in applications processing untrusted input. Many opening double quotes followed by unmatched closing single quotes cause repeated scans of the entire opener stack. The same i

**Evidencia:** `Paquete: markdown-it v14.1.0 | Fix: 15.0.2, 14.3.2`

**✅ Remediación:** Actualizar markdown-it de 14.1.0 a 15.0.2, 14.3.2

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

**Evidencia:** `Paquete: minimatch v3.1.2 | Fix: 10.2.1, 9.0.6, 8.0.5, 7.4.7, 6.2.1, 5.1.7, 4.2.4, 3.1.3`

**✅ Remediación:** Actualizar minimatch de 3.1.2 a 10.2.1, 9.0.6, 8.0.5, 7.4.7, 6.2.1, 5.1.7, 4.2.4, 3.1.3

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

**Evidencia:** `Paquete: minimatch v3.1.2 | Fix: 10.2.3, 9.0.7, 8.0.6, 7.4.8, 6.2.2, 5.1.8, 4.2.5, 3.1.3`

**✅ Remediación:** Actualizar minimatch de 3.1.2 a 10.2.3, 9.0.7, 8.0.6, 7.4.8, 6.2.2, 5.1.8, 4.2.5, 3.1.3

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

**Evidencia:** `Paquete: minimatch v3.1.2 | Fix: 10.2.3, 9.0.7, 8.0.6, 7.4.8, 6.2.2, 5.1.8, 4.2.5, 3.1.4`

**✅ Remediación:** Actualizar minimatch de 3.1.2 a 10.2.3, 9.0.7, 8.0.6, 7.4.8, 6.2.2, 5.1.8, 4.2.5, 3.1.4

---

#### 🟠 [HIGH] CVE-2026-125117 – Mongoose walks into inherited properties when hydrating, setting, and merging, allowing overwrites of built-in functions (denial of service) and shared schema state

| Campo | Valor |
|---|---|
| **ID** | `TRI-7659740A` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `8.2` |
| **Archivo** | `Node.js:None` |

**Descripción:** Mongoose is a MongoDB object modeling tool designed to work in an asynchronous environment. Prior to 6.13.12, 7.8.13, 8.24.7, and 9.11.4, Mongoose can descend into inherited properties while loading database documents in init(), setting dotted paths in $__set, and merging update documents in utils.mergeClone. Attacker-controlled keys such as toString or valueOf can therefore cause Mongoose to writ

**Evidencia:** `Paquete: mongoose v8.20.0 | Fix: 6.13.12, 7.8.13, 8.24.7, 9.11.4`

**✅ Remediación:** Actualizar mongoose de 8.20.0 a 6.13.12, 7.8.13, 8.24.7, 9.11.4

---

#### 🟠 [HIGH] CVE-2026-125119 – Mongoose: Connection-level sanitizeFilter not applied

| Campo | Valor |
|---|---|
| **ID** | `TRI-C5494C74` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `Node.js:None` |

**Descripción:** Mongoose is a MongoDB object modeling tool designed to work in an asynchronous environment. From 6.0.0 until 6.13.12, 7.8.13, 8.24.7, and 9.11.4, Mongoose stores the connection-level sanitizeFilter option in Connection.config, but Query.prototype._castConditions() and query casting check other option locations and do not read that configuration. An application that enables sanitizeFilter through m

**Evidencia:** `Paquete: mongoose v8.20.0 | Fix: 6.13.12, 7.8.13, 8.24.7, 9.11.4`

**✅ Remediación:** Actualizar mongoose de 8.20.0 a 6.13.12, 7.8.13, 8.24.7, 9.11.4

---

#### 🟠 [HIGH] CVE-2026-42334 – Mongoose's Improper Sanitization of $nor in sanitizeFilter May Allow NoSQL Injection

| Campo | Valor |
|---|---|
| **ID** | `TRI-57534C85` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `Node.js:None` |

**Descripción:** Mongoose is a MongoDB object modeling tool designed to work in an asynchronous environment. Prior to 6.13.9, 7.8.9, 8.22.1, and 9.1.6, a vulnerability allows bypassing Mongoose’s sanitizeFilter query sanitization mechanism via the $nor operator. When sanitizeFilter is enabled, Mongoose wraps query operators in $eq to neutralize them. However, prior to the fix, $nor was not included in the set of l

**Evidencia:** `Paquete: mongoose v8.20.0 | Fix: 6.13.9, 7.8.9, 8.22.1, 9.1.6`

**✅ Remediación:** Actualizar mongoose de 8.20.0 a 6.13.9, 7.8.9, 8.22.1, 9.1.6

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

#### 🟠 [HIGH] CVE-2026-4867 – path-to-regexp: path-to-regexp: Denial of Service via catastrophic backtracking from malformed URL parameters

| Campo | Valor |
|---|---|
| **ID** | `TRI-5D2C4372` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `5.3` |
| **Archivo** | `Node.js:None` |

**Descripción:** Impact:

A bad regular expression is generated any time you have three or more parameters within a single segment, separated by something that is not a period (.). For example, /:a-:b-:c or /:a-:b-:c-:d. The backtrack protection added in path-to-regexp@0.1.12 only prevents ambiguity for two parameters. With three or more, the generated lookahead does not block single separator characters, so captu

**Evidencia:** `Paquete: path-to-regexp v0.1.12 | Fix: 0.1.13`

**✅ Remediación:** Actualizar path-to-regexp de 0.1.12 a 0.1.13

---

#### 🟠 [HIGH] CVE-2026-112366 – picomatch: picomatch: Denial of Service via single-branch repeated extglob patterns

| Campo | Valor |
|---|---|
| **ID** | `TRI-41CE4384` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `Node.js:None` |

**Descripción:** Picomatch through 4.0.7 contains a regular expression denial of service vulnerability that allows attackers to block the event loop by supplying single-branch repeated extglob patterns. Attackers can provide globs like +(*) or +(*a), which analyzeRepeatedExtglob in lib/parse.js skips, causing exponential backtracking against short crafted strings and denying service to Node.js applications.

**Evidencia:** `Paquete: picomatch v2.3.1 | Fix: Not available`

**✅ Remediación:** No hay fix disponible para picomatch 2.3.1 — considerar alternativa

---

#### 🟠 [HIGH] CVE-2026-33671 – picomatch: Picomatch: Regular Expression Denial of Service via crafted extglob patterns

| Campo | Valor |
|---|---|
| **ID** | `TRI-46F03624` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `6.5` |
| **Archivo** | `Node.js:None` |

**Descripción:** Picomatch is a glob matcher written JavaScript. Versions prior to 4.0.4, 3.0.2, and 2.3.2 are vulnerable to Regular Expression Denial of Service (ReDoS) when processing crafted extglob patterns. Certain patterns using extglob quantifiers such as `+()` and `*()`, especially when combined with overlapping alternatives or nested extglobs, are compiled into regular expressions that can exhibit catastr

**Evidencia:** `Paquete: picomatch v2.3.1 | Fix: 4.0.4, 3.0.2, 2.3.2`

**✅ Remediación:** Actualizar picomatch de 2.3.1 a 4.0.4, 3.0.2, 2.3.2

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

#### 🟠 [HIGH] CVE-2026-27601 – Underscore.js: Underscore.js: Denial of Service via recursive data structures in flatten and isEqual functions

| Campo | Valor |
|---|---|
| **ID** | `TRI-A68F09F1` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `5.9` |
| **Archivo** | `Node.js:None` |

**Descripción:** Underscore.js is a utility-belt library for JavaScript. Prior to 1.13.8, the _.flatten and _.isEqual functions use recursion without a depth limit. Under very specific conditions, detailed below, an attacker could exploit this in a Denial of Service (DoS) attack by triggering a stack overflow. Untrusted input must be used to create a recursive datastructure, for example using JSON.parse, with no e

**Evidencia:** `Paquete: underscore v1.13.7 | Fix: 1.13.8`

**✅ Remediación:** Actualizar underscore de 1.13.7 a 1.13.8

---

#### 🟡🟢⚪ Medios, Bajos e Info (54)

| Severidad | CVE / Advisory | CVSS | Remediación |
|---|---|---|---|
| 🟡 MEDIUM | CVE-2024-58251 – In netstat in BusyBox through 1.37.0,  | None | Actualizar busybox de 1.37.0-r12 a 1.37.0-r14 |
| 🟡 MEDIUM | CVE-2025-69419 – openssl: OpenSSL: Arbitrary code execu | 7.4 | Actualizar libcrypto3 de 3.3.3-r0 a 3.3.6-r0 |
| 🟡 MEDIUM | CVE-2025-9230 – openssl: Out-of-bounds read & write in  | 5.6 | Actualizar libcrypto3 de 3.3.3-r0 a 3.3.5-r0 |
| 🟡 MEDIUM | CVE-2025-9231 – openssl: Timing side-channel in SM2 alg | 5.9 | Actualizar libcrypto3 de 3.3.3-r0 a 3.3.5-r0 |
| 🟡 MEDIUM | CVE-2026-31790 – openssl: openssl: Information Disclosu | 5.9 | Actualizar libcrypto3 de 3.3.3-r0 a 3.3.7-r0 |
| 🟡 MEDIUM | CVE-2026-34182 – openssl: CMS AuthEnvelopedData Process | 7.4 | Actualizar libcrypto3 de 3.3.3-r0 a 3.3.7-r1 |
| 🟡 MEDIUM | CVE-2026-34183 – openssl: Unbounded Memory Growth in th | 7.5 | Actualizar libcrypto3 de 3.3.3-r0 a 3.3.7-r1 |
| 🟡 MEDIUM | CVE-2026-45445 – openssl: AES-OCB IV Ignored on EVP_Cip | 9.1 | Actualizar libcrypto3 de 3.3.3-r0 a 3.3.7-r1 |
| 🟡 MEDIUM | CVE-2026-54872 – openssl: OpenSSL: Private key recovery | 5.9 | Actualizar libcrypto3 de 3.3.3-r0 a 3.3.7-r2 |
| 🟡 MEDIUM | CVE-2026-54875 – openssl: openssl: information disclosu | 4.7 | Actualizar libcrypto3 de 3.3.3-r0 a 3.3.7-r2 |
| 🟡 MEDIUM | CVE-2026-63072 – openssl: heap buffer overflow in CMS k | 7.5 | Actualizar libcrypto3 de 3.3.3-r0 a 3.3.7-r1 |
| 🟡 MEDIUM | CVE-2026-63076 – openssl: invalid pointer dereference i | 7.5 | Actualizar libcrypto3 de 3.3.3-r0 a 3.3.7-r1 |
| 🟡 MEDIUM | CVE-2026-72897 – openssl: openssl: Denial of Service vi | 5.9 | Actualizar libcrypto3 de 3.3.3-r0 a 3.3.7-r2 |
| 🟡 MEDIUM | CVE-2026-75804 – openssl: OpenSSL: Denial of Service vi | 5.3 | Actualizar libcrypto3 de 3.3.3-r0 a 3.3.7-r2 |
| 🟡 MEDIUM | CVE-2026-75805 – openssl: openssl: Denial of Service vi | 5.9 | Actualizar libcrypto3 de 3.3.3-r0 a 3.3.7-r2 |
| 🟡 MEDIUM | CVE-2026-75806 – openssl: OpenSSL: Denial of Service vi | 5.3 | Actualizar libcrypto3 de 3.3.3-r0 a 3.3.7-r2 |
| 🟡 MEDIUM | CVE-2026-77696 – openssl: OpenSSL: Private key recovery | 5.9 | Actualizar libcrypto3 de 3.3.3-r0 a 3.3.7-r2 |
| 🟡 MEDIUM | CVE-2026-84784 – openssl: OpenSSL: Denial of Service vi | 5.3 | Actualizar libcrypto3 de 3.3.3-r0 a 3.3.7-r2 |
| 🟡 MEDIUM | CVE-2026-6042 – musl libc: GB18030 4-byte Decoder: musl | 5.5 | Actualizar musl de 1.2.5-r9 a 1.2.5-r10 |
| 🟡 MEDIUM | CVE-2026-27171 – zlib: zlib: Denial of Service via infi | 5.5 | Actualizar zlib de 1.3.1-r2 a 1.3.2-r0 |
| 🟡 MEDIUM | CVE-2026-4738 – Improper Restriction of Operations with | None | Actualizar zlib de 1.3.1-r2 a 1.4-r0 |
| 🟡 MEDIUM | CVE-2026-48758 – sigstore-core: @sigstore/core: Signatu | 5.4 | Actualizar @sigstore/core de 1.1.0 a 3.2.1 |
| 🟡 MEDIUM | CVE-2026-45819 – baseline-browser-mapping: baseline-bro | 7.5 | Actualizar baseline-browser-mapping de 2.8.29 a 2.11.0 |
| 🟡 MEDIUM | CVE-2026-102277 – brace-expansion: brace-expansion: Den | 5.3 | Actualizar brace-expansion de 1.1.12 a 5.0.12, 3.0.9, 2.1.7, 1.1.21 |
| 🟡 MEDIUM | CVE-2026-33750 – brace-expansion: brace-expansion: Deni | 7.5 | Actualizar brace-expansion de 1.1.12 a 5.0.5, 3.0.2, 2.0.3, 1.1.13 |
| 🟡 MEDIUM | CVE-2026-118773 – glob: glob: Denial of Service (DoS) v | 5.3 | Actualizar glob de 10.4.2 a 14.0.2 |
| 🟡 MEDIUM | CVE-2026-106444 – handlebars: Handlebars: Cross-Site Sc | 4.7 | Actualizar handlebars de 4.7.8 a 4.7.10 |
| 🟡 MEDIUM | CVE-2026-33916 – handlebars.js: Handlebars: Cross-Site  | 4.7 | Actualizar handlebars de 4.7.8 a 4.7.9 |
| 🟡 MEDIUM | GHSA-7rx3-28cr-v5wh – Handlebars.js has a Prototype Met | 4.8 | Actualizar handlebars de 4.7.8 a 4.7.9 |
| 🟡 MEDIUM | CVE-2026-101911 – ip-address: ip-address: Denial of Ser | 5.3 | Actualizar ip-address de 9.0.5 a 10.7.1 |
| 🟡 MEDIUM | CVE-2026-101912 – ip-address: ip-address: Access contro | 5.3 | Actualizar ip-address de 9.0.5 a 10.7.1 |
| 🟡 MEDIUM | CVE-2026-101913 – ip-address: ip-address: Security bypa | 5.3 | Actualizar ip-address de 9.0.5 a 10.5.1 |
| 🟡 MEDIUM | CVE-2026-111997 – ip-address: ip-address: Denial of Ser | 5.3 | Actualizar ip-address de 9.0.5 a 10.7.4 |
| 🟡 MEDIUM | CVE-2026-42338 – ip-address: ip-address: Cross-site scr | 6.1 | Actualizar ip-address de 9.0.5 a 10.1.1 |
| 🟡 MEDIUM | CVE-2026-53550 – js-yaml: js-yaml: Denial of Service vi | 5.3 | Actualizar js-yaml de 3.14.2 a 4.2.0, 3.15.0 |
| 🟡 MEDIUM | CVE-2025-13465 – lodash: prototype pollution in _.unset | 5.3 | Actualizar lodash de 4.17.21 a 4.17.23 |
| 🟡 MEDIUM | CVE-2026-2327 – markdown-it: markdown-it: Denial of Ser | 7.5 | Actualizar markdown-it de 14.1.0 a 14.1.1 |
| 🟡 MEDIUM | CVE-2026-48988 – markdown-it: markdown-it: Denial of Se | 5.3 | Actualizar markdown-it de 14.1.0 a 14.2.0 |
| 🟡 MEDIUM | GHSA-253c-mchw-3w2r – markdown-it linkify: true has two | None | Actualizar markdown-it de 14.1.0 a 15.0.1, 14.3.1 |
| 🟡 MEDIUM | CVE-2025-66400 – mdast-util-to-hast: mdast-util-to-hast | 5.3 | Actualizar mdast-util-to-hast de 13.2.0 a 13.2.1 |
| 🟡 MEDIUM | CVE-2026-118764 – minimatch: minimatch: Denial of Servi | 5.9 | Actualizar minimatch de 9.0.5 a 11.0.1 |
| 🟡 MEDIUM | CVE-2026-125116 – Mongoose: Discriminator key values ma | 4.8 | Actualizar mongoose de 8.20.0 a 6.13.12, 7.8.13, 8.24.7, 9.11.4 |
| 🟡 MEDIUM | CVE-2026-125118 – Mongoose: Prototype pollution via Sch | 6.5 | Actualizar mongoose de 8.20.0 a 6.13.12, 7.8.13, 8.24.7, 9.11.4 |
| 🟡 MEDIUM | CVE-2026-73562 – Mongoose: Prototype pollution in mongo | 6.5 | Actualizar mongoose de 8.20.0 a 6.13.10, 7.8.10, 8.24.1, 9.7.2 |
| 🟡 MEDIUM | CVE-2026-33672 – picomatch: Picomatch: Data integrity c | 5.3 | Actualizar picomatch de 2.3.1 a 4.0.4, 3.0.2, 2.3.2 |
| 🟡 MEDIUM | CVE-2026-104844 – postcss-selector-parser: postcss-sele | 5.9 | Actualizar postcss-selector-parser de 6.1.0 a 7.1.6, 6.1.5 |
| 🟡 MEDIUM | CVE-2025-15284 – qs: qs: Denial of Service via improper | 7.5 | Actualizar qs de 6.13.0 a 6.14.1 |
| 🟡 MEDIUM | CVE-2026-110816 – qs: qs: Denial of Service via unhandl | 5.3 | Actualizar qs de 6.13.0 a 6.16.1 |
| 🟡 MEDIUM | CVE-2026-82417 – qs: qs: Denial of Service via improper | 7.5 | Actualizar qs de 6.13.0 a 6.16.0 |
| 🟡 MEDIUM | CVE-2026-8723 – qs: qs: Denial of Service due to improp | 5.3 | Actualizar qs de 6.13.0 a 6.15.2 |
| 🟡 MEDIUM | CVE-2026-53655 – node-tar: node-tar: File smuggling due | 5.5 | Actualizar tar de 6.2.1 a 7.5.16 |
| 🟡 MEDIUM | CVE-2026-59871 – node-tar: node-tar: Denial of Service  | 7.5 | Actualizar tar de 6.2.1 a 7.5.18 |
| 🟡 MEDIUM | CVE-2026-59875 – node-tar: node-tar: Denial of Service  | 5.3 | Actualizar tar de 6.2.1 a 7.5.17 |
| 🟡 MEDIUM | CVE-2026-33532 – yaml: yaml: Denial of Service via deep | 6.5 | Actualizar yaml de 2.8.1 a 2.8.3, 1.10.3 |

### 🌐 OWASP ZAP (DAST) — `ASC-DAST-001`

> **Tipo:** Análisis Dinámico en Ejecución  
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

### 🎯 Nuclei (Pentesting) — `ASC-PENTEST-001`

> **Tipo:** Validación Activa de Templates  
> **Raw:** 11 | **Únicos:** 4 | **Deduplicados:** 7 (63.6%)

**Distribución:** 🟡 MEDIUM: **1** | 🟢 LOW: **3**

#### 🟡🟢⚪ Medios, Bajos e Info (4)

| Severidad | Hallazgo | Endpoint | Remediación |
|---|---|---|---|
| 🟡 MEDIUM | Node.js Express NODE_ENV Development Mode | `http://localhost:3000` | Revisar: The Node.js application runs in development mode, which can e |
| 🟢 LOW | Cookies without Secure attribute - Detect | `localhost:3000` | Ensure that all cookies are set with the Secure attribute to prevent M |
| 🟢 LOW | HTTP Missing Security Headers | `http://localhost:3000` | Revisar: This template searches for missing HTTP security headers. The |
| 🟢 LOW | Missing Cookie SameSite Strict | `http://localhost:3000` | Revisar: Identified cookies that lacked the samesite=strict attribute, |

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
| Trivy | SCA | `ASC-SCA-001` | 117 |
| OWASP ZAP | DAST | `ASC-DAST-001` | 6 |
| Nuclei v3 | Pentesting | `ASC-PENTEST-001` | 4 |

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

- Este reporte corresponde a una única corrida sobre `fitfusion-backend`. La validación completa
  abarca nueve casos de estudio documentados en la tesis (Capítulo 5).
- La evaluación IA requiere validación humana antes de decisiones en producción.
- No reemplaza una auditoría de seguridad formal ni un pentest manual.
- El gate SSVC prioriza la cautela ante hallazgos críticos — ver tesis sección 5.6.3.

---

_Reporte generado el 2026-11-17 20:39:07 | Pipeline Run: `44169603311`_

_**Autores:** Jhojan Stiven Castaño Jejen & Juan Manuel Arango Rodas_
_**Universidad del Valle** — Ingeniería de Sistemas — 2026_
