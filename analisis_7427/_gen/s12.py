from helpers import *
from data import *

PERIODS = [
    ("FY2/2022 – Informe anual (F_2021.pdf) · mar-2021 a feb-2022", [
        ("Entorno descrito", "COVID prolongado; la demanda de mascotas se mantiene, pero suben los costes de materias primas, la competencia en precio y los costes de personal y logística. Por primera vez en 3 años sube el número de gatos y sigue cayendo el de perros."),
        ("Acciones destacadas", "Reorganización comercial en un sistema de «sede central de ventas» (mar-2021); propuestas de «valor total»; Pets Value llega a 268 tiendas gestionadas. Arranca el plan a medio plazo **«I3☆55» con el concepto CED**."),
        ("Resultados explicados", "Ventas de 91.930 (+7,3%); BO de 466 (+47,7%) «gracias a la eficiencia pese al aumento de costes variables»; BN de 288 (+18,7%). OCF de −2.311 por la reversión del calendario de pagos."),
        ("Promesas / perspectivas", "FY2/2023, «2.º año del plan»: lema «**Cumplir lo básico, y luego crecer**»; «mejora sólida del beneficio para **alcanzar los objetivos numéricos**» (no publicados en el Yuho)."),
        ("Tono", "🟡 Prudente y operativo."),
    ], YUHO[2022] + ", p.9-12"),
    ("FY2/2023 – Informe anual (F_2022.pdf) · mar-2022 a feb-2023", [
        ("Entorno descrito", "Normalización post-COVID; yen débil, energía cara, problemas de suministro de productos importados."),
        ("Acciones destacadas", "«Gestión por producto (単品管理)» para mejorar el margen; revisión de los centros logísticos por zonas; lanzamiento del e-learning «Echo Study»; Pets Value con 258 tiendas."),
        ("Resultados explicados", "Ventas de 96.955 (primer año con la nueva norma de ingresos, sin comparación); BO de 858 (+83,9%) «por la mejora del margen bruto gracias a la gestión por producto y la eficiencia»; BN de 590 (+104,9%)."),
        ("Promesas / perspectivas", "FY2/2024, 3.er año: «mayor mejora del beneficio para **alcanzar los objetivos numéricos**»; optimización de la red logística; traspaso del desarrollo de producto de Pets Value a I&I."),
        ("Tono", "🟢 Confiado. 🔍 Promesa cumplida: FY2/2024 fue un año récord."),
    ], YUHO[2023] + ", p.9-12"),
    ("FY2/2024 – Informe anual (F_2023.pdf) · mar-2023 a feb-2024", [
        ("Entorno descrito", "COVID pasa a enfermedad común (clase 5); inflación; menos perros; costes de electricidad y transporte."),
        ("Acciones destacadas", "Vuelve la feria Pet Kingdom (≈40.000 visitantes); marca propia **ShareZ** (primer producto, «Shelf & Tower with Cat»); Pets Value con 254 tiendas."),
        ("Resultados explicados", "**Récord**: ventas de 107.406 (+10,8%) «por la subida del precio unitario por las revisiones de precios y productos de alto valor añadido»; BO de 1.719 (+100,4%) «por la gestión por producto y la reducción de costes logísticos»; BN de 1.213 (+105,6%). Dividendo de 33 JPY (incluye 5 extraordinarios)."),
        ("Promesas / perspectivas", "FY2/2025: «2.º récord consecutivo» con Bº ordinario de **1.780 (+2,5%)**. Traslado de centros logísticos y de la sede; «más inversión en las personas»."),
        ("Tono", "🟢 Triunfal. ⚠️ El récord se atribuye a la gestión, aunque la propia explicación reconoce que el motor fueron las subidas de precio de los fabricantes."),
    ], YUHO[2024] + ", p.10 y p.17-19; Kabutan 5-abr-2024"),
    ("FY2/2025 – Informe anual (F_2024.pdf) · mar-2024 a feb-2025", [
        ("Entorno descrito", "Recuperación moderada; tipos altos en EE. UU. y Europa; China débil; consumo afectado por la inflación."),
        ("Acciones destacadas", "Entregas conjuntas, tabletas para preparar pedidos, AI-OCR; nueva sede en Osaka-Miyahara; venta de la sede de Nishinomiya; Pets Value baja a 215 tiendas «por cambios en la forma de algunos contratos»; spray contra el pelo de mascota."),
        ("Resultados explicados", "Ventas de 106.388 (−0,9%); **BO de 1.359 (−20,9%) explicado como «inversión en infraestructura para el crecimiento continuo de las ventas»** (centros logísticos, personas, traslado de sede); BN de 1.001 (−17,5%) con la plusvalía de 205 de la sede."),
        ("Promesas / perspectivas", "FY2/2026 (último año del plan): **Bº ordinario de 1.459 (+6,6%)**; nuevo lenguaje: «**propuestas basadas en el valor, no en el precio**»; lanzamiento de comida fresca ShareZ."),
        ("Tono", "🟡 Defensivo. 🔴 **Promesa incumplida**: el Bº ordinario previsto de 1.780 se quedó en 1.370 (−23%), y el informe no compara con la previsión."),
    ], YUHO[2025] + ", p.10 y p.17-19; Kabutan 11-abr-2025"),
    ("FY2/2026 – Informe anual (F_2025.pdf) · mar-2025 a feb-2026", [
        ("Entorno descrito", "Humanización de las mascotas y premiumización; consumidor ahorrador; costes de personal, logística y materias primas al alza: el entorno «es cada vez más duro»."),
        ("Acciones destacadas", "«**Selección y concentración**», «revisión radical de la cartera», «operación de bajo coste exhaustiva»: cierre del portal PetPet, traspaso de la escuela; I&I y PetPet pasan al 100%; comida fresca ShareZ «Magokoro Gohan»; colaboración con «Gekiochi-kun»; Rakuten aparece como cliente del 10,5%."),
        ("Resultados explicados", "Ventas de 105.811 (−0,5%) «porque el efecto de las subidas de precio se agotó y por **cambios en las condiciones de algunos clientes**»; margen bruto −258 por la «**competencia en precios del sector**»; BO de 1.110 (−18,4%) atribuido otra vez a la «inversión en infraestructura y personas». Se publican el margen operativo (1,0%) y el ROE (6,6%)."),
        ("Promesas / perspectivas", "Nuevo plan desde FY2/2027: «**Desafío, hacia un mayor crecimiento**» / «Socio que crea el futuro con el cliente»; CED + Connect + Data Science; «**base de análisis de datos abrumadora (圧倒的)**»; IA generativa; integración de Pets Value e I&I. Previsión FY2/2027: ventas de 110.000, BO de 1.150, BN de 758. Nuevo bonus ligado al BO frente a la previsión."),
        ("Tono", "🔴 **Eufemismo**: el Yuho afirma que el plan «terminó **aproximadamente según el plan inicial** (概ね当初の計画どおりの着地)» a pesar de que el Bº ordinario (1.107) quedó un 24% por debajo de la previsión del año (1.459), mantenida aún el 9-ene-2026."),
    ], YUHO[2026] + ", p.10-11 y p.18-22; Kabutan 10-abr-2026; Monex 9-ene-2026"),
    ("1T FY2/2027 – Informe trimestral (Q1_2026.pdf) · mar-may 2026", [
        ("Entorno descrito", "Recuperación gradual; Oriente Medio y volatilidad financiera; los consumidores ahorran; costes en toda la cadena de suministro."),
        ("Acciones destacadas", "Feria Pet Kingdom 2026 «con más visitantes que el año anterior»; Pets Value con 201 tiendas; centralización del desarrollo de producto en I&I; GOODISH (de Fancl) para otoño de 2026; repetición del discurso de «empresa de planificación de categorías n.º 1 del mundo»."),
        ("Resultados explicados", "Ventas de 27.285 (+2,9%) «**las ventas se dan la vuelta** gracias a las propuestas comerciales»; **BO de 8 (−96,1%)** por «aumento continuo de los costes logísticos y **cambios en las condiciones de algunos clientes**»; BN de −6."),
        ("Promesas / perspectivas", "**Previsión sin cambios** (1S: BO de 555; año: 1.150) pese a que el 1T solo cubre el 1,4% del BO del 1S."),
        ("Tono", "🔴 Desconexión entre el lenguaje ambicioso («abrumadora», «n.º 1 del mundo», «nueva etapa de crecimiento») y la realidad de un trimestre en equilibrio."),
    ], Q1 + ", p.1-3"),
]


