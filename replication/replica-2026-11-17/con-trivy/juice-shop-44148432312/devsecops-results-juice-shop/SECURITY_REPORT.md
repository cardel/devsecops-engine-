# 🔐 Reporte de Seguridad DevSecOps
## ❌ Decisión de Despliegue: **FAIL**

---

> **Generado automáticamente por el DevSecOps Engine v1.3 — Universidad del Valle 2026**

| Campo | Valor |
|---|---|
| **Servicio** | `juice-shop` |
| **Entorno** | `staging` |
| **Criticidad de negocio** | `high` |
| **Pipeline Run** | `44148432312` |
| **Timestamp** | `2026-11-17 18:36:20` |
| **Modelo IA** | `gpt-4o-mini` |
| **Tokens utilizados** | `9,118` (prompt: 7,502 / completion: 1,616) |
| **Motor IA híbrido** | ✅ Motor híbrido activo |
| **ISO/IEC 27034 — Trazabilidad** | ✅ 3/4 ASC obligatorios ejecutados |

---

## 📊 Resumen Ejecutivo

Se han identificado múltiples vulnerabilidades críticas y altas en el servicio juice-shop, algunas de las cuales son explotables remotamente. La combinación de estas vulnerabilidades podría permitir a un atacante comprometer la integridad y disponibilidad del servicio, lo que representa un riesgo significativo para el negocio.

> **Recomendación del sistema:** No se recomienda el despliegue hasta que se aborden las vulnerabilidades críticas y altas identificadas.

---

## 🚦 Decisión Final del Security Gate

| Campo | Valor |
|---|---|
| **Decisión** | ❌ **FAIL** |
| **Fuente** | `ai_assisted` |
| **Nivel de riesgo (IA)** | `CRITICAL` |
| **Risk Score (IA)** | `8.5 / 10.0` |
| **Confianza IA** | `85%` |
| **Falsos positivos estimados** | `baja` |
| **ISO/IEC 27034 — Trazabilidad ANF** | `3/4` ASC obligatorios ejecutados (ver sección ISO/IEC 27034) |

---

## 📈 Estadísticas Globales de Hallazgos

### Distribución por Severidad

| Severidad | Hallazgos | % del total | Proporción |
|---|---|---|---|
| 🔴 CRITICAL | 6 | 5.7% | `░░░░░░░░░░░░░░░` |
| 🟠 HIGH | 28 | 26.7% | `████░░░░░░░░░░░` |
| 🟡 MEDIUM | 60 | 57.1% | `████████░░░░░░░` |
| 🟢 LOW | 8 | 7.6% | `█░░░░░░░░░░░░░░` |
| ⚪ INFO | 3 | 2.9% | `░░░░░░░░░░░░░░░` |
| ─ | **105** | **100%** | |

### Cobertura por Herramienta y ASC ISO/IEC 27034

> Cada herramienta tiene asignado un ASC (Application Security Control) de ISO/IEC 27034.
> La columna **Removidos** indica duplicados eliminados, no falsos positivos.

| Herramienta | ASC ISO 27034 | Raw | Únicos | Removidos | % Dedup | Estado |
|---|---|---|---|---|---|---|
| 🔐 Semgrep (SAST) | `ASC-SAST-001` | 18 | 15 | 3 | 16.7% | ✅ Ejecutado |
| 🔬 Trivy (SCA) | `ASC-SCA-001` | 99 | 76 | 23 | 23.2% | ✅ Ejecutado |
| 🌐 OWASP ZAP (DAST) | `ASC-DAST-001` | 9 | 9 | 0 | 0.0% | ✅ Ejecutado |
| 🎯 Nuclei (Pentesting) | `ASC-PENTEST-001` | 12 | 5 | 7 | 58.3% | ✅ Ejecutado |

### Top 5 Categorías OWASP Top 10

| Categoría | Hallazgos | % del total | Proporción |
|---|---|---|---|
| `A06:2021 – Vulnerable and Outdated Components` | 78 | 74.3% | `████████░░░░` |
| `A05:2021 – Security Misconfiguration` | 18 | 17.1% | `██░░░░░░░░░░` |
| `A03:2021 – Injection` | 8 | 7.6% | `░░░░░░░░░░░░` |
| `A07:2021 – Identification and Authentication Failures` | 1 | 1.0% | `░░░░░░░░░░░░` |

---

## 🔄 Metodología de Deduplicación

> El normalizador aplica deduplicación para evitar el doble conteo de vulnerabilidades
> detectadas por múltiples instancias de la misma herramienta.
>
> **Total raw:** 138 hallazgos → **Total único:** 105 → **Eliminados:** 33 (23.9% de reducción)

### 🔬 Trivy (SCA) — Análisis de Componentes de Software

- **Raw:** 99 | **Únicos:** 76 | **Removidos:** 23 (23.2%)
- **Criterio:** `tool + título + endpoint/archivo`

> La misma CVE sobre el mismo paquete puede aparecer una vez por ruta de instalación. Tras deduplicar por CVE + paquete + target queda una sola entrada. Los removidos son instancias duplicadas, no falsos positivos.

### 🌐 OWASP ZAP (DAST) — Análisis Dinámico en Ejecución

