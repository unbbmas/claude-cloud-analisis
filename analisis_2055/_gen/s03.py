from helpers import *
from data import *


def build(out):
    D = Doc(3, "Análisis del Balance")
    D.h1("Visión general del balance consolidado")
    rows = []
    items = [("Caja y depósitos", cash), ("Clientes (efectos + e-créditos + cuentas)", rec), ("Existencias", inv),
             ("Activo corriente", ca), ("Inmovilizado material neto", ppe), ("Inversiones financieras (valores)", invsec),
             ("Préstamos a largo plazo", ltloan), ("Créditos concursales (bruto)", bankr), ("Provisión insolvencias (no corriente)", allow_fix),
             ("ACTIVO TOTAL", ta), ("Proveedores", pay), ("Deuda financiera total", debt), ("Pasivo corriente", cl), ("PASIVO TOTAL", tl), ("PATRIMONIO NETO", equity)]
    for name, dct in items:
        rows.append([name] + [n(dct[y]) for y in Y])
    D.table(["M JPY (31-mar)"] + [f"FY3/{y}" for y in Y], rows, size=8)
    D.src("Balances consolidados: " + YUHO[2021] + " p.31-32; " + YUHO[2022] + " p.32-33; " + YUHO[2023] + " p.33-34; " + YUHO[2024] + " p.32-33; " + YUHO[2025] + " p.32-33; " + YUHO[2026] + " p.31-32")
    D.p("**Balance a 30-jun-2026 (1T FY3/2027):** activo total 32.010; caja 10.089 (+699); clientes 11.360; existencias 3.168; PP&E 3.931; deuda financiera ≈4.312 (CP 3.379 + LP 733 + ≈199 de vencimiento corriente ⚠️ incluido en «otros»); patrimonio neto 19.314; ratio de solvencia 60,3%.")
    D.src(Q1 + ", p.5")

    D.h1("3.1 Activos Fijos (PP&E)")
    D.table(["Partida (FY3/2026)", "Coste bruto", "Amort. acumulada", "Neto", "% amortizado"], [
        ["Edificios y construcciones", "5.846", "4.816", "1.030", "82%"],
        ["Maquinaria y vehículos", "15.097", "13.593", "1.503", "90%"],
        ["Herramientas y mobiliario", "1.103", "955", "148", "87%"],
        ["Terrenos", "1.330", "—", "1.330", "—"],
        ["Obra en curso", "4", "—", "4", "—"],
        ["Total inmovilizado material", "23.380", "19.364", "4.016", "≈86% (ex terrenos)"],
    ])
    D.src(YUHO[2026] + ", p.31 (連結貸借対照表)")
    D.p("🔴 **Red flag: activo muy envejecido.** La maquinaria está amortizada al 90%, señal de plantas antiguas (Kobe 1968, Mihara 1963/1987, Kagoshima 1974, Hachinohe 1983, Sakaide 1995). El CapEx de FY3/2026 (106 M JPY declarados) fue **0,2x la amortización**, algo que no puede mantenerse en el tiempo sin pérdida de eficiencia.")
    D.table(["Centro (31-mar-2026)", "Segmento", "Edificios", "Maquinaria", "Terreno (m²)", "Terreno (valor contable)", "Total contable", "Empleados"], [
        ["Fábrica de Kobe", "Piensos", "113", "213", "6.611", "80", "457", "22"],
        ["Fábrica de Mihara", "Piensos", "133", "91", "12.521", "169", "407", "26"],
        ["Fábrica de Kagoshima", "Piensos", "121", "590", "16.497", "82", "831", "44"],
        ["Fábrica de Hachinohe", "Piensos", "115", "379", "19.368", "295", "822", "42"],
        ["Fábrica de Sakaide", "Piensos", "78", "66", "9.140", "200", "351", "19"],
        ["Oficina de Nagasaki", "Piensos", "177", "0", "17.158", "64", "250", "9"],
        ["Sede central (Kobe)", "Corporativo", "4", "69", "—", "—", "77", "7"],
        ["Towa Chikusan (granjas)", "Ganadería", "137", "0", "411.277", "162", "300", "54"],
    ], size=8)
    D.src(YUHO[2026] + ", p.12 «主要な設備の状況»")
    D.p("⚠️ ESPECULACIÓN: los terrenos están al **coste histórico** (1.330 M JPY por ≈81.000 m² industriales portuarios más 411.000 m² de granjas). Japón no obliga a revalorizarlos. En FY3/2024 la venta de un terreno generó una plusvalía de 371 M JPY, lo que sugiere **plusvalías latentes** en el inmobiliario. No es cuantificable sin tasaciones.")
    D.src(YUHO[2024] + ", nota ※5 «固定資産売却益» (terreno 371 M JPY)")

    D.h1("3.2 Deuda a Largo Plazo")
    D.h2("Estructura de la deuda (31-mar-2026)")
    D.table(["Instrumento", "Saldo (M JPY)", "Tipo medio", "Vencimiento", "Tipo"], [
        ["Préstamos a corto plazo", "3.379", "1,83%", "<1 año (renovables)", "Variable"],
        ["Préstamo a largo plazo (parte corriente)", "199", "1,36%", "<1 año", "Variable"],
        ["Préstamo a largo plazo (no corriente)", "783", "1,36%", "abr-2027 a feb-2031", "Variable"],
        ["Total deuda financiera", "4.362", "≈1,74% (ponderado)", "", ""],
        ["Línea de crédito comprometida (8 bancos)", "5.230 total; 523 dispuestos; **4.707 disponibles**", "", "", ""],
    ], size=8.5)
    D.src(YUHO[2026] + ", p.42 (貸出コミットメント), p.50 y p.61 «借入金等明細表»")
    D.h2("Calendario de vencimientos")
    D.table(["Plazo", "<1 año", "1-2 años", "2-3 años", "3-4 años", "4-5 años", ">5 años"], [
        ["Préstamos CP", "3.379", "—", "—", "—", "—", "—"],
        ["Préstamos LP", "199", "199", "199", "199", "183", "—"],
        ["Total", "3.578", "199", "199", "199", "183", "—"],
    ])
    D.src(YUHO[2026] + ", p.50 nota 3")
    D.h2("Evolución histórica del apalancamiento")
    rows = []
    for y in Y:
        ebitda = op[y] + da[y]
        nd = debt[y] - cash[y]
        rows.append([f"FY3/{y}", n(debt[y]), n(cash[y]), n(nd), n(debt[y] / equity[y], 2), n(nd / ebitda, 1) + "x", n(ebitda / interest[y], 1) + "x", pct(equity[y] / ta[y] * 100)])
    D.table(["Ejercicio", "Deuda", "Caja", "Deuda neta", "Deuda/FP", "DN/EBITDA", "EBITDA/Intereses", "Solvencia (FP/AT)"], rows, size=8)
    D.calc("EBITDA = BO + amortización. Deuda neta negativa = caja neta. Intereses = gasto financiero de la cuenta de resultados.")
    D.p("🟢 **Caja neta durante todo el periodo**, incluido el peor año del ciclo (FY3/2023, caja neta de 913 M JPY). El préstamo a largo de 1.000 M JPY tomado en FY3/2026 sustituyó parcialmente deuda a corto (−590). ⚠️ Probablemente busca alargar vencimientos ante la subida de tipos en Japón; no hay inversión que lo justifique.")
    D.h2("Covenants")
    D.p("🔍 Los informes no revelan covenants financieros en los préstamos ni en la línea comprometida. Dado el apalancamiento negativo, el riesgo de incumplimiento es despreciable. 🟢")

    D.h1("3.3 NCAV (Net Current Asset Value) – Método Benjamin Graham")
    D.table(["Concepto (M JPY)", "31-mar-2026", "30-jun-2026"], [
        ["Activo corriente", "24.050", "25.147"],
        ["(−) Pasivo total", "11.777", "12.696"],
        ["**NCAV**", "**12.273**", "**12.451**"],
        ["Acciones en circulación (ex autocartera)", "18.111.793", "18.111.793"],
        ["**NCAV por acción (JPY)**", "**677,6**", "**687,5**"],
        ["Precio / NCAV", "**0,51x**", "**0,50x**"],
    ])
    D.calc("NCAV = AC − Pasivo total. Por acción: 12.451 M / 18.111.793 = 687,5 JPY. Precio 346 / 687,5 = 0,50x.")
    D.h2("Net-Net Working Capital (versión conservadora de Graham)")
    D.table(["Partida", "Saldo", "Factor", "Valor ajustado"], [
        ["Caja", "9.390", "100%", "9.390"],
        ["Clientes", "11.363", "75%", "8.522"],
        ["Existencias", "2.782", "50%", "1.391"],
        ["(−) Pasivo total", "11.777", "100%", "−11.777"],
        ["**NNWC**", "", "", "**7.526 → 415,5 JPY/acción**"],
    ])
    D.box("🟢 **La acción cotiza a 346 JPY, por debajo de su NCAV (≈688 JPY) e incluso de su NNWC (≈416 JPY).** Es una «net-net» clásica de Graham: el mercado valora a cero las cinco fábricas, los terrenos (al coste), las inversiones financieras (1.908 M JPY) y el negocio en marcha.\n"
          "🔴 Matices: (i) parte de la caja está atada al ciclo de circulante del grano; (ii) la calidad de los clientes es dudosa (KAM del auditor), aunque las provisiones ya cubren el 100% de los créditos concursales; (iii) sin un catalizador (recompras, OPA o reparto de caja) el descuento puede durar años: el precio/NCAV ya estaba en ≈0,4-0,5x en 2021-2025.", fill="E8F5E9")

    D.h1("3.4 Ratios de Liquidez")
    rows = []
    for y in Y:
        rows.append([f"FY3/{y}", n(ca[y] / cl[y], 2), n((ca[y] - inv[y]) / cl[y], 2), n(cash[y] / cl[y], 2), n(ca[y] - cl[y])])
    rows.append(["30-jun-2026", n(25147 / 11271, 2), n((25147 - 3168) / 11271, 2), n(10089 / 11271, 2), n(25147 - 11271)])
    D.table(["Fecha", "Current Ratio", "Quick Ratio", "Cash Ratio", "Fondo de maniobra (M JPY)"], rows)
    D.calc("Quick ratio = (AC − existencias)/PC; cash ratio = caja/PC. Existencias a 30-jun-2026 = 127 + 437 + 2.604 = 3.168.")
    D.p("🟢 Liquidez holgada. El current ratio (1,8-2,3x) supera el benchmark de Dorsey para sectores cíclicos (>1,5x). El mínimo del cash ratio (0,43x en FY3/2023) muestra cuánto consume el circulante en un ciclo de grano caro.")

    D.h1("3.5 Working Capital Trends")
    rows = []
    for y in Y:
        wc_op = rec[y] + inv[y] - pay[y]
        dso = rec[y] / sales[y] * 365; dio = inv[y] / cogs[y] * 365; dpo = pay[y] / cogs[y] * 365
        rows.append([f"FY3/{y}", n(rec[y]), n(inv[y]), n(pay[y]), n(wc_op), pct(wc_op / sales[y] * 100), n(dso + dio - dpo)])
    D.table(["Ejercicio", "Clientes", "Existencias", "Proveedores", "Circulante operativo", "% Ventas", "CCC (días)"], rows, size=8.5)
    D.calc("Circulante operativo = clientes + existencias − proveedores.")
    D.p("**Lectura:** el circulante operativo pasó de 6.433 M JPY (FY3/2021) a 9.172 (FY3/2024) en plena inflación del grano: **absorbió ≈2.700 M JPY de caja**. Se liberó parcialmente en FY3/2025 (−1.263) y se mantiene en ≈8.300 M JPY (18% de ventas). 🟡 El repunte del grano y del yen en 2026 podría volver a absorber caja en FY3/2027: en el 1T las existencias de materias primas subieron +345 M JPY y los proveedores +836.")
    D.src(Q1 + ", p.4")

    D.h1("3.6 CapEx Histórico")
    rows = []
    for y in Y:
        rows.append([f"FY3/{y}", n(capex_rep[y]), n(capex_cash[y]), n(da[y]), n(capex_cash[y] / da[y], 2), n(min(capex_cash[y], da[y])), n(max(capex_cash[y] - da[y], 0)), pct(capex_cash[y] / sales[y] * 100, 2)])
    D.table(["Ejercicio", "CapEx declarado (devengo)", "CapEx caja", "Amortización", "CapEx/D&A", "💡 Mantenimiento", "💡 Crecimiento", "CapEx/Ventas"], rows, size=8)
    D.calc("Sin desglose oficial entre mantenimiento y crecimiento, se aproxima el CapEx de mantenimiento por el menor entre CapEx y amortización, y el resto se trata como crecimiento/modernización. CapEx caja = adquisición de inmovilizado material + inmaterial (estado de flujos).")
    D.src("Estados de flujos de efectivo y «設備投資等の概要» de cada Yuho")
    D.p("🟡 Entre FY3/2021 y FY3/2024 la empresa invirtió por encima de la amortización (renovación de líneas y obra de reubicación por un proyecto público que generó una compensación de 331 M JPY en FY3/2023). Desde FY3/2025 **ha recortado el CapEx a 0,75x la amortización**. Esto mejora el FCF a corto plazo pero es **insostenible**.")

    D.h1("3.7 CapEx Futuro Estimado")
    D.table(["Ejercicio", "💡 CapEx estimado", "Base", "Fuente/justificación"], [
        ["FY3/2027", "400-550", "Amortización ≈480 (1T: 119 × 4)", "Yuho FY3/2026 p.13: «no hay planes significativos de nuevas instalaciones ni bajas». Q1: amortización de 119 M JPY"],
        ["FY3/2028", "500-700", "Reposición de maquinaria (90% amortizada)", "💡 Estimación propia: vuelta a CapEx/D&A ≈1,0-1,3x como en FY3/2021-24"],
        ["FY3/2029", "500-800", "Posible renovación de una línea", "⚠️ Especulación: plantas de 1963-1983 requerirán inversiones; la NIIF16-J (nueva norma de arrendamientos desde FY3/2028) no cambia el CapEx"],
    ], size=8.5)
    D.src(YUHO[2026] + ", p.13 «設備の新設、除却等の計画» y p.41 (nueva norma de arrendamientos desde FY3/2028); " + Q1 + ", p.9")

    D.h1("Otros elementos del balance relevantes")
    D.bullets([
        "**Cartera de valores:** 1.908 M JPY, de los que 1.665 M JPY son cotizados con un coste de solo 198 M JPY (plusvalía latente antes de impuestos de 1.466 M JPY). Principales posiciones: Toyota Tsusho 1.028, Resona HD 478, Mizuho 52, S Foods 51; además, un fondo monetario de 200 M JPY. 🟢 Activo líquido no operativo.",
        "**Pensiones:** sobrefinanciadas (activo neto de 117 M JPY). 🟢",
        "**Impuestos diferidos:** provisión de valoración de 1.283 M JPY sobre activos fiscales (créditos dudosos, deterioros, bases imponibles negativas de 237 M JPY), es decir, activos fiscales no reconocidos que podrían aflorar. 🟡",
        "**Préstamos de la matriz a Towa Chikusan:** 2.163 M JPY con una provisión de 1.604 M JPY (en las cuentas individuales). Confirma que la filial ganadera es **técnicamente insolvente** y depende de la matriz. 🔴",
        "**Autocartera:** 2.719.032 acciones (13,05% del capital) a un coste de 722 M JPY (≈265 JPY/acción); no se han amortizado. 🟡",
    ])
    D.src(YUHO[2026] + ", p.27-28, p.52 (valores), p.54 (pensiones), p.55 (impuestos), p.63-65 (cuentas individuales), p.16 (autocartera)")

    D.h1("Conclusión de la Sección 3")
    D.box("🟢 **Balance de fortaleza excepcional**: caja neta de 5.028 M JPY (80% de la capitalización), solvencia del 62%, cobertura de intereses de 28x, NCAV del doble del precio y valores cotizados con plusvalías.\n"
          "🔴 Puntos débiles: activos fijos muy envejecidos con infrainversión reciente; riesgo de crédito a ganaderos; filial ganadera insolvente; caja sensible al ciclo del grano.\n"
          "**Veredicto:** el balance **limita mucho el riesgo de pérdida permanente** y es el principal argumento de la tesis.", fill="E8F5E9")
    return D.save(out, "Analisis_del_Balance")
