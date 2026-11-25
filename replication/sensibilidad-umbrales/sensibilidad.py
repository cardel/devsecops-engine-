"""Sensibilidad de la compuerta tradicional a sus umbrales.

Regla del codigo (scripts/gate.py, traditional_gate, lineas 69 a 90 del motor):
FAIL si CRITICAL >= critical_min (por defecto 1, fail_on_critical), o
HIGH >= high_min (5); si no, CONDITIONAL si MEDIUM >= medium_min (20); si no,
PASS. Un MEDIUM alto nunca baja un FAIL (gate.py linea 85). La version previa
(regla del articulo, FAIL/PASS con comparacion estricta) quedo en
sensibilidad_regla-articulo.py.
Fuente por caso: findings.json (summary.by_severity) donde existe; si no, la
tabla tab:consolidated del manuscrito (CRITICAL y HIGH; MEDIUM desconocido).
Solo biblioteca estandar.
"""
import csv
import json
import os

AQUI = os.path.dirname(os.path.abspath(__file__))
REPORTES = os.path.join(AQUI, "..", "v1.3-reports")
INF = float("inf")

JSON_CASOS = {
    "Juice Shop": ("juice-shop", "alto"),
    "FitFusion": ("fitfusion-backend", "alto"),
    "SecureTaskAPI": ("secure-task-api", "medio"),
    "SimpleHealthAPI": ("simple-health-api", "bajo"),
}
# (CRITICAL, HIGH) de tab:consolidated; MEDIUM no esta en el manuscrito.
TABLA = {"WebGoat": (9, 55, "alto"), "DVWA": (65, 178, "alto"),
         "PyGoat": (67, 1703, "alto")}
ORDEN = ["Juice Shop", "FitFusion", "WebGoat", "DVWA", "PyGoat",
         "SecureTaskAPI", "SimpleHealthAPI"]

CRIT = [1, 2, 5]
HIGH = [1, 5, 10, 15, 20, 50, 100]
MED = [10, 20, 50, 100, INF]
BASE = (1, 5, 20)


def cargar():
    casos = {}
    for nombre, (carpeta, riesgo) in JSON_CASOS.items():
        ruta = os.path.join(REPORTES, carpeta, "findings.json")
        with open(ruta, encoding="utf-8") as f:
            sev = json.load(f)["summary"]["by_severity"]
        casos[nombre] = dict(c=sev["CRITICAL"], h=sev["HIGH"],
                             m=sev["MEDIUM"], riesgo=riesgo,
                             fuente="findings.json")
    for nombre, (c, h, riesgo) in TABLA.items():
        casos[nombre] = dict(c=c, h=h, m=None, riesgo=riesgo,
                             fuente="tab:consolidated (MEDIUM no disponible)")
    return casos


def decide(caso, cmin, hmin, mmin):
    if caso["c"] >= cmin or caso["h"] >= hmin:
        return "FAIL"
    if caso["m"] is None:
        return "INDETERMINADO"
    return "CONDITIONAL" if caso["m"] >= mmin else "PASS"


def etiqueta(v):
    return "sin_limite" if v == INF else str(v)


def main():
    casos = cargar()
    filas = []
    for nombre in ORDEN:
        caso = casos[nombre]
        base = decide(caso, *BASE)
        for cmin in CRIT:
            for hmax in HIGH:
                for mmax in MED:
                    d = decide(caso, cmin, hmax, mmax)
                    filas.append([nombre, caso["riesgo"], caso["c"], caso["h"],
                                  "" if caso["m"] is None else caso["m"],
                                  caso["fuente"], cmin, hmax, etiqueta(mmax),
                                  base, d, int(d != base)])
    ruta = os.path.join(AQUI, "sensibilidad.csv")
    with open(ruta, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["caso", "riesgo", "critical", "high", "medium", "fuente",
                    "critical_min", "high_min", "medium_min", "base",
                    "decision", "cambia"])
        w.writerows(filas)

    print("Celdas por caso:", len(CRIT) * len(HIGH) * len(MED))
    for nombre in ORDEN:
        caso = casos[nombre]
        propias = [x for x in filas if x[0] == nombre]
        cambian = [x for x in propias if x[-1]]
        indet = [x for x in propias if x[10] == "INDETERMINADO"]
        print(f"\n{nombre} (riesgo {caso['riesgo']}; C={caso['c']} H={caso['h']}"
              f" M={caso['m']}; fuente: {caso['fuente']}) base="
              f"{propias[0][9]}; celdas que cambian: {len(cambian)}; "
              f"indeterminadas: {len(indet)}")
        if cambian:
            cm = sorted({x[6] for x in cambian})
            hm = sorted({x[7] for x in cambian})
            print("  critical_min en", cm, "| high_min en", hm)
            for x in cambian:
                print("   ", x[6], x[7], x[8], "->", x[10])
    for nombre in ["SecureTaskAPI", "SimpleHealthAPI"]:
        caso = casos[nombre]
        # menor high_min con el que el caso deja de ser FAIL por HIGH
        hm = caso["h"] + 1
        print(f"\n{nombre}: C={caso['c']} H={caso['h']} M={caso['m']}; "
              f"high_min minimo para no fallar = {hm}; con medium_min=20: "
              f"{decide(caso, 1, hm, 20)}; menor medium_min que da PASS = "
              f"{caso['m'] + 1}")
    print("\nCasos de alto riesgo con PASS en alguna celda:")
    for nombre in ORDEN:
        caso = casos[nombre]
        if caso["riesgo"] == "alto":
            for dec in ("PASS", "CONDITIONAL", "INDETERMINADO"):
                n = sum(1 for x in filas if x[0] == nombre and x[10] == dec)
                print(" ", nombre, dec, n, "celdas")


if __name__ == "__main__":
    main()