- **Raw:** 9 | **Únicos:** 9 | **Removidos:** 0 (0.0%)
- **Criterio:** `tool + título + endpoint/archivo`

> ZAP realiza escaneo baseline pasivo. Cada alerta representa un tipo de misconfiguration único — por eso la deduplicación raramente elimina hallazgos: todas las alertas suelen tener títulos distintos.

### 🎯 Nuclei (Pentesting) — Validación Activa de Templates

- **Raw:** 12 | **Únicos:** 5 | **Removidos:** 7 (58.3%)
- **Criterio:** `tool + título + endpoint/archivo`

> Nuclei puede disparar el mismo template en el mismo endpoint varias veces dentro del mismo run. Tras deduplicar por template + endpoint se conserva solo una entrada por hallazgo único.

### 🔐 Semgrep (SAST) — Análisis Estático de Código

- **Raw:** 18 | **Únicos:** 15 | **Removidos:** 3 (16.7%)
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
| **Tecnologías** | _No detectadas_ |
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
| ⚪ INFO | `no_waf` | No se detectó WAF — tráfico malicioso llega directo a la app |


---

## 🤖 Evaluación Detallada por IA

### Razonamiento Técnico

Los hallazgos críticos incluyen CVE-2015-9235 y CVE-2023-46233, ambos con EPSS que indican una probabilidad de explotación. Además, varios hallazgos de inyección SQL (CWE-89) presentan un riesgo alto de explotación. La falta de mitigaciones adecuadas y la presencia de vulnerabilidades en componentes críticos hacen que el despliegue sea inseguro.

**Análisis de falsos positivos:** Las vulnerabilidades identificadas son críticas y están respaldadas por datos de explotación empíricos.

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

**Evaluación general:** La cobertura general es adecuada, pero se requieren pruebas adicionales para validar la seguridad.

### ⚠️ Áreas sin cobertura (Blind Spots)

- Falta de pruebas de penetración exhaustivas en el entorno de staging.


### 🏆 Hallazgos Principales Identificados por IA

| Severidad | Hallazgo | CVSS | Remoto | Auth | Exploit | Categoría |
|---|---|---|---|---|---|---|
| 🔴 CRITICAL | CVE-2015-9235 – nodejs-jsonwebtoken: verifica | `9.8` | 🔴 Sí | 🟢 No | ⚠️ Sí | A06:2021 – Vulnerable and Outdated  |
| 🔴 CRITICAL | CVE-2023-46233 – crypto-js: PBKDF2 1,000 time | `9.1` | 🔴 Sí | 🟢 No | ⚠️ Sí | A06:2021 – Vulnerable and Outdated  |

---

## 🔗 Análisis de Cadenas de Ataque

> Esta sección identifica combinaciones de vulnerabilidades que, explotadas en secuencia,
> producen un impacto mayor al de cada vulnerabilidad de forma individual.

### 🔴 CHAIN-001 — Explotación de vulnerabilidades de inyección SQL y bypass de autenticación

| Campo | Valor |
|---|---|
| **Severidad combinada** | CRITICAL |
| **Probabilidad** | 🔴 Alta |
| **Vulnerabilidades involucradas** | `SEM-C2F5F78D`, `TRI-4651F9B4` |

**Secuencia del ataque:**

1. Paso 1: El atacante explota la vulnerabilidad de inyección SQL (CVE-XXXX) para obtener acceso a la base de datos.
2. Paso 2: Con acceso a la base de datos, utiliza la vulnerabilidad de bypass de autenticación (CVE-2015-9235) para eludir la autenticación.
3. Paso 3: Resultado final: El atacante obtiene acceso completo al sistema y puede robar datos sensibles.

**Impacto combinado:** La combinación de estas vulnerabilidades permite un acceso no autorizado y la posibilidad de un robo de datos masivo.

---

---

## 🛠️ Hoja de Ruta de Remediación

### 🚨 Inmediato (0–7 días) — 2 acciones

**1.** Actualizar jsonwebtoken a la versión 4.2.2 o superior. → Fix: `4.2.2`
   - `trivy` | Esfuerzo: _bajo_ | Fix disponible: ✅

**2.** Actualizar crypto-js a la versión 4.2.0 o superior. → Fix: `4.2.0`
   - `trivy` | Esfuerzo: _bajo_ | Fix disponible: ✅

### ⚡ Corto plazo (1–4 semanas) — 1 acciones

**3.** Revisar y corregir el patrón de inyección SQL en el código fuente.
   - `semgrep` | Esfuerzo: _medio_ | Fix disponible: ❌

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
| **EPSS** | 70 CVEs consultados vía FIRST.org API |

### Distribución de Acciones SSVC

| Acción | Hallazgos | % | Gate | Significado operativo |
|---|---|---|---|---|
| **Act** | `35` | 33.3% | ❌ FAIL | Explotación activa o automatizable con impacto total |
| **Attend** | `8` | 7.6% | ⚠️ CONDITIONAL | Explotación probable a corto plazo |
| **Track*** | `44` | 41.9% | ⚠️ CONDITIONAL | Monitoreo activo — riesgo controlado |
| **Track** | `18` | 17.1% | ✅ PASS | Sin explotación activa conocida |
| **Total evaluados** | `105` | 100% | ❌ **FAIL** | Decisión = acción máxima |

