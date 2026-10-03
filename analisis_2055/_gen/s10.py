from helpers import *
from data import *


def build(out):
    D = Doc(10, "Valoración y Comparables")
    D.h1("10.1 Múltiplos Actuales")
    D.p("🔍 **Precio actual: 346 JPY** (dato del encargo; contrastado con fuentes de mercado: 345,0 JPY al cierre del 25-sep-2026, con PER 20,89x, PBR 0,37x, yield 1,73% y capitalización de 72.000 M JPY según el cálculo del portal sobre las acciones emitidas). Ticker: **2055.T** (Yahoo Finance) / **TSE:2055** (TradingView). Segmento Standard de la TSE.")
    D.src("Monex Scouter / Matsui / kabuyoho (búsqueda web del 3-oct-2026). Nota: los portales calculan PER y PBR con la previsión de BPA (16,56) y con el número de acciones emitidas; aquí usamos las acciones en circulación (18.111.793)")
    D.table(["Dato base", "Valor", "Cálculo / fuente"], [
        ["Acciones en circulación", "18.111.793", "20.830.825 emitidas − 2.719.032 en autocartera (Q1 p.2)"],
        ["**Capitalización**", "**6.267 M JPY** (≈42 M USD a 150 JPY/USD)", "346 × 18.111.793"],
        ["Deuda financiera (30-jun-26)", "≈4.312", "3.379 CP + 733 LP + ≈199 de vencimiento corriente ⚠️"],
        ["Caja (30-jun-26)", "10.089", "Q1 p.5"],
        ["**EV (30-jun-26)**", "**≈490 M JPY**", "6.267 + 4.312 − 10.089"],
        ["EV (31-mar-26, coherente con las cifras anuales)", "1.239 M JPY", "6.267 + 4.362 − 9.390"],
        ["BN de los últimos 12 meses (TTM)", "464 M JPY → BPA 25,6 JPY", "378 − 214 (1T FY26) + 300 (1T FY27)"],
        ["BO TTM", "1.564 M JPY", "1.456 − 274 + 382"],
        ["Valor contable por acción (30-jun-26)", "1.066 JPY", "19.314 / 18,11 M"],
    ], size=8.5)
    D.h2("Tabla de múltiplos (vs historia propia y sector)")
    D.table(["Múltiplo", "Actual", "Base de cálculo", "Historia propia (cierres FY3/2021-26)", "Sector (Feed One / Chubu)", "Valoración"], [
        ["P/E (TTM)", "13,5x", "BPA TTM 25,6", "10,4x – 49,4x (mediana ≈22x)", "≈9,0x / ≈10,0x", "🟡"],
        ["P/E (FY3/2026)", "16,5x", "BPA 20,92", "", "", "🟡"],
        ["P/E forward (previsión de la empresa)", "20,9x", "BPA previsto 16,56", "", "8,7x / ≈8,1x", "🔴"],
        ["P/E forward (💡 estimación propia)", "11,4x", "BPA base ≈30,4", "", "", "🟡"],
        ["P/S", "0,14x", "Ventas TTM 45.829", "0,08-0,17x", "0,20x / ≈0,26x", "🟢"],
        ["P/B", "**0,32x**", "VC 1.066", "0,25x – 0,39x", "0,91x / ≈0,77x", "🟢"],
        ["EV/Revenue", "0,01-0,03x", "EV 490-1.239", "—", "n.d.", "🟢"],
        ["EV/EBITDA (FY3/2026)", "0,63x", "EBITDA 1.967", "0,3x – 8,1x", "n.d. (≈4-6x ⚠️)", "🟢"],
        ["EV/EBITDA normalizado", "1,1x", "EBITDA normalizado 1.150", "", "", "🟢"],
        ["EV/FCF (FY3/2026)", "1,6x", "FCF 773", "", "", "🟢"],
        ["EV/FCF normalizado", "3,8x", "FCF normalizado 330", "", "", "🟢"],
        ["Precio/NCAV", "0,50x", "NCAV 687,5", "≈0,4-0,6x", "—", "🟢"],
    ], size=7.5)
    D.calc("Precios al cierre de cada ejercicio = PER publicado × BPA: FY3/2021 356; FY3/2022 295; FY3/2023 238; FY3/2024 311; FY3/2025 301; FY3/2026 384 JPY → P/B 0,39 / 0,31 / 0,25 / 0,31 / 0,30 / 0,37. EV/EBITDA histórico = (cap. + deuda − caja) / (BO + D&A).")
    D.src("PER publicados: " + YUHO[2021] + " p.2 y " + YUHO[2026] + " p.2")

    D.h1("10.2 Empresas Comparables")
    D.table(["Empresa", "Ticker", "Justificación", "Limitaciones"], [
        ["Feed One", "TSE Prime 2060", "N.º 1 privado en pienso compuesto (fusión de Kyodo Shiryo y Nippon Haigo); mismo negocio y mismos riesgos (grano, yen, fondo)", "6,4x más grande; incluye negocio de alimentación"],
        ["Chubu Shiryo", "TSE Prime 2053", "Fabricante de pienso de Nagoya, aliado de Itochu; modelo muy similar y balance sólido (66,8% de solvencia)", "4,6x más grande"],
        ["Higashimaru", "Fukuoka 2058", "Fabricante pequeño de pienso para acuicultura y alimentación en Kagoshima (misma región que una planta de Nichiwa); tamaño comparable", "Más acuícola; bolsa regional"],
        ["Axyz", "TSE Standard 1381", "Integradora avícola de Kagoshima (pienso + broiler): proxy del segmento ganadero y de los clientes de Nichiwa", "Modelo integrado; ejercicio a junio"],
    ], size=8)
    D.p("⚠️ Nota de verificación: los datos de los peers proceden de búsquedas web (TDnet, portales de Monex, Matsui, kabuyoho, edinetdb) del 3-oct-2026. No se han podido descargar los documentos originales por restricciones de red, así que se tratan como **datos secundarios** y algunos se marcan n.d. o con ⚠️ cuando las fuentes discrepan.")

    D.h1("10.3 TABLA SCREENER COMPARATIVA COMPLETA")
    nd = "n.d."
    D.table(["Métrica", "Nichiwa 2055", "Feed One 2060", "Chubu 2053", "Higashimaru 2058", "Axyz 1381", "Media peers", "Posición"], [
        ["DATOS BÁSICOS"],
        ["Ticker", "2055.T", "2060.T", "2053.T", "2058 (Fukuoka)", "1381.T", "-", "-"],
        ["Precio (fecha)", "346 (2-oct-26)", "1.489 (25-sep-26)", "≈2.010 (sep-26) ⚠️", "1.010 (24-sep-26)", nd, "-", "-"],
        ["Market Cap (M JPY)", "6.267", "≈57.300", "≈55.700 ⚠️", nd, nd, "≈56.500", "−89%"],
        ["Enterprise Value (M JPY)", "490-1.239", nd, nd, nd, nd, nd, "-"],
        ["VALORACIÓN"],
        ["P/E (TTM / FY3/26)", "13,5x / 16,5x", "≈9,0x", "≈10,0x", nd, nd, "≈9,5x", "🔴 más caro por beneficio"],
        ["P/E Forward", "20,9x (prev.) / 11,4x 💡", "8,7x", "≈8,1x", nd, nd, "≈8,4x", "🔴/🟡"],
        ["P/S", "0,14x", "0,20x", "≈0,26x", nd, nd, "≈0,23x", "🟢"],
        ["P/B", "0,32x", "0,91x", "≈0,77x", "0,89x", nd, "≈0,86x", "🟢 −63%"],
        ["EV/Revenue", "0,01-0,03x", nd, nd, nd, nd, nd, "🟢"],
        ["EV/EBITDA", "0,6x", nd, nd, nd, nd, "≈4-6x ⚠️", "🟢"],
        ["EV/FCF", "1,6x (3,8x norm.)", nd, nd, nd, nd, nd, "🟢"],
        ["DEUDA"],
        ["Debt/Equity", "0,23x", nd, nd, nd, nd, nd, "🟢"],
        ["Net Debt/EBITDA", "−2,6x (caja neta)", nd, nd, nd, nd, nd, "🟢"],
        ["Interest Coverage (EBITDA/int.)", "27,7x", nd, nd, nd, nd, nd, "🟢"],
        ["Solvencia (FP/AT)", "61,8%", "46,4%", "66,8%", nd, nd, "56,6%", "🟢"],
        ["LIQUIDEZ"],
        ["Current Ratio", "2,33x", nd, nd, nd, nd, nd, "🟢"],
        ["Quick Ratio", "2,06x", nd, nd, nd, nd, nd, "🟢"],
        ["RENTABILIDAD"],
        ["ROE %", "2,0%", "11,0%", "7,9%", nd, nd, "9,5%", "🔴 −7,5 pp"],
        ["ROA %", "1,25%", "≈5% ⚠️", "5,1%", nd, nd, "≈5,1%", "🔴 −3,8 pp"],
        ["ROIC %", "7,2%", nd, nd, nd, nd, nd, "🟡"],
        ["MÁRGENES"],
        ["Gross Margin %", "9,1%", nd, nd, nd, nd, nd, "🟡"],
        ["EBITDA Margin %", "4,3%", nd, nd, nd, nd, nd, "🟡"],
        ["Operating Margin %", "3,2%", "2,8%", "3,1%", "3,3%", nd, "3,1%", "🟡 +0,1 pp (pico)"],
        ["Net Margin %", "0,8%", "2,2%", "2,6%", nd, nd, "2,4%", "🔴 −1,6 pp"],
        ["CRECIMIENTO"],
        ["Revenue Growth YoY %", "−6,2%", "+1,8%", "+0,9%", "−(decrecimiento) ⚠️", nd, "+1,4%", "🔴 −7,6 pp"],
        ["Operating profit (≈EBITDA) Growth YoY %", "+60,7% (BO)", "+27,6% (BO)", "+53,8% (BO)", nd, "+88,8% (Bº ord.)", "+40,7% (FO/Chubu)", "🟢"],
        ["EPS Growth YoY %", "+22,2%", "+18,4% (BN)", "+58,5% (BN)", nd, nd, "+38,5%", "🔴"],
        ["Revenue CAGR 3Y %", "−5,9%", nd, nd, nd, nd, nd, "🔴"],
        ["CASH FLOW"],
        ["Operating CF (M JPY)", "1.154", nd, "7.193", nd, nd, "-", "-"],
        ["Free Cash Flow (M JPY)", "773 (norm. 330)", nd, nd, nd, nd, "-", "-"],
        ["FCF Margin %", "1,7% (norm. 0,7%)", nd, nd, nd, nd, nd, "🟡"],
        ["FCF Yield %", "12,3% (norm. 5,3%)", nd, nd, nd, nd, nd, "🟢"],
        ["CapEx/Revenue %", "0,8%", nd, nd, nd, nd, nd, "🔴 infrainversión"],
        ["SHAREHOLDER RETURNS"],
        ["Dividend Yield %", "1,73%", "3,49%", "0,9-4,0% ⚠️ conflicto", "1,19%", nd, "≈2,3%", "🔴"],
        ["Payout Ratio %", "29% (consolidado)", "≈31% 💡", nd, nd, nd, nd, "🟡"],
        ["Buyback Yield %", "0%", nd, nd, nd, nd, nd, "🔴"],
        ["Total Yield %", "1,73%", "≥3,5%", nd, "1,19%", nd, nd, "🔴"],
    ], size=7, widths=[3.6, 2.4, 2.0, 2.0, 2.0, 1.6, 1.7, 2.3])
    D.p("*🔍 Nichiwa: DATOS VERIFICADOS (Yuho FY3/2026 y Tanshin 1T FY3/2027). Peers: datos secundarios.*", size=8.5, italic=True)
    D.src("Feed One: precio 1.489 (25-sep-2026), PBR 0,91, yield 3,49% (DPA previsto 52), ROE 10,97%, solvencia 46,4% (Monex Scouter); resultados FY3/2026 y previsión FY3/2027 (TDnet). Chubu Shiryo: PER 7,97, PBR 0,73 y yield previsto 4,01% (10-ago-2026, kabuyoho); cierre ≈2.010 JPY (sep-2026, traders.co.jp); FY3/2026 y FY3/2027E (TDnet/edinetdb); edinetdb indica DPA de 18 JPY ⚠️ en conflicto. Higashimaru: 1.010 JPY, PBR 0,89, DPA 12 (kabuyoho, 24-sep-2026). Axyz: Bº ordinario FY6/2026 4.098 M JPY (+88,8%) (Monex). Payout de Feed One ≈ 52 × 38,5 M acc. / 6.500 previsto ≈ 31% ⚠️")
    D.h2("Interpretación del posicionamiento")
    D.p("Nichiwa es **la más barata del grupo sobre activos** (P/B de 0,32x frente a ≈0,86x de media; EV casi nulo), pero **no sobre beneficios**: su P/E TTM (13,5x) es mayor que el de Feed One y Chubu (9-10x), porque su ROE es 4-5 veces menor. La relación P/B/ROE muestra que el mercado aplica a los grandes un múltiplo de ≈0,08-0,10x P/B por punto de ROE y a Nichiwa ≈0,16x: **el descuento sobre el VC está explicado en gran parte por la baja rentabilidad**, y el valor «escondido» está en la caja, no en el negocio. 🟢 Fortalezas relativas: balance, liquidez y caja neta. 🔴 Debilidades: ROE, crecimiento, retribución al accionista y tamaño.")

    D.h1("10.4 Valoración intrínseca (💡 cálculos propios)")
    D.table(["Método", "Supuestos clave", "Valor equity (M JPY)", "Valor por acción (JPY)", "vs 346"], [
        ["1. NNWC (Graham, suelo de liquidación)", "Caja 100% + clientes 75% + existencias 50% − pasivo total (mar-26)", "7.526", "**416**", "+20%"],
        ["2. NCAV", "AC − pasivo total (jun-26)", "12.451", "**688**", "+99%"],
        ["3. P/B justificado (ROE/Ke)", "ROE de mitad de ciclo 3,0% / Ke 7,5% = 0,40x × VC 1.066", "7.725", "**426**", "+23%"],
        ["4. Earnings Power Value (EPV)", "NOPAT normalizado 416 / WACC 8% = 5.200 + caja excedente (5.028 − 2.000 de colchón de circulante) + valores netos de impuestos 1.459", "9.687", "**535**", "+55%"],
        ["5. EV/EBITDA normalizado 3,0x", "1.150 × 3,0 = 3.450 + caja neta 5.028 + valores netos 1.459", "9.937", "**549**", "+59%"],
        ["6. DCF de FCF normalizado (crecimiento 0%)", "330 / 8% = 4.125 + caja excedente 3.028 + valores netos 1.459", "8.612", "**475**", "+37%"],
        ["**Rango / mediana**", "", "", "**416-688 / mediana ≈505**", "**+46% (mediana)**"],
    ], size=7.5)
    D.calc("Valores netos de impuestos = 1.908 − 30,6% × plusvalía latente de 1.466 = 1.459 M JPY. WACC del 8,0% = tasa usada por la empresa en su deterioro de FY3/2026 (p.44). Colchón de circulante de 2.000 M JPY ≈ caja consumida en el peor año del ciclo. Ke 7,5% = prima de riesgo de una microcap japonesa ilíquida.")

    D.h1("10.5 Precio objetivo 6-18 meses y escenarios")
    D.table(["Escenario", "Probabilidad", "Supuestos FY3/2027-28", "Múltiplo", "Precio objetivo", "Retorno (+ dividendo 6 JPY)"], [
        ["🔴 Bajista", "25%", "BO cae al nivel de la previsión (500); BN ≈300 (BPA 16,6); nuevos deterioros en ganadería; sin cambios de capital", "P/B 0,28x × VC ≈1.080", "**≈300 JPY**", "−12%"],
        ["🟡 Base", "55%", "BO ≈900 (1T 382 + 2S con compresión); BN ≈550 (BPA ≈30); revisión al alza de la previsión en nov-2026; dividendo plano", "P/B 0,40x × VC ≈1.090", "**≈440 JPY**", "+29%"],
        ["🟢 Alcista", "20%", "BO ≥1.200; anuncio de plan de P/B, recompras/dividendo extraordinario, o una OPA/integración (p. ej. un accionista estratégico)", "P/B 0,55-0,65x", "**≈620 JPY**", "+81%"],
        ["**Valor esperado ponderado**", "100%", "", "", "**≈441 JPY**", "**≈+29%**"],
    ], size=7.5)
    D.calc("VE = 0,25×300 + 0,55×440 + 0,20×620 = 75 + 242 + 124 = 441 JPY. VC por acción estimado a mar-2027 (base) = 1.066 + (550 − 109)/18,11 ≈ 1.090 JPY. BPA base = 550/18,11 = 30,4 JPY. Escenario base de BO: 1T 382 + 2T ≈250 + 2S ≈270 = ≈900.")
    D.box("**Precio objetivo base a 12 meses: 440 JPY (+27%; +29% con dividendo). Rango 300-620 JPY. Valor intrínseco central ≈505 JPY.**\n"
          "🟢 La relación asimétrica es favorable: el riesgo bajista está limitado por el NNWC (≈416) y la caja neta (≈319 JPY/acción a jun-2026), mientras que el alcista depende de catalizadores de capital.\n"
          "🔴 El precio objetivo base exige que el P/B suba de 0,32x a 0,40x, algo que no ha pasado de forma sostenida en seis años sin catalizador.", fill="E8F5E9")
    D.calc("Caja neta por acción a jun-2026 = 5.777 / 18,11 M = 319 JPY → el mercado valora el negocio operativo, las fábricas, los terrenos y los valores en solo ≈27 JPY/acción (≈490 M JPY).")
    return D.save(out, "Valoracion_y_Comparables")
