from helpers import *
from data import *


def build(out):
    D = Doc(1, "Entender el Negocio - Lo Básico")
    D.h1("Resumen ejecutivo de la sección")
    D.box(
        "**Qué es:** Echo Trading (エコートレーディング, «Echo») es el **segundo mayorista especializado de comida y accesorios para mascotas de Japón**. Fundada en Osaka en 1971, cotiza en el segmento Standard de la Bolsa de Tokio y su accionista de referencia es el gran distribuidor alimentario **Kokubu** (18,2%).\n"
        "**Cómo gana dinero:** compra unas 20.000 referencias a fabricantes nacionales e internacionales y a Kokubu y las distribuye a cadenas de bricolaje y hogar (home centers), droguerías, supermercados, tiendas especializadas y comercio electrónico (Rakuten es ya el 10,5% de las ventas). Gana un **margen bruto de ≈11%** que, tras logística (5% de ventas), personal y alquileres, deja un **margen operativo de solo 1,0-1,6%**. Las rebajas por volumen que pagan los proveedores (rappels, 2.199 M JPY pendientes de cobro) son clave en el beneficio.\n"
        "**Dónde opera:** 100% Japón, mercado de mascotas de ≈1,9 billones de JPY que crece ≈2-3% al año por precio y por la «humanización» de las mascotas, pero con **volúmenes estancados** (menos perros y gatos estables).\n"
        "**Lectura inversora:** negocio de distribución de margen muy fino, sin crecimiento real y con beneficios en caída desde el máximo de FY2/2024, pero que cotiza a **0,42x el valor contable y ≈0,5x su NCAV**. Además, el sector se está consolidando con salidas de bolsa promovidas por los grandes accionistas.",
        fill="EAF1FB")

    D.h1("1.1 Modelo de Negocio")
    D.h2("Actividad principal y estructura del grupo")
    D.p("🔍 El grupo está formado por la matriz, **tres filiales** y una «sociedad vinculada» (その他の関係会社), Kokubu Group, con un 18,2% de los votos. Tiene un único segmento contable («negocio relacionado con mascotas»):")
    D.table(["Sociedad", "Actividad", "Relación"], [
        ["Echo Trading K.K. (matriz)", "Mayorista de comida y accesorios para mascotas; formación (escuela Echo Pet Business, traspasada en abr-2026); eventos (feria «Pet Kingdom»)", "Cotizada (TSE Standard 7427)"],
        ["Pets Value K.K.", "Desarrollo y gestión de tiendas de mascotas para clientes (200 tiendas gestionadas); antes también producto propio", "Filial 100%"],
        ["I&I K.K.", "Producto propio (marca «ShareZ», «GOODISH» procedente de Fancl) y material promocional para tiendas; desde FY2/2027 centraliza todo el desarrollo de producto", "Filial 100% (desde feb-2026)"],
        ["PetPet K.K.", "Portal de información para mascotas (cerrado en sep-2025; ya sin actividad)", "Filial 100%"],
        ["Kokubu Group Honsha", "Gran distribuidor de alimentación y bebidas (no cotizado). **Accionista principal y a la vez proveedor** (compras de 10.822 M JPY en FY2/2026)", "Sociedad vinculada (18,2%)"],
    ], size=8.5)
    D.src(YUHO[2026] + ", p.6-7 (事業の内容, 関係会社の状況) y p.77 (関連当事者情報)")

    D.h2("Productos y servicios")
    D.p("Distribuye **comida para mascotas** (78,4% de las ventas de FY2/2026: gato, snacks, perro, pequeños animales y peces) y **accesorios** (21,2%: arena, empapadores, juguetes, collares, jaulas, cuidado). Añade servicios de valor: planificación de lineales y categorías («la mejor empresa de planificación de categorías de mascotas del mundo» es su lema), material promocional, formación para personal de tiendas (e-learning «Echo Study»), gestión de tiendas especializadas (Pets Value) y la feria anual **«Minna Daisuki!! Pet Kingdom»** (≈40.000 visitantes en 2023).")
    D.src(YUHO[2026] + ", p.18-20; " + YUHO[2024] + ", p.17")

    D.h2("Propuesta de valor")
    D.p("Para un **fabricante**, Echo da acceso a miles de puntos de venta en todo Japón con una sola relación logística y comercial. Para un **minorista** (home center, droguería, supermercado), Echo agrupa en un solo pedido y una sola entrega cientos de proveedores pequeños de un surtido muy fragmentado (20.000 referencias), gestiona la categoría completa y asume el riesgo de stock. Su discurso estratégico, el concepto **«CED»** (Communication, Education/Entertainment, Design, al que se añaden Connect y Data Science en el nuevo plan), busca diferenciarse con propuestas de valor y no por precio.")
    D.src(YUHO[2026] + ", p.10-11 «経営方針» y «対処すべき課題»; " + Q1 + ", p.2")
    D.p("⚠️ ESPECULACIÓN razonada: es una propuesta real (la distribución japonesa está muy fragmentada y los minoristas externalizan la gestión de categorías), pero **replicable por mayoristas generalistas** (Arata, PALTAC, Kokubu) y por el líder especializado Japell. El margen operativo del 1% muestra que el poder de negociación lo tienen fabricantes y grandes cadenas.")

    D.h2("Evolución histórica")
    D.table(["Año", "Hito"], [
        ["1971", "Fundación en Osaka como Echo Hanbai: venta de comida para mascotas, aves y peces"],
        ["1975-1993", "Red nacional de oficinas (Sapporo, Tokio, Nagoya, Fukuoka, Hiroshima, Sendai…)"],
        ["1992", "Absorbe Nihon Max y Yamato Kogyo; nuevo nombre: Echo Trading"],
        ["1995 / 2003 / 2005", "Cotiza en Osaka (2.ª sección), en Tokio (2.ª) y pasa a la 1.ª sección"],
        ["2000", "Crea Pets Value y la escuela Echo Pet Business"],
        ["2013", "**Alianza de capital y negocio con Kokubu**, que pasa a primer accionista (18,31%)"],
        ["2016", "Llega como presidente Minoru Toyoda (ex Nisshin Seifun Premix); sociedad con comité de auditoría"],
        ["2021", "Plan a medio plazo «I3☆55» (FY2/2022-FY2/2026)"],
        ["2022", "Paso al segmento Standard; oficina central en Tokio"],
        ["2024", "Traslado de la sede a Osaka-Miyahara; venta de la antigua sede de Nishinomiya (plusvalía de 205 M JPY)"],
        ["2025", "Cierre del portal PetPet; Rakuten pasa a ser cliente >10%"],
        ["2026", "Venta de la escuela a Yashima Gakuen; **nuevo plan a medio plazo** («Desafío, hacia un mayor crecimiento»); marca GOODISH (de Fancl)"],
    ], widths=[3.2, 13.8], size=8.5)
    D.src(YUHO[2026] + ", p.4-5 «沿革» y p.18; " + Q1 + ", p.2")

    D.h1("1.2 Productos y Evolución de Ventas")
    rows = []
    for y in Y:
        d, c, s, sm, g1, g2, o = mix[y]
        rows.append([f"FY2/{y}", n(d), n(c), n(s), n(sm), n(d + c + s + sm), n(g1), n(g2), n(g1 + g2), n(o), n(sales[y])])
    D.table(["Ejercicio", "Perro", "Gato", "Snacks", "Peq. animal/peces", "Total comida", "Accesorios perro/gato", "Otros accesorios", "Total accesorios", "Otros", "Total"], rows, size=7)
    D.src("Cuadro «販売実績» por productos: " + YUHO[2022] + " p.12; " + YUHO[2023] + " p.12; " + YUHO[2024] + " p.19; " + YUHO[2025] + " p.19; " + YUHO[2026] + " p.20. FY2/2023 aplica por primera vez la norma de reconocimiento de ingresos (no comparable al 100%)")
    rows = []
    for y in Y:
        d, c, s, sm, g1, g2, o = mix[y]
        t = sales[y]
        rows.append([f"FY2/{y}", pct(d / t * 100), pct(c / t * 100), pct(s / t * 100), pct((d + c + s + sm) / t * 100), pct((g1 + g2) / t * 100)])
    D.table(["Ejercicio", "% Perro", "% Gato", "% Snacks", "% Comida total", "% Accesorios"], rows)
    D.calc(f"CAGR de ventas FY2/2022→FY2/2026 = (105.811/91.930)^(1/4) − 1 = **+3,6%**; FY2/2019→FY2/2026 = **+3,9%**. Comida de gato: +8,5% anual (25.354→35.180). Accesorios: −2,8% anual (25.210→22.474).")
    D.p("**Lectura:** 🟢 la mezcla se desplaza hacia la **comida (78%) y en especial la de gato** (33% de las ventas, el segmento más dinámico de Japón). 🔴 Los **accesorios caen en 3 de los últimos 4 años** (−11% acumulado desde FY2/2022) y los «otros accesorios» se han reducido a la mitad: es el efecto de la estrategia de «selección y concentración» y de la pérdida de algunos clientes. 🟡 El salto de FY2/2024 (+10,8%) se debió casi por completo a **subidas de precio** de los fabricantes; desde entonces las ventas retroceden (−0,9% y −0,5%) porque «el efecto de las subidas de precios se ha agotado» y algunos clientes han cambiado sus condiciones.")
    D.src(YUHO[2024] + ", p.17; " + YUHO[2026] + ", p.18")

    D.h1("1.3 Segmentación de Ingresos")
    D.h2("Por segmento y geografía")
    D.p("🔍 **Segmento único** («negocio relacionado con mascotas») y **100% Japón** (no hay ventas al exterior). Por eso la única segmentación disponible es la de producto (1.2) y la de clientes.")
    D.h2("Por canal y cliente")
    D.table(["Canal / cliente", "Evidencia", "Peso"], [
        ["**Rakuten Group** (comercio electrónico)", "Primer cliente que supera el 10%: 11.073 M JPY en FY2/2026", "**10,5%** 🔍"],
        ["Home centers (Kohnan, DCM, Arenza)", "Participaciones en clientes («政策保有株式»): Kohnan 350 M JPY, DCM 38, Arenza 23", "n.d. (canal principal ⚠️)"],
        ["Droguerías (Genky DrugStores)", "Participación de 116 M JPY", "n.d."],
        ["Supermercados y grandes superficies (AEON, Okuwa, Life, H2O Retailing)", "Participaciones de 67 / 53 / 33 / 29 M JPY", "n.d."],
        ["Comercio electrónico especializado (PetGo)", "Participación de 32 M JPY", "n.d."],
        ["Tiendas especializadas (200 gestionadas por Pets Value)", "Pets Value: de 268 tiendas (FY2/2022) a 200 (FY2/2026)", "n.d."],
    ], size=8)
    D.src(YUHO[2026] + ", p.20 (相手先別販売実績) y p.47-48 (特定投資株式)")
    D.p("⚠️ La presencia de Rakuten por encima del 10% es **nueva** en FY2/2026. Comercio electrónico de bajo margen y alta exigencia logística: explica parte de la caída del margen bruto (de 11,32% a 11,14%) y abre una **dependencia comercial**.")

    D.h1("1.4 KPIs Clave del Negocio")
    rows = [
        ["Ventas (M JPY)"] + [n(sales[y]) for y in Y],
        ["Margen bruto"] + [pct(gp[y] / sales[y] * 100, 2) for y in Y],
        ["SG&A / ventas"] + [pct((gp[y] - op[y]) / sales[y] * 100, 2) for y in Y],
        ["Margen operativo"] + [pct(op[y] / sales[y] * 100, 2) for y in Y],
        ["Beneficio operativo (M JPY)"] + [n(op[y]) for y in Y],
        ["Plantilla (+ temporales medios)"] + [f"{emp[y][0]} ({emp[y][1]})" for y in Y],
        ["Ventas por empleado (M JPY)"] + [n(sales[y] / emp[y][0]) for y in Y],
        ["Tiendas gestionadas por Pets Value"] + [str(stores[y]) for y in Y],
        ["Fletes y embalaje (M JPY)", "n.d.", "n.d.", "n.d.", "5.256", "5.294"],
        ["Alquileres (M JPY)", "n.d.", "n.d.", "n.d.", "1.059", "1.080"],
        ["Rappels de proveedores pendientes de cobro", "n.d.", "n.d.", "n.d.", "n.d.", "2.199"],
    ]
    D.table(["KPI"] + [f"FY2/{y}" for y in Y], rows, size=8)
    D.src(TIKR + "; Yuho FY2/2022-26 (従業員の状況, MD&A); " + YUHO[2026] + ", p.54 (gastos), p.94 (KAM, rappels)")
    D.p("🔴 **El margen bruto baja en 3 de los últimos 4 años** (11,73% → 11,14%; LTM 10,95%) por la «competencia en precios dentro del sector» y la mezcla de clientes. 🟢 La plantilla se reduce (340 → 300) y las ventas por empleado suben de 270 a 353 M JPY. 🔴 La logística (5,0% de las ventas) y los alquileres (1,0%) son costes que suben con la inflación japonesa de salarios y transporte (la «crisis logística de 2024»).")

    D.h1("1.5 Clasificación Sectorial y KPIs de Pat Dorsey")
    D.p("La guía de Dorsey no tiene un capítulo específico para distribución mayorista. Echo es un **distribuidor B2B de bienes de consumo**. Aplicamos (i) los KPIs universales y de activos físicos/logística de **Servicios Empresariales** (sección 3: rotación de activos, densidad logística, ROIC, FCF/BN) y (ii) los KPIs de cadena de suministro de **Bienes de Consumo** (sección 10: rotación de inventario, días de existencias, crecimiento volumen vs precio).")
    D.src("GUIA_SECTORES_Y_KPIS_COMPLETA.md, secciones 3 (A y D) y 10 (A, B y E)")
    ebitda = op[2026] + da[2026]
    D.table(["KPI Dorsey", "Benchmark guía", "Echo FY2/2026", "Valoración"], [
        ["Crecimiento de ingresos", ">5-10% (servicios)", "−0,5% (CAGR 4 años +3,6%)", "🔴"],
        ["Margen EBITDA", ">15-25%", "1,1%", "🔴 (normal en distribución)"],
        ["Margen operativo", ">12-20%", "1,05%", "🔴"],
        ["ROIC (NOPAT/capital invertido)", ">15%", "≈9,6% (FY2/2024 11,6%)", "🟡"],
        ["ROE", ">20% (consumo)", "6,6% (máx. 12,0% en FY2/2024)", "🟡"],
        ["FCF / BN", ">100%", "Volátil: 482% (FY2/2026) / −10% (FY2/2025)", "🟡"],
        ["Rotación de activos", ">1,0x", "2,9x", "🟢"],
        ["Rotación de inventario", ">6-10x", "≈26x (14 días)", "🟢"],
        ["Días de inventario", "<60 días", "14 días", "🟢"],
        ["Ciclo de caja", "<60 días", "≈18-30 días", "🟢"],
        ["Volumen vs precio", "Volumen +1-3%", "Volumen negativo; crecimiento vía precio", "🔴"],
        ["Concentración de clientes", "<30% top 10", "1 cliente >10% (Rakuten 10,5%)", "🟡"],
        ["Deuda neta / EBITDA", "<2x", "Caja neta (normalizada ≈1.000-1.500)", "🟢"],
        ["CapEx de mantenimiento / CapEx total", "<50%", "Modelo asset-light (CapEx ≈0,2% de ventas)", "🟢"],
    ], size=8)
    D.calc(f"EBITDA FY2/2026 = BO 1.110 + amortización 94 = {n(ebitda)} M JPY. ROIC = BO × (1 − 34%) / (PN 12.178 + deuda 1.650 − caja 6.231) = 733 / 7.597 = 9,6%. Rotación de activos = 105.811 / media (34.065; 38.899) = 2,9x. Días de inventario = 3.530 / coste de ventas 94.025 × 365 = 14 días.")
    D.box("**Evaluación de moat (preliminar): ESTRECHO a INEXISTENTE.** 🟡 Hay escala logística nacional (≈20 centros), relaciones de décadas y conocimiento de categoría, que dan un ROIC aceptable (8-12%) gracias a la alta rotación. Pero el margen del 1% y su caída sostenida muestran que **no hay poder de precio**. Se detalla en la Sección 2.", fill="FFF4E5")

    D.h1("1.6 Mecánica de Generación de Ingresos")
    D.h2("Modelo de pricing")
    D.bullets([
        "**Precio de compra − precio de venta = margen bruto (≈11%)**. El precio de venta al minorista se negocia por cuenta y por categoría. Cuando los fabricantes suben precios (FY2/2023-24), las ventas suben y el margen absoluto también; cuando el efecto de esas subidas se agota, el margen se estrecha por la competencia.",
        "**Rappels y promociones de proveedores (仕入割戻金)**: parte crucial del beneficio. Rappels pendientes de cobro a cierre: 2.199 M JPY (≈2x el BO). El auditor (Deloitte Tohmatsu) lo considera **asunto clave de auditoría (KAM)** por su importancia y complejidad.",
        "**Ingresos netos de descuentos y devoluciones**; reconocimiento en el momento de la expedición. El cobro llega «generalmente en 3 meses».",
        "**Logística como principal coste variable**: fletes y embalaje de 5.294 M JPY (5,0% de las ventas). Iniciativas: entregas conjuntas, preparación simultánea de pedidos con tabletas, AI-OCR, centros nuevos (Hashima en 2023, Takaoka en 2024, Hayashima en 2026).",
    ])
    D.src(YUHO[2026] + ", p.59-60 (収益認識), p.54 (gastos), p.94 (KAM); " + YUHO[2025] + ", p.17")
    D.h2("Estacionalidad")
    D.p("Moderada. El **1T (mar-may)** incluye la feria Pet Kingdom (mayo) y suele tener ventas altas (26.508 M JPY en el 1T FY2/2026, el 25% del año). El margen se resiente en trimestres con revisiones de condiciones comerciales. 🔴 **Efecto calendario muy relevante en el balance y los flujos**: cuando el cierre cae en día festivo bancario (28-feb-2021 domingo, 28-feb-2026 sábado, 31-may-2026 domingo), cobros y pagos se desplazan al mes siguiente y **clientes, proveedores, caja y OCF quedan inflados**.")
    D.src(YUHO[2026] + ", p.19 (explicación de la empresa sobre el efecto festivo); " + YUHO[2022] + ", p.11; " + Q1)
    D.h2("Ciclo de conversión de caja")
    rows = []
    for y in Y:
        cogs = sales[y] - gp[y]
        dso = rec[y] / sales[y] * 365; dio = inv[y] / cogs * 365; dpo = pay[y] / cogs * 365
        rows.append([f"FY2/{y}", n(dso), n(dio), n(dpo), n(dso + dio - dpo), "Sí (sábado)" if y == 2026 else "No"])
    D.table(["Ejercicio", "DSO", "DIO", "DPO", "CCC (días)", "¿Cierre en festivo?"], rows)
    D.calc("DSO = clientes/ventas×365; DIO = existencias/coste de ventas×365; DPO = proveedores/coste de ventas×365.")
    D.p("🟢 Ciclo de caja corto (≈30 días en años normales): los proveedores financian buena parte de los clientes. Al crecer las ventas, el circulante absorbe ≈6% del incremento. 🔴 FY2/2026 (18 días) está **distorsionado** por el cierre en sábado.")
    D.h2("Drivers de ingresos")
    D.table(["Driver", "Efecto", "Situación oct-2026"], [
        ["Subidas de precio de fabricantes (inflación de materias primas, yen)", "+ ventas, + margen absoluto", "🟡 efecto agotado en FY2/2026; nuevas subidas en 2026 posibles"],
        ["Número de mascotas (perros ↓, gatos =)", "Volumen", "🔴 estructuralmente negativo"],
        ["Premiumización / «humanización» (comida fresca, salud)", "+ precio medio", "🟢 tendencia de fondo"],
        ["Clientes clave (Rakuten, home centers)", "Volumen y margen", "🟡 Rakuten en aumento, a cambio de menor margen"],
        ["Costes logísticos y laborales", "− margen", "🔴 suben («crisis logística 2024»)"],
        ["Consolidación de minoristas", "Poder del comprador", "🔴 aumenta"],
    ], size=8.5)

    D.h1("1.7 El mercado en el que opera")
    D.p("🔍/💡 **Mercado de productos y servicios para mascotas en Japón: 1,9108 billones de JPY en FY2024 (+2,6%), 1,9257 billones previstos en FY2025 y 2,0279 billones en FY2027** (Yano Research). El valor de la comida para mascotas suma **9 años seguidos de aumento (459.400 M JPY)**, mientras el **volumen sigue cayendo**: el crecimiento es de precio y de mayor valor añadido. El número de perros y gatos se ha estancado y el gasto por animal crece.")
    D.src("Yano Research Institute, notas de prensa 3906 y 4169 (yano.co.jp, 2025-2026), vía búsqueda web del 3-oct-2026")
    D.p("**Estructura de la distribución:** el líder especializado es **Japell** (no cotizada, 187.000 M JPY de ventas en FY3/2025). Le siguen **Echo** (≈106.000 M JPY) y los mayoristas generalistas de droguería y hogar (**Arata**, con una división de mascotas; **PALTAC**) y de alimentación (**Kokubu**, accionista de Echo). Hay también importadores y distribuidores de nicho. ⚠️ Cuota estimada de Echo en la distribución mayorista de productos para mascotas: ≈15-20%.")
    D.calc("Comida distribuida por Echo (83.006 M JPY, a precio mayorista) / valor de la comida en el mercado (459.400 M JPY) ≈ 18%. Son magnitudes de distinto nivel de la cadena (precio de fábrica vs mayorista), así que es solo una aproximación.")
    D.src("Japell: nissyoku.co.jp (2025); " + YUHO[2026])
    D.p("**Tendencias:** 🔴 consolidación del comercio minorista (fusiones de home centers y droguerías) y presión de los costes logísticos; 🔴 **consolidación del sector mayorista con salidas de bolsa promovidas por los grandes accionistas**: Mitsubishi Corp compró el resto de Mitsubishi Shokuhin (sep-2025), Itochu el de Itochu Shokuhin (abr-2026) y Medipal lanzó una OPA sobre PALTAC con una prima del 43% (jul-2026); 🟢 premiumización y comida fresca; 🟢 crecimiento del comercio electrónico (Rakuten).")
    D.src("Búsquedas web 3-oct-2026: kabukiso.com y lnews.jp (OPA de PALTAC); edinetdb/itochu-shokuhin.com (exclusión de Itochu Shokuhin); traders/edinetdb (Mitsubishi Shokuhin)")

    D.h1("Conclusión de la Sección 1")
    D.box("🟡 **Negocio sencillo y útil, pero de margen mínimo**: Echo es un logista-mayorista especializado con 100.000 M JPY de ventas, 1% de margen operativo y alta rotación de activos. 🟢 Su posición de n.º 2 especializado, la exposición a la premiumización (gato, snacks, comida fresca) y la estructura asset-light son fortalezas. 🔴 El volumen no crece, el margen bruto se erosiona desde hace 4 años y el beneficio cae desde el máximo de FY2/2024 (BO de 1.720 → 1.110 → 1T FY2/2027 de solo 8 M JPY). 🟢 La valoración (P/B de 0,42x) y el contexto de consolidación son el núcleo de la tesis.", fill="FFF4E5")
    return D.save(out, "Entender_el_Negocio")
