# 🔐 Reporte de Seguridad DevSecOps
## ❌ Decisión de Despliegue: **FAIL**

---

> **Generado automáticamente por el DevSecOps Engine v1.3 — Universidad del Valle 2026**

| Campo | Valor |
|---|---|
| **Servicio** | `dvwa` |
| **Entorno** | `staging` |
| **Criticidad de negocio** | `high` |
| **Pipeline Run** | `44148411474` |
| **Timestamp** | `2026-11-17 18:36:44` |
| **Modelo IA** | `gpt-4o-mini` |
| **Tokens utilizados** | `8,854` (prompt: 7,357 / completion: 1,497) |
| **Motor IA híbrido** | ✅ Motor híbrido activo |
| **ISO/IEC 27034 — Trazabilidad** | ✅ 3/4 ASC obligatorios ejecutados |

---

## 📊 Resumen Ejecutivo

El análisis revela múltiples hallazgos críticos y altos que son explotables remotamente, lo que representa un riesgo significativo para el entorno de staging. La presencia de vulnerabilidades de inyección SQL y componentes vulnerables en el servidor Apache requiere atención inmediata.

> **Recomendación del sistema:** No se recomienda el despliegue hasta que se aborden las vulnerabilidades críticas identificadas.

---

## 🚦 Decisión Final del Security Gate

| Campo | Valor |
|---|---|
| **Decisión** | ❌ **FAIL** |
| **Fuente** | `ai_assisted` |
| **Nivel de riesgo (IA)** | `CRITICAL` |
| **Risk Score (IA)** | `0.0 / 10.0` |
| **Confianza IA** | `90%` |
| **Falsos positivos estimados** | `baja` |
| **ISO/IEC 27034 — Trazabilidad ANF** | `3/4` ASC obligatorios ejecutados (ver sección ISO/IEC 27034) |

---

## 📈 Estadísticas Globales de Hallazgos

### Distribución por Severidad

| Severidad | Hallazgos | % del total | Proporción |
|---|---|---|---|
| 🔴 CRITICAL | 65 | 15.0% | `██░░░░░░░░░░░░░` |
| 🟠 HIGH | 180 | 41.5% | `██████░░░░░░░░░` |
| 🟡 MEDIUM | 166 | 38.2% | `█████░░░░░░░░░░` |
| 🟢 LOW | 17 | 3.9% | `░░░░░░░░░░░░░░░` |
| ⚪ INFO | 6 | 1.4% | `░░░░░░░░░░░░░░░` |
| ─ | **434** | **100%** | |

### Cobertura por Herramienta y ASC ISO/IEC 27034

> Cada herramienta tiene asignado un ASC (Application Security Control) de ISO/IEC 27034.
> La columna **Removidos** indica duplicados eliminados, no falsos positivos.

| Herramienta | ASC ISO 27034 | Raw | Únicos | Removidos | % Dedup | Estado |
|---|---|---|---|---|---|---|
| 🔐 Semgrep (SAST) | `ASC-SAST-001` | 44 | 19 | 25 | 56.8% | ✅ Ejecutado |
| 🔬 Trivy (SCA) | `ASC-SCA-001` | 1447 | 386 | 1061 | 73.3% | ✅ Ejecutado |
| 🌐 OWASP ZAP (DAST) | `ASC-DAST-001` | 21 | 21 | 0 | 0.0% | ✅ Ejecutado |
| 🎯 Nuclei (Pentesting) | `ASC-PENTEST-001` | 8 | 8 | 0 | 0.0% | ✅ Ejecutado |

### Top 5 Categorías OWASP Top 10

| Categoría | Hallazgos | % del total | Proporción |
|---|---|---|---|
| `A06:2021 – Vulnerable and Outdated Components` | 389 | 89.6% | `██████████░░` |
| `A05:2021 – Security Misconfiguration` | 29 | 6.7% | `░░░░░░░░░░░░` |
| `A03:2021 – Injection` | 11 | 2.5% | `░░░░░░░░░░░░` |
| `A07:2021 – Identification and Authentication Failures` | 4 | 0.9% | `░░░░░░░░░░░░` |
| `A02:2021 – Cryptographic Failures` | 1 | 0.2% | `░░░░░░░░░░░░` |

---

## 🔄 Metodología de Deduplicación

> El normalizador aplica deduplicación para evitar el doble conteo de vulnerabilidades
> detectadas por múltiples instancias de la misma herramienta.
>
> **Total raw:** 1520 hallazgos → **Total único:** 434 → **Eliminados:** 1086 (71.4% de reducción)

### 🔬 Trivy (SCA) — Análisis de Componentes de Software

- **Raw:** 1447 | **Únicos:** 386 | **Removidos:** 1061 (73.3%)
- **Criterio:** `tool + título + endpoint/archivo`

> La misma CVE sobre el mismo paquete puede aparecer una vez por ruta de instalación. Tras deduplicar por CVE + paquete + target queda una sola entrada. Los removidos son instancias duplicadas, no falsos positivos.

### 🌐 OWASP ZAP (DAST) — Análisis Dinámico en Ejecución

- **Raw:** 21 | **Únicos:** 21 | **Removidos:** 0 (0.0%)
- **Criterio:** `tool + título + endpoint/archivo`

> ZAP realiza escaneo baseline pasivo. Cada alerta representa un tipo de misconfiguration único — por eso la deduplicación raramente elimina hallazgos: todas las alertas suelen tener títulos distintos.

### 🎯 Nuclei (Pentesting) — Validación Activa de Templates

- **Raw:** 8 | **Únicos:** 8 | **Removidos:** 0 (0.0%)
- **Criterio:** `tool + título + endpoint/archivo`

> Nuclei puede disparar el mismo template en el mismo endpoint varias veces dentro del mismo run. Tras deduplicar por template + endpoint se conserva solo una entrada por hallazgo único.

### 🔐 Semgrep (SAST) — Análisis Estático de Código

- **Raw:** 44 | **Únicos:** 19 | **Removidos:** 25 (56.8%)
- **Criterio:** `tool + título + endpoint/archivo`

> Semgrep analiza el código fuente del repositorio consumidor. La deduplicación elimina la misma regla disparada en múltiples archivos del mismo módulo, conservando solo la primera ocurrencia por regla + ruta.

---

## 🕵️ Fase de Reconocimiento Activo

> El reconocimiento activo descubre la superficie de ataque real antes del escaneo
> dinámico, enriqueciendo los targets de Nuclei y ZAP.

| Campo | Valor |
|---|---|
| **URL objetivo** | `http://localhost:80` |
| **Host** | `localhost` |
| **Puerto** | `80` |
| **WAF detectado** | ❌ No detectado |
| **Servidor** | `Apache/2.4.25 (Debian)` |
| **Tecnologías** | `Apache HTTP Server:2.4.25`, `Debian`, `PHP` |
| **Targets generados para Nuclei** | 1 URLs |

### Puertos detectados (nmap)

