# 🔐 Reporte de Seguridad DevSecOps
## ❌ Decisión de Despliegue: **FAIL**

---

> **Generado automáticamente por el DevSecOps Engine v1.3 — Universidad del Valle 2026**

| Campo | Valor |
|---|---|
| **Servicio** | `webgoat` |
| **Entorno** | `staging` |
| **Criticidad de negocio** | `high` |
| **Pipeline Run** | `44148452239` |
| **Timestamp** | `2026-11-17 18:40:03` |
| **Modelo IA** | `gpt-4o-mini` |
| **Tokens utilizados** | `9,380` (prompt: 7,779 / completion: 1,601) |
| **Motor IA híbrido** | ✅ Motor híbrido activo |
| **ISO/IEC 27034 — Trazabilidad** | ✅ 3/4 ASC obligatorios ejecutados |

---

## 📊 Resumen Ejecutivo

El análisis de seguridad del servicio WebGoat revela múltiples hallazgos críticos y altos, algunos de los cuales son explotables remotamente. La presencia de vulnerabilidades de inyección SQL y componentes vulnerables que pueden ser explotados sin autenticación representan un riesgo significativo para la integridad y confidencialidad de los datos.

> **Recomendación del sistema:** No se recomienda el despliegue hasta que se aborden las vulnerabilidades críticas y se implementen las correcciones necesarias.

---

## 🚦 Decisión Final del Security Gate

| Campo | Valor |
|---|---|
| **Decisión** | ❌ **FAIL** |
| **Fuente** | `ai_assisted` |
| **Nivel de riesgo (IA)** | `CRITICAL` |
| **Risk Score (IA)** | `9.8 / 10.0` |
| **Confianza IA** | `90%` |
| **Falsos positivos estimados** | `baja` |
| **ISO/IEC 27034 — Trazabilidad ANF** | `3/4` ASC obligatorios ejecutados (ver sección ISO/IEC 27034) |

---

## 📈 Estadísticas Globales de Hallazgos

### Distribución por Severidad

| Severidad | Hallazgos | % del total | Proporción |
|---|---|---|---|
| 🔴 CRITICAL | 5 | 4.6% | `░░░░░░░░░░░░░░░` |
| 🟠 HIGH | 42 | 38.5% | `█████░░░░░░░░░░` |
| 🟡 MEDIUM | 57 | 52.3% | `███████░░░░░░░░` |
| 🟢 LOW | 4 | 3.7% | `░░░░░░░░░░░░░░░` |
| ⚪ INFO | 1 | 0.9% | `░░░░░░░░░░░░░░░` |
| ─ | **109** | **100%** | |

### Cobertura por Herramienta y ASC ISO/IEC 27034

> Cada herramienta tiene asignado un ASC (Application Security Control) de ISO/IEC 27034.
> La columna **Removidos** indica duplicados eliminados, no falsos positivos.

| Herramienta | ASC ISO 27034 | Raw | Únicos | Removidos | % Dedup | Estado |
|---|---|---|---|---|---|---|
| 🔐 Semgrep (SAST) | `ASC-SAST-001` | 17 | 16 | 1 | 5.9% | ✅ Ejecutado |
| 🔬 Trivy (SCA) | `ASC-SCA-001` | 163 | 87 | 76 | 46.6% | ✅ Ejecutado |
| 🌐 OWASP ZAP (DAST) | `ASC-DAST-001` | 3 | 3 | 0 | 0.0% | ✅ Ejecutado |
| 🎯 Nuclei (Pentesting) | `ASC-PENTEST-001` | 12 | 3 | 9 | 75.0% | ✅ Ejecutado |

### Top 5 Categorías OWASP Top 10

| Categoría | Hallazgos | % del total | Proporción |
|---|---|---|---|
| `A06:2021 – Vulnerable and Outdated Components` | 88 | 80.7% | `█████████░░░` |
| `A03:2021 – Injection` | 11 | 10.1% | `█░░░░░░░░░░░` |
| `A05:2021 – Security Misconfiguration` | 7 | 6.4% | `░░░░░░░░░░░░` |
| `A07:2021 – Identification and Authentication Failures` | 2 | 1.8% | `░░░░░░░░░░░░` |
| `A02:2021 – Cryptographic Failures` | 1 | 0.9% | `░░░░░░░░░░░░` |

---

## 🔄 Metodología de Deduplicación

> El normalizador aplica deduplicación para evitar el doble conteo de vulnerabilidades
> detectadas por múltiples instancias de la misma herramienta.
>
> **Total raw:** 195 hallazgos → **Total único:** 109 → **Eliminados:** 86 (44.1% de reducción)

### 🔬 Trivy (SCA) — Análisis de Componentes de Software

- **Raw:** 163 | **Únicos:** 87 | **Removidos:** 76 (46.6%)
- **Criterio:** `tool + título + endpoint/archivo`

> La misma CVE sobre el mismo paquete puede aparecer una vez por ruta de instalación. Tras deduplicar por CVE + paquete + target queda una sola entrada. Los removidos son instancias duplicadas, no falsos positivos.

### 🌐 OWASP ZAP (DAST) — Análisis Dinámico en Ejecución

- **Raw:** 3 | **Únicos:** 3 | **Removidos:** 0 (0.0%)
- **Criterio:** `tool + título + endpoint/archivo`

> ZAP realiza escaneo baseline pasivo. Cada alerta representa un tipo de misconfiguration único — por eso la deduplicación raramente elimina hallazgos: todas las alertas suelen tener títulos distintos.

### 🎯 Nuclei (Pentesting) — Validación Activa de Templates

- **Raw:** 12 | **Únicos:** 3 | **Removidos:** 9 (75.0%)
- **Criterio:** `tool + título + endpoint/archivo`

> Nuclei puede disparar el mismo template en el mismo endpoint varias veces dentro del mismo run. Tras deduplicar por template + endpoint se conserva solo una entrada por hallazgo único.

### 🔐 Semgrep (SAST) — Análisis Estático de Código

- **Raw:** 17 | **Únicos:** 16 | **Removidos:** 1 (5.9%)
- **Criterio:** `tool + título + endpoint/archivo`

> Semgrep analiza el código fuente del repositorio consumidor. La deduplicación elimina la misma regla disparada en múltiples archivos del mismo módulo, conservando solo la primera ocurrencia por regla + ruta.

---

## 🕵️ Fase de Reconocimiento Activo

> El reconocimiento activo descubre la superficie de ataque real antes del escaneo
> dinámico, enriqueciendo los targets de Nuclei y ZAP.

| Campo | Valor |
|---|---|
| **URL objetivo** | `http://localhost:8080` |
| **Host** | `localhost` |
| **Puerto** | `8080` |
| **WAF detectado** | ❌ No detectado |
| **Servidor** | `No detectado` |
| **Tecnologías** | _No detectadas_ |
| **Targets generados para Nuclei** | 1 URLs |

### Puertos detectados (nmap)