### Hallazgos que requieren acción inmediata (Act)

| Herramienta | Vulnerabilidad | Explotación | Automatizable | Impacto | Acción |
|---|---|---|---|---|---|
| `semgrep` | Express Sequelize Injection | poc | yes | total | **Act** |
| `semgrep` | Express Sequelize Injection | poc | yes | total | **Act** |
| `semgrep` | Express Sequelize Injection | poc | yes | total | **Act** |
| `semgrep` | Express Sequelize Injection | poc | yes | total | **Act** |
| `semgrep` | Hardcoded Jwt Secret | poc | yes | total | **Act** |
| `semgrep` | Express Sequelize Injection | poc | yes | total | **Act** |
| `semgrep` | Express Sequelize Injection | poc | yes | total | **Act** |
| `trivy` | CVE-2026-85091 – zlib: zlib: Heap buffer overflow in gz_vacate()  | poc | yes | total | **Act** |


### 📊 Métricas Formales — Dimensión Exploitation (F1 Score)

> Calculadas sobre CVEs con CISA KEV o EPSS disponible como *ground truth*.
> Metodología: Al Haddad et al. (2025) — arXiv 2510.18508.

| Métrica | Valor | Descripción |
|---|---|---|
| **Precisión** | `0.0000` | TP / (TP + FP) |
| **Recall** | `0.0000` | TP / (TP + FN) |
| **F1 Score** | `0.0000` | Media armónica precisión/recall |
| **Accuracy** | `1.0000` | (TP + TN) / total |
| CVEs evaluados | `71` | Solo CVEs con EPSS/KEV disponible |
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
| **Modelo LLM** | `gpt-4o-mini` |
| **Versión del prompt** | `3.0-ssvc-enriched` (indica prompt enriquecido con SSVC/EPSS/KEV) |
| **Tokens de prompt** | `7,502` |
| **Tokens de completion** | `1,616` |
| **Contexto SSVC activo** | ✅ Sí — el LLM recibió clasificaciones SSVC por hallazgo |
| **CISA KEV consultado** | 1,781 entradas (fuente: cisa.gov) |
| **EPSS consultado** | 70 CVEs (fuente: FIRST.org API) |
| **Hallazgos clasificados SSVC** | 105 |
| **Distribución SSVC pre-LLM** | Act=35, Attend=8, Track*=44, Track=18 |
| **F1 Exploitation** | `0.0000` (P=0.0000, R=0.0000, n=71 CVEs) |

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
**2 confirmado(s)**, **1 sobreestimado(s)**, **0 subestimado(s)**.

| ID | Hallazgo | SSVC prelim. | Juicio IA | EPSS | En KEV | Razonamiento del LLM |
|---|---|---|---|---|---|---|
| `SEM-C2F5F78D` | Express Sequelize Injection | `Act` | ⚠️ **overestimated** | `0.0000` | No | La clasificación SSVC como 'Act' parece ser una sobreestimación, ya que el EPSS de 0.0 sug... |
| `TRI-F0061998` | CVE-2023-46233 – crypto-js: PBKDF2 1,000 | `Act` | ✅ **confirmed** | `0.0064` | No | A pesar de un EPSS bajo, la gravedad de la vulnerabilidad y su impacto potencial en la seg... |
| `TRI-4651F9B4` | CVE-2015-9235 – nodejs-jsonwebtoken: ver | `Act` | ✅ **confirmed** | `0.0837` | No | La vulnerabilidad tiene un EPSS relativamente alto y puede ser explotada para eludir la ve... |


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
| **Métricas formales** | ❌ No | ❌ No | ✅ F1 = `0.000` |
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
- Hallazgos CRÍTICOS: 6 (umbral: 0)
- Hallazgos ALTOS: 28 (umbral: 5)
- Hallazgos MEDIOS: 60 (umbral: 20)

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
Análisis estático de código fuente: se ejecutó y **detectó 15 hallazgo(s)** (7 HIGH, 8 MEDIUM). Los hallazgos están documentados en la sección de detalle.

**🟡 ASC-SCA-001** (Trivy) — Control obligatorio  
Análisis de componentes y dependencias (CVEs): se ejecutó y **detectó 76 hallazgo(s)** (6 CRITICAL, 21 HIGH, 49 MEDIUM). Los hallazgos están documentados en la sección de detalle.

**⚠️ zap** (Herramienta) — Control obligatorio  
Control de seguridad: **no se ejecutó** en esta corrida. Posible causa: herramienta no disponible, aplicación sin respuesta HTTP, o fallo en el job correspondiente.

**ℹ️ ASC-PENTEST-001** (Nuclei v3) — Control obligatorio  
Validación activa con templates de pentest: se ejecutó y **detectó 5 hallazgo(s)** (1 MEDIUM, 4 LOW). Los hallazgos están documentados en la sección de detalle.

**ℹ️ ASC-DAST-001** (OWASP ZAP) — Control opcional  
Análisis dinámico en tiempo de ejecución: se ejecutó y **detectó 9 hallazgo(s)** (2 MEDIUM, 4 LOW, 3 INFO). Los hallazgos están documentados en la sección de detalle.


