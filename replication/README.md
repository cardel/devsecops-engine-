# Replication data

This folder holds the data behind the repeated evaluations, the replication
and the sensitivity analysis reported in the article *Comparing Threshold LLM
and SSVC Security Gates in a Reusable DevSecOps Pipeline*.

| Folder | Contents |
|---|---|
| `original-findings/` | Normalized findings of the original campaign for the four cases whose workflow artifacts were still available: Juice Shop, FitFusion Backend, SecureTaskAPI and SimpleHealthAPI. |
| `v1.3-reports/` | Reports of the original campaign for the same four cases, as the engine produced them. |
| `repeticion-ia/` | Repeated AI evaluations over the original findings: five runs per case with LLaMA 3.3 70B and five with GPT-4o-mini. `resumen.csv` lists the decision and the confidence of every run. |
| `replica-2026-11-17/` | Replication of the seven cases. `llama33/` uses LLaMA 3.3 70B as the evaluating model and `con-trivy/` uses GPT-4o-mini. Each case folder keeps the AI evaluation, the three gate decisions and the report; `resumen.csv` summarizes each batch. |
| `sensibilidad-umbrales/` | Script and results of the sensitivity analysis of the traditional gate over 105 threshold combinations per case. |
| `workflows/` | The GitHub Actions workflows that ran the replication and the repeated evaluations. They call the reusable workflow of this branch. |

The raw output of the four analysis tools for the replication is about 380 MB
and is not stored here; it is available from the corresponding author.

The workflows read their API keys and the application secrets from repository
secrets. The test secret of SecureTaskAPI was replaced by a placeholder.
