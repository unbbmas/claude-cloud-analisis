from helpers import *
from data import *

YEARS = [
    (2021, "FY3/2021 (abr-2020 a mar-2021) – COVID y primer repunte del grano", [
        ("Entorno según la dirección", "Economía muy débil por el COVID (estado de emergencia en abr-2020 y ene-2021). El maíz estuvo flojo hasta el 2S y luego subió por la demanda china y el retraso de siembras en Sudamérica. El yen pasó de fuerte a débil. Los precios del huevo y del pollo subieron en el 2S por la gripe aviar; el cerdo, firme en el 1S y flojo en el 2S; el vacuno, firme."),
        ("Acciones de precio", "Bajadas en abr y jul-2020; subidas en oct-2020 y ene-2021."),
        ("Resultados explicados", "Ventas de 39.900 (−4,9%); BO de 283 (−46,3%); Bº ordinario de 379 (−42,6%); BN de 139 (−62,6%). Piensos: BO de 767 (−5,9%). Ganadería: BO de 141 (x7,8). OCF de 1.263, con una dotación de insolvencias de 540 M JPY."),
        ("Retos declarados", "Grano en máximos, mercado ganadero afectado por el COVID, competencia «cada vez más intensa». Prioridades: nuevos productos y marcas, eficiencia y prevención de contagios."),
        ("Previsión para el año siguiente", "FY3/2022: ventas de 40.000; BO de 400; Bº ordinario de 500; BN de 300."),
        ("Nuestra valoración", "🔴 La dirección infravaloró el ciclo de inflación del grano que ya había empezado. La dotación de 540 M JPY por clientes es la primera gran señal del riesgo de crédito."),
    ], YUHO[2021] + ", p.7-11"),
    (2022, "FY3/2022 – Inflación del grano y problemas de cobro", [
        ("Entorno según la dirección", "Variantes del COVID, cuellos de botella logísticos, materias primas caras. Maíz al alza por China, el etanol y la invasión de Ucrania; harina de soja también. El yen se debilita por las subidas de tipos en EE. UU. Huevo débil (recuperación de la oferta), pollo débil, cerdo firme desde fin de año y vacuno estable."),
        ("Acciones de precio", "Subidas en abr y jul-2021; bajada en oct-2021; subida en ene-2022."),
        ("Resultados explicados", "Ventas de 44.906 (+12,5%); BO de 117 (−58,5%) «porque surgieron dudas sobre el cobro de algunos clientes» que elevaron el SG&A; Bº ordinario de 216; BN de 116. Piensos: BO de 624 (−18,7%). Ganadería: −2. OCF de −1.038 (clientes +2.333). Recompra de 1,2 M de acciones por 426 M JPY."),
        ("Retos declarados", "Grano caro por Ucrania; COVID; competencia. Prioridades: diversificar el aprovisionamiento, desarrollar productos, reducir costes y prevenir enfermedades."),
        ("Previsión para el año siguiente", "FY3/2023: ventas de 48.000; BO de 300; Bº ordinario de 400; BN de 200."),
        ("Nuestra valoración", "🔴 Segundo año de problemas de crédito (dotación de 407). 🟢 La recompra a 0,37x VC fue la mejor decisión de capital del periodo. 🔴 Previsión de nuevo demasiado optimista."),
    ], YUHO[2022] + ", p.7-11"),
    (2023, "FY3/2023 – Máximos del grano y pérdida operativa", [
        ("Entorno según la dirección", "Normalización post-COVID, tipo de cambio muy volátil e inflación por Ucrania. Maíz disparado por Ucrania, la demanda de etanol y la sequía en Sudamérica; harina de soja muy cara. El yen, muy débil. La gripe aviar dispara el precio del huevo; el pollo y el cerdo, por encima del año anterior; el vacuno, estable."),
        ("Acciones de precio", "Tres subidas (abr, jul y oct-2022)."),
        ("Resultados explicados", "Ventas récord de 54.659 (+21,7%), pero **pérdida operativa de −200** y Bº ordinario de −99 por los costes de materias primas. BN de 157 gracias a una compensación de 331 por la reubicación de instalaciones por obra pública. Piensos: BO de 258 (−58,6%). Ganadería: −123. OCF de −1.533; la caja baja a 5.182."),
        ("Retos declarados", "Ucrania y energía; volatilidad de ventas por la gripe aviar. Prioridades: diversificar materias primas y proveedores, reducir costes y prevenir enfermedades."),
        ("Previsión para el año siguiente", "FY3/2024: ventas de 50.000; BO de 200; Bº ordinario de 300; BN de 200."),
        ("Nuestra valoración", "🟡 Año de estrés máximo superado **sin endeudarse** (la deuda bruta se mantiene en 4.269): prueba de la resistencia del balance. Previsión prudente para el año siguiente."),
    ], YUHO[2023] + ", p.7-11"),
    (2024, "FY3/2024 – Normalización del grano y vuelta a beneficios", [
        ("Entorno según la dirección", "Recuperación por la vuelta del turismo; inflación por el yen débil. Maíz a la baja (buena cosecha en EE. UU. y China floja); soja cara hasta fin de año. Yen débil por la política monetaria del BoJ. El huevo baja al recuperarse la oferta; el pollo y el cerdo, a la baja en el 2S."),
        ("Acciones de precio", "Bajadas en abr, jul y oct-2023; subida en ene-2024."),
        ("Resultados explicados", "Ventas de 52.887 (−3,2%); BO de 905 (desde −200); Bº ordinario de 915; BN de 541 (+244%), con una plusvalía por venta de terreno de 395 frente a un deterioro de 168 en Towa Chikusan y la baja de software (−88). Piensos: BO de 968 (x3,7). Ganadería: −249 (peor año). OCF de 2.052. Dividendo de 8 JPY (incluye 2 JPY del centenario)."),
        ("Retos declarados", "Yen débil, desaceleración china, Oriente Medio y Ucrania. Prioridades: reducir costes, captar y formar talento diverso y prevenir enfermedades."),
        ("Previsión para el año siguiente", "FY3/2025: ventas de 50.000; BO de 400; Bº ordinario de 400; BN de 300."),
        ("Nuestra valoración", "🟢 El ciclo se da la vuelta como era previsible (el margen se amplía con el grano a la baja). 🔴 El segmento ganadero empeora y empieza la cadena de deterioros."),
    ], YUHO[2024] + ", p.7-11"),
    (2025, "FY3/2025 – Primer año del nuevo presidente", [
        ("Entorno según la dirección", "Recuperación moderada por el turismo con consumo débil; incertidumbre por la política comercial de EE. UU. Maíz bajista por la buena cosecha en EE. UU. y luego al alza por la sequía en Sudamérica (desde sep); soja floja. El yen se recupera algo y luego se vuelve volátil por los aranceles. La gripe aviar vuelve a subir el huevo desde octubre; el cerdo, alto en verano (PPC y calor) y luego a la baja."),
        ("Acciones de precio", "Bajadas en abr y oct-2024; subidas en jul-2024 y ene-2025."),
        ("Resultados explicados", "Ventas de 48.577 (−8,1%); BO de 906 (plano); Bº ordinario de 1.143 (+24,9%) con una reversión de provisiones de 186; BN de 310 (−42,7%) por **deterioros de 644** (granjas de Miki y Kanoya). Piensos: BO de 1.087 (+12,3%). Ganadería: −127. OCF de 2.444 (liberación de clientes de 3.476). La caja sube a 9.019."),
        ("Retos declarados", "Tipo de cambio volátil e incertidumbre internacional. Prioridades: **productos para necesidades de clientes cada vez más diversas**, talento y prevención de enfermedades."),
        ("Previsión para el año siguiente", "FY3/2026: ventas de 50.000; BO de 400; Bº ordinario de 400; BN de 300."),
        ("Nuestra valoración", "🟡 La nueva dirección reconoce pérdidas en ganadería (limpieza contable). 🔴 Ningún anuncio de política de capital pese a acumular caja."),
    ], YUHO[2025] + ", p.7-10"),
    (2026, "FY3/2026 – Máximo de margen en piensos", [
        ("Entorno según la dirección", "Recuperación gradual con empleo e ingresos mejores; inflación por el yen débil e incertidumbre internacional. Maíz a la baja (buena siembra en EE. UU. y cosecha récord en Sudamérica), al alza desde agosto por las exportaciones de EE. UU. y otra vez al alza al final por **el encarecimiento del transporte por la tensión en Oriente Medio**. Harina de soja: misma tendencia. Yen débil. Huevo alto todo el año (gripe aviar); pollo por encima del año anterior; cerdo alto en verano y normal en el 2S; vacuno plano."),
        ("Acciones de precio", "Tres bajadas (abr, jul y oct-2025); subida en ene-2026."),
        ("Resultados explicados", "Ventas de 45.579 (−6,2%); **BO de 1.456 (+60,7%)** por un margen bruto mayor (+573); Bº ordinario de 1.440 (+26,0%); BN de 378 (+22,1%) tras **deterioros de 633** (granjas de Unzen y otras). Piensos: BO de 1.485 (+36,6%), «por el efecto de los precios de las materias primas». Ganadería: +5 (desde −127). OCF de 1.154; préstamo a largo plazo de 1.000; préstamos a clientes de 585."),
        ("Retos declarados", "Tipo de cambio impredecible e inestabilidad internacional. Prioridades: reducir costes de producción, talento diverso y prevención de enfermedades."),
        ("Previsión para el año siguiente", "**FY3/2027: ventas de 50.000 (+9,7%); BO de 500 (−65,7%); Bº ordinario de 500 (−65,3%); BN de 300 (−20,8%); dividendo de 6 JPY.**"),
        ("Nuestra valoración", "🟢 El mejor año operativo de la serie, pero conseguido por un diferencial temporal de precios. 🔴 Tercer año de deterioros y fuerte aumento de los préstamos a clientes (+442 en largo plazo). La previsión de FY3/2027 descuenta una fuerte reversión del margen."),
    ], YUHO[2026] + ", p.6-10"),
]


