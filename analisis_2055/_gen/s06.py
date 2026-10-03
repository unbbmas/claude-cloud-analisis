from helpers import *
from data import *


def build(out):
    D = Doc(6, "Análisis de Cash Flow")
    D.h1("6.1 Operating Cash Flow Trends")
    rows = []
    for y in range(2017, 2027):
        conv = ocf[y] / ni[y]
        e = (op[y] + da[y]) if y in op else None
        rows.append([f"FY3/{y}", n(ni[y]), n(ocf[y]), n(conv, 1) + "x", n(e) if e else "n.d.", (pct(ocf[y] / e * 100, 0) if e else "n.d.")])
    D.table(["Ejercicio", "BN", "Flujo operativo (OCF)", "OCF/BN", "EBITDA", "OCF/EBITDA"], rows)
    D.src("FY3/2017-21: " + YUHO[2021] + " p.2; FY3/2022-26: " + YUHO[2026] + " p.2 y estados de flujos de cada Yuho")
    D.p("🟡 La conversión de caja es **muy volátil** y está dominada por el capital circulante: en FY3/2022-23 el grano caro inflaba clientes y existencias (OCF de −1.038 y −1.533) y en FY3/2024-25 el proceso se invirtió (+2.052 y +2.444). **Media de 10 años del OCF: 970 M JPY/año**, unas 3,1x la media del BN de 10 años (312), gracias a una amortización y unas provisiones no monetarias elevadas.")
    D.h2("Detalle FY3/2026")
    D.table(["Partida OCF FY3/2026", "M JPY"], [
        ["Bº antes de impuestos", "807"], ["+ Amortización", "511"], ["+ Deterioros (no monetarios)", "633"],
        ["− Aplicación de provisiones de insolvencias", "−373"], ["Δ Clientes", "−165"], ["Δ Existencias", "+69"],
        ["Δ Proveedores", "−317"], ["Otros", "+442"], ["Subtotal", "1.607"], ["Intereses y dividendos netos", "−22"],
        ["Impuestos pagados", "−430"], ["**OCF**", "**1.154**"],
    ])
    D.src(YUHO[2026] + ", p.37")

    D.h1("6.2 Free Cash Flow")
    rows = []
    for y in Y:
        fcf = ocf[y] - capex_cash[y]
        netloan = loans_out[y] - loans_in[y]
        rows.append([f"FY3/{y}", n(ocf[y]), n(-capex_cash[y]), n(fcf), n(-netloan), n(fcf - netloan), pct(fcf / MCAP * 100), n(fcf / ni[y], 1) + "x"])
    D.table(["Ejercicio", "OCF", "CapEx", "FCF", "Préstamos netos a clientes", "FCF tras préstamos", "FCF yield (cap. actual)", "FCF/BN"], rows, size=8)
    D.calc(f"FCF = OCF − CapEx (inmovilizado material + inmaterial). FCF yield = FCF / capitalización actual (346 JPY × 18.111.793 acciones = {n(MCAP)} M JPY). FCF acumulado FY3/2021-26 = 259 M JPY (media de 43/año): **el ciclo del circulante consume casi todo el FCF de los años buenos**.")
    D.h2("💡 FCF NORMALIZADO y FCF yield sobre normalizado (obligatorio)")
    D.p("Como el FCF anual está distorsionado por el circulante (que se neutraliza en el ciclo) y por un CapEx temporalmente bajo, se estima un **FCF normalizado de mitad de ciclo** con tres métodos:")
    D.table(["Método", "Cálculo", "FCF normalizado (M JPY)"], [
        ["A. Medias históricas", "OCF medio de 10 años (970) − CapEx medio de 7 años (728)", "**242**"],
        ["B. NOPAT de mitad de ciclo", "BO normalizado 600 × (1 − 30,6%) = 416 + amortización 540 − CapEx de mantenimiento 600 (≈1,1x D&A por plantas envejecidas) ± ΔWC 0", "**356**"],
        ["C. EBITDA ajustado normalizado", "EBITDA normalizado 1.150 − impuestos sobre BO normalizado (184) − CapEx de mantenimiento 600", "**366**"],
        ["**Base (media B y C, ponderando A)**", "(242 + 356 + 366) / 3 ≈ 321 → redondeo", "**≈330**"],
    ], size=8.5)
    D.table(["Métrica", "Conservador", "**Base**", "Optimista"], [
        ["FCF normalizado (M JPY)", "240", "**330**", "450"],
        ["FCF normalizado por acción (JPY)", "13,3", "**18,2**", "24,8"],
        ["**FCF yield sobre capitalización (6.267 M JPY)**", "3,8%", "**5,3%**", "7,2%"],
        ["EV (cap. − caja neta 5.028) = 1.239 M JPY", "", "", ""],
        ["**FCF yield sobre EV**", "19,4%", "**26,6%**", "36,3%"],
        ["P/FCF normalizado", "26,1x", "**19,0x**", "13,9x"],
    ], size=8.5)
    D.calc("FCF yield normalizado (base) = 330 / 6.267 = 5,3%. Sobre EV = 330 / 1.239 = 26,6%. El supuesto optimista (450) usa un BO de mitad de ciclo de 750 (la media FY3/2024-26 es 1.089, pero contiene el pico).")
    D.box("🟡 **FCF yield normalizado ≈5,3% sobre capitalización** (rango 3,8-7,2%): razonable, sin ser llamativo, para una empresa sin crecimiento. 🟢 **Sobre EV es ≈27%**, porque casi toda la capitalización está respaldada por caja neta. El inversor compra ≈80% caja neta y ≈20% un negocio que genera ≈330 M JPY/año de caja de mitad de ciclo.", fill="FFF4E5")

    D.h1("6.3 Cash Burn Rate")
    D.p("No aplica: la empresa es FCF positiva en el ciclo. Como **prueba de estrés**, en el peor bienio (FY3/2022-23) el FCF acumulado fue de **−4.274 M JPY** (−1.835 y −2.439) y, con dividendos y la recompra, la caja bajó de 9.818 a 5.182 M JPY **sin necesidad de nueva deuda**. 🟢 La caja actual (10.089 M JPY a jun-2026) cubriría ≈2,4 ciclos de estrés equivalentes.")
    D.src(YUHO[2023] + ", p.39; " + Q1 + ", p.5")

    D.h1("6.4 Sostenibilidad de las Operaciones")
    D.table(["Fuente / necesidad", "M JPY", "Comentario"], [
        ["Caja (30-jun-2026)", "10.089", "🔍"],
        ["Línea comprometida no dispuesta", "4.707", "8 bancos (FY3/2026)"],
        ["Valores cotizados (valor de mercado)", "≈1.750", "Toyota Tsusho, Resona, etc. (a mar-2026: 1.665)"],
        ["**Liquidez total disponible**", "**≈16.500**", ""],
        ["Deuda que vence a <12 meses", "≈3.578", "Préstamos a corto renovables"],
        ["Dividendo anual", "≈109", "6 JPY × 18,1 M acciones"],
        ["CapEx de mantenimiento", "≈500-600", ""],
        ["Necesidad de circulante en un shock de grano (peor caso histórico)", "≈2.700-4.300", "FY3/2022-23"],
    ], size=8.5)
    D.p("🟢 **Altamente sostenible.** Incluso en un escenario de estrés severo la empresa conserva más de 8.000 M JPY de liquidez.")

    D.h1("6.5 CapEx y FCF: mantenimiento vs crecimiento (5 años)")
    rows = []
    for y in Y[1:]:
        maint = min(capex_cash[y], da[y]); growth = max(capex_cash[y] - da[y], 0)
        rows.append([f"FY3/{y}", n(capex_cash[y]), n(maint), n(growth), n(ocf[y] - capex_cash[y]), n(ocf[y] - maint)])
    D.table(["Ejercicio", "CapEx total", "💡 Mantenimiento (≈min[CapEx; D&A])", "💡 Crecimiento", "FCF", "FCF «de propietario» (OCF − mantenimiento)"], rows, size=8.5)
    D.calc("No hay desglose oficial. El supuesto de mantenimiento ≈ amortización es estándar; con plantas de 40-60 años probablemente infraestima el mantenimiento real.")
    D.p("🔴 En FY3/2025-26 el CapEx (448 y 381) estuvo **por debajo de la amortización** (588 y 511). Parte del FCF reciente es «prestado» del futuro.")

    D.h1("Conclusión de la Sección 6")
    D.box("🟡 FCF real muy volátil (acumulado de 6 años de solo 259 M JPY) por el circulante del grano. **FCF normalizado ≈330 M JPY → FCF yield normalizado del 5,3% sobre capitalización y del ≈27% sobre EV.** 🟢 La liquidez (≈16.500 M JPY entre caja, línea comprometida y valores) elimina cualquier riesgo de financiación. 🔴 La calidad del FCF reciente está inflada por la infrainversión.", fill="FFF4E5")
    return D.save(out, "Analisis_de_Cash_Flow")
