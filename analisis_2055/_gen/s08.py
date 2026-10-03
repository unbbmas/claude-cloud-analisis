from helpers import *
from data import *


def build(out):
    D = Doc(8, "Dividendos y Recompras")
    D.h1("8.1 Política de Dividendos")
    D.p("🔍 Política declarada: «asegurar reservas internas para reforzar a largo plazo la estructura financiera y la base de gestión, y pagar un **dividendo estable y continuado**». Un único pago anual (dividendo final), con posibilidad estatutaria de dividendo a cuenta, que **nunca se ha utilizado**. Desde la reforma de estatutos, el dividendo lo decide el consejo y no la junta.")
    D.src(YUHO[2026] + ", p.17 «配当政策» y p.20")
    rows = []
    shares = {2017: 19.312, 2018: 19.312, 2019: 19.312, 2020: 19.312, 2021: 19.312, 2022: 18.112, 2023: 18.112, 2024: 18.112, 2025: 18.112, 2026: 18.112}
    parent_payout = {2017: "31,4%", 2018: "20,0%", 2019: "21,3%", 2020: "34,7%", 2021: "382,2%", 2022: "84,3%", 2023: "36,8%", 2024: "25,6%", 2025: "34,4%", 2026: "36,0%"}
    for y in range(2017, 2027):
        tot = dps[y] * shares[y]
        rows.append([f"FY3/{y}", n(dps[y], 0) + (" (6+2 cent.)" if y == 2024 else ""), n(tot, 0), n(eps[y], 2), pct(dps[y] / eps[y] * 100, 0), parent_payout[y], pct(dps[y] / PRICE * 100, 2)])
    rows.append(["FY3/2027E", "6 (previsión)", "109", "16,56 (prev.) / ≈30 💡", "36% / ≈20%", "—", "1,73%"])
    D.table(["Ejercicio", "DPA (JPY)", "Total (M JPY)", "BPA consolidado", "Payout consolidado", "Payout individual (oficial)", "Yield a 346 JPY"], rows, size=8)
    D.src("DPA y payout individual: " + YUHO[2021] + " p.3; " + YUHO[2026] + " p.3; FY3/2027E: " + Q1 + " p.1 (dividendo a cuenta 0, final 6). FY3/2024 incluye 2 JPY de dividendo conmemorativo del centenario")
    D.calc("Total = DPA × acciones en circulación (19,31 M hasta FY3/2021; 18,11 M desde la recompra de feb-2022). Dividend yield = 6/346 = 1,73%.")
    D.p("🔴 **Dividendo plano**: 5-6 JPY en 10 años (solo el extra del centenario en FY3/2024), sin relación con el beneficio, el FCF ni la caja. El payout consolidado de mitad de ciclo ronda el 30-35% y **el dividendo apenas representa el 2,2% de la caja neta al año**. 🟢 El dividendo es muy seguro: el coste anual (≈109 M JPY) es el 1,1% de la caja. ⚠️ Una búsqueda secundaria indica 12 JPY (6+6) para FY3/2027; **el Tanshin oficial muestra dividendo a cuenta 0,00 y final 6,00 (total 6)**. Prevalece la fuente primaria.")

    D.h1("8.2 Recompras")
    D.table(["Ejercicio", "Acciones recompradas", "Importe (M JPY)", "Precio medio (JPY)", "P/VC implícito", "Autocartera a cierre", "Buyback yield"], [
        ["FY3/2021", "≈77 (fracciones)", "0,02", "—", "—", "1.518.877", "0,0%"],
        ["FY3/2022", "**1.200.041**", "**426,3**", "**355**", "**≈0,37x**", "2.718.918", "≈6,0% (sobre la cap. de entonces)"],
        ["FY3/2023", "53", "0,0", "—", "—", "2.718.971", "0,0%"],
        ["FY3/2024", "≈1", "0,0", "—", "—", "2.718.972", "0,0%"],
        ["FY3/2025", "60", "0,0", "—", "—", "2.719.032", "0,0%"],
        ["FY3/2026", "0", "0", "—", "—", "2.719.032", "0,0%"],
    ], size=8)
    D.src(YUHO[2022] + " p.17 (acuerdo del consejo de 24-feb-2022: 1.200.000 acciones por 426.000 miles de JPY, ejecutado el 25-feb-2022); " + YUHO[2026] + " p.16-17 y p.45-46")
    D.p("🟢 La recompra de 2022 fue **muy acertada**: a 355 JPY, un 66% por debajo del valor contable, añadió ≈42 JPY de valor contable por acción a los accionistas que se quedaron. 🔴 Fue un hecho aislado, probablemente para dar salida a un accionista concreto (bloque fuera de mercado, en un solo día). Desde entonces **no hay recompras**, a pesar de que el P/B ha bajado a 0,33x. 🟡 La autocartera (13,05%) **no se ha amortizado**: puede reutilizarse (por ejemplo, para alianzas o intercambios de acciones).")
    D.calc("Efecto en el VC por acción de la recompra de 2022: PN tras la recompra 17.410 / 18,112 M acciones = 961 JPY frente a (17.410 + 426) / 19,312 M = 924 JPY sin recompra → +37-42 JPY/acción (≈+4%).")

    D.h1("8.3 Capital Allocation")
    D.table(["Uso del capital (acumulado FY3/2021-26)", "M JPY", "% de la caja operativa generada"], [
        ["Flujo operativo (OCF) generado", "4.342", "100%"],
        ["CapEx", "−4.083", "94%"],
        ["Préstamos netos a clientes (cobros − concesiones)", "+160", "−4%"],
        ["Venta de activos (terreno FY3/2024)", "+581", "−13%"],
        ["Compra de valores", "−211", "5%"],
        ["Dividendos", "−699", "16%"],
        ["Recompras", "−426", "10%"],
        ["Variación neta de deuda", "+93", "−2%"],
        ["Otros", "−185", "4%"],
        ["**Variación de caja (9.818 → 9.390)**", "**−428**", ""],
    ], size=8.5)
    D.src("Estados de flujos de efectivo FY3/2021-26 (suma de los Yuho). Cálculo propio")
    D.table(["Opción de asignación", "Situación actual", "Valoración"], [
        ["Reinversión en el negocio", "CapEx ≈ amortización; sin proyectos de crecimiento", "🟡"],
        ["M&A", "Ninguna", "🟡"],
        ["Dividendos", "Payout de mitad de ciclo ≈30-35%; yield 1,7%", "🔴 Bajo para el balance"],
        ["Recompras", "0 desde 2022", "🔴 Con P/B de 0,33x cada recompra acumula valor"],
        ["Acumular caja", "Caja neta de 5.028 M JPY → 5.777 M a jun-2026 💡", "🔴 Destruye ROE"],
    ], size=8.5)
    D.calc("Potencial: un programa de recompra del 10% del capital (1,8 M acciones a ≈380 JPY = 690 M JPY) consumiría solo el 14% de la caja neta y subiría el VC por acción de ≈1.066 a ≈1.140 JPY (+7%) y el BPA ≈+11%. Un dividendo extraordinario de 100 JPY (1.811 M JPY) dejaría la caja neta en ≈3.950 M JPY y supondría un 29% del precio actual.")

    D.h1("Conclusión de la Sección 8")
    D.box("🔴 **La retribución al accionista es la gran asignatura pendiente**: yield del 1,7%, dividendo congelado desde hace 10 años, sin recompras desde 2022 y caja creciendo. 🟢 La capacidad de pago es enorme: total shareholder yield potencial >15% sin comprometer la solvencia. **Cualquier cambio de política (aumento de payout, recompra, amortización de autocartera, plan de P/B) sería un catalizador directo del precio.**", fill="FFF4E5")
    return D.save(out, "Dividendos_y_Recompras")
