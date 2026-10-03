from helpers import *
from data import *


def build(out):
    D = Doc(4, "Análisis Financiero Detallado")
    D.h1("4.1 Revenue Analysis")
    D.h2("Evolución trimestral / semestral (últimos 8 periodos disponibles)")
    D.p("🔍 Desde abril de 2024 Japón eliminó el informe trimestral obligatorio (四半期報告書) y lo sustituyó por un informe semestral (半期報告書). Nichiwa publica el Kessan Tanshin del 1T, pero los informes anuales de FY3/2025 y FY3/2026 solo dan datos semestrales. La serie combina trimestres y semestres según disponibilidad.")
    D.table(["Periodo", "Ventas", "Var. a/a", "BO", "Bº antes de impuestos", "BN atribuible", "Comentario"], [
        ["3T FY3/2024 (oct-dic 23)", "13.760", "−9,9%", "n.d.", "279", "163", "Bajada de precios en oct"],
        ["4T FY3/2024 (ene-mar 24)", "13.239", "−3,4%", "n.d.", "212", "−16", "Deterioro de 168 en Towa; venta de terreno +395"],
        ["1T FY3/2025 (abr-jun 24)", "≈12.394 💡", "≈−9,1%", "≈180 💡", "n.d.", "n.d.", "Estimado a partir de la variación publicada en 1T FY3/2026"],
        ["2T FY3/2025 (jul-sep 24)", "≈12.122 💡", "≈−1,1%", "n.d.", "n.d.", "n.d.", "1S FY3/2025: ventas 24.516, BAI 545, BN 399"],
        ["2S FY3/2025 (oct-24 a mar-25)", "24.061", "−10,9%", "n.d.", "−46", "−89", "Deterioro de 644 (Miki y Kanoya)"],
        ["1T FY3/2026 (abr-jun 25)", "11.514", "−7,1%", "274", "301", "214", "BO +51,8%"],
        ["2T FY3/2026 (jul-sep 25)", "10.729", "≈−11,5%", "n.d.", "255", "189", "1S FY3/2026: ventas 22.243, BAI 556, BN 403"],
        ["2S FY3/2026 (oct-25 a mar-26)", "23.336", "−3,0%", "n.d.", "251", "−25", "Deterioro de 633 (Unzen y otras granjas)"],
        ["**1T FY3/2027 (abr-jun 26)**", "**11.764**", "**+2,2%**", "**382**", "**413**", "**300**", "**BO +39,1%; subida de precio en abr-26**"],
    ], size=7.5)
    D.src(YUHO[2024] + " p.62 (四半期情報); " + YUHO[2025] + " p.61 (半期情報); " + YUHO[2026] + " p.62; " + Q1 + " p.1 y p.6")
    D.calc("1T FY3/2025: 11.514/(1−0,071) = 12.394 y BO 274/1,518 = 180. 2T = 1S − 1T. 2S = año − 1S. Var. a/a del 2S FY3/2025 = 24.061/(52.887−25.888) − 1 = −10,9%.")

    D.h2("Evolución anual (últimos 6 años)")
    rows = []
    for y in Y:
        rows.append([f"FY3/{y}", n(sales[y]), pct((sales[y] / sales[y - 1] - 1) * 100), n(gp[y]), n(op[y]), n(ordinary[y]), n(ni[y]), n(eps[y], 2)])
    D.table(["Ejercicio", "Ventas", "Δ%", "Bº bruto", "BO", "Bº ordinario", "BN", "BPA (JPY)"], rows)
    D.src("Cuentas de resultados consolidadas de cada Yuho (p.33-35)")
    D.h2("CAGR")
    D.table(["Métrica", "Inicio", "Fin", "Años", "CAGR"], [
        ["Ventas FY3/2017→FY3/2026", "41.055", "45.579", "9", "+1,2%"],
        ["Ventas FY3/2021→FY3/2026", "39.901", "45.579", "5", "+2,7%"],
        ["Ventas FY3/2023→FY3/2026 (desde el pico)", "54.659", "45.579", "3", "−5,9%"],
        ["Bº ordinario FY3/2017→FY3/2026", "806", "1.440", "9", "+6,7%"],
        ["BN FY3/2017→FY3/2026", "324", "378", "9", "+1,7%"],
        ["BPA FY3/2017→FY3/2026", "16,80", "20,92", "9", "+2,5% (ayudado por la recompra de 2022)"],
        ["Valor contable por acción FY3/2017→FY3/2026", "871,31", "1.051,22", "9", "+2,1%"],
    ], size=8.5)
    D.calc("CAGR = (Fin/Inicio)^(1/años) − 1. Ej.: (45.579/41.055)^(1/9) − 1 = 1,17%.")

    D.h1("4.2 Recurrencia de Ingresos")
    D.p("🟡 **Recurrencia «de facto» alta (~95%+), pero sin contratos.** El pienso es un consumible diario: los mismos ganaderos compran cada semana. Sin embargo **no hay contratos plurianuales ni volúmenes garantizados**, y el precio se revisa cada trimestre. La empresa «no produce bajo pedido» (受注生産を行っていない), así que no hay cartera de pedidos.")
    D.table(["Tipo de ingreso", "% estimado", "Naturaleza"], [
        ["Pienso a clientes habituales", "≈90-95% 💡", "Recurrente no contractual; volumen estable, precio variable"],
        ["Compraventa de productos ganaderos de clientes", "n.d. (dentro de piensos)", "Ligada a la financiación del cliente; volátil"],
        ["Productos ganaderos propios (Towa)", "≈4%", "Precio de mercado spot (cerdo, pollo); muy volátil"],
        ["Ingresos no operativos (venta de electricidad solar, alquileres, dividendos)", "<0,5%", "Recurrentes y pequeños (venta de electricidad 49 M JPY, alquileres 22, dividendos 34)"],
    ], size=8.5)
    D.src(YUHO[2026] + ", p.9 (b. 受注実績) y p.33 (営業外収益)")

    D.h1("4.3 Crecimiento Orgánico vs Adquisiciones")
    D.table(["Ejercicio", "Δ Ventas", "Orgánico", "Adquisiciones", "💡 Efecto precio (estimado)", "💡 Efecto volumen/mix"], [
        ["FY3/2022", "+5.005", "100%", "0", "≈+12-15%", "≈−1 a −3%"],
        ["FY3/2023", "+9.753", "100%", "0", "≈+20-25%", "≈−1 a −3%"],
        ["FY3/2024", "−1.772", "100%", "0", "≈−3 a −5%", "≈0 a +2%"],
        ["FY3/2025", "−4.310", "100%", "0", "≈−7 a −9%", "≈0%"],
        ["FY3/2026", "−2.998", "100%", "0", "≈−3 a −5%", "≈−2 a −4%"],
    ], size=8.5)
    D.p("🔍 **Todo el crecimiento es orgánico**; no hay adquisiciones en el periodo. ⚠️ La separación precio/volumen es una estimación propia: la empresa no publica toneladas. La comparamos con el valor de producción a coste (FY3/2026: −8,7% en piensos frente a ventas −6,5%) y con los movimientos del precio Zen-Noh. Que en FY3/2026 las ventas de Nichiwa (−6,5% en piensos) cayeran más que las de Feed One (+1,8%) y Chubu (+0,9%) sugiere **pérdida de volumen**.")
    D.src(YUHO[2026] + ", p.9 (生産実績 飼料事業 37.151, −8,7%)")

    D.h1("4.4 Análisis M&A")
    D.table(["Operación", "Año", "Importe", "Valor creado/destruido"], [
        ["Michinoku Shiryo (asociada, planta de pienso de vacuno)", "2003", "Participación de 31 M JPY al coste", "🟡 Neutral: externaliza producción de vacuno en Tohoku"],
        ["Transferencia interna de granjas a Towa Chikusan", "2018", "Intragrupo", "🔴 Destrucción: el negocio ganadero acumula deterioros de 1.445 M JPY (FY3/2024-26) y préstamos provisionados de 1.604 M JPY"],
        ["Recompra de acciones (ToSTNeT)", "feb-2022", "426 M JPY (1,2 M acciones a 355 JPY)", "🟢 Creación: a 0,37x valor contable; probablemente compradas a un accionista que salía (Unearth International, Seychelles, 4,95% en 2021 y ausente desde 2022 ⚠️)"],
    ], size=8)
    D.src(YUHO[2026] + " p.4 y p.44; " + YUHO[2022] + " p.17; " + YUHO[2021] + " p.17 (accionistas)")
    D.p("🟡 Nichiwa **no hace M&A**. La gran decisión de asignación de capital pendiente es qué hacer con el segmento ganadero, que lleva tres ejercicios consecutivos de deterioros.")

    D.h1("4.5 Backlog y Pipeline")
    D.p("🔴 **Sin backlog.** No se produce bajo pedido. La visibilidad se limita a: (i) el precio ya anunciado para el trimestre en curso; (ii) el coste del grano y las coberturas de divisa (615 M JPY de nocional a mar-2026, cobertura pequeña); (iii) la previsión anual de la empresa: **ventas de 50.000 M JPY (+9,7%), BO de 500 M JPY (−65,7%), Bº ordinario de 500 M JPY (−65,3%) y BN de 300 M JPY (−20,8%)** para FY3/2027, sin cambios tras el 1T.")
    D.src(YUHO[2026] + " p.6 (経営戦略等) y p.53; " + Q1 + " p.1 y p.4")
    D.calc("El 1T FY3/2027 ya ha generado un BO de 382 M JPY, el **76% de la previsión anual** (500). Con el patrón histórico (en FY3/2026 el 1T fue el 19% del BO anual), la previsión parece **muy conservadora** salvo un fuerte deterioro del margen en el 2S. Escenario base propio para FY3/2027: BO de 800-1.100 M JPY (ver Sección 10).")

    D.h1("4.6 Drivers de Crecimiento")
    D.table(["Driver", "Descripción", "Impacto potencial (BO)", "Probabilidad 6-18m"], [
        ["1. Diferencial de precio vs coste del grano", "Si el maíz y la soja se estabilizan y las subidas de abr/jul-2026 se mantienen, el margen bruto puede seguir por encima del 7%", "±500-800 M JPY", "🟡 Media (50%)"],
        ["2. Saneamiento del segmento ganadero", "Tras 1.445 M JPY de deterioros, la base de activos es menor; el 1T muestra un BO de 60 M JPY con cerdo y huevo altos", "+100-250 M JPY y menos deterioros", "🟡 Media (40-50%)"],
        ["3. Reversión de provisiones de clientes", "Recuperación de créditos concursales (1.243 M JPY brutos, provisionados al 100%)", "+50-200 M JPY no recurrente", "🟡 Media-baja (30%)"],
        ["4. Reducción de la aportación al fondo", "Si el fondo de estabilización se recapitaliza, las aportaciones (≈1.200 M JPY) pueden bajar", "+100-400 M JPY", "🔴 Baja a 18 meses (20%)"],
        ["5. Piensos funcionales (bajo metano, sin antibióticos)", "Nicho de valor añadido en línea con la política agrícola", "Marginal", "🔴 Baja (10%)"],
    ], size=8)

    D.h1("Conclusión de la Sección 4")
    D.box("🟡 Ingresos estancados en volumen y totalmente orgánicos, con un crecimiento nominal que depende del precio del grano. El beneficio es muy volátil (pérdida operativa en FY3/2023 y máximo en FY3/2026). 🟢 El 1T FY3/2027 es **fuerte** (BO +39%) y deja la previsión anual de la dirección (BO de 500) con mucho margen de sorpresa positiva.", fill="FFF4E5")
    return D.save(out, "Analisis_Financiero")