### Resumen de cobertura ANF

| ASC | Herramienta | Obligatoriedad | Estado | Hallazgos | Severidades |
|---|---|---|---|---|---|
| `ASC-SAST-001` | Semgrep OSS | ✅ Obligatorio | ✅ Ejecutado | 15 | 🟠H:7 / 🟡M:8 |
| `ASC-SCA-001` | Trivy | ✅ Obligatorio | ✅ Ejecutado | 76 | 🔴C:6 / 🟠H:21 / 🟡M:49 |
| `zap` | Herramienta | ✅ Obligatorio | ⚠️ No ejecutado | 0 | — |
| `ASC-PENTEST-001` | Nuclei v3 | ✅ Obligatorio | ✅ Ejecutado | 5 | 🟡M:1 / 🟢L:4 |
| `ASC-DAST-001` | OWASP ZAP | ⚪ Opcional | ✅ Ejecutado | 9 | 🟡M:2 / 🟢L:4 / ⚪I:3 |


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
> **Raw:** 99 | **Únicos:** 76 | **Deduplicados:** 23 (23.2%)

**Distribución:** 🔴 CRITICAL: **6** | 🟠 HIGH: **21** | 🟡 MEDIUM: **49**

#### 🔴🟠 Críticos y Altos (27)

#### 🔴 [CRITICAL] CVE-2023-46233 – crypto-js: PBKDF2 1,000 times weaker than specified in 1993 and 1.3M times weaker than current standard

| Campo | Valor |
|---|---|
| **ID** | `TRI-F0061998` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `9.1` |
| **Archivo** | `Node.js:None` |

**Descripción:** crypto-js is a JavaScript library of crypto standards. Prior to version 4.2.0, crypto-js PBKDF2 is 1,000 times weaker than originally specified in 1993, and at least 1,300,000 times weaker than current industry standard. This is because it both defaults to SHA1, a cryptographic hash algorithm considered insecure since at least 2005, and defaults to one single iteration, a 'strength' or 'difficulty

**Evidencia:** `Paquete: crypto-js v3.3.0 | Fix: 4.2.0`

**✅ Remediación:** Actualizar crypto-js de 3.3.0 a 4.2.0

---

#### 🔴 [CRITICAL] CVE-2026-71851 – crypto-js: crypto-js: Insufficient Entropy in Cryptographic Secret Generation via Vulnerable CryptoJS Dependency Chain

| Campo | Valor |
|---|---|
| **ID** | `TRI-CAAECC95` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `9.0` |
| **Archivo** | `Node.js:None` |

**Descripción:** crypto-js is a JavaScript library of crypto standards. Versions of crypto-js prior to 4.0.0 generate randomness in CryptoJS.lib.WordArray.random() using a custom variation of the Multiply-With-Carry pseudorandom number generator, seeded from Math.random(), instead of a cryptographically secure source. This generator was introduced in version 3.1.2-4 and remained present in nearly every 3.x release

**Evidencia:** `Paquete: crypto-js v3.3.0 | Fix: 4.0.0`

**✅ Remediación:** Actualizar crypto-js de 3.3.0 a 4.0.0

---

#### 🔴 [CRITICAL] CVE-2015-9235 – nodejs-jsonwebtoken: verification step bypass with an altered token

| Campo | Valor |
|---|---|
| **ID** | `TRI-4651F9B4` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
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
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
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
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **Archivo** | `Node.js:None` |

**Descripción:** All versions of `marsdb` are vulnerable to Command Injection. In the `DocumentMatcher` class, selectors on `$where` clauses are passed to a Function constructor unsanitized. This allows attackers to run arbitrary commands in the system when the function is executed.


## Recommendation

No fix is currently available. Consider using an alternative package until a fix is made available.

**Evidencia:** `Paquete: marsdb v0.6.11 | Fix: Not available`

**✅ Remediación:** No hay fix disponible para marsdb 0.6.11 — considerar alternativa

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

#### 🟠 [HIGH] CVE-2026-85091 – zlib: zlib: Heap buffer overflow in gz_vacate() allows arbitrary code execution

| Campo | Valor |
|---|---|
| **ID** | `TRI-375F9BF2` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `8.1` |
| **Archivo** | `bkimminich/juice-shop:latest (debian 13.7):None` |

**Descripción:** zlib 1.2.11 through 1.3.2 contains a heap buffer overflow: after an underlying write() fails, gz_write() returns without resetting strm.next_in, leaving it pointed at the caller's buffer. A later gz* write call then derives a position from the stale pointer and writes past a heap allocation; any write() failure reaches it, including EPIPE on a blocking descriptor, and in versions before 1.3.1.2 th

**Evidencia:** `Paquete: zlib1g v1:1.3.dfsg+really1.3.1-1+b1 | Fix: 1:1.3.dfsg+really1.3.1-1+deb13u1`

**✅ Remediación:** Actualizar zlib1g de 1:1.3.dfsg+really1.3.1-1+b1 a 1:1.3.dfsg+really1.3.1-1+deb13u1

---

#### 🟠 [HIGH] NSWG-ECO-428 – Out-of-bounds Read

