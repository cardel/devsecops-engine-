# Reportes finales de la campaña v1.3 (21-may-2026)

Copias de los artefactos `devsecops-final-report` de GitHub Actions (retención
30 días, ya expirados en GitHub) que Arango y Castaño preservaron y enviaron
por Filen (`/Paperdevops/reporte-*.zip`, recibidos el 15-jul-2026). Son la
evidencia primaria de las Tablas III y IV del manuscrito IEEE.

| Caso | Carpeta | Run | Criticidad | Únicos | Decisión final |
|---|---|---|---|---|---|
| OWASP Juice Shop | `juice-shop/` | 26253680284 | high | 82 (4 CRIT / 38 HIGH) | FAIL |
| FitFusion Backend | `fitfusion-backend/` | (21-may 21:24) | high | 59 (2 CRIT / 29 HIGH) | FAIL |
| SecureTaskAPI | `secure-task-api/` | (21-may 21:20) | medium | 17 (0 CRIT / 11 HIGH) | FAIL (escalado SSVC) |
| SimpleHealthAPI | `simple-health-api/` | 26253101059 | low | 17 (0 CRIT / 11 HIGH) | CONDITIONAL |

Cada carpeta contiene `findings.json` (hallazgos únicos normalizados),
`gate_decision.json` (los tres gates + `f1_metrics`), `ai_evaluation.json`,
`scan_config.json`, `recon_context.json` y `SECURITY_REPORT.md`.

## Discrepancias con el documento de correcciones (julio 2026)

El documento *Correcciones al paper — alineación con datos finales TG v1.3*
declara dos valores que **no** coinciden con estos JSON:

1. **Juice Shop**: el documento y el TG dicen 92 únicos / 5 CRIT; el reporte
   dice 82 / 4 (y ZAP terminó sin hallazgos en esa corrida). El manuscrito usa
   82 / 4 / 38, respaldado por este JSON. Si existe otra corrida que respalde
   92 / 5, hay que archivar su reporte aquí y actualizar la tabla.
2. **SimpleHealthAPI**: el documento dice 15 únicos con 0,0 % de deduplicación;
   ese 15 es exactamente Semgrep+Trivy+ZAP sin contar Nuclei y coincide con la
   tabla v1.2 del TG (corrida donde Nuclei no encontró nada). En la corrida
   final (esta), Nuclei aportó 2 únicos: total 17 (24 crudos, 29,2 % dedup).
   No existe ninguna corrida posterior en el repositorio. El manuscrito usa 17.

Además, la afirmación del documento de que Nuclei confirmó el JWT (CWE-347) en
FitFusion no aparece en `fitfusion-backend/findings.json` (los hallazgos de
Nuclei son cookies, cabeceras y NODE_ENV); el manuscrito no la incluye.

## Totales del manuscrito

Con las dos correcciones anteriores, los totales de la campaña quedan en
**11 571 crudos → 7 494 únicos (35,2 %)** en lugar de los 11 572 → 7 502 del
documento. Los crudos de WebGoat, DVWA y PyGoat provienen del Capítulo 5 del
TG v1.3 (sus reportes no fueron enviados); si se archivan aquí, verificar el
total.
