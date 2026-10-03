from helpers import *
from data import *

prov = {2021: 540, 2022: 407, 2023: 296, 2024: -191, 2025: -22, 2026: 25}  # dotación (+) / reversión (−) de insolvencias en SG&A
nonop_rev = {2025: 186}


def build(out):
    D = Doc(5, "Análisis de Rentabilidad")
    D.h1("5.1 Evolución de Márgenes")
    rows = []
    for y in Y:
        ebitda = op[y] + da[y]
        rows.append([f"FY3/{y}", pct(gp[y] / sales[y] * 100), pct(sga[y] / sales[y] * 100), pct(ebitda / sales[y] * 100, 2), pct(op[y] / sales[y] * 100, 2), pct(ordinary[y] / sales[y] * 100, 2), pct(ni[y] / sales[y] * 100, 2)])
    D.table(["Ejercicio", "Margen bruto", "SG&A/Ventas", "Margen EBITDA", "Margen operativo", "Margen ordinario", "Margen neto"], rows)
    D.src("Cálculo propio sobre las cuentas de resultados consolidadas (Yuho FY3/2021-FY3/2026)")
    D.p("1T FY3/2027: margen bruto **8,98%** (1.056/11.764), margen operativo **3,25%** (382/11.764) y margen neto **2,55%** (300/11.764), frente a 8,28%, 2,38% y 1,86% en el 1T FY3/2026. 🟢")
    D.src(Q1 + ", p.6")
    D.h2("Desglose de SG&A y factores que explican el margen")
    rows = []
    for y in Y:
        rows.append([f"FY3/{y}", n(sga[y]), n(fund[y]), n(prov[y]), n(sga[y] - fund[y] - prov[y]), n(op[y])])
    D.table(["Ejercicio", "SG&A total", "Aportación al fondo de estabilización", "Dotación (+)/reversión (−) de insolvencias", "Resto de SG&A", "BO"], rows, size=8.5)
    D.src("Notas «販売費及び一般管理費» de cada Yuho (consolidado)")
    D.p("**Lectura:** el «resto de SG&A» (personal, fletes y almacenaje de 537-613, amortización corporativa, etc.) es estable en ≈1.430-1.530 M JPY. La volatilidad viene de (i) el **margen bruto** (diferencial grano-precio) y (ii) dos partidas «semi-cíclicas»: la aportación al **fondo** y las **provisiones por clientes**, que en FY3/2021-23 restaron entre 400 y 1.200 M JPY por año.")

    D.h1("5.2 EBITDA Ajustado vs Reportado")
    rows = []
    adj_list = []
    for y in Y:
        ebitda = op[y] + da[y]
        adj = ebitda + prov[y]
        adj_list.append(adj)
        rows.append([f"FY3/{y}", n(op[y]), n(da[y]), n(ebitda), n(prov[y]), n(adj), pct(adj / sales[y] * 100, 2)])
    D.table(["Ejercicio", "BO reportado", "+ Amortización", "= EBITDA reportado", "+ Dotación neta de insolvencias", "= EBITDA ajustado", "Margen ajustado"], rows, size=8.5)
    D.calc(f"EBITDA ajustado medio FY3/2021-26 = {n(sum(adj_list) / 6)} M JPY. Pérdida media por insolvencias en el ciclo = (540+407+296−191−22+25)/6 = 176 M JPY/año. "
           "**EBITDA normalizado (mitad de ciclo) ≈ 1.330 − 176 ≈ 1.150 M JPY** y **BO normalizado ≈ 600 M JPY** (media FY3/2020-26: 571).")
    D.table(["Partida excluida del ajuste", "Justificación"], [
        ["Deterioros de activos (168 / 644 / 633)", "Partida extraordinaria por debajo del BO. Recurrente en la práctica: tres años seguidos en ganadería. 🔴 No se suma al EBITDA, pero se tiene en cuenta en la valoración"],
        ["Compensación por reubicación (331, FY3/2023) y venta de terreno (395, FY3/2024)", "Extraordinarios no recurrentes; ya fuera del BO"],
        ["Reversión de provisión no operativa (186, FY3/2025)", "No operativo; se excluye"],
        ["Aportación al fondo de estabilización", "🟡 **No se ajusta**: es un coste real y recurrente del negocio, aunque cíclico"],
    ], size=8.5)

    D.h1("5.3 Comparación con Competidores")
    D.table(["Métrica (FY3/2026)", "Nichiwa (2055)", "Feed One (2060)", "Chubu Shiryo (2053)", "Higashimaru (2058)", "Posición Nichiwa"], [
        ["Ventas (M JPY)", "45.579", "290.675", "211.814", "13.332", "Pequeño"],
        ["Margen operativo", "3,19%", "2,78%", "3,11%", "3,26%", "🟡 En línea (pico de ciclo)"],
        ["Margen ordinario", "3,16%", "2,96%", "3,38%", "≈3,8% ⚠️", "🟡"],
        ["Margen neto", "0,83%", "2,19%", "2,62%", "n.d.", "🔴 Deterioros"],
        ["ROE", "2,0%", "≈11,0%", "≈7,9%", "n.d.", "🔴 −6 a −9 pp"],
        ["ROA (BN/activo)", "1,25%", "≈5% ⚠️", "≈5,1%", "n.d.", "🔴"],
        ["ROIC (NOPAT/CI)", "7,2%", "n.d.", "n.d.", "n.d.", "🟡"],
        ["Solvencia (FP/AT)", "61,8%", "46,4%", "66,8%", "n.d.", "🟢"],
        ["Margen operativo medio de 6 años", "1,2%", "n.d. (≈2% ⚠️)", "n.d. (≈2-2,5% ⚠️)", "n.d.", "🔴 Inferior en el ciclo"],
    ], size=8)
    D.src("Nichiwa: Yuho FY3/2026. Feed One: resultados FY3/2026 (ventas 290.675, BO 8.091, Bº ordinario 8.612, BN 6.377), ROE 10,97% y solvencia 46,4% (Monex Scouter/kabuyoho, sep-2026). Chubu Shiryo: FY3/2026 (ventas 211.814, BO 6.584, Bº ordinario 7.168, BN 5.551; activo 108.935; PN 72.824; ROE 7,9%; solvencia 66,8%) vía edinetdb/TDnet. Higashimaru: ventas 13.332, BO 434 (kabuyoho/logmi). Todas las búsquedas a 3-oct-2026; ⚠️ datos secundarios no verificados contra los documentos originales")
    D.calc("ROA de Chubu = 5.551/108.935 = 5,1%. Margen ordinario de Higashimaru ≈ 512/13.332 (el dato de 512 puede ser acumulado a 3T) ⚠️.")
    D.h2("Descomposición DuPont del ROE de Nichiwa")
    rows = []
    for y in Y:
        nm_ = ni[y] / sales[y]; at = sales[y] / ((ta[y] + ta[y - 1]) / 2); lev = ((ta[y] + ta[y - 1]) / 2) / ((equity[y] + equity[y - 1]) / 2)
        rows.append([f"FY3/{y}", pct(nm_ * 100, 2), n(at, 2) + "x", n(lev, 2) + "x", pct(nm_ * at * lev * 100, 2)])
    D.table(["Ejercicio", "Margen neto", "Rotación de activos", "Apalancamiento", "ROE"], rows)
    D.p("🔴 La rotación (≈1,5-1,9x) y el apalancamiento (≈1,6-1,7x) son normales para el sector. **El ROE bajo se debe enteramente al margen neto**, lastrado por (i) un margen bruto estructuralmente fino, (ii) las aportaciones al fondo y las insolvencias, y (iii) los deterioros del segmento ganadero. A esto se suma el exceso de caja: con 9.390 M JPY en depósitos casi sin rendimiento (intereses cobrados de 18 M JPY), el ROE sobre capital operativo sería mayor.")
    D.calc("ROE sobre capital operativo FY3/2026 ≈ (BN 378 − intereses netos de caja ≈ 0) / (PN 19.039 − caja neta 5.028 − valores 1.908) = 378 / 12.103 = 3,1%. Sigue siendo bajo: el problema no es solo la caja ociosa.")

    D.h1("Conclusión de la Sección 5")
    D.box("🔴 **Rentabilidad estructuralmente pobre**: ROE medio de 1,5% y margen operativo medio de 1,2% en seis años. FY3/2026 es un **pico** (margen operativo de 3,2%, el más alto de la serie), en línea con los grandes del sector solo en el mejor momento del ciclo. 🟡 El EBITDA ajustado por insolvencias es más estable (≈1.100-2.000 M JPY), lo que soporta una valoración por EV muy baja (Sección 10).", fill="FDECEA")
    return D.save(out, "Analisis_de_Rentabilidad")