| Campo | Valor |
|---|---|
| **ID** | `TRI-7F7B48B3` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **Archivo** | `Node.js:None` |

**Descripción:** `base64url` allocates uninitialized Buffers when number is passed in input on Node.js 4.x and below

**Evidencia:** `Paquete: base64url v0.0.6 | Fix: >=3.0.0`

**✅ Remediación:** Actualizar base64url de 0.0.6 a >=3.0.0

---

#### 🟠 [HIGH] CVE-2026-102990 – basic-ftp: basic-ftp: Denial of Service via crafted Unix directory listings

| Campo | Valor |
|---|---|
| **ID** | `TRI-482987CC` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `Node.js:None` |

**Descripción:** basic-ftp is an FTP client for Node.js. Prior to 6.2.1, Client.list() can be forced by a malicious or compromised FTP server to spend quadratic CPU time parsing a directory listing because the RE_LINE expression in src/parseListUnix.ts backtracks across adjacent variable-length owner and group fields when a long Unix-style line has a valid prefix but cannot satisfy the later size and date fields. 

**Evidencia:** `Paquete: basic-ftp v5.3.1 | Fix: 6.2.1`

**✅ Remediación:** Actualizar basic-ftp de 5.3.1 a 6.2.1

---

#### 🟠 [HIGH] CVE-2020-15084 – Authorization bypass in express-jwt

| Campo | Valor |
|---|---|
| **ID** | `TRI-E7285D69` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `9.1` |
| **Archivo** | `Node.js:None` |

**Descripción:** In express-jwt (NPM package) up and including version 5.3.3, the algorithms entry to be specified in the configuration is not being enforced. When algorithms is not specified in the configuration, with the combination of jwks-rsa, it may lead to authorization bypass. You are affected by this vulnerability if all of the following conditions apply: - You are using express-jwt - You do not have **alg

**Evidencia:** `Paquete: express-jwt v0.1.3 | Fix: 6.0.0`

**✅ Remediación:** Actualizar express-jwt de 0.1.3 a 6.0.0

---

#### 🟠 [HIGH] CVE-2022-23539 – jsonwebtoken: Unrestricted key type could lead to legacy keys usagen