| Puerto | Servicio | Versión | Interesante |
|---|---|---|---|
| `22` | ssh | OpenSSH 10.2p1 Ubuntu 2ubuntu3.8 (Ubuntu | No |
| `8080` | http | Apache Tomcat (language: en) | No |


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

Se identificaron vulnerabilidades críticas como inyecciones SQL (CWE-89) y componentes vulnerables (CVE-2026-111497) con un EPSS de 0.826, lo que indica una alta probabilidad de explotación. Además, el hallazgo CVE-2026-109518, aunque tiene un EPSS de 0.009, es crítico debido a su naturaleza de ejecución remota. La combinación de estas vulnerabilidades puede permitir a un atacante comprometer el sistema de manera efectiva.

**Análisis de falsos positivos:** La mayoría de los hallazgos son válidos y se basan en patrones de código que son comúnmente explotables.

### Categorías OWASP Top 10 Detectadas

- `A03:2021 – Injection`
- `A06:2021 – Vulnerable and Outdated Components`

### Cobertura por Tipo de Herramienta

| Tipo de análisis | Cobertura | Estado |
|---|---|---|
| SAST – Código fuente | buena | ✅ |
| SCA – Dependencias | buena | ✅ |
| DAST – Tiempo de ejecución | parcial | 🟡 |
| Pentesting automatizado | parcial | 🟡 |

**Evaluación general:** La cobertura general es adecuada, pero se deben abordar las vulnerabilidades críticas.

### ⚠️ Áreas sin cobertura (Blind Spots)

- Falta de pruebas de penetración exhaustivas en el entorno de staging.


### 🏆 Hallazgos Principales Identificados por IA

| Severidad | Hallazgo | CVSS | Remoto | Auth | Exploit | Categoría |
|---|---|---|---|---|---|---|
| 🟠 HIGH | CVE-2026-111497 – brotli: Out-of-Bounds Write | `9.8` | 🔴 Sí | 🟢 No | ⚠️ Sí | A06:2021 – Vulnerable and Outdated  |
| 🟠 HIGH | Tainted Sql String | `0.0` | 🔴 Sí | 🟢 No | ⚠️ Sí | A03:2021 – Injection |

---

## 🔗 Análisis de Cadenas de Ataque

> Esta sección identifica combinaciones de vulnerabilidades que, explotadas en secuencia,
> producen un impacto mayor al de cada vulnerabilidad de forma individual.

### 🔴 CHAIN-001 — Explotación de inyección SQL y ejecución remota de código

| Campo | Valor |
|---|---|
| **Severidad combinada** | CRITICAL |
| **Probabilidad** | 🔴 Alta |
| **Vulnerabilidades involucradas** | `SEM-1557C43F`, `TRI-C4C5C885` |

**Secuencia del ataque:**

1. Paso 1: El atacante explota la vulnerabilidad de inyección SQL para obtener acceso a la base de datos.
2. Paso 2: Con acceso a la base de datos, el atacante puede manipular datos o ejecutar comandos SQL maliciosos.
3. Paso 3: Utilizando la vulnerabilidad de ejecución remota de código en el componente Brotli, el atacante ejecuta código arbitrario en el servidor.

**Impacto combinado:** La combinación de estas vulnerabilidades permite un ataque devastador que puede comprometer completamente el sistema y exponer datos sensibles.

---

---

## 🛠️ Hoja de Ruta de Remediación

### 🚨 Inmediato (0–7 días) — 1 acciones

**1.** Actualizar libbrotli1 de 1.1.0-2build2 a 1.1.0-2ubuntu0.1 → Fix: `1.1.0-2ubuntu0.1`
   - `trivy` | Esfuerzo: _bajo_ | Fix disponible: ✅

### ⚡ Corto plazo (1–4 semanas) — 1 acciones

**2.** Revisar y corregir el patrón de inyección SQL en el código fuente.
   - `semgrep` | Esfuerzo: _alto_ | Fix disponible: ❌

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
| **CISA KEV** | 1,781 entradas consultadas |
| **EPSS** | 86 CVEs consultados vía FIRST.org API |

### Distribución de Acciones SSVC

| Acción | Hallazgos | % | Gate | Significado operativo |
|---|---|---|---|---|
| **Act** | `54` | 49.5% | ❌ FAIL | Explotación activa o automatizable con impacto total |
| **Attend** | `17` | 15.6% | ⚠️ CONDITIONAL | Explotación probable a corto plazo |
| **Track*** | `31` | 28.4% | ⚠️ CONDITIONAL | Monitoreo activo — riesgo controlado |
| **Track** | `7` | 6.4% | ✅ PASS | Sin explotación activa conocida |
| **Total evaluados** | `109` | 100% | ❌ **FAIL** | Decisión = acción máxima |

### Hallazgos que requieren acción inmediata (Act)

| Herramienta | Vulnerabilidad | Explotación | Automatizable | Impacto | Acción |
|---|---|---|---|---|---|
| `semgrep` | Tainted Sql String | poc | yes | total | **Act** |
| `semgrep` | Formatted Sql String | poc | yes | total | **Act** |
| `semgrep` | Tainted Url Host | poc | yes | total | **Act** |
| `semgrep` | Httpservlet Path Traversal | poc | yes | total | **Act** |
| `semgrep` | Tainted Sql String | poc | yes | total | **Act** |
| `semgrep` | Formatted Sql String | poc | yes | total | **Act** |
| `semgrep` | Formatted Sql String | poc | yes | total | **Act** |
| `semgrep` | Formatted Sql String | poc | yes | total | **Act** |


### 📊 Métricas Formales — Dimensión Exploitation (F1 Score)

> Calculadas sobre CVEs con CISA KEV o EPSS disponible como *ground truth*.
> Metodología: Al Haddad et al. (2025) — arXiv 2510.18508.

| Métrica | Valor | Descripción |
|---|---|---|
| **Precisión** | `1.0000` | TP / (TP + FP) |
| **Recall** | `1.0000` | TP / (TP + FN) |
| **F1 Score** | `1.0000` | Media armónica precisión/recall |
| **Accuracy** | `1.0000` | (TP + TN) / total |
| CVEs evaluados | `87` | Solo CVEs con EPSS/KEV disponible |
| Verdaderos positivos | `12` | Clasificados active, ground truth active |
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
| **Modelo LLM** | `gpt-4o-mini` |
| **Versión del prompt** | `3.0-ssvc-enriched` (indica prompt enriquecido con SSVC/EPSS/KEV) |
| **Tokens de prompt** | `7,779` |
| **Tokens de completion** | `1,601` |
| **Contexto SSVC activo** | ✅ Sí — el LLM recibió clasificaciones SSVC por hallazgo |
| **CISA KEV consultado** | 1,781 entradas (fuente: cisa.gov) |
| **EPSS consultado** | 86 CVEs (fuente: FIRST.org API) |
| **Hallazgos clasificados SSVC** | 109 |
| **Distribución SSVC pre-LLM** | Act=54, Attend=17, Track*=31, Track=7 |
| **F1 Exploitation** | `1.0000` (P=1.0000, R=1.0000, n=87 CVEs) |

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

### Respuesta del LLM — Validación cruzada SSVC (3 hallazgos)

El LLM analizó las clasificaciones SSVC preliminares y emitió su propio juicio:
**1 confirmado(s)**, **2 sobreestimado(s)**, **0 subestimado(s)**.

| ID | Hallazgo | SSVC prelim. | Juicio IA | EPSS | En KEV | Razonamiento del LLM |
|---|---|---|---|---|---|---|
| `SEM-1557C43F` | Tainted Sql String | `Act` | ⚠️ **overestimated** | `0.0000` | No | La clasificación SSVC como 'Act' es una sobreestimación, ya que el EPSS de 0.0 indica que ... |
| `TRI-83E0FAD3` | CVE-2026-109518 – apt: Remote code execu | `Act` | ⚠️ **overestimated** | `0.0093` | No | Aunque se clasifica como 'Act', el bajo EPSS y la ausencia en KEV sugieren que el riesgo r... |
| `TRI-C4C5C885` | CVE-2026-111497 – brotli: Out-of-Bounds  | `Act` | ✅ **confirmed** | `0.8264` | ✅ Sí | Este hallazgo tiene un EPSS alto y está en KEV, lo que confirma su explotación activa y ju... |


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
- Hallazgos CRÍTICOS: 5 (umbral: 0)
- Hallazgos ALTOS: 42 (umbral: 5)
- Hallazgos MEDIOS: 57 (umbral: 20)

---

## 📋 Trazabilidad Normativa ISO/IEC 27034

**Estado de cumplimiento: ⚠️ **PARCIAL** — 3 de 4 controles obligatorios ejecutados**

ISO/IEC 27034-1:2011 exige que cada aplicación defina un **ANF** (*Application Normative
Framework*) con los controles de seguridad obligatorios según su nivel de criticidad.
Para este servicio con `criticality=high` el ANF requiere 4 control(es)
obligatorio(s). Los 1 control(es) restante(s) son opcionales y se ejecutaron
como cobertura adicional.

### Resultado por control de seguridad

**🟡 ASC-SAST-001** (Semgrep OSS) — Control obligatorio  
Análisis estático de código fuente: se ejecutó y **detectó 16 hallazgo(s)** (13 HIGH, 3 MEDIUM). Los hallazgos están documentados en la sección de detalle.

**🟡 ASC-SCA-001** (Trivy) — Control obligatorio  
Análisis de componentes y dependencias (CVEs): se ejecutó y **detectó 87 hallazgo(s)** (5 CRITICAL, 29 HIGH, 53 MEDIUM). Los hallazgos están documentados en la sección de detalle.

**⚠️ zap** (Herramienta) — Control obligatorio  
Control de seguridad: **no se ejecutó** en esta corrida. Posible causa: herramienta no disponible, aplicación sin respuesta HTTP, o fallo en el job correspondiente.

**ℹ️ ASC-PENTEST-001** (Nuclei v3) — Control obligatorio  
Validación activa con templates de pentest: se ejecutó y **detectó 3 hallazgo(s)** (3 LOW). Los hallazgos están documentados en la sección de detalle.

**ℹ️ ASC-DAST-001** (OWASP ZAP) — Control opcional  
Análisis dinámico en tiempo de ejecución: se ejecutó y **detectó 3 hallazgo(s)** (1 MEDIUM, 1 LOW, 1 INFO). Los hallazgos están documentados en la sección de detalle.


### Resumen de cobertura ANF

| ASC | Herramienta | Obligatoriedad | Estado | Hallazgos | Severidades |
|---|---|---|---|---|---|
| `ASC-SAST-001` | Semgrep OSS | ✅ Obligatorio | ✅ Ejecutado | 16 | 🟠H:13 / 🟡M:3 |
| `ASC-SCA-001` | Trivy | ✅ Obligatorio | ✅ Ejecutado | 87 | 🔴C:5 / 🟠H:29 / 🟡M:53 |
| `zap` | Herramienta | ✅ Obligatorio | ⚠️ No ejecutado | 0 | — |
| `ASC-PENTEST-001` | Nuclei v3 | ✅ Obligatorio | ✅ Ejecutado | 3 | 🟢L:3 |
| `ASC-DAST-001` | OWASP ZAP | ⚪ Opcional | ✅ Ejecutado | 3 | 🟡M:1 / 🟢L:1 / ⚪I:1 |


> ⚠️ **Brechas de cobertura:** los siguientes controles obligatorios no se ejecutaron en esta corrida: `zap`. Revisar la configuración del pipeline antes de promover a producción.


> **ANF generado por:** `detector.py` según `criticality=high` y `language=java` — ✅ generado automáticamente  
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
> **Raw:** 163 | **Únicos:** 87 | **Deduplicados:** 76 (46.6%)

**Distribución:** 🔴 CRITICAL: **5** | 🟠 HIGH: **29** | 🟡 MEDIUM: **53**

#### 🔴🟠 Críticos y Altos (34)

#### 🔴 [CRITICAL] CVE-2013-7285 – XStream: remote code execution due to insecure XML deserialization

| Campo | Valor |
|---|---|
| **ID** | `TRI-3C7EF471` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `9.8` |
| **Archivo** | `Java:None` |

**Descripción:** Xstream API versions up to 1.4.6 and version 1.4.10, if the security framework has not been initialized, may allow a remote attacker to run arbitrary shell commands by manipulating the processed input stream when unmarshaling XML or any supported format. e.g. JSON.

**Evidencia:** `Paquete: com.thoughtworks.xstream:xstream v1.4.5 | Fix: 1.4.7, 1.4.11`

**✅ Remediación:** Actualizar com.thoughtworks.xstream:xstream de 1.4.5 a 1.4.7, 1.4.11

---

#### 🔴 [CRITICAL] CVE-2026-65182 – tomcat: Apache Tomcat: Security constraint bypass due to improper access control

| Campo | Valor |
|---|---|
| **ID** | `TRI-5144334C` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `8.2` |
| **Archivo** | `Java:None` |

**Descripción:** Improper Access Control, Incorrect Authorization vulnerability in Apache Tomcat leads to security constraint bypass if a constraint for a longer path is specified before a more restrictive constraint for a shorter sub-path.



This issue affects Apache Tomcat: from 11.0.0-M1 through 11.0.24, from 10.1.0-M1 through 10.1.57, from 9.0.0.M1 through 9.0.120, from 8.5.0 through 8.5.100, from 7.0.0 throu

**Evidencia:** `Paquete: org.apache.tomcat.embed:tomcat-embed-core v11.0.24 | Fix: 11.0.25, 10.1.58, 9.0.121`

**✅ Remediación:** Actualizar org.apache.tomcat.embed:tomcat-embed-core de 11.0.24 a 11.0.25, 10.1.58, 9.0.121

---

#### 🔴 [CRITICAL] CVE-2026-65637 – tomcat: Apache Tomcat: Improper Input Validation allows HTTP/2 no-authority bypass of strict SNI validation

| Campo | Valor |
|---|---|
| **ID** | `TRI-AFDF76EF` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `6.5` |
| **Archivo** | `Java:None` |

**Descripción:** Improper Input Validation vulnerability in Apache Tomcat due to incomplete fix for CVE-2026-32990.



This issue affects Apache Tomcat: from 11.0.20 through 11.0.24, from 10.1.53 through 10.1.57, from 9.0.115 through 9.0.120.



Users are recommended to upgrade to version 11.0.25, 10.1.58 or 9.0.121, which fix the issue.

**Evidencia:** `Paquete: org.apache.tomcat.embed:tomcat-embed-core v11.0.24 | Fix: 11.0.25, 10.1.59, 9.0.121`

**✅ Remediación:** Actualizar org.apache.tomcat.embed:tomcat-embed-core de 11.0.24 a 11.0.25, 10.1.59, 9.0.121

---

#### 🔴 [CRITICAL] CVE-2026-65905 – tomcat: Apache Tomcat: Authentication bypass via limited replay attack in DIGEST authenticator

| Campo | Valor |
|---|---|
| **ID** | `TRI-7A97C7C4` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `4.8` |
| **Archivo** | `Java:None` |

**Descripción:** Authentication Bypass by Capture-replay vulnerability in Apache Tomcat's DIGEST authenticator. If, before windowSize requests have been made, a client makes a DIGEST 
authenticated request with a nonceCount on the upper boundary of the 
replay window then that request is replayable once only while the 
associated nonceCount remains within the replay window.



 

This issue affects Apache Tomcat: 

**Evidencia:** `Paquete: org.apache.tomcat.embed:tomcat-embed-core v11.0.24 | Fix: 11.0.25, 10.1.58, 9.0.121`

**✅ Remediación:** Actualizar org.apache.tomcat.embed:tomcat-embed-core de 11.0.24 a 11.0.25, 10.1.58, 9.0.121

---

#### 🔴 [CRITICAL] CVE-2026-68525 – tomcat: Apache Tomcat: Unauthorized resource access via FORM authentication bypass

| Campo | Valor |
|---|---|
| **ID** | `TRI-E7E7449F` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `6.5` |
| **Archivo** | `Java:None` |

**Descripción:** Incorrect Authorization vulnerability in Apache Tomcat's FORM authentication process allows the bypassing of a security constraint that limits user has access to a resource POST but not GET.







This issue affects Apache Tomcat: from 11.0.0-M1 through 11.0.24, from 10.1.0-M1 through 10.1.57, from 9.0.0.M1 through 9.0.120.







The following versions were EOL at the time the CVE was created bu

**Evidencia:** `Paquete: org.apache.tomcat.embed:tomcat-embed-core v11.0.24 | Fix: 11.0.25, 10.1.58, 9.0.121`

**✅ Remediación:** Actualizar org.apache.tomcat.embed:tomcat-embed-core de 11.0.24 a 11.0.25, 10.1.58, 9.0.121

---

#### 🟠 [HIGH] CVE-2026-109518 – apt: apt: Remote code execution via hard link reuse during package download retries

| Campo | Valor |
|---|---|
| **ID** | `TRI-83E0FAD3` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `8.1` |
| **Archivo** | `webgoat/webgoat:latest (ubuntu 24.04):None` |

**Descripción:** On Debian, Ubuntu, and derivative Linux distributions, an on-path attacker who can manipulate the HTTP traffic (including a malicious mirror or proxy) between an APT client and an archive server triggered by a package install can trick the client into installing an attacker-controlled unverified package and achieve remote code execution with root privileges.



The vulnerability is caused by the r

**Evidencia:** `Paquete: apt v2.8.3 | Fix: 2.8.4ubuntu0.1`

**✅ Remediación:** Actualizar apt de 2.8.3 a 2.8.4ubuntu0.1

---

#### 🟠 [HIGH] CVE-2026-111497 – brotli: Out-of-Bounds Write in Google Brotli Decoder

| Campo | Valor |
|---|---|
| **ID** | `TRI-C4C5C885` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `9.8` |
| **Archivo** | `webgoat/webgoat:latest (ubuntu 24.04):None` |

**Descripción:** A buffer overflow vulnerability in the Brotli decoder (c/dec/decode.c) in Google Brotli versions 1.0.3 through 1.2.0 on all platforms allows a remote unauthenticated attacker to corrupt adjacent decoder state memory, disclose sensitive memory contents, cause a denial of service, or potentially execute arbitrary code using a crafted Brotli-compressed stream.





Users need to update any Brotli lib

**Evidencia:** `Paquete: libbrotli1 v1.1.0-2build2 | Fix: 1.1.0-2ubuntu0.1`

**✅ Remediación:** Actualizar libbrotli1 de 1.1.0-2build2 a 1.1.0-2ubuntu0.1

---

#### 🟠 [HIGH] CVE-2026-89407 – com.fasterxml.jackson/jackson-core: tools.jackson.core/jackson-core: Jackson-core: Denial of Service via regular expression backtracking

| Campo | Valor |
|---|---|
| **ID** | `TRI-BE94D8BD` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `5.9` |
| **Archivo** | `Java:None` |

**Descripción:** NumberInput.looksLikeValidNumber() in FasterXML jackson-core pre-validates "stringified numbers" with two regular expressions: PATTERN_FLOAT ([+-]?[0-9]*[\.]?[0-9]+([eE][+-]?[0-9]+)?), present since 2.17.0, and PATTERN_FLOAT_TRAILING_DOT, added in 2.17.2. PATTERN_FLOAT places adjacent quantifiers over the same character class -- an optional [0-9]* run, an optional dot, then a required [0-9]+ run -

**Evidencia:** `Paquete: com.fasterxml.jackson.core:jackson-core v2.21.5 | Fix: 2.18.11, 2.21.7, 2.22.3`

**✅ Remediación:** Actualizar com.fasterxml.jackson.core:jackson-core de 2.21.5 a 2.18.11, 2.21.7, 2.22.3

---

#### 🟠 [HIGH] CVE-2026-89425 – com.fasterxml.jackson.core/jackson-core: Jackson-core: Denial of Service via unbounded StringBuilder growth during malformed token processing

| Campo | Valor |
|---|---|
| **ID** | `TRI-1C0C5898` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `Java:None` |

**Descripción:** UTF8DataInputJsonParser._reportInvalidToken() in FasterXML jackson-core builds the offending-token text for its error message by appending Java identifier characters to a StringBuilder in a loop that has no upper bound. Unlike the three sibling parser implementations, including UTF8StreamJsonParser, it never consults ErrorReportConfiguration.getMaxErrorTokenLength() (default 256). A malformed toke

**Evidencia:** `Paquete: com.fasterxml.jackson.core:jackson-core v2.21.5 | Fix: 2.21.7, 2.22.3, 2.18.11`

**✅ Remediación:** Actualizar com.fasterxml.jackson.core:jackson-core de 2.21.5 a 2.21.7, 2.22.3, 2.18.11

---

#### 🟠 [HIGH] CVE-2026-68497 – com.fasterxml.jackson.core/jackson-databind: tools.jackson.core/jackson-databind: jackson-databind: CPU Denial of Service via unbounded numeric parsing

| Campo | Valor |
|---|---|
| **ID** | `TRI-60B39C15` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `Java:None` |

**Descripción:** jackson-databind binds a JSON string to a javax.xml.datatype.Duration or javax.xml.datatype.XMLGregorianCalendar field by passing the raw string verbatim to DatatypeFactory.newDuration(value) or newXMLGregorianCalendar(value) in CoreXMLDeserializers.Std._deserialize. These deserializers are registered by default with no opt-in, so a plain ObjectMapper or JsonMapper with no polymorphic typing and n

**Evidencia:** `Paquete: com.fasterxml.jackson.core:jackson-databind v2.21.5 | Fix: 2.18.10, 2.21.6, 2.22.2`

**✅ Remediación:** Actualizar com.fasterxml.jackson.core:jackson-databind de 2.21.5 a 2.18.10, 2.21.6, 2.22.2

---

#### 🟠 [HIGH] CVE-2026-91776 – jackson-databind: com.fasterxml.jackson/jackson-core: jackson-databind: Denial of Service via unbounded cache growth in TypeDeserializerBase

| Campo | Valor |
|---|---|
| **ID** | `TRI-36F1CC70` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `Java:None` |

**Descripción:** TypeDeserializerBase._findDeserializer() in FasterXML jackson-databind caches the resolved deserializer under the raw, attacker-supplied type ID. When name-based polymorphism is configured with a fallback, for example @JsonTypeInfo(use = Id.NAME, defaultImpl = ...), every distinct unrecognized type ID resolves to the same fallback deserializer but is retained as its own key in the _deserializers m

**Evidencia:** `Paquete: com.fasterxml.jackson.core:jackson-databind v2.21.5 | Fix: 2.18.11, 2.21.7, 2.22.3`

**✅ Remediación:** Actualizar com.fasterxml.jackson.core:jackson-databind de 2.21.5 a 2.18.11, 2.21.7, 2.22.3

---

#### 🟠 [HIGH] CVE-2026-91777 – com.fasterxml.jackson.core/jackson-databind: tools.jackson.core:jackson-databind: Jackson-databind: Denial of Service via quadratic forward-reference completion

| Campo | Valor |
|---|---|
| **ID** | `TRI-0CBF6D15` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `Java:None` |

**Descripción:** Forward-reference completion for @JsonIdentityInfo object IDs in FasterXML jackson-databind performs a linear scan of the pending-reference accumulator for every resolved ID. The affected paths are CollectionDeserializer.CollectionReferringAccumulator.resolveForwardReference() and the equivalent implementation in MapDeserializer. When a document first creates N unresolved object-ID references in a

**Evidencia:** `Paquete: com.fasterxml.jackson.core:jackson-databind v2.21.5 | Fix: 2.21.7, 2.18.11, 2.22.3`

**✅ Remediación:** Actualizar com.fasterxml.jackson.core:jackson-databind de 2.21.5 a 2.21.7, 2.18.11, 2.22.3

---

#### 🟠 [HIGH] CVE-2016-3674 – XStream: enabled processing of external entities

| Campo | Valor |
|---|---|
| **ID** | `TRI-D47A216A` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `Java:None` |

**Descripción:** Multiple XML external entity (XXE) vulnerabilities in the (1) Dom4JDriver, (2) DomDriver, (3) JDomDriver, (4) JDom2Driver, (5) SjsxpDriver, (6) StandardStaxDriver, and (7) WstxDriver drivers in XStream before 1.4.9 allow remote attackers to read arbitrary files via a crafted XML document.

**Evidencia:** `Paquete: com.thoughtworks.xstream:xstream v1.4.5 | Fix: 1.4.9`

**✅ Remediación:** Actualizar com.thoughtworks.xstream:xstream de 1.4.5 a 1.4.9

---

#### 🟠 [HIGH] CVE-2017-7957 – XStream: DoS when unmarshalling void type

| Campo | Valor |
|---|---|
| **ID** | `TRI-AD9A9896` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `Java:None` |

**Descripción:** XStream through 1.4.9, when a certain denyTypes workaround is not used, mishandles attempts to create an instance of the primitive type 'void' during unmarshalling, leading to a remote application crash, as demonstrated by an xstream.fromXML("<void/>") call.

**Evidencia:** `Paquete: com.thoughtworks.xstream:xstream v1.4.5 | Fix: 1.4.10`

**✅ Remediación:** Actualizar com.thoughtworks.xstream:xstream de 1.4.5 a 1.4.10

---

#### 🟠 [HIGH] CVE-2020-26217 – XStream: remote code execution due to insecure XML deserialization when relying on blocklists

| Campo | Valor |
|---|---|
| **ID** | `TRI-D8E5E4D2` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `8.8` |
| **Archivo** | `Java:None` |

**Descripción:** XStream before version 1.4.14 is vulnerable to Remote Code Execution.The vulnerability may allow a remote attacker to run arbitrary shell commands only by manipulating the processed input stream. Only users who rely on blocklists are affected. Anyone using XStream's Security Framework allowlist is not affected. The linked advisory provides code workarounds for users who cannot upgrade. The issue i

**Evidencia:** `Paquete: com.thoughtworks.xstream:xstream v1.4.5 | Fix: 1.4.14-java7`

**✅ Remediación:** Actualizar com.thoughtworks.xstream:xstream de 1.4.5 a 1.4.14-java7

---

#### 🟠 [HIGH] CVE-2021-21341 – XStream: allow a remote attacker to cause DoS only by manipulating the processed input stream

| Campo | Valor |
|---|---|
| **ID** | `TRI-D663ABA3` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `Java:None` |

**Descripción:** XStream is a Java library to serialize objects to XML and back again. In XStream before version 1.4.16, there is vulnerability which may allow a remote attacker to allocate 100% CPU time on the target system depending on CPU type or parallel execution of such a payload resulting in a denial of service only by manipulating the processed input stream. No user is affected who followed the recommendat

**Evidencia:** `Paquete: com.thoughtworks.xstream:xstream v1.4.5 | Fix: 1.4.16`

**✅ Remediación:** Actualizar com.thoughtworks.xstream:xstream de 1.4.5 a 1.4.16

---

#### 🟠 [HIGH] CVE-2021-29505 – XStream: remote command execution attack by manipulating the processed input stream

| Campo | Valor |
|---|---|
| **ID** | `TRI-8DCA53D9` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `8.8` |
| **Archivo** | `Java:None` |

**Descripción:** XStream is software for serializing Java objects to XML and back again. A vulnerability in XStream versions prior to 1.4.17 may allow a remote attacker has sufficient rights to execute commands of the host only by manipulating the processed input stream. No user who followed the recommendation to setup XStream's security framework with a whitelist limited to the minimal required types is affected.

**Evidencia:** `Paquete: com.thoughtworks.xstream:xstream v1.4.5 | Fix: 1.4.17`

**✅ Remediación:** Actualizar com.thoughtworks.xstream:xstream de 1.4.5 a 1.4.17

---

#### 🟠 [HIGH] CVE-2021-39139 – xstream: Arbitrary code execution via unsafe deserialization of Xalan xsltc.trax.TemplatesImpl

| Campo | Valor |
|---|---|
| **ID** | `TRI-5D555486` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `8.8` |
| **Archivo** | `Java:None` |

**Descripción:** XStream is a simple library to serialize objects to XML and back again. In affected versions this vulnerability may allow a remote attacker to load and execute arbitrary code from a remote host only by manipulating the processed input stream. A user is only affected if using the version out of the box with JDK 1.7u21 or below. However, this scenario can be adjusted easily to an external Xalan that

**Evidencia:** `Paquete: com.thoughtworks.xstream:xstream v1.4.5 | Fix: 1.4.18`

**✅ Remediación:** Actualizar com.thoughtworks.xstream:xstream de 1.4.5 a 1.4.18

---

#### 🟠 [HIGH] CVE-2021-39141 – xstream: Arbitrary code execution via unsafe deserialization of com.sun.xml.internal.ws.client.sei.*

| Campo | Valor |
|---|---|
| **ID** | `TRI-B27F3E9F` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `8.5` |
| **Archivo** | `Java:None` |

**Descripción:** XStream is a simple library to serialize objects to XML and back again. In affected versions this vulnerability may allow a remote attacker to load and execute arbitrary code from a remote host only by manipulating the processed input stream. No user is affected, who followed the recommendation to setup XStream's security framework with a whitelist limited to the minimal required types. XStream 1.

**Evidencia:** `Paquete: com.thoughtworks.xstream:xstream v1.4.5 | Fix: 1.4.18`

**✅ Remediación:** Actualizar com.thoughtworks.xstream:xstream de 1.4.5 a 1.4.18

---

#### 🟠 [HIGH] CVE-2021-39144 – xstream: Arbitrary code execution via unsafe deserialization of sun.tracing.*

| Campo | Valor |
|---|---|
| **ID** | `TRI-70832944` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `8.5` |
| **Archivo** | `Java:None` |

**Descripción:** XStream is a simple library to serialize objects to XML and back again. In affected versions this vulnerability may allow a remote attacker has sufficient rights to execute commands of the host only by manipulating the processed input stream. No user is affected, who followed the recommendation to setup XStream's security framework with a whitelist limited to the minimal required types. XStream 1.

**Evidencia:** `Paquete: com.thoughtworks.xstream:xstream v1.4.5 | Fix: 1.4.18`

**✅ Remediación:** Actualizar com.thoughtworks.xstream:xstream de 1.4.5 a 1.4.18

---

#### 🟠 [HIGH] CVE-2021-39145 – xstream: Arbitrary code execution via unsafe deserialization of com.sun.jndi.ldap.LdapBindingEnumeration

| Campo | Valor |
|---|---|
| **ID** | `TRI-3C7A2AF3` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `8.5` |
| **Archivo** | `Java:None` |

**Descripción:** XStream is a simple library to serialize objects to XML and back again. In affected versions this vulnerability may allow a remote attacker to load and execute arbitrary code from a remote host only by manipulating the processed input stream. No user is affected, who followed the recommendation to setup XStream's security framework with a whitelist limited to the minimal required types. XStream 1.

**Evidencia:** `Paquete: com.thoughtworks.xstream:xstream v1.4.5 | Fix: 1.4.18`

**✅ Remediación:** Actualizar com.thoughtworks.xstream:xstream de 1.4.5 a 1.4.18

---

#### 🟠 [HIGH] CVE-2021-39146 – xstream: Arbitrary code execution via unsafe deserialization of javax.swing.UIDefaults$ProxyLazyValue

| Campo | Valor |
|---|---|
| **ID** | `TRI-DB28849B` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `8.5` |
| **Archivo** | `Java:None` |

**Descripción:** XStream is a simple library to serialize objects to XML and back again. In affected versions this vulnerability may allow a remote attacker to load and execute arbitrary code from a remote host only by manipulating the processed input stream. No user is affected, who followed the recommendation to setup XStream's security framework with a whitelist limited to the minimal required types. XStream 1.

**Evidencia:** `Paquete: com.thoughtworks.xstream:xstream v1.4.5 | Fix: 1.4.18`

**✅ Remediación:** Actualizar com.thoughtworks.xstream:xstream de 1.4.5 a 1.4.18

---

#### 🟠 [HIGH] CVE-2021-39147 – xstream: Arbitrary code execution via unsafe deserialization of com.sun.jndi.ldap.LdapSearchEnumeration

| Campo | Valor |
|---|---|
| **ID** | `TRI-A1163F30` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `8.5` |
| **Archivo** | `Java:None` |

**Descripción:** XStream is a simple library to serialize objects to XML and back again. In affected versions this vulnerability may allow a remote attacker to load and execute arbitrary code from a remote host only by manipulating the processed input stream. No user is affected, who followed the recommendation to setup XStream's security framework with a whitelist limited to the minimal required types. XStream 1.

**Evidencia:** `Paquete: com.thoughtworks.xstream:xstream v1.4.5 | Fix: 1.4.18`

**✅ Remediación:** Actualizar com.thoughtworks.xstream:xstream de 1.4.5 a 1.4.18

---

#### 🟠 [HIGH] CVE-2021-39148 – xstream: Arbitrary code execution via unsafe deserialization of com.sun.jndi.toolkit.dir.ContextEnumerator

| Campo | Valor |
|---|---|
| **ID** | `TRI-4F1231D5` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `8.5` |
| **Archivo** | `Java:None` |

**Descripción:** XStream is a simple library to serialize objects to XML and back again. In affected versions this vulnerability may allow a remote attacker to load and execute arbitrary code from a remote host only by manipulating the processed input stream. No user is affected, who followed the recommendation to setup XStream's security framework with a whitelist limited to the minimal required types. XStream 1.

**Evidencia:** `Paquete: com.thoughtworks.xstream:xstream v1.4.5 | Fix: 1.4.18`

**✅ Remediación:** Actualizar com.thoughtworks.xstream:xstream de 1.4.5 a 1.4.18

---

#### 🟠 [HIGH] CVE-2021-39149 – xstream: Arbitrary code execution via unsafe deserialization of com.sun.corba.*

| Campo | Valor |
|---|---|
| **ID** | `TRI-D212FC06` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `8.5` |
| **Archivo** | `Java:None` |

**Descripción:** XStream is a simple library to serialize objects to XML and back again. In affected versions this vulnerability may allow a remote attacker to load and execute arbitrary code from a remote host only by manipulating the processed input stream. No user is affected, who followed the recommendation to setup XStream's security framework with a whitelist limited to the minimal required types. XStream 1.

**Evidencia:** `Paquete: com.thoughtworks.xstream:xstream v1.4.5 | Fix: 1.4.18`

**✅ Remediación:** Actualizar com.thoughtworks.xstream:xstream de 1.4.5 a 1.4.18

---

#### 🟠 [HIGH] CVE-2021-39150 – xstream: Server-side request forgery (SSRF) via unsafe deserialization of com.sun.xml.internal.ws.client.sei.*

| Campo | Valor |
|---|---|
| **ID** | `TRI-ECBC33C3` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `8.5` |
| **Archivo** | `Java:None` |

**Descripción:** XStream is a simple library to serialize objects to XML and back again. In affected versions this vulnerability may allow a remote attacker to request data from internal resources that are not publicly available only by manipulating the processed input stream with a Java runtime version 14 to 8. No user is affected, who followed the recommendation to setup XStream's security framework with a white

**Evidencia:** `Paquete: com.thoughtworks.xstream:xstream v1.4.5 | Fix: 1.4.18`

**✅ Remediación:** Actualizar com.thoughtworks.xstream:xstream de 1.4.5 a 1.4.18

---

#### 🟠 [HIGH] CVE-2021-39151 – xstream: Arbitrary code execution via unsafe deserialization of com.sun.jndi.ldap.LdapBindingEnumeration

| Campo | Valor |
|---|---|
| **ID** | `TRI-53B3EEFF` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `8.5` |
| **Archivo** | `Java:None` |

**Descripción:** XStream is a simple library to serialize objects to XML and back again. In affected versions this vulnerability may allow a remote attacker to load and execute arbitrary code from a remote host only by manipulating the processed input stream. No user is affected, who followed the recommendation to setup XStream's security framework with a whitelist limited to the minimal required types. XStream 1.

**Evidencia:** `Paquete: com.thoughtworks.xstream:xstream v1.4.5 | Fix: 1.4.18`

**✅ Remediación:** Actualizar com.thoughtworks.xstream:xstream de 1.4.5 a 1.4.18

---

#### 🟠 [HIGH] CVE-2021-39152 – xstream: Server-side request forgery (SSRF) via unsafe deserialization of jdk.nashorn.internal.runtime.Source$URLData

| Campo | Valor |
|---|---|
| **ID** | `TRI-C73B35F6` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `8.5` |
| **Archivo** | `Java:None` |

**Descripción:** XStream is a simple library to serialize objects to XML and back again. In affected versions this vulnerability may allow a remote attacker to request data from internal resources that are not publicly available only by manipulating the processed input stream with a Java runtime version 14 to 8. No user is affected, who followed the recommendation to setup XStream's security framework with a white

**Evidencia:** `Paquete: com.thoughtworks.xstream:xstream v1.4.5 | Fix: 1.4.18`

**✅ Remediación:** Actualizar com.thoughtworks.xstream:xstream de 1.4.5 a 1.4.18

---

#### 🟠 [HIGH] CVE-2021-39153 – xstream: Arbitrary code execution via unsafe deserialization of Xalan xsltc.trax.TemplatesImpl

| Campo | Valor |
|---|---|
| **ID** | `TRI-1ACCC553` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `8.5` |
| **Archivo** | `Java:None` |

**Descripción:** XStream is a simple library to serialize objects to XML and back again. In affected versions this vulnerability may allow a remote attacker to load and execute arbitrary code from a remote host only by manipulating the processed input stream, if using the version out of the box with Java runtime version 14 to 8 or with JavaFX installed. No user is affected, who followed the recommendation to setup

**Evidencia:** `Paquete: com.thoughtworks.xstream:xstream v1.4.5 | Fix: 1.4.18`

**✅ Remediación:** Actualizar com.thoughtworks.xstream:xstream de 1.4.5 a 1.4.18

---

#### 🟠 [HIGH] CVE-2021-39154 – xstream: Arbitrary code execution via unsafe deserialization of javax.swing.UIDefaults$ProxyLazyValue

| Campo | Valor |
|---|---|
| **ID** | `TRI-EBF759F6` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `8.5` |
| **Archivo** | `Java:None` |

**Descripción:** XStream is a simple library to serialize objects to XML and back again. In affected versions this vulnerability may allow a remote attacker to load and execute arbitrary code from a remote host only by manipulating the processed input stream. No user is affected, who followed the recommendation to setup XStream's security framework with a whitelist limited to the minimal required types. XStream 1.

**Evidencia:** `Paquete: com.thoughtworks.xstream:xstream v1.4.5 | Fix: 1.4.18`

**✅ Remediación:** Actualizar com.thoughtworks.xstream:xstream de 1.4.5 a 1.4.18

---

#### 🟠 [HIGH] CVE-2021-43859 – xstream: Injecting highly recursive collections or maps can cause a DoS

| Campo | Valor |
|---|---|
| **ID** | `TRI-E877AF64` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `Java:None` |

**Descripción:** XStream is an open source java library to serialize objects to XML and back again. Versions prior to 1.4.19 may allow a remote attacker to allocate 100% CPU time on the target system depending on CPU type or parallel execution of such a payload resulting in a denial of service only by manipulating the processed input stream. XStream 1.4.19 monitors and accumulates the time it takes to add elements

**Evidencia:** `Paquete: com.thoughtworks.xstream:xstream v1.4.5 | Fix: 1.4.19`

**✅ Remediación:** Actualizar com.thoughtworks.xstream:xstream de 1.4.5 a 1.4.19

---

#### 🟠 [HIGH] CVE-2022-40151 – xstream: Xstream to serialise XML data was vulnerable to Denial of Service attacks

| Campo | Valor |
|---|---|
| **ID** | `TRI-0D0FB2CD` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `Java:None` |

**Descripción:** Those using Xstream to seralize XML data may be vulnerable to Denial of Service attacks (DOS). If the parser is running on user supplied input, an attacker may supply content that causes the parser to crash by stackoverflow. This effect may support a denial of service attack.

**Evidencia:** `Paquete: com.thoughtworks.xstream:xstream v1.4.5 | Fix: 1.4.20`

**✅ Remediación:** Actualizar com.thoughtworks.xstream:xstream de 1.4.5 a 1.4.20

---

#### 🟠 [HIGH] CVE-2022-41966 – xstream: Denial of Service by injecting recursive collections or maps based on element's hash values raising a stack overflow

| Campo | Valor |
|---|---|
| **ID** | `TRI-18456E36` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `Java:None` |

**Descripción:** XStream serializes Java objects to XML and back again. Versions prior to 1.4.20 may allow a remote attacker to terminate the application with a stack overflow error, resulting in a denial of service only via manipulation the processed input stream. The attack uses the hash code implementation for collections and maps to force recursive hash calculation causing a stack overflow. This issue is patch

**Evidencia:** `Paquete: com.thoughtworks.xstream:xstream v1.4.5 | Fix: 1.4.20`

**✅ Remediación:** Actualizar com.thoughtworks.xstream:xstream de 1.4.5 a 1.4.20

---

#### 🟠 [HIGH] CVE-2024-47072 – com.thoughtworks.xstream: XStream is vulnerable to a Denial of Service attack due to stack overflow from a manipulated binary input stream

| Campo | Valor |
|---|---|
| **ID** | `TRI-CF56C805` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `Java:None` |

**Descripción:** XStream is a simple library to serialize objects to XML and back again. This vulnerability may allow a remote attacker to terminate the application with a stack overflow error resulting in a denial of service only by manipulating the processed input stream when XStream is configured to use the BinaryStreamDriver. XStream 1.4.21 has been patched to detect the manipulation in the binary input stream

**Evidencia:** `Paquete: com.thoughtworks.xstream:xstream v1.4.5 | Fix: 1.4.21`

**✅ Remediación:** Actualizar com.thoughtworks.xstream:xstream de 1.4.5 a 1.4.21

---

#### 🟡🟢⚪ Medios, Bajos e Info (53)

| Severidad | CVE / Advisory | CVSS | Remediación |
|---|---|---|---|
| 🟡 MEDIUM | CVE-2025-69644 – binutils: Binutils: Denial of Service  | 2.8 | No hay fix disponible para binutils 2.42-4ubuntu2.10 — considerar alte |
| 🟡 MEDIUM | CVE-2025-69645 – binutils: Binutils objdump: Denial of  | 2.8 | No hay fix disponible para binutils 2.42-4ubuntu2.10 — considerar alte |
| 🟡 MEDIUM | CVE-2025-69646 – binutils: Binutils: Denial of Service  | 2.8 | No hay fix disponible para binutils 2.42-4ubuntu2.10 — considerar alte |
| 🟡 MEDIUM | CVE-2025-69647 – binutils: infinite loop in readelf via | 3.3 | No hay fix disponible para binutils 2.42-4ubuntu2.10 — considerar alte |
| 🟡 MEDIUM | CVE-2025-69648 – binutils: infinite loop in readelf via | 3.3 | No hay fix disponible para binutils 2.42-4ubuntu2.10 — considerar alte |
| 🟡 MEDIUM | CVE-2025-69651 – binutils: Binutils: Denial of Service  | 5.5 | No hay fix disponible para binutils 2.42-4ubuntu2.10 — considerar alte |
| 🟡 MEDIUM | CVE-2025-69652 – binutils: abort in readelf via crafted | 3.3 | No hay fix disponible para binutils 2.42-4ubuntu2.10 — considerar alte |
| 🟡 MEDIUM | CVE-2026-76642 – util-linux: util-linux: failed externa | 7.8 | No hay fix disponible para bsdutils 1:2.39.3-9ubuntu6.6 — considerar a |
| 🟡 MEDIUM | CVE-2026-102473 – dash: dash: Super-polynomial backtrac | 5.5 | No hay fix disponible para dash 0.5.12-6ubuntu5 — considerar alternati |
| 🟡 MEDIUM | CVE-2026-102474 – dash: dash: Heap out-of-bounds write  | 4.0 | No hay fix disponible para dash 0.5.12-6ubuntu5 — considerar alternati |
| 🟡 MEDIUM | CVE-2026-18374 – glibc: glibc: Heap buffer overflow via | 4.9 | Actualizar libc-bin de 2.39-0ubuntu8.9 a 2.39-0ubuntu8.12 |
| 🟡 MEDIUM | CVE-2026-84243 – glibc: glibc: Arbitrary code execution | 7.0 | Actualizar libc-bin de 2.39-0ubuntu8.9 a 2.39-0ubuntu8.12 |
| 🟡 MEDIUM | CVE-2026-8674 – glibc: glibc DNS stub resolver: Denial  | 5.3 | Actualizar libc-bin de 2.39-0ubuntu8.9 a 2.39-0ubuntu8.12 |
| 🟡 MEDIUM | CVE-2026-86805 – glibc: glibc: Privilege escalation and | 7.0 | Actualizar libc-bin de 2.39-0ubuntu8.9 a 2.39-0ubuntu8.12 |
| 🟡 MEDIUM | CVE-2026-95818 – glibc: glibc: Local attacker can cause | 7.0 | Actualizar libc-bin de 2.39-0ubuntu8.9 a 2.39-0ubuntu8.12 |
| 🟡 MEDIUM | CVE-2026-97399 – glibc: glibc: Denial of Service via ou | 3.7 | Actualizar libc-bin de 2.39-0ubuntu8.9 a 2.39-0ubuntu8.12 |
| 🟡 MEDIUM | CVE-2025-66382 – libexpat: libexpat: Denial of service  | 5.5 | No hay fix disponible para libexpat1 2.6.1-2ubuntu0.6 — considerar alt |
| 🟡 MEDIUM | CVE-2026-102633 – expat: expat: Denial of Service via i | 5.9 | No hay fix disponible para libexpat1 2.6.1-2ubuntu0.6 — considerar alt |
| 🟡 MEDIUM | CVE-2026-95512 – freetype: FreeType: Denial of Service  | 5.5 | Actualizar libfreetype6 de 2.13.2+dfsg-1ubuntu0.1 a 2.13.2+dfsg-1ubunt |
| 🟡 MEDIUM | CVE-2026-67693 – gnutls: gnutls: Information disclosure | None | No hay fix disponible para libgnutls30t64 3.8.3-1.1ubuntu3.6 — conside |
| 🟡 MEDIUM | CVE-2026-88647 – gnutls: gnutls: Information disclosure | None | No hay fix disponible para libgnutls30t64 3.8.3-1.1ubuntu3.6 — conside |
| 🟡 MEDIUM | CVE-2026-88648 – gnutls: gnutls: Cross-domain certifica | None | No hay fix disponible para libgnutls30t64 3.8.3-1.1ubuntu3.6 — conside |
| 🟡 MEDIUM | CVE-2026-95184 – gnutls: gnutls: legitimate user certif | 5.3 | No hay fix disponible para libgnutls30t64 3.8.3-1.1ubuntu3.6 — conside |
| 🟡 MEDIUM | CVE-2026-95210 – gnutls: gnutls: certificates with inva | None | No hay fix disponible para libgnutls30t64 3.8.3-1.1ubuntu3.6 — conside |
| 🟡 MEDIUM | CVE-2026-103111 – pcre2: pcre2: Out-of-bounds write via | 7.6 | Actualizar libpcre2-8-0 de 10.42-4ubuntu2.1 a 10.42-4ubuntu2.2 |
| 🟡 MEDIUM | CVE-2026-86145 – pcre2: PCRE2: Out-of-bounds write allo | 8.2 | Actualizar libpcre2-8-0 de 10.42-4ubuntu2.1 a 10.42-4ubuntu2.2 |
| 🟡 MEDIUM | CVE-2026-89156 – PCRE2: PCRE2: Out-of-bounds read via i | 5.9 | Actualizar libpcre2-8-0 de 10.42-4ubuntu2.1 a 10.42-4ubuntu2.2 |
| 🟡 MEDIUM | CVE-2026-89157 – pcre2: PCRE2: Out-of-bounds write via  | 7.4 | Actualizar libpcre2-8-0 de 10.42-4ubuntu2.1 a 10.42-4ubuntu2.2 |
| 🟡 MEDIUM | CVE-2026-89158 – PCRE2: PCRE2: Out-of-bounds write via  | 6.5 | Actualizar libpcre2-8-0 de 10.42-4ubuntu2.1 a 10.42-4ubuntu2.2 |
| 🟡 MEDIUM | CVE-2026-89160 – pcre2: PCRE2: Denial of Service via ou | 6.5 | Actualizar libpcre2-8-0 de 10.42-4ubuntu2.1 a 10.42-4ubuntu2.2 |
| 🟡 MEDIUM | CVE-2026-89161 – pcre2: PCRE2: Memory corruption vulner | 7.8 | Actualizar libpcre2-8-0 de 10.42-4ubuntu2.1 a 10.42-4ubuntu2.2 |
| 🟡 MEDIUM | CVE-2026-46675 – libpng: libpng: Use-after-free in sequ | 5.9 | Actualizar libpng16-16t64 de 1.6.43-5ubuntu0.6 a 1.6.43-5ubuntu0.7 |
| 🟡 MEDIUM | CVE-2026-121876 – sandboxed-containers: kernel: systemd | 7.9 | No hay fix disponible para libsystemd0 255.4-1ubuntu8.17 — considerar  |
| 🟡 MEDIUM | CVE-2026-82560 – Pod::Text versions before 6.1.1 for Pe | None | Actualizar perl-base de 5.38.2-3.2ubuntu0.6 a 5.38.2-3.2ubuntu0.7 |
| 🟡 MEDIUM | CVE-2026-18477 – tar: tar: TOCTOU in incremental dumpdi | 4.4 | No hay fix disponible para tar 1.35+dfsg-3ubuntu0.4 — considerar alter |
| 🟡 MEDIUM | CVE-2026-18508 – tar: tar: --one-top-level hardlink tar | 4.4 | No hay fix disponible para tar 1.35+dfsg-3ubuntu0.4 — considerar alter |
| 🟡 MEDIUM | CVE-2026-85091 – zlib: zlib: Heap buffer overflow in gz | 8.1 | Actualizar zlib1g de 1:1.3.dfsg-3.1ubuntu2.2 a 1:1.3.dfsg-3.1ubuntu2.3 |
| 🟡 MEDIUM | CVE-2026-19032 – com.fasterxml.jackson.core/jackson-dat | 5.3 | Actualizar com.fasterxml.jackson.core:jackson-databind de 2.21.5 a 2.1 |
| 🟡 MEDIUM | CVE-2026-83557 – com.fasterxml.jackson.core/jackson-dat | 5.6 | Actualizar com.fasterxml.jackson.core:jackson-databind de 2.21.5 a 2.1 |
| 🟡 MEDIUM | CVE-2020-26258 – XStream: Server-Side Forgery Request v | 7.7 | Actualizar com.thoughtworks.xstream:xstream de 1.4.5 a 1.4.15 |
| 🟡 MEDIUM | CVE-2020-26259 – XStream: arbitrary file deletion on th | 6.8 | Actualizar com.thoughtworks.xstream:xstream de 1.4.5 a 1.4.15 |
| 🟡 MEDIUM | CVE-2021-21342 – XStream: SSRF via crafted input stream | 9.1 | Actualizar com.thoughtworks.xstream:xstream de 1.4.5 a 1.4.16 |
| 🟡 MEDIUM | CVE-2021-21343 – XStream: arbitrary file deletion on th | 7.5 | Actualizar com.thoughtworks.xstream:xstream de 1.4.5 a 1.4.16 |
| 🟡 MEDIUM | CVE-2021-21344 – XStream: Unsafe deserizaliation of jav | 9.8 | Actualizar com.thoughtworks.xstream:xstream de 1.4.5 a 1.4.16 |
| 🟡 MEDIUM | CVE-2021-21345 – XStream: Unsafe deserizaliation of com | 9.9 | Actualizar com.thoughtworks.xstream:xstream de 1.4.5 a 1.4.16 |
| 🟡 MEDIUM | CVE-2021-21346 – XStream: Unsafe deserizaliation of sun | 9.8 | Actualizar com.thoughtworks.xstream:xstream de 1.4.5 a 1.4.16 |
| 🟡 MEDIUM | CVE-2021-21347 – XStream: Unsafe deserizaliation of com | 9.8 | Actualizar com.thoughtworks.xstream:xstream de 1.4.5 a 1.4.16 |
| 🟡 MEDIUM | CVE-2021-21348 – XStream: ReDoS vulnerability | 7.5 | Actualizar com.thoughtworks.xstream:xstream de 1.4.5 a 1.4.16 |
| 🟡 MEDIUM | CVE-2021-21349 – XStream: SSRF can be activated unmarsh | 8.6 | Actualizar com.thoughtworks.xstream:xstream de 1.4.5 a 1.4.16 |
| 🟡 MEDIUM | CVE-2021-21350 – XStream: Unsafe deserizaliation of com | 9.8 | Actualizar com.thoughtworks.xstream:xstream de 1.4.5 a 1.4.16 |
| 🟡 MEDIUM | CVE-2021-21351 – XStream: allow a remote attacker to lo | 9.1 | Actualizar com.thoughtworks.xstream:xstream de 1.4.5 a 1.4.16 |
| 🟡 MEDIUM | CVE-2021-39140 – xstream: Infinite loop DoS via unsafe  | 6.3 | Actualizar com.thoughtworks.xstream:xstream de 1.4.5 a 1.4.18 |
| 🟡 MEDIUM | CVE-2025-48924 – commons-lang/commons-lang: org.apache. | 3.7 | Actualizar org.apache.commons:commons-lang3 de 3.14.0 a 3.18.0 |

### 🌐 OWASP ZAP (DAST) — `ASC-DAST-001`

> **Tipo:** Análisis Dinámico en Ejecución  
> **Raw:** 3 | **Únicos:** 3 | **Deduplicados:** 0 (0.0%)

**Distribución:** 🟡 MEDIUM: **1** | 🟢 LOW: **1** | ⚪ INFO: **1**

#### 🟡🟢⚪ Medios, Bajos e Info (3)

| Severidad | Hallazgo | Endpoint | Remediación |
|---|---|---|---|
| 🟡 MEDIUM | Content Security Policy (CSP) Header Not Set | `http://localhost:8080` | Ensure that your web server, application server, load balancer, etc. i |
| 🟢 LOW | Permissions Policy Header Not Set | `http://localhost:8080` | Ensure that your web server, application server, load balancer, etc. i |
| ⚪ INFO | Storable and Cacheable Content | `http://localhost:8080` | Validate that the response does not contain sensitive, personal or use |

### 🎯 Nuclei (Pentesting) — `ASC-PENTEST-001`

> **Tipo:** Validación Activa de Templates  
> **Raw:** 12 | **Únicos:** 3 | **Deduplicados:** 9 (75.0%)

**Distribución:** 🟢 LOW: **3**

#### 🟡🟢⚪ Medios, Bajos e Info (3)

| Severidad | Hallazgo | Endpoint | Remediación |
|---|---|---|---|
| 🟢 LOW | SSH SHA-1 HMAC Algorithms Enabled | `localhost:22` | Revisar: The SSH server at the remote end is set up to allow the use o |
| 🟢 LOW | Tomcat Stack Traces Enabled | `http://localhost:8080/?f=\[` | Revisar: Examine whether Tomcat stack traces are turned on by employin |
| 🟢 LOW | HTTP Missing Security Headers | `http://localhost:8080` | Revisar: This template searches for missing HTTP security headers. The |

### 🔐 Semgrep (SAST) — `ASC-SAST-001`

> **Tipo:** Análisis Estático de Código  
> **Raw:** 17 | **Únicos:** 16 | **Deduplicados:** 1 (5.9%)

**Distribución:** 🟠 HIGH: **13** | 🟡 MEDIUM: **3**

#### 🔴🟠 Críticos y Altos (13)

#### 🟠 [HIGH] Tainted Sql String

| Campo | Valor |
|---|---|
| **ID** | `SEM-1557C43F` |
| **Herramienta** | `SEMGREP` (SAST) |
| **ASC ISO/IEC 27034** | `ASC-SAST-001` |
| **Categoría OWASP** | A03:2021 – Injection |
| **CWE** | `["CWE-89: Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection')"]` |
| **Archivo** | `source_to_scan/src/main/java/org/owasp/webgoat/lessons/challenges/challenge5/Assignment5.java:45` |

**Descripción:** User data flows into this manually-constructed SQL string. User data can be safely inserted into SQL strings using prepared statements or an object-relational mapper (ORM). Manually-constructed SQL strings is a possible indicator of SQL injection, which could let an attacker steal or manipulate data from the database. Instead, use prepared statements (`connection.PreparedStatement`) or a safe libr

**Evidencia:** `requires login`

**✅ Remediación:** Revisar y corregir el patrón identificado en source_to_scan/src/main/java/org/owasp/webgoat/lessons/challenges/challenge5/Assignment5.java:45

---

#### 🟠 [HIGH] Formatted Sql String

| Campo | Valor |
|---|---|
| **ID** | `SEM-27642124` |
| **Herramienta** | `SEMGREP` (SAST) |
| **ASC ISO/IEC 27034** | `ASC-SAST-001` |
| **Categoría OWASP** | A03:2021 – Injection |
| **CWE** | `["CWE-89: Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection')"]` |
| **Archivo** | `source_to_scan/src/main/java/org/owasp/webgoat/lessons/challenges/challenge5/Assignment5.java:50` |

**Descripción:** Detected a formatted string in a SQL statement. This could lead to SQL injection if variables in the SQL statement are not properly sanitized. Use a prepared statements (java.sql.PreparedStatement) instead. You can obtain a PreparedStatement using 'connection.prepareStatement'.

**Evidencia:** `requires login`

**✅ Remediación:** Revisar y corregir el patrón identificado en source_to_scan/src/main/java/org/owasp/webgoat/lessons/challenges/challenge5/Assignment5.java:50

---

#### 🟠 [HIGH] Tainted Url Host

| Campo | Valor |
|---|---|
| **ID** | `SEM-F36F98BE` |
| **Herramienta** | `SEMGREP` (SAST) |
| **ASC ISO/IEC 27034** | `ASC-SAST-001` |
| **Categoría OWASP** | A07:2021 – Identification and Authentication Failures |
| **CWE** | `['CWE-918: Server-Side Request Forgery (SSRF)']` |
| **Archivo** | `source_to_scan/src/main/java/org/owasp/webgoat/lessons/jwt/claimmisuse/JWTHeaderJKUEndpoint.java:57` |

**Descripción:** User data flows into the host portion of this manually-constructed URL. This could allow an attacker to send data to their own server, potentially exposing sensitive data such as cookies or authorization information sent with this request. They could also probe internal servers or other resources that the server running this code can access. (This is called server-side request forgery, or SSRF.) D

**Evidencia:** `requires login`

**✅ Remediación:** Revisar y corregir el patrón identificado en source_to_scan/src/main/java/org/owasp/webgoat/lessons/jwt/claimmisuse/JWTHeaderJKUEndpoint.java:57

---

#### 🟠 [HIGH] Httpservlet Path Traversal

| Campo | Valor |
|---|---|
| **ID** | `SEM-855AA649` |
| **Herramienta** | `SEMGREP` (SAST) |
| **ASC ISO/IEC 27034** | `ASC-SAST-001` |
| **Categoría OWASP** | A05:2021 – Security Misconfiguration |
| **CWE** | `["CWE-22: Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal')"]` |
| **Archivo** | `source_to_scan/src/main/java/org/owasp/webgoat/lessons/pathtraversal/ProfileUploadRetrieval.java:100` |

**Descripción:** Detected a potential path traversal. A malicious actor could control the location of this file, to include going backwards in the directory with '../'. To address this, ensure that user-controlled variables in file paths are sanitized. You may also consider using a utility method such as org.apache.commons.io.FilenameUtils.getName(...) to only retrieve the file name from the path.

**Evidencia:** `requires login`

**✅ Remediación:** Revisar y corregir el patrón identificado en source_to_scan/src/main/java/org/owasp/webgoat/lessons/pathtraversal/ProfileUploadRetrieval.java:100

---

#### 🟠 [HIGH] Tainted Sql String

| Campo | Valor |
|---|---|
| **ID** | `SEM-D5FBB9B3` |
| **Herramienta** | `SEMGREP` (SAST) |
| **ASC ISO/IEC 27034** | `ASC-SAST-001` |
| **Categoría OWASP** | A03:2021 – Injection |
| **CWE** | `["CWE-89: Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection')"]` |
| **Archivo** | `source_to_scan/src/main/java/org/owasp/webgoat/lessons/sqlinjection/advanced/SqlInjectionChallenge.java:55` |

**Descripción:** User data flows into this manually-constructed SQL string. User data can be safely inserted into SQL strings using prepared statements or an object-relational mapper (ORM). Manually-constructed SQL strings is a possible indicator of SQL injection, which could let an attacker steal or manipulate data from the database. Instead, use prepared statements (`connection.PreparedStatement`) or a safe libr

**Evidencia:** `requires login`

**✅ Remediación:** Revisar y corregir el patrón identificado en source_to_scan/src/main/java/org/owasp/webgoat/lessons/sqlinjection/advanced/SqlInjectionChallenge.java:55

---

#### 🟠 [HIGH] Formatted Sql String

| Campo | Valor |
|---|---|
| **ID** | `SEM-34BBB18F` |
| **Herramienta** | `SEMGREP` (SAST) |
| **ASC ISO/IEC 27034** | `ASC-SAST-001` |
| **Categoría OWASP** | A03:2021 – Injection |
| **CWE** | `["CWE-89: Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection')"]` |
| **Archivo** | `source_to_scan/src/main/java/org/owasp/webgoat/lessons/sqlinjection/advanced/SqlInjectionChallenge.java:57` |

**Descripción:** Detected a formatted string in a SQL statement. This could lead to SQL injection if variables in the SQL statement are not properly sanitized. Use a prepared statements (java.sql.PreparedStatement) instead. You can obtain a PreparedStatement using 'connection.prepareStatement'.

**Evidencia:** `requires login`

**✅ Remediación:** Revisar y corregir el patrón identificado en source_to_scan/src/main/java/org/owasp/webgoat/lessons/sqlinjection/advanced/SqlInjectionChallenge.java:57

---

#### 🟠 [HIGH] Formatted Sql String

| Campo | Valor |
|---|---|
| **ID** | `SEM-820966C3` |
| **Herramienta** | `SEMGREP` (SAST) |
| **ASC ISO/IEC 27034** | `ASC-SAST-001` |
| **Categoría OWASP** | A03:2021 – Injection |
| **CWE** | `["CWE-89: Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection')"]` |
| **Archivo** | `source_to_scan/src/main/java/org/owasp/webgoat/lessons/sqlinjection/introduction/SqlInjectionLesson10.java:56` |

**Descripción:** Detected a formatted string in a SQL statement. This could lead to SQL injection if variables in the SQL statement are not properly sanitized. Use a prepared statements (java.sql.PreparedStatement) instead. You can obtain a PreparedStatement using 'connection.prepareStatement'.

**Evidencia:** `requires login`

**✅ Remediación:** Revisar y corregir el patrón identificado en source_to_scan/src/main/java/org/owasp/webgoat/lessons/sqlinjection/introduction/SqlInjectionLesson10.java:56

---

#### 🟠 [HIGH] Formatted Sql String

| Campo | Valor |
|---|---|
| **ID** | `SEM-CDE10182` |
| **Herramienta** | `SEMGREP` (SAST) |
| **ASC ISO/IEC 27034** | `ASC-SAST-001` |
| **Categoría OWASP** | A03:2021 – Injection |
| **CWE** | `["CWE-89: Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection')"]` |
| **Archivo** | `source_to_scan/src/main/java/org/owasp/webgoat/lessons/sqlinjection/introduction/SqlInjectionLesson5a.java:52` |

**Descripción:** Detected a formatted string in a SQL statement. This could lead to SQL injection if variables in the SQL statement are not properly sanitized. Use a prepared statements (java.sql.PreparedStatement) instead. You can obtain a PreparedStatement using 'connection.prepareStatement'.

**Evidencia:** `requires login`

**✅ Remediación:** Revisar y corregir el patrón identificado en source_to_scan/src/main/java/org/owasp/webgoat/lessons/sqlinjection/introduction/SqlInjectionLesson5a.java:52

---

#### 🟠 [HIGH] Formatted Sql String

| Campo | Valor |
|---|---|
| **ID** | `SEM-48B3E255` |
| **Herramienta** | `SEMGREP` (SAST) |
| **ASC ISO/IEC 27034** | `ASC-SAST-001` |
| **Categoría OWASP** | A03:2021 – Injection |
| **CWE** | `["CWE-89: Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection')"]` |
| **Archivo** | `source_to_scan/src/main/java/org/owasp/webgoat/lessons/sqlinjection/introduction/SqlInjectionLesson5b.java:69` |

**Descripción:** Detected a formatted string in a SQL statement. This could lead to SQL injection if variables in the SQL statement are not properly sanitized. Use a prepared statements (java.sql.PreparedStatement) instead. You can obtain a PreparedStatement using 'connection.prepareStatement'.

**Evidencia:** `requires login`

**✅ Remediación:** Revisar y corregir el patrón identificado en source_to_scan/src/main/java/org/owasp/webgoat/lessons/sqlinjection/introduction/SqlInjectionLesson5b.java:69

---

#### 🟠 [HIGH] Formatted Sql String

| Campo | Valor |
|---|---|
| **ID** | `SEM-684DE80C` |
| **Herramienta** | `SEMGREP` (SAST) |
| **ASC ISO/IEC 27034** | `ASC-SAST-001` |
| **Categoría OWASP** | A03:2021 – Injection |
| **CWE** | `["CWE-89: Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection')"]` |
| **Archivo** | `source_to_scan/src/main/java/org/owasp/webgoat/lessons/sqlinjection/introduction/SqlInjectionLesson8.java:62` |

**Descripción:** Detected a formatted string in a SQL statement. This could lead to SQL injection if variables in the SQL statement are not properly sanitized. Use a prepared statements (java.sql.PreparedStatement) instead. You can obtain a PreparedStatement using 'connection.prepareStatement'.

**Evidencia:** `requires login`

**✅ Remediación:** Revisar y corregir el patrón identificado en source_to_scan/src/main/java/org/owasp/webgoat/lessons/sqlinjection/introduction/SqlInjectionLesson8.java:62

---

#### 🟠 [HIGH] Formatted Sql String

| Campo | Valor |
|---|---|
| **ID** | `SEM-42D9D5DE` |
| **Herramienta** | `SEMGREP` (SAST) |
| **ASC ISO/IEC 27034** | `ASC-SAST-001` |
| **Categoría OWASP** | A03:2021 – Injection |
| **CWE** | `["CWE-89: Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection')"]` |
| **Archivo** | `source_to_scan/src/main/java/org/owasp/webgoat/lessons/sqlinjection/introduction/SqlInjectionLesson9.java:65` |

**Descripción:** Detected a formatted string in a SQL statement. This could lead to SQL injection if variables in the SQL statement are not properly sanitized. Use a prepared statements (java.sql.PreparedStatement) instead. You can obtain a PreparedStatement using 'connection.prepareStatement'.

**Evidencia:** `requires login`

**✅ Remediación:** Revisar y corregir el patrón identificado en source_to_scan/src/main/java/org/owasp/webgoat/lessons/sqlinjection/introduction/SqlInjectionLesson9.java:65

---

#### 🟠 [HIGH] Tainted Sql String

| Campo | Valor |
|---|---|
| **ID** | `SEM-322B435C` |
| **Herramienta** | `SEMGREP` (SAST) |
| **ASC ISO/IEC 27034** | `ASC-SAST-001` |
| **Categoría OWASP** | A03:2021 – Injection |
| **CWE** | `["CWE-89: Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection')"]` |
| **Archivo** | `source_to_scan/src/main/java/org/owasp/webgoat/lessons/sqlinjection/mitigation/Servers.java:51` |

**Descripción:** User data flows into this manually-constructed SQL string. User data can be safely inserted into SQL strings using prepared statements or an object-relational mapper (ORM). Manually-constructed SQL strings is a possible indicator of SQL injection, which could let an attacker steal or manipulate data from the database. Instead, use prepared statements (`connection.PreparedStatement`) or a safe libr

**Evidencia:** `requires login`

**✅ Remediación:** Revisar y corregir el patrón identificado en source_to_scan/src/main/java/org/owasp/webgoat/lessons/sqlinjection/mitigation/Servers.java:51

---

#### 🟠 [HIGH] Tainted File Path

| Campo | Valor |
|---|---|
| **ID** | `SEM-04E1D7DF` |
| **Herramienta** | `SEMGREP` (SAST) |
| **ASC ISO/IEC 27034** | `ASC-SAST-001` |
| **Categoría OWASP** | A05:2021 – Security Misconfiguration |
| **CWE** | `['CWE-23: Relative Path Traversal']` |
| **Archivo** | `source_to_scan/src/main/java/org/owasp/webgoat/webwolf/FileServer.java:79` |

**Descripción:** Detected user input controlling a file path. An attacker could control the location of this file, to include going backwards in the directory with '../'. To address this, ensure that user-controlled variables in file paths are sanitized. You may also consider using a utility method such as org.apache.commons.io.FilenameUtils.getName(...) to only retrieve the file name from the path.

**Evidencia:** `requires login`

**✅ Remediación:** Revisar y corregir el patrón identificado en source_to_scan/src/main/java/org/owasp/webgoat/webwolf/FileServer.java:79

---

#### 🟡🟢⚪ Medios, Bajos e Info (3)

| Severidad | Hallazgo | Endpoint | Remediación |
|---|---|---|---|
| 🟡 MEDIUM | Tainted Session From Http Request | `None` | Revisar y corregir el patrón identificado en source_to_scan/src/main/j |
| 🟡 MEDIUM | Use Of Md5 | `None` | Revisar y corregir el patrón identificado en source_to_scan/src/main/j |
| 🟡 MEDIUM | Spring Unvalidated Redirect | `None` | Revisar y corregir el patrón identificado en source_to_scan/src/main/j |

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
| Semgrep OSS | SAST | `ASC-SAST-001` | 16 |
| Trivy | SCA | `ASC-SCA-001` | 87 |
| OWASP ZAP | DAST | `ASC-DAST-001` | 3 |
| Nuclei v3 | Pentesting | `ASC-PENTEST-001` | 3 |

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

- Este reporte corresponde a una única corrida sobre `webgoat`. La validación completa
  abarca nueve casos de estudio documentados en la tesis (Capítulo 5).
- La evaluación IA requiere validación humana antes de decisiones en producción.
- No reemplaza una auditoría de seguridad formal ni un pentest manual.
- El gate SSVC prioriza la cautela ante hallazgos críticos — ver tesis sección 5.6.3.

---

_Reporte generado el 2026-11-17 18:40:03 | Pipeline Run: `44148452239`_

_**Autores:** Jhojan Stiven Castaño Jejen & Juan Manuel Arango Rodas_
_**Universidad del Valle** — Ingeniería de Sistemas — 2026_
