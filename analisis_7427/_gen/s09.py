from helpers import *
from data import *


def build(out):
    D = Doc(9, "Análisis de Riesgos (Top 5 priorizados)")
    D.p("Riesgos declarados por la empresa (事業等のリスク): (1) desastres naturales y sistemas; (2) seguridad alimentaria de la comida para mascotas; (3) **cambios importantes de condiciones comerciales** (bajada de precios de venta, subida de los de compra, cambio de mayorista); (4) impago de clientes; (5) evolución del número de mascotas. Abajo se priorizan los que más pesan en la tesis a 6-18 meses.")
    D.src(YUHO[2026] + ", p.17")

    D.h1("9.1 Top 5 Riesgos Priorizados")
    D.h2("Riesgo 1 – Hundimiento del margen y nuevo incumplimiento de la previsión (FY2/2027)")
    D.bullets([
        "**Descripción:** el 1T FY2/2027 cerró con un BO de 8 M JPY (−96%) por «cambios de condiciones con algunos clientes» y fletes al alza. La previsión del 1S (BO de 555) y la anual (1.150) parecen inalcanzables. Sería el **tercer incumplimiento seguido**, con riesgo de una revisión fuerte en los resultados del 1S (≈9-10 oct-2026).",
        "**Probabilidad:** 🔴 Alta (70-80%) de revisión a la baja de la previsión.",
        "**Impacto:** 🔴 Alto a corto plazo: con un BPA de ≈40-70 JPY el PER pasaría a 12-20x; caída potencial del precio del 10-20%.",
        "**Mitigantes:** el precio ya cotiza cerca del mínimo de 52 semanas (811 JPY); el 1T es estacionalmente débil (feria de mayo); posible recuperación de condiciones comerciales en el 2S.",
        "**Señales de alerta:** margen bruto <10,5% en el 1S; SG&A/ventas >10,2%; revisión de la previsión por debajo de 700 M JPY de BO.",
    ])
    D.src(Q1 + ", p.1-3")
    D.h2("Riesgo 2 – Pérdida de clientes o cambio de mayorista (帳合変更) y dependencia de Rakuten")
    D.bullets([
        "**Descripción:** el sector reasigna cuentas con frecuencia. Echo pierde terreno frente a Japell (57% de su tamaño frente a 61% un año antes) y depende cada vez más de Rakuten (10,5%), un cliente de gran poder negociador.",
        "**Probabilidad:** 🟡 Media (40%).",
        "**Impacto:** 🔴 Alto: perder una cuenta del 5% de las ventas con margen bruto del 11% = ≈580 M JPY de margen bruto (≈50% del BO).",
        "**Mitigantes:** amplitud de surtido, servicios de gestión de categoría, relación con Kokubu.",
        "**Señales de alerta:** caída de ventas >3%; nuevos «cambios de condiciones» citados en el MD&A; Rakuten fuera del desglose o por encima del 15%.",
    ])
    D.h2("Riesgo 3 – Inflación de costes logísticos y laborales")
    D.bullets([
        "**Descripción:** fletes y embalaje (5,0% de las ventas), alquileres (1,0%) y personal (2,3%) suben con la escasez de conductores (crisis logística de 2024) y los salarios. Con un margen operativo del 1%, un +5% en fletes (≈265 M JPY) se come ≈25% del BO.",
        "**Probabilidad:** 🔴 Alta (70%).",
        "**Impacto:** 🟡 Medio-alto.",
        "**Mitigantes:** entregas conjuntas, digitalización (AI-OCR, tabletas), centros nuevos y repercusión parcial a clientes.",
        "**Señales de alerta:** fletes/ventas >5,2%.",
    ])
    D.h2("Riesgo 4 – Trampa de valor: el descuento no se corrige")
    D.bullets([
        "**Descripción:** P/B de 0,42x con un ROE en caída (6,6% → ≈3%), sin recompras, sin plan sobre el P/B y con accionariado minorista. El descuento puede persistir mientras el beneficio no se recupere.",
        "**Probabilidad:** 🟡 Media-alta (50-60%).",
        "**Impacto:** 🟡 Medio (rentabilidad ≈ dividendo del 3,6%).",
        "**Mitigantes:** presión de la TSE (petición de 2023 sobre el coste de capital); ola de exclusiones de bolsa promovidas por accionistas en distribución (Mitsubishi Shokuhin, Itochu Shokuhin, PALTAC).",
        "**Señales de alerta:** junta de 2027 sin medidas; P/B <0,40x sostenido.",
    ])
    D.h2("Riesgo 5 – Riesgo de crédito, rappels y efecto calendario (calidad contable)")
    D.bullets([
        "**Descripción:** (i) clientes minoristas en consolidación (posibles quiebras); (ii) **rappels pendientes de 2.199 M JPY**, un asunto clave de auditoría y una partida grande frente al BO; (iii) balance y OCF distorsionados por los cierres en festivo, que dificultan el análisis.",
        "**Probabilidad:** 🟢 Baja-media (20%).",
        "**Impacto:** 🟡 Medio.",
        "**Mitigantes:** seguro de crédito comercial; provisión de insolvencias de solo 9 M JPY (cartera de calidad); auditoría limpia.",
        "**Señales de alerta:** dotaciones >50 M JPY; rappels/BO >2,5x; salvedad del auditor.",
    ])
    D.src(YUHO[2026] + ", p.17, p.19, p.94")

    D.h1("9.2 Matriz de Riesgos")
    D.table(["#", "Riesgo", "Probabilidad", "Impacto", "Horizonte", "Prioridad"], [
        ["1", "Margen y previsión FY2/2027", "🔴 Alta", "🔴 Alto", "0-6 meses", "**MUY ALTA**"],
        ["2", "Pérdida de clientes / Rakuten", "🟡 Media", "🔴 Alto", "6-18 meses", "**ALTA**"],
        ["3", "Costes logísticos y laborales", "🔴 Alta", "🟡 Medio", "Continuo", "**ALTA**"],
        ["4", "Trampa de valor", "🟡 Media-alta", "🟡 Medio", "6-18 meses", "MEDIA"],
        ["5", "Crédito, rappels, calidad contable", "🟢 Baja-media", "🟡 Medio", "Continuo", "MEDIA-BAJA"],
        ["—", "Otros: desastre natural en centros clave, retirada de producto, iliquidez", "🟢 Baja", "🟡", "—", "BAJA"],
    ], size=8)
    D.box("**Balance de riesgos:** 🔴 a **corto plazo (0-6 meses) los riesgos son claramente negativos**: un 1T casi en pérdidas y una revisión de la previsión probable. 🟢 A **12-18 meses** el riesgo de pérdida permanente es limitado: no hay deuda a largo, el P/B es de 0,42x y el NCAV de ≈1.616 JPY/acción, y existe la opción de una operación corporativa.", fill="FFF4E5")
    return D.save(out, "Analisis_de_Riesgos")
