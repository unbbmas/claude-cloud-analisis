from helpers import *
from data import *


def build(out):
    D = Doc(1, "Entender el Negocio - Lo Básico")
    D.h1("Resumen ejecutivo de la sección")
    D.box(
        "**Qué es:** Nichiwa Sangyo (日和産業, «Nichiwa») es un fabricante independiente y de tamaño pequeño de **piensos compuestos (配合飼料)** para avicultura, porcino, vacuno y acuicultura, con sede en Kobe, fundado en 1924 y cotizado desde 1961. Opera **5 fábricas** en puertos de Japón y una filial ganadera (Towa Chikusan).\n"
        "**Cómo gana dinero:** compra maíz, harina de soja y otros granos (casi todo importado, pagado en USD), los muele y mezcla según fórmulas por especie, y los vende a ganaderos y distribuidores con un precio que se **revisa cada trimestre** siguiendo el coste de la materia prima. Gana un **margen bruto muy fino (4-9% de ventas)** que se amplía cuando el grano baja y se comprime cuando sube.\n"
        "**Dónde opera:** 100% Japón, mercado maduro de unos 23 millones de toneladas/año dominado por el sistema cooperativo JA Zen-Noh y por grandes grupos ligados a las tradings. Nichiwa es un actor de nicho regional (Kansai, Chugoku-Shikoku, Kyushu y Tohoku).\n"
        "**Lectura inversora:** negocio de commodity sin foso, rentabilidad sobre capital muy baja (ROE 0,7-3%), pero con un balance extraordinariamente líquido (caja neta ≈ 80% de la capitalización) que hace que la acción cotice por debajo de su valor de liquidación contable (NCAV).",
        fill="EAF1FB")

    # 1.1
    D.h1("1.1 Modelo de Negocio")
    D.h2("Actividad principal y estructura del grupo")
    D.p("🔍 El grupo está formado por la matriz Nichiwa Sangyo, **una filial consolidada** (Towa Chikusan K.K., 100%, Kagoshima, capital 50 M JPY) y **una asociada** no consolidada (Michinoku Shiryo K.K., Hachinohe). Su actividad principal es «la fabricación y venta de piensos compuestos para avicultura, porcino, vacuno y peces, utilizando cereales como materia prima principal», y de forma secundaria **la producción y venta de productos ganaderos** a través de la filial. Existen además dos filiales no consolidadas por irrelevancia (Takano Chiiki Chikusan Kankyo Shisetsu y NBI Bokujo).")
    D.src(YUHO[2026] + ", p.5 «事業の内容» y p.38 notas de consolidación")
    D.p("La empresa reporta **dos segmentos**:")
    D.bullets([
        "**Segmento Piensos (飼料事業)** – ≈96% de las ventas externas. Fabricación y venta de piensos compuestos para ganadería y acuicultura. Una parte se vende, a través de distribuidores, a la propia filial Towa Chikusan; el pienso para vacuno se fabrica parcialmente por encargo en la asociada Michinoku Shiryo. Incluye también la **compraventa de productos ganaderos producidos por sus clientes** (huevos, carne), actividad que funciona como mecanismo comercial y de cobro frente a ganaderos financiados por la empresa.",
        "**Segmento Ganadería (畜産事業)** – ≈4% de las ventas. Towa Chikusan cría cerdos (lechones y cebo) y pollos en granjas de Nagasaki (Shimabara/Unzen), Kagoshima (Kanoya-Kihoku) y Hyogo (Miki). Es un segmento estructuralmente deficitario o de equilibrio, que ha generado deterioros de activos en FY3/2024, FY3/2025 y FY3/2026.",
    ])
    D.src(YUHO[2026] + ", p.5 y p.57 (セグメント情報); " + YUHO[2021] + ", p.53")

    D.h2("Productos y servicios")
    D.p("Nichiwa vende **piensos compuestos formulados por especie y fase productiva**: ponedoras (huevo), pollos de engorde (broiler), porcino (lechones, cebo, reproductoras), vacuno lechero y de carne, y peces de acuicultura. A esto añade **asistencia técnica** a los ganaderos desde sus cinco fábricas (reuniones, formación, intercambio de información), y una oferta de **financiación comercial** (crédito largo a clientes, préstamos a largo plazo y compra de su producción) que es habitual en el sector japonés.")
    D.p("🔍 Líneas de I+D declaradas (79 M JPY en FY3/2026, 0,17% de ventas): (1) piensos que reducen el metano y otras cargas ambientales del estiércol; (2) piensos que mejoran la digestión y la productividad; (3) sustitutos naturales de los aditivos antimicrobianos en porcino. Los ensayos se hacen en las granjas del grupo.")
    D.src(YUHO[2026] + ", p.11 «研究開発活動»")

    D.h2("Propuesta de valor")
    D.p("La propuesta de valor de Nichiwa no se basa en marca ni en tecnología propietaria, sino en tres elementos: (i) **cercanía logística**, porque las fábricas están en puertos con silos de almacenamiento (Kobe, Mihara, Kagoshima, Hachinohe, Sakaide), lo que minimiza el coste de descarga del grano importado y el transporte del pienso (un producto voluminoso y de bajo valor por tonelada); (ii) **relación técnica y comercial de décadas** con ganaderos regionales; y (iii) **financiación y flexibilidad crediticia** que las cooperativas o los grandes grupos no siempre ofrecen a explotaciones medianas. Su lema corporativo es «お客様第一主義» (el cliente primero) y suministrar «pienso seguro, de buena calidad y de forma estable».")
    D.src(YUHO[2026] + ", p.6 «経営方針» y p.12 «主要な設備の状況»")
    D.p("⚠️ ESPECULACIÓN razonada: esta propuesta es defendible a escala local pero **no genera poder de precio**. El precio del pienso en Japón lo fija de facto el mercado (las revisiones trimestrales de JA Zen-Noh sirven de referencia) y el producto es casi una commodity.")

    D.h2("Evolución histórica")
    D.table(["Año", "Hito"], [
        ["1924 (ago)", "Fundación en Kobe como Nihon Kachiku Shiryo K.K. (日本家畜飼料)"],
        ["1927", "Designada fábrica de pienso compuesto por el Ministerio de Agricultura; oficinas en Dalian y Shimonoseki (cerradas en 1939)"],
        ["1948", "Cambio de nombre a Nichiwa Sangyo K.K."],
        ["1951", "Absorbe Hyogo Seiyu (aceites)"],
        ["1961", "Cotiza en la 2.ª sección de la Bolsa de Osaka"],
        ["1963 / 1968", "Fábrica de Mihara (Hiroshima) / fábrica de Kobe en terreno ganado al mar; sede actual en Kobe"],
        ["1974-1978", "Fábrica de Kagoshima y silos de almacenamiento en Kagoshima y Mihara"],
        ["1975", "Constitución de Towa Chikusan (filial ganadera)"],
        ["1983", "Fábrica de Hachinohe (Aomori)"],
        ["1986-1999", "Granjas Kihoku (1986), Unzen (1987) y Miki (1999)"],
        ["1995", "Fábrica de Sakaide (Kagawa)"],
        ["2003", "Michinoku Shiryo (Hachinohe), planta específica de pienso para vacuno, como asociada"],
        ["2013", "Pasa a la 2.ª sección de la Bolsa de Tokio por la fusión TSE-OSE"],
        ["2018", "Transfiere las granjas Kihoku y Unzen a Towa Chikusan"],
        ["2022 (feb)", "Recompra de 1,2 M de acciones (5,8% del capital) por 426 M JPY (355 JPY/acción)"],
        ["2022 (abr)", "Migración al segmento Standard de la TSE"],
        ["2024 (jun)", "Relevo generacional: Taichiro Nakahashi (hijo del anterior presidente) pasa a presidente"],
        ["2025 (jun)", "Paso a «sociedad con comité de auditoría y supervisión» (監査等委員会設置会社)"],
    ], widths=[3, 14])
    D.src(YUHO[2026] + ", p.4 «沿革» y p.22; " + YUHO[2022] + ", p.17 (自己株式の取得)")

    # 1.2
    D.h1("1.2 Productos y Evolución de Ventas")
    D.p("La empresa **no publica el desglose de ventas por especie animal ni el volumen en toneladas**. El único desglose de producto es el de segmentos (pienso vs. ganadería). La tabla muestra la serie larga de ventas consolidadas y la serie de segmentos.")
    rows = []
    prev = None
    for y in range(2017, 2027):
        g = "" if prev is None else pct((sales[y] / prev - 1) * 100)
        rows.append([f"FY3/{y}", n(sales[y]), g, n(ordinary[y]), n(ni[y])])
        prev = sales[y]
    D.table(["Ejercicio", "Ventas (M JPY)", "Var. a/a", "Beneficio ordinario", "Beneficio neto"], rows)
    D.src("FY3/2017-FY3/2021: " + YUHO[2021] + ", p.2; FY3/2022-FY3/2026: " + YUHO[2026] + ", p.2 (主要な経営指標等の推移)")
    D.calc(f"CAGR de ventas FY3/2021→FY3/2026 = (45.579 / 39.901)^(1/5) − 1 = **+2,7% anual**; en 9 años (FY3/2017→FY3/2026) = **+1,2% anual**. "
           "El crecimiento es casi íntegramente efecto precio (coste del grano y tipo de cambio), no volumen. El pico de FY3/2023 (54.659 M JPY) coincide con el máximo histórico del maíz tras la invasión de Ucrania y el yen débil.")

    rows = []
    for y in range(2020, 2027):
        fs, fo, ls, lo_ = seg[y]
        rows.append([f"FY3/{y}", n(fs), n(fo), pct(fo / fs * 100, 2), n(ls), n(lo_), pct(lo_ / ls * 100, 1), n(op[y])])
    D.table(["Ejercicio", "Piensos ventas", "Piensos BO", "Margen", "Ganadería ventas", "Ganadería BO", "Margen", "BO consolidado"], rows, size=8)
    D.src("Notas de segmentos: " + YUHO[2021] + " p.53; " + YUHO[2022] + " p.9; " + YUHO[2023] + " p.9; " + YUHO[2024] + " p.9; " + YUHO[2025] + " p.9; " + YUHO[2026] + " p.57-58. Ventas a clientes externos; BO = beneficio operativo del segmento antes de ajustes corporativos.")
    D.p("**Lectura:** 🟢 El segmento piensos ha **casi duplicado su margen** (de 0,5% en FY3/2023 a 3,4% en FY3/2026) gracias a la bajada del grano y a que la empresa trasladó precios con retraso a la baja. 🔴 El segmento ganadero acumula pérdidas operativas en 4 de los últimos 5 años y deterioros por 1.445 M JPY en tres ejercicios (168 + 644 + 633). 🟡 El primer trimestre de FY3/2027 mantiene la mejora: piensos +21,7% en BO y ganadería 60 M JPY de beneficio.")
    D.src(Q1 + ", p.4 y p.8")

    # 1.3
    D.h1("1.3 Segmentación de Ingresos")
    D.h2("Por segmento")
    D.table(["Segmento", "FY3/2024", "%", "FY3/2025", "%", "FY3/2026", "%", "1T FY3/2027", "%"], [
        ["Piensos", "51.157", "96,7%", "46.698", "96,1%", "43.669", "95,8%", "11.252", "95,6%"],
        ["Ganadería", "1.729", "3,3%", "1.879", "3,9%", "1.910", "4,2%", "512", "4,4%"],
        ["Total", "52.887", "100%", "48.577", "100%", "45.579", "100%", "11.764", "100%"],
    ])
    D.src(YUHO[2026] + ", p.57-58; " + YUHO[2024] + ", p.9; " + Q1 + ", p.8")
    D.h2("Por geografía")
    D.p("🔍 **100% Japón.** «No hay ventas a clientes externos fuera de Japón» y no hay activos fijos fuera de Japón. La exposición internacional está en el **lado del coste**: la mayoría de las materias primas son importadas (maíz de EE. UU. y Brasil, harina de soja), con precios indexados a la bolsa de Chicago y pagados en USD.")
    D.src(YUHO[2026] + ", p.59 «関連情報»; p.7 «事業等のリスク» (1) y (2)")
    D.p("💡 Por la ubicación de las fábricas, la distribución regional aproximada del negocio sería: **Kyushu** (Kagoshima + oficina de Nagasaki), **Chugoku-Shikoku** (Mihara + Sakaide), **Kansai** (Kobe) y **Tohoku** (Hachinohe, con producción adicional en Michinoku Shiryo). Kagoshima, Miyazaki y Aomori/Iwate están entre las grandes zonas ganaderas de Japón (porcino, broiler, vacuno de carne). La empresa no publica este desglose.")
    D.h2("Por cliente")
    D.p("🔍 **Ningún cliente supera el 10% de las ventas.** La base de clientes son explotaciones ganaderas, integradoras avícolas y distribuidores (特約店). Algunos clientes relevantes son también accionistas: **Jumonji Chicken Company** (integradora de pollos de Iwate y mayor accionista, con un 8,70%) refleja la relación comercial de Hachinohe con la cadena avícola de Tohoku. ⚠️ Esto último es una inferencia a partir del registro de accionistas, no un dato publicado de ventas.")
    D.src(YUHO[2026] + ", p.9 «販売実績» nota 2 y p.15 «大株主の状況»")

    # 1.4
    D.h1("1.4 KPIs Clave del Negocio")
    D.p("Nichiwa no publica KPIs operativos (toneladas, precio medio por tonelada, cuota de mercado ni utilización de capacidad). Esta tabla reúne los indicadores que sí se pueden extraer de los informes anuales y que explican el negocio.")
    rows = [["Ventas (M JPY)"] + [n(sales[y]) for y in Y],
            ["Margen bruto %"] + [pct(gp[y] / sales[y] * 100) for y in Y],
            ["BO piensos (M JPY)"] + [n(seg[y][1]) for y in Y],
            ["BO ganadería (M JPY)"] + [n(seg[y][3]) for y in Y],
            ["Aportación al Fondo de Estabilización del Precio del Pienso"] + [n(fund[y]) for y in Y],
            ["Fondo / Ventas %"] + [pct(fund[y] / sales[y] * 100, 2) for y in Y],
            ["Valor de producción de piensos (a coste)", "33.306", "n.d.", "n.d.", "n.d.", "40.676", "37.151"],
            ["Gasto en I+D", "85", "83", "74", "71", "74", "79"],
            ["Plantilla consolidada (+temporales)", "180 (33)", "179 (35)", "183 (38)", "187 (36)", "178 (39)", "179 (44)"],
            ["Ventas por empleado (M JPY)"] + [n(sales[y] / e, 0) for y, e in zip(Y, [180, 179, 183, 187, 178, 179])],
            ["Clientes en concurso/insolvencia (bruto, M JPY)"] + [n(bankr[y]) for y in Y],
            ]
    D.table(["KPI"] + [f"FY3/{y}" for y in Y], rows, size=8)
    D.src("Yuho FY3/2021-FY3/2026: estados consolidados, notas de gastos de venta («飼料価格安定基金負担金»), «生産実績», «研究開発活動», «従業員の状況»")
    D.p("**Interpretación:** 🔴 la aportación al **Fondo de Estabilización del Precio del Pienso** (飼料価格安定基金) ha pasado de 0 en FY3/2021 a 1.198-1.240 M JPY en FY3/2025-26, equivalente al **82% del beneficio operativo de FY3/2026**. Es un coste regulado que el sector paga para compensar a los ganaderos cuando sube el pienso, y que tiende a aumentar tras años de grano caro (el fondo tiene que reponerse). 🟢 Un volumen plano con margen bruto en máximos de 9,1% indica que el beneficio actual depende de un **diferencial transitorio** entre el precio de venta y el coste.")

    # 1.5
    D.h1("1.5 Clasificación Sectorial y KPIs de Pat Dorsey")
    D.h2("Clasificación")
    D.p("La Bolsa de Tokio clasifica a Nichiwa en «食料品» (alimentación), que en la guía de Dorsey correspondería a **Bienes de Consumo – Alimentos**. Económicamente, sin embargo, Nichiwa **no vende marcas al consumidor**: transforma una commodity agrícola en un insumo B2B con margen fino. Por eso aplicamos el marco de **Materiales Industriales – commodities / transformadores** (rentabilidad a lo largo del ciclo, traslado de costes, balance y circulante) y lo complementamos con los KPIs de cadena de suministro de Bienes de Consumo.")
    D.src("GUIA_SECTORES_Y_KPIS_COMPLETA.md, secciones 10 (Bienes de Consumo) y 11 (Materiales Industriales)")
    D.h2("KPIs de Dorsey aplicados (FY3/2026 salvo indicación)")
    D.table(["KPI Dorsey", "Fórmula", "Benchmark guía", "Nichiwa", "Valoración"], [
        ["Margen bruto", "BB/Ventas", ">50-60% (consumo) / commodity bajo", "9,1% (media 6 años 6,4%)", "🔴 commodity puro"],
        ["Margen EBITDA", "EBITDA/Ventas", "12-18% a mitad de ciclo", "4,3% (máximo en 6 años)", "🔴"],
        ["Margen operativo", "EBIT/Ventas", "8-12% a mitad de ciclo", "3,2% (media FY21-26: 1,2%)", "🔴"],
        ["ROE", "BN/FP medios", "12-15% a mitad de ciclo", "2,0% (media 1,5%)", "🔴"],
        ["ROIC", "NOPAT/Capital invertido", "10-12%", "7,2% (pico); media ≈2,9%", "🔴"],
        ["Traslado de precios", "Δ precio / Δ coste", ">0,8x valor añadido", "≈1x con 1-2 trimestres de retraso", "🟡"],
        ["Deuda neta/EBITDA", "DN/EBITDA", "<2x", "Caja neta: −2,6x", "🟢"],
        ["Cobertura de intereses", "EBITDA/Intereses", ">5x", "27,7x", "🟢"],
        ["Ratio corriente", "AC/PC", ">1,5x", "2,33x", "🟢"],
        ["Deuda/Fondos propios", "Deuda/FP", "<0,5x", "0,23x", "🟢"],
        ["CapEx/Ventas", "CapEx/Ventas", "4-8% mantenimiento", "0,8% (media FY21-26: 1,4%)", "🟡 infrainversión"],
        ["CapEx/Amortización", "CapEx/D&A", "≈1,0x mantenimiento", "0,75x (FY21-24: 1,2-1,6x)", "🟡"],
        ["Rotación de activos", "Ventas/Activo total", ">1,0x", "1,48x", "🟢"],
        ["Rotación de activo fijo", "Ventas/PP&E", ">2x", "11,3x", "🟢"],
        ["DSO", "Clientes/Ventas×365", "<60 días", "91 días", "🔴"],
        ["DIO", "Existencias/Coste ventas×365", "<90 días", "24 días", "🟢"],
        ["DPO", "Proveedores/Coste ventas×365", ">60 días", "51 días", "🟡"],
        ["Ciclo de caja (CCC)", "DSO+DIO−DPO", "<60 días", "64 días", "🟡"],
        ["Circulante/Ventas", "(AC−PC)/Ventas", "<15%", "30% (incluye caja)", "🟡"],
        ["Concentración de clientes", "% top clientes", "<40%", "Ninguno >10%", "🟢"],
    ], size=8)
    D.calc("EBITDA FY3/2026 = BO 1.456 + amortización 511 = 1.967 M JPY. Caja neta = caja 9.390 − deuda financiera 4.362 = 5.028 M JPY → DN/EBITDA = −2,6x. "
           "ROIC = BO × (1 − 30,6%) / (FP 19.039 + deuda 4.362 − caja 9.390) = 1.010 / 14.011 = 7,2%. DSO = 11.363/45.579×365 = 91 días.")
    D.h2("Evaluación de existencia de moat")
    D.p("Según Dorsey, los transformadores de commodities casi nunca tienen foso económico: compiten en precio y el retorno sobre capital a lo largo del ciclo converge al coste de capital o por debajo. Nichiwa lo confirma: **ROE medio de 1,5% en seis años** frente a un coste de capital que la propia empresa estima en **6,7-8,0%** (las tasas que usa en sus pruebas de deterioro). **Conclusión preliminar: SIN MOAT (inexistente)**, con ventajas locales menores (logística portuaria y relaciones con clientes). Se desarrolla en la Sección 2.")
    D.src(YUHO[2025] + " nota de deterioro (WACC 6,7%); " + YUHO[2026] + ", p.44 (WACC 8,0%)")

    # 1.6
    D.h1("1.6 Mecánica de Generación de Ingresos")
    D.h2("Modelo de pricing")
    D.bullets([
        "**Revisión trimestral del precio** (abril, julio, octubre, enero), en línea con el calendario de JA Zen-Noh y del resto del sector. El precio se ajusta a la variación esperada del coste de maíz (CBOT), harina de soja, fletes marítimos y el tipo USD/JPY. Revisiones recientes: FY3/2026 bajó tres veces (abr, jul y oct-2025) y subió en ene-2026; en abr-2026 volvió a subir.",
        "**Retraso del traslado + FIFO:** las existencias se valoran por FIFO y el grano se compra con meses de antelación. Cuando el coste sube, el margen se comprime (FY3/2022-23); cuando baja, el precio de venta baja más despacio y el margen se amplía (FY3/2024-26). **El beneficio es un diferencial temporal, no un margen estructural.**",
        "**Fondo de Estabilización (配合飼料価格安定制度):** fabricantes y ganaderos aportan a un fondo que compensa al ganadero cuando el precio del pienso supera la media del último año. Para Nichiwa es un **gasto de venta** variable (1.198 M JPY en FY3/2026) que sube con el tiempo tras periodos de grano caro.",
        "**Cobertura de divisa:** contratos a plazo USD/JPY solo sobre cuentas a pagar en divisa (615 M JPY de nocional a mar-2026); sin especulación. 🟡 La cobertura es pequeña frente a un coste de ventas de 41.448 M JPY: el tipo de cambio se traslada sobre todo vía precio.",
    ])
    D.src(YUHO[2026] + ", p.7-8 (riesgos y MD&A), p.38 (FIFO), p.43 (gastos de venta), p.53 (derivados); " + Q1 + ", p.4")
    D.h2("Estacionalidad")
    D.p("Estacionalidad baja en volumen (el ganado come todo el año), pero con dos efectos: (i) el **4.º trimestre fiscal (ene-mar)** concentra los brotes de **gripe aviar**, que reducen las cabañas de ponedoras y la demanda de pienso avícola; (ii) los **cambios de precio en enero y abril** desplazan márgenes entre trimestres. Ejemplo FY3/2024: beneficio antes de impuestos acumulado de 151 / 563 / 842 / 1.054 M JPY por trimestre, con el 1T débil.")
    D.src(YUHO[2024] + ", p.62 «四半期情報»")
    D.h2("Ciclo de conversión de caja")
    rows = []
    for y in Y:
        dso = rec[y] / sales[y] * 365; dio = inv[y] / cogs[y] * 365; dpo = pay[y] / cogs[y] * 365
        rows.append([f"FY3/{y}", n(dso), n(dio), n(dpo), n(dso + dio - dpo)])
    D.table(["Ejercicio", "DSO (días)", "DIO (días)", "DPO (días)", "CCC (días)"], rows)
    D.calc("DSO = (efectos + derechos de cobro electrónicos + clientes) / ventas × 365; DIO = existencias / coste de ventas × 365; DPO = proveedores / coste de ventas × 365. Datos de los balances consolidados de cada Yuho.")
    D.p("**Lectura:** el ciclo de caja de ~60 días se debe a que **Nichiwa financia a sus clientes ganaderos** (DSO de 85-100 días) mientras paga el grano en ~50 días. Cuando suben los precios del grano, el circulante absorbe caja: en FY3/2022-23 el flujo operativo fue de −1.038 y −1.533 M JPY. Por eso **la caja del balance no es íntegramente «excedente»**: en parte es un colchón para el ciclo de circulante.")
    D.h2("Drivers de ingresos")
    D.table(["Driver", "Efecto en ventas", "Efecto en margen", "Situación oct-2026"], [
        ["Precio maíz/soja (CBOT)", "Directo (+)", "Inverso a corto plazo (retraso)", "🟡 maíz al alza en 1T por fletes, a la baja por buena cosecha EE. UU."],
        ["USD/JPY", "Directo (+ con yen débil)", "Inverso a corto plazo", "🔴 yen débil por diferencial de tipos y Oriente Medio"],
        ["Fletes marítimos / petróleo", "Directo", "Inverso", "🔴 al alza por Oriente Medio"],
        ["Cabaña ganadera (gripe aviar, PPC)", "Volumen", "Mayor riesgo de crédito", "🟡 la gripe aviar sigue reduciendo la oferta de huevo"],
        ["Precios de productos ganaderos", "Solvencia de clientes; segmento ganadería", "Directo en ganadería", "🟢 huevo alto; cerdo y pollo estables"],
        ["Aportación al fondo de estabilización", "—", "Inverso", "🔴 en máximos (≈1.200 M JPY/año)"],
        ["Cuota de mercado y volumen", "Directo", "Apalancamiento operativo", "🟡 sin datos; sector maduro"],
    ], size=8)
    D.src(Q1 + ", p.4; " + YUHO[2026] + ", p.8")

    D.h1("1.7 El mercado en el que opera")
    D.p("💡 / ⚠️ Contexto sectorial (fuentes secundarias; la empresa no publica cuotas): Japón produce unos **23 millones de toneladas anuales de pienso compuesto** y depende de la importación para la mayor parte del maíz y la soja. El mercado está dominado por (i) el sistema cooperativo **JA Zen-Noh** y sus filiales, que marca de facto el precio de referencia trimestral; (ii) grupos comerciales ligados a las grandes tradings: **Feed One** (TSE 2060, ventas de 290.675 M JPY en FY3/2026), **Chubu Shiryo** (TSE 2053, 211.814 M JPY), Marubeni-Nisshin Feed, Nosan (grupo Mitsubishi) y la alianza Itochu Feed/Chubu; y (iii) independientes regionales pequeños como Nichiwa. Con ≈44.000 M JPY de ventas de pienso, **Nichiwa factura ≈15% de lo que factura Feed One**. ⚠️ Su cuota de volumen estimada sería de ≈1,5-2,5% del mercado nacional.")
    D.calc("Si el precio medio del pienso compuesto se sitúa en ≈90.000-100.000 JPY/t (referencia Zen-Noh; varía por especie), 43.669 M JPY de ventas de piensos equivalen a ≈440.000-490.000 t/año, es decir ≈1,9-2,1% de 23 Mt. El componente de compraventa de productos ganaderos dentro del segmento hace que esta cifra esté sobreestimada.")
    D.src("JA Zen-Noh: subida de 3.700 JPY/t para jul-sep 2026 (logi-today.com/966921, sogyotecho.jp, jul-2026); resultados FY3/2026 de Feed One y Chubu Shiryo (TDnet, mayo-2026, vía búsqueda); kantei.go.jp (estructura del sector)")
    D.p("**Tendencias estructurales:** 🔴 menos explotaciones ganaderas, pero más grandes (más poder de negociación de los clientes); 🔴 población japonesa en descenso; 🟡 consolidación del sector (Feed One nace en 2014-15 de la fusión de Kyodo Shiryo y Nippon Haigo Shiryo; alianza Itochu/Chubu de 2015); 🟢 la seguridad alimentaria y el autoabastecimiento son prioridad política, con apoyo del Ministerio de Agricultura a la racionalización de fábricas y silos; 🟢 la presión para reducir metano abre un nicho de piensos funcionales, donde Nichiwa investiga.")

    D.h1("Conclusión de la Sección 1")
    D.box("🟡 **Negocio comprensible, maduro y sin ventaja competitiva.** Nichiwa es un molinero de pienso regional que convierte grano importado en alimento animal con un margen fino y cíclico. Ingresos ≈45.000 M JPY, sin crecimiento real en volumen, 96% del negocio en piensos y una filial ganadera que destruye valor.\n"
          "🟢 Lo que la hace interesante no es el negocio sino el **balance**: 9.390 M JPY de caja (≈150% de la capitalización) y fondos propios de 19.039 M JPY frente a 6.267 M JPY de capitalización.\n"
          "🔴 El beneficio de FY3/2026 (BO de 1.456 M JPY) está en **máximos de ciclo** por el diferencial temporal de precios del grano. La propia dirección prevé una caída del 66% en FY3/2027.", fill="FFF4E5")
    return D.save(out, "Entender_el_Negocio")
