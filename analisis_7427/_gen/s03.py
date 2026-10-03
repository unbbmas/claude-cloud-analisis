from helpers import *
from data import *


def build(out):
    D = Doc(3, "Análisis del Balance")
    D.h1("Visión general del balance consolidado")
    items = [("Caja y depósitos", cash), ("Clientes (efectos y cuentas)", rec), ("Otras cuentas a cobrar (rappels)", orec), ("Existencias", inv),
             ("Activo corriente", ca), ("Inmovilizado material neto", ppe), ("ACTIVO TOTAL", ta), ("Proveedores", pay), ("Acreedores varios (未払金)", accr),
             ("Deuda financiera (préstamos a corto)", debt), ("Pasivo corriente", cl), ("PASIVO TOTAL", tl), ("PATRIMONIO NETO", equity)]
    rows = [[nm] + [n(d[y]) for y in Y] + [n({'Caja y depósitos': Q1d['cash'], 'Clientes (efectos y cuentas)': Q1d['rec'], 'Otras cuentas a cobrar (rappels)': Q1d['orec'], 'Existencias': Q1d['inv'], 'Activo corriente': Q1d['ca'], 'Inmovilizado material neto': 965, 'ACTIVO TOTAL': Q1d['ta'], 'Proveedores': Q1d['pay'], 'Acreedores varios (未払金)': Q1d['accr'], 'Deuda financiera (préstamos a corto)': Q1d['debt'], 'Pasivo corriente': Q1d['cl'], 'PASIVO TOTAL': Q1d['tl'], 'PATRIMONIO NETO': Q1d['eq']}[nm])] for nm, d in items]
    D.table(["M JPY"] + [f"feb-{y}" for y in Y] + ["may-2026"], rows, size=7.5)
    D.src("Balances consolidados: " + TIKR + "; " + YUHO[2026] + " p.52-53; " + Q1 + " p.4")
    D.p("🔴 **Advertencia clave:** los cierres de feb-2026 (sábado) y de may-2026 (domingo) fueron días festivos bancarios. Según la propia empresa, cobros y pagos previstos para ese día se desplazaron al mes siguiente, lo que **infla clientes (+2.234), proveedores (+5.204) y caja** en feb-2026. Lo mismo ocurrió en feb-2021 (domingo), revertido en feb-2022. **La caja neta de 4.581 M JPY de feb-2026 no es representativa.**")
    D.src(YUHO[2026] + ", p.19 (explicación del efecto festivo) y p.86 (efectos y créditos electrónicos con vencimiento en día festivo: 737 M JPY)")

    D.h1("3.1 Activos Fijos (PP&E)")
    D.table(["Partida (feb-2026)", "Coste bruto", "Amort. acumulada", "Deterioro acumulado", "Neto"], [
        ["Edificios y construcciones", "1.206", "905", "64", "238"],
        ["Terrenos", "650", "—", "—", "650"],
        ["Otros (maquinaria, mobiliario, leasing)", "202", "128", "5", "69"],
        ["**Inmovilizado material**", "2.058", "1.033", "69", "**957**"],
        ["Inmovilizado inmaterial (software)", "", "", "", "252"],
    ])
    D.src(YUHO[2026] + ", p.52")
    D.p("🟢 **Modelo asset-light**: el inmovilizado material es solo el **2,5% del activo total**. Casi todos los centros logísticos son **alquilados** (88.734 m² de suelo y 77.955 m² de naves; alquiler anual de 1.023 M JPY) y los vehículos y equipos informáticos van en leasing (514 ordenadores, 146 vehículos). Terrenos propios: Sapporo (6.700 m²), Yokohama (726), Hiroshima (5.533) y Yao, Osaka (2.502).")
    D.src(YUHO[2026] + ", p.23-24 «主要な設備の状況»")
    D.p("🟡 **Cambio contable relevante:** la nueva norma japonesa de arrendamientos (equivalente a NIIF 16) se aplicará desde FY2/2028. Llevará al balance los contratos de alquiler de los centros logísticos, con **aumento de activos y pasivos y menor ratio de solvencia**, aunque sin efecto en la caja.")
    D.src(YUHO[2026] + ", p.60 «未適用の会計基準等»")

    D.h1("3.2 Deuda a Largo Plazo")
    D.table(["Instrumento", "feb-2025", "feb-2026", "may-2026", "Comentario"], [
        ["Préstamos bancarios a corto plazo", "3.250", "1.650", "3.625", "Financian el circulante; suben y bajan con el ciclo de cobros y pagos"],
        ["Deuda a largo plazo", "0", "0", "0", "🟢 Sin deuda a largo"],
        ["Arrendamientos financieros (aprox.)", "≈80", "≈78", "n.d.", "Deuda con coste total de 1.728 M JPY con leasings (feb-2026)"],
        ["Arrendamientos operativos no cancelables", "788", "742", "n.d.", "Fuera de balance hasta FY2/2028"],
    ], size=8.5)
    D.src(YUHO[2026] + ", p.22 (有利子負債 1.728) y p.70 (リース); " + Q1 + ", p.4")
    D.h2("Evolución del apalancamiento")
    rows = []
    for y in YA[1:]:
        e = op[y] + da[y]
        nd = debt[y] - cash[y]
        rows.append([f"FY2/{y}", n(debt[y]), n(cash[y]), n(nd), n(debt[y] / equity[y], 2), (n(nd / e, 1) + "x") if e > 0 else "n.s.", pct(equity[y] / ta[y] * 100)])
    D.table(["Ejercicio", "Deuda", "Caja", "Deuda neta (− = caja neta)", "Deuda/FP", "DN/EBITDA", "Solvencia"], rows, size=8)
    D.p("🟢 **Apalancamiento financiero bajo**: deuda/FP de 0,14-0,46x, sin deuda a largo y caja neta en 5 de 7 cierres. 🟡 La solvencia (31%) parece baja, pero es normal en distribución: el pasivo es sobre todo **deuda comercial sin coste** con proveedores (20.306 M JPY). Coste de intereses: 47 M JPY (cobertura EBIT/intereses de 24x).")
    D.p("💡 **Caja neta normalizada (sin efecto festivo): ≈1.000-1.600 M JPY.** Cierres «normales»: 860 (feb-2024) y 971 (feb-2025). En feb-2026, restando el exceso de proveedores sobre clientes por el festivo (5.204 − 2.234 ≈ 2.970): 4.581 − 2.970 ≈ 1.610. **Usamos ≈1.500 M JPY (≈247 JPY/acción) en la valoración.**")
    D.h2("Covenants")
    D.p("🔍 No se divulgan covenants. Con deuda solo a corto, renovable y sin garantías relevantes, el riesgo es bajo. 🟢 La empresa contrata **seguros de crédito comercial** para sus clientes.")
    D.src(YUHO[2026] + ", p.17 (riesgo (4))")

    D.h1("3.3 NCAV (Net Current Asset Value) – Método Benjamin Graham")
    nc26 = ca[2026] - tl[2026]
    ncq = Q1d['ca'] - Q1d['tl']
    D.table(["Concepto (M JPY)", "feb-2025", "feb-2026", "may-2026"], [
        ["Activo corriente", n(ca[2025]), n(ca[2026]), n(Q1d['ca'])],
        ["(−) Pasivo total", n(tl[2025]), n(tl[2026]), n(Q1d['tl'])],
        ["**NCAV**", n(ca[2025] - tl[2025]), n(nc26), n(ncq)],
        ["Acciones en circulación", "6.036.061", "6.073.021", "6.072.421"],
        ["**NCAV por acción (JPY)**", n((ca[2025] - tl[2025]) / 6.036061, 0), n(nc26 / 6.073021, 0), n(ncq / SH * 1e6, 0)],
        ["**Precio / NCAV (a 835 JPY)**", n(PRICE / ((ca[2025] - tl[2025]) / 6.036061), 2) + "x", n(PRICE / (nc26 / 6.073021), 2) + "x", n(PRICE / (ncq / SH * 1e6), 2) + "x"],
    ])
    D.calc(f"NCAV may-2026 = 41.572 − 31.761 = {n(ncq)} M JPY → {n(ncq / SH * 1e6)} JPY/acción. NCAV es menos sensible al efecto festivo porque clientes y proveedores se inflan a la vez.")
    q = Q1d
    nnwc = q['cash'] + 0.75 * (q['rec'] + q['orec']) + 0.5 * q['inv'] - q['tl']
    D.table(["Net-Net Working Capital (may-2026)", "Saldo", "Factor", "Ajustado"], [
        ["Caja", n(q['cash']), "100%", n(q['cash'])],
        ["Clientes + otras cuentas a cobrar", n(q['rec'] + q['orec']), "75%", n(0.75 * (q['rec'] + q['orec']))],
        ["Existencias", n(q['inv']), "50%", n(0.5 * q['inv'])],
        ["(−) Pasivo total", n(q['tl']), "100%", "−" + n(q['tl'])],
        ["**NNWC**", "", "", f"**{n(nnwc)} → ≈{n(nnwc / SH * 1e6)} JPY/acción**"],
    ])
    D.box("🟢 **La acción cotiza a ≈0,52x su NCAV (≈1.616 JPY/acción)**: el mercado valora el negocio en marcha por debajo de su capital circulante neto.\n"
          "🟡 Con los recortes conservadores de Graham (NNWC), el valor de liquidación es **≈0**: en un mayorista el activo corriente es casi todo deuda de clientes que solo vale si el negocio sigue pagando a sus proveedores. Echo **no es una net-net en sentido estricto**, pero sí un caso de **P/B y P/NCAV muy bajos con clientes de buena calidad** (grandes cadenas cotizadas, con seguro de crédito; provisión de insolvencias de solo 9 M JPY).", fill="E8F5E9")

    D.h1("3.4 Ratios de Liquidez")
    rows = []
    for y in Y:
        rows.append([f"feb-{y}", n(ca[y] / cl[y], 2), n((ca[y] - inv[y]) / cl[y], 2), n(cash[y] / cl[y], 2), n(ca[y] - cl[y])])
    rows.append(["may-2026", n(Q1d['ca'] / Q1d['cl'], 2), n((Q1d['ca'] - Q1d['inv']) / Q1d['cl'], 2), n(Q1d['cash'] / Q1d['cl'], 2), n(Q1d['ca'] - Q1d['cl'])])
    D.table(["Fecha", "Current Ratio", "Quick Ratio", "Cash Ratio", "Fondo de maniobra"], rows)
    D.p("🟡 Current ratio de 1,3-1,4x (por debajo del benchmark de 1,5x, aunque normal en distribución, donde los proveedores financian el circulante). 🟢 El quick ratio de ≈1,2-1,3x muestra que el activo corriente es **líquido**: clientes a ≈75-80 días e inventario de solo 14 días.")

    D.h1("3.5 Working Capital Trends")
    rows = []
    for y in YA:
        wc = rec[y] + orec[y] + inv[y] - pay[y] - accr[y]
        rows.append([f"FY2/{y}", n(rec[y] + orec[y]), n(inv[y]), n(pay[y] + accr[y]), n(wc), pct(wc / sales[y] * 100)])
    wcq = Q1d['rec'] + Q1d['orec'] + Q1d['inv'] - Q1d['pay'] - Q1d['accr']
    rows.append(["may-2026", n(Q1d['rec'] + Q1d['orec']), n(Q1d['inv']), n(Q1d['pay'] + Q1d['accr']), n(wcq), "—"])
    D.table(["Cierre", "Clientes + otros", "Existencias", "Proveedores + acreedores", "Circulante operativo", "% Ventas"], rows, size=8)
    D.calc("Circulante operativo = clientes + otras cuentas a cobrar + existencias − proveedores − acreedores varios.")
    D.p("**Lectura:** en años «normales» el circulante operativo ronda el **7-9% de las ventas** (≈8.000-9.000 M JPY). FY2/2021 y FY2/2026, con cierre en festivo, muestran un circulante artificialmente bajo. 🟡 Un crecimiento de ventas del 4% exigiría ≈300-350 M JPY de circulante adicional al año.")

    D.h1("3.6 CapEx Histórico")
    rows = []
    for y in YA:
        rows.append([f"FY2/{y}", n(capex[y]), n(da[y]), n(capex[y] / da[y], 2), pct(capex[y] / sales[y] * 100, 2)])
    D.table(["Ejercicio", "CapEx (material + inmaterial)", "Amortización", "CapEx/D&A", "CapEx/Ventas"], rows)
    D.src(TIKR + " (FCF: gastos de capital + activos intangibles); " + YUHO[2026] + " p.58")
    D.p("🟢 CapEx mínimo (0,02-0,2% de las ventas): los almacenes son alquilados. En FY2/2026 subió a 227 M JPY por **inversión en sistemas** (209 M JPY de software). En FY2/2025 vendió la antigua sede de Nishinomiya (454 M JPY de cobro, plusvalía de 205). 💡 Mantenimiento ≈ amortización (≈80-95 M JPY/año). El resto es inversión en sistemas y equipamiento de centros nuevos.")

    D.h1("3.7 CapEx Futuro Estimado")
    D.table(["Ejercicio", "💡 CapEx estimado", "Fundamento"], [
        ["FY2/2027", "150-300", "Nuevo plan: datos e IA generativa, unificación de I&I y Pets Value, centro de Hayashima (2026). «No hay planes de nuevas instalaciones relevantes» (Yuho)"],
        ["FY2/2028", "100-250", "Continuidad de sistemas; a partir de aquí la norma de arrendamientos lleva el derecho de uso al balance (no cambia el CapEx en caja)"],
        ["FY2/2029", "100-250", "Mantenimiento ≈ amortización + digitalización"],
    ], size=8.5)
    D.src(YUHO[2026] + ", p.24 «設備の新設、除却等の計画» y p.10-11")

    D.h1("Otros elementos relevantes del balance")
    D.bullets([
        "**Participaciones en clientes (政策保有株式)**: 14 valores cotizados por 785 M JPY (Kohnan 350, Genky 116, AEON 67, Okuwa 53, DCM 38, Life 33, PetGo 32, H2O 29, Arenza 23…) y 7 no cotizados (66). Aumentan cada año por compras en las asociaciones de proveedores de esos clientes. 🔴 Práctica que la TSE pide reducir.",
        "**Rappels pendientes de cobro**: 2.199 M JPY (KAM del auditor). Activo esencial para el beneficio y de valoración compleja. 🟡",
        "**Pensiones**: plan de aportación definida, **sin pasivo actuarial**. 🟢",
        "**Autocartera**: 42.125 acciones (0,7%), sobre todo procedentes de acciones restringidas recuperadas. 🟡",
    ])
    D.src(YUHO[2026] + ", p.47-48, p.70, p.94; " + Q1 + ", p.2")

    D.h1("Conclusión de la Sección 3")
    D.box("🟢 **Balance sano y asset-light**: sin deuda a largo, caja neta normalizada de ≈1.500 M JPY, cobertura de intereses de 24x, pensiones sin pasivo, clientes de calidad e inventario de 14 días. Patrimonio neto de 12.008 M JPY (≈1.977 JPY/acción) y NCAV de ≈1.616 JPY/acción, frente a un precio de 835 JPY.\n"
          "🔴 Puntos a vigilar: caja muy volátil por el calendario de cobros y pagos; dependencia de los rappels; participaciones en clientes; la nueva norma de arrendamientos (2028) inflará el pasivo.", fill="E8F5E9")
    return D.save(out, "Analisis_del_Balance")