def build(out):
    D = Doc(12, "Análisis del comentario del Management por año y perspectivas")
    D.p("Esta sección resume y analiza críticamente, ejercicio a ejercicio, el **comentario de la dirección** recogido en el apartado «経営者による財政状態、経営成績及びキャッシュ・フローの状況の分析» (MD&A) y «経営方針、経営環境及び対処すべき課題等» de cada Yuho, y el Tanshin del 1T FY3/2027. La traducción del japonés es propia; las cifras están en M JPY.")
    D.h1("Resumen comparativo")
    D.table(["Ejercicio", "Grano / yen", "Precio del pienso", "BO", "BN", "Mensaje clave de la dirección", "Tono"], [
        ["FY3/2021", "↑ en el 2S / yen fuerte→débil", "↓↓↑↑", "283", "139", "COVID y competencia", "🟡"],
        ["FY3/2022", "↑↑ / yen débil", "↑↑↓↑", "117", "116", "Dudas de cobro; Ucrania", "🔴"],
        ["FY3/2023", "↑↑↑ / yen muy débil", "↑↑↑", "−200", "157", "Coste récord; diversificar aprovisionamiento", "🔴"],
        ["FY3/2024", "↓ / yen débil", "↓↓↓↑", "905", "541", "Grano más tranquilo", "🟢"],
        ["FY3/2025", "↓↑ / volátil", "↓↑↓↑", "906", "310", "Deterioros en ganadería; nuevos productos", "🟡"],
        ["FY3/2026", "↓ y luego ↑ (Oriente Medio)", "↓↓↓↑", "1.456", "378", "Margen récord; cautela", "🟢/🟡"],
        ["1T FY3/2027", "↑ fletes / ↓ cosecha; yen débil", "↑ (abr-26)", "382", "300", "Previsión sin cambios", "🟡"],
    ], size=8)
    D.p("**Patrón:** el comentario es **descriptivo y repetitivo**. Explica el resultado por el entorno (grano, yen, gripe aviar) y casi nunca por decisiones propias. Las prioridades («reducir costes», «prevenir enfermedades», «talento») se repiten año tras año sin objetivos cuantificados. No hay estrategia de crecimiento, plan a medio plazo ni objetivos de rentabilidad o de capital.")

    for y, title, items, src in YEARS:
        D.h1(title)
        D.table(["Aspecto", "Contenido (traducción y síntesis)"], [[k, v] for k, v in items], widths=[3.5, 13.5], size=8.5)
        D.src(src)

    D.h1("1T FY3/2027 (abr-jun 2026) – Último comentario de la dirección")
    D.table(["Aspecto", "Contenido"], [
        ["Entorno", "Recuperación moderada con inflación por la inestabilidad internacional y la subida de tipos. Maíz: al alza por los fletes (petróleo) y a la baja por la buena siembra en EE. UU.; harina de soja, igual. **El yen se deprecia por el diferencial de tipos y Oriente Medio.** El huevo, por debajo del año anterior pero alto (la oferta sigue corta por la gripe aviar); el pollo, plano; el cerdo, pico en mayo y luego normal; el vacuno, plano."],
        ["Acción de precio", "**Subida en abril de 2026.**"],
        ["Resultados", "Ventas de 11.764 (+2,2%); BO de 382 (+39,1%); Bº ordinario de 413 (+36,9%); BN de 300 (+40,0%). Piensos: ventas de 11.252 (+2,1%), BO de 343 (+21,7%). Ganadería: ventas de 512 (+4,4%), BO de 60 (+215,5%)."],
        ["Balance", "Activo de 32.010 (+1.193): caja +699, materias primas +345, valores +119. Proveedores +836. Patrimonio neto de 19.314."],
        ["Previsión", "**Sin cambios** respecto a la publicada el 12-may-2026 (ventas de 50.000; BO de 500; BN de 300; dividendo de 6)."],
    ], widths=[3.5, 13.5], size=8.5)
    D.src(Q1 + ", p.1-5")

    D.h1("Perspectivas para el año siguiente (FY3/2027) – Análisis crítico")
    D.table(["Partida", "Previsión de la dirección", "💡 Nuestra estimación base", "Rango", "Comentario"], [
        ["Ventas", "50.000", "≈48.000", "46.000-51.000", "La subida de precios de abr/jul-2026 y el yen débil empujan las ventas; el volumen está estancado"],
        ["BO", "500", "≈900", "500-1.300", "1T: 382. Suponemos compresión en el 2S por el grano/fletes y una aportación al fondo alta"],
        ["Bº ordinario", "500", "≈950", "550-1.350", "Ingresos no operativos netos ≈+50"],
        ["BN", "300", "≈550", "300-850", "Riesgo de nuevos deterioros en ganadería (−100 en el caso base); tipo efectivo ≈35%"],
        ["BPA (JPY)", "16,56", "≈30,4", "16,6-47", ""],
        ["DPA (JPY)", "6", "6", "6-8", "Sin cambio de política salvo un catalizador"],
    ], size=8)
    D.p("**Lectura de la previsión:** 🟡 la dirección prevé un BO de 500, en línea con su sesgo histórico a fijar cifras «redondas» y prudentes (ha superado su previsión de BO por 2-4 veces en FY3/2024-26). Pero esta vez hay **razones fundamentales para la cautela**: (i) el comentario del 1T señala costes de fletes y un yen débil; (ii) el margen bruto de FY3/2026 (9,1%) fue excepcional; (iii) la aportación al fondo sigue cerca de máximos. Nuestra lectura: **FY3/2027 será inferior a FY3/2026, pero bastante mejor que la previsión oficial**. Lo más probable es una revisión al alza con los resultados del 1S (nov-2026), que sería un catalizador de corto plazo.")
    D.p("**Lo que la dirección NO dice (y debería):** política de capital ante un P/B de 0,32x; destino de la caja (≈10.000 M JPY); futuro del segmento ganadero; plan de inversión en plantas de 40-60 años; objetivos de ROE. 🔴 Este silencio es coherente con un gobierno corporativo pasivo y es el principal factor que mantiene el descuento.")

    D.h1("Conclusión de la Sección 12")
    D.box("🟡 El discurso de la dirección es **coherente pero pasivo**: atribuye resultados al entorno y repite prioridades genéricas. La previsión es una herramienta conservadora y poco informativa. 🟢 El 1T FY3/2027 y el historial de previsiones superadas apuntan a **sorpresa positiva** en FY3/2027. 🔴 No hay señales en el discurso de un cambio en la asignación de capital: el inversor no debe contar con él en su escenario base.", fill="FFF4E5")
    return D.save(out, "Comentario_del_Management")
