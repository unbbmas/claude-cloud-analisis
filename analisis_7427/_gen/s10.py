from helpers import *
from data import *


def build(out):
    D = Doc(10, "Valoración y Comparables")
    D.h1("10.1 Múltiplos Actuales")
    D.p("🔍 **Precio actual: 835 JPY** (Investing.com, oct-2026: 835 JPY, −1,76% en la sesión, rango intradía 821-850; rango de 52 semanas 811-958). Referencias previas: 839 JPY el 28-ago-2026 (Matsui/kabuyoho: capitalización de 5.175 M JPY, PER de 6,78x, PBR de 0,42x, yield del 3,58%). Ticker **7427.T** (Yahoo) / **TSE:7427** (TradingView), segmento Standard de la TSE. ⚠️ No se pudo consultar directamente el cierre del 2-oct-2026 por restricciones de red; conviene confirmar el precio antes de operar.")
    D.src("Investing.com y Matsui Securities / kabuyoho vía búsqueda web (3-oct-2026)")
    D.table(["Dato base", "Valor", "Cálculo / fuente"], [
        ["Acciones en circulación", "6.072.421", "6.114.546 emitidas − 42.125 en autocartera (Q1 p.2)"],
        ["**Capitalización**", f"**{n(MCAP)} M JPY** (≈34 M USD)", "835 × 6.072.421"],
        ["Caja − deuda (may-2026, reportado)", "7.567 − 3.625 = 3.942", "Inflado por el cierre en domingo"],
        ["**Caja neta normalizada (💡)**", "**≈1.500**", "Ver Sección 3"],
        ["EV reportado / **EV normalizado**", f"1.128 / **{n(MCAP - 1500)}**", "Capitalización − caja neta"],
        ["BPA FY2/2026 / LTM / previsión FY2/2027", "128,63 / 105,77 / 124,81", "Yuho; TIKR; Tanshin"],
        ["Valor contable por acción (may-2026)", "1.977 JPY", "12.008 / 6.072.421"],
    ], size=8.5)
    D.h2("Tabla de múltiplos")
    evn = MCAP - 1500
    D.table(["Múltiplo", "Actual", "Base", "Historia propia (cierres FY2/2022-26)", "Sector (Arata / Kato Sangyo)", "Valoración"], [
        ["P/E (FY2/2026)", "6,5x", "BPA 128,63", "5,0x – 12,2x", "12,7x / 14,2x", "🟢"],
        ["P/E (LTM)", "7,9x", "BPA 105,77", "", "", "🟢"],
        ["P/E forward (previsión de la empresa)", "6,7x", "BPA 124,81", "", "", "🟢 (poco fiable)"],
        ["P/E forward (💡 base propia)", "≈11,1x", "BPA ≈75", "", "", "🟡"],
        ["P/S", "0,048x", "Ventas 105.811", "≈0,04-0,07x", "0,10x / ≈0,1x", "🟢"],
        ["P/B", "**0,42x**", "VC 1.977", "0,39x – 0,68x", "0,72x / 1,17x", "🟢"],
        ["EV/Ventas (normalizado)", "0,034x", f"EV {n(evn)}", "", "", "🟢"],
        ["EV/EBITDA FY2/2026 (normalizado)", n(evn / 1204, 1) + "x", "EBITDA 1.204", "", "≈5-7x ⚠️", "🟢"],
        ["EV/EBITDA LTM (normalizado)", n(evn / 1006, 1) + "x", "EBITDA LTM ≈1.006", "", "", "🟢"],
        ["EV/FCF normalizado", n(evn / 420, 1) + "x", "FCF norm. 420", "", "", "🟢"],
        ["Precio/NCAV", "0,52x", "NCAV 1.616", "≈0,5-0,8x", "—", "🟢"],
        ["Dividend yield", "3,59%", "DPA 30", "2,7-3,8%", "4,21% / 2,39%", "🟢"],
    ], size=7.5)
    D.calc("Precio a cierre de cada ejercicio = PER publicado × BPA: FY2/2022 583; FY2/2023 813; FY2/2024 1.210; FY2/2025 832; FY2/2026 913 JPY → P/B 0,39 / 0,51 / 0,68 / 0,44 / 0,46.")
    D.src("PER publicados: " + YUHO[2026] + " p.2")

    D.h1("10.2 Empresas Comparables")
    D.table(["Empresa", "Ticker", "Justificación", "Limitaciones"], [
        ["Arata", "TSE Prime 2733", "Mayorista de droguería, hogar y **mascotas**; mismos clientes (home centers, droguerías)", "10x más grande; generalista"],
        ["Kato Sangyo", "TSE Prime 9869", "Mayorista de alimentación de Kansai; margen y modelo comparables", "Alimentación, no mascotas"],
        ["PALTAC", "TSE Prime 8283 (OPA de Medipal, jul-2026)", "Mayorista líder de droguería; **referencia de una operación de compra** (6.650 JPY, prima del 43%, P/B ≈1,33x)", "En proceso de exclusión de bolsa"],
        ["Itochu Shokuhin", "TSE Prime 2692 (compra del resto por Itochu, 2026)", "Mayorista de alimentación con accionista de control: **precedente directo** del escenario Kokubu/Echo", "Excluida"],
        ["Japell", "No cotizada", "Líder de distribución de productos para mascotas (187.000 M JPY)", "Sin datos de mercado"],
    ], size=8)

    D.h1("10.3 TABLA SCREENER COMPARATIVA COMPLETA")
    nd = "n.d."
    D.table(["Métrica", "Echo 7427", "Arata 2733", "Kato Sangyo 9869", "PALTAC 8283", "Itochu Shokuhin 2692", "Media peers", "Posición"], [
        ["DATOS BÁSICOS"],
        ["Ticker", "7427.T", "2733.T", "9869.T", "8283.T", "2692.T", "-", "-"],
        ["Precio (fecha)", "835 (oct-26)", "2.661 (8-sep-26)", "6.690 (4-sep-26)", "6.650 (OPA, jul-26)", "Excluida (2026)", "-", "-"],
        ["Market Cap (M JPY)", n(MCAP), "≈95.900", nd, "≈411.100", nd, "-", "Microcap"],
        ["Enterprise Value (M JPY)", f"{n(evn)} (norm.)", nd, nd, nd, nd, "-", "-"],
        ["VALORACIÓN"],
        ["P/E (TTM)", "7,9x", nd, nd, nd, "11,6x", "11,6x", "🟢 −32%"],
        ["P/E Forward", "6,7x (prev.) / 11,1x 💡", "12,7x", "14,2x", nd, nd, "13,5x", "🟢/🟡"],
        ["P/S", "0,048x", "≈0,10x", nd, nd, nd, "≈0,10x", "🟢"],
        ["P/B", "0,42x", "0,72x", "1,17x", "1,33x (OPA)", nd, "1,07x", "🟢 −61%"],
        ["EV/Revenue", "0,034x", nd, nd, nd, nd, nd, "🟢"],
        ["EV/EBITDA", n(evn / 1204, 1) + "x", nd, nd, nd, nd, "≈5-7x ⚠️", "🟢"],
        ["EV/FCF", n(evn / 420, 1) + "x (norm.)", nd, nd, nd, nd, nd, "🟢"],
        ["DEUDA"],
        ["Debt/Equity", "0,14x (feb-26) / 0,30x (may-26)", nd, nd, nd, nd, nd, "🟢"],
        ["Net Debt/EBITDA", "Caja neta", nd, nd, nd, nd, nd, "🟢"],
        ["Interest Coverage", "24x", nd, nd, nd, nd, nd, "🟢"],
        ["Solvencia (FP/AT)", "31,3%", "35,7%", "36,2%", "56,7%", "42,6%", "42,8%", "🔴 −11,5 pp"],
        ["LIQUIDEZ"],
        ["Current Ratio", "1,39x", nd, nd, nd, nd, nd, "🟡"],
        ["Quick Ratio", "1,26x", nd, nd, nd, nd, nd, "🟢"],
        ["RENTABILIDAD"],
        ["ROE %", "6,6%", "8,4%", "8,1%", "7,5%", "7,3%", "7,8%", "🔴 −1,2 pp"],
        ["ROA %", "2,1%", nd, nd, "4,2%", nd, nd, "🔴"],
        ["ROIC %", "≈9,6%", nd, nd, nd, nd, nd, "🟡"],
        ["MÁRGENES"],
        ["Gross Margin %", "11,1%", nd, nd, nd, nd, nd, "-"],
        ["EBITDA Margin %", "1,1%", nd, nd, nd, nd, nd, "-"],
        ["Operating Margin %", "1,05%", "1,31%", "1,50%", nd, "≈1,2-1,5%", "≈1,4%", "🔴 −0,35 pp"],
        ["Net Margin %", "0,74%", "1,01%", "1,09%", nd, nd, "1,05%", "🔴 −0,3 pp"],
        ["CRECIMIENTO"],
        ["Revenue Growth YoY %", "−0,5%", "+1,9%", nd, nd, nd, "+1,9%", "🔴"],
        ["Operating profit growth YoY %", "−18,4%", "−11,9%", nd, nd, nd, "−11,9%", "🔴"],
        ["EPS Growth YoY %", "−22,7%", "−2,2% (BN)", nd, nd, nd, "−2,2%", "🔴"],
        ["Revenue CAGR 3Y %", "+2,9%", nd, nd, nd, nd, nd, "🟡"],
        ["CASH FLOW"],
        ["Operating CF (M JPY)", "3.980 (inflado)", nd, nd, nd, nd, "-", "-"],
        ["Free Cash Flow (M JPY)", "3.753 / norm. 420", nd, nd, nd, nd, "-", "-"],
        ["FCF Margin %", "0,4% (norm.)", nd, nd, nd, nd, nd, "-"],
        ["FCF Yield %", f"{pct(420 / MCAP * 100)} (norm.)", nd, nd, nd, nd, nd, "🟢"],
        ["CapEx/Revenue %", "0,21%", nd, nd, nd, nd, nd, "🟢"],
        ["SHAREHOLDER RETURNS"],
        ["Dividend Yield %", "3,59%", "4,21%", "2,39%", "0% (OPA)", "1,87%", "≈2,8%", "🟢"],
        ["Payout Ratio %", "23%", "53,5%", nd, nd, nd, nd, "🟡"],
        ["Buyback Yield %", "0%", nd, nd, nd, nd, nd, "🔴"],
        ["Total Yield %", "3,59%", "≥4,2%", nd, nd, nd, nd, "🟡"],
    ], size=7, widths=[3.4, 2.6, 2.0, 2.0, 2.0, 2.0, 1.6, 2.0])
    D.p("*🔍 Echo: DATOS VERIFICADOS (Yuho FY2/2026, Tanshin 1T FY2/2027, TIKR). Peers: datos secundarios (kabuyoho, edinetdb, Monex, kabukiso, búsqueda web del 3-oct-2026).*", size=8.5, italic=True)
    D.calc("Revenue CAGR 3 años = (105.811/96.955)^(1/3) − 1 = 2,9%. Media de solvencia = (35,7 + 36,2 + 56,7 + 42,6)/4 = 42,8%. Media de ROE = (8,4 + 8,1 + 7,5 + 7,3)/4 = 7,8%.")
    D.h2("Interpretación del posicionamiento")
    D.p("Echo cotiza con **el mayor descuento del grupo en todas las métricas de valoración** (P/E −32%, P/B −61%, EV/EBITDA ≈3x). Una parte está justificada: es la más pequeña, la de menor margen y ROE, crece menos y su beneficio va a la baja. Pero el descuento parece **excesivo** para una empresa sin deuda y con dividendo del 3,6%. 🟢 Los precedentes recientes (PALTAC a P/B de 1,33x; Itochu Shokuhin y Mitsubishi Shokuhin comprados por sus accionistas de referencia) muestran el **valor estratégico** de los mayoristas para sus socios.")

    D.h1("10.4 Valoración intrínseca (💡 cálculos propios)")
    D.table(["Método", "Supuestos", "Valor equity (M JPY)", "JPY/acción", "vs 835"], [
        ["1. P/E normalizado 10x", "BN normalizado = (BO 1.000 + 10) × 0,66 = 667 → BPA 110", "6.670", "**1.099**", "+32%"],
        ["2. EV/EBIT normalizado 6x", "6 × 1.000 + caja neta normalizada 1.500", "7.500", "**1.235**", "+48%"],
        ["3. DCF de FCF normalizado", "420 / (8% − 1%) + 1.500", "7.500", "**1.235**", "+48%"],
        ["4. P/B justificado (ROE/Ke)", "ROE normalizado 5,6% / Ke 8% = 0,70x × VC 1.977", "8.405", "**1.384**", "+66%"],
        ["5. NCAV", "AC − pasivo total (may-2026)", "9.811", "**1.616**", "+94%"],
        ["Referencia: operación corporativa", "P/B 1,0x (PALTAC 1,33x)", "12.008", "1.977", "+137%"],
        ["**Rango / mediana (métodos 1-5)**", "", "", "**1.099-1.616 / ≈1.235**", "**+48%**"],
    ], size=7.5)
    D.calc("ROE normalizado = 667/12.008 = 5,6%. Ke del 8% = prima de una microcap japonesa ilíquida. La caja neta normalizada (1.500) excluye el efecto festivo. 🔴 Todos los métodos dependen de un BO normalizado de ≈1.000 M JPY: si el 1T FY2/2027 marca un nuevo nivel (BO ≈300-500), el valor intrínseco bajaría a ≈700-900 JPY.")

    D.h1("10.5 Precio objetivo 6-18 meses y escenarios")
    D.table(["Escenario", "Probabilidad", "Supuestos", "Múltiplo", "Precio", "Retorno (+30 JPY de dividendo)"], [
        ["🔴 Bajista", "35%", "Fuerte revisión de la previsión (BO de FY2/2027 ≈400; BPA ≈43); más clientes perdidos; sin catalizadores", "P/B 0,36x × VC ≈1.970", "**≈710**", "−11%"],
        ["🟡 Base", "45%", "BO de FY2/2027 ≈700 (BPA ≈75; previsión incumplida pero 2S estable); recuperación hacia ≈1.000 en FY2/2028", "P/B 0,47x (media histórica) × VC ≈1.990", "**≈930**", "+15%"],
        ["🟢 Alcista", "20%", "Recuperación del margen u **operación corporativa** (Kokubu/Itochu/consolidador) en un sector en consolidación", "P/B 0,8x", "**≈1.580**", "+93%"],
        ["**Valor esperado ponderado**", "100%", "", "", "**≈983 JPY**", "**≈+21%**"],
    ], size=7.5)
    D.calc("VE = 0,35 × 710 + 0,45 × 930 + 0,20 × 1.580 = 249 + 419 + 316 = 983 JPY; con dividendo: (983 + 30)/835 − 1 = +21%. Base FY2/2027: BO = 1T 8 + resto del año ≈700 (los 3 últimos trimestres de FY2/2026 sumaron 904) → Bº ordinario ≈700, BN ≈460, BPA ≈75.")
    D.box("**Precio objetivo base a 12 meses: ≈930 JPY (+11%; +15% con dividendo). Valor esperado ≈983 JPY (+21% con dividendo). Valor intrínseco central ≈1.235 JPY.**\n"
          "🔴 **Advertencia temporal:** los resultados del 1S (≈9-10 oct-2026) tienen alta probabilidad de traer una **revisión a la baja** que puede llevar el precio a la zona de 700-780 JPY. **El punto de entrada es probablemente mejor después de esa publicación.**\n"
          "🟢 La asimetría a 12-18 meses es favorable: suelo de valor en el NCAV y el P/B históricamente bajo (0,36-0,39x) frente a la opción de una operación corporativa.", fill="E8F5E9")
    return D.save(out, "Valoracion_y_Comparables")
