from helpers import *
from data import *


def build(out):
    D = Doc(5, "Análisis de Rentabilidad")
    D.h1("5.1 Evolución de Márgenes")
    rows = []
    for y in YA:
        e = op[y] + da[y]
        rows.append([f"FY2/{y}", pct(gp[y] / sales[y] * 100, 2), pct((gp[y] - op[y]) / sales[y] * 100, 2), pct(e / sales[y] * 100, 2), pct(op[y] / sales[y] * 100, 2), pct(ordinary[y] / sales[y] * 100, 2), pct(ni[y] / sales[y] * 100, 2)])
    rows.append(["1T FY2/2027", "10,18%", "10,16%", "≈0,12%", "0,03%", "0,03%", "−0,02%"])
    D.table(["Ejercicio", "Margen bruto", "SG&A/Ventas", "Margen EBITDA", "Margen operativo", "Margen ordinario", "Margen neto"], rows, size=8)
    D.src(TIKR + "; " + Q1)
    D.h2("Estructura de costes (FY2/2026)")
    D.table(["Partida", "M JPY", "% Ventas", "Δ vs FY2/2025"], [
        ["Margen bruto", "11.786", "11,14%", "−258"],
        ["Fletes y embalaje", "5.294", "5,00%", "+38"],
        ["Sueldos y salarios", "2.427", "2,29%", "−10"],
        ["Alquileres", "1.080", "1,02%", "+21"],
        ["Bienestar social", "399", "0,38%", "−13"],
        ["Bonus (empleados y consejeros)", "86", "0,08%", "−86"],
        ["Amortización", "93", "0,09%", "+10"],
        ["Otros (incl. pensiones e insolvencias)", "1.297", "1,23%", "+31"],
        ["**BO**", "**1.110**", "**1,05%**", "**−250**"],
    ], size=8.5)
    D.src(YUHO[2026] + ", p.54")
    D.p("🔴 El **margen bruto** es la variable crítica: un movimiento de ±0,1 pp equivale a ±106 M JPY de BO (≈10%). 🟡 Los gastos están contenidos (−9 M JPY en FY2/2026 gracias al menor bonus), pero los fletes suben. **Apalancamiento operativo extremo**: con un SG&A casi fijo de ≈10.700 M JPY, cada punto de margen bruto mueve el beneficio un 95%.")

    D.h1("5.2 EBITDA Ajustado vs Reportado")
    D.table(["Ejercicio", "BO", "+ Amortización", "= EBITDA", "Ajustes no recurrentes", "EBITDA ajustado", "EBITDAR (+ alquileres)"], [
        ["FY2/2022", "467", "82", "549", "—", "549", "1.436"],
        ["FY2/2023", "858", "72", "930", "—", "930", "1.819"],
        ["FY2/2024", "1.720", "67", "1.787", "—", "1.787", "2.709"],
        ["FY2/2025", "1.360", "83", "1.443", "Gastos del traslado de sede (no cuantificados ⚠️)", "≈1.443-1.550", "2.501"],
        ["FY2/2026", "1.110", "94", "1.204", "Bonus de consejeros 0 (−43 vs FY2/2025)", "≈1.160", "2.283"],
    ], size=8)
    D.src(TIKR + " (EBITDAR); " + YUHO[2025] + " p.17 (traslado de sede)")
    D.p("🟡 No hay grandes ajustes: Echo no publica un «EBITDA ajustado». Los extraordinarios están **por debajo del BO**: plusvalía de la venta de la sede (205, FY2/2025), venta de valores (+67, FY2/2026), deterioros pequeños (18, FY2/2025) y reestructuración de la escuela (8). 💡 **EBITDA normalizado de mitad de ciclo ≈1.050-1.150 M JPY** (BO ≈1.000 + amortización ≈90).")
    D.calc("BO normalizado ≈ media FY2/2023-26 (858; 1.720; 1.360; 1.110) = 1.262, descontando el pico de FY2/2024 (subidas de precio no repetibles) y la tendencia actual → **≈1.000 M JPY** (margen ≈0,95%).")

    D.h1("5.3 Comparación con Competidores")
    D.table(["Métrica", "Echo (FY2/2026)", "Arata 2733 (FY3/2026)", "Kato Sangyo 9869 (FY9/2025)", "PALTAC 8283", "Itochu Shokuhin 2692 (FY3/2026)", "Posición Echo"], [
        ["Ventas (M JPY)", "105.811", "1.004.749", "≈1.210.000", "≈1.200.000 ⚠️", "≈720.000 ⚠️", "Pequeño"],
        ["Margen operativo", "1,05%", "1,31%", "1,50%", "≈2,5% ⚠️", "1,2-1,5%", "🔴 El más bajo"],
        ["Margen neto", "0,74%", "1,01%", "1,09%", "n.d.", "n.d.", "🔴"],
        ["ROE", "6,6%", "8,4%", "8,1%", "7,5%", "7,3%", "🔴 −1 a −2 pp"],
        ["ROA", "2,1%", "n.d.", "n.d.", "4,2%", "n.d.", "🔴"],
        ["Solvencia", "31,3%", "35,7%", "36,2%", "56,7%", "42,6%", "🟡"],
        ["ROIC (NOPAT/CI)", "≈9,6%", "n.d.", "n.d.", "n.d.", "n.d.", "🟡"],
    ], size=7.5)
    D.src("Arata: FY3/2026 (ventas 1.004.749, BO 13.207, BN 10.130), ROE 8,42%, solvencia 35,7% (kabuyoho, TDnet). Kato Sangyo: FY9/2025 (ventas 1,21 billones, BO 18.200, BN 13.200, ROE 8,1%, solvencia 36,2%) (edinetdb). PALTAC: ROE 7,48%, ROA 4,24%, solvencia 56,7% (Monex). Itochu Shokuhin: margen 1,2-1,47%, ROE 7,3%, solvencia 42,6% (edinetdb). Todas las búsquedas a 3-oct-2026; ⚠️ datos secundarios")
    D.calc("Margen operativo de Arata = 13.207/1.004.749 = 1,31%; margen neto = 10.130/1.004.749 = 1,01%. Kato Sangyo = 18.200/1.210.000 = 1,50% y 13.200/1.210.000 = 1,09%.")
    D.h2("DuPont del ROE de Echo")
    rows = []
    for y in Y:
        nm_ = ni[y] / sales[y]; at = sales[y] / ((ta[y] + ta[y - 1]) / 2); lev = ((ta[y] + ta[y - 1]) / 2) / ((equity[y] + equity[y - 1]) / 2)
        rows.append([f"FY2/{y}", pct(nm_ * 100, 2), n(at, 2) + "x", n(lev, 2) + "x", pct(nm_ * at * lev * 100, 1)])
    D.table(["Ejercicio", "Margen neto", "Rotación de activos", "Apalancamiento", "ROE"], rows)
    D.p("🟢 La **rotación (≈3x)** y el **apalancamiento comercial (≈3x, financiado por proveedores sin coste)** multiplican un margen ínfimo hasta un ROE razonable (6-12%). 🔴 Con margen neto del 0,74%, el ROE depende totalmente de que el margen no caiga: en el 1T FY2/2027 el ROE anualizado es **≈0%**.")

    D.h1("Conclusión de la Sección 5")
    D.box("🔴 **Rentabilidad baja y en descenso**: margen operativo del 1,05% (el menor del grupo de comparables), margen bruto en tendencia bajista y ROE del 6,6% (frente al 12% de FY2/2024), por debajo del coste de capital (≈7-8%). 🟢 La rotación de activos y la financiación de proveedores dan un ROIC del ≈10% en años normales. 🔴 El 1T FY2/2027 marca un **mínimo de rentabilidad**: la clave de la tesis es si es transitorio (cambio puntual de condiciones con un cliente) o estructural.", fill="FDECEA")
    return D.save(out, "Analisis_de_Rentabilidad")
