from helpers import *
from data import *


def build(out):
    D = Doc(8, "Dividendos y Recompras")
    D.h1("8.1 Política de Dividendos")
    D.p("🔍 Política declarada: «mantener el dividendo actual como base, con el **objetivo de un payout consolidado igual o superior al 30%**, y decidir con flexibilidad según las circunstancias». Dos pagos al año (a cuenta en agosto, decidido por el consejo; final en febrero, aprobado por la junta).")
    D.src(YUHO[2026] + ", p.29 «配当政策»")
    rows = []
    for y in YA:
        tot = divpaid[y]
        rows.append([f"FY2/{y}", n(dps[y]) + (" (28+5 extra)" if y == 2024 else ""), n(eps[y], 2), pct(dps[y] / eps[y] * 100, 0) if eps[y] > 0 else "n.s.", n(tot), pct(dps[y] / PRICE * 100, 2)])
    rows.append(["FY2/2027E", "30 (15+15)", "124,81 (prev.) / ≈75 💡", "24% / ≈40%", "≈182", "3,59%"])
    D.table(["Ejercicio", "DPA (JPY)", "BPA", "Payout", "Dividendos pagados en el año (M JPY)", "Yield a 835 JPY"], rows, size=8)
    D.src(TIKR + "; " + YUHO[2026] + " p.3 y p.29; " + Q1 + " p.1")
    D.p("🟢 **Dividendo creciente y nunca recortado** en 8 años (20 → 30 JPY, CAGR +6%) y **yield del 3,6%**. 🔴 El payout de FY2/2026 (23%) quedó **por debajo del objetivo del 30%**: con el BPA de 128,63, un 30% equivaldría a 39 JPY. 🟡 Si el BPA de FY2/2027 cae a ≈75 JPY (escenario base propio), los 30 JPY supondrían un payout del ≈40%, todavía cómodo.")

    D.h1("8.2 Recompras")
    D.table(["Ejercicio", "Recompra (M JPY)", "Acciones en autocartera a cierre", "Comentario"], [
        ["FY2/2019-23", "0", "≈10.400", "Sin recompras"],
        ["FY2/2024", "82", "70.400", "≈60.000 acciones (≈1.370 JPY ⚠️)"],
        ["FY2/2025", "0", "≈39.485", "Reducción de la autocartera (destino no detallado ⚠️)"],
        ["FY2/2026", "0", "41.525", "+2.040 acciones restringidas recuperadas"],
        ["1T FY2/2027", "0", "42.125", "—"],
    ], size=8.5)
    D.src(TIKR + " (recompra 82 M JPY en FY2/2024); Yuho FY2/2022, FY2/2024 y FY2/2026 (自己株式等)")
    D.p("🔴 **Recompras prácticamente inexistentes**, a pesar de cotizar a 0,4-0,5x el valor contable. 🟡 La emisión de acciones restringidas añade +39.000 acciones/año (≈0,65% de dilución), así que el número de acciones crece ligeramente.")

    D.h1("8.3 Capital Allocation")
    D.table(["Uso del capital (acumulado FY2/2022-26)", "M JPY"], [
        ["Flujo operativo (OCF)", "3.573"],
        ["CapEx (material + sistemas)", "−410"],
        ["Venta de la antigua sede (Nishinomiya)", "+454"],
        ["Compra/venta de valores (neto)", "+40"],
        ["Dividendos", "−805"],
        ["Recompras", "−82"],
        ["Variación de la deuda bancaria (2.500 → 1.650)", "−850"],
        ["Otros (minoritarios, leasing)", "−135"],
        ["**Variación de caja (4.446 → 6.231)**", "**+1.785**"],
    ])
    D.src(TIKR + " y estados de flujos de los Yuho FY2/2022-26. Cálculo propio")
    D.calc("El OCF acumulado está inflado en ≈2.970 M JPY por el cierre en festivo de feb-2026: sin ese efecto, la caja «real» apenas habría variado y la deuda neta habría bajado ≈1.000 M JPY en 5 años.")
    D.table(["Opción", "Situación", "Valoración"], [
        ["Reinversión en el negocio", "Mínima (asset-light); sistemas e IA", "🟢 Adecuada"],
        ["M&A", "Pequeñas compras de marca (GOODISH)", "🟡"],
        ["Dividendo", "Yield del 3,6%; payout del 23% < objetivo del 30%", "🟡"],
        ["Recompras", "82 M JPY en 5 años", "🔴 Insuficiente a P/B 0,42x"],
        ["Reducción de deuda", "Deuda a corto, variable", "🟢"],
    ], size=8.5)

    D.h1("Conclusión de la Sección 8")
    D.box("🟢 **Dividendo atractivo y estable (3,6%)**, con 8 años sin recortes, bien cubierto en un año normal. 🔴 Sin recompras relevantes ni plan sobre el P/B, y con payout por debajo de su propio objetivo. 🟡 Un aumento del payout o un programa de recompra serían catalizadores, pero la caída del beneficio en FY2/2027 los hace poco probables a corto plazo.", fill="FFF4E5")
    return D.save(out, "Dividendos_y_Recompras")