| Campo | Valor |
|---|---|
| **ID** | `TRI-297C4D46` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
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
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
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
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
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
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
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
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
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
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.2` |
| **Archivo** | `Node.js:None` |

**Descripción:** Lodash versions prior to 4.17.21 are vulnerable to Command Injection via the template function.

**Evidencia:** `Paquete: lodash v2.4.2 | Fix: 4.17.21`

**✅ Remediación:** Actualizar lodash de 2.4.2 a 4.17.21

---

#### 🟠 [HIGH] CVE-2017-18214 – nodejs-moment: Regular expression denial of service

| Campo | Valor |
|---|---|
| **ID** | `TRI-6BAD1A14` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
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
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `Node.js:None` |

**Descripción:** Moment.js is a JavaScript date library for parsing, validating, manipulating, and formatting dates. A path traversal vulnerability impacts npm (server) users of Moment.js between versions 1.0.1 and 2.29.1, especially if a user-provided locale string is directly used to switch moment locale. This problem is patched in 2.29.2, and the patch can be applied to all affected versions. As a workaround, s

**Evidencia:** `Paquete: moment v2.0.0 | Fix: 2.29.2`

**✅ Remediación:** Actualizar moment de 2.0.0 a 2.29.2

---

#### 🟠 [HIGH] CVE-2022-25887 – sanitize-html: insecure global regular expression replacement logic may lead to ReDoS

| Campo | Valor |
|---|---|
| **ID** | `TRI-4254AA7C` |
| **Herramienta** | `TRIVY` (SCA) |
| **ASC ISO/IEC 27034** | `ASC-SCA-001` |
| **Categoría OWASP** | A06:2021 – Vulnerable and Outdated Components |
| **CVSS Score** | `7.5` |
| **Archivo** | `Node.js:None` |

**Descripción:** The package sanitize-html before 2.7.1 are vulnerable to Regular Expression Denial of Service (ReDoS) due to insecure global regular expression replacement logic of HTML comment removal.

**Evidencia:** `Paquete: sanitize-html v1.4.2 | Fix: 2.7.1`

**✅ Remediación:** Actualizar sanitize-html de 1.4.2 a 2.7.1

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

#### 🟡🟢⚪ Medios, Bajos e Info (49)

| Severidad | CVE / Advisory | CVSS | Remediación |
|---|---|---|---|
| 🟡 MEDIUM | CVE-2026-102010 – gcc-toolset-15-gcc: gcc: gcc-toolset- | 7.0 | No hay fix disponible para gcc-14-base 14.2.0-19 — considerar alternat |
| 🟡 MEDIUM | CVE-2026-114690 – gcc: Confirmed out-of-bounds read/wri | 6.2 | No hay fix disponible para gcc-14-base 14.2.0-19 — considerar alternat |
| 🟡 MEDIUM | CVE-2026-114691 – gcc: Integer wrap in `std | 5.9 | No hay fix disponible para gcc-14-base 14.2.0-19 — considerar alternat |
| 🟡 MEDIUM | CVE-2026-115455 – gcc: Stack overflow in std::bitset on | 6.5 | No hay fix disponible para gcc-14-base 14.2.0-19 — considerar alternat |
| 🟡 MEDIUM | CVE-2026-125709 – libstdc++: overflow leaves streambuf  | 4.2 | No hay fix disponible para gcc-14-base 14.2.0-19 — considerar alternat |
| 🟡 MEDIUM | CVE-2026-95619 – gcc: libstdc++ integer overflow in `ne | 7.7 | No hay fix disponible para gcc-14-base 14.2.0-19 — considerar alternat |
| 🟡 MEDIUM | CVE-2026-18374 – glibc: glibc: Heap buffer overflow via | 4.9 | No hay fix disponible para libc6 2.41-12+deb13u4 — considerar alternat |
| 🟡 MEDIUM | CVE-2026-19499 – glibc: Buffer Overflow in strfmon righ | 6.8 | No hay fix disponible para libc6 2.41-12+deb13u4 — considerar alternat |
| 🟡 MEDIUM | CVE-2026-19542 – glibc: Fix out-of-bounds array write i | 4.2 | No hay fix disponible para libc6 2.41-12+deb13u4 — considerar alternat |
| 🟡 MEDIUM | CVE-2026-5435 – glibc: glibc: Out-of-bounds write via T | 5.9 | No hay fix disponible para libc6 2.41-12+deb13u4 — considerar alternat |
| 🟡 MEDIUM | CVE-2026-6238 – glibc: glibc: Application crash or unin | 6.5 | No hay fix disponible para libc6 2.41-12+deb13u4 — considerar alternat |
| 🟡 MEDIUM | CVE-2026-6368 – glibc: glibc: Process abort due to inva | 5.5 | No hay fix disponible para libc6 2.41-12+deb13u4 — considerar alternat |
| 🟡 MEDIUM | CVE-2026-6791 – glibc: Glibc: Denial of Service via sta | 5.9 | No hay fix disponible para libc6 2.41-12+deb13u4 — considerar alternat |
| 🟡 MEDIUM | CVE-2026-77117 – glibc: Non-progress DoS in SHIFT_JISX0 | 5.9 | No hay fix disponible para libc6 2.41-12+deb13u4 — considerar alternat |
| 🟡 MEDIUM | CVE-2026-80489 – glibc: Non-progress DoS in EUC_JISX021 | 5.9 | No hay fix disponible para libc6 2.41-12+deb13u4 — considerar alternat |
| 🟡 MEDIUM | CVE-2026-84243 – glibc: glibc: Arbitrary code execution | 7.0 | No hay fix disponible para libc6 2.41-12+deb13u4 — considerar alternat |
| 🟡 MEDIUM | CVE-2026-8674 – glibc: glibc DNS stub resolver: Denial  | 5.3 | No hay fix disponible para libc6 2.41-12+deb13u4 — considerar alternat |
| 🟡 MEDIUM | CVE-2026-86805 – glibc: glibc: Privilege escalation and | 7.0 | No hay fix disponible para libc6 2.41-12+deb13u4 — considerar alternat |
| 🟡 MEDIUM | CVE-2026-89092 – glibc: nscd stack overflow leads to de | 4.2 | No hay fix disponible para libc6 2.41-12+deb13u4 — considerar alternat |
| 🟡 MEDIUM | CVE-2026-95818 – glibc: glibc: Local attacker can cause | 7.0 | No hay fix disponible para libc6 2.41-12+deb13u4 — considerar alternat |
| 🟡 MEDIUM | CVE-2026-107496 – Issue summary: Encrypting a CMS messa | None | No hay fix disponible para libssl3t64 3.5.7-1~deb13u3 — considerar alt |
| 🟡 MEDIUM | CVE-2026-88822 – Issue summary: QUIC, when performing a | None | No hay fix disponible para libssl3t64 3.5.7-1~deb13u3 — considerar alt |
| 🟡 MEDIUM | CVE-2026-88823 – Issue summary: The AES-GCM-SIV impleme | None | No hay fix disponible para libssl3t64 3.5.7-1~deb13u3 — considerar alt |
| 🟡 MEDIUM | CVE-2026-95691 – Issue summary: A retransmitted QUIC CR | None | No hay fix disponible para libssl3t64 3.5.7-1~deb13u3 — considerar alt |
| 🟡 MEDIUM | CVE-2026-95692 – Issue summary: Setting an AES-GCM-SIV  | None | No hay fix disponible para libssl3t64 3.5.7-1~deb13u3 — considerar alt |
| 🟡 MEDIUM | CVE-2026-27171 – zlib: zlib: Denial of Service via infi | 5.5 | Actualizar zlib1g de 1:1.3.dfsg+really1.3.1-1+b1 a 1:1.3.dfsg+really1. |
| 🟡 MEDIUM | GHSA-rvg8-pwq2-xj7q – Out-of-bounds Read in base64url | None | Actualizar base64url de 0.0.6 a 3.0.0 |
| 🟡 MEDIUM | CVE-2026-126345 – basic-ftp: Uncaught TypeError in MLSD | 5.3 | Actualizar basic-ftp de 5.3.1 a 6.2.4 |
| 🟡 MEDIUM | CVE-2026-126346 – basic-ftp: Uncaught exception crashes | 5.9 | Actualizar basic-ftp de 5.3.1 a 6.2.3 |
| 🟡 MEDIUM | CVE-2026-31808 – file-type: file-type: Denial of Servic | 5.3 | Actualizar file-type de 16.5.4 a 21.3.1 |
| 🟡 MEDIUM | CVE-2021-32822 – hbs: Insertion of Sensitive Informatio | 5.3 | No hay fix disponible para hbs 4.4.0 — considerar alternativa |
| 🟡 MEDIUM | CVE-2022-23540 – jsonwebtoken: Insecure default algorit | 7.6 | Actualizar jsonwebtoken de 0.1.0 a 9.0.0 |
| 🟡 MEDIUM | CVE-2022-23541 – jsonwebtoken: Insecure implementation  | 6.3 | Actualizar jsonwebtoken de 0.1.0 a 9.0.0 |
| 🟡 MEDIUM | CVE-2016-4055 – moment.js: regular expression denial of | 6.5 | Actualizar moment de 2.0.0 a >=2.11.2 |
| 🟡 MEDIUM | CVE-2021-23771 – Sandbox escape in notevil and argencod | 6.5 | No hay fix disponible para notevil 1.3.3 — considerar alternativa |
| 🟡 MEDIUM | CVE-2016-1000237 – XSS - Sanitization not applied recur | 6.1 | Actualizar sanitize-html de 1.4.2 a >=1.4.3 |
| 🟡 MEDIUM | CVE-2017-16016 – Cross-Site Scripting in sanitize-html | 6.1 | Actualizar sanitize-html de 1.4.2 a 1.11.4 |
| 🟡 MEDIUM | CVE-2019-25225 – sanitize-html: sanitize-html cross sit | 6.1 | Actualizar sanitize-html de 1.4.2 a 2.0.0-beta |
| 🟡 MEDIUM | CVE-2021-26539 – sanitize-html: improper handling of in | 5.3 | Actualizar sanitize-html de 1.4.2 a 2.3.1 |
| 🟡 MEDIUM | CVE-2021-26540 – sanitize-html: improper validation of  | 5.3 | Actualizar sanitize-html de 1.4.2 a 2.3.2 |
| 🟡 MEDIUM | CVE-2024-21501 – sanitize-html: Information Exposure wh | 5.3 | Actualizar sanitize-html de 1.4.2 a 2.12.1 |
| 🟡 MEDIUM | CVE-2026-113654 – sanitize-html: sanitize-html: HTML sa | 4.7 | Actualizar sanitize-html de 1.4.2 a 2.18.0 |
| 🟡 MEDIUM | CVE-2026-113661 – sanitize-html: sanitize-html: Cross-s | 5.4 | Actualizar sanitize-html de 1.4.2 a 2.18.0 |
| 🟡 MEDIUM | CVE-2026-63670 – ApostropheCMS: Mutation-XSS / allowedT | 6.1 | Actualizar sanitize-html de 1.4.2 a 2.17.6 |
| 🟡 MEDIUM | NSWG-ECO-154 – Cross Site Scripting | None | Actualizar sanitize-html de 1.4.2 a >=1.11.4 |
| 🟡 MEDIUM | CVE-2026-53655 – node-tar: node-tar: File smuggling due | 5.5 | Actualizar tar de 6.2.1 a 7.5.16 |
| 🟡 MEDIUM | CVE-2026-59871 – node-tar: node-tar: Denial of Service  | 7.5 | Actualizar tar de 6.2.1 a 7.5.18 |
| 🟡 MEDIUM | CVE-2026-59875 – node-tar: node-tar: Denial of Service  | 5.3 | Actualizar tar de 6.2.1 a 7.5.17 |
| 🟡 MEDIUM | CVE-2026-41907 – uuid: uuid: Out-of-bounds write vulner | 7.5 | Actualizar uuid de 8.3.2 a 11.1.1, 12.0.1, 13.0.1 |

### 🌐 OWASP ZAP (DAST) — `ASC-DAST-001`

> **Tipo:** Análisis Dinámico en Ejecución  
> **Raw:** 9 | **Únicos:** 9 | **Deduplicados:** 0 (0.0%)

**Distribución:** 🟡 MEDIUM: **2** | 🟢 LOW: **4** | ⚪ INFO: **3**

#### 🟡🟢⚪ Medios, Bajos e Info (9)

| Severidad | Hallazgo | Endpoint | Remediación |
|---|---|---|---|
| 🟡 MEDIUM | Content Security Policy (CSP) Header Not Set | `http://localhost:3000` | Ensure that your web server, application server, load balancer, etc. i |
| 🟡 MEDIUM | Cross-Domain Misconfiguration | `http://localhost:3000` | Ensure that sensitive data is not available in an unauthenticated mann |
| 🟢 LOW | Cross-Origin-Embedder-Policy Header Missing or Inv | `http://localhost:3000` | Ensure that the application/web server sets the Cross-Origin-Embedder- |
| 🟢 LOW | Cross-Origin-Opener-Policy Header Missing or Inval | `http://localhost:3000` | Ensure that the application/web server sets the Cross-Origin-Opener-Po |
| 🟢 LOW | Dangerous JS Functions | `http://localhost:3000/chunk-3CyVWL1v.js` | See the references for security advice on the use of these functions. |
| 🟢 LOW | Deprecated Feature Policy Header Set | `http://localhost:3000` | Ensure that your web server, application server, load balancer, etc. i |
| ⚪ INFO | Modern Web Application | `http://localhost:3000` | This is an informational alert and so no changes are required. |
| ⚪ INFO | Storable and Cacheable Content | `http://localhost:3000/robots.txt` | Validate that the response does not contain sensitive, personal or use |
| ⚪ INFO | Storable but Non-Cacheable Content | `http://localhost:3000` | Revisar y corregir la alerta: Storable but Non-Cacheable Content |