| Puerto | Servicio | Versión | Interesante |
|---|---|---|---|
| `22` | ssh | OpenSSH 10.2p1 Ubuntu 2ubuntu3.8 (Ubuntu | No |
| `80` | http | Apache httpd 2.4.25 ((Debian)) | No |


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

Se identificaron varias vulnerabilidades críticas, incluyendo CVE-2021-26691 y CVE-2021-40438, que son explotables remotamente y tienen un alto impacto potencial. Además, la clasificación SSVC de varios hallazgos como 'Act' se valida con EPSS y KEV, indicando que son relevantes para la seguridad del servicio. La combinación de estas vulnerabilidades puede permitir a un atacante comprometer el sistema y acceder a datos sensibles.

**Análisis de falsos positivos:** Las vulnerabilidades identificadas son críticas y están respaldadas por datos de EPSS y KEV, lo que sugiere que son reales y explotables.

### Categorías OWASP Top 10 Detectadas

- `A06:2021 – Vulnerable and Outdated Components`
- `A03:2021 – Injection`

### Cobertura por Tipo de Herramienta

| Tipo de análisis | Cobertura | Estado |
|---|---|---|
| SAST – Código fuente | buena | ✅ |
| SCA – Dependencias | buena | ✅ |
| DAST – Tiempo de ejecución | parcial | 🟡 |
| Pentesting automatizado | parcial | 🟡 |

**Evaluación general:** La cobertura general es adecuada, pero se deben abordar las vulnerabilidades críticas identificadas.

### ⚠️ Áreas sin cobertura (Blind Spots)

- Falta de pruebas de penetración exhaustivas en el entorno de staging.


### 🏆 Hallazgos Principales Identificados por IA

| Severidad | Hallazgo | CVSS | Remoto | Auth | Exploit | Categoría |
|---|---|---|---|---|---|---|
| 🔴 CRITICAL | CVE-2021-26691 – httpd: mod_session: Heap ove | `9.8` | 🔴 Sí | 🟢 No | ⚠️ Sí | A06:2021 – Vulnerable and Outdated  |
| 🔴 CRITICAL | CVE-2021-40438 – httpd: mod_proxy: SSRF via a | `9.0` | 🔴 Sí | 🟢 No | ⚠️ Sí | A06:2021 – Vulnerable and Outdated  |

---

## 🔗 Análisis de Cadenas de Ataque

> Esta sección identifica combinaciones de vulnerabilidades que, explotadas en secuencia,
> producen un impacto mayor al de cada vulnerabilidad de forma individual.

### 🔴 CHAIN-001 — Explotación de vulnerabilidades críticas en Apache HTTP Server

| Campo | Valor |
|---|---|
| **Severidad combinada** | CRITICAL |
| **Probabilidad** | 🔴 Alta |
| **Vulnerabilidades involucradas** | `TRI-B5B0B6D8`, `TRI-E2222A48` |

**Secuencia del ataque:**

1. Paso 1: El atacante envía una solicitud manipulada que explota CVE-2021-40438 para redirigir el tráfico a un servidor interno.
2. Paso 2: Utilizando la vulnerabilidad CVE-2021-26691, el atacante ejecuta código arbitrario en el servidor Apache.
3. Paso 3: Resultado final: El atacante obtiene acceso a datos sensibles y puede comprometer la infraestructura interna.

**Impacto combinado:** La combinación de estas vulnerabilidades permite un acceso completo al sistema, lo que resulta en una violación de datos y posible daño a la infraestructura.

---

---

## 🛠️ Hoja de Ruta de Remediación

### 🚨 Inmediato (0–7 días) — 2 acciones

**1.** Actualizar apache2 de 2.4.25-3+deb9u5 a 2.4.25-3+deb9u10 → Fix: `2.4.25-3+deb9u10`
   - `trivy` | Esfuerzo: _bajo_ | Fix disponible: ✅

**2.** Actualizar apache2 de 2.4.25-3+deb9u5 a 2.4.25-3+deb9u11 → Fix: `2.4.25-3+deb9u11`
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
| **CISA KEV** | 1,781 entradas consultadas |
| **EPSS** | 386 CVEs consultados vía FIRST.org API |

### Distribución de Acciones SSVC

| Acción | Hallazgos | % | Gate | Significado operativo |
|---|---|---|---|---|
| **Act** | `259` | 59.7% | ❌ FAIL | Explotación activa o automatizable con impacto total |
| **Attend** | `7` | 1.6% | ⚠️ CONDITIONAL | Explotación probable a corto plazo |
| **Track*** | `148` | 34.1% | ⚠️ CONDITIONAL | Monitoreo activo — riesgo controlado |
| **Track** | `20` | 4.6% | ✅ PASS | Sin explotación activa conocida |
| **Total evaluados** | `434` | 100% | ❌ **FAIL** | Decisión = acción máxima |

### Hallazgos que requieren acción inmediata (Act)

| Herramienta | Vulnerabilidad | Explotación | Automatizable | Impacto | Acción |
|---|---|---|---|---|---|
| `semgrep` | Tainted Filename | poc | yes | total | **Act** |
| `semgrep` | Tainted Exec | poc | yes | total | **Act** |
| `semgrep` | Tainted Sql String | poc | yes | total | **Act** |
| `semgrep` | Tainted Sql String | poc | yes | total | **Act** |
| `semgrep` | Tainted Sql String | poc | yes | total | **Act** |
| `semgrep` | Tainted Exec | poc | yes | total | **Act** |
| `semgrep` | Tainted Exec | poc | yes | total | **Act** |
| `semgrep` | Tainted Exec | poc | yes | total | **Act** |


### 📊 Métricas Formales — Dimensión Exploitation (F1 Score)

> Calculadas sobre CVEs con CISA KEV o EPSS disponible como *ground truth*.
> Metodología: Al Haddad et al. (2025) — arXiv 2510.18508.

| Métrica | Valor | Descripción |
|---|---|---|
| **Precisión** | `1.0000` | TP / (TP + FP) |
| **Recall** | `1.0000` | TP / (TP + FN) |
| **F1 Score** | `1.0000` | Media armónica precisión/recall |
| **Accuracy** | `1.0000` | (TP + TN) / total |
| CVEs evaluados | `386` | Solo CVEs con EPSS/KEV disponible |
| Verdaderos positivos | `42` | Clasificados active, ground truth active |
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
| **Tokens de prompt** | `7,357` |
| **Tokens de completion** | `1,497` |
| **Contexto SSVC activo** | ✅ Sí — el LLM recibió clasificaciones SSVC por hallazgo |
| **CISA KEV consultado** | 1,781 entradas (fuente: cisa.gov) |
| **EPSS consultado** | 386 CVEs (fuente: FIRST.org API) |
| **Hallazgos clasificados SSVC** | 434 |
| **Distribución SSVC pre-LLM** | Act=259, Attend=7, Track*=148, Track=20 |
| **F1 Exploitation** | `1.0000` (P=1.0000, R=1.0000, n=386 CVEs) |

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
| `TRI-B5B0B6D8` | CVE-2021-26691 – httpd: mod_session: Hea | `Act` | ✅ **confirmed** | `0.6807` | No | La vulnerabilidad tiene un EPSS alto, lo que indica que es explotable en el contexto actua... |
| `TRI-E2222A48` | CVE-2021-40438 – httpd: mod_proxy: SSRF  | `Act` | ✅ **confirmed** | `1.0000` | ✅ Sí | La vulnerabilidad está en KEV y tiene un EPSS de 1.0, confirmando su explotación activa y ... |


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
- Hallazgos CRÍTICOS: 65 (umbral: 0)
- Hallazgos ALTOS: 180 (umbral: 5)
- Hallazgos MEDIOS: 166 (umbral: 20)

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
Análisis estático de código fuente: se ejecutó y **detectó 19 hallazgo(s)** (9 HIGH, 10 MEDIUM). Los hallazgos están documentados en la sección de detalle.

**🟡 ASC-SCA-001** (Trivy) — Control obligatorio  
Análisis de componentes y dependencias (CVEs): se ejecutó y **detectó 386 hallazgo(s)** (65 CRITICAL, 169 HIGH, 152 MEDIUM). Los hallazgos están documentados en la sección de detalle.

**⚠️ zap** (Herramienta) — Control obligatorio  
Control de seguridad: **no se ejecutó** en esta corrida. Posible causa: herramienta no disponible, aplicación sin respuesta HTTP, o fallo en el job correspondiente.

**🟡 ASC-PENTEST-001** (Nuclei v3) — Control obligatorio  
Validación activa con templates de pentest: se ejecutó y **detectó 8 hallazgo(s)** (1 HIGH, 1 MEDIUM, 6 LOW). Los hallazgos están documentados en la sección de detalle.

**🟡 ASC-DAST-001** (OWASP ZAP) — Control opcional  
Análisis dinámico en tiempo de ejecución: se ejecutó y **detectó 21 hallazgo(s)** (1 HIGH, 3 MEDIUM, 11 LOW, 6 INFO). Los hallazgos están documentados en la sección de detalle.


### Resumen de cobertura ANF

| ASC | Herramienta | Obligatoriedad | Estado | Hallazgos | Severidades |
|---|---|---|---|---|---|
| `ASC-SAST-001` | Semgrep OSS | ✅ Obligatorio | ✅ Ejecutado | 19 | 🟠H:9 / 🟡M:10 |
| `ASC-SCA-001` | Trivy | ✅ Obligatorio | ✅ Ejecutado | 386 | 🔴C:65 / 🟠H:169 / 🟡M:152 |
| `zap` | Herramienta | ✅ Obligatorio | ⚠️ No ejecutado | 0 | — |
| `ASC-PENTEST-001` | Nuclei v3 | ✅ Obligatorio | ✅ Ejecutado | 8 | 🟠H:1 / 🟡M:1 / 🟢L:6 |
| `ASC-DAST-001` | OWASP ZAP | ⚪ Opcional | ✅ Ejecutado | 21 | 🟠H:1 / 🟡M:3 / 🟢L:11 / ⚪I:6 |


> ⚠️ **Brechas de cobertura:** los siguientes controles obligatorios no se ejecutaron en esta corrida: `zap`. Revisar la configuración del pipeline antes de promover a producción.


> **ANF generado por:** `detector.py` según `criticality=high` y `language=generic` — ✅ generado automáticamente  
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
> **Raw:** 1447 | **Únicos:** 386 | **Deduplicados:** 1061 (73.3%)

**Distribución:** 🔴 CRITICAL: **65** | 🟠 HIGH: **169** | 🟡 MEDIUM: **152**

#### 🔴🟠 Críticos y Altos (234)

#### 🔴 [CRITICAL] CVE-2019-10082 – httpd: read-after-free in h2 connection shutdown

| Campo | Valor |
|---|---|
| **ID** | `TRI-D6433241` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `9.1` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** In Apache HTTP Server 2.4.18-2.4.39, using fuzzed network input, the http/2 session handling could be made to read memory after being freed, during connection shutdown.

**Evidencia:** `Paquete: apache2 v2.4.25-3+deb9u5 | Fix: 2.4.25-3+deb9u8`

**✅ Remediación:** Actualizar apache2 de 2.4.25-3+deb9u5 a 2.4.25-3+deb9u8

---

#### 🔴 [CRITICAL] CVE-2021-26691 – httpd: mod_session: Heap overflow via a crafted SessionHeader value

| Campo | Valor |
|---|---|
| **ID** | `TRI-B5B0B6D8` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `9.8` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** In Apache HTTP Server versions 2.4.0 to 2.4.46 a specially crafted SessionHeader sent by an origin server could cause a heap overflow

**Evidencia:** `Paquete: apache2 v2.4.25-3+deb9u5 | Fix: 2.4.25-3+deb9u10`

**✅ Remediación:** Actualizar apache2 de 2.4.25-3+deb9u5 a 2.4.25-3+deb9u10

---

#### 🔴 [CRITICAL] CVE-2021-39275 – httpd: Out-of-bounds write in ap_escape_quotes() via malicious input

| Campo | Valor |
|---|---|
| **ID** | `TRI-0D9BCD03` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `9.8` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** ap_escape_quotes() may write beyond the end of a buffer when given malicious input. No included modules pass untrusted data to these functions, but third-party / external modules may. This issue affects Apache HTTP Server 2.4.48 and earlier.

**Evidencia:** `Paquete: apache2 v2.4.25-3+deb9u5 | Fix: 2.4.25-3+deb9u11`

**✅ Remediación:** Actualizar apache2 de 2.4.25-3+deb9u5 a 2.4.25-3+deb9u11

---

#### 🔴 [CRITICAL] CVE-2021-40438 – httpd: mod_proxy: SSRF via a crafted request uri-path containing "unix:"

| Campo | Valor |
|---|---|
| **ID** | `TRI-E2222A48` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `9.0` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** A crafted request uri-path can cause mod_proxy to forward the request to an origin server choosen by the remote user. This issue affects Apache HTTP Server 2.4.48 and earlier.

**Evidencia:** `Paquete: apache2 v2.4.25-3+deb9u5 | Fix: 2.4.25-3+deb9u11`

**✅ Remediación:** Actualizar apache2 de 2.4.25-3+deb9u5 a 2.4.25-3+deb9u11

---

#### 🔴 [CRITICAL] CVE-2021-44790 – httpd: mod_lua: Possible buffer overflow when parsing multipart content

| Campo | Valor |
|---|---|
| **ID** | `TRI-DFC76F3F` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `9.8` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** A carefully crafted request body can cause a buffer overflow in the mod_lua multipart parser (r:parsebody() called from Lua scripts). The Apache httpd team is not aware of an exploit for the vulnerabilty though it might be possible to craft one. This issue affects Apache HTTP Server 2.4.51 and earlier.

**Evidencia:** `Paquete: apache2 v2.4.25-3+deb9u5 | Fix: 2.4.25-3+deb9u12`

**✅ Remediación:** Actualizar apache2 de 2.4.25-3+deb9u5 a 2.4.25-3+deb9u12

---

#### 🔴 [CRITICAL] CVE-2022-22720 – httpd: Errors encountered during the discarding of request body lead to HTTP request smuggling

| Campo | Valor |
|---|---|
| **ID** | `TRI-05FB8763` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `9.8` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** Apache HTTP Server 2.4.52 and earlier fails to close inbound connection when errors are encountered discarding the request body, exposing the server to HTTP Request Smuggling

**Evidencia:** `Paquete: apache2 v2.4.25-3+deb9u5 | Fix: 2.4.25-3+deb9u13`

**✅ Remediación:** Actualizar apache2 de 2.4.25-3+deb9u5 a 2.4.25-3+deb9u13

---

#### 🔴 [CRITICAL] CVE-2022-22721 – httpd: core: Possible buffer overflow with very large or unlimited LimitXMLRequestBody

| Campo | Valor |
|---|---|
| **ID** | `TRI-90220C94` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `9.1` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** If LimitXMLRequestBody is set to allow request bodies larger than 350MB (defaults to 1M) on 32 bit systems an integer overflow happens which later causes out of bounds writes. This issue affects Apache HTTP Server 2.4.52 and earlier.

**Evidencia:** `Paquete: apache2 v2.4.25-3+deb9u5 | Fix: 2.4.25-3+deb9u13`

**✅ Remediación:** Actualizar apache2 de 2.4.25-3+deb9u5 a 2.4.25-3+deb9u13

---

#### 🔴 [CRITICAL] CVE-2022-23943 – httpd: mod_sed: Read/write beyond bounds

| Campo | Valor |
|---|---|
| **ID** | `TRI-A1C5FD28` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `9.8` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** Out-of-bounds Write vulnerability in mod_sed of Apache HTTP Server allows an attacker to overwrite heap memory with possibly attacker provided data. This issue affects Apache HTTP Server 2.4 version 2.4.52 and prior versions.

**Evidencia:** `Paquete: apache2 v2.4.25-3+deb9u5 | Fix: 2.4.25-3+deb9u13`

**✅ Remediación:** Actualizar apache2 de 2.4.25-3+deb9u5 a 2.4.25-3+deb9u13

---

#### 🔴 [CRITICAL] CVE-2019-12900 – bzip2: bzip2: Data integrity error when decompressing (with data integrity tests fail).

| Campo | Valor |
|---|---|
| **ID** | `TRI-5461D904` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `9.8` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** BZ2_decompress in decompress.c in bzip2 through 1.0.6 has an out-of-bounds write when there are many selectors.

**Evidencia:** `Paquete: bzip2 v1.0.6-8.1 | Fix: Not available`

**✅ Remediación:** No hay fix disponible para bzip2 1.0.6-8.1 — considerar alternativa

---

#### 🔴 [CRITICAL] CVE-2022-1664 – Dpkg::Source::Archive in dpkg, the Debian package management system, b ...

| Campo | Valor |
|---|---|
| **ID** | `TRI-071C1DD2` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `9.8` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** Dpkg::Source::Archive in dpkg, the Debian package management system, before version 1.21.8, 1.20.10, 1.19.8, 1.18.26 is prone to a directory traversal vulnerability. When extracting untrusted source packages in v2 and v3 source package formats that include a debian.tar, the in-place extraction can lead to directory traversal situations on specially crafted orig.tar and debian.tar tarballs.

**Evidencia:** `Paquete: dpkg v1.18.25 | Fix: 1.18.26`

**✅ Remediación:** Actualizar dpkg de 1.18.25 a 1.18.26

---

#### 🔴 [CRITICAL] CVE-2020-10188 – telnet-server: no bounds checks in nextitem() function allows to remotely execute arbitrary code

| Campo | Valor |
|---|---|
| **ID** | `TRI-03ECBD0B` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `9.8` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** utility.c in telnetd in netkit telnet through 0.17 allows remote attackers to execute arbitrary code via short writes or urgent data, because of a buffer overflow involving the netclear and nextitem functions.

**Evidencia:** `Paquete: inetutils-ping v2:1.9.4-2+b1 | Fix: 2:1.9.4-2+deb9u1`

**✅ Remediación:** Actualizar inetutils-ping de 2:1.9.4-2+b1 a 2:1.9.4-2+deb9u1

---

#### 🔴 [CRITICAL] CVE-2017-8923 – php: Overflowing the length of string causes crash

| Campo | Valor |
|---|---|
| **ID** | `TRI-9AAE27DD` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `9.8` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** The zend_string_extend function in Zend/zend_string.h in PHP through 7.1.5 does not prevent changes to string objects that result in a negative length, which allows remote attackers to cause a denial of service (application crash) or possibly have unspecified other impact by leveraging a script's use of .= with a long string.

**Evidencia:** `Paquete: libapache2-mod-php7.0 v7.0.30-0+deb9u1 | Fix: Not available`

**✅ Remediación:** No hay fix disponible para libapache2-mod-php7.0 7.0.30-0+deb9u1 — considerar alternativa

---

#### 🔴 [CRITICAL] CVE-2019-11034 – php: Heap buffer overflow in function exif_process_IFD_TAG()

| Campo | Valor |
|---|---|
| **ID** | `TRI-828446FD` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `9.1` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** When processing certain files, PHP EXIF extension in versions 7.1.x below 7.1.28, 7.2.x below 7.2.17 and 7.3.x below 7.3.4 can be caused to read past allocated buffer in exif_process_IFD_TAG function. This may lead to information disclosure or crash.

**Evidencia:** `Paquete: libapache2-mod-php7.0 v7.0.30-0+deb9u1 | Fix: 7.0.33-0+deb9u5`

**✅ Remediación:** Actualizar libapache2-mod-php7.0 de 7.0.30-0+deb9u1 a 7.0.33-0+deb9u5

---

#### 🔴 [CRITICAL] CVE-2019-11035 – php: Heap buffer overflow in function exif_iif_add_value()

| Campo | Valor |
|---|---|
| **ID** | `TRI-9D47A8B0` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `9.1` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** When processing certain files, PHP EXIF extension in versions 7.1.x below 7.1.28, 7.2.x below 7.2.17 and 7.3.x below 7.3.4 can be caused to read past allocated buffer in exif_iif_add_value function. This may lead to information disclosure or crash.

**Evidencia:** `Paquete: libapache2-mod-php7.0 v7.0.30-0+deb9u1 | Fix: 7.0.33-0+deb9u5`

**✅ Remediación:** Actualizar libapache2-mod-php7.0 de 7.0.30-0+deb9u1 a 7.0.33-0+deb9u5

---

#### 🔴 [CRITICAL] CVE-2019-11036 – php: Buffer over-read in exif_process_IFD_TAG() leading to information disclosure

| Campo | Valor |
|---|---|
| **ID** | `TRI-983BD224` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `9.1` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** When processing certain files, PHP EXIF extension in versions 7.1.x below 7.1.29, 7.2.x below 7.2.18 and 7.3.x below 7.3.5 can be caused to read past allocated buffer in exif_process_IFD_TAG function. This may lead to information disclosure or crash.

**Evidencia:** `Paquete: libapache2-mod-php7.0 v7.0.30-0+deb9u1 | Fix: 7.0.33-0+deb9u5`

**✅ Remediación:** Actualizar libapache2-mod-php7.0 de 7.0.30-0+deb9u1 a 7.0.33-0+deb9u5

---

#### 🔴 [CRITICAL] CVE-2019-11039 – php: Out-of-bounds read due to integer overflow in iconv_mime_decode_headers()

| Campo | Valor |
|---|---|
| **ID** | `TRI-10A96A2A` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `9.1` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** Function iconv_mime_decode_headers() in PHP versions 7.1.x below 7.1.30, 7.2.x below 7.2.19 and 7.3.x below 7.3.6 may perform out-of-buffer read due to integer overflow when parsing MIME headers. This may lead to information disclosure or crash.

**Evidencia:** `Paquete: libapache2-mod-php7.0 v7.0.30-0+deb9u1 | Fix: 7.0.33-0+deb9u5`

**✅ Remediación:** Actualizar libapache2-mod-php7.0 de 7.0.30-0+deb9u1 a 7.0.33-0+deb9u5

---

#### 🔴 [CRITICAL] CVE-2019-11040 – php: Buffer over-read in exif_read_data()

| Campo | Valor |
|---|---|
| **ID** | `TRI-F00007A9` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `9.1` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** When PHP EXIF extension is parsing EXIF information from an image, e.g. via exif_read_data() function, in PHP versions 7.1.x below 7.1.30, 7.2.x below 7.2.19 and 7.3.x below 7.3.6 it is possible to supply it with data what will cause it to read past the allocated buffer. This may lead to information disclosure or crash.

**Evidencia:** `Paquete: libapache2-mod-php7.0 v7.0.30-0+deb9u1 | Fix: 7.0.33-0+deb9u5`

**✅ Remediación:** Actualizar libapache2-mod-php7.0 de 7.0.30-0+deb9u1 a 7.0.33-0+deb9u5

---

#### 🔴 [CRITICAL] CVE-2019-11043 – php: underflow in env_path_info in fpm_main.c

| Campo | Valor |
|---|---|
| **ID** | `TRI-FC9473D6` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `9.8` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** In PHP versions 7.1.x below 7.1.33, 7.2.x below 7.2.24 and 7.3.x below 7.3.11 in certain configurations of FPM setup it is possible to cause FPM module to write past allocated buffers into the space reserved for FCGI protocol data, thus opening the possibility of remote code execution.

**Evidencia:** `Paquete: libapache2-mod-php7.0 v7.0.30-0+deb9u1 | Fix: 7.0.33-0+deb9u6`

**✅ Remediación:** Actualizar libapache2-mod-php7.0 de 7.0.30-0+deb9u1 a 7.0.33-0+deb9u6

---

#### 🔴 [CRITICAL] CVE-2019-13224 – oniguruma: Use-after-free in onig_new_deluxe() in regext.c

| Campo | Valor |
|---|---|
| **ID** | `TRI-504356DD` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `9.8` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** A use-after-free in onig_new_deluxe() in regext.c in Oniguruma 6.9.2 allows attackers to potentially cause information disclosure, denial of service, or possibly code execution by providing a crafted regular expression. The attacker provides a pair of a regex pattern and a string, with a multi-byte encoding that gets handled by onig_new_deluxe(). Oniguruma issues often affect Ruby, as well as comm

**Evidencia:** `Paquete: libapache2-mod-php7.0 v7.0.30-0+deb9u1 | Fix: 7.0.33-0+deb9u5`

**✅ Remediación:** Actualizar libapache2-mod-php7.0 de 7.0.30-0+deb9u1 a 7.0.33-0+deb9u5

---

#### 🔴 [CRITICAL] CVE-2019-9020 – php: Invalid memory access in function xmlrpc_decode()

| Campo | Valor |
|---|---|
| **ID** | `TRI-4C6ADBCB` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `9.8` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** An issue was discovered in PHP before 5.6.40, 7.x before 7.1.26, 7.2.x before 7.2.14, and 7.3.x before 7.3.1. Invalid input to the function xmlrpc_decode() can lead to an invalid memory access (heap out of bounds read or read after free). This is related to xml_elem_parse_buf in ext/xmlrpc/libxmlrpc/xml_element.c.

**Evidencia:** `Paquete: libapache2-mod-php7.0 v7.0.30-0+deb9u1 | Fix: 7.0.33-0+deb9u2`

**✅ Remediación:** Actualizar libapache2-mod-php7.0 de 7.0.30-0+deb9u1 a 7.0.33-0+deb9u2

---

#### 🔴 [CRITICAL] CVE-2019-9021 – php: Heap-based buffer over-read in PHAR reading functions

| Campo | Valor |
|---|---|
| **ID** | `TRI-47292D98` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `9.8` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** An issue was discovered in PHP before 5.6.40, 7.x before 7.1.26, 7.2.x before 7.2.14, and 7.3.x before 7.3.1. A heap-based buffer over-read in PHAR reading functions in the PHAR extension may allow an attacker to read allocated or unallocated memory past the actual data when trying to parse the file name, a different vulnerability than CVE-2018-20783. This is related to phar_detect_phar_fname_ext 

**Evidencia:** `Paquete: libapache2-mod-php7.0 v7.0.30-0+deb9u1 | Fix: 7.0.33-0+deb9u2`

**✅ Remediación:** Actualizar libapache2-mod-php7.0 de 7.0.30-0+deb9u1 a 7.0.33-0+deb9u2

---

#### 🔴 [CRITICAL] CVE-2019-9023 – php: Heap-based buffer over-read in mbstring regular expression functions

| Campo | Valor |
|---|---|
| **ID** | `TRI-80C6CDF8` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `9.8` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** An issue was discovered in PHP before 5.6.40, 7.x before 7.1.26, 7.2.x before 7.2.14, and 7.3.x before 7.3.1. A number of heap-based buffer over-read instances are present in mbstring regular expression functions when supplied with invalid multibyte data. These occur in ext/mbstring/oniguruma/regcomp.c, ext/mbstring/oniguruma/regexec.c, ext/mbstring/oniguruma/regparse.c, ext/mbstring/oniguruma/enc

**Evidencia:** `Paquete: libapache2-mod-php7.0 v7.0.30-0+deb9u1 | Fix: 7.0.33-0+deb9u2`

**✅ Remediación:** Actualizar libapache2-mod-php7.0 de 7.0.30-0+deb9u1 a 7.0.33-0+deb9u2

---

#### 🔴 [CRITICAL] CVE-2019-9641 – php: Uninitialized read in exif_process_IFD_in_TIFF

| Campo | Valor |
|---|---|
| **ID** | `TRI-FDE269FC` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `9.8` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** An issue was discovered in the EXIF component in PHP before 7.1.27, 7.2.x before 7.2.16, and 7.3.x before 7.3.3. There is an uninitialized read in exif_process_IFD_in_TIFF.

**Evidencia:** `Paquete: libapache2-mod-php7.0 v7.0.30-0+deb9u1 | Fix: 7.0.33-0+deb9u3`

**✅ Remediación:** Actualizar libapache2-mod-php7.0 de 7.0.30-0+deb9u1 a 7.0.33-0+deb9u3

---

#### 🔴 [CRITICAL] CVE-2020-7059 – php: Out of bounds read in php_strip_tags_ex

| Campo | Valor |
|---|---|
| **ID** | `TRI-CA500464` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `9.1` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** When using fgetss() function to read data with stripping tags, in PHP versions 7.2.x below 7.2.27, 7.3.x below 7.3.14 and 7.4.x below 7.4.2 it is possible to supply data that will cause this function to read past the allocated buffer. This may lead to information disclosure or crash.

**Evidencia:** `Paquete: libapache2-mod-php7.0 v7.0.30-0+deb9u1 | Fix: 7.0.33-0+deb9u7`

**✅ Remediación:** Actualizar libapache2-mod-php7.0 de 7.0.30-0+deb9u1 a 7.0.33-0+deb9u7

---

#### 🔴 [CRITICAL] CVE-2020-7060 – php: Global buffer-overflow in mbfl_filt_conv_big5_wchar function

| Campo | Valor |
|---|---|
| **ID** | `TRI-73BE63E4` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `9.1` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** When using certain mbstring functions to convert multibyte encodings, in PHP versions 7.2.x below 7.2.27, 7.3.x below 7.3.14 and 7.4.x below 7.4.2 it is possible to supply data that will cause function mbfl_filt_conv_big5_wchar to read past the allocated buffer. This may lead to information disclosure or crash.

**Evidencia:** `Paquete: libapache2-mod-php7.0 v7.0.30-0+deb9u1 | Fix: 7.0.33-0+deb9u7`

**✅ Remediación:** Actualizar libapache2-mod-php7.0 de 7.0.30-0+deb9u1 a 7.0.33-0+deb9u7

---

#### 🔴 [CRITICAL] CVE-2019-20367 – nlist.c in libbsd before 0.10.0 has an out-of-bounds read during a com ...

| Campo | Valor |
|---|---|
| **ID** | `TRI-C1419A9B` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `9.1` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** nlist.c in libbsd before 0.10.0 has an out-of-bounds read during a comparison for a symbol name from the string table (strtab).

**Evidencia:** `Paquete: libbsd0 v0.8.3-1 | Fix: 0.8.3-1+deb9u1`

**✅ Remediación:** Actualizar libbsd0 de 0.8.3-1 a 0.8.3-1+deb9u1

---

#### 🔴 [CRITICAL] CVE-2017-18269 – glibc: memory corruption in memcpy-sse2-unaligned.S

| Campo | Valor |
|---|---|
| **ID** | `TRI-25CD01E4` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `9.8` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** An SSE2-optimized memmove implementation for i386 in sysdeps/i386/i686/multiarch/memcpy-sse2-unaligned.S in the GNU C Library (aka glibc or libc6) 2.21 through 2.27 does not correctly perform the overlapping memory check if the source memory range spans the middle of the address space, resulting in corrupt data being produced by the copy operation. This may disclose information to context-dependen

**Evidencia:** `Paquete: libc-bin v2.24-11+deb9u3 | Fix: 2.24-11+deb9u4`

**✅ Remediación:** Actualizar libc-bin de 2.24-11+deb9u3 a 2.24-11+deb9u4

---

#### 🔴 [CRITICAL] CVE-2019-8457 – sqlite: heap out-of-bound read in function rtreenode()

| Campo | Valor |
|---|---|
| **ID** | `TRI-ACDB87FA` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `9.8` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** SQLite3 from 3.6.0 to and including 3.27.2 is vulnerable to heap out-of-bound read in the rtreenode() function when handling invalid rtree tables.

**Evidencia:** `Paquete: libdb5.3 v5.3.28-12+deb9u1 | Fix: Not available`

**✅ Remediación:** No hay fix disponible para libdb5.3 5.3.28-12+deb9u1 — considerar alternativa

---

#### 🔴 [CRITICAL] CVE-2017-10788 – perl-DBD-MySQL: Use-after-free when calling mysql_stmt_error() after mysql_stmt_close()

| Campo | Valor |
|---|---|
| **ID** | `TRI-EC18A136` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `9.8` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** The DBD::mysql module through 4.043 for Perl allows remote attackers to cause a denial of service (use-after-free and application crash) or possibly have unspecified other impact by triggering (1) certain error responses from a MySQL server or (2) a loss of a network connection to a MySQL server. The use-after-free defect was introduced by relying on incorrect Oracle mysql_stmt_close documentation

**Evidencia:** `Paquete: libdbd-mysql-perl v4.041-2 | Fix: Not available`

**✅ Remediación:** No hay fix disponible para libdbd-mysql-perl 4.041-2 — considerar alternativa

---

#### 🔴 [CRITICAL] CVE-2018-16402 – elfutils: Double-free due to double decompression of sections in crafted ELF causes crash

| Campo | Valor |
|---|---|
| **ID** | `TRI-097BD0CD` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `9.8` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** libelf/elf_end.c in elfutils 0.173 allows remote attackers to cause a denial of service (double free and application crash) or possibly have unspecified other impact because it tries to decompress twice.

**Evidencia:** `Paquete: libelf1 v0.168-1 | Fix: 0.168-1+deb9u1`

**✅ Remediación:** Actualizar libelf1 de 0.168-1 a 0.168-1+deb9u1

---

#### 🔴 [CRITICAL] CVE-2022-22822 – expat: Integer overflow in addBinding in xmlparse.c

| Campo | Valor |
|---|---|
| **ID** | `TRI-880374C5` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `9.8` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** addBinding in xmlparse.c in Expat (aka libexpat) before 2.4.3 has an integer overflow.

**Evidencia:** `Paquete: libexpat1 v2.2.0-2+deb9u1 | Fix: 2.2.0-2+deb9u4`

**✅ Remediación:** Actualizar libexpat1 de 2.2.0-2+deb9u1 a 2.2.0-2+deb9u4

---

#### 🔴 [CRITICAL] CVE-2022-22823 – expat: Expat: Denial of Service vulnerability in XML parsing

| Campo | Valor |
|---|---|
| **ID** | `TRI-3CB1E3F1` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `9.8` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** build_model in xmlparse.c in Expat (aka libexpat) before 2.4.3 has an integer overflow.

**Evidencia:** `Paquete: libexpat1 v2.2.0-2+deb9u1 | Fix: 2.2.0-2+deb9u4`

**✅ Remediación:** Actualizar libexpat1 de 2.2.0-2+deb9u1 a 2.2.0-2+deb9u4

---

#### 🔴 [CRITICAL] CVE-2022-22824 – expat: Expat: Denial of service and memory issues due to integer overflow

| Campo | Valor |
|---|---|
| **ID** | `TRI-2928D94C` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `9.8` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** defineAttribute in xmlparse.c in Expat (aka libexpat) before 2.4.3 has an integer overflow.

**Evidencia:** `Paquete: libexpat1 v2.2.0-2+deb9u1 | Fix: 2.2.0-2+deb9u4`

**✅ Remediación:** Actualizar libexpat1 de 2.2.0-2+deb9u1 a 2.2.0-2+deb9u4

---

#### 🔴 [CRITICAL] CVE-2022-23852 – expat: Integer overflow in function XML_GetBuffer

| Campo | Valor |
|---|---|
| **ID** | `TRI-71EB220E` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `9.8` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** Expat (aka libexpat) before 2.4.4 has a signed integer overflow in XML_GetBuffer, for configurations with a nonzero XML_CONTEXT_BYTES.

**Evidencia:** `Paquete: libexpat1 v2.2.0-2+deb9u1 | Fix: 2.2.0-2+deb9u5`

**✅ Remediación:** Actualizar libexpat1 de 2.2.0-2+deb9u1 a 2.2.0-2+deb9u5

---

#### 🔴 [CRITICAL] CVE-2022-25235 – expat: Malformed 2- and 3-byte UTF-8 sequences can lead to arbitrary code execution

| Campo | Valor |
|---|---|
| **ID** | `TRI-178FEA72` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `9.8` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** xmltok_impl.c in Expat (aka libexpat) before 2.4.5 lacks certain validation of encoding, such as checks for whether a UTF-8 character is valid in a certain context.

**Evidencia:** `Paquete: libexpat1 v2.2.0-2+deb9u1 | Fix: 2.2.0-2+deb9u5`

**✅ Remediación:** Actualizar libexpat1 de 2.2.0-2+deb9u1 a 2.2.0-2+deb9u5

---

#### 🔴 [CRITICAL] CVE-2022-25236 – expat: Namespace-separator characters in "xmlns[:prefix]" attribute values can lead to arbitrary code execution

| Campo | Valor |
|---|---|
| **ID** | `TRI-77F90852` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `9.8` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** xmlparse.c in Expat (aka libexpat) before 2.4.5 allows attackers to insert namespace-separator characters into namespace URIs.

**Evidencia:** `Paquete: libexpat1 v2.2.0-2+deb9u1 | Fix: 2.2.0-2+deb9u5`

**✅ Remediación:** Actualizar libexpat1 de 2.2.0-2+deb9u1 a 2.2.0-2+deb9u5

---

#### 🔴 [CRITICAL] CVE-2022-25315 – expat: Integer overflow in storeRawNames()

| Campo | Valor |
|---|---|
| **ID** | `TRI-D1923674` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `9.8` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** In Expat (aka libexpat) before 2.4.5, there is an integer overflow in storeRawNames.

**Evidencia:** `Paquete: libexpat1 v2.2.0-2+deb9u1 | Fix: 2.2.0-2+deb9u5`

**✅ Remediación:** Actualizar libexpat1 de 2.2.0-2+deb9u1 a 2.2.0-2+deb9u5

---

#### 🔴 [CRITICAL] CVE-2020-15999 – freetype: Heap-based buffer overflow due to integer truncation in Load_SBit_Png

| Campo | Valor |
|---|---|
| **ID** | `TRI-F1143662` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `9.6` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** Heap buffer overflow in Freetype in Google Chrome prior to 86.0.4240.111 allowed a remote attacker to potentially exploit heap corruption via a crafted HTML page.

**Evidencia:** `Paquete: libfreetype6 v2.6.3-3.2 | Fix: 2.6.3-3.2+deb9u2`

**✅ Remediación:** Actualizar libfreetype6 de 2.6.3-3.2 a 2.6.3-3.2+deb9u2

---

#### 🔴 [CRITICAL] CVE-2022-27404 – FreeType: Buffer overflow in sfnt_init_face

| Campo | Valor |
|---|---|
| **ID** | `TRI-72CB95FC` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `9.8` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** FreeType commit 1e2eb65048f75c64b68708efed6ce904c31f3b2f was discovered to contain a heap buffer overflow via the function sfnt_init_face.

**Evidencia:** `Paquete: libfreetype6 v2.6.3-3.2 | Fix: Not available`

**✅ Remediación:** No hay fix disponible para libfreetype6 2.6.3-3.2 — considerar alternativa

---

#### 🔴 [CRITICAL] CVE-2019-6978 – gd: Double free in the gdImage*Ptr in gd_gif_out.c, gd_jpeg.c, and gd_wbmp.c

| Campo | Valor |
|---|---|
| **ID** | `TRI-5286D57C` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `9.8` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** The GD Graphics Library (aka LibGD) 2.2.5 has a double free in the gdImage*Ptr() functions in gd_gif_out.c, gd_jpeg.c, and gd_wbmp.c. NOTE: PHP is unaffected.

**Evidencia:** `Paquete: libgd3 v2.2.4-2+deb9u2 | Fix: 2.2.4-2+deb9u4`

**✅ Remediación:** Actualizar libgd3 de 2.2.4-2+deb9u2 a 2.2.4-2+deb9u4

---

#### 🔴 [CRITICAL] CVE-2017-14062 – libidn2: Integer overflow in puny_decode.c/decode_digit

| Campo | Valor |
|---|---|
| **ID** | `TRI-BEA13C5D` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `9.8` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** Integer overflow in the decode_digit function in puny_decode.c in Libidn2 before 2.0.4 allows remote attackers to cause a denial of service or possibly have unspecified other impact.

**Evidencia:** `Paquete: libidn11 v1.33-1 | Fix: 1.33-1+deb9u1`

**✅ Remediación:** Actualizar libidn11 de 1.33-1 a 1.33-1+deb9u1

---

#### 🔴 [CRITICAL] CVE-2022-29155 – openldap: OpenLDAP SQL injection

| Campo | Valor |
|---|---|
| **ID** | `TRI-AA76E5D3` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `9.8` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** In OpenLDAP 2.x before 2.5.12 and 2.6.x before 2.6.2, a SQL injection vulnerability exists in the experimental back-sql backend to slapd, via a SQL statement within an LDAP query. This can occur during an LDAP search operation when the search filter is processed, due to a lack of proper escaping.

**Evidencia:** `Paquete: libldap-2.4-2 v2.4.44+dfsg-5+deb9u2 | Fix: 2.4.44+dfsg-5+deb9u9`

**✅ Remediación:** Actualizar libldap-2.4-2 de 2.4.44+dfsg-5+deb9u2 a 2.4.44+dfsg-5+deb9u9

---

#### 🔴 [CRITICAL] CVE-2021-3520 – lz4: memory corruption due to an integer overflow bug caused by memmove argument

| Campo | Valor |
|---|---|
| **ID** | `TRI-C6D0BCD3` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `9.8` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** There's a flaw in lz4. An attacker who submits a crafted file to an application linked with lz4 may be able to trigger an integer overflow, leading to calling of memmove() on a negative size argument, causing an out-of-bounds write and/or a crash. The greatest impact of this flaw is to availability, with some potential impact to confidentiality and integrity as well.

**Evidencia:** `Paquete: liblz4-1 v0.0~r131-2+b1 | Fix: 0.0~r131-2+deb9u1`

**✅ Remediación:** Actualizar liblz4-1 de 0.0~r131-2+b1 a 0.0~r131-2+deb9u1

---

#### 🔴 [CRITICAL] CVE-2020-15180 – mariadb: Insufficient SST method name check leading to code injection in mysql-wsrep

| Campo | Valor |
|---|---|
| **ID** | `TRI-7C6DEAAE` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `9.0` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** A flaw was found in the mysql-wsrep component of mariadb. Lack of input sanitization in `wsrep_sst_method` allows for command injection that can be exploited by a remote attacker to execute arbitrary commands on galera cluster nodes. This threatens the system's confidentiality, integrity, and availability. This flaw affects mariadb versions before 10.1.47, before 10.2.34, before 10.3.25, before 10

**Evidencia:** `Paquete: libmariadbclient18 v10.1.26-0+deb9u1 | Fix: 10.1.47-0+deb9u1`

**✅ Remediación:** Actualizar libmariadbclient18 de 10.1.26-0+deb9u1 a 10.1.47-0+deb9u1

---

#### 🔴 [CRITICAL] CVE-2018-18311 – perl: Integer overflow leading to buffer overflow in Perl_my_setenv()

| Campo | Valor |
|---|---|
| **ID** | `TRI-8B2DC114` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `9.8` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** Perl before 5.26.3 and 5.28.x before 5.28.1 has a buffer overflow via a crafted regular expression that triggers invalid write operations.

**Evidencia:** `Paquete: libperl5.24 v5.24.1-3+deb9u4 | Fix: 5.24.1-3+deb9u5`

**✅ Remediación:** Actualizar libperl5.24 de 5.24.1-3+deb9u4 a 5.24.1-3+deb9u5

---

#### 🔴 [CRITICAL] CVE-2018-18312 – perl: Heap-based buffer overflow in S_handle_regex_sets()

| Campo | Valor |
|---|---|
| **ID** | `TRI-19F44EE2` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `9.8` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** Perl before 5.26.3 and 5.28.0 before 5.28.1 has a buffer overflow via a crafted regular expression that triggers invalid write operations.

**Evidencia:** `Paquete: libperl5.24 v5.24.1-3+deb9u4 | Fix: 5.24.1-3+deb9u5`

**✅ Remediación:** Actualizar libperl5.24 de 5.24.1-3+deb9u4 a 5.24.1-3+deb9u5

---

#### 🔴 [CRITICAL] CVE-2018-18313 – perl: Heap-based buffer read overflow in S_grok_bslash_N()

| Campo | Valor |
|---|---|
| **ID** | `TRI-7CFA744F` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `9.1` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** Perl before 5.26.3 has a buffer over-read via a crafted regular expression that triggers disclosure of sensitive information from process memory.

**Evidencia:** `Paquete: libperl5.24 v5.24.1-3+deb9u4 | Fix: 5.24.1-3+deb9u5`

**✅ Remediación:** Actualizar libperl5.24 de 5.24.1-3+deb9u4 a 5.24.1-3+deb9u5

---

#### 🔴 [CRITICAL] CVE-2018-18314 – perl: Heap-based buffer overflow in S_regatom()

| Campo | Valor |
|---|---|
| **ID** | `TRI-C2B5AF0D` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `9.8` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** Perl before 5.26.3 has a buffer overflow via a crafted regular expression that triggers invalid write operations.

**Evidencia:** `Paquete: libperl5.24 v5.24.1-3+deb9u4 | Fix: 5.24.1-3+deb9u5`

**✅ Remediación:** Actualizar libperl5.24 de 5.24.1-3+deb9u4 a 5.24.1-3+deb9u5

---

#### 🔴 [CRITICAL] CVE-2017-12652 – libpng: does not check length of chunks against user limit

| Campo | Valor |
|---|---|
| **ID** | `TRI-FC17FA1D` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `9.8` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** libpng before 1.6.32 does not properly check the length of chunks against the user limit.

**Evidencia:** `Paquete: libpng16-16 v1.6.28-1 | Fix: Not available`

**✅ Remediación:** No hay fix disponible para libpng16-16 1.6.28-1 — considerar alternativa

---

#### 🔴 [CRITICAL] CVE-2018-25009 – libwebp: out-of-bounds read in WebPMuxCreateInternal

| Campo | Valor |
|---|---|
| **ID** | `TRI-9628C7A9` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `9.1` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** A heap-based buffer overflow was found in libwebp in versions before 1.0.1 in GetLE16().

**Evidencia:** `Paquete: libwebp6 v0.5.2-1 | Fix: 0.5.2-1+deb9u1`

**✅ Remediación:** Actualizar libwebp6 de 0.5.2-1 a 0.5.2-1+deb9u1

---

#### 🔴 [CRITICAL] CVE-2018-25010 – libwebp: out-of-bounds read in ApplyFilter()

| Campo | Valor |
|---|---|
| **ID** | `TRI-3D5EA016` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `9.1` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** A heap-based buffer overflow was found in libwebp in versions before 1.0.1 in ApplyFilter().

**Evidencia:** `Paquete: libwebp6 v0.5.2-1 | Fix: 0.5.2-1+deb9u1`

**✅ Remediación:** Actualizar libwebp6 de 0.5.2-1 a 0.5.2-1+deb9u1

---

#### 🔴 [CRITICAL] CVE-2018-25011 – libwebp: heap-based buffer overflow in PutLE16()

| Campo | Valor |
|---|---|
| **ID** | `TRI-34582FB2` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `9.8` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** A heap-based buffer overflow was found in libwebp in versions before 1.0.1 in PutLE16().

**Evidencia:** `Paquete: libwebp6 v0.5.2-1 | Fix: 0.5.2-1+deb9u1`

**✅ Remediación:** Actualizar libwebp6 de 0.5.2-1 a 0.5.2-1+deb9u1

---

#### 🔴 [CRITICAL] CVE-2018-25012 – libwebp: out-of-bounds read in WebPMuxCreateInternal()

| Campo | Valor |
|---|---|
| **ID** | `TRI-FD6E243E` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `9.1` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** A heap-based buffer overflow was found in libwebp in versions before 1.0.1 in GetLE24().

**Evidencia:** `Paquete: libwebp6 v0.5.2-1 | Fix: 0.5.2-1+deb9u1`

**✅ Remediación:** Actualizar libwebp6 de 0.5.2-1 a 0.5.2-1+deb9u1

---

#### 🔴 [CRITICAL] CVE-2018-25013 – libwebp: out-of-bounds read in ShiftBytes()

| Campo | Valor |
|---|---|
| **ID** | `TRI-C89FFB93` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `9.1` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** A heap-based buffer overflow was found in libwebp in versions before 1.0.1 in ShiftBytes().

**Evidencia:** `Paquete: libwebp6 v0.5.2-1 | Fix: 0.5.2-1+deb9u1`

**✅ Remediación:** Actualizar libwebp6 de 0.5.2-1 a 0.5.2-1+deb9u1

---

#### 🔴 [CRITICAL] CVE-2018-25014 – libwebp: use of uninitialized value in ReadSymbol()

| Campo | Valor |
|---|---|
| **ID** | `TRI-F8ABA861` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `9.8` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** A use of uninitialized value was found in libwebp in versions before 1.0.1 in ReadSymbol().

**Evidencia:** `Paquete: libwebp6 v0.5.2-1 | Fix: 0.5.2-1+deb9u1`

**✅ Remediación:** Actualizar libwebp6 de 0.5.2-1 a 0.5.2-1+deb9u1

---

#### 🔴 [CRITICAL] CVE-2020-36328 – libwebp: heap-based buffer overflow in WebPDecode*Into functions

| Campo | Valor |
|---|---|
| **ID** | `TRI-C957E0A3` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `9.8` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** A flaw was found in libwebp in versions before 1.0.1. A heap-based buffer overflow in function WebPDecodeRGBInto is possible due to an invalid check for buffer size. The highest threat from this vulnerability is to data confidentiality and integrity as well as system availability.

**Evidencia:** `Paquete: libwebp6 v0.5.2-1 | Fix: 0.5.2-1+deb9u1`

**✅ Remediación:** Actualizar libwebp6 de 0.5.2-1 a 0.5.2-1+deb9u1

---

#### 🔴 [CRITICAL] CVE-2020-36329 – libwebp: use-after-free in EmitFancyRGB() in dec/io_dec.c

| Campo | Valor |
|---|---|
| **ID** | `TRI-DD39BA0D` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `9.8` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** A flaw was found in libwebp in versions before 1.0.1. A use-after-free was found due to a thread being killed too early. The highest threat from this vulnerability is to data confidentiality and integrity as well as system availability.

**Evidencia:** `Paquete: libwebp6 v0.5.2-1 | Fix: 0.5.2-1+deb9u1`

**✅ Remediación:** Actualizar libwebp6 de 0.5.2-1 a 0.5.2-1+deb9u1

---

#### 🔴 [CRITICAL] CVE-2020-36330 – libwebp: out-of-bounds read in ChunkVerifyAndAssign() in mux/muxread.c

| Campo | Valor |
|---|---|
| **ID** | `TRI-504F5CE7` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `9.1` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** A flaw was found in libwebp in versions before 1.0.1. An out-of-bounds read was found in function ChunkVerifyAndAssign. The highest threat from this vulnerability is to data confidentiality and to the service availability.

**Evidencia:** `Paquete: libwebp6 v0.5.2-1 | Fix: 0.5.2-1+deb9u1`

**✅ Remediación:** Actualizar libwebp6 de 0.5.2-1 a 0.5.2-1+deb9u1

---

#### 🔴 [CRITICAL] CVE-2020-36331 – libwebp: out-of-bounds read in ChunkAssignData() in mux/muxinternal.c

| Campo | Valor |
|---|---|
| **ID** | `TRI-B734F9EB` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `9.1` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** A flaw was found in libwebp in versions before 1.0.1. An out-of-bounds read was found in function ChunkAssignData. The highest threat from this vulnerability is to data confidentiality and to the service availability.

**Evidencia:** `Paquete: libwebp6 v0.5.2-1 | Fix: 0.5.2-1+deb9u1`

**✅ Remediación:** Actualizar libwebp6 de 0.5.2-1 a 0.5.2-1+deb9u1

---

#### 🔴 [CRITICAL] CVE-2021-31535 – libX11: missing request length checks

| Campo | Valor |
|---|---|
| **ID** | `TRI-64FA7123` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `9.8` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** LookupCol.c in X.Org X through X11R7.7 and libX11 before 1.7.1 might allow remote attackers to execute arbitrary code. The libX11 XLookupColor request (intended for server-side color lookup) contains a flaw allowing a client to send color-name requests with a name longer than the maximum size allowed by the protocol (and also longer than the maximum packet size for normal-sized packets). The user-

**Evidencia:** `Paquete: libx11-6 v2:1.6.4-3 | Fix: 2:1.6.4-3+deb9u4`

**✅ Remediación:** Actualizar libx11-6 de 2:1.6.4-3 a 2:1.6.4-3+deb9u4

---

#### 🔴 [CRITICAL] CVE-2017-8872 – libxml2: Out-of-bounds read in htmlParseTryOrFinish

| Campo | Valor |
|---|---|
| **ID** | `TRI-201946D5` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `9.1` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** The htmlParseTryOrFinish function in HTMLparser.c in libxml2 2.9.4 allows attackers to cause a denial of service (buffer over-read) or information disclosure.

**Evidencia:** `Paquete: libxml2 v2.9.4+dfsg1-2.2+deb9u2 | Fix: 2.9.4+dfsg1-2.2+deb9u3`

**✅ Remediación:** Actualizar libxml2 de 2.9.4+dfsg1-2.2+deb9u2 a 2.9.4+dfsg1-2.2+deb9u3

---

#### 🔴 [CRITICAL] CVE-2019-11068 – libxslt: xsltCheckRead and xsltCheckWrite routines security bypass by crafted URL

| Campo | Valor |
|---|---|
| **ID** | `TRI-9B74A15E` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `9.8` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** libxslt through 1.1.33 allows bypass of a protection mechanism because callers of xsltCheckRead and xsltCheckWrite permit access even upon receiving a -1 error code. xsltCheckRead can return -1 for a crafted URL that is not actually invalid and is subsequently loaded.

**Evidencia:** `Paquete: libxslt1.1 v1.1.29-2.1 | Fix: 1.1.29-2.1+deb9u1`

**✅ Remediación:** Actualizar libxslt1.1 de 1.1.29-2.1 a 1.1.29-2.1+deb9u1

---

#### 🔴 [CRITICAL] CVE-2017-12424 – shadow-utils: Buffer overflow via newusers tool

| Campo | Valor |
|---|---|
| **ID** | `TRI-2A0A3051` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `9.8` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** In shadow before 4.5, the newusers tool could be made to manipulate internal data structures in ways unintended by the authors. Malformed input may lead to crashes (with a buffer overflow or other memory corruption) or other unspecified behaviors. This crosses a privilege boundary in, for example, certain web-hosting environments in which a Control Panel allows an unprivileged user account to crea

**Evidencia:** `Paquete: login v1:4.4-4.1 | Fix: 1:4.4-4.1+deb9u1`

**✅ Remediación:** Actualizar login de 1:4.4-4.1 a 1:4.4-4.1+deb9u1

---

#### 🔴 [CRITICAL] CVE-2016-9841 – zlib: Out-of-bounds pointer arithmetic in inffast.c

| Campo | Valor |
|---|---|
| **ID** | `TRI-235B18E1` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `9.8` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** inffast.c in zlib 1.2.8 might allow context-dependent attackers to have unspecified impact by leveraging improper pointer arithmetic.

**Evidencia:** `Paquete: rsync v3.1.2-1+deb9u1 | Fix: 3.1.2-1+deb9u2`

**✅ Remediación:** Actualizar rsync de 3.1.2-1+deb9u1 a 3.1.2-1+deb9u2

---

#### 🔴 [CRITICAL] CVE-2016-9843 – zlib: Big-endian out-of-bounds pointer

| Campo | Valor |
|---|---|
| **ID** | `TRI-D771E905` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `9.8` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** The crc32_big function in crc32.c in zlib 1.2.8 might allow context-dependent attackers to have unspecified impact via vectors involving big-endian CRC calculation.

**Evidencia:** `Paquete: rsync v3.1.2-1+deb9u1 | Fix: 3.1.2-1+deb9u2`

**✅ Remediación:** Actualizar rsync de 3.1.2-1+deb9u1 a 3.1.2-1+deb9u2

---

#### 🟠 [HIGH] CVE-2018-1333 – httpd: mod_http2: Too much time allocated to workers, possibly leading to DoS

| Campo | Valor |
|---|---|
| **ID** | `TRI-AFDDFC47` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** By specially crafting HTTP/2 requests, workers would be allocated 60 seconds longer than necessary, leading to worker exhaustion and a denial of service. Fixed in Apache HTTP Server 2.4.34 (Affected 2.4.18-2.4.30,2.4.33).

**Evidencia:** `Paquete: apache2 v2.4.25-3+deb9u5 | Fix: 2.4.25-3+deb9u6`

**✅ Remediación:** Actualizar apache2 de 2.4.25-3+deb9u5 a 2.4.25-3+deb9u6

---

#### 🟠 [HIGH] CVE-2018-17199 – httpd: mod_session_cookie does not respect expiry time

| Campo | Valor |
|---|---|
| **ID** | `TRI-8BD3347B` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** In Apache HTTP Server 2.4 release 2.4.37 and prior, mod_session checks the session expiry time before decoding the session. This causes session expiry time to be ignored for mod_session_cookie sessions since the expiry time is loaded when the session is decoded.

**Evidencia:** `Paquete: apache2 v2.4.25-3+deb9u5 | Fix: 2.4.25-3+deb9u7`

**✅ Remediación:** Actualizar apache2 de 2.4.25-3+deb9u5 a 2.4.25-3+deb9u7

---

#### 🟠 [HIGH] CVE-2019-0211 – httpd: privilege escalation from modules scripts

| Campo | Valor |
|---|---|
| **ID** | `TRI-D702B7E5` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.8` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** In Apache HTTP Server 2.4 releases 2.4.17 to 2.4.38, with MPM event, worker or prefork, code executing in less-privileged child processes or threads (including scripts executed by an in-process scripting interpreter) could execute arbitrary code with the privileges of the parent process (usually root) by manipulating the scoreboard. Non-Unix systems are not affected.

**Evidencia:** `Paquete: apache2 v2.4.25-3+deb9u5 | Fix: 2.4.25-3+deb9u7`

**✅ Remediación:** Actualizar apache2 de 2.4.25-3+deb9u5 a 2.4.25-3+deb9u7

---

#### 🟠 [HIGH] CVE-2019-0217 – httpd: mod_auth_digest: access control bypass due to race condition

| Campo | Valor |
|---|---|
| **ID** | `TRI-0041E9E1` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** In Apache HTTP Server 2.4 release 2.4.38 and prior, a race condition in mod_auth_digest when running in a threaded server could allow a user with valid credentials to authenticate using another username, bypassing configured access control restrictions.

**Evidencia:** `Paquete: apache2 v2.4.25-3+deb9u5 | Fix: 2.4.25-3+deb9u7`

**✅ Remediación:** Actualizar apache2 de 2.4.25-3+deb9u5 a 2.4.25-3+deb9u7

---

#### 🟠 [HIGH] CVE-2019-10081 – httpd: memory corruption on early pushes

| Campo | Valor |
|---|---|
| **ID** | `TRI-97811910` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** HTTP/2 (2.4.20 through 2.4.39) very early pushes, for example configured with "H2PushResource", could lead to an overwrite of memory in the pushing request's pool, leading to crashes. The memory copied is that of the configured push link header values, not data supplied by the client.

**Evidencia:** `Paquete: apache2 v2.4.25-3+deb9u5 | Fix: 2.4.25-3+deb9u8`

**✅ Remediación:** Actualizar apache2 de 2.4.25-3+deb9u5 a 2.4.25-3+deb9u8

---

#### 🟠 [HIGH] CVE-2019-9517 – HTTP/2: request for large response leads to denial of service

| Campo | Valor |
|---|---|
| **ID** | `TRI-3DCC97AC` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** Some HTTP/2 implementations are vulnerable to unconstrained interal data buffering, potentially leading to a denial of service. The attacker opens the HTTP/2 window so the peer can send without constraint; however, they leave the TCP window closed so the peer cannot actually write (many of) the bytes on the wire. The attacker then sends a stream of requests for a large response object. Depending o

**Evidencia:** `Paquete: apache2 v2.4.25-3+deb9u5 | Fix: 2.4.25-3+deb9u8`

**✅ Remediación:** Actualizar apache2 de 2.4.25-3+deb9u5 a 2.4.25-3+deb9u8

---

#### 🟠 [HIGH] CVE-2020-11993 – httpd: mod_http2 concurrent pool usage

| Campo | Valor |
|---|---|
| **ID** | `TRI-EE5024BF` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** Apache HTTP Server versions 2.4.20 to 2.4.43 When trace/debug was enabled for the HTTP/2 module and on certain traffic edge patterns, logging statements were made on the wrong connection, causing concurrent use of memory pools. Configuring the LogLevel of mod_http2 above "info" will mitigate this vulnerability for unpatched servers.

**Evidencia:** `Paquete: apache2 v2.4.25-3+deb9u5 | Fix: Not available`

**✅ Remediación:** No hay fix disponible para apache2 2.4.25-3+deb9u5 — considerar alternativa

---

#### 🟠 [HIGH] CVE-2020-35452 – httpd: Single zero byte stack overflow in mod_auth_digest

| Campo | Valor |
|---|---|
| **ID** | `TRI-B0B13A7E` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.3` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** Apache HTTP Server versions 2.4.0 to 2.4.46 A specially crafted Digest nonce can cause a stack overflow in mod_auth_digest. There is no report of this overflow being exploitable, nor the Apache HTTP Server team could create one, though some particular compiler and/or compilation option might make it possible, with limited consequences anyway due to the size (a single byte) and the value (zero byte

**Evidencia:** `Paquete: apache2 v2.4.25-3+deb9u5 | Fix: 2.4.25-3+deb9u10`

**✅ Remediación:** Actualizar apache2 de 2.4.25-3+deb9u5 a 2.4.25-3+deb9u10

---

#### 🟠 [HIGH] CVE-2020-9490 – httpd: Push diary crash on specifically crafted HTTP/2 header

| Campo | Valor |
|---|---|
| **ID** | `TRI-796091D3` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** Apache HTTP Server versions 2.4.20 to 2.4.43. A specially crafted value for the 'Cache-Digest' header in a HTTP/2 request would result in a crash when the server actually tries to HTTP/2 PUSH a resource afterwards. Configuring the HTTP/2 feature via "H2Push off" will mitigate this vulnerability for unpatched servers.

**Evidencia:** `Paquete: apache2 v2.4.25-3+deb9u5 | Fix: Not available`

**✅ Remediación:** No hay fix disponible para apache2 2.4.25-3+deb9u5 — considerar alternativa

---

#### 🟠 [HIGH] CVE-2021-26690 – httpd: mod_session: NULL pointer dereference when parsing Cookie header

| Campo | Valor |
|---|---|
| **ID** | `TRI-5AA4E850` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** Apache HTTP Server versions 2.4.0 to 2.4.46 A specially crafted Cookie header handled by mod_session can cause a NULL pointer dereference and crash, leading to a possible Denial Of Service

**Evidencia:** `Paquete: apache2 v2.4.25-3+deb9u5 | Fix: 2.4.25-3+deb9u10`

**✅ Remediación:** Actualizar apache2 de 2.4.25-3+deb9u5 a 2.4.25-3+deb9u10

---

#### 🟠 [HIGH] CVE-2021-31618 – httpd: NULL pointer dereference on specially crafted HTTP/2 request

| Campo | Valor |
|---|---|
| **ID** | `TRI-36A76AC7` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** Apache HTTP Server protocol handler for the HTTP/2 protocol checks received request headers against the size limitations as configured for the server and used for the HTTP/1 protocol as well. On violation of these restrictions and HTTP response is sent to the client with a status code indicating why the request was rejected. This rejection response was not fully initialised in the HTTP/2 protocol 

**Evidencia:** `Paquete: apache2 v2.4.25-3+deb9u5 | Fix: 2.4.25-3+deb9u10`

**✅ Remediación:** Actualizar apache2 de 2.4.25-3+deb9u5 a 2.4.25-3+deb9u10

---

#### 🟠 [HIGH] CVE-2021-33193 – httpd: Request splitting via HTTP/2 method injection and mod_proxy

| Campo | Valor |
|---|---|
| **ID** | `TRI-A3717316` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** A crafted method sent through HTTP/2 will bypass validation and be forwarded by mod_proxy, which can lead to request splitting or cache poisoning. This issue affects Apache HTTP Server 2.4.17 to 2.4.48.

**Evidencia:** `Paquete: apache2 v2.4.25-3+deb9u5 | Fix: Not available`

**✅ Remediación:** No hay fix disponible para apache2 2.4.25-3+deb9u5 — considerar alternativa

---

#### 🟠 [HIGH] CVE-2021-34798 – httpd: NULL pointer dereference via malformed requests

| Campo | Valor |
|---|---|
| **ID** | `TRI-17570332` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** Malformed requests may cause the server to dereference a NULL pointer. This issue affects Apache HTTP Server 2.4.48 and earlier.

**Evidencia:** `Paquete: apache2 v2.4.25-3+deb9u5 | Fix: 2.4.25-3+deb9u11`

**✅ Remediación:** Actualizar apache2 de 2.4.25-3+deb9u5 a 2.4.25-3+deb9u11

---

#### 🟠 [HIGH] CVE-2021-44224 – httpd: possible NULL dereference or SSRF in forward proxy configurations

| Campo | Valor |
|---|---|
| **ID** | `TRI-7BF39231` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `8.2` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** A crafted URI sent to httpd configured as a forward proxy (ProxyRequests on) can cause a crash (NULL pointer dereference) or, for configurations mixing forward and reverse proxy declarations, can allow for requests to be directed to a declared Unix Domain Socket endpoint (Server Side Request Forgery). This issue affects Apache HTTP Server 2.4.7 up to 2.4.51 (included).

**Evidencia:** `Paquete: apache2 v2.4.25-3+deb9u5 | Fix: 2.4.25-3+deb9u12`

**✅ Remediación:** Actualizar apache2 de 2.4.25-3+deb9u5 a 2.4.25-3+deb9u12

---

#### 🟠 [HIGH] CVE-2022-22719 – httpd: mod_lua: Use of uninitialized value of in r:parsebody

| Campo | Valor |
|---|---|
| **ID** | `TRI-95EB2210` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** A carefully crafted request body can cause a read to a random memory area which could cause the process to crash. This issue affects Apache HTTP Server 2.4.52 and earlier.

**Evidencia:** `Paquete: apache2 v2.4.25-3+deb9u5 | Fix: 2.4.25-3+deb9u13`

**✅ Remediación:** Actualizar apache2 de 2.4.25-3+deb9u5 a 2.4.25-3+deb9u13

---

#### 🟠 [HIGH] CVE-2019-3462 – Incorrect sanitation of the 302 redirect field in HTTP transport metho ...

| Campo | Valor |
|---|---|
| **ID** | `TRI-A75C67CA` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `8.1` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** Incorrect sanitation of the 302 redirect field in HTTP transport method of apt versions 1.4.8 and earlier can lead to content injection by a MITM attacker, potentially leading to remote code execution on the target machine.

**Evidencia:** `Paquete: apt v1.4.8 | Fix: 1.4.9`

**✅ Remediación:** Actualizar apt de 1.4.8 a 1.4.9

---

#### 🟠 [HIGH] CVE-2016-2779 – util-linux: runuser tty hijack via TIOCSTI ioctl

| Campo | Valor |
|---|---|
| **ID** | `TRI-20DFB615` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.8` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** runuser in util-linux allows local users to escape to the parent session via a crafted TIOCSTI ioctl call, which pushes characters to the terminal's input buffer.

**Evidencia:** `Paquete: bsdutils v1:2.29.2-1+deb9u1 | Fix: Not available`

**✅ Remediación:** No hay fix disponible para bsdutils 1:2.29.2-1+deb9u1 — considerar alternativa

---

#### 🟠 [HIGH] CVE-2022-1304 – e2fsprogs: out-of-bounds read/write via crafted filesystem

| Campo | Valor |
|---|---|
| **ID** | `TRI-361A3065` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.8` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** An out-of-bounds read/write vulnerability was found in e2fsprogs 1.46.5. This issue leads to a segmentation fault and possibly arbitrary code execution via a specially crafted filesystem.

**Evidencia:** `Paquete: e2fslibs v1.43.4-2 | Fix: Not available`

**✅ Remediación:** No hay fix disponible para e2fslibs 1.43.4-2 — considerar alternativa

---

#### 🟠 [HIGH] CVE-2019-18218 – file: heap-based buffer overflow in cdf_read_property_info in cdf.c

| Campo | Valor |
|---|---|
| **ID** | `TRI-762775AC` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.8` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** cdf_read_property_info in cdf.c in file through 5.37 does not restrict the number of CDF_VECTOR elements, which allows a heap-based buffer overflow (4-byte out-of-bounds write).

**Evidencia:** `Paquete: file v1:5.30-1+deb9u2 | Fix: 1:5.30-1+deb9u3`

**✅ Remediación:** Actualizar file de 1:5.30-1+deb9u2 a 1:5.30-1+deb9u3

---

#### 🟠 [HIGH] CVE-2019-8907 – file: do_core_note in readelf.c allows remote attackers to cause a denial of service

| Campo | Valor |
|---|---|
| **ID** | `TRI-57EC23DA` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `8.8` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** do_core_note in readelf.c in libmagic.a in file 5.35 allows remote attackers to cause a denial of service (stack corruption and application crash) or possibly have unspecified other impact.

**Evidencia:** `Paquete: file v1:5.30-1+deb9u2 | Fix: Not available`

**✅ Remediación:** No hay fix disponible para file 1:5.30-1+deb9u2 — considerar alternativa

---

#### 🟠 [HIGH] CVE-2018-12886 – gcc: spilling of stack protection address in cfgexpand.c and function.c leads to stack-overflow protection bypass

| Campo | Valor |
|---|---|
| **ID** | `TRI-66097BA4` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `8.1` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** stack_protect_prologue in cfgexpand.c and stack_protect_epilogue in function.c in GNU Compiler Collection (GCC) 4.1 through 8 (under certain circumstances) generate instruction sequences when targeting ARM targets that spill the address of the stack protector guard, which allows an attacker to bypass the protection of -fstack-protector, -fstack-protector-all, -fstack-protector-strong, and -fstack-

**Evidencia:** `Paquete: gcc-6-base v6.3.0-18+deb9u1 | Fix: Not available`

**✅ Remediación:** No hay fix disponible para gcc-6-base 6.3.0-18+deb9u1 — considerar alternativa

---

#### 🟠 [HIGH] CVE-2018-1000858 – gnupg2: Cross site request forgery in dirmngr resulting in an information disclosure or denial of service

| Campo | Valor |
|---|---|
| **ID** | `TRI-0BCD64CE` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `8.8` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** GnuPG version 2.1.12 - 2.2.11 contains a Cross ite Request Forgery (CSRF) vulnerability in dirmngr that can result in Attacker controlled CSRF, Information Disclosure, DoS. This attack appear to be exploitable via Victim must perform a WKD request, e.g. enter an email address in the composer window of Thunderbird/Enigmail. This vulnerability appears to have been fixed in after commit 4a4bb874f6374

**Evidencia:** `Paquete: gpgv v2.1.18-8~deb9u2 | Fix: Not available`

**✅ Remediación:** No hay fix disponible para gpgv 2.1.18-8~deb9u2 — considerar alternativa

---

#### 🟠 [HIGH] CVE-2022-1271 – gzip: arbitrary-file-write vulnerability

| Campo | Valor |
|---|---|
| **ID** | `TRI-A6DB82D4` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `8.8` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** An arbitrary file write vulnerability was found in GNU gzip's zgrep utility. When zgrep is applied on the attacker's chosen file name (for example, a crafted file name), this can overwrite an attacker's content to an arbitrary attacker-selected file. This flaw occurs due to insufficient validation when processing filenames with two or more newlines where selected content and the target file names 

**Evidencia:** `Paquete: gzip v1.6-5+b1 | Fix: 1.6-5+deb9u1`

**✅ Remediación:** Actualizar gzip de 1.6-5+b1 a 1.6-5+deb9u1

---

#### 🟠 [HIGH] CVE-2020-28196 – krb5: unbounded recursion via an ASN.1-encoded Kerberos message in lib/krb5/asn.1/asn1_encode.c may lead to DoS

| Campo | Valor |
|---|---|
| **ID** | `TRI-ED935D15` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** MIT Kerberos 5 (aka krb5) before 1.17.2 and 1.18.x before 1.18.3 allows unbounded recursion via an ASN.1-encoded Kerberos message because the lib/krb5/asn.1/asn1_encode.c support for BER indefinite lengths lacks a recursion limit.

**Evidencia:** `Paquete: krb5-locales v1.15-1+deb9u1 | Fix: 1.15-1+deb9u2`

**✅ Remediación:** Actualizar krb5-locales de 1.15-1+deb9u1 a 1.15-1+deb9u2

---

#### 🟠 [HIGH] CVE-2017-7189 – php: misparsing fsockopen calls in main/streams/xp_socket.c leads to information disclosure

| Campo | Valor |
|---|---|
| **ID** | `TRI-1CAACFDE` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** main/streams/xp_socket.c in PHP 7.x before 2017-03-07 misparses fsockopen calls, such as by interpreting fsockopen('127.0.0.1:80', 443) as if the address/port were 127.0.0.1:80:443, which is later truncated to 127.0.0.1:80. This behavior has a security risk if the explicitly provided port number (i.e., 443 in this example) is hardcoded into an application as a security policy, but the hostname arg

**Evidencia:** `Paquete: libapache2-mod-php7.0 v7.0.30-0+deb9u1 | Fix: Not available`

**✅ Remediación:** No hay fix disponible para libapache2-mod-php7.0 7.0.30-0+deb9u1 — considerar alternativa

---

#### 🟠 [HIGH] CVE-2017-7272 – php: potential SSRF via fsockopen

| Campo | Valor |
|---|---|
| **ID** | `TRI-5477117D` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.4` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** PHP through 7.1.11 enables potential SSRF in applications that accept an fsockopen or pfsockopen hostname argument with an expectation that the port number is constrained. Because a :port syntax is recognized, fsockopen will use the port number that is specified in the hostname argument, instead of the port number in the second argument of the function.

**Evidencia:** `Paquete: libapache2-mod-php7.0 v7.0.30-0+deb9u1 | Fix: Not available`

**✅ Remediación:** No hay fix disponible para libapache2-mod-php7.0 7.0.30-0+deb9u1 — considerar alternativa

---

#### 🟠 [HIGH] CVE-2018-14883 – php: exif: integer overflow leading to out-of-bound buffer read in exif_thumbnail_extract()

| Campo | Valor |
|---|---|
| **ID** | `TRI-5B27067E` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** An issue was discovered in PHP before 5.6.37, 7.0.x before 7.0.31, 7.1.x before 7.1.20, and 7.2.x before 7.2.8. An Integer Overflow leads to a heap-based buffer over-read in exif_thumbnail_extract of exif.c.

**Evidencia:** `Paquete: libapache2-mod-php7.0 v7.0.30-0+deb9u1 | Fix: 7.0.33-0+deb9u1`

**✅ Remediación:** Actualizar libapache2-mod-php7.0 de 7.0.30-0+deb9u1 a 7.0.33-0+deb9u1

---

#### 🟠 [HIGH] CVE-2018-19518 – php: imap_open() allows running arbitrary shell commands via mailbox parameter

| Campo | Valor |
|---|---|
| **ID** | `TRI-D9CA6370` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** University of Washington IMAP Toolkit 2007f on UNIX, as used in imap_open() in PHP and other products, launches an rsh command (by means of the imap_rimap function in c-client/imap4r1.c and the tcp_aopen function in osdep/unix/tcp_unix.c) without preventing argument injection, which might allow remote attackers to execute arbitrary OS commands if the IMAP server name is untrusted input (e.g., ente

**Evidencia:** `Paquete: libapache2-mod-php7.0 v7.0.30-0+deb9u1 | Fix: 7.0.33-0+deb9u1`

**✅ Remediación:** Actualizar libapache2-mod-php7.0 de 7.0.30-0+deb9u1 a 7.0.33-0+deb9u1

---

#### 🟠 [HIGH] CVE-2018-19935 – php: NULL pointer dereference in ext/imap/php_imap.c resulting in a denial of service

| Campo | Valor |
|---|---|
| **ID** | `TRI-70C0F4BD` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** ext/imap/php_imap.c in PHP 5.x and 7.x before 7.3.0 allows remote attackers to cause a denial of service (NULL pointer dereference and application crash) via an empty string in the message argument to the imap_mail function.

**Evidencia:** `Paquete: libapache2-mod-php7.0 v7.0.30-0+deb9u1 | Fix: 7.0.33-0+deb9u1`

**✅ Remediación:** Actualizar libapache2-mod-php7.0 de 7.0.30-0+deb9u1 a 7.0.33-0+deb9u1

---

#### 🟠 [HIGH] CVE-2018-20783 – php: Buffer over-read in PHAR reading functions

| Campo | Valor |
|---|---|
| **ID** | `TRI-B976750E` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** In PHP before 5.6.39, 7.x before 7.0.33, 7.1.x before 7.1.25, and 7.2.x before 7.2.13, a buffer over-read in PHAR reading functions may allow an attacker to read allocated or unallocated memory past the actual data when trying to parse a .phar file. This is related to phar_parse_pharfile in ext/phar/phar.c.

**Evidencia:** `Paquete: libapache2-mod-php7.0 v7.0.30-0+deb9u1 | Fix: 7.0.33-0+deb9u1`

**✅ Remediación:** Actualizar libapache2-mod-php7.0 de 7.0.30-0+deb9u1 a 7.0.33-0+deb9u1

---

#### 🟠 [HIGH] CVE-2019-11041 – php: Heap buffer over-read in exif_scan_thumbnail()

| Campo | Valor |
|---|---|
| **ID** | `TRI-2D794933` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.1` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** When PHP EXIF extension is parsing EXIF information from an image, e.g. via exif_read_data() function, in PHP versions 7.1.x below 7.1.31, 7.2.x below 7.2.21 and 7.3.x below 7.3.8 it is possible to supply it with data what will cause it to read past the allocated buffer. This may lead to information disclosure or crash.

**Evidencia:** `Paquete: libapache2-mod-php7.0 v7.0.30-0+deb9u1 | Fix: 7.0.33-0+deb9u5`

**✅ Remediación:** Actualizar libapache2-mod-php7.0 de 7.0.30-0+deb9u1 a 7.0.33-0+deb9u5

---

#### 🟠 [HIGH] CVE-2019-11042 – php: Heap buffer over-read in exif_process_user_comment()

| Campo | Valor |
|---|---|
| **ID** | `TRI-94AB5089` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.1` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** When PHP EXIF extension is parsing EXIF information from an image, e.g. via exif_read_data() function, in PHP versions 7.1.x below 7.1.31, 7.2.x below 7.2.21 and 7.3.x below 7.3.8 it is possible to supply it with data what will cause it to read past the allocated buffer. This may lead to information disclosure or crash.

**Evidencia:** `Paquete: libapache2-mod-php7.0 v7.0.30-0+deb9u1 | Fix: 7.0.33-0+deb9u5`

**✅ Remediación:** Actualizar libapache2-mod-php7.0 de 7.0.30-0+deb9u1 a 7.0.33-0+deb9u5

---

#### 🟠 [HIGH] CVE-2019-9022 – php: memcpy with negative length via crafted DNS response

| Campo | Valor |
|---|---|
| **ID** | `TRI-BBD1AC65` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** An issue was discovered in PHP 7.x before 7.1.26, 7.2.x before 7.2.14, and 7.3.x before 7.3.2. dns_get_record misparses a DNS response, which can allow a hostile DNS server to cause PHP to misuse memcpy, leading to read operations going past the buffer allocated for DNS data. This affects php_parserr in ext/standard/dns.c for DNS_CAA and DNS_ANY queries.

**Evidencia:** `Paquete: libapache2-mod-php7.0 v7.0.30-0+deb9u1 | Fix: 7.0.33-0+deb9u2`

**✅ Remediación:** Actualizar libapache2-mod-php7.0 de 7.0.30-0+deb9u1 a 7.0.33-0+deb9u2

---

#### 🟠 [HIGH] CVE-2019-9024 – php: Out-of-bounds read in base64_decode_xmlrpc in ext/xmlrpc/libxmlrpc/base64.c

| Campo | Valor |
|---|---|
| **ID** | `TRI-50C7F200` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** An issue was discovered in PHP before 5.6.40, 7.x before 7.1.26, 7.2.x before 7.2.14, and 7.3.x before 7.3.1. xmlrpc_decode() can allow a hostile XMLRPC server to cause PHP to read memory outside of allocated areas in base64_decode_xmlrpc in ext/xmlrpc/libxmlrpc/base64.c.

**Evidencia:** `Paquete: libapache2-mod-php7.0 v7.0.30-0+deb9u1 | Fix: 7.0.33-0+deb9u2`

**✅ Remediación:** Actualizar libapache2-mod-php7.0 de 7.0.30-0+deb9u1 a 7.0.33-0+deb9u2

---

#### 🟠 [HIGH] CVE-2019-9637 – php: File rename across filesystems may allow unwanted access during processing

| Campo | Valor |
|---|---|
| **ID** | `TRI-2FDEA12C` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** An issue was discovered in PHP before 7.1.27, 7.2.x before 7.2.16, and 7.3.x before 7.3.3. Due to the way rename() across filesystems is implemented, it is possible that file being renamed is briefly available with wrong permissions while the rename is ongoing, thus enabling unauthorized users to access the data.

**Evidencia:** `Paquete: libapache2-mod-php7.0 v7.0.30-0+deb9u1 | Fix: 7.0.33-0+deb9u3`

**✅ Remediación:** Actualizar libapache2-mod-php7.0 de 7.0.30-0+deb9u1 a 7.0.33-0+deb9u3

---

#### 🟠 [HIGH] CVE-2019-9638 – php: Uninitialized read in exif_process_IFD_in_MAKERNOTE

| Campo | Valor |
|---|---|
| **ID** | `TRI-229D166D` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** An issue was discovered in the EXIF component in PHP before 7.1.27, 7.2.x before 7.2.16, and 7.3.x before 7.3.3. There is an uninitialized read in exif_process_IFD_in_MAKERNOTE because of mishandling the maker_note->offset relationship to value_len.

**Evidencia:** `Paquete: libapache2-mod-php7.0 v7.0.30-0+deb9u1 | Fix: 7.0.33-0+deb9u3`

**✅ Remediación:** Actualizar libapache2-mod-php7.0 de 7.0.30-0+deb9u1 a 7.0.33-0+deb9u3

---

#### 🟠 [HIGH] CVE-2019-9639 – php: Uninitialized read in exif_process_IFD_in_MAKERNOTE

| Campo | Valor |
|---|---|
| **ID** | `TRI-DCFECA51` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** An issue was discovered in the EXIF component in PHP before 7.1.27, 7.2.x before 7.2.16, and 7.3.x before 7.3.3. There is an uninitialized read in exif_process_IFD_in_MAKERNOTE because of mishandling the data_len variable.

**Evidencia:** `Paquete: libapache2-mod-php7.0 v7.0.30-0+deb9u1 | Fix: 7.0.33-0+deb9u3`

**✅ Remediación:** Actualizar libapache2-mod-php7.0 de 7.0.30-0+deb9u1 a 7.0.33-0+deb9u3

---

#### 🟠 [HIGH] CVE-2019-9640 – php: Invalid read in exif_process_SOFn()

| Campo | Valor |
|---|---|
| **ID** | `TRI-A3B023B9` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** An issue was discovered in the EXIF component in PHP before 7.1.27, 7.2.x before 7.2.16, and 7.3.x before 7.3.3. There is an Invalid Read in exif_process_SOFn.

**Evidencia:** `Paquete: libapache2-mod-php7.0 v7.0.30-0+deb9u1 | Fix: 7.0.33-0+deb9u3`

**✅ Remediación:** Actualizar libapache2-mod-php7.0 de 7.0.30-0+deb9u1 a 7.0.33-0+deb9u3

---

#### 🟠 [HIGH] CVE-2019-9675 – php: buffer overflow in ext/phar/tar.c

| Campo | Valor |
|---|---|
| **ID** | `TRI-A086BC2D` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `8.1` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** An issue was discovered in PHP 7.x before 7.1.27 and 7.3.x before 7.3.3. phar_tar_writeheaders_int in ext/phar/tar.c has a buffer overflow via a long link value. NOTE: The vendor indicates that the link value is used only when an archive contains a symlink, which currently cannot happen: "This issue allows theoretical compromise of security, but a practical attack is usually impossible.

**Evidencia:** `Paquete: libapache2-mod-php7.0 v7.0.30-0+deb9u1 | Fix: 7.0.33-0+deb9u3`

**✅ Remediación:** Actualizar libapache2-mod-php7.0 de 7.0.30-0+deb9u1 a 7.0.33-0+deb9u3

---

#### 🟠 [HIGH] CVE-2020-7062 – php: NULL pointer dereference in PHP session upload progress

| Campo | Valor |
|---|---|
| **ID** | `TRI-1CB04094` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** In PHP versions 7.2.x below 7.2.28, 7.3.x below 7.3.15 and 7.4.x below 7.4.3, when using file upload functionality, if upload progress tracking is enabled, but session.upload_progress.cleanup is set to 0 (disabled), and the file upload fails, the upload procedure would try to clean up data that does not exist and encounter null pointer dereference, which would likely lead to a crash.

**Evidencia:** `Paquete: libapache2-mod-php7.0 v7.0.30-0+deb9u1 | Fix: 7.0.33-0+deb9u8`

**✅ Remediación:** Actualizar libapache2-mod-php7.0 de 7.0.30-0+deb9u1 a 7.0.33-0+deb9u8

---

#### 🟠 [HIGH] CVE-2020-7067 – php: out-of-bounds read when using a malformed url-encoded string

| Campo | Valor |
|---|---|
| **ID** | `TRI-49E117C3` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** In PHP versions 7.2.x below 7.2.30, 7.3.x below 7.3.17 and 7.4.x below 7.4.5, if PHP is compiled with EBCDIC support (uncommon), urldecode() function can be made to access locations past the allocated memory, due to erroneously using signed numbers as array indexes.

**Evidencia:** `Paquete: libapache2-mod-php7.0 v7.0.30-0+deb9u1 | Fix: 7.0.33-0+deb9u8`

**✅ Remediación:** Actualizar libapache2-mod-php7.0 de 7.0.30-0+deb9u1 a 7.0.33-0+deb9u8

---

#### 🟠 [HIGH] CVE-2021-21702 – php: NULL pointer dereference in SoapClient

| Campo | Valor |
|---|---|
| **ID** | `TRI-60CC9341` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** In PHP versions 7.3.x below 7.3.27, 7.4.x below 7.4.15 and 8.0.x below 8.0.2, when using SOAP extension to connect to a SOAP server, a malicious SOAP server could return malformed XML data as a response that would cause PHP to access a null pointer and thus cause a crash.

**Evidencia:** `Paquete: libapache2-mod-php7.0 v7.0.30-0+deb9u1 | Fix: 7.0.33-0+deb9u11`

**✅ Remediación:** Actualizar libapache2-mod-php7.0 de 7.0.30-0+deb9u1 a 7.0.33-0+deb9u11

---

#### 🟠 [HIGH] CVE-2021-21703 – php: Local privilege escalation via PHP-FPM

| Campo | Valor |
|---|---|
| **ID** | `TRI-3F0D307D` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.0` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** In PHP versions 7.3.x up to and including 7.3.31, 7.4.x below 7.4.25 and 8.0.x below 8.0.12, when running PHP FPM SAPI with main FPM daemon process running as root and child worker processes running as lower-privileged users, it is possible for the child processes to access memory shared with the main process and write to it, modifying it in a way that would cause the root process to conduct inval

**Evidencia:** `Paquete: libapache2-mod-php7.0 v7.0.30-0+deb9u1 | Fix: 7.0.33-0+deb9u12`

**✅ Remediación:** Actualizar libapache2-mod-php7.0 de 7.0.30-0+deb9u1 a 7.0.33-0+deb9u12

---

#### 🟠 [HIGH] CVE-2022-31625 – php: Uninitialized array in pg_query_params() leading to RCE

| Campo | Valor |
|---|---|
| **ID** | `TRI-76FF2AF7` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `8.1` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** In PHP versions 7.4.x below 7.4.30, 8.0.x below 8.0.20, and 8.1.x below 8.1.7, when using Postgres database extension, supplying invalid parameters to the parametrized query may lead to PHP attempting to free memory using uninitialized data as pointers. This could lead to RCE vulnerability or denial of service.

**Evidencia:** `Paquete: libapache2-mod-php7.0 v7.0.30-0+deb9u1 | Fix: Not available`

**✅ Remediación:** No hay fix disponible para libapache2-mod-php7.0 7.0.30-0+deb9u1 — considerar alternativa

---

#### 🟠 [HIGH] CVE-2022-31626 – php: password of excessive length triggers buffer overflow leading to RCE

| Campo | Valor |
|---|---|
| **ID** | `TRI-8ADE29B9` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `8.8` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** In PHP versions 7.4.x below 7.4.30, 8.0.x below 8.0.20, and 8.1.x below 8.1.7, when pdo_mysql extension with mysqlnd driver, if the third party is allowed to supply host to connect to and the password for the connection, password of excessive length can trigger a buffer overflow in PHP, which can lead to a remote code execution vulnerability.

**Evidencia:** `Paquete: libapache2-mod-php7.0 v7.0.30-0+deb9u1 | Fix: Not available`

**✅ Remediación:** No hay fix disponible para libapache2-mod-php7.0 7.0.30-0+deb9u1 — considerar alternativa

---

#### 🟠 [HIGH] CVE-2017-12613 – apr: Out-of-bounds array deref in apr_time_exp*() functions

| Campo | Valor |
|---|---|
| **ID** | `TRI-D5612BAB` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.1` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** When apr_time_exp*() or apr_os_exp_time*() functions are invoked with an invalid month field value in Apache Portable Runtime APR 1.6.2 and prior, out of bounds memory may be accessed in converting this value to an apr_time_exp_t value, potentially revealing the contents of a different static heap value or resulting in program termination, and may represent an information disclosure or denial of s

**Evidencia:** `Paquete: libapr1 v1.5.2-5 | Fix: 1.5.2-5+deb9u1`

**✅ Remediación:** Actualizar libapr1 de 1.5.2-5 a 1.5.2-5+deb9u1

---

#### 🟠 [HIGH] CVE-2017-1000408 – glibc: Memory leak reachable via LD_HWCAP_MASK

| Campo | Valor |
|---|---|
| **ID** | `TRI-93B69258` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.8` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** A memory leak in glibc 2.1.1 (released on May 24, 1999) can be reached and amplified through the LD_HWCAP_MASK environment variable. Please note that many versions of glibc are not vulnerable to this issue if patched for CVE-2017-1000366.

**Evidencia:** `Paquete: libc-bin v2.24-11+deb9u3 | Fix: 2.24-11+deb9u4`

**✅ Remediación:** Actualizar libc-bin de 2.24-11+deb9u3 a 2.24-11+deb9u4

---

#### 🟠 [HIGH] CVE-2017-1000409 – glibc: Buffer overflow triggerable via LD_LIBRARY_PATH

| Campo | Valor |
|---|---|
| **ID** | `TRI-CB101DA3` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.0` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** A buffer overflow in glibc 2.5 (released on September 29, 2006) and can be triggered through the LD_LIBRARY_PATH environment variable. Please note that many versions of glibc are not vulnerable to this issue if patched for CVE-2017-1000366.

**Evidencia:** `Paquete: libc-bin v2.24-11+deb9u3 | Fix: 2.24-11+deb9u4`

**✅ Remediación:** Actualizar libc-bin de 2.24-11+deb9u3 a 2.24-11+deb9u4

---

#### 🟠 [HIGH] CVE-2017-16997 – glibc: Incorrect handling of RPATH in elf/dl-load.c can be used to execute code loaded from arbitrary libraries

| Campo | Valor |
|---|---|
| **ID** | `TRI-38D9B849` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.8` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** elf/dl-load.c in the GNU C Library (aka glibc or libc6) 2.19 through 2.26 mishandles RPATH and RUNPATH containing $ORIGIN for a privileged (setuid or AT_SECURE) program, which allows local users to gain privileges via a Trojan horse library in the current working directory, related to the fillin_rpath and decompose_rpath functions. This is associated with misinterpretion of an empty RPATH/RUNPATH 

**Evidencia:** `Paquete: libc-bin v2.24-11+deb9u3 | Fix: 2.24-11+deb9u4`

**✅ Remediación:** Actualizar libc-bin de 2.24-11+deb9u3 a 2.24-11+deb9u4

---

#### 🟠 [HIGH] CVE-2020-14393 – perl-dbi: Buffer overflow on an overlong DBD class name

| Campo | Valor |
|---|---|
| **ID** | `TRI-BED56857` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.1` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** A buffer overflow was found in perl-DBI < 1.643 in DBI.xs. A local attacker who is able to supply a string longer than 300 characters could cause an out-of-bounds write, affecting the availability of the service or integrity of data.

**Evidencia:** `Paquete: libdbi-perl v1.636-1+b1 | Fix: 1.636-1+deb9u1`

**✅ Remediación:** Actualizar libdbi-perl de 1.636-1+b1 a 1.636-1+deb9u1

---

#### 🟠 [HIGH] CVE-2018-20843 – expat: large number of colons in input makes parser consume high amount of resources, leading to DoS

| Campo | Valor |
|---|---|
| **ID** | `TRI-F9715E25` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** In libexpat in Expat before 2.2.7, XML input including XML names that contain a large number of colons could make the XML parser consume a high amount of RAM and CPU resources while processing (enough to be usable for denial-of-service attacks).

**Evidencia:** `Paquete: libexpat1 v2.2.0-2+deb9u1 | Fix: 2.2.0-2+deb9u2`

**✅ Remediación:** Actualizar libexpat1 de 2.2.0-2+deb9u1 a 2.2.0-2+deb9u2

---

#### 🟠 [HIGH] CVE-2019-15903 – expat: heap-based buffer over-read via crafted XML input

| Campo | Valor |
|---|---|
| **ID** | `TRI-99FDBFAF` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** In libexpat before 2.2.8, crafted XML input could fool the parser into changing from DTD parsing to document parsing too early; a consecutive call to XML_GetCurrentLineNumber (or XML_GetCurrentColumnNumber) then resulted in a heap-based buffer over-read.

**Evidencia:** `Paquete: libexpat1 v2.2.0-2+deb9u1 | Fix: 2.2.0-2+deb9u3`

**✅ Remediación:** Actualizar libexpat1 de 2.2.0-2+deb9u1 a 2.2.0-2+deb9u3

---

#### 🟠 [HIGH] CVE-2021-45960 – expat: Large number of prefixed XML attributes on a single tag can crash libexpat

| Campo | Valor |
|---|---|
| **ID** | `TRI-B3AB98C9` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `8.8` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** In Expat (aka libexpat) before 2.4.3, a left shift by 29 (or more) places in the storeAtts function in xmlparse.c can lead to realloc misbehavior (e.g., allocating too few bytes, or only freeing memory).

**Evidencia:** `Paquete: libexpat1 v2.2.0-2+deb9u1 | Fix: 2.2.0-2+deb9u4`

**✅ Remediación:** Actualizar libexpat1 de 2.2.0-2+deb9u1 a 2.2.0-2+deb9u4

---

#### 🟠 [HIGH] CVE-2021-46143 – expat: Integer overflow in doProlog in xmlparse.c

| Campo | Valor |
|---|---|
| **ID** | `TRI-7B581427` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.8` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** In doProlog in xmlparse.c in Expat (aka libexpat) before 2.4.3, an integer overflow exists for m_groupSize.

**Evidencia:** `Paquete: libexpat1 v2.2.0-2+deb9u1 | Fix: 2.2.0-2+deb9u4`

**✅ Remediación:** Actualizar libexpat1 de 2.2.0-2+deb9u1 a 2.2.0-2+deb9u4

---

#### 🟠 [HIGH] CVE-2022-22825 – expat: Integer overflow in lookup in xmlparse.c

| Campo | Valor |
|---|---|
| **ID** | `TRI-80050EC6` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `8.8` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** lookup in xmlparse.c in Expat (aka libexpat) before 2.4.3 has an integer overflow.

**Evidencia:** `Paquete: libexpat1 v2.2.0-2+deb9u1 | Fix: 2.2.0-2+deb9u4`

**✅ Remediación:** Actualizar libexpat1 de 2.2.0-2+deb9u1 a 2.2.0-2+deb9u4

---

#### 🟠 [HIGH] CVE-2022-22826 – expat: Integer overflow in nextScaffoldPart in xmlparse.c

| Campo | Valor |
|---|---|
| **ID** | `TRI-0127A2A8` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `8.8` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** nextScaffoldPart in xmlparse.c in Expat (aka libexpat) before 2.4.3 has an integer overflow.

**Evidencia:** `Paquete: libexpat1 v2.2.0-2+deb9u1 | Fix: 2.2.0-2+deb9u4`

**✅ Remediación:** Actualizar libexpat1 de 2.2.0-2+deb9u1 a 2.2.0-2+deb9u4

---

#### 🟠 [HIGH] CVE-2022-22827 – expat: Integer overflow in storeAtts in xmlparse.c

| Campo | Valor |
|---|---|
| **ID** | `TRI-5CB318BA` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `8.8` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** storeAtts in xmlparse.c in Expat (aka libexpat) before 2.4.3 has an integer overflow.

**Evidencia:** `Paquete: libexpat1 v2.2.0-2+deb9u1 | Fix: 2.2.0-2+deb9u4`

**✅ Remediación:** Actualizar libexpat1 de 2.2.0-2+deb9u1 a 2.2.0-2+deb9u4

---

#### 🟠 [HIGH] CVE-2022-23990 – expat: integer overflow in the doProlog function

| Campo | Valor |
|---|---|
| **ID** | `TRI-C9CCF573` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** Expat (aka libexpat) before 2.4.4 has an integer overflow in the doProlog function.

**Evidencia:** `Paquete: libexpat1 v2.2.0-2+deb9u1 | Fix: 2.2.0-2+deb9u4`

**✅ Remediación:** Actualizar libexpat1 de 2.2.0-2+deb9u1 a 2.2.0-2+deb9u4

---

#### 🟠 [HIGH] CVE-2022-27405 – FreeType: Segmentation violation via FNT_Size_Request

| Campo | Valor |
|---|---|
| **ID** | `TRI-9D005565` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** FreeType commit 53dfdcd8198d2b3201a23c4bad9190519ba918db was discovered to contain a segmentation violation via the function FNT_Size_Request.

**Evidencia:** `Paquete: libfreetype6 v2.6.3-3.2 | Fix: Not available`

**✅ Remediación:** No hay fix disponible para libfreetype6 2.6.3-3.2 — considerar alternativa

---

#### 🟠 [HIGH] CVE-2022-27406 – Freetype: Segmentation violation via FT_Request_Size

| Campo | Valor |
|---|---|
| **ID** | `TRI-47934A2E` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** FreeType commit 22a0cccb4d9d002f33c1ba7a4b36812c7d4f46b5 was discovered to contain a segmentation violation via the function FT_Request_Size.

**Evidencia:** `Paquete: libfreetype6 v2.6.3-3.2 | Fix: Not available`

**✅ Remediación:** No hay fix disponible para libfreetype6 2.6.3-3.2 — considerar alternativa

---

#### 🟠 [HIGH] CVE-2021-33560 – libgcrypt: mishandles ElGamal encryption because it lacks exponent blinding to address a side-channel attack against mpi_powm

| Campo | Valor |
|---|---|
| **ID** | `TRI-0BE4287C` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** Libgcrypt before 1.8.8 and 1.9.x before 1.9.3 mishandles ElGamal encryption because it lacks exponent blinding to address a side-channel attack against mpi_powm, and the window size is not chosen appropriately. This, for example, affects use of ElGamal in OpenPGP.

**Evidencia:** `Paquete: libgcrypt20 v1.7.6-2+deb9u3 | Fix: Not available`

**✅ Remediación:** No hay fix disponible para libgcrypt20 1.7.6-2+deb9u3 — considerar alternativa

---

#### 🟠 [HIGH] CVE-2017-6363 – In the GD Graphics Library (aka LibGD) through 2.2.5, there is a heap- ...

| Campo | Valor |
|---|---|
| **ID** | `TRI-66BFB889` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `8.1` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** In the GD Graphics Library (aka LibGD) through 2.2.5, there is a heap-based buffer over-read in tiffWriter in gd_tiff.c. NOTE: the vendor says "In my opinion this issue should not have a CVE, since the GD and GD2 formats are documented to be 'obsolete, and should only be used for development and testing purposes.'

**Evidencia:** `Paquete: libgd3 v2.2.4-2+deb9u2 | Fix: Not available`

**✅ Remediación:** No hay fix disponible para libgd3 2.2.4-2+deb9u2 — considerar alternativa

---

#### 🟠 [HIGH] CVE-2019-6977 – gd: Heap-based buffer overflow in gdImageColorMatch() in gd_color_match.c

| Campo | Valor |
|---|---|
| **ID** | `TRI-21E4CA45` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `8.8` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** gdImageColorMatch in gd_color_match.c in the GD Graphics Library (aka LibGD) 2.2.5, as used in the imagecolormatch function in PHP before 5.6.40, 7.x before 7.1.26, 7.2.x before 7.2.14, and 7.3.x before 7.3.1, has a heap-based buffer overflow. This can be exploited by an attacker who is able to trigger imagecolormatch calls with crafted image data.

**Evidencia:** `Paquete: libgd3 v2.2.4-2+deb9u2 | Fix: 2.2.4-2+deb9u4`

**✅ Remediación:** Actualizar libgd3 de 2.2.4-2+deb9u2 a 2.2.4-2+deb9u4

---

#### 🟠 [HIGH] CVE-2021-43618 – gmp: Integer overflow and resultant buffer overflow via crafted input

| Campo | Valor |
|---|---|
| **ID** | `TRI-51B84646` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** GNU Multiple Precision Arithmetic Library (GMP) through 6.2.1 has an mpz/inp_raw.c integer overflow and resultant buffer overflow via crafted input, leading to a segmentation fault on 32-bit platforms.

**Evidencia:** `Paquete: libgmp10 v2:6.1.2+dfsg-1 | Fix: 2:6.1.2+dfsg-1+deb9u1`

**✅ Remediación:** Actualizar libgmp10 de 2:6.1.2+dfsg-1 a 2:6.1.2+dfsg-1+deb9u1

---

#### 🟠 [HIGH] CVE-2019-3829 – gnutls: use-after-free/double-free in certificate verification

| Campo | Valor |
|---|---|
| **ID** | `TRI-89AF7064` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** A vulnerability was found in gnutls versions from 3.5.8 before 3.6.7. A memory corruption (double free) vulnerability in the certificate verification API. Any client or server application that verifies X.509 certificates with GnuTLS 3.5.8 or later is affected.

**Evidencia:** `Paquete: libgnutls30 v3.5.8-5+deb9u3 | Fix: 3.5.8-5+deb9u5`

**✅ Remediación:** Actualizar libgnutls30 de 3.5.8-5+deb9u3 a 3.5.8-5+deb9u5

---

#### 🟠 [HIGH] CVE-2021-20305 – nettle: Out of bounds memory access in signature verification

| Campo | Valor |
|---|---|
| **ID** | `TRI-286CDA3A` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `8.1` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** A flaw was found in Nettle in versions before 3.7.2, where several Nettle signature verification functions (GOST DSA, EDDSA & ECDSA) result in the Elliptic Curve Cryptography point (ECC) multiply function being called with out-of-range scalers, possibly resulting in incorrect results. This flaw allows an attacker to force an invalid signature, causing an assertion failure or possible validation. T

**Evidencia:** `Paquete: libhogweed4 v3.3-1+b2 | Fix: 3.3-1+deb9u1`

**✅ Remediación:** Actualizar libhogweed4 de 3.3-1+b2 a 3.3-1+deb9u1

---

#### 🟠 [HIGH] CVE-2021-3580 – nettle: Remote crash in RSA decryption via manipulated ciphertext

| Campo | Valor |
|---|---|
| **ID** | `TRI-AE6313BA` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** A flaw was found in the way nettle's RSA decryption functions handled specially crafted ciphertext. An attacker could use this flaw to provide a manipulated ciphertext leading to application crash and denial of service.

**Evidencia:** `Paquete: libhogweed4 v3.3-1+b2 | Fix: 3.3-1+deb9u1`

**✅ Remediación:** Actualizar libhogweed4 de 3.3-1+b2 a 3.3-1+deb9u1

---

#### 🟠 [HIGH] CVE-2020-10531 – ICU: Integer overflow in UnicodeString::doAppend()

| Campo | Valor |
|---|---|
| **ID** | `TRI-C54FC55F` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `8.8` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** An issue was discovered in International Components for Unicode (ICU) for C/C++ through 66.1. An integer overflow, leading to a heap-based buffer overflow, exists in the UnicodeString::doAppend() function in common/unistr.cpp.

**Evidencia:** `Paquete: libicu57 v57.1-6+deb9u2 | Fix: 57.1-6+deb9u4`

**✅ Remediación:** Actualizar libicu57 de 57.1-6+deb9u2 a 57.1-6+deb9u4

---

#### 🟠 [HIGH] CVE-2019-2201 – libjpeg-turbo: several integer overflows and subsequent segfaults when attempting to compress/decompress gigapixel images

| Campo | Valor |
|---|---|
| **ID** | `TRI-868AB41C` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.8` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** In generate_jsimd_ycc_rgb_convert_neon of jsimd_arm64_neon.S, there is a possible out of bounds write due to a missing bounds check. This could lead to remote code execution in an unprivileged process with no additional execution privileges needed. User interaction is needed for exploitation.Product: AndroidVersions: Android-8.0 Android-8.1 Android-9 Android-10Android ID: A-120551338

**Evidencia:** `Paquete: libjpeg62-turbo v1:1.5.1-2 | Fix: 1:1.5.1-2+deb9u2`

**✅ Remediación:** Actualizar libjpeg62-turbo de 1:1.5.1-2 a 1:1.5.1-2+deb9u2

---

#### 🟠 [HIGH] CVE-2020-13790 – libjpeg-turbo: heap-based buffer over-read in get_rgb_row() in rdppm.c

| Campo | Valor |
|---|---|
| **ID** | `TRI-06E13880` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `8.1` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** libjpeg-turbo 2.0.4, and mozjpeg 4.0.0, has a heap-based buffer over-read in get_rgb_row() in rdppm.c via a malformed PPM input file.

**Evidencia:** `Paquete: libjpeg62-turbo v1:1.5.1-2 | Fix: 1:1.5.1-2+deb9u1`

**✅ Remediación:** Actualizar libjpeg62-turbo de 1:1.5.1-2 a 1:1.5.1-2+deb9u1

---

#### 🟠 [HIGH] CVE-2020-14152 – libjpeg: improper handling of max_memory_to_use setting can lead to excessive memory consumption

| Campo | Valor |
|---|---|
| **ID** | `TRI-FCC31F78` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.1` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** In IJG JPEG (aka libjpeg) before 9d, jpeg_mem_available() in jmemnobs.c in djpeg does not honor the max_memory_to_use setting, possibly causing excessive memory consumption.

**Evidencia:** `Paquete: libjpeg62-turbo v1:1.5.1-2 | Fix: 1:1.5.1-2+deb9u1`

**✅ Remediación:** Actualizar libjpeg62-turbo de 1:1.5.1-2 a 1:1.5.1-2+deb9u1

---

#### 🟠 [HIGH] CVE-2020-12243 – openldap: denial of service via nested boolean expressions in LDAP search filters

| Campo | Valor |
|---|---|
| **ID** | `TRI-D46887BF` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** In filter.c in slapd in OpenLDAP before 2.4.50, LDAP search filters with nested boolean expressions can result in denial of service (daemon crash).

**Evidencia:** `Paquete: libldap-2.4-2 v2.4.44+dfsg-5+deb9u2 | Fix: 2.4.44+dfsg-5+deb9u4`

**✅ Remediación:** Actualizar libldap-2.4-2 de 2.4.44+dfsg-5+deb9u2 a 2.4.44+dfsg-5+deb9u4

---

#### 🟠 [HIGH] CVE-2020-25692 – openldap: NULL pointer dereference for unauthenticated packet in slapd

| Campo | Valor |
|---|---|
| **ID** | `TRI-8D4DD7D8` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** A NULL pointer dereference was found in OpenLDAP server and was fixed in openldap 2.4.55, during a request for renaming RDNs. An unauthenticated attacker could remotely crash the slapd process by sending a specially crafted request, causing a Denial of Service.

**Evidencia:** `Paquete: libldap-2.4-2 v2.4.44+dfsg-5+deb9u2 | Fix: 2.4.44+dfsg-5+deb9u5`

**✅ Remediación:** Actualizar libldap-2.4-2 de 2.4.44+dfsg-5+deb9u2 a 2.4.44+dfsg-5+deb9u5

---

#### 🟠 [HIGH] CVE-2020-25709 – openldap: assertion failure in Certificate List syntax validation

| Campo | Valor |
|---|---|
| **ID** | `TRI-BABEC741` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** A flaw was found in OpenLDAP. This flaw allows an attacker who can send a malicious packet to be processed by OpenLDAP’s slapd server, to trigger an assertion failure. The highest threat from this vulnerability is to system availability.

**Evidencia:** `Paquete: libldap-2.4-2 v2.4.44+dfsg-5+deb9u2 | Fix: 2.4.44+dfsg-5+deb9u6`

**✅ Remediación:** Actualizar libldap-2.4-2 de 2.4.44+dfsg-5+deb9u2 a 2.4.44+dfsg-5+deb9u6

---

#### 🟠 [HIGH] CVE-2020-25710 – openldap: assertion failure in CSN normalization with invalid input

| Campo | Valor |
|---|---|
| **ID** | `TRI-06548932` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** A flaw was found in OpenLDAP in versions before 2.4.56. This flaw allows an attacker who sends a malicious packet processed by OpenLDAP to force a failed assertion in csnNormalize23(). The highest threat from this vulnerability is to system availability.

**Evidencia:** `Paquete: libldap-2.4-2 v2.4.44+dfsg-5+deb9u2 | Fix: 2.4.44+dfsg-5+deb9u6`

**✅ Remediación:** Actualizar libldap-2.4-2 de 2.4.44+dfsg-5+deb9u2 a 2.4.44+dfsg-5+deb9u6

---

#### 🟠 [HIGH] CVE-2020-36221 – openldap: Integer underflow in serialNumberAndIssuerCheck in schema_init.c

| Campo | Valor |
|---|---|
| **ID** | `TRI-B67C7C26` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** An integer underflow was discovered in OpenLDAP before 2.4.57 leading to slapd crashes in the Certificate Exact Assertion processing, resulting in denial of service (schema_init.c serialNumberAndIssuerCheck).

**Evidencia:** `Paquete: libldap-2.4-2 v2.4.44+dfsg-5+deb9u2 | Fix: 2.4.44+dfsg-5+deb9u7`

**✅ Remediación:** Actualizar libldap-2.4-2 de 2.4.44+dfsg-5+deb9u2 a 2.4.44+dfsg-5+deb9u7

---

#### 🟠 [HIGH] CVE-2020-36222 – openldap: Assertion failure in slapd in the saslAuthzTo validation

| Campo | Valor |
|---|---|
| **ID** | `TRI-6C90F885` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** A flaw was discovered in OpenLDAP before 2.4.57 leading to an assertion failure in slapd in the saslAuthzTo validation, resulting in denial of service.

**Evidencia:** `Paquete: libldap-2.4-2 v2.4.44+dfsg-5+deb9u2 | Fix: 2.4.44+dfsg-5+deb9u7`

**✅ Remediación:** Actualizar libldap-2.4-2 de 2.4.44+dfsg-5+deb9u2 a 2.4.44+dfsg-5+deb9u7

---

#### 🟠 [HIGH] CVE-2020-36223 – openldap: Out-of-bounds read in Values Return Filter

| Campo | Valor |
|---|---|
| **ID** | `TRI-6A096CE5` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** A flaw was discovered in OpenLDAP before 2.4.57 leading to a slapd crash in the Values Return Filter control handling, resulting in denial of service (double free and out-of-bounds read).

**Evidencia:** `Paquete: libldap-2.4-2 v2.4.44+dfsg-5+deb9u2 | Fix: 2.4.44+dfsg-5+deb9u7`

**✅ Remediación:** Actualizar libldap-2.4-2 de 2.4.44+dfsg-5+deb9u2 a 2.4.44+dfsg-5+deb9u7

---

#### 🟠 [HIGH] CVE-2020-36224 – openldap: Invalid pointer free in the saslAuthzTo processing

| Campo | Valor |
|---|---|
| **ID** | `TRI-24ECE788` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** A flaw was discovered in OpenLDAP before 2.4.57 leading to an invalid pointer free and slapd crash in the saslAuthzTo processing, resulting in denial of service.

**Evidencia:** `Paquete: libldap-2.4-2 v2.4.44+dfsg-5+deb9u2 | Fix: 2.4.44+dfsg-5+deb9u7`

**✅ Remediación:** Actualizar libldap-2.4-2 de 2.4.44+dfsg-5+deb9u2 a 2.4.44+dfsg-5+deb9u7

---

#### 🟠 [HIGH] CVE-2020-36225 – openldap: Double free in the saslAuthzTo processing

| Campo | Valor |
|---|---|
| **ID** | `TRI-DCCD1F70` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** A flaw was discovered in OpenLDAP before 2.4.57 leading to a double free and slapd crash in the saslAuthzTo processing, resulting in denial of service.

**Evidencia:** `Paquete: libldap-2.4-2 v2.4.44+dfsg-5+deb9u2 | Fix: 2.4.44+dfsg-5+deb9u7`

**✅ Remediación:** Actualizar libldap-2.4-2 de 2.4.44+dfsg-5+deb9u2 a 2.4.44+dfsg-5+deb9u7

---

#### 🟠 [HIGH] CVE-2020-36226 – openldap: Denial of service via length miscalculation in slap_parse_user

| Campo | Valor |
|---|---|
| **ID** | `TRI-7142B9C9` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** A flaw was discovered in OpenLDAP before 2.4.57 leading to a memch->bv_len miscalculation and slapd crash in the saslAuthzTo processing, resulting in denial of service.

**Evidencia:** `Paquete: libldap-2.4-2 v2.4.44+dfsg-5+deb9u2 | Fix: 2.4.44+dfsg-5+deb9u7`

**✅ Remediación:** Actualizar libldap-2.4-2 de 2.4.44+dfsg-5+deb9u2 a 2.4.44+dfsg-5+deb9u7

---

#### 🟠 [HIGH] CVE-2020-36227 – openldap: Infinite loop in slapd with the cancel_extop Cancel operation

| Campo | Valor |
|---|---|
| **ID** | `TRI-57D720B7` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** A flaw was discovered in OpenLDAP before 2.4.57 leading to an infinite loop in slapd with the cancel_extop Cancel operation, resulting in denial of service.

**Evidencia:** `Paquete: libldap-2.4-2 v2.4.44+dfsg-5+deb9u2 | Fix: 2.4.44+dfsg-5+deb9u7`

**✅ Remediación:** Actualizar libldap-2.4-2 de 2.4.44+dfsg-5+deb9u2 a 2.4.44+dfsg-5+deb9u7

---

#### 🟠 [HIGH] CVE-2020-36228 – openldap: Integer underflow in issuerAndThisUpdateCheck in schema_init.c

| Campo | Valor |
|---|---|
| **ID** | `TRI-786BA1EB` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** An integer underflow was discovered in OpenLDAP before 2.4.57 leading to a slapd crash in the Certificate List Exact Assertion processing, resulting in denial of service.

**Evidencia:** `Paquete: libldap-2.4-2 v2.4.44+dfsg-5+deb9u2 | Fix: 2.4.44+dfsg-5+deb9u7`

**✅ Remediación:** Actualizar libldap-2.4-2 de 2.4.44+dfsg-5+deb9u2 a 2.4.44+dfsg-5+deb9u7

---

#### 🟠 [HIGH] CVE-2020-36229 – openldap: Type confusion in ad_keystring in ad.c

| Campo | Valor |
|---|---|
| **ID** | `TRI-F0D5FDD5` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** A flaw was discovered in ldap_X509dn2bv in OpenLDAP before 2.4.57 leading to a slapd crash in the X.509 DN parsing in ad_keystring, resulting in denial of service.

**Evidencia:** `Paquete: libldap-2.4-2 v2.4.44+dfsg-5+deb9u2 | Fix: 2.4.44+dfsg-5+deb9u7`

**✅ Remediación:** Actualizar libldap-2.4-2 de 2.4.44+dfsg-5+deb9u2 a 2.4.44+dfsg-5+deb9u7

---

#### 🟠 [HIGH] CVE-2020-36230 – openldap: Assertion failure in ber_next_element in decode.c

| Campo | Valor |
|---|---|
| **ID** | `TRI-52A018F6` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** A flaw was discovered in OpenLDAP before 2.4.57 leading in an assertion failure in slapd in the X.509 DN parsing in decode.c ber_next_element, resulting in denial of service.

**Evidencia:** `Paquete: libldap-2.4-2 v2.4.44+dfsg-5+deb9u2 | Fix: 2.4.44+dfsg-5+deb9u7`

**✅ Remediación:** Actualizar libldap-2.4-2 de 2.4.44+dfsg-5+deb9u2 a 2.4.44+dfsg-5+deb9u7

---

#### 🟠 [HIGH] CVE-2021-27212 – openldap: Assertion failure in slapd in the issuerAndThisUpdateCheck function

| Campo | Valor |
|---|---|
| **ID** | `TRI-95EE3D08` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** In OpenLDAP through 2.4.57 and 2.5.x through 2.5.1alpha, an assertion failure in slapd can occur in the issuerAndThisUpdateCheck function via a crafted packet, resulting in a denial of service (daemon exit) via a short timestamp. This is related to schema_init.c and checkTime.

**Evidencia:** `Paquete: libldap-2.4-2 v2.4.44+dfsg-5+deb9u2 | Fix: 2.4.44+dfsg-5+deb9u8`

**✅ Remediación:** Actualizar libldap-2.4-2 de 2.4.44+dfsg-5+deb9u2 a 2.4.44+dfsg-5+deb9u8

---

#### 🟠 [HIGH] CVE-2017-15365 – mariadb: Replication in sql/event_data_objects.cc occurs before ACL checks

| Campo | Valor |
|---|---|
| **ID** | `TRI-614608DA` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `8.8` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** sql/event_data_objects.cc in MariaDB before 10.1.30 and 10.2.x before 10.2.10 and Percona XtraDB Cluster before 5.6.37-26.21-3 and 5.7.x before 5.7.19-29.22-3 allows remote authenticated users with SQL access to bypass intended access restrictions and replicate data definition language (DDL) statements to cluster nodes by leveraging incorrect ordering of DDL replication and ACL checking.

**Evidencia:** `Paquete: libmariadbclient18 v10.1.26-0+deb9u1 | Fix: 10.1.37-0+deb9u1`

**✅ Remediación:** Actualizar libmariadbclient18 de 10.1.26-0+deb9u1 a 10.1.37-0+deb9u1

---

#### 🟠 [HIGH] CVE-2018-2562 – mysql: Server: Partition unspecified vulnerability (CPU Jan 2018)

| Campo | Valor |
|---|---|
| **ID** | `TRI-681F62B7` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.1` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** Vulnerability in the MySQL Server component of Oracle MySQL (subcomponent: Server : Partition). Supported versions that are affected are 5.5.58 and prior, 5.6.38 and prior and 5.7.19 and prior. Easily exploitable vulnerability allows low privileged attacker with network access via multiple protocols to compromise MySQL Server. Successful attacks of this vulnerability can result in unauthorized abi

**Evidencia:** `Paquete: libmariadbclient18 v10.1.26-0+deb9u1 | Fix: 10.1.37-0+deb9u1`

**✅ Remediación:** Actualizar libmariadbclient18 de 10.1.26-0+deb9u1 a 10.1.37-0+deb9u1

---

#### 🟠 [HIGH] CVE-2018-2755 – mysql: Server: Replication unspecified vulnerability (CPU Apr 2018)

| Campo | Valor |
|---|---|
| **ID** | `TRI-BBC981CC` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.7` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** Vulnerability in the MySQL Server component of Oracle MySQL (subcomponent: Server: Replication). Supported versions that are affected are 5.5.59 and prior, 5.6.39 and prior and 5.7.21 and prior. Difficult to exploit vulnerability allows unauthenticated attacker with logon to the infrastructure where MySQL Server executes to compromise MySQL Server. Successful attacks require human interaction from

**Evidencia:** `Paquete: libmariadbclient18 v10.1.26-0+deb9u1 | Fix: 10.1.37-0+deb9u1`

**✅ Remediación:** Actualizar libmariadbclient18 de 10.1.26-0+deb9u1 a 10.1.37-0+deb9u1

---

#### 🟠 [HIGH] CVE-2018-3064 – mysql: InnoDB unspecified vulnerability (CPU Jul 2018)

| Campo | Valor |
|---|---|
| **ID** | `TRI-995775C6` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.1` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** Vulnerability in the MySQL Server component of Oracle MySQL (subcomponent: InnoDB). Supported versions that are affected are 5.6.40 and prior, 5.7.22 and prior and 8.0.11 and prior. Easily exploitable vulnerability allows low privileged attacker with network access via multiple protocols to compromise MySQL Server. Successful attacks of this vulnerability can result in unauthorized ability to caus

**Evidencia:** `Paquete: libmariadbclient18 v10.1.26-0+deb9u1 | Fix: 10.1.37-0+deb9u1`

**✅ Remediación:** Actualizar libmariadbclient18 de 10.1.26-0+deb9u1 a 10.1.37-0+deb9u1

---

#### 🟠 [HIGH] CVE-2021-27928 – mariadb: writable system variables allows a database user with SUPER privilege to execute arbitrary code as the system mysql user

| Campo | Valor |
|---|---|
| **ID** | `TRI-C5A7D387` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.2` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** A remote code execution issue was discovered in MariaDB 10.2 before 10.2.37, 10.3 before 10.3.28, 10.4 before 10.4.18, and 10.5 before 10.5.9; Percona Server through 2021-03-03; and the wsrep patch through 2021-03-03 for MySQL. An untrusted search path leads to eval injection, in which a database SUPER user can execute OS commands after modifying wsrep_provider and wsrep_notify_cmd. NOTE: this doe

**Evidencia:** `Paquete: libmariadbclient18 v10.1.26-0+deb9u1 | Fix: 10.1.48-0+deb9u2`

**✅ Remediación:** Actualizar libmariadbclient18 de 10.1.26-0+deb9u1 a 10.1.48-0+deb9u2

---

#### 🟠 [HIGH] CVE-2022-29458 – ncurses: segfaulting OOB read

| Campo | Valor |
|---|---|
| **ID** | `TRI-435586A0` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.1` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** ncurses 6.3 before patch 20220416 has an out-of-bounds read and segmentation violation in convert_strings in tinfo/read_entry.c in the terminfo library.

**Evidencia:** `Paquete: libncurses5 v6.0+20161126-1+deb9u2 | Fix: Not available`

**✅ Remediación:** No hay fix disponible para libncurses5 6.0+20161126-1+deb9u2 — considerar alternativa

---

#### 🟠 [HIGH] CVE-2018-1000168 – nghttp2: Null pointer dereference when too large ALTSVC frame is received

| Campo | Valor |
|---|---|
| **ID** | `TRI-877A32F0` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** nghttp2 version >= 1.10.0 and nghttp2 <= v1.31.0 contains an Improper Input Validation CWE-20 vulnerability in ALTSVC frame handling that can result in segmentation fault leading to denial of service. This attack appears to be exploitable via network client. This vulnerability appears to have been fixed in >= 1.31.1.

**Evidencia:** `Paquete: libnghttp2-14 v1.18.1-1 | Fix: 1.18.1-1+deb9u2`

**✅ Remediación:** Actualizar libnghttp2-14 de 1.18.1-1 a 1.18.1-1+deb9u2

---

#### 🟠 [HIGH] CVE-2019-9511 – HTTP/2: large amount of data requests leads to denial of service

| Campo | Valor |
|---|---|
| **ID** | `TRI-48ABBADF` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** Some HTTP/2 implementations are vulnerable to window size manipulation and stream prioritization manipulation, potentially leading to a denial of service. The attacker requests a large amount of data from a specified resource over multiple streams. They manipulate window size and stream priority to force the server to queue the data in 1-byte chunks. Depending on how efficiently this data is queue

**Evidencia:** `Paquete: libnghttp2-14 v1.18.1-1 | Fix: 1.18.1-1+deb9u1`

**✅ Remediación:** Actualizar libnghttp2-14 de 1.18.1-1 a 1.18.1-1+deb9u1

---

#### 🟠 [HIGH] CVE-2019-9513 – HTTP/2: flood using PRIORITY frames results in excessive resource consumption

| Campo | Valor |
|---|---|
| **ID** | `TRI-8D72DDCC` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** Some HTTP/2 implementations are vulnerable to resource loops, potentially leading to a denial of service. The attacker creates multiple request streams and continually shuffles the priority of the streams in a way that causes substantial churn to the priority tree. This can consume excess CPU.

**Evidencia:** `Paquete: libnghttp2-14 v1.18.1-1 | Fix: 1.18.1-1+deb9u1`

**✅ Remediación:** Actualizar libnghttp2-14 de 1.18.1-1 a 1.18.1-1+deb9u1

---

#### 🟠 [HIGH] CVE-2020-11080 – nghttp2: overly large SETTINGS frames can lead to DoS

| Campo | Valor |
|---|---|
| **ID** | `TRI-65102346` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** In nghttp2 before version 1.41.0, the overly large HTTP/2 SETTINGS frame payload causes denial of service. The proof of concept attack involves a malicious client constructing a SETTINGS frame with a length of 14,400 bytes (2400 individual settings entries) over and over again. The attack causes the CPU to spike at 100%. nghttp2 v1.41.0 fixes this vulnerability. There is a workaround to this vulne

**Evidencia:** `Paquete: libnghttp2-14 v1.18.1-1 | Fix: 1.18.1-1+deb9u2`

**✅ Remediación:** Actualizar libnghttp2-14 de 1.18.1-1 a 1.18.1-1+deb9u2

---

#### 🟠 [HIGH] CVE-2020-29361 – p11-kit: integer overflow when allocating memory for arrays or attributes and object identifiers

| Campo | Valor |
|---|---|
| **ID** | `TRI-99304057` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** An issue was discovered in p11-kit 0.21.1 through 0.23.21. Multiple integer overflows have been discovered in the array allocations in the p11-kit library and the p11-kit list command, where overflow checks are missing before calling realloc or calloc.

**Evidencia:** `Paquete: libp11-kit0 v0.23.3-2 | Fix: 0.23.3-2+deb9u1`

**✅ Remediación:** Actualizar libp11-kit0 de 0.23.3-2 a 0.23.3-2+deb9u1

---

#### 🟠 [HIGH] CVE-2020-10543 – perl: heap-based buffer overflow in regular expression compiler leads to DoS

| Campo | Valor |
|---|---|
| **ID** | `TRI-C9632C61` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `8.2` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** Perl before 5.30.3 on 32-bit platforms allows a heap-based buffer overflow because nested regular expression quantifiers have an integer overflow.

**Evidencia:** `Paquete: libperl5.24 v5.24.1-3+deb9u4 | Fix: 5.24.1-3+deb9u7`

**✅ Remediación:** Actualizar libperl5.24 de 5.24.1-3+deb9u4 a 5.24.1-3+deb9u7

---

#### 🟠 [HIGH] CVE-2020-10878 – perl: corruption of intermediate language state of compiled regular expression due to integer overflow leads to DoS

| Campo | Valor |
|---|---|
| **ID** | `TRI-8FCF1412` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `8.6` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** Perl before 5.30.3 has an integer overflow related to mishandling of a "PL_regkind[OP(n)] == NOTHING" situation. A crafted regular expression could lead to malformed bytecode with a possibility of instruction injection.

**Evidencia:** `Paquete: libperl5.24 v5.24.1-3+deb9u4 | Fix: 5.24.1-3+deb9u7`

**✅ Remediación:** Actualizar libperl5.24 de 5.24.1-3+deb9u4 a 5.24.1-3+deb9u7

---

#### 🟠 [HIGH] CVE-2020-12723 – perl: corruption of intermediate language state of compiled regular expression due to recursive S_study_chunk() calls leads to DoS

| Campo | Valor |
|---|---|
| **ID** | `TRI-54B52AD4` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** regcomp.c in Perl before 5.30.3 allows a buffer overflow via a crafted regular expression because of recursive S_study_chunk calls.

**Evidencia:** `Paquete: libperl5.24 v5.24.1-3+deb9u4 | Fix: 5.24.1-3+deb9u7`

**✅ Remediación:** Actualizar libperl5.24 de 5.24.1-3+deb9u4 a 5.24.1-3+deb9u7

---

#### 🟠 [HIGH] CVE-2020-16156 – perl-CPAN: Bypass of verification of signatures in CHECKSUMS files

| Campo | Valor |
|---|---|
| **ID** | `TRI-87F3FAD8` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.8` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** CPAN 2.28 allows Signature Verification Bypass.

**Evidencia:** `Paquete: libperl5.24 v5.24.1-3+deb9u4 | Fix: Not available`

**✅ Remediación:** No hay fix disponible para libperl5.24 5.24.1-3+deb9u4 — considerar alternativa

---

#### 🟠 [HIGH] CVE-2019-10208 – postgresql: TYPE in pg_temp executes arbitrary SQL during SECURITY DEFINER execution

| Campo | Valor |
|---|---|
| **ID** | `TRI-BD87E7EC` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `8.8` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** A flaw was discovered in postgresql versions 9.4.x before 9.4.24, 9.5.x before 9.5.19, 9.6.x before 9.6.15, 10.x before 10.10 and 11.x before 11.5 where arbitrary SQL statements can be executed given a suitable SECURITY DEFINER function. An attacker, with EXECUTE permission on the function, can execute arbitrary SQL as the owner of the function.

**Evidencia:** `Paquete: libpq5 v9.6.10-0+deb9u1 | Fix: 9.6.15-0+deb9u1`

**✅ Remediación:** Actualizar libpq5 de 9.6.10-0+deb9u1 a 9.6.15-0+deb9u1

---

#### 🟠 [HIGH] CVE-2020-14350 – postgresql: Uncontrolled search path element in CREATE EXTENSION

| Campo | Valor |
|---|---|
| **ID** | `TRI-15645ED6` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.3` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** It was found that some PostgreSQL extensions did not use search_path safely in their installation script. An attacker with sufficient privileges could use this flaw to trick an administrator into executing a specially crafted script, during the installation or update of such extension. This affects PostgreSQL versions before 12.4, before 11.9, before 10.14, before 9.6.19, and before 9.5.23.

**Evidencia:** `Paquete: libpq5 v9.6.10-0+deb9u1 | Fix: 9.6.19-0+deb9u1`

**✅ Remediación:** Actualizar libpq5 de 9.6.10-0+deb9u1 a 9.6.19-0+deb9u1

---

#### 🟠 [HIGH] CVE-2020-25694 – postgresql: Reconnection can downgrade connection security settings

| Campo | Valor |
|---|---|
| **ID** | `TRI-EE92E902` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `8.1` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** A flaw was found in PostgreSQL versions before 13.1, before 12.5, before 11.10, before 10.15, before 9.6.20 and before 9.5.24. If a client application that creates additional database connections only reuses the basic connection parameters while dropping security-relevant parameters, an opportunity for a man-in-the-middle attack, or the ability to observe clear-text transmissions, could exist. The

**Evidencia:** `Paquete: libpq5 v9.6.10-0+deb9u1 | Fix: 9.6.20-0+deb9u1`

**✅ Remediación:** Actualizar libpq5 de 9.6.10-0+deb9u1 a 9.6.20-0+deb9u1

---

#### 🟠 [HIGH] CVE-2020-25695 – postgresql: Multiple features escape "security restricted operation" sandbox

| Campo | Valor |
|---|---|
| **ID** | `TRI-177CC285` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `8.8` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** A flaw was found in PostgreSQL versions before 13.1, before 12.5, before 11.10, before 10.15, before 9.6.20 and before 9.5.24. An attacker having permission to create non-temporary objects in at least one schema can execute arbitrary SQL functions under the identity of a superuser. The highest threat from this vulnerability is to data confidentiality and integrity as well as system availability.

**Evidencia:** `Paquete: libpq5 v9.6.10-0+deb9u1 | Fix: 9.6.20-0+deb9u1`

**✅ Remediación:** Actualizar libpq5 de 9.6.10-0+deb9u1 a 9.6.20-0+deb9u1

---

#### 🟠 [HIGH] CVE-2020-25696 – postgresql: psql's \gset allows overwriting specially treated variables

| Campo | Valor |
|---|---|
| **ID** | `TRI-27E70E82` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** A flaw was found in the psql interactive terminal of PostgreSQL in versions before 13.1, before 12.5, before 11.10, before 10.15, before 9.6.20 and before 9.5.24. If an interactive psql session uses \gset when querying a compromised server, the attacker can execute arbitrary code as the operating system account running psql. The highest threat from this vulnerability is to data confidentiality and

**Evidencia:** `Paquete: libpq5 v9.6.10-0+deb9u1 | Fix: 9.6.20-0+deb9u1`

**✅ Remediación:** Actualizar libpq5 de 9.6.10-0+deb9u1 a 9.6.20-0+deb9u1

---

#### 🟠 [HIGH] CVE-2021-23214 – postgresql: server processes unencrypted bytes from man-in-the-middle

| Campo | Valor |
|---|---|
| **ID** | `TRI-BBD48923` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `8.1` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** When the server is configured to use trust authentication with a clientcert requirement or to use cert authentication, a man-in-the-middle attacker can inject arbitrary SQL queries when a connection is first established, despite the use of SSL certificate verification and encryption.

**Evidencia:** `Paquete: libpq5 v9.6.10-0+deb9u1 | Fix: 9.6.24-0+deb9u1`

**✅ Remediación:** Actualizar libpq5 de 9.6.10-0+deb9u1 a 9.6.24-0+deb9u1

---

#### 🟠 [HIGH] CVE-2021-32027 – postgresql: Buffer overrun from integer overflow in array subscripting calculations

| Campo | Valor |
|---|---|
| **ID** | `TRI-ADB2E9AE` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `8.8` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** A flaw was found in postgresql in versions before 13.3, before 12.7, before 11.12, before 10.17 and before 9.6.22. While modifying certain SQL array values, missing bounds checks let authenticated database users write arbitrary bytes to a wide area of server memory. The highest threat from this vulnerability is to data confidentiality and integrity as well as system availability.

**Evidencia:** `Paquete: libpq5 v9.6.10-0+deb9u1 | Fix: 9.6.22-0+deb9u1`

**✅ Remediación:** Actualizar libpq5 de 9.6.10-0+deb9u1 a 9.6.22-0+deb9u1

---

#### 🟠 [HIGH] CVE-2019-19906 – cyrus-sasl: denial of service in _sasl_add_string function

| Campo | Valor |
|---|---|
| **ID** | `TRI-6EA8428A` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** cyrus-sasl (aka Cyrus SASL) 2.1.27 has an out-of-bounds write leading to unauthenticated remote denial-of-service in OpenLDAP via a malformed LDAP packet. The OpenLDAP crash is ultimately caused by an off-by-one error in _sasl_add_string in common.c in cyrus-sasl.

**Evidencia:** `Paquete: libsasl2-2 v2.1.27~101-g0780600+dfsg-3 | Fix: 2.1.27~101-g0780600+dfsg-3+deb9u1`

**✅ Remediación:** Actualizar libsasl2-2 de 2.1.27~101-g0780600+dfsg-3 a 2.1.27~101-g0780600+dfsg-3+deb9u1

---

#### 🟠 [HIGH] CVE-2022-24407 – cyrus-sasl: failure to properly escape SQL input allows an attacker to execute arbitrary SQL commands

| Campo | Valor |
|---|---|
| **ID** | `TRI-39985621` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `8.8` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** In Cyrus SASL 2.1.17 through 2.1.27 before 2.1.28, plugins/sql.c does not escape the password for a SQL INSERT or UPDATE statement.

**Evidencia:** `Paquete: libsasl2-2 v2.1.27~101-g0780600+dfsg-3 | Fix: 2.1.27~101-g0780600+dfsg-3+deb9u2`

**✅ Remediación:** Actualizar libsasl2-2 de 2.1.27~101-g0780600+dfsg-3 a 2.1.27~101-g0780600+dfsg-3+deb9u2

---

#### 🟠 [HIGH] CVE-2018-20346 – sqlite: Multiple flaws in sqlite which can be triggered via corrupted internal databases (Magellan)

| Campo | Valor |
|---|---|
| **ID** | `TRI-CB8B2A15` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `8.1` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** SQLite before 3.25.3, when the FTS3 extension is enabled, encounters an integer overflow (and resultant buffer overflow) for FTS3 queries that occur after crafted changes to FTS3 shadow tables, allowing remote attackers to execute arbitrary code by leveraging the ability to run arbitrary SQL statements (such as in certain WebSQL use cases), aka Magellan.

**Evidencia:** `Paquete: libsqlite3-0 v3.16.2-5+deb9u1 | Fix: 3.16.2-5+deb9u2`

**✅ Remediación:** Actualizar libsqlite3-0 de 3.16.2-5+deb9u1 a 3.16.2-5+deb9u2

---

#### 🟠 [HIGH] CVE-2018-20506 – sqlite: Multiple flaws in sqlite which can be triggered via corrupted internal databases (Magellan)

| Campo | Valor |
|---|---|
| **ID** | `TRI-3967306B` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `8.1` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** SQLite before 3.25.3, when the FTS3 extension is enabled, encounters an integer overflow (and resultant buffer overflow) for FTS3 queries in a "merge" operation that occurs after crafted changes to FTS3 shadow tables, allowing remote attackers to execute arbitrary code by leveraging the ability to run arbitrary SQL statements (such as in certain WebSQL use cases). This is a different vulnerability

**Evidencia:** `Paquete: libsqlite3-0 v3.16.2-5+deb9u1 | Fix: 3.16.2-5+deb9u2`

**✅ Remediación:** Actualizar libsqlite3-0 de 3.16.2-5+deb9u1 a 3.16.2-5+deb9u2

---

#### 🟠 [HIGH] CVE-2018-8740 – sqlite: NULL pointer dereference with databases with schema corrupted with CREATE TABLE AS allows for denial of service

| Campo | Valor |
|---|---|
| **ID** | `TRI-2A07DD18` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** In SQLite through 3.22.0, databases whose schema is corrupted using a CREATE TABLE AS statement could cause a NULL pointer dereference, related to build.c and prepare.c.

**Evidencia:** `Paquete: libsqlite3-0 v3.16.2-5+deb9u1 | Fix: 3.16.2-5+deb9u2`

**✅ Remediación:** Actualizar libsqlite3-0 de 3.16.2-5+deb9u1 a 3.16.2-5+deb9u2

---

#### 🟠 [HIGH] CVE-2019-20218 – sqlite: selectExpander in select.c proceeds with WITH stack unwinding even after a parsing error

| Campo | Valor |
|---|---|
| **ID** | `TRI-2FAD3730` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** selectExpander in select.c in SQLite 3.30.1 proceeds with WITH stack unwinding even after a parsing error.

**Evidencia:** `Paquete: libsqlite3-0 v3.16.2-5+deb9u1 | Fix: 3.16.2-5+deb9u3`

**✅ Remediación:** Actualizar libsqlite3-0 de 3.16.2-5+deb9u1 a 3.16.2-5+deb9u3

---

#### 🟠 [HIGH] CVE-2019-5827 – sqlite: out-of-bounds access due to the use of 32-bit memory allocator interfaces

| Campo | Valor |
|---|---|
| **ID** | `TRI-387459B2` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `8.8` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** Integer overflow in SQLite via WebSQL in Google Chrome prior to 74.0.3729.131 allowed a remote attacker to potentially exploit heap corruption via a crafted HTML page.

**Evidencia:** `Paquete: libsqlite3-0 v3.16.2-5+deb9u1 | Fix: 3.16.2-5+deb9u2`

**✅ Remediación:** Actualizar libsqlite3-0 de 3.16.2-5+deb9u1 a 3.16.2-5+deb9u2

---

#### 🟠 [HIGH] CVE-2019-9936 – sqlite: heap-based buffer over-read in function fts5HashEntrySort in sqlite3.c

| Campo | Valor |
|---|---|
| **ID** | `TRI-594687CA` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** In SQLite 3.27.2, running fts5 prefix queries inside a transaction could trigger a heap-based buffer over-read in fts5HashEntrySort in sqlite3.c, which may lead to an information leak. This is related to ext/fts5/fts5_hash.c.

**Evidencia:** `Paquete: libsqlite3-0 v3.16.2-5+deb9u1 | Fix: 3.16.2-5+deb9u2`

**✅ Remediación:** Actualizar libsqlite3-0 de 3.16.2-5+deb9u1 a 3.16.2-5+deb9u2

---

#### 🟠 [HIGH] CVE-2019-9937 – sqlite: null-pointer dereference in function fts5ChunkIterate in sqlite3.c

| Campo | Valor |
|---|---|
| **ID** | `TRI-38D93111` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** In SQLite 3.27.2, interleaving reads and writes in a single transaction with an fts5 virtual table will lead to a NULL Pointer Dereference in fts5ChunkIterate in sqlite3.c. This is related to ext/fts5/fts5_hash.c and ext/fts5/fts5_index.c.

**Evidencia:** `Paquete: libsqlite3-0 v3.16.2-5+deb9u1 | Fix: 3.16.2-5+deb9u2`

**✅ Remediación:** Actualizar libsqlite3-0 de 3.16.2-5+deb9u1 a 3.16.2-5+deb9u2

---

#### 🟠 [HIGH] CVE-2020-11655 – sqlite: malformed window-function query leads to DoS

| Campo | Valor |
|---|---|
| **ID** | `TRI-F84CEE07` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** SQLite through 3.31.1 allows attackers to cause a denial of service (segmentation fault) via a malformed window-function query because the AggInfo object's initialization is mishandled.

**Evidencia:** `Paquete: libsqlite3-0 v3.16.2-5+deb9u1 | Fix: 3.16.2-5+deb9u2`

**✅ Remediación:** Actualizar libsqlite3-0 de 3.16.2-5+deb9u1 a 3.16.2-5+deb9u2

---

#### 🟠 [HIGH] CVE-2020-13630 – sqlite: Use-after-free in fts3EvalNextRow in ext/fts3/fts3.c

| Campo | Valor |
|---|---|
| **ID** | `TRI-BA57BDB8` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.0` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** ext/fts3/fts3.c in SQLite before 3.32.0 has a use-after-free in fts3EvalNextRow, related to the snippet feature.

**Evidencia:** `Paquete: libsqlite3-0 v3.16.2-5+deb9u1 | Fix: 3.16.2-5+deb9u2`

**✅ Remediación:** Actualizar libsqlite3-0 de 3.16.2-5+deb9u1 a 3.16.2-5+deb9u2

---

#### 🟠 [HIGH] CVE-2020-13871 – sqlite: use-after-free in resetAccumulator in select.c

| Campo | Valor |
|---|---|
| **ID** | `TRI-51072536` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** SQLite 3.32.2 has a use-after-free in resetAccumulator in select.c because the parse tree rewrite for window functions is too late.

**Evidencia:** `Paquete: libsqlite3-0 v3.16.2-5+deb9u1 | Fix: 3.16.2-5+deb9u2`

**✅ Remediación:** Actualizar libsqlite3-0 de 3.16.2-5+deb9u1 a 3.16.2-5+deb9u2

---

#### 🟠 [HIGH] CVE-2018-0732 – openssl: Malicious server can send large prime to client during DH(E) TLS handshake causing the client to hang

| Campo | Valor |
|---|---|
| **ID** | `TRI-8A31D251` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** During key agreement in a TLS handshake using a DH(E) based ciphersuite a malicious server can send a very large prime value to the client. This will cause the client to spend an unreasonably long period of time generating a key for this prime resulting in a hang until the client has finished. This could be exploited in a Denial Of Service attack. Fixed in OpenSSL 1.1.0i-dev (Affected 1.1.0-1.1.0h

**Evidencia:** `Paquete: libssl1.0.2 v1.0.2l-2+deb9u3 | Fix: 1.0.2q-1~deb9u1`

**✅ Remediación:** Actualizar libssl1.0.2 de 1.0.2l-2+deb9u3 a 1.0.2q-1~deb9u1

---

#### 🟠 [HIGH] CVE-2021-23840 – openssl: integer overflow in CipherUpdate

| Campo | Valor |
|---|---|
| **ID** | `TRI-A690BC67` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** Calls to EVP_CipherUpdate, EVP_EncryptUpdate and EVP_DecryptUpdate may overflow the output length argument in some cases where the input length is close to the maximum permissable length for an integer on the platform. In such cases the return value from the function call will be 1 (indicating success), but the output length value will be negative. This could cause applications to behave incorrect

**Evidencia:** `Paquete: libssl1.0.2 v1.0.2l-2+deb9u3 | Fix: 1.0.2u-1~deb9u4`

**✅ Remediación:** Actualizar libssl1.0.2 de 1.0.2l-2+deb9u3 a 1.0.2u-1~deb9u4

---

#### 🟠 [HIGH] CVE-2021-3712 – openssl: Read buffer overruns processing ASN.1 strings

| Campo | Valor |
|---|---|
| **ID** | `TRI-5E651D95` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.4` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** ASN.1 strings are represented internally within OpenSSL as an ASN1_STRING structure which contains a buffer holding the string data and a field holding the buffer length. This contrasts with normal C strings which are repesented as a buffer for the string data which is terminated with a NUL (0) byte. Although not a strict requirement, ASN.1 strings that are parsed using OpenSSL's own "d2i" functio

**Evidencia:** `Paquete: libssl1.0.2 v1.0.2l-2+deb9u3 | Fix: 1.0.2u-1~deb9u6`

**✅ Remediación:** Actualizar libssl1.0.2 de 1.0.2l-2+deb9u3 a 1.0.2u-1~deb9u6

---

#### 🟠 [HIGH] CVE-2022-0778 – openssl: Infinite loop in BN_mod_sqrt() reachable when parsing certificates

| Campo | Valor |
|---|---|
| **ID** | `TRI-B6E35717` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** The BN_mod_sqrt() function, which computes a modular square root, contains a bug that can cause it to loop forever for non-prime moduli. Internally this function is used when parsing certificates that contain elliptic curve public keys in compressed form or explicit elliptic curve parameters with a base point encoded in compressed form. It is possible to trigger the infinite loop by crafting a cer

**Evidencia:** `Paquete: libssl1.0.2 v1.0.2l-2+deb9u3 | Fix: 1.0.2u-1~deb9u7`

**✅ Remediación:** Actualizar libssl1.0.2 de 1.0.2l-2+deb9u3 a 1.0.2u-1~deb9u7

---

#### 🟠 [HIGH] CVE-2019-1543 – openssl: ChaCha20-Poly1305 with long nonces

| Campo | Valor |
|---|---|
| **ID** | `TRI-25B353AD` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.4` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** ChaCha20-Poly1305 is an AEAD cipher, and requires a unique nonce input for every encryption operation. RFC 7539 specifies that the nonce value (IV) should be 96 bits (12 bytes). OpenSSL allows a variable nonce length and front pads the nonce with 0 bytes if it is less than 12 bytes. However it also incorrectly allows a nonce to be set of up to 16 bytes. In this case only the last 12 bytes are sign

**Evidencia:** `Paquete: libssl1.1 v1.1.0f-3+deb9u2 | Fix: 1.1.0k-1~deb9u1`

**✅ Remediación:** Actualizar libssl1.1 de 1.1.0f-3+deb9u2 a 1.1.0k-1~deb9u1

---

#### 🟠 [HIGH] CVE-2022-1292 – openssl: c_rehash script allows command injection

| Campo | Valor |
|---|---|
| **ID** | `TRI-26D12DB7` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.3` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** The c_rehash script does not properly sanitise shell metacharacters to prevent command injection. This script is distributed by some operating systems in a manner where it is automatically executed. On such operating systems, an attacker could execute arbitrary commands with the privileges of the script. Use of the c_rehash script is considered obsolete and should be replaced by the OpenSSL rehash

**Evidencia:** `Paquete: libssl1.1 v1.1.0f-3+deb9u2 | Fix: 1.1.0l-1~deb9u6`

**✅ Remediación:** Actualizar libssl1.1 de 1.1.0f-3+deb9u2 a 1.1.0l-1~deb9u6

---

#### 🟠 [HIGH] CVE-2018-15686 – systemd: line splitting via fgets() allows for state injection during daemon-reexec

| Campo | Valor |
|---|---|
| **ID** | `TRI-30753FE3` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.8` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** A vulnerability in unit_deserialize of systemd allows an attacker to supply arbitrary state across systemd re-execution via NotifyAccess. This can be used to improperly influence systemd execution and possibly lead to root privilege escalation. Affected releases are systemd versions up to and including 239.

**Evidencia:** `Paquete: libsystemd0 v232-25+deb9u4 | Fix: 232-25+deb9u10`

**✅ Remediación:** Actualizar libsystemd0 de 232-25+deb9u4 a 232-25+deb9u10

---

#### 🟠 [HIGH] CVE-2018-15688 – systemd: Out-of-bounds heap write in systemd-networkd dhcpv6 option handling

| Campo | Valor |
|---|---|
| **ID** | `TRI-868C1FBB` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `8.8` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** A buffer overflow vulnerability in the dhcp6 client of systemd allows a malicious dhcp6 server to overwrite heap memory in systemd-networkd. Affected releases are systemd: versions up to and including 239.

**Evidencia:** `Paquete: libsystemd0 v232-25+deb9u4 | Fix: 232-25+deb9u6`

**✅ Remediación:** Actualizar libsystemd0 de 232-25+deb9u4 a 232-25+deb9u6

---

#### 🟠 [HIGH] CVE-2018-16864 – systemd: stack overflow when calling syslog from a command with long cmdline

| Campo | Valor |
|---|---|
| **ID** | `TRI-CA364F17` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.8` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** An allocation of memory without limits, that could result in the stack clashing with another memory region, was discovered in systemd-journald when a program with long command line arguments calls syslog. A local attacker may use this flaw to crash systemd-journald or escalate his privileges. Versions through v240 are vulnerable.

**Evidencia:** `Paquete: libsystemd0 v232-25+deb9u4 | Fix: 232-25+deb9u7`

**✅ Remediación:** Actualizar libsystemd0 de 232-25+deb9u4 a 232-25+deb9u7

---

#### 🟠 [HIGH] CVE-2018-16865 – systemd: stack overflow when receiving many journald entries

| Campo | Valor |
|---|---|
| **ID** | `TRI-ECFE7C91` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.8` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** An allocation of memory without limits, that could result in the stack clashing with another memory region, was discovered in systemd-journald when many entries are sent to the journal socket. A local attacker, or a remote one if systemd-journal-remote is used, may use this flaw to crash systemd-journald or execute code with journald privileges. Versions through v240 are vulnerable.

**Evidencia:** `Paquete: libsystemd0 v232-25+deb9u4 | Fix: 232-25+deb9u7`

**✅ Remediación:** Actualizar libsystemd0 de 232-25+deb9u4 a 232-25+deb9u7

---

#### 🟠 [HIGH] CVE-2019-3842 – systemd: Spoofing of XDG_SEAT allows for actions to be checked against "allow_active" instead of "allow_any"

| Campo | Valor |
|---|---|
| **ID** | `TRI-078FF1A4` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.0` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** In systemd before v242-rc4, it was discovered that pam_systemd does not properly sanitize the environment before using the XDG_SEAT variable. It is possible for an attacker, in some particular configurations, to set a XDG_SEAT environment variable which allows for commands to be checked against polkit policies using the "allow_active" element rather than "allow_any".

**Evidencia:** `Paquete: libsystemd0 v232-25+deb9u4 | Fix: 232-25+deb9u11`

**✅ Remediación:** Actualizar libsystemd0 de 232-25+deb9u4 a 232-25+deb9u11

---

#### 🟠 [HIGH] CVE-2019-3843 – systemd: services with DynamicUser can create SUID/SGID binaries

| Campo | Valor |
|---|---|
| **ID** | `TRI-4E1685F2` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.8` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** It was discovered that a systemd service that uses DynamicUser property can create a SUID/SGID binary that would be allowed to run as the transient service UID/GID even after the service is terminated. A local attacker may use this flaw to access resources that will be owned by a potentially different service in the future, when the UID/GID will be recycled.

**Evidencia:** `Paquete: libsystemd0 v232-25+deb9u4 | Fix: Not available`

**✅ Remediación:** No hay fix disponible para libsystemd0 232-25+deb9u4 — considerar alternativa

---

#### 🟠 [HIGH] CVE-2019-3844 – systemd: services with DynamicUser can get new privileges and create SGID binaries

| Campo | Valor |
|---|---|
| **ID** | `TRI-B3DD8DC8` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.8` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** It was discovered that a systemd service that uses DynamicUser property can get new privileges through the execution of SUID binaries, which would allow to create binaries owned by the service transient group with the setgid bit set. A local attacker may use this flaw to access resources that will be owned by a potentially different service in the future, when the GID will be recycled.

**Evidencia:** `Paquete: libsystemd0 v232-25+deb9u4 | Fix: Not available`

**✅ Remediación:** No hay fix disponible para libsystemd0 232-25+deb9u4 — considerar alternativa

---

#### 🟠 [HIGH] CVE-2020-1712 – systemd: use-after-free when asynchronous polkit queries are performed

| Campo | Valor |
|---|---|
| **ID** | `TRI-3AC659E4` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.8` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** A heap use-after-free vulnerability was found in systemd before version v245-rc1, where asynchronous Polkit queries are performed while handling dbus messages. A local unprivileged attacker can abuse this flaw to crash systemd services or potentially execute code and elevate their privileges, by sending specially crafted dbus messages.

**Evidencia:** `Paquete: libsystemd0 v232-25+deb9u4 | Fix: 232-25+deb9u14`

**✅ Remediación:** Actualizar libsystemd0 de 232-25+deb9u4 a 232-25+deb9u14

---

#### 🟠 [HIGH] CVE-2017-17095 – libtiff: Heap-based buffer overflow in tools/pal2rgb.c can lead to denial of service

| Campo | Valor |
|---|---|
| **ID** | `TRI-C1428DDD` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `8.8` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** tools/pal2rgb.c in pal2rgb in LibTIFF 4.0.9 allows remote attackers to cause a denial of service (TIFFSetupStrips heap-based buffer overflow and application crash) or possibly have unspecified other impact via a crafted TIFF file.

**Evidencia:** `Paquete: libtiff5 v4.0.8-2+deb9u2 | Fix: 4.0.8-2+deb9u4`

**✅ Remediación:** Actualizar libtiff5 de 4.0.8-2+deb9u2 a 4.0.8-2+deb9u4

---

#### 🟠 [HIGH] CVE-2018-12900 – libtiff: Heap-based buffer overflow in the cpSeparateBufToContigBuf function resulting in a denial of service or possibly code execution

| Campo | Valor |
|---|---|
| **ID** | `TRI-57DD97DB` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `8.8` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** Heap-based buffer overflow in the cpSeparateBufToContigBuf function in tiffcp.c in LibTIFF 3.9.3, 3.9.4, 3.9.5, 3.9.6, 3.9.7, 4.0.0beta7, 4.0.0alpha4, 4.0.0alpha5, 4.0.0alpha6, 4.0.0, 4.0.1, 4.0.2, 4.0.3, 4.0.4, 4.0.4beta, 4.0.5, 4.0.6, 4.0.7, 4.0.8 and 4.0.9 allows remote attackers to cause a denial of service (crash) or possibly have unspecified other impact via a crafted TIFF file.

**Evidencia:** `Paquete: libtiff5 v4.0.8-2+deb9u2 | Fix: 4.0.8-2+deb9u5`

**✅ Remediación:** Actualizar libtiff5 de 4.0.8-2+deb9u2 a 4.0.8-2+deb9u5

---

#### 🟠 [HIGH] CVE-2018-15209 – libtiff: Heap-based buffer overflow in ChopUpSingleUncompressedStrip in tif_dirread.c

| Campo | Valor |
|---|---|
| **ID** | `TRI-FFDE8C1E` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `8.8` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** ChopUpSingleUncompressedStrip in tif_dirread.c in LibTIFF 4.0.9 allows remote attackers to cause a denial of service (heap-based buffer overflow and application crash) or possibly have unspecified other impact via a crafted TIFF file, as demonstrated by tiff2pdf.

**Evidencia:** `Paquete: libtiff5 v4.0.8-2+deb9u2 | Fix: 4.0.8-2+deb9u4`

**✅ Remediación:** Actualizar libtiff5 de 4.0.8-2+deb9u2 a 4.0.8-2+deb9u4

---

#### 🟠 [HIGH] CVE-2018-16335 – libtiff: Heap-based buffer overflow in ChopUpSingleUncompressedStrip in tif_dirread.c

| Campo | Valor |
|---|---|
| **ID** | `TRI-377A16D2` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `8.8` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** newoffsets handling in ChopUpSingleUncompressedStrip in tif_dirread.c in LibTIFF 4.0.9 allows remote attackers to cause a denial of service (heap-based buffer overflow and application crash) or possibly have unspecified other impact via a crafted TIFF file, as demonstrated by tiff2pdf. This is a different vulnerability than CVE-2018-15209.

**Evidencia:** `Paquete: libtiff5 v4.0.8-2+deb9u2 | Fix: 4.0.8-2+deb9u4`

**✅ Remediación:** Actualizar libtiff5 de 4.0.8-2+deb9u2 a 4.0.8-2+deb9u4

---

#### 🟠 [HIGH] CVE-2018-17100 – libtiff: Integer overflow in multiply_ms in tools/ppm2tiff.c

| Campo | Valor |
|---|---|
| **ID** | `TRI-A7BA93B8` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `8.8` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** An issue was discovered in LibTIFF 4.0.9. There is a int32 overflow in multiply_ms in tools/ppm2tiff.c, which can cause a denial of service (crash) or possibly have unspecified other impact via a crafted image file.

**Evidencia:** `Paquete: libtiff5 v4.0.8-2+deb9u2 | Fix: 4.0.8-2+deb9u5`

**✅ Remediación:** Actualizar libtiff5 de 4.0.8-2+deb9u2 a 4.0.8-2+deb9u5

---

#### 🟠 [HIGH] CVE-2018-17101 – libtiff: Two out-of-bounds writes in cpTags in tools/tiff2bw.c and tools/pal2rgb.c

| Campo | Valor |
|---|---|
| **ID** | `TRI-CA4F8C70` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `8.8` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** An issue was discovered in LibTIFF 4.0.9. There are two out-of-bounds writes in cpTags in tools/tiff2bw.c and tools/pal2rgb.c, which can cause a denial of service (application crash) or possibly have unspecified other impact via a crafted image file.

**Evidencia:** `Paquete: libtiff5 v4.0.8-2+deb9u2 | Fix: 4.0.8-2+deb9u4`

**✅ Remediación:** Actualizar libtiff5 de 4.0.8-2+deb9u2 a 4.0.8-2+deb9u4

---

#### 🟠 [HIGH] CVE-2018-18557 – libtiff: Out-of-bounds write in tif_jbig.c

| Campo | Valor |
|---|---|
| **ID** | `TRI-CD43D08F` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `8.8` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** LibTIFF 3.9.3, 3.9.4, 3.9.5, 3.9.6, 3.9.7, 4.0.0alpha4, 4.0.0alpha5, 4.0.0alpha6, 4.0.0beta7, 4.0.0, 4.0.1, 4.0.2, 4.0.3, 4.0.4, 4.0.4beta, 4.0.5, 4.0.6, 4.0.7, 4.0.8 and 4.0.9 (with JBIG enabled) decodes arbitrarily-sized JBIG into a buffer, ignoring the buffer size, which leads to a tif_jbig.c JBIGDecode out-of-bounds write.

**Evidencia:** `Paquete: libtiff5 v4.0.8-2+deb9u2 | Fix: 4.0.8-2+deb9u4`

**✅ Remediación:** Actualizar libtiff5 de 4.0.8-2+deb9u2 a 4.0.8-2+deb9u4

---

#### 🟠 [HIGH] CVE-2018-8905 – libtiff: heap-based buffer overflow in tif_lzw.c:LZWDecodeCompat() allows for denial of service

| Campo | Valor |
|---|---|
| **ID** | `TRI-CC4C5DFD` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `8.8` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** In LibTIFF 4.0.9, a heap-based buffer overflow occurs in the function LZWDecodeCompat in tif_lzw.c via a crafted TIFF file, as demonstrated by tiff2ps.

**Evidencia:** `Paquete: libtiff5 v4.0.8-2+deb9u2 | Fix: 4.0.8-2+deb9u4`

**✅ Remediación:** Actualizar libtiff5 de 4.0.8-2+deb9u2 a 4.0.8-2+deb9u4

---

#### 🟠 [HIGH] CVE-2019-17546 – libtiff: integer overflow leading to heap-based buffer overflow in tif_getimage.c

| Campo | Valor |
|---|---|
| **ID** | `TRI-0D4553E6` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `8.8` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** tif_getimage.c in LibTIFF through 4.0.10, as used in GDAL through 3.0.1 and other products, has an integer overflow that potentially causes a heap-based buffer overflow via a crafted RGBA image, related to a "Negative-size-param" condition.

**Evidencia:** `Paquete: libtiff5 v4.0.8-2+deb9u2 | Fix: 4.0.8-2+deb9u5`

**✅ Remediación:** Actualizar libtiff5 de 4.0.8-2+deb9u2 a 4.0.8-2+deb9u5

---

#### 🟠 [HIGH] CVE-2020-19131 – libtiff: a buffer overflow via the "invertImage()" may lead to DoS

| Campo | Valor |
|---|---|
| **ID** | `TRI-059C2785` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** Buffer Overflow in LibTiff v4.0.10 allows attackers to cause a denial of service via the "invertImage()" function in the component "tiffcrop".

**Evidencia:** `Paquete: libtiff5 v4.0.8-2+deb9u2 | Fix: 4.0.8-2+deb9u7`

**✅ Remediación:** Actualizar libtiff5 de 4.0.8-2+deb9u2 a 4.0.8-2+deb9u7

---

#### 🟠 [HIGH] CVE-2020-35523 – libtiff: Integer overflow in tif_getimage.c

| Campo | Valor |
|---|---|
| **ID** | `TRI-306E8346` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.8` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** An integer overflow flaw was found in libtiff that exists in the tif_getimage.c file. This flaw allows an attacker to inject and execute arbitrary code when a user opens a crafted TIFF file. The highest threat from this vulnerability is to confidentiality, integrity, as well as system availability.

**Evidencia:** `Paquete: libtiff5 v4.0.8-2+deb9u2 | Fix: 4.0.8-2+deb9u6`

**✅ Remediación:** Actualizar libtiff5 de 4.0.8-2+deb9u2 a 4.0.8-2+deb9u6

---

#### 🟠 [HIGH] CVE-2020-35524 – libtiff: Heap-based buffer overflow in TIFF2PDF tool

| Campo | Valor |
|---|---|
| **ID** | `TRI-5E97AF49` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.8` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** A heap-based buffer overflow flaw was found in libtiff in the handling of TIFF images in libtiff's TIFF2PDF tool. A specially crafted TIFF file can lead to arbitrary code execution. The highest threat from this vulnerability is to confidentiality, integrity, as well as system availability.

**Evidencia:** `Paquete: libtiff5 v4.0.8-2+deb9u2 | Fix: 4.0.8-2+deb9u6`

**✅ Remediación:** Actualizar libtiff5 de 4.0.8-2+deb9u2 a 4.0.8-2+deb9u6

---

#### 🟠 [HIGH] CVE-2020-36332 – libwebp: excessive memory allocation when reading a file

| Campo | Valor |
|---|---|
| **ID** | `TRI-DDD659C2` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** A flaw was found in libwebp in versions before 1.0.1. When reading a file libwebp allocates an excessive amount of memory. The highest threat from this vulnerability is to the service availability.

**Evidencia:** `Paquete: libwebp6 v0.5.2-1 | Fix: Not available`

**✅ Remediación:** No hay fix disponible para libwebp6 0.5.2-1 — considerar alternativa

---

#### 🟠 [HIGH] CVE-2020-14363 – libX11: integer overflow leads to double free in locale handling

| Campo | Valor |
|---|---|
| **ID** | `TRI-8EE6964B` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.8` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** An integer overflow vulnerability leading to a double-free was found in libX11. This flaw allows a local privileged attacker to cause an application compiled with libX11 to crash, or in some cases, result in arbitrary code execution. The highest threat from this flaw is to confidentiality, integrity as well as system availability.

**Evidencia:** `Paquete: libx11-6 v2:1.6.4-3 | Fix: 2:1.6.4-3+deb9u3`

**✅ Remediación:** Actualizar libx11-6 de 2:1.6.4-3 a 2:1.6.4-3+deb9u3

---

#### 🟠 [HIGH] CVE-2017-16932 – libxml2: Infinite recursion in parameter entities

| Campo | Valor |
|---|---|
| **ID** | `TRI-A10A6461` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** parser.c in libxml2 before 2.9.5 does not prevent infinite recursion in parameter entities.

**Evidencia:** `Paquete: libxml2 v2.9.4+dfsg1-2.2+deb9u2 | Fix: 2.9.4+dfsg1-2.2+deb9u6`

**✅ Remediación:** Actualizar libxml2 de 2.9.4+dfsg1-2.2+deb9u2 a 2.9.4+dfsg1-2.2+deb9u6

---

#### 🟠 [HIGH] CVE-2017-5130 – chromium-browser: heap overflow in libxml2

| Campo | Valor |
|---|---|
| **ID** | `TRI-11C60655` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `8.8` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** An integer overflow in xmlmemory.c in libxml2 before 2.9.5, as used in Google Chrome prior to 62.0.3202.62 and other products, allowed a remote attacker to potentially exploit heap corruption via a crafted XML file.

**Evidencia:** `Paquete: libxml2 v2.9.4+dfsg1-2.2+deb9u2 | Fix: 2.9.4+dfsg1-2.2+deb9u6`

**✅ Remediación:** Actualizar libxml2 de 2.9.4+dfsg1-2.2+deb9u2 a 2.9.4+dfsg1-2.2+deb9u6

---

#### 🟠 [HIGH] CVE-2018-14404 – libxml2: NULL pointer dereference in xmlXPathCompOpEval() function in xpath.c

| Campo | Valor |
|---|---|
| **ID** | `TRI-881D7952` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** A NULL pointer dereference vulnerability exists in the xpath.c:xmlXPathCompOpEval() function of libxml2 through 2.9.8 when parsing an invalid XPath expression in the XPATH_OP_AND or XPATH_OP_OR case. Applications processing untrusted XSL format inputs with the use of the libxml2 library may be vulnerable to a denial of service attack due to a crash of the application.

**Evidencia:** `Paquete: libxml2 v2.9.4+dfsg1-2.2+deb9u2 | Fix: 2.9.4+dfsg1-2.2+deb9u3`

**✅ Remediación:** Actualizar libxml2 de 2.9.4+dfsg1-2.2+deb9u2 a 2.9.4+dfsg1-2.2+deb9u3

---

#### 🟠 [HIGH] CVE-2019-19956 – libxml2: memory leak in xmlParseBalancedChunkMemoryRecover in parser.c

| Campo | Valor |
|---|---|
| **ID** | `TRI-515F77E4` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** xmlParseBalancedChunkMemoryRecover in parser.c in libxml2 before 2.9.10 has a memory leak related to newDoc->oldNs.

**Evidencia:** `Paquete: libxml2 v2.9.4+dfsg1-2.2+deb9u2 | Fix: 2.9.4+dfsg1-2.2+deb9u3`

**✅ Remediación:** Actualizar libxml2 de 2.9.4+dfsg1-2.2+deb9u2 a 2.9.4+dfsg1-2.2+deb9u3

---

#### 🟠 [HIGH] CVE-2019-20388 – libxml2: memory leak in xmlSchemaPreRun in xmlschemas.c

| Campo | Valor |
|---|---|
| **ID** | `TRI-853C0E75` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** xmlSchemaPreRun in xmlschemas.c in libxml2 2.9.10 allows an xmlSchemaValidateStream memory leak.

**Evidencia:** `Paquete: libxml2 v2.9.4+dfsg1-2.2+deb9u2 | Fix: 2.9.4+dfsg1-2.2+deb9u3`

**✅ Remediación:** Actualizar libxml2 de 2.9.4+dfsg1-2.2+deb9u2 a 2.9.4+dfsg1-2.2+deb9u3

---

#### 🟠 [HIGH] CVE-2020-7595 – libxml2: infinite loop in xmlStringLenDecodeEntities in some end-of-file situations

| Campo | Valor |
|---|---|
| **ID** | `TRI-D34D45B2` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** xmlStringLenDecodeEntities in parser.c in libxml2 2.9.10 has an infinite loop in a certain end-of-file situation.

**Evidencia:** `Paquete: libxml2 v2.9.4+dfsg1-2.2+deb9u2 | Fix: 2.9.4+dfsg1-2.2+deb9u3`

**✅ Remediación:** Actualizar libxml2 de 2.9.4+dfsg1-2.2+deb9u2 a 2.9.4+dfsg1-2.2+deb9u3

---

#### 🟠 [HIGH] CVE-2021-3516 – libxml2: Use-after-free in xmlEncodeEntitiesInternal() in entities.c

| Campo | Valor |
|---|---|
| **ID** | `TRI-3B9E8D2E` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.8` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** There's a flaw in libxml2's xmllint in versions before 2.9.11. An attacker who is able to submit a crafted file to be processed by xmllint could trigger a use-after-free. The greatest impact of this flaw is to confidentiality, integrity, and availability.

**Evidencia:** `Paquete: libxml2 v2.9.4+dfsg1-2.2+deb9u2 | Fix: 2.9.4+dfsg1-2.2+deb9u4`

**✅ Remediación:** Actualizar libxml2 de 2.9.4+dfsg1-2.2+deb9u2 a 2.9.4+dfsg1-2.2+deb9u4

---

#### 🟠 [HIGH] CVE-2021-3517 – libxml2: Heap-based buffer overflow in xmlEncodeEntitiesInternal() in entities.c

| Campo | Valor |
|---|---|
| **ID** | `TRI-D40DBF8C` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `8.6` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** There is a flaw in the xml entity encoding functionality of libxml2 in versions before 2.9.11. An attacker who is able to supply a crafted file to be processed by an application linked with the affected functionality of libxml2 could trigger an out-of-bounds read. The most likely impact of this flaw is to application availability, with some potential impact to confidentiality and integrity if an a

**Evidencia:** `Paquete: libxml2 v2.9.4+dfsg1-2.2+deb9u2 | Fix: 2.9.4+dfsg1-2.2+deb9u4`

**✅ Remediación:** Actualizar libxml2 de 2.9.4+dfsg1-2.2+deb9u2 a 2.9.4+dfsg1-2.2+deb9u4

---

#### 🟠 [HIGH] CVE-2021-3518 – libxml2: Use-after-free in xmlXIncludeDoProcess() in xinclude.c

| Campo | Valor |
|---|---|
| **ID** | `TRI-673E253D` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `8.8` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** There's a flaw in libxml2 in versions before 2.9.11. An attacker who is able to submit a crafted file to be processed by an application linked with libxml2 could trigger a use-after-free. The greatest impact from this flaw is to confidentiality, integrity, and availability.

**Evidencia:** `Paquete: libxml2 v2.9.4+dfsg1-2.2+deb9u2 | Fix: 2.9.4+dfsg1-2.2+deb9u4`

**✅ Remediación:** Actualizar libxml2 de 2.9.4+dfsg1-2.2+deb9u2 a 2.9.4+dfsg1-2.2+deb9u4

---

#### 🟠 [HIGH] CVE-2022-23308 – libxml2: Use-after-free of ID and IDREF attributes

| Campo | Valor |
|---|---|
| **ID** | `TRI-C2808B5A` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** valid.c in libxml2 before 2.9.13 has a use-after-free of ID and IDREF attributes.

**Evidencia:** `Paquete: libxml2 v2.9.4+dfsg1-2.2+deb9u2 | Fix: 2.9.4+dfsg1-2.2+deb9u6`

**✅ Remediación:** Actualizar libxml2 de 2.9.4+dfsg1-2.2+deb9u2 a 2.9.4+dfsg1-2.2+deb9u6

---

#### 🟠 [HIGH] CVE-2019-18197 – libxslt: use after free in xsltCopyText in transform.c could lead to information disclosure

| Campo | Valor |
|---|---|
| **ID** | `TRI-6CF43852` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** In xsltCopyText in transform.c in libxslt 1.1.33, a pointer variable isn't reset under certain circumstances. If the relevant memory area happened to be freed and reused in a certain way, a bounds check could fail and memory outside a buffer could be written to, or uninitialized data could be disclosed.

**Evidencia:** `Paquete: libxslt1.1 v1.1.29-2.1 | Fix: 1.1.29-2.1+deb9u2`

**✅ Remediación:** Actualizar libxslt1.1 de 1.1.29-2.1 a 1.1.29-2.1+deb9u2

---

#### 🟠 [HIGH] CVE-2017-20002 – The Debian shadow package before 1:4.5-1 for Shadow incorrectly lists  ...

| Campo | Valor |
|---|---|
| **ID** | `TRI-A3659869` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.8` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** The Debian shadow package before 1:4.5-1 for Shadow incorrectly lists pts/0 and pts/1 as physical terminals in /etc/securetty. This allows local users to login as password-less users even if they are connected by non-physical means such as SSH (hence bypassing PAM's nullok_secure configuration). This notably affects environments such as virtual machines automatically generated with a default blank

**Evidencia:** `Paquete: login v1:4.4-4.1 | Fix: 1:4.4-4.1+deb9u1`

**✅ Remediación:** Actualizar login de 1:4.4-4.1 a 1:4.4-4.1+deb9u1

---

#### 🟠 [HIGH] CVE-2018-1000888 – php-pear: Unsafe deserialization of data in Archive_Tar class

| Campo | Valor |
|---|---|
| **ID** | `TRI-AADF0ED6` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `8.8` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** PEAR Archive_Tar version 1.4.3 and earlier contains a CWE-502, CWE-915 vulnerability in the Archive_Tar class. There are several file operations with `$v_header['filename']` as parameter (such as file_exists, is_file, is_dir, etc). When extract is called without a specific prefix path, we can trigger unserialization by crafting a tar file with `phar://[path_to_malicious_phar_file]` as path. Object

**Evidencia:** `Paquete: php-pear v1:1.10.1+submodules+notgz-9 | Fix: 1:1.10.1+submodules+notgz-9+deb9u1`

**✅ Remediación:** Actualizar php-pear de 1:1.10.1+submodules+notgz-9 a 1:1.10.1+submodules+notgz-9+deb9u1

---

#### 🟠 [HIGH] CVE-2020-28948 – Archive_Tar: allows an unserialization attack because phar: is blocked but PHAR: is not blocked

| Campo | Valor |
|---|---|
| **ID** | `TRI-FACDDA58` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.8` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** Archive_Tar through 1.4.10 allows an unserialization attack because phar: is blocked but PHAR: is not blocked.

**Evidencia:** `Paquete: php-pear v1:1.10.1+submodules+notgz-9 | Fix: 1:1.10.1+submodules+notgz-9+deb9u2`

**✅ Remediación:** Actualizar php-pear de 1:1.10.1+submodules+notgz-9 a 1:1.10.1+submodules+notgz-9+deb9u2

---

#### 🟠 [HIGH] CVE-2020-28949 – Archive_Tar: improper filename sanitization leads to file overwrites

| Campo | Valor |
|---|---|
| **ID** | `TRI-37D2EB3A` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.8` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** Archive_Tar through 1.4.10 has :// filename sanitization only to address phar attacks, and thus any other stream-wrapper attack (such as file:// to overwrite files) can still succeed.

**Evidencia:** `Paquete: php-pear v1:1.10.1+submodules+notgz-9 | Fix: 1:1.10.1+submodules+notgz-9+deb9u2`

**✅ Remediación:** Actualizar php-pear de 1:1.10.1+submodules+notgz-9 a 1:1.10.1+submodules+notgz-9+deb9u2

---

#### 🟠 [HIGH] CVE-2020-36193 – Archive_Tar: directory traversal due to inadequate checking of symbolic links

| Campo | Valor |
|---|---|
| **ID** | `TRI-D6A0432A` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** Tar.php in Archive_Tar through 1.4.11 allows write operations with Directory Traversal due to inadequate checking of symbolic links, a related issue to CVE-2020-28948.

**Evidencia:** `Paquete: php-pear v1:1.10.1+submodules+notgz-9 | Fix: 1:1.10.1+submodules+notgz-9+deb9u3`

**✅ Remediación:** Actualizar php-pear de 1:1.10.1+submodules+notgz-9 a 1:1.10.1+submodules+notgz-9+deb9u3

---

#### 🟠 [HIGH] CVE-2021-32610 – php-pear: Directory traversal vulnerability

| Campo | Valor |
|---|---|
| **ID** | `TRI-FAA6B3B0` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.1` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** In Archive_Tar before 1.4.14, symlinks can refer to targets outside of the extracted archive, a different vulnerability than CVE-2020-36193.

**Evidencia:** `Paquete: php-pear v1:1.10.1+submodules+notgz-9 | Fix: Not available`

**✅ Remediación:** No hay fix disponible para php-pear 1:1.10.1+submodules+notgz-9 — considerar alternativa

---

#### 🟠 [HIGH] CVE-2016-9840 – zlib: Out-of-bound pointer arithmetic in inftrees.c

| Campo | Valor |
|---|---|
| **ID** | `TRI-DDD838BD` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `8.8` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** inftrees.c in zlib 1.2.8 might allow context-dependent attackers to have unspecified impact by leveraging improper pointer arithmetic.

**Evidencia:** `Paquete: rsync v3.1.2-1+deb9u1 | Fix: 3.1.2-1+deb9u2`

**✅ Remediación:** Actualizar rsync de 3.1.2-1+deb9u1 a 3.1.2-1+deb9u2

---

#### 🟠 [HIGH] CVE-2016-9842 – zlib: Undefined left shift of negative number

| Campo | Valor |
|---|---|
| **ID** | `TRI-DC56C50B` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `8.8` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** The inflateMark function in inflate.c in zlib 1.2.8 might allow context-dependent attackers to have unspecified impact via vectors involving left shifts of negative integers.

**Evidencia:** `Paquete: rsync v3.1.2-1+deb9u1 | Fix: 3.1.2-1+deb9u2`

**✅ Remediación:** Actualizar rsync de 3.1.2-1+deb9u1 a 3.1.2-1+deb9u2

---

#### 🟠 [HIGH] CVE-2018-5764 – rsync: sanitization bypass in parse_argument in options.c

| Campo | Valor |
|---|---|
| **ID** | `TRI-3178B878` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** The parse_arguments function in options.c in rsyncd in rsync before 3.1.3 does not prevent multiple --protect-args uses, which allows remote attackers to bypass an argument-sanitization protection mechanism.

**Evidencia:** `Paquete: rsync v3.1.2-1+deb9u1 | Fix: 3.1.2-1+deb9u3`

**✅ Remediación:** Actualizar rsync de 3.1.2-1+deb9u1 a 3.1.2-1+deb9u3

---

#### 🟠 [HIGH] CVE-2018-25032 – zlib: A flaw found in zlib when compressing (not decompressing) certain inputs

| Campo | Valor |
|---|---|
| **ID** | `TRI-2052408C` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `vulnerables/web-dvwa:latest (debian 9.5):None` |

**Descripción:** zlib before 1.2.12 allows memory corruption when deflating (i.e., when compressing) if the input has many distant matches.

**Evidencia:** `Paquete: zlib1g v1:1.2.8.dfsg-5 | Fix: 1:1.2.8.dfsg-5+deb9u1`

**✅ Remediación:** Actualizar zlib1g de 1:1.2.8.dfsg-5 a 1:1.2.8.dfsg-5+deb9u1

---

#### 🟡🟢⚪ Medios, Bajos e Info (152)

| Severidad | CVE / Advisory | CVSS | Remediación |
|---|---|---|---|
| 🟡 MEDIUM | CVE-2018-11763 – httpd: DoS for HTTP/2 connections by c | 5.9 | Actualizar apache2 de 2.4.25-3+deb9u5 a 2.4.25-3+deb9u6 |
| 🟡 MEDIUM | CVE-2018-17189 – httpd: mod_http2: DoS via slow, unneed | 5.3 | Actualizar apache2 de 2.4.25-3+deb9u5 a 2.4.25-3+deb9u7 |
| 🟡 MEDIUM | CVE-2019-0196 – httpd: mod_http2: read-after-free on a  | 5.3 | Actualizar apache2 de 2.4.25-3+deb9u5 a 2.4.25-3+deb9u7 |
| 🟡 MEDIUM | CVE-2019-0220 – httpd: URL normalization inconsistency | 5.3 | Actualizar apache2 de 2.4.25-3+deb9u5 a 2.4.25-3+deb9u7 |
| 🟡 MEDIUM | CVE-2019-10092 – httpd: limited cross-site scripting in | 6.1 | Actualizar apache2 de 2.4.25-3+deb9u5 a 2.4.25-3+deb9u9 |
| 🟡 MEDIUM | CVE-2019-10098 – httpd: mod_rewrite potential open redi | 6.1 | Actualizar apache2 de 2.4.25-3+deb9u5 a 2.4.25-3+deb9u8 |
| 🟡 MEDIUM | CVE-2019-17567 – httpd: mod_proxy_wstunnel tunneling of | 5.3 | No hay fix disponible para apache2 2.4.25-3+deb9u5 — considerar altern |
| 🟡 MEDIUM | CVE-2020-1927 – httpd: mod_rewrite configurations vulne | 6.1 | Actualizar apache2 de 2.4.25-3+deb9u5 a 2.4.25-3+deb9u10 |
| 🟡 MEDIUM | CVE-2020-1934 – httpd: mod_proxy_ftp use of uninitializ | 5.3 | Actualizar apache2 de 2.4.25-3+deb9u5 a 2.4.25-3+deb9u10 |
| 🟡 MEDIUM | CVE-2021-30641 – httpd: Unexpected URL matching with 'M | 5.3 | Actualizar apache2 de 2.4.25-3+deb9u5 a 2.4.25-3+deb9u10 |
| 🟡 MEDIUM | CVE-2020-27350 – APT had several integer overflows and  | 5.7 | Actualizar apt de 1.4.8 a 1.4.11 |
| 🟡 MEDIUM | CVE-2020-3810 – Missing input validation in the ar/tar  | 5.5 | Actualizar apt de 1.4.8 a 1.4.10 |
| 🟡 MEDIUM | CVE-2019-5094 – e2fsprogs: Crafted ext4 partition leads | 6.7 | Actualizar e2fslibs de 1.43.4-2 a 1.43.4-2+deb9u1 |
| 🟡 MEDIUM | CVE-2019-5188 – e2fsprogs: Out-of-bounds write in e2fsc | 6.7 | Actualizar e2fslibs de 1.43.4-2 a 1.43.4-2+deb9u2 |
| 🟡 MEDIUM | CVE-2019-8905 – file: stack-based buffer over-read in d | 4.4 | No hay fix disponible para file 1:5.30-1+deb9u2 — considerar alternati |
| 🟡 MEDIUM | CVE-2021-40491 – The ftp client in GNU Inetutils before | 6.5 | No hay fix disponible para inetutils-ping 2:1.9.4-2+b1 — considerar al |
| 🟡 MEDIUM | CVE-2018-20217 – krb5: Reachable assertion in the KDC u | 5.3 | Actualizar krb5-locales de 1.15-1+deb9u1 a 1.15-1+deb9u3 |
| 🟡 MEDIUM | CVE-2018-5710 – krb5: null pointer deference in strlen  | 6.5 | Actualizar krb5-locales de 1.15-1+deb9u1 a 1.15-1+deb9u3 |
| 🟡 MEDIUM | CVE-2018-5729 – krb5: null dereference in kadmind or DN | 4.7 | Actualizar krb5-locales de 1.15-1+deb9u1 a 1.15-1+deb9u3 |
| 🟡 MEDIUM | CVE-2021-37750 – krb5: NULL pointer dereference in proc | 6.5 | Actualizar krb5-locales de 1.15-1+deb9u1 a 1.15-1+deb9u3 |
| 🟡 MEDIUM | CVE-2018-14851 – php: exif: Buffer over-read in exif_pr | 5.5 | Actualizar libapache2-mod-php7.0 de 7.0.30-0+deb9u1 a 7.0.33-0+deb9u1 |
| 🟡 MEDIUM | CVE-2018-17082 – php: Cross-site scripting (XSS) flaw i | 6.1 | Actualizar libapache2-mod-php7.0 de 7.0.30-0+deb9u1 a 7.0.33-0+deb9u1 |
| 🟡 MEDIUM | CVE-2019-11038 – gd: Information disclosure in gdImageC | 5.3 | Actualizar libapache2-mod-php7.0 de 7.0.30-0+deb9u1 a 7.0.33-0+deb9u5 |
| 🟡 MEDIUM | CVE-2019-11045 – php: DirectoryIterator class accepts f | 5.9 | Actualizar libapache2-mod-php7.0 de 7.0.30-0+deb9u1 a 7.0.33-0+deb9u7 |
| 🟡 MEDIUM | CVE-2019-11046 – php: OOB read  in bc_shift_addsub | 5.3 | Actualizar libapache2-mod-php7.0 de 7.0.30-0+deb9u1 a 7.0.33-0+deb9u7 |
| 🟡 MEDIUM | CVE-2019-11047 – php: Information disclosure in exif_re | 6.5 | Actualizar libapache2-mod-php7.0 de 7.0.30-0+deb9u1 a 7.0.33-0+deb9u7 |
| 🟡 MEDIUM | CVE-2019-11048 – php: Integer wraparounds when receivin | 5.3 | Actualizar libapache2-mod-php7.0 de 7.0.30-0+deb9u1 a 7.0.33-0+deb9u8 |
| 🟡 MEDIUM | CVE-2019-11050 – php: Out of bounds read when parsing E | 6.5 | Actualizar libapache2-mod-php7.0 de 7.0.30-0+deb9u1 a 7.0.33-0+deb9u7 |
| 🟡 MEDIUM | CVE-2020-7063 – php: Files added to tar with Phar::buil | 5.3 | Actualizar libapache2-mod-php7.0 de 7.0.30-0+deb9u1 a 7.0.33-0+deb9u8 |
| 🟡 MEDIUM | CVE-2020-7064 – php: Information disclosure in exif_rea | 5.4 | Actualizar libapache2-mod-php7.0 de 7.0.30-0+deb9u1 a 7.0.33-0+deb9u8 |
| 🟡 MEDIUM | CVE-2020-7066 – php: Information disclosure in function | 4.3 | Actualizar libapache2-mod-php7.0 de 7.0.30-0+deb9u1 a 7.0.33-0+deb9u8 |
| 🟡 MEDIUM | CVE-2020-7070 – php: URL decoding of cookie names can l | 5.3 | Actualizar libapache2-mod-php7.0 de 7.0.30-0+deb9u1 a 7.0.33-0+deb9u10 |
| 🟡 MEDIUM | CVE-2020-7071 – php: FILTER_VALIDATE_URL accepts URLs w | 5.3 | Actualizar libapache2-mod-php7.0 de 7.0.30-0+deb9u1 a 7.0.33-0+deb9u11 |
| 🟡 MEDIUM | CVE-2021-21704 – php: security issues in pdo_firebase m | 5.9 | Actualizar libapache2-mod-php7.0 de 7.0.30-0+deb9u1 a 7.0.33-0+deb9u11 |
| 🟡 MEDIUM | CVE-2021-21705 – php: SSRF bypass in FILTER_VALIDATE_UR | 5.3 | Actualizar libapache2-mod-php7.0 de 7.0.30-0+deb9u1 a 7.0.33-0+deb9u11 |
| 🟡 MEDIUM | CVE-2021-21707 – php: Special character breaks path in  | 5.3 | No hay fix disponible para libapache2-mod-php7.0 7.0.30-0+deb9u1 — con |
| 🟡 MEDIUM | CVE-2017-10789 – perl-DBD-MySQL: Possible MITM attack w | 5.9 | No hay fix disponible para libdbd-mysql-perl 4.041-2 — considerar alte |
| 🟡 MEDIUM | CVE-2014-10402 – perl-dbi: Incomplete fix for CVE-2014- | 6.1 | Actualizar libdbi-perl de 1.636-1+b1 a 1.636-1+deb9u2 |
| 🟡 MEDIUM | CVE-2019-20919 – perl-dbi: NULL profile dereference in  | 4.7 | Actualizar libdbi-perl de 1.636-1+b1 a 1.636-1+deb9u1 |
| 🟡 MEDIUM | CVE-2020-14392 – perl-dbi: Memory corruption in XS func | 5.5 | Actualizar libdbi-perl de 1.636-1+b1 a 1.636-1+deb9u1 |
| 🟡 MEDIUM | CVE-2018-16062 – elfutils: Heap-based buffer over-read  | 5.5 | Actualizar libelf1 de 0.168-1 a 0.168-1+deb9u1 |
| 🟡 MEDIUM | CVE-2018-18310 – elfutils: invalid memory address deref | 5.5 | Actualizar libelf1 de 0.168-1 a 0.168-1+deb9u1 |
| 🟡 MEDIUM | CVE-2018-18520 – elfutils: eu-size cannot handle recurs | 6.5 | Actualizar libelf1 de 0.168-1 a 0.168-1+deb9u1 |
| 🟡 MEDIUM | CVE-2018-18521 – elfutils: Divide-by-zero in arlib_add_ | 5.5 | Actualizar libelf1 de 0.168-1 a 0.168-1+deb9u1 |
| 🟡 MEDIUM | CVE-2019-7150 – elfutils: segmentation fault in elf64_x | 5.5 | Actualizar libelf1 de 0.168-1 a 0.168-1+deb9u1 |
| 🟡 MEDIUM | CVE-2019-7665 – elfutils: heap-based buffer over-read i | 5.5 | Actualizar libelf1 de 0.168-1 a 0.168-1+deb9u1 |
| 🟡 MEDIUM | CVE-2022-25313 – expat: Stack exhaustion in doctype par | 6.5 | Actualizar libexpat1 de 2.2.0-2+deb9u1 a 2.2.0-2+deb9u5 |
| 🟡 MEDIUM | CVE-2019-13627 – libgcrypt: ECDSA timing attack allowin | 6.3 | No hay fix disponible para libgcrypt20 1.7.6-2+deb9u3 — considerar alt |
| 🟡 MEDIUM | CVE-2021-40528 – libgcrypt: ElGamal implementation allo | 5.9 | Actualizar libgcrypt20 de 1.7.6-2+deb9u3 a 1.7.6-2+deb9u4 |
| 🟡 MEDIUM | CVE-2018-5711 – gd: Infinite loop in gdImageCreateFromG | 5.5 | Actualizar libgd3 de 2.2.4-2+deb9u2 a 2.2.4-2+deb9u3 |
| 🟡 MEDIUM | CVE-2021-38115 – read_header_tga in gd_tga.c in the GD  | 6.5 | No hay fix disponible para libgd3 2.2.4-2+deb9u2 — considerar alternat |
| 🟡 MEDIUM | CVE-2021-40812 – The GD Graphics Library (aka LibGD) th | 6.5 | No hay fix disponible para libgd3 2.2.4-2+deb9u2 — considerar alternat |
| 🟡 MEDIUM | CVE-2018-10844 – gnutls: HMAC-SHA-256 vulnerable to Luc | 5.9 | Actualizar libgnutls30 de 3.5.8-5+deb9u3 a 3.5.8-5+deb9u4 |
| 🟡 MEDIUM | CVE-2018-10845 – gnutls: HMAC-SHA-384 vulnerable to Luc | 5.9 | Actualizar libgnutls30 de 3.5.8-5+deb9u3 a 3.5.8-5+deb9u4 |
| 🟡 MEDIUM | CVE-2018-10846 – gnutls: "Just in Time" PRIME + PROBE c | 5.6 | Actualizar libgnutls30 de 3.5.8-5+deb9u3 a 3.5.8-5+deb9u4 |
| 🟡 MEDIUM | CVE-2018-16868 – gnutls: Bleichenbacher-like side chann | 5.6 | No hay fix disponible para libgnutls30 3.5.8-5+deb9u3 — considerar alt |
| 🟡 MEDIUM | CVE-2021-4209 – GnuTLS: Null pointer dereference in MD_ | 6.5 | No hay fix disponible para libgnutls30 3.5.8-5+deb9u3 — considerar alt |
| 🟡 MEDIUM | CVE-2018-16869 – nettle: Leaky data conversion exposing | 5.7 | No hay fix disponible para libhogweed4 3.3-1+b2 — considerar alternati |
| 🟡 MEDIUM | CVE-2020-21913 – icu: Use after free in pkg_createWithA | 5.5 | Actualizar libicu57 de 57.1-6+deb9u2 a 57.1-6+deb9u5 |
| 🟡 MEDIUM | CVE-2018-1152 – libjpeg-turbo: Divide by zero allows fo | 6.5 | Actualizar libjpeg62-turbo de 1:1.5.1-2 a 1:1.5.1-2+deb9u1 |
| 🟡 MEDIUM | CVE-2018-14498 – libjpeg-turbo: heap-based buffer over- | 6.5 | Actualizar libjpeg62-turbo de 1:1.5.1-2 a 1:1.5.1-2+deb9u1 |
| 🟡 MEDIUM | CVE-2017-10268 – mysql: Server: Replication unspecified | 4.1 | Actualizar libmariadbclient18 de 10.1.26-0+deb9u1 a 10.1.37-0+deb9u1 |
| 🟡 MEDIUM | CVE-2017-10378 – mysql: Server: Optimizer unspecified v | 6.5 | Actualizar libmariadbclient18 de 10.1.26-0+deb9u1 a 10.1.37-0+deb9u1 |
| 🟡 MEDIUM | CVE-2018-2612 – mysql: InnoDB unspecified vulnerability | 6.5 | Actualizar libmariadbclient18 de 10.1.26-0+deb9u1 a 10.1.37-0+deb9u1 |
| 🟡 MEDIUM | CVE-2018-2622 – mysql: Server: DDL unspecified vulnerab | 6.5 | Actualizar libmariadbclient18 de 10.1.26-0+deb9u1 a 10.1.37-0+deb9u1 |
| 🟡 MEDIUM | CVE-2018-2640 – mysql: Server: Optimizer unspecified vu | 6.5 | Actualizar libmariadbclient18 de 10.1.26-0+deb9u1 a 10.1.37-0+deb9u1 |
| 🟡 MEDIUM | CVE-2018-2665 – mysql: Server: Optimizer unspecified vu | 6.5 | Actualizar libmariadbclient18 de 10.1.26-0+deb9u1 a 10.1.37-0+deb9u1 |
| 🟡 MEDIUM | CVE-2018-2668 – mysql: Server: Optimizer unspecified vu | 6.5 | Actualizar libmariadbclient18 de 10.1.26-0+deb9u1 a 10.1.37-0+deb9u1 |
| 🟡 MEDIUM | CVE-2018-2761 – mysql: Client programs unspecified vuln | 5.9 | Actualizar libmariadbclient18 de 10.1.26-0+deb9u1 a 10.1.37-0+deb9u1 |
| 🟡 MEDIUM | CVE-2018-2766 – mysql: InnoDB unspecified vulnerability | 4.9 | Actualizar libmariadbclient18 de 10.1.26-0+deb9u1 a 10.1.37-0+deb9u1 |
| 🟡 MEDIUM | CVE-2018-2771 – mysql: Server: Locking unspecified vuln | 4.4 | Actualizar libmariadbclient18 de 10.1.26-0+deb9u1 a 10.1.37-0+deb9u1 |
| 🟡 MEDIUM | CVE-2018-2781 – mysql: Server: Optimizer unspecified vu | 4.9 | Actualizar libmariadbclient18 de 10.1.26-0+deb9u1 a 10.1.37-0+deb9u1 |
| 🟡 MEDIUM | CVE-2018-2782 – mysql: InnoDB unspecified vulnerability | 6.5 | Actualizar libmariadbclient18 de 10.1.26-0+deb9u1 a 10.1.37-0+deb9u1 |
| 🟡 MEDIUM | CVE-2018-2784 – mysql: InnoDB unspecified vulnerability | 6.5 | Actualizar libmariadbclient18 de 10.1.26-0+deb9u1 a 10.1.37-0+deb9u1 |
| 🟡 MEDIUM | CVE-2018-2787 – mysql: InnoDB unspecified vulnerability | 5.5 | Actualizar libmariadbclient18 de 10.1.26-0+deb9u1 a 10.1.37-0+deb9u1 |
| 🟡 MEDIUM | CVE-2018-2813 – mysql: Server: DDL unspecified vulnerab | 4.3 | Actualizar libmariadbclient18 de 10.1.26-0+deb9u1 a 10.1.37-0+deb9u1 |
| 🟡 MEDIUM | CVE-2018-2817 – mysql: Server: DDL unspecified vulnerab | 6.5 | Actualizar libmariadbclient18 de 10.1.26-0+deb9u1 a 10.1.37-0+deb9u1 |
| 🟡 MEDIUM | CVE-2018-2819 – mysql: InnoDB unspecified vulnerability | 6.5 | Actualizar libmariadbclient18 de 10.1.26-0+deb9u1 a 10.1.37-0+deb9u1 |
| 🟡 MEDIUM | CVE-2018-3058 – mysql: MyISAM unspecified vulnerability | 4.3 | Actualizar libmariadbclient18 de 10.1.26-0+deb9u1 a 10.1.37-0+deb9u1 |
| 🟡 MEDIUM | CVE-2018-3063 – mysql: Server: Security: Privileges uns | 4.9 | Actualizar libmariadbclient18 de 10.1.26-0+deb9u1 a 10.1.37-0+deb9u1 |
| 🟡 MEDIUM | CVE-2018-3081 – mysql: Client programs unspecified vuln | 5.0 | Actualizar libmariadbclient18 de 10.1.26-0+deb9u1 a 10.1.37-0+deb9u1 |
| 🟡 MEDIUM | CVE-2018-3143 – mysql: InnoDB unspecified vulnerability | 6.5 | Actualizar libmariadbclient18 de 10.1.26-0+deb9u1 a 10.1.37-0+deb9u1 |
| 🟡 MEDIUM | CVE-2018-3156 – mysql: InnoDB unspecified vulnerability | 6.5 | Actualizar libmariadbclient18 de 10.1.26-0+deb9u1 a 10.1.37-0+deb9u1 |
| 🟡 MEDIUM | CVE-2018-3174 – mysql: Init script calling kill with ro | 5.3 | Actualizar libmariadbclient18 de 10.1.26-0+deb9u1 a 10.1.37-0+deb9u1 |
| 🟡 MEDIUM | CVE-2018-3251 – mysql: InnoDB unspecified vulnerability | 6.5 | Actualizar libmariadbclient18 de 10.1.26-0+deb9u1 a 10.1.37-0+deb9u1 |
| 🟡 MEDIUM | CVE-2018-3282 – mysql: Server: Storage Engines unspecif | 4.9 | Actualizar libmariadbclient18 de 10.1.26-0+deb9u1 a 10.1.37-0+deb9u1 |
| 🟡 MEDIUM | CVE-2019-2503 – mysql: Server: Connection Handling unsp | 6.4 | Actualizar libmariadbclient18 de 10.1.26-0+deb9u1 a 10.1.37-0+deb9u1 |
| 🟡 MEDIUM | CVE-2019-2529 – mysql: Server: Optimizer unspecified vu | 6.5 | Actualizar libmariadbclient18 de 10.1.26-0+deb9u1 a 10.1.38-0+deb9u1 |
| 🟡 MEDIUM | CVE-2019-2537 – mysql: Server: DDL unspecified vulnerab | 4.9 | Actualizar libmariadbclient18 de 10.1.26-0+deb9u1 a 10.1.38-0+deb9u1 |
| 🟡 MEDIUM | CVE-2019-2614 – mysql: Server: Replication unspecified  | 4.4 | Actualizar libmariadbclient18 de 10.1.26-0+deb9u1 a 10.1.41-0+deb9u1 |
| 🟡 MEDIUM | CVE-2019-2627 – mysql: Server: Security: Privileges uns | 4.9 | Actualizar libmariadbclient18 de 10.1.26-0+deb9u1 a 10.1.41-0+deb9u1 |
| 🟡 MEDIUM | CVE-2019-2737 – mysql: Server: Pluggable Auth unspecifi | 4.9 | Actualizar libmariadbclient18 de 10.1.26-0+deb9u1 a 10.1.41-0+deb9u1 |
| 🟡 MEDIUM | CVE-2019-2739 – mysql: Server: Security: Privileges uns | 5.1 | Actualizar libmariadbclient18 de 10.1.26-0+deb9u1 a 10.1.41-0+deb9u1 |
| 🟡 MEDIUM | CVE-2019-2740 – mysql: Server: XML unspecified vulnerab | 6.5 | Actualizar libmariadbclient18 de 10.1.26-0+deb9u1 a 10.1.41-0+deb9u1 |
| 🟡 MEDIUM | CVE-2019-2805 – mysql: Server: Parser unspecified vulne | 6.5 | Actualizar libmariadbclient18 de 10.1.26-0+deb9u1 a 10.1.41-0+deb9u1 |
| 🟡 MEDIUM | CVE-2019-2974 – mysql: Server: Optimizer unspecified vu | 6.5 | Actualizar libmariadbclient18 de 10.1.26-0+deb9u1 a 10.1.44-0+deb9u1 |
| 🟡 MEDIUM | CVE-2020-14765 – mysql: Server: FTS unspecified vulnera | 6.5 | Actualizar libmariadbclient18 de 10.1.26-0+deb9u1 a 10.1.48-0+deb9u1 |
| 🟡 MEDIUM | CVE-2020-14812 – mysql: Server: Locking unspecified vul | 4.9 | Actualizar libmariadbclient18 de 10.1.26-0+deb9u1 a 10.1.48-0+deb9u1 |
| 🟡 MEDIUM | CVE-2020-2574 – mysql: C API unspecified vulnerability  | 5.9 | Actualizar libmariadbclient18 de 10.1.26-0+deb9u1 a 10.1.44-0+deb9u1 |
| 🟡 MEDIUM | CVE-2020-2752 – mysql: C API unspecified vulnerability  | 5.3 | Actualizar libmariadbclient18 de 10.1.26-0+deb9u1 a 10.1.45-0+deb9u1 |
| 🟡 MEDIUM | CVE-2020-2812 – mysql: Server: Stored Procedure unspeci | 4.9 | Actualizar libmariadbclient18 de 10.1.26-0+deb9u1 a 10.1.45-0+deb9u1 |
| 🟡 MEDIUM | CVE-2020-2814 – mysql: InnoDB unspecified vulnerability | 4.9 | Actualizar libmariadbclient18 de 10.1.26-0+deb9u1 a 10.1.45-0+deb9u1 |
| 🟡 MEDIUM | CVE-2021-2022 – mysql: InnoDB unspecified vulnerability | 4.4 | Actualizar libmariadbclient18 de 10.1.26-0+deb9u1 a 10.1.47-0+deb9u1 |
| 🟡 MEDIUM | CVE-2020-29362 – p11-kit: out-of-bounds read in p11_rpc | 5.3 | Actualizar libp11-kit0 de 0.23.3-2 a 0.23.3-2+deb9u1 |
| 🟡 MEDIUM | CVE-2020-14155 – pcre: Integer overflow when parsing ca | 5.3 | No hay fix disponible para libpcre3 2:8.39-3 — considerar alternativa |
| 🟡 MEDIUM | CVE-2019-7317 – libpng: use-after-free in png_image_fre | 5.3 | Actualizar libpng16-16 de 1.6.28-1 a 1.6.28-1+deb9u1 |
| 🟡 MEDIUM | CVE-2019-10130 – postgresql: Selectivity estimators byp | 4.3 | Actualizar libpq5 de 9.6.10-0+deb9u1 a 9.6.13-0+deb9u1 |
| 🟡 MEDIUM | CVE-2020-1720 – postgresql: ALTER ... DEPENDS ON EXTENS | 6.5 | Actualizar libpq5 de 9.6.10-0+deb9u1 a 9.6.17-0+deb9u1 |
| 🟡 MEDIUM | CVE-2021-23222 – postgresql: libpq processes unencrypte | 5.9 | Actualizar libpq5 de 9.6.10-0+deb9u1 a 9.6.24-0+deb9u1 |
| 🟡 MEDIUM | CVE-2021-32028 – postgresql: Memory disclosure in INSER | 6.5 | Actualizar libpq5 de 9.6.10-0+deb9u1 a 9.6.22-0+deb9u1 |
| 🟡 MEDIUM | CVE-2019-16168 – sqlite: Division by zero in whereLoopA | 6.5 | Actualizar libsqlite3-0 de 3.16.2-5+deb9u1 a 3.16.2-5+deb9u2 |
| 🟡 MEDIUM | CVE-2019-19645 – sqlite: infinite recursion via certain | 5.5 | No hay fix disponible para libsqlite3-0 3.16.2-5+deb9u1 — considerar a |
| 🟡 MEDIUM | CVE-2020-13434 – sqlite: integer overflow in sqlite3_st | 5.5 | Actualizar libsqlite3-0 de 3.16.2-5+deb9u1 a 3.16.2-5+deb9u2 |
| 🟡 MEDIUM | CVE-2020-13631 – sqlite: Virtual table can be renamed i | 5.5 | No hay fix disponible para libsqlite3-0 3.16.2-5+deb9u1 — considerar a |
| 🟡 MEDIUM | CVE-2020-13632 – sqlite: NULL pointer dereference in ex | 5.5 | Actualizar libsqlite3-0 de 3.16.2-5+deb9u1 a 3.16.2-5+deb9u2 |
| 🟡 MEDIUM | CVE-2018-0734 – openssl: timing side channel attack in  | 5.9 | Actualizar libssl1.0.2 de 1.0.2l-2+deb9u3 a 1.0.2q-1~deb9u1 |
| 🟡 MEDIUM | CVE-2018-0737 – openssl: RSA key generation cache timin | 5.9 | Actualizar libssl1.0.2 de 1.0.2l-2+deb9u3 a 1.0.2q-1~deb9u1 |
| 🟡 MEDIUM | CVE-2018-5407 – openssl: Side-channel vulnerability on  | 4.7 | Actualizar libssl1.0.2 de 1.0.2l-2+deb9u3 a 1.0.2q-1~deb9u1 |
| 🟡 MEDIUM | CVE-2019-1547 – openssl: side-channel weak encryption v | 4.7 | Actualizar libssl1.0.2 de 1.0.2l-2+deb9u3 a 1.0.2t-1~deb9u1 |
| 🟡 MEDIUM | CVE-2019-1551 – openssl: Integer overflow in RSAZ modul | 5.3 | Actualizar libssl1.0.2 de 1.0.2l-2+deb9u3 a 1.0.2u-1~deb9u1 |
| 🟡 MEDIUM | CVE-2019-1559 – openssl: 0-byte record padding oracle | 5.9 | Actualizar libssl1.0.2 de 1.0.2l-2+deb9u3 a 1.0.2r-1~deb9u1 |
| 🟡 MEDIUM | CVE-2020-1971 – openssl: EDIPARTYNAME NULL pointer de-r | 5.9 | Actualizar libssl1.0.2 de 1.0.2l-2+deb9u3 a 1.0.2u-1~deb9u3 |
| 🟡 MEDIUM | CVE-2021-23841 – openssl: NULL pointer dereference in X | 5.9 | Actualizar libssl1.0.2 de 1.0.2l-2+deb9u3 a 1.0.2u-1~deb9u4 |
| 🟡 MEDIUM | CVE-2018-0735 – openssl: timing side channel attack in  | 5.9 | Actualizar libssl1.1 de 1.1.0f-3+deb9u2 a 1.1.0j-1~deb9u1 |
| 🟡 MEDIUM | CVE-2021-4160 – openssl: Carry propagation bug in the M | 5.9 | No hay fix disponible para libssl1.1 1.1.0f-3+deb9u2 — considerar alte |
| 🟡 MEDIUM | CVE-2018-1049 – systemd: automount: access to automount | 5.9 | Actualizar libsystemd0 de 232-25+deb9u4 a 232-25+deb9u10 |
| 🟡 MEDIUM | CVE-2019-6454 – systemd: Insufficient input validation  | 5.5 | Actualizar libsystemd0 de 232-25+deb9u4 a 232-25+deb9u9 |
| 🟡 MEDIUM | CVE-2021-33910 – systemd: uncontrolled allocation on th | 5.5 | Actualizar libsystemd0 de 232-25+deb9u4 a 232-25+deb9u13 |
| 🟡 MEDIUM | CVE-2021-3997 – systemd: Uncontrolled recursion in syst | 5.5 | No hay fix disponible para libsystemd0 232-25+deb9u4 — considerar alte |
| 🟡 MEDIUM | CVE-2017-11613 – libtiff: Memory leak via corrupt td_im | 6.5 | Actualizar libtiff5 de 4.0.8-2+deb9u2 a 4.0.8-2+deb9u4 |
| 🟡 MEDIUM | CVE-2018-10963 – libtiff: reachable assertion in TIFFWr | 6.5 | Actualizar libtiff5 de 4.0.8-2+deb9u2 a 4.0.8-2+deb9u4 |
| 🟡 MEDIUM | CVE-2018-17000 – libtiff: NULL pointer dereference in f | 6.5 | Actualizar libtiff5 de 4.0.8-2+deb9u2 a 4.0.8-2+deb9u5 |
| 🟡 MEDIUM | CVE-2018-19210 – libtiff: NULL pointer dereference in T | 6.5 | Actualizar libtiff5 de 4.0.8-2+deb9u2 a 4.0.8-2+deb9u5 |
| 🟡 MEDIUM | CVE-2018-5784 – libtiff: uncontrolled resource consumpt | 6.5 | Actualizar libtiff5 de 4.0.8-2+deb9u2 a 4.0.8-2+deb9u4 |
| 🟡 MEDIUM | CVE-2018-7456 – libtiff: NULL pointer dereference in ti | 6.5 | Actualizar libtiff5 de 4.0.8-2+deb9u2 a 4.0.8-2+deb9u4 |
| 🟡 MEDIUM | CVE-2019-14973 – libtiff: integer overflow in _TIFFChec | 6.5 | Actualizar libtiff5 de 4.0.8-2+deb9u2 a 4.0.8-2+deb9u5 |
| 🟡 MEDIUM | CVE-2019-7663 – libtiff: integer overflow in libtiff/ti | 6.5 | Actualizar libtiff5 de 4.0.8-2+deb9u2 a 4.0.8-2+deb9u5 |
| 🟡 MEDIUM | CVE-2020-18768 – libtiff: heap-based buffer overflow in | 5.5 | Actualizar libtiff5 de 4.0.8-2+deb9u2 a 4.0.8-2+deb9u7 |
| 🟡 MEDIUM | CVE-2020-19144 – libtiff: heap-based buffer overflow in | 6.5 | Actualizar libtiff5 de 4.0.8-2+deb9u2 a 4.0.8-2+deb9u7 |
| 🟡 MEDIUM | CVE-2022-0561 – libtiff: Denial of Service via crafted  | 5.5 | Actualizar libtiff5 de 4.0.8-2+deb9u2 a 4.0.8-2+deb9u8 |
| 🟡 MEDIUM | CVE-2022-0562 – libtiff: Null source pointer lead to De | 5.5 | Actualizar libtiff5 de 4.0.8-2+deb9u2 a 4.0.8-2+deb9u8 |
| 🟡 MEDIUM | CVE-2022-22844 – libtiff: out-of-bounds read in _TIFFme | 5.5 | Actualizar libtiff5 de 4.0.8-2+deb9u2 a 4.0.8-2+deb9u8 |
| 🟡 MEDIUM | CVE-2020-14344 – libX11: Heap overflow in the X input m | 6.7 | Actualizar libx11-6 de 2:1.6.4-3 a 2:1.6.4-3+deb9u2 |
| 🟡 MEDIUM | CVE-2016-9318 – libxml2: XML External Entity vulnerabil | 5.5 | Actualizar libxml2 de 2.9.4+dfsg1-2.2+deb9u2 a 2.9.4+dfsg1-2.2+deb9u6 |
| 🟡 MEDIUM | CVE-2017-18258 – libxml2: Unrestricted memory usage in  | 6.5 | Actualizar libxml2 de 2.9.4+dfsg1-2.2+deb9u2 a 2.9.4+dfsg1-2.2+deb9u3 |
| 🟡 MEDIUM | CVE-2017-5969 – libxml2: Null pointer dereference in xm | 4.7 | Actualizar libxml2 de 2.9.4+dfsg1-2.2+deb9u2 a 2.9.4+dfsg1-2.2+deb9u6 |
| 🟡 MEDIUM | CVE-2018-14567 – libxml2: Infinite loop caused by incor | 6.5 | Actualizar libxml2 de 2.9.4+dfsg1-2.2+deb9u2 a 2.9.4+dfsg1-2.2+deb9u3 |
| 🟡 MEDIUM | CVE-2020-24977 – libxml2: Buffer overflow vulnerability | 6.5 | Actualizar libxml2 de 2.9.4+dfsg1-2.2+deb9u2 a 2.9.4+dfsg1-2.2+deb9u3 |
| 🟡 MEDIUM | CVE-2021-3537 – libxml2: NULL pointer dereference when  | 5.9 | Actualizar libxml2 de 2.9.4+dfsg1-2.2+deb9u2 a 2.9.4+dfsg1-2.2+deb9u4 |
| 🟡 MEDIUM | CVE-2021-3541 – libxml2: Exponential entity expansion a | 6.5 | Actualizar libxml2 de 2.9.4+dfsg1-2.2+deb9u2 a 2.9.4+dfsg1-2.2+deb9u5 |
| 🟡 MEDIUM | CVE-2022-29824 – libxml2: integer overflows in xmlBuf a | 6.5 | Actualizar libxml2 de 2.9.4+dfsg1-2.2+deb9u2 a 2.9.4+dfsg1-2.2+deb9u7 |
| 🟡 MEDIUM | CVE-2018-20482 – tar: Infinite read loop in sparse_dump | 4.7 | Actualizar tar de 1.29b-1.1 a 1.29b-1.1+deb9u1 |

### 🌐 OWASP ZAP (DAST) — `ASC-DAST-001`

> **Tipo:** Análisis Dinámico en Ejecución  
> **Raw:** 21 | **Únicos:** 21 | **Deduplicados:** 0 (0.0%)

**Distribución:** 🟠 HIGH: **1** | 🟡 MEDIUM: **3** | 🟢 LOW: **11** | ⚪ INFO: **6**

#### 🔴🟠 Críticos y Altos (1)

#### 🟠 [HIGH] Apache HTTP Server Version with Known Vulnerabilities

| Campo | Valor |
|---|---|
| **ID** | `ZAP-687A0987` |
| **Herramienta** | `ZAP` (DAST) |
| **ASC ISO/IEC 27034** | `ASC-DAST-001` |
| **Categoría OWASP** | A05:2021 – Security Misconfiguration |
| **CWE** | `1395` |
| **Endpoint** | `GET http://localhost:80/login.php` |

**Descripción:** The server disclosed the version of a server side technology it is running via an HTTP response header, and that version is affected by known vulnerabilities. The version, header and vulnerabilities, listed by severity, are given in the other info. See the references for the details of each. Note that some distributions backport security fixes without changing the version number, so check whether 

**Evidencia:** `Apache/2.4.25`

**✅ Remediación:** Upgrade Apache HTTP Server to a supported version which includes fixes for the listed vulnerabilities. Also configure the server not to disclose its version, e.g. by setting "ServerTokens Prod" and "ServerSignature Off".

---

#### 🟡🟢⚪ Medios, Bajos e Info (20)

| Severidad | Hallazgo | Endpoint | Remediación |
|---|---|---|---|
| 🟡 MEDIUM | Content Security Policy (CSP) Header Not Set | `http://localhost/about.php` | Ensure that your web server, application server, load balancer, etc. i |
| 🟡 MEDIUM | Missing Anti-clickjacking Header | `http://localhost/about.php` | Modern Web browsers support the Content-Security-Policy and X-Frame-Op |
| 🟡 MEDIUM | Source Code Disclosure - SQL | `http://localhost/instructions.php` | Ensure that application Source Code is not available with alternative  |
| 🟢 LOW | Cookie No HttpOnly Flag | `http://localhost` | Ensure that the HttpOnly flag is set for all cookies. |
| 🟢 LOW | Cookie without SameSite Attribute | `http://localhost` | Ensure that the SameSite attribute is set to either 'lax' or ideally ' |
| 🟢 LOW | Cross-Origin-Embedder-Policy Header Missing or Inv | `http://localhost:80/login.php` | Ensure that the application/web server sets the Cross-Origin-Embedder- |
| 🟢 LOW | Cross-Origin-Opener-Policy Header Missing or Inval | `http://localhost:80/login.php` | Ensure that the application/web server sets the Cross-Origin-Opener-Po |
| 🟢 LOW | Cross-Origin-Resource-Policy Header Missing or Inv | `http://localhost/dvwa/css/login.css` | Ensure that the application/web server sets the Cross-Origin-Resource- |
| 🟢 LOW | Dangerous JS Functions | `http://localhost/dvwa/js/dvwaPage.js` | See the references for security advice on the use of these functions. |
| 🟢 LOW | In Page Banner Information Leak | `http://localhost/sitemap.xml` | Configure the server to prevent such information leaks. For example: U |
| 🟢 LOW | Information Disclosure - Debug Error Messages | `http://localhost/instructions.php` | Disable debugging messages before pushing to production. |
| 🟢 LOW | Permissions Policy Header Not Set | `http://localhost/about.php` | Ensure that your web server, application server, load balancer, etc. i |
| 🟢 LOW | Server Leaks Version Information via "Server" HTTP | `http://localhost` | Ensure that your web server, application server, load balancer, etc. i |
| 🟢 LOW | X-Content-Type-Options Header Missing | `http://localhost/dvwa/css/login.css` | Ensure that the application/web server sets the Content-Type header ap |
| ⚪ INFO | Authentication Request Identified | `http://localhost/login.php` | This is an informational alert rather than a vulnerability and so ther |
| ⚪ INFO | Information Disclosure - Suspicious Comments | `http://localhost/setup.php` | Remove all comments that return information that may help an attacker  |
| ⚪ INFO | Non-Storable Content | `http://localhost` | The content may be marked as storable by ensuring that the following c |
| ⚪ INFO | Session Management Response Identified | `http://localhost` | This is an informational alert rather than a vulnerability and so ther |
| ⚪ INFO | Storable and Cacheable Content | `http://localhost/dvwa/css/login.css` | Validate that the response does not contain sensitive, personal or use |
| ⚪ INFO | Storable but Non-Cacheable Content | `http://localhost:80/login.php` | Revisar y corregir la alerta: Storable but Non-Cacheable Content |

### 🎯 Nuclei (Pentesting) — `ASC-PENTEST-001`

> **Tipo:** Validación Activa de Templates  
> **Raw:** 8 | **Únicos:** 8 | **Deduplicados:** 0 (0.0%)

**Distribución:** 🟠 HIGH: **1** | 🟡 MEDIUM: **1** | 🟢 LOW: **6**

#### 🔴🟠 Críticos y Altos (1)

#### 🟠 [HIGH] DVWA Exposed Setup Page

| Campo | Valor |
|---|---|
| **ID** | `NUC-964C9A18` |
| **Herramienta** | `NUCLEI` (PENTEST) |
| **ASC ISO/IEC 27034** | `ASC-PENTEST-001` |
| **Categoría OWASP** | A07:2021 – Identification and Authentication Failures |
| **Endpoint** | `HTTP http://localhost:80/setup.php` |

**Descripción:** A Damn Vulnerable Web Application (DVWA) setup page is exposed. An unauthenticated attacker can use the setup page to reset the database, which restores the default credentials (admin:password), and the page discloses database configuration details.

**Evidencia:** `curl -X 'GET' -H 'Accept: */*' -H 'Accept-Language: en' -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0' 'http://localhost:80/setup.php'`

**✅ Remediación:** Revisar: A Damn Vulnerable Web Application (DVWA) setup page is exposed. An unauthenticated attacker can use the setup page to reset the database, which restores the default credentials (admin:password), and t

---

#### 🟡🟢⚪ Medios, Bajos e Info (7)

| Severidad | Hallazgo | Endpoint | Remediación |
|---|---|---|---|
| 🟡 MEDIUM | Sensitive Configuration Files Listing - Detect | `http://localhost:80/config/` | Revisar: Listing of sensitive configuration files containing items suc |
| 🟢 LOW | Cookies without Secure attribute - Detect | `localhost:80` | Ensure that all cookies are set with the Secure attribute to prevent M |
| 🟢 LOW | Cookies without HttpOnly attribute - Detect | `localhost:80` | Ensure that all cookies are set with the HttpOnly attribute to prevent |
| 🟢 LOW | SSH SHA-1 HMAC Algorithms Enabled | `localhost:22` | Revisar: The SSH server at the remote end is set up to allow the use o |
| 🟢 LOW | README.md file disclosure | `http://localhost:80/README.md` | Revisar: Internal documentation file often used in projects which can  |
| 🟢 LOW | Gitignore Config - Detect | `http://localhost:80/.gitignore` | Revisar: Gitignore configuration information was detected. |
| 🟢 LOW | Missing Cookie SameSite Strict | `http://localhost:80` | Revisar: Identified cookies that lacked the samesite=strict attribute, |

### 🔐 Semgrep (SAST) — `ASC-SAST-001`

> **Tipo:** Análisis Estático de Código  
> **Raw:** 44 | **Únicos:** 19 | **Deduplicados:** 25 (56.8%)

**Distribución:** 🟠 HIGH: **9** | 🟡 MEDIUM: **10**

#### 🔴🟠 Críticos y Altos (9)

#### 🟠 [HIGH] Phpinfo Use

| Campo | Valor |
|---|---|
| **ID** | `SEM-4059CA7C` |
| **Herramienta** | `SEMGREP` (SAST) |
| **ASC ISO/IEC 27034** | `ASC-SAST-001` |
| **Categoría OWASP** | A05:2021 – Security Misconfiguration |
| **CWE** | `['CWE-200: Exposure of Sensitive Information to an Unauthorized Actor']` |
| **Archivo** | `source_to_scan/phpinfo.php:8` |

**Descripción:** The 'phpinfo' function may reveal sensitive information about your environment.

**Evidencia:** `requires login`

**✅ Remediación:** Revisar y corregir el patrón identificado en source_to_scan/phpinfo.php:8

---

#### 🟠 [HIGH] Tainted Sql String

| Campo | Valor |
|---|---|
| **ID** | `SEM-BE2783C8` |
| **Herramienta** | `SEMGREP` (SAST) |
| **ASC ISO/IEC 27034** | `ASC-SAST-001` |
| **Categoría OWASP** | A03:2021 – Injection |
| **CWE** | `["CWE-89: Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection')"]` |
| **Archivo** | `source_to_scan/vulnerabilities/bac/source/low.php:22` |

**Descripción:** User data flows into this manually-constructed SQL string. User data can be safely inserted into SQL strings using prepared statements or an object-relational mapper (ORM). Manually-constructed SQL strings is a possible indicator of SQL injection, which could let an attacker steal or manipulate data from the database. Instead, use prepared statements (`$mysqli->prepare("INSERT INTO test(id, label)

**Evidencia:** `requires login`

**✅ Remediación:** Revisar y corregir el patrón identificado en source_to_scan/vulnerabilities/bac/source/low.php:22

---

#### 🟠 [HIGH] Tainted Sql String

| Campo | Valor |
|---|---|
| **ID** | `SEM-696EA25D` |
| **Herramienta** | `SEMGREP` (SAST) |
| **ASC ISO/IEC 27034** | `ASC-SAST-001` |
| **Categoría OWASP** | A03:2021 – Injection |
| **CWE** | `["CWE-89: Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection')"]` |
| **Archivo** | `source_to_scan/vulnerabilities/bac/source/medium.php:21` |

**Descripción:** User data flows into this manually-constructed SQL string. User data can be safely inserted into SQL strings using prepared statements or an object-relational mapper (ORM). Manually-constructed SQL strings is a possible indicator of SQL injection, which could let an attacker steal or manipulate data from the database. Instead, use prepared statements (`$mysqli->prepare("INSERT INTO test(id, label)

**Evidencia:** `requires login`

**✅ Remediación:** Revisar y corregir el patrón identificado en source_to_scan/vulnerabilities/bac/source/medium.php:21

---

#### 🟠 [HIGH] Tainted Sql String

| Campo | Valor |
|---|---|
| **ID** | `SEM-E08ADF2A` |
| **Herramienta** | `SEMGREP` (SAST) |
| **ASC ISO/IEC 27034** | `ASC-SAST-001` |
| **Categoría OWASP** | A03:2021 – Injection |
| **CWE** | `["CWE-89: Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection')"]` |
| **Archivo** | `source_to_scan/vulnerabilities/brute/source/low.php:12` |

**Descripción:** User data flows into this manually-constructed SQL string. User data can be safely inserted into SQL strings using prepared statements or an object-relational mapper (ORM). Manually-constructed SQL strings is a possible indicator of SQL injection, which could let an attacker steal or manipulate data from the database. Instead, use prepared statements (`$mysqli->prepare("INSERT INTO test(id, label)

**Evidencia:** `requires login`

**✅ Remediación:** Revisar y corregir el patrón identificado en source_to_scan/vulnerabilities/brute/source/low.php:12

---

#### 🟠 [HIGH] Echoed Request

| Campo | Valor |
|---|---|
| **ID** | `SEM-1BB9695C` |
| **Herramienta** | `SEMGREP` (SAST) |
| **ASC ISO/IEC 27034** | `ASC-SAST-001` |
| **Categoría OWASP** | A03:2021 – Injection |
| **CWE** | `["CWE-79: Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting')"]` |
| **Archivo** | `source_to_scan/vulnerabilities/csp/source/jsonp.php:12` |

**Descripción:** `Echo`ing user input risks cross-site scripting vulnerability. You should use `htmlentities()` when showing data to users.

**Evidencia:** `requires login`

**✅ Remediación:** Revisar y corregir el patrón identificado en source_to_scan/vulnerabilities/csp/source/jsonp.php:12

---

#### 🟠 [HIGH] Tainted Sql String

| Campo | Valor |
|---|---|
| **ID** | `SEM-EF7FAFC8` |
| **Herramienta** | `SEMGREP` (SAST) |
| **ASC ISO/IEC 27034** | `ASC-SAST-001` |
| **Categoría OWASP** | A03:2021 – Injection |
| **CWE** | `["CWE-89: Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection')"]` |
| **Archivo** | `source_to_scan/vulnerabilities/sqli/source/low.php:10` |

**Descripción:** User data flows into this manually-constructed SQL string. User data can be safely inserted into SQL strings using prepared statements or an object-relational mapper (ORM). Manually-constructed SQL strings is a possible indicator of SQL injection, which could let an attacker steal or manipulate data from the database. Instead, use prepared statements (`$mysqli->prepare("INSERT INTO test(id, label)

**Evidencia:** `requires login`

**✅ Remediación:** Revisar y corregir el patrón identificado en source_to_scan/vulnerabilities/sqli/source/low.php:10

---

#### 🟠 [HIGH] Tainted Sql String

| Campo | Valor |
|---|---|
| **ID** | `SEM-565BB80E` |
| **Herramienta** | `SEMGREP` (SAST) |
| **ASC ISO/IEC 27034** | `ASC-SAST-001` |
| **Categoría OWASP** | A03:2021 – Injection |
| **CWE** | `["CWE-89: Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection')"]` |
| **Archivo** | `source_to_scan/vulnerabilities/sqli_blind/source/high.php:11` |

**Descripción:** User data flows into this manually-constructed SQL string. User data can be safely inserted into SQL strings using prepared statements or an object-relational mapper (ORM). Manually-constructed SQL strings is a possible indicator of SQL injection, which could let an attacker steal or manipulate data from the database. Instead, use prepared statements (`$mysqli->prepare("INSERT INTO test(id, label)

**Evidencia:** `requires login`

**✅ Remediación:** Revisar y corregir el patrón identificado en source_to_scan/vulnerabilities/sqli_blind/source/high.php:11

---

#### 🟠 [HIGH] Tainted Sql String

| Campo | Valor |
|---|---|
| **ID** | `SEM-DD601F83` |
| **Herramienta** | `SEMGREP` (SAST) |
| **ASC ISO/IEC 27034** | `ASC-SAST-001` |
| **Categoría OWASP** | A03:2021 – Injection |
| **CWE** | `["CWE-89: Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection')"]` |
| **Archivo** | `source_to_scan/vulnerabilities/sqli_blind/source/low.php:11` |

**Descripción:** User data flows into this manually-constructed SQL string. User data can be safely inserted into SQL strings using prepared statements or an object-relational mapper (ORM). Manually-constructed SQL strings is a possible indicator of SQL injection, which could let an attacker steal or manipulate data from the database. Instead, use prepared statements (`$mysqli->prepare("INSERT INTO test(id, label)

**Evidencia:** `requires login`

**✅ Remediación:** Revisar y corregir el patrón identificado en source_to_scan/vulnerabilities/sqli_blind/source/low.php:11

---

#### 🟠 [HIGH] Tainted Sql String

| Campo | Valor |
|---|---|
| **ID** | `SEM-74AF4D80` |
| **Herramienta** | `SEMGREP` (SAST) |
| **ASC ISO/IEC 27034** | `ASC-SAST-001` |
| **Categoría OWASP** | A03:2021 – Injection |
| **CWE** | `["CWE-89: Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection')"]` |
| **Archivo** | `source_to_scan/vulnerabilities/sqli_blind/source/medium.php:34` |

**Descripción:** User data flows into this manually-constructed SQL string. User data can be safely inserted into SQL strings using prepared statements or an object-relational mapper (ORM). Manually-constructed SQL strings is a possible indicator of SQL injection, which could let an attacker steal or manipulate data from the database. Instead, use prepared statements (`$mysqli->prepare("INSERT INTO test(id, label)

**Evidencia:** `requires login`

**✅ Remediación:** Revisar y corregir el patrón identificado en source_to_scan/vulnerabilities/sqli_blind/source/medium.php:34

---

#### 🟡🟢⚪ Medios, Bajos e Info (10)

| Severidad | Hallazgo | Endpoint | Remediación |
|---|---|---|---|
| 🟡 MEDIUM | Tainted Filename | `None` | Revisar y corregir el patrón identificado en source_to_scan/instructio |
| 🟡 MEDIUM | Tainted Exec | `None` | Revisar y corregir el patrón identificado en source_to_scan/vulnerabil |
| 🟡 MEDIUM | Tainted Exec | `None` | Revisar y corregir el patrón identificado en source_to_scan/vulnerabil |
| 🟡 MEDIUM | Tainted Exec | `None` | Revisar y corregir el patrón identificado en source_to_scan/vulnerabil |
| 🟡 MEDIUM | Tainted Exec | `None` | Revisar y corregir el patrón identificado en source_to_scan/vulnerabil |
| 🟡 MEDIUM | Tainted Exec | `None` | Revisar y corregir el patrón identificado en source_to_scan/vulnerabil |
| 🟡 MEDIUM | Tainted Filename | `None` | Revisar y corregir el patrón identificado en source_to_scan/vulnerabil |
| 🟡 MEDIUM | Tainted Filename | `None` | Revisar y corregir el patrón identificado en source_to_scan/vulnerabil |
| 🟡 MEDIUM | Tainted Filename | `None` | Revisar y corregir el patrón identificado en source_to_scan/vulnerabil |
| 🟡 MEDIUM | Tainted Filename | `None` | Revisar y corregir el patrón identificado en source_to_scan/vulnerabil |

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
| Semgrep OSS | SAST | `ASC-SAST-001` | 19 |
| Trivy | SCA | `ASC-SCA-001` | 386 |
| OWASP ZAP | DAST | `ASC-DAST-001` | 21 |
| Nuclei v3 | Pentesting | `ASC-PENTEST-001` | 8 |

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

- Este reporte corresponde a una única corrida sobre `dvwa`. La validación completa
  abarca nueve casos de estudio documentados en la tesis (Capítulo 5).
- La evaluación IA requiere validación humana antes de decisiones en producción.
- No reemplaza una auditoría de seguridad formal ni un pentest manual.
- El gate SSVC prioriza la cautela ante hallazgos críticos — ver tesis sección 5.6.3.

---

_Reporte generado el 2026-11-17 18:36:44 | Pipeline Run: `44148411474`_

_**Autores:** Jhojan Stiven Castaño Jejen & Juan Manuel Arango Rodas_
_**Universidad del Valle** — Ingeniería de Sistemas — 2026_