def build(out):
    D = Doc(12, "Análisis del comentario por management")
    D.p("Analizamos el comentario de la dirección en **todos los informes adjuntos**: los informes anuales F_2021…F_2025 (ejercicios FY2/2022 a FY2/2026: apartados «経営方針・経営環境及び対処すべき課題» y MD&A «経営者による財政状態…の分析») y el informe trimestral Q1_2026 (1T FY2/2027). No hay informes semestrales (H_) adjuntos. Las previsiones de cada año (publicadas en los Tanshin anuales, no adjuntos) se han tomado de Kabutan y Monex (fuentes secundarias). La traducción del japonés es propia; cifras en M JPY.")

    D.h1("12.1 Evolución cronológica del discurso")
    for title, items, src in PERIODS:
        D.h2(title)
        D.table(["Aspecto", "Contenido (síntesis traducida)"], [[k, v] for k, v in items], widths=[3.3, 13.7], size=8)
        D.src(src)

    D.h1("12.2 Lo prometido frente a lo cumplido")
    D.table(["Informe", "Promesa / proyección", "Cumplimiento posterior", "Valoración"], [
        ["FY2/2022", "«Mejora sólida del beneficio para alcanzar los objetivos numéricos» del plan", "BO +84% en FY2/2023", "🟢 Cumplido"],
        ["FY2/2023", "«Mayor mejora del beneficio»; optimización logística", "BO récord de 1.720 en FY2/2024", "🟢 Cumplido (con ayuda de las subidas de precio)"],
        ["FY2/2024", "2.º récord consecutivo: Bº ordinario de 1.780 (+2,5%)", "1.370 (−23%)", "🔴 Incumplido"],
        ["FY2/2025", "Bº ordinario de 1.459 (+6,6%); «valor, no precio»", "1.107 (−24%); margen bruto a la baja por la «competencia en precios»", "🔴 Incumplido y contradicho"],
        ["FY2/2025", "Comida fresca ShareZ", "Lanzada en oct-2025", "🟢 Cumplido"],
        ["Plan «I3☆55» (FY2/2022-26)", "«Objetivos numéricos» (nunca publicados en el Yuho)", "«Aproximadamente según el plan inicial» (FY2/2026)", "🔴 No verificable"],
        ["FY2/2026", "Ventas de 110.000, BO de 1.150 en FY2/2027", "1T: BO de 8; ventas +2,9%", "🔴 En riesgo grave"],
        ["Pets Value", "«Aumentar de forma constante las tiendas gestionadas» (FY2/2022)", "268 → 258 → 254 → 215 → 200 → 201", "🔴 Incumplido"],
    ], size=8)

    D.h1("12.3 Cambios de tono, prioridades y lenguaje")
    D.table(["Periodo", "Lema / foco", "Palabras clave nuevas", "Lectura"], [
        ["FY2/2022-23", "«Cumplir lo básico, y luego crecer»; gestión por producto; coste bajo", "単品管理, ローコストオペレーション", "Foco en eficiencia"],
        ["FY2/2024", "Récord; marca propia ShareZ", "高付加価値, ShareZ", "Euforia"],
        ["FY2/2025", "Inversión para el crecimiento; personas", "「価格ではなく価値」, 人的資本経営", "Justificación de la caída de beneficio"],
        ["FY2/2026", "«Selección y concentración», revisión radical", "選択と集中, 抜本的な見直し, 変革期", "Reestructuración"],
        ["1T FY2/2027", "Nuevo plan: datos, IA, «n.º 1 del mundo»", "Connect, Data Science, 生成AI, 圧倒的", "Ambición creciente con resultados decrecientes"],
    ], size=8)
    D.p("🔴 **Patrón**: cuanto peores son los resultados, más ambicioso y abstracto es el lenguaje (CED → CED + Connect + Data Science; «base de datos abrumadora»; «n.º 1 del mundo»). 🟡 La dirección sí ha pasado de la «inversión para crecer» (FY2/2025) a reconocer problemas concretos («competencia en precios», «cambios de condiciones con clientes») en FY2/2026-27, lo cual es positivo.")

    D.h1("12.4 Guidance y objetivos cuantitativos")
    D.table(["Ejercicio", "Previsión (Bº ordinario)", "Real", "Desviación", "¿Revisión previa?"], [
        ["FY2/2024", "Crecimiento «más moderado» (n.d.)", "1.745", "Muy positiva", "n.d."],
        ["FY2/2025", "1.780", "1.370", "−23%", "No localizada"],
        ["FY2/2026", "1.459", "1.107", "−24%", "No (mantenida el 9-ene-2026)"],
        ["FY2/2027", "1.147 (1S: 554)", "1T: 7", "1T = 1,3% del 1S", "Mantenida el 10-jul-2026"],
    ], size=8.5)
    D.src("Kabutan (5-abr-2024; 11-abr-2025; 10-abr-2026); Monex (9-ene-2026); " + Q1)
    D.p("🔴 **Credibilidad baja**: dos fallos consecutivos de ≈−24%, ambos **sin revisión anticipada** (por debajo del umbral del 30% que obliga a revisar), y un tercero en ciernes. 🔴 El nuevo bonus de los consejeros se calcula **frente a esa misma previsión**, lo que puede sesgar las previsiones futuras a la baja.")

    D.h1("12.5 Red flags del comentario")
    D.bullets([
        "🔴 **Eufemismo**: «el plan terminó aproximadamente según lo previsto» (FY2/2026) tras dos incumplimientos del ≈24%.",
        "🔴 **Explicación reciclada**: la caída del BO de FY2/2025 y de FY2/2026 se atribuye en ambos casos a «inversión en infraestructura y personas para el crecimiento», sin cuantificar esa inversión.",
        "🔴 **Explicación que cambia**: FY2/2025 → inversión; FY2/2026 → «agotamiento del efecto precio», «cambios con clientes» y «competencia en precios»; 1T FY2/2027 → «logística» y «cambios con clientes». La causa estructural (presión de clientes y erosión del margen) aparece tarde.",
        "🔴 **Métricas que nunca aparecen**: los objetivos numéricos del plan «I3☆55» (citados pero no publicados en el Yuho); volúmenes; margen por canal.",
        "🟡 **Métricas que aparecen**: cliente >10% (Rakuten) en FY2/2026; margen operativo y ROE en el MD&A desde FY2/2026 (positivo).",
        "🟡 **Métrica en declive sostenido**: tiendas gestionadas por Pets Value, explicado como «cambios en la forma de algunos contratos».",
        "🟢 **Buena práctica**: explica con transparencia el efecto de los cierres en festivo sobre clientes, proveedores y OCF.",
    ])

    D.h1("12.6 Perspectivas para el año siguiente (FY2/2027): análisis crítico")
    D.table(["Partida", "Previsión de la dirección", "💡 Estimación base propia", "Rango", "Comentario"], [
        ["Ventas", "110.000 (+4,0%)", "≈108.000 (+2%)", "106.000-110.000", "1T +2,9%; Rakuten y precios"],
        ["BO", "1.150 (+3,6%)", "≈700", "400-1.000", "1T: 8. El resto del año a ritmo de FY2/2026 (904) menos presión"],
        ["Bº ordinario", "1.147", "≈700", "400-1.000", ""],
        ["BN", "758 (−2,6%)", "≈460", "260-650", "Incluye la venta de valores (+15 en el 1T)"],
        ["BPA (JPY)", "124,81", "≈75", "43-107", ""],
        ["DPA (JPY)", "30", "30", "30", "Payout ≈40% en el caso base"],
    ], size=8)

    D.h1("12.7 Valoración final de la calidad y transparencia del comentario")
    D.box("**Calificación: 🔴/🟡 BAJA-MEDIA (4/10).**\n"
          "🟢 Fortalezas: informes completos y puntuales; explicación honesta del efecto calendario; reconocimiento reciente de la competencia en precios y de los cambios con clientes; publicación del margen y del ROE.\n"
          "🔴 Debilidades: previsiones poco fiables y no revisadas a tiempo; eufemismos («según el plan»); objetivos del plan no publicados; lenguaje cada vez más grandilocuente frente a resultados en caída; sin presentaciones ni conferencias para inversores.\n"
          "**Implicación para la inversión:** no hay que tomar la previsión de la dirección como escenario base. Conviene descontar ≈30-40% del BO previsto y esperar a ver datos reales (1S, oct-2026) antes de aumentar la posición.", fill="FDECEA")
    return D.save(out, "Comentario_del_Management")
