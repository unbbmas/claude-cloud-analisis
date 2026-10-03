from helpers import *
from data import *


def build(out):
    D = Doc(2, "Perspectiva del Cliente y Ventaja Competitiva (Pat Dorsey)")
    D.h1("2.1 Moat Económico (Pat Dorsey)")
    D.table(["Fuente de moat", "¿Presente?", "Evidencia", "Valoración"], [
        ["Intangibles (marcas, patentes, licencias)", "☐ No", "No hay marcas de consumo. I+D de 79 M JPY (0,17% de ventas) sin patentes relevantes. La fabricación de pienso exige registro sanitario, pero es una barrera común a todo el sector.", "🔴"],
        ["Costes de cambio", "☐ Débil", "Cambiar de proveedor de pienso exige ajustar dietas y tiene algo de riesgo productivo, pero es habitual. El crédito comercial y los préstamos que Nichiwa da a ganaderos crean una dependencia financiera (lock-in), aunque concentrada en los clientes más débiles.", "🟡"],
        ["Efecto red", "☐ No", "No aplica.", "🔴"],
        ["Ventajas de coste", "☐ Parcial/local", "Fábricas en puertos con silos propios (menor coste de descarga y transporte). Pero los competidores grandes tienen escala de compra superior (Feed One ≈6,7x y Chubu ≈4,9x las ventas de piensos de Nichiwa) y plantas más modernas. Margen operativo medio de 1,2% frente a 2,8% de Feed One y 3,1% de Chubu en FY3/2026.", "🟡/🔴"],
        ["Escala eficiente / mercado local", "☐ Parcial", "El pienso es voluminoso y de bajo valor por kg, así que el radio económico de una fábrica es regional. En zonas como el sur de Kyushu o Aomori el número de proveedores es limitado.", "🟡"],
    ], size=8)
    D.src(YUHO[2026] + ", p.11-12; datos de peers: resultados FY3/2026 de Feed One y Chubu Shiryo (TDnet, mayo-2026)")
    D.calc("Margen operativo FY3/2026: Nichiwa 1.456/45.579 = 3,2%; Feed One 8.091/290.675 = 2,8%; Chubu Shiryo 6.584/211.814 = 3,1%. En FY3/2026 el margen de Nichiwa está en línea con los grandes, pero su media de 6 años (1,2%) es claramente inferior.")
    D.box("**Conclusión moat: INEXISTENTE.** 🔴 Nichiwa no tiene ninguna de las cuatro fuentes de foso de Dorsey de forma sostenible. Su ROE medio de 1,5% (FY3/2021-26) está muy por debajo de su coste de capital (6,7-8,0% según sus propias pruebas de deterioro), que es la prueba empírica de la ausencia de ventaja competitiva.", fill="FDECEA")

    D.h1("2.2 Concentración de Clientes")
    D.table(["Indicador", "Dato", "Fuente"], [
        ["Clientes >10% de ventas", "Ninguno", YUHO[2026] + ", p.9 y p.59"],
        ["Tipología", "Ganaderos (avícola, porcino, vacuno), integradoras, distribuidores (特約店), acuicultura", YUHO[2026] + ", p.5"],
        ["Clientes con relación accionarial", "Jumonji Chicken Co. (8,70%, integradora avícola de Iwate); Tohoku Grain Terminal (6,37%, terminal de grano de Hachinohe)", YUHO[2026] + ", p.15"],
        ["Créditos dudosos y concursales (bruto)", "1.243 M JPY (2,7% de ventas); provisión de 1.364 M JPY (cubre el 100%)", YUHO[2026] + ", p.31 y KAM del auditor"],
        ["Préstamos a largo plazo a clientes", "756 M JPY (+442 M JPY en FY3/2026)", YUHO[2026] + ", p.31 y p.37"],
    ], size=8.5)
    D.p("🟡 No hay concentración comercial relevante, pero sí **riesgo de crédito**: la empresa actúa en parte como financiador de explotaciones ganaderas. El auditor (EY ShinNihon) señala como **asunto clave de auditoría (KAM)** la valoración de los créditos dudosos y concursales, cuya garantía son **animales vivos (vacas, cerdos, pollos) y terrenos**.")
    D.src(YUHO[2026] + ", p.79 «監査上の主要な検討事項»")

    D.h1("2.3 Posicionamiento Competitivo")
    D.table(["Aspecto", "Evaluación"], [
        ["Posición", "**Nicho regional / seguidor.** Independiente pequeño (≈2% del volumen nacional, ⚠️ estimación)."],
        ["Competidores principales", "JA Zen-Noh y filiales (referencia de precios); Feed One (2060); Chubu Shiryo (2053) / Itochu Feed; Marubeni-Nisshin Feed; Nosan (Mitsubishi); Showa Sangyo; fabricantes regionales y de acuicultura como Higashimaru (2058)."],
        ["Diferenciadores", "Atención técnica cercana; financiación al ganadero; logística portuaria; flexibilidad de un fabricante pequeño."],
        ["Barreras de entrada", "🟡 Moderadas: fábricas con silos portuarios, licencias sanitarias, capital circulante elevado y relación con importadores de grano (Toyota Tsusho, Cargill, Kanematsu son proveedores y accionistas). Pero el sector está en sobrecapacidad y no atrae nuevos entrantes."],
        ["Amenaza de sustitutos", "🟢 Baja: el pienso compuesto es imprescindible en la ganadería intensiva japonesa."],
        ["Poder de los clientes", "🔴 Alto y creciente: menos explotaciones y más grandes; integradoras con varios proveedores."],
        ["Poder de los proveedores", "🔴 Alto: el grano es una commodity global; el precio lo fija Chicago y el tipo de cambio."],
    ], size=8.5)
    D.src(YUHO[2026] + ", p.15 y p.27 (Toyota Tsusho y Kanematsu como «principales proveedores del negocio de piensos»)")

    D.h1("2.4 Análisis del Mercado")
    D.table(["Indicador", "FY3/2022", "FY3/2023", "FY3/2024", "FY3/2025", "FY3/2026", "Comentario"], [
        ["Producción nacional de pienso compuesto (Mt)", "≈23-24", "≈23", "≈23", "≈23", "≈23", "⚠️ Fuente secundaria; mercado estable/ligeramente decreciente"],
        ["Ventas de piensos Nichiwa (M JPY)", "43.211", "52.952", "51.157", "46.698", "43.669", "🔍 Yuho"],
        ["Feed One ventas (M JPY)", "n.d.", "n.d.", "n.d.", "≈285.500", "290.675", "Fuente secundaria (TDnet)"],
        ["Chubu Shiryo ventas (M JPY)", "n.d.", "n.d.", "n.d.", "≈209.900", "211.814", "Fuente secundaria (TDnet)"],
        ["Ratio Nichiwa / (Feed One + Chubu)", "—", "—", "—", "≈9,4%", "≈8,7%", "💡 La cuota relativa frente a los dos grandes cotizados cae ≈0,7 pp"],
    ], size=8)
    D.calc("Ventas de Feed One FY3/2025 = 290.675/1,018 ≈ 285.500; Chubu FY3/2025 = 211.814/1,009 ≈ 209.900 (a partir de las variaciones publicadas de +1,8% y +0,9%). Ratio FY3/2026 = 43.669/(290.675+211.814) = 8,7%. "
           "🔴 Nichiwa vendió −6,5% en piensos en FY3/2026 frente a +1,8% y +0,9% de los dos grandes, lo que apunta a **pérdida de volumen o de mix**, no solo a efecto precio.")
    D.src("Feed One: resultados FY3/2026 (+1,8% ventas, +27,6% BO); Chubu Shiryo: FY3/2026 (+0,9% ventas, +53,8% BO), vía TDnet/búsquedas web 3-oct-2026")

    D.h1("2.5 Necesidad del Cliente")
    D.p("🟢 **Crítica.** El pienso supone ≈50-70% del coste de producción de huevo, pollo y cerdo en Japón; sin suministro estable las explotaciones intensivas no pueden operar. Esto da **estabilidad de volumen**, pero no poder de precio, porque el producto es intercambiable entre fabricantes y su precio de referencia es público (Zen-Noh). ⚠️ El porcentaje de coste es una referencia sectorial general, no un dato de la empresa.")

    D.h1("2.6 Costes de Cambio")
    D.p("**Switching costs: BAJOS-MODERADOS.** 🟡 Cambiar de pienso implica un periodo de adaptación de dietas y cierto riesgo productivo, pero los grandes clientes licitan y comparan precios cada trimestre. El vínculo más fuerte es **financiero**: los ganaderos que deben dinero a Nichiwa (créditos comerciales largos, préstamos, compra de su producción) tienen difícil cambiar. Es un «moat» de mala calidad, porque **ata precisamente a los clientes de mayor riesgo**.")

    D.h1("2.7 Ventaja Competitiva Sostenible")
    D.p("No hay una ventaja competitiva sostenible identificable. Las ventajas relativas son: (1) **ubicación portuaria con silos** en cinco puntos del país; (2) **relaciones con proveedores de grano que además son accionistas** (Toyota Tsusho 7,52%, Cargill Japan 5,52%, Tohoku Grain Terminal 6,37%), que dan seguridad de suministro; y (3) **balance sin riesgo**, que permite financiar clientes y sobrevivir ciclos que podrían quebrar a competidores más pequeños. 🟡 Estas ventajas permiten **sobrevivir** (casi 102 años de historia), pero no **generar retornos superiores**.")
    D.src(YUHO[2026] + ", p.15 y p.27")

    D.h1("2.8 Poder de Pricing")
    D.table(["Episodio", "Coste del grano", "Acción de precio de Nichiwa", "Resultado en margen"], [
        ["FY3/2022", "↑ (China, etanol, Ucrania)", "Subidas en abr, jul y ene; bajada en oct", "BO 118 (−58,5%); margen 0,3%"],
        ["FY3/2023", "↑↑ (máximo histórico, yen débil)", "Tres subidas (abr, jul, oct)", "🔴 Pérdida operativa de −200"],
        ["FY3/2024", "↓ (buena cosecha EE. UU.)", "Bajadas en abr, jul y oct; subida en ene", "BO 905; margen 1,7%"],
        ["FY3/2025", "↓/volátil", "Bajadas en abr y oct; subidas en jul y ene", "BO 906; margen 1,9%"],
        ["FY3/2026", "↓ y luego ↑ (Oriente Medio)", "Bajadas en abr, jul y oct; subida en ene-2026", "🟢 BO 1.456; margen 3,2% (máximo)"],
        ["1T FY3/2027", "↑ por fletes, ↓ por cosecha", "Subida en abr-2026", "BO 382 (+39%)"],
    ], size=8.5)
    D.src("MD&A de cada Yuho FY3/2022-FY3/2026 (p.9) y " + Q1 + " p.4")
    D.p("**Conclusión:** 🔴 Nichiwa **no tiene poder de precio**: sigue al mercado. Traslada el coste con retraso, lo que produce un patrón «anticíclico» del margen respecto al grano: pierde cuando el grano sube y gana cuando baja. Con el grano y el yen otra vez al alza en 2026, el patrón apunta a **compresión de márgenes en FY3/2027**, que es lo que prevé la dirección (BO de 500 M JPY).")

    D.h1("2.9 Proveedores")
    D.table(["Proveedor / grupo", "Rol", "Relación accionarial", "Fuente"], [
        ["Toyota Tsusho", "Principal proveedor de materias primas de piensos", "Accionista (7,52%); Nichiwa tiene 172.779 acciones de Toyota Tsusho (1.028 M JPY): participación cruzada", YUHO[2026] + ", p.15 y p.27"],
        ["Cargill Japan", "Trading global de grano (proveedor probable ⚠️)", "Accionista (5,52%)", YUHO[2026] + ", p.15"],
        ["Tohoku Grain Terminal", "Terminal de grano de Hachinohe (descarga y silos)", "Accionista (6,37%)", YUHO[2026] + ", p.15"],
        ["Kanematsu", "Principal proveedor del negocio de piensos", "Participación cruzada (Nichiwa tiene 3.600 acciones)", YUHO[2026] + ", p.27"],
        ["Michinoku Shiryo (asociada)", "Fabrica por encargo pienso para vacuno", "Asociada (método de coste, no se aplica puesta en equivalencia)", YUHO[2026] + ", p.5 y p.38"],
    ], size=8)
    D.p("🟡 **Concentración moderada**: dependencia de pocas tradings para un insumo commodity, mitigada porque el grano es fungible y hay varios proveedores alternativos. Las participaciones cruzadas (政策保有株式) con proveedores son típicas en Japón y una **señal de gobierno corporativo a vigilar** (ver Sección 7).")

    D.h1("Conclusión de la Sección 2")
    D.box("🔴 **Sin moat. Precio aceptante. Clientes con poder creciente y proveedores con poder total sobre el coste.** La ventaja de Nichiwa es de supervivencia (balance y ubicación), no de rentabilidad. Para un horizonte de 6-18 meses la tesis **no puede apoyarse en la calidad del negocio**; tiene que apoyarse en la **valoración de activos** y en catalizadores de capital (Sección 10).", fill="FDECEA")
    return D.save(out, "Ventaja_Competitiva")