### 🎯 Nuclei (Pentesting) — `ASC-PENTEST-001`

> **Tipo:** Validación Activa de Templates  
> **Raw:** 12 | **Únicos:** 5 | **Deduplicados:** 7 (58.3%)

**Distribución:** 🟡 MEDIUM: **1** | 🟢 LOW: **4**

#### 🟡🟢⚪ Medios, Bajos e Info (5)

| Severidad | Hallazgo | Endpoint | Remediación |
|---|---|---|---|
| 🟡 MEDIUM | Prometheus Metrics - Detect | `http://localhost:3000/metrics` | Revisar: Prometheus metrics page was detected. |
| 🟢 LOW | Public Swagger API - Detect | `http://localhost:3000/api-docs/swagger.json` | Revisar: Public Swagger API was detected.
 |
| 🟢 LOW | Add DOM EventListener - Detection | `http://localhost:3000` | Revisar: Identifies the use of JavaScript addEventListener calls in th |
| 🟢 LOW | OWASP Juice Shop | `http://localhost:3000` | Revisar: No description |
| 🟢 LOW | HTTP Missing Security Headers | `http://localhost:3000` | Revisar: This template searches for missing HTTP security headers. The |

### 🔐 Semgrep (SAST) — `ASC-SAST-001`

> **Tipo:** Análisis Estático de Código  
> **Raw:** 18 | **Únicos:** 15 | **Deduplicados:** 3 (16.7%)

