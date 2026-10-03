from helpers import *
from data import *


def build(out):
    D = Doc(2, "Perspectiva del Cliente y Ventaja Competitiva (Pat Dorsey)")
    D.h1("2.1 Moat Económico (Pat Dorsey)")
    D.table(["Fuente de moat", "¿Presente?", "Evidencia", "Valoración"], [
        ["Intangibles (marcas, patentes, licencias)", "☐ Débil", "Echo distribuye marcas ajenas. Sus marcas propias (ShareZ, GOODISH, productos de Pets Value) son incipientes. No hay patentes ni licencias exclusivas.", "🔴"],
        ["Costes de cambio", "☐ Moderados", "Cambiar de mayorista (帳合変更) exige rehacer logística, sistemas y lineales; pero el riesgo de cambio aparece como riesgo declarado y «cambios en las condiciones de algunos clientes» explican caídas en FY2/2026 y en el 1T FY2/2027.", "🟡"],
        ["Efecto red", "☐ Parcial", "Más fabricantes atraen a más minoristas y viceversa (plataforma de surtido de 20.000 referencias). Efecto débil: los minoristas grandes trabajan con varios mayoristas.", "🟡"],
        ["Ventajas de coste / escala", "☐ Parcial", "Red nacional de ≈20 centros, densidad de entregas y n.º 2 especializado. Pero Japell es 1,8x más grande y los generalistas (Arata, 1 billón de JPY de ventas) tienen escala logística muy superior.", "🟡"],
    ], size=8)
    D.src(YUHO[2026] + ", p.17 (riesgo (3) 取引条件の大幅な変更), p.18; " + Q1 + ", p.2")
    D.box("**Conclusión moat: ESTRECHO / INEXISTENTE (más cerca de inexistente).** 🟡 La escala logística y la especialización dan un ROIC del 8-12% en años normales, aceptable gracias a la rotación (2,9x). Pero un margen operativo del 1% que cae, la pérdida de condiciones con clientes y la dependencia de rappels indican que **el valor generado lo capturan fabricantes y grandes minoristas**.", fill="FFF4E5")

    D.h1("2.2 Concentración de Clientes")
    D.table(["Cliente", "FY2/2025", "FY2/2026", "Comentario"], [
        ["Rakuten Group", "<10% (no desglosado)", "11.073 M JPY (10,5%)", "🟡 Nuevo cliente >10%: canal EC en crecimiento, pero con alto poder negociador"],
        ["Resto de clientes", "Ninguno >10%", "Ninguno >10%", "Home centers, droguerías, supermercados, tiendas especializadas"],
    ], size=8.5)
    D.src(YUHO[2026] + ", p.20; " + YUHO[2025] + ", p.19")
    D.p("🟡 **Concentración moderada.** El riesgo no es tanto un cliente concreto como el **«cambio de mayorista» (帳合変更)** en cuentas grandes, que la empresa declara como riesgo principal y que ya cita como causa de la caída del BO en el 1T FY2/2027 (BO de 8 M JPY frente a 206).")
    D.src(Q1 + ", p.2: «一部のお得意先様における取引内容の変更等の影響»")

    D.h1("2.3 Posicionamiento Competitivo")
    D.table(["Aspecto", "Evaluación"], [
        ["Posición", "**N.º 2 en distribución especializada para mascotas** (tras Japell); challenger frente a los generalistas."],
        ["Competidores", "Japell (líder, no cotizada, 187.000 M JPY); Arata (2733, división de mascotas); PALTAC (8283, en OPA de Medipal); Kokubu (accionista y a la vez proveedor/competidor potencial); importadores de nicho; venta directa de fabricantes al comercio electrónico."],
        ["Diferenciadores", "Especialización y conocimiento de categoría; concepto «CED»; feria Pet Kingdom; formación para tiendas; gestión de tiendas (Pets Value); análisis de datos y IA generativa (nuevo plan)."],
        ["Barreras de entrada", "🟡 Moderadas: red logística nacional, relaciones con fabricantes y sistemas. Pero los generalistas pueden ampliar su surtido de mascotas con poco coste incremental."],
        ["Poder de los clientes", "🔴 Alto: grandes cadenas en consolidación y el comercio electrónico (Rakuten)."],
        ["Poder de los proveedores", "🔴 Alto: multinacionales (Mars, Nestlé, Colgate-Hill's) y grandes nacionales (Unicharm, Inaba) fijan los precios y las condiciones de rappel."],
        ["Sustitutos", "🟡 Venta directa del fabricante (D2C) y logística propia de los grandes minoristas."],
    ], size=8.5)

    D.h1("2.4 Análisis del Mercado")
    D.table(["Indicador", "FY2024", "FY2025E", "FY2027E", "Fuente"], [
        ["Mercado de mascotas en Japón (M JPY)", "1.910.800 (+2,6%)", "1.925.700", "2.027.900", "Yano Research ⚠️ secundario"],
        ["Valor de la comida para mascotas (M JPY)", "459.400 (9.º año de aumento)", "n.d.", "n.d.", "Yano / asociación de comida para mascotas ⚠️"],
        ["Ventas de Echo (M JPY; ejercicio a febrero)", "107.406 (FY2/24)", "106.388 (FY2/25)", "110.000 (previsión FY2/27)", "Yuho / Tanshin 🔍"],
        ["Ventas de Japell (M JPY; ejercicio a marzo)", "≈176.600", "187.000 (FY3/25)", "n.d.", "nissyoku.co.jp ⚠️"],
        ["Echo / Japell", "≈61%", "≈57%", "", "💡 Echo pierde terreno frente al líder"],
    ], size=8)
    D.calc("Japell FY3/2024 ≈ 187.000/1,059 = 176.600 (a partir de su +5,9% publicado). Ratio Echo/Japell: 107.406/176.600 = 61%; 106.388/187.000 = 57%. 🔴 Mientras Japell creció +5,9%, Echo bajó −0,9% en el periodo comparable.")

    D.h1("2.5 Necesidad del Cliente")
    D.p("🟢 **Necesidad real y recurrente.** La comida para mascotas es un consumo diario y no aplazable (las mascotas son «familia»); los minoristas necesitan reposición frecuente de un surtido muy fragmentado. Para el minorista, el mayorista es **crítico** en logística y surtido, pero **sustituible** entre mayoristas. Para el fabricante, es un canal útil pero no exclusivo.")

    D.h1("2.6 Costes de Cambio")
    D.p("**Switching costs: MODERADOS.** 🟡 El cambio de mayorista es costoso a corto plazo (sistemas EDI, planogramas, logística), pero frecuente en el sector japonés, donde las grandes cadenas renegocian y reasignan categorías («帳合変更»). Echo lo cita como riesgo n.º 3 y como causa de pérdidas recientes: la evidencia indica que los costes de cambio **no protegen** el margen.")

    D.h1("2.7 Ventaja Competitiva Sostenible")
    D.p("La ventaja más defendible es la **especialización de categoría**: datos de venta, conocimiento del producto, formación y propuestas de lineal, que los generalistas no siempre igualan. A esto se suman la **red logística nacional** y la **relación con Kokubu** (acceso a su red de alimentación y a sus clientes de supermercado). 🟡 Son ventajas que sostienen la cuota pero no el margen. El nuevo plan (2027-) apuesta por **datos e IA generativa** y por marcas propias (I&I) para «salir de la competencia en precio». ⚠️ Es una apuesta todavía sin resultados medibles.")
    D.src(YUHO[2026] + ", p.10-11")

    D.h1("2.8 Poder de Pricing")
    D.table(["Ejercicio", "Ventas", "Margen bruto", "Explicación de la dirección"], [
        ["FY2/2022", "+7,3%", "11,73%", "Demanda por COVID; costes logísticos al alza"],
        ["FY2/2023", "+5,5% (nueva norma)", "11,54%", "Gestión por producto (単品管理); subidas de proveedores"],
        ["FY2/2024", "+10,8%", "11,57%", "**Subidas de precio de los fabricantes** y productos de mayor valor añadido"],
        ["FY2/2025", "−0,9%", "11,32%", "Inversión en logística y nueva sede"],
        ["FY2/2026", "−0,5%", "11,14%", "«Efecto de las subidas de precio agotado»; **empeoramiento del margen por la competencia en precio**"],
        ["1T FY2/2027", "+2,9%", "10,18%", "Ventas al alza, pero **cambios de condiciones con algunos clientes** y fletes"],
    ], size=8)
    D.src("MD&A de los Yuho FY2/2022-26; " + Q1 + ", p.2 y p.5; margen bruto: " + TIKR)
    D.p("🔴 **Sin poder de precio**: Echo traslada las subidas de los fabricantes, pero no puede defender su propio margen. El margen bruto pierde ≈0,15 pp por año de media (−0,59 pp entre FY2/2022 y FY2/2026) y en el 1T FY2/2027 cae a 10,18% (−0,75 pp interanual).")
    D.calc("Margen bruto 1T FY2/2027 = 2.779/27.285 = 10,18%; 1T FY2/2026 = 2.896/26.508 = 10,92%.")

    D.h1("2.9 Proveedores")
    D.table(["Proveedor", "Relación", "Dato"], [
        ["Kokubu Group (accionista del 18,2%)", "Proveedor y accionista; un consejero de Echo es directivo de Kokubu", "Compras de 10.822 M JPY (11,5% de las compras); saldo a pagar de 2.934 M JPY 🔍"],
        ["Fabricantes de comida (Mars, Nestlé Purina, Hill's, Unicharm, Inaba, Petline, etc.) ⚠️", "Proveedores principales (no desglosados)", "Compras totales de 94.272 M JPY (FY2/2026): comida 79%, accesorios 21%"],
        ["Itochu (accionista del 3,6%)", "Trading general (relación histórica) ⚠️", "—"],
        ["«Echo Trading Kyoeikai» (asociación de proveedores-accionistas, 5,6%)", "Los proveedores invierten en Echo a través de su asociación", "342 miles de acciones"],
    ], size=8)
    D.src(YUHO[2026] + ", p.21 (仕入実績), p.26 (大株主), p.77 (関連当事者)")
    D.p("🟡 Los proveedores son **también accionistas** (Kokubu, Kyoeikai, Itochu: ≈27% entre los tres). Esto estabiliza las relaciones, pero alinea a la empresa con proveedores más que con el minoritario.")

    D.h1("Conclusión de la Sección 2")
    D.box("🔴/🟡 **Moat estrecho-inexistente.** Echo es útil para la cadena, pero está atrapada entre proveedores potentes y clientes en consolidación. Su margen bruto se erosiona y pierde cuota frente al líder Japell. 🟢 La especialización, la red nacional y el vínculo con Kokubu dan estabilidad. **Para 6-18 meses la tesis no puede basarse en la ventaja competitiva**: depende de la valoración y de una posible operación corporativa.", fill="FDECEA")
    return D.save(out, "Ventaja_Competitiva")
