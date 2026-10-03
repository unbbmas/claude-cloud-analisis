from helpers import *
from data import *

holiday = {2021: "Sí (dom.)", 2026: "Sí (sáb.)"}


def build(out):
    D = Doc(6, "Análisis de Cash Flow")
    D.h1("6.1 Operating Cash Flow Trends")
    rows = []
    for y in YA:
        e = op[y] + da[y]
        rows.append([f"FY2/{y}", n(ni[y]), n(ocf[y]), (n(ocf[y] / ni[y], 1) + "x") if ni[y] > 0 else "n.s.", n(e), pct(ocf[y] / e * 100, 0), holiday.get(y, "No")])
    D.table(["Ejercicio", "BN", "OCF", "OCF/BN", "EBITDA", "OCF/EBITDA", "¿Cierre en festivo?"], rows, size=8)
    D.src(TIKR + "; Yuho FY2/2022-26 p.2")
    D.p("🔴 **El OCF anual no sirve para analizar la empresa**: está dominado por el calendario de cobros y pagos. FY2/2020 (+3.557) y FY2/2026 (+3.980) están inflados por pagos a proveedores desplazados; FY2/2022 (−2.311) es la reversión del cierre en domingo de feb-2021. Lo significativo es la **suma de varios años**.")
    D.calc(f"OCF acumulado FY2/2019-2026 = {n(sum(ocf.values()))} M JPY frente a un BN acumulado de {n(sum(ni.values()))} → conversión del {n(sum(ocf.values()) / sum(ni.values()) * 100)}%, inflada por el cierre de feb-2026. Excluyendo FY2/2026: OCF FY2/2019-25 = {n(sum(ocf[y] for y in range(2019, 2026)))} vs BN {n(sum(ni[y] for y in range(2019, 2026)))} (conversión del {n(sum(ocf[y] for y in range(2019, 2026)) / sum(ni[y] for y in range(2019, 2026)) * 100)}%).")
    D.h2("Detalle de FY2/2026")
    D.table(["Partida", "M JPY"], [
        ["Bº antes de impuestos", "1.167"], ["+ Amortización", "94"], ["Δ Clientes", "−2.234"], ["Δ Existencias", "−235"],
        ["**Δ Proveedores (efecto festivo)**", "**+5.208**"], ["Δ Acreedores varios", "+647"], ["Otros", "−148"],
        ["Subtotal", "4.499"], ["Intereses y dividendos netos", "−29"], ["Impuestos pagados (netos)", "−482"], ["Reestructuración", "−8"], ["**OCF**", "**3.980**"],
    ])
    D.src(YUHO[2026] + ", p.58")

    D.h1("6.2 Free Cash Flow")
    rows = []
    for y in YA:
        f = ocf[y] - capex[y]
        rows.append([f"FY2/{y}", n(ocf[y]), n(-capex[y]), n(f), pct(f / sales[y] * 100, 2), pct(f / MCAP * 100), (n(f / ni[y], 1) + "x") if ni[y] > 0 else "n.s."])
    D.table(["Ejercicio", "OCF", "CapEx", "FCF", "Margen FCF", "FCF yield (cap. actual)", "FCF/BN"], rows, size=8)
    D.calc(f"FCF = OCF − CapEx (material + inmaterial). FCF yield = FCF / capitalización actual (835 × {SH:,} acciones = {n(MCAP)} M JPY).".replace(",", "."))

    D.h2("💡 FCF NORMALIZADO y FCF yield sobre normalizado (obligatorio)")
    fa = sum(ocf[y] - capex[y] for y in range(2019, 2026)) / 7
    D.table(["Método", "Cálculo", "FCF normalizado (M JPY)"], [
        ["A. Media de 7 años (FY2/2019-25)", f"Suma del FCF de FY2/2019-25 = 3.078 / 7 (el ciclo festivo feb-2021/feb-2022 se compensa)", f"**{n(fa)}**"],
        ["B. Media de 8 años ajustada", "FCF FY2/2019-26 (6.831) − exceso de proveedores por el festivo de feb-2026 (≈2.970) = 3.861 / 8", "**483**"],
        ["C. NOPAT de mitad de ciclo", "BO normalizado 1.000 × (1 − 34%) = 660 + amortización 90 − CapEx 150 − Δ circulante por crecimiento (3% × 8,5% × 106.000 ≈ 270) + resultado financiero neto ≈ +10", "**340**"],
        ["**Base**", "Media de A, B y C = (440 + 483 + 340)/3 ≈ 421", "**≈420**"],
    ], size=8)
    ev_n = MCAP - 1500
    D.table(["Métrica", "Conservador", "**Base**", "Optimista"], [
        ["FCF normalizado (M JPY)", "300", "**420**", "550"],
        ["FCF normalizado por acción (JPY)", n(300 / SH * 1e6, 1), f"**{n(420 / SH * 1e6, 1)}**", n(550 / SH * 1e6, 1)],
        [f"**FCF yield sobre capitalización ({n(MCAP)} M JPY)**", pct(300 / MCAP * 100), f"**{pct(420 / MCAP * 100)}**", pct(550 / MCAP * 100)],
        [f"EV normalizado (cap. − caja neta normalizada 1.500) = {n(ev_n)} M JPY", "", "", ""],
        ["**FCF yield sobre EV normalizado**", pct(300 / ev_n * 100), f"**{pct(420 / ev_n * 100)}**", pct(550 / ev_n * 100)],
        ["P/FCF normalizado", n(MCAP / 300, 1) + "x", f"**{n(MCAP / 420, 1)}x**", n(MCAP / 550, 1) + "x"],
    ], size=8.5)
    D.calc(f"FCF yield normalizado (base) = 420 / {n(MCAP)} = {pct(420 / MCAP * 100)}. Escenario conservador: BO de 700 (nivel del LTM de 912 con más presión). Optimista: BO de 1.250 (recuperación al margen de 1,2%).")
    D.box(f"🟢 **FCF yield normalizado ≈{pct(420 / MCAP * 100)} sobre capitalización** (rango {pct(300 / MCAP * 100)}-{pct(550 / MCAP * 100)}) y **≈{pct(420 / ev_n * 100)} sobre EV normalizado**: atractivo para una empresa sin deuda. 🔴 **Condición:** que el BO vuelva a ≈1.000 M JPY. Si el 1T FY2/2027 (BO de 8) refleja una nueva normalidad, el FCF normalizado caería a ≈100-150 M JPY (yield del 2-3%).", fill="FFF4E5")

    D.h1("6.3 Cash Burn Rate")
    D.p("No aplica: la empresa es FCF positiva en el ciclo (FCF acumulado de 8 años de +6.831 M JPY, ≈+3.860 ajustado). En el peor ejercicio (FY2/2022, efecto calendario) el FCF fue de −2.367 M JPY, cubierto con préstamos bancarios a corto (+1.700).")

    D.h1("6.4 Sostenibilidad de las Operaciones")
    D.table(["Fuente / necesidad", "M JPY", "Comentario"], [
        ["Caja (may-2026)", "7.567", "Inflada por el cierre en domingo"],
        ["Caja normalizada (estimada)", "≈4.000-5.000", "💡"],
        ["Deuda bancaria a corto", "3.625", "Renovable"],
        ["Dividendo anual (30 JPY)", "≈182", "Cubierto ≈4x por el BN previsto (758)"],
        ["CapEx anual", "≈150-300", "Asset-light"],
        ["Alquileres no cancelables", "742", "Compromisos de leasing operativo"],
    ], size=8.5)
    D.p("🟢 **Sostenible**: sin vencimientos a largo plazo ni CapEx relevante; las necesidades son de circulante, financiadas por proveedores y bancos. 🟡 El riesgo es de **rentabilidad**, no de liquidez.")

    D.h1("6.5 CapEx y FCF: mantenimiento vs crecimiento")
    rows = []
    for y in Y:
        m = min(capex[y], da[y]); g = max(capex[y] - da[y], 0)
        rows.append([f"FY2/{y}", n(capex[y]), n(m), n(g), n(ocf[y] - capex[y]), n(ni[y] + da[y] - m)])
    D.table(["Ejercicio", "CapEx", "💡 Mantenimiento", "💡 Crecimiento/sistemas", "FCF reportado", "«Owner earnings» (BN + D&A − mant.)"], rows, size=8)
    D.p("🟢 El CapEx de mantenimiento es mínimo (≈50-90 M JPY). Los «owner earnings» (sin circulante) siguen al BN: 288 → 590 → 1.214 → 1.002 → 778. La caída de 2025-26 se debe al **beneficio**, no a la inversión.")

    D.h1("Conclusión de la Sección 6")
    D.box(f"🟢 Negocio **asset-light con CapEx mínimo** y FCF normalizado de ≈420 M JPY (**FCF yield normalizado del {pct(420 / MCAP * 100)}**). 🔴 El OCF anual está distorsionado por el calendario: hay que mirar medias de varios años. 🔴 La sostenibilidad del FCF normalizado depende de que el margen operativo vuelva a ≈1%; el 1T FY2/2027 lo pone en duda.", fill="FFF4E5")
    return D.save(out, "Analisis_de_Cash_Flow")