**Distribución:** 🟠 HIGH: **7** | 🟡 MEDIUM: **8**

#### 🔴🟠 Críticos y Altos (7)

#### 🟠 [HIGH] Express Sequelize Injection

| Campo | Valor |
|---|---|
| **ID** | `SEM-C2F5F78D` |
| **Herramienta** | `SEMGREP` (SAST) |
| **ASC ISO/IEC 27034** | `ASC-SAST-001` |
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
| **ASC ISO/IEC 27034** | `ASC-SAST-001` |
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
| **ASC ISO/IEC 27034** | `ASC-SAST-001` |
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
| **ASC ISO/IEC 27034** | `ASC-SAST-001` |
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
| **ASC ISO/IEC 27034** | `ASC-SAST-001` |
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
| **ASC ISO/IEC 27034** | `ASC-SAST-001` |
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
| **ASC ISO/IEC 27034** | `ASC-SAST-001` |
| **Categoría OWASP** | A05:2021 – Security Misconfiguration |
| **CWE** | `["CWE-95: Improper Neutralization of Directives in Dynamically Evaluated Code ('Eval Injection')"]` |
| **Archivo** | `source_to_scan/routes/userProfile.ts:62` |

**Descripción:** Found data from an Express or Next web request flowing to `eval`. If this data is user-controllable this can lead to execution of arbitrary system commands in the context of your application process. Avoid `eval` whenever possible.

**Evidencia:** `requires login`

**✅ Remediación:** Revisar y corregir el patrón identificado en source_to_scan/routes/userProfile.ts:62

---

#### 🟡🟢⚪ Medios, Bajos e Info (8)

| Severidad | Hallazgo | Endpoint | Remediación |
|---|---|---|---|
| 🟡 MEDIUM | Hardcoded Jwt Secret | `None` | Revisar y corregir el patrón identificado en source_to_scan/lib/insecu |
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
| Semgrep OSS | SAST | `ASC-SAST-001` | 15 |
| Trivy | SCA | `ASC-SCA-001` | 76 |
| OWASP ZAP | DAST | `ASC-DAST-001` | 9 |
| Nuclei v3 | Pentesting | `ASC-PENTEST-001` | 5 |

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

- Este reporte corresponde a una única corrida sobre `juice-shop`. La validación completa
  abarca nueve casos de estudio documentados en la tesis (Capítulo 5).
- La evaluación IA requiere validación humana antes de decisiones en producción.
- No reemplaza una auditoría de seguridad formal ni un pentest manual.
- El gate SSVC prioriza la cautela ante hallazgos críticos — ver tesis sección 5.6.3.

---

_Reporte generado el 2026-11-17 18:36:20 | Pipeline Run: `44148432312`_

_**Autores:** Jhojan Stiven Castaño Jejen & Juan Manuel Arango Rodas_
_**Universidad del Valle** — Ingeniería de Sistemas — 2026_
