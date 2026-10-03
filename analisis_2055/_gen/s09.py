from helpers import *
from data import *


def build(out):
    D = Doc(9, "Análisis de Riesgos (Top 5 priorizados)")
    D.p("Riesgos declarados por la empresa (事業等のリスク): (1) precio del grano; (2) tipo de cambio; (3) precios de productos ganaderos y cobro a clientes; (4) fondo de estabilización del precio del pienso; (5) enfermedades animales; (6) cambio climático y desastres naturales. Abajo se priorizan los que más afectan a la tesis a 6-18 meses, añadiendo riesgos propios del inversor (gobierno corporativo, liquidez).")
    D.src(YUHO[2026] + ", p.7 «事業等のリスク»")

    D.h1("9.1 Top 5 Riesgos Priorizados")
    D.h2("Riesgo 1 – Reversión del ciclo de márgenes (grano, yen, fletes)")
    D.bullets([
        "**Descripción:** FY3/2026 marcó un margen bruto récord de 9,1% gracias a la bajada del grano. En 2026 el maíz y la soja suben por fletes y tensiones en Oriente Medio y el yen sigue débil. Zen-Noh subió el pienso 3.700 JPY/t para jul-sep 2026. Si el coste sube más deprisa de lo que Nichiwa traslada, el margen se comprime como en FY3/2022-23 (BO de 118 y −200). La propia dirección prevé un BO de 500 (−66%) en FY3/2027.",
        "**Probabilidad:** 🔴 Alta (60%) de que el BO de FY3/2027 sea inferior al de FY3/2026.",
        "**Impacto:** 🟡 Medio sobre el valor (el balance amortigua); 🔴 alto sobre el sentimiento: un BPA por debajo de 17 JPY eleva el PER por encima de 20x.",
        "**Mitigantes:** revisiones trimestrales de precio; coberturas de divisa; fuerte 1T (BO de 382); caja que absorbe el circulante.",
        "**Señales de alerta:** margen bruto trimestral <7%; USD/JPY >160; maíz CBOT >5,5 USD/bu; existencias y proveedores al alza en el 2T.",
    ])
    D.src(YUHO[2026] + " p.6 y p.8; " + Q1 + " p.4; JA Zen-Noh (jul-2026)")

    D.h2("Riesgo 2 – Trampa de valor: el descuento no se corrige por el gobierno corporativo")
    D.bullets([
        "**Descripción:** la acción cotiza por debajo de 0,5x el valor contable desde hace años (P/B de 0,25-0,39 al cierre de cada ejercicio entre FY3/2021 y FY3/2026). Sin recompras, sin plan de P/B, con incentivos fijos y accionistas «estables» cercanos al 62%, el descuento puede no cerrarse en 6-18 meses.",
        "**Probabilidad:** 🔴 Alta (55-65%) de que no haya cambios de política de capital en el horizonte.",
        "**Impacto:** 🟡 Medio: no destruye valor, pero inmoviliza capital y reduce el rendimiento a ≈dividendo (1,7%) + crecimiento del VC (≈2-4%).",
        "**Mitigantes:** presión de la TSE sobre las empresas con P/B<1; posible entrada de activistas en microcaps japonesas; acumulación de Jumonji Chicken.",
        "**Señales de alerta:** junta de jun-2027 sin propuestas de capital; ausencia de un documento «資本コストや株価を意識した経営».",
    ])
    D.h2("Riesgo 3 – Crédito a clientes y enfermedades animales")
    D.bullets([
        "**Descripción:** Nichiwa financia a ganaderos (DSO de 91 días, préstamos de 756 M JPY, créditos concursales de 1.243 M JPY). La gripe aviar (casi anual), la peste porcina clásica (CSF, presente en Japón desde 2018) y una hipotética llegada de la peste porcina africana (ASF) pueden diezmar cabañas y quebrar clientes. En FY3/2021-23 se dotaron ≈1.240 M JPY por insolvencias. El auditor lo considera un asunto clave (las garantías son animales vivos).",
        "**Probabilidad:** 🟡 Media (30-40% de un episodio relevante en 18 meses).",
        "**Impacto:** 🟡 Medio: una dotación de 300-500 M JPY borraría el 30-60% del BO de un año normal.",
        "**Mitigantes:** provisiones que ya cubren el 100% de los créditos concursales; diversificación por especies y regiones; ningún cliente >10%.",
        "**Señales de alerta:** brotes de gripe aviar en Kyushu y Tohoku en invierno 2026-27; aumento de «破産更生債権等»; dotaciones en SG&A.",
    ])
    D.src(YUHO[2026] + ", p.7, p.39-40 y p.79 (KAM)")
    D.h2("Riesgo 4 – Pérdidas y deterioros en el segmento ganadero")
    D.bullets([
        "**Descripción:** Towa Chikusan ha perdido dinero en 4 de los últimos 6 años, ha registrado 1.445 M JPY de deterioros en tres ejercicios y debe 2.163 M JPY a la matriz (provisionados en 1.604). Los precios del cerdo y del pollo son volátiles y la filial compra el pienso a precio de mercado.",
        "**Probabilidad:** 🟡 Media (40%) de nuevos deterioros o pérdidas significativas.",
        "**Impacto:** 🟢/🟡 Bajo-medio: la PP&E restante del segmento es pequeña (≈300 M JPY contables), así que el daño contable futuro está acotado.",
        "**Mitigantes:** la base de activos ya está saneada; BO de 60 M JPY en el 1T FY3/2027.",
        "**Señales de alerta:** BO del segmento negativo en el 2T; nuevos préstamos de la matriz.",
    ])
    D.src(YUHO[2026] + ", p.12, p.44 y p.63-65; " + Q1 + " p.8")
    D.h2("Riesgo 5 – Iliquidez, tamaño y aumento de costes regulados (fondo de estabilización)")
    D.bullets([
        "**Descripción:** con una capitalización de ≈6.300 M JPY (≈42 M USD), un free float reducido y 1.596 accionistas, la liquidez es muy baja: entrar y salir mueve el precio. A esto se suma un coste regulado creciente: la aportación al fondo de estabilización ha pasado de 0 (FY3/2021) a 1.198 M JPY (82% del BO de FY3/2026) y puede seguir alta para recapitalizar el fondo tras años de compensaciones. Las plantas envejecidas pueden exigir inversiones extraordinarias.",
        "**Probabilidad:** 🔴 Alta (iliquidez: certeza); 🟡 media (fondo y CapEx).",
        "**Impacto:** 🟡 Medio.",
        "**Mitigantes:** horizonte paciente; órdenes limitadas; el balance cubre cualquier CapEx extraordinario.",
        "**Señales de alerta:** volumen diario <2.000 acciones; anuncios del MAFF sobre el fondo; un CapEx declarado >1.000 M JPY.",
    ])
    D.src(YUHO[2026] + ", p.15 y p.43")

    D.h1("9.2 Matriz de Riesgos")
    D.table(["#", "Riesgo", "Probabilidad", "Impacto", "Horizonte", "Prioridad"], [
        ["1", "Reversión de márgenes (grano/yen/fletes)", "🔴 Alta", "🟡 Medio", "6-12 meses", "**ALTA**"],
        ["2", "Trampa de valor por gobierno corporativo", "🔴 Alta", "🟡 Medio", "6-18 meses", "**ALTA**"],
        ["3", "Crédito a clientes y enfermedades animales", "🟡 Media", "🟡 Medio", "Invierno 2026-27", "MEDIA"],
        ["4", "Segmento ganadero", "🟡 Media", "🟢 Bajo-medio", "Continuo", "MEDIA-BAJA"],
        ["5", "Iliquidez, fondo de estabilización y CapEx", "🔴/🟡", "🟡 Medio", "Continuo", "MEDIA"],
        ["—", "Riesgos no prioritarios: desastre natural en una planta portuaria (terremoto o tsunami en Kobe/Kagoshima); cambios regulatorios; subida de tipos (🟢 neta positiva: caja > deuda)", "🟢 Baja", "🔴 Alto (desastre)", "—", "BAJA"],
    ], size=8)
    D.box("**Balance de riesgos:** 🟡 los riesgos de **beneficio** son elevados (ciclo), pero los de **pérdida permanente de capital** son bajos gracias al balance (precio < NNWC). El riesgo dominante para un horizonte de 6-18 meses es el **coste de oportunidad**: que nada cambie y la acción siga barata.", fill="FFF4E5")
    return D.save(out, "Analisis_de_Riesgos")
