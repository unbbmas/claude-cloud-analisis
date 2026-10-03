from helpers import *
from data import *


def build(out):
    D = Doc(11, "Factores a Monitorear")
    D.h1("11.1 KPIs Críticos")
    D.table(["KPI", "Último dato", "Umbral 🟢", "Umbral 🔴 (alerta)", "Fuente / frecuencia"], [
        ["Margen bruto trimestral", "8,98% (1T FY3/2027)", ">8%", "<6,5%", "Tanshin trimestral"],
        ["BO del segmento piensos", "343 M JPY (1T)", ">250 / trimestre", "<100 / trimestre", "Tanshin (nota de segmentos)"],
        ["BO del segmento ganadero", "60 M JPY (1T)", "≥0", "<−50 / trimestre", "Tanshin"],
        ["Previsión anual de BO", "500 M JPY", "Revisión al alza ≥800", "Revisión a la baja <400", "TDnet (業績予想の修正)"],
        ["Caja neta", "≈5.777 M JPY (jun-26)", ">5.000", "<3.000", "Balance trimestral"],
        ["Clientes + existencias − proveedores", "≈7.900 M JPY (jun-26 💡)", "<9.000", ">10.500 (absorción de caja)", "Balance"],
        ["Créditos concursales (bruto)", "1.293 M JPY (jun-26)", "Estable/bajando", ">1.700", "Balance (破産更生債権等)"],
        ["Aportación al fondo de estabilización", "1.198 M JPY/año", "<900", ">1.400", "Yuho (gastos de venta)"],
        ["USD/JPY", "Yen débil (Tanshin 1T) ⚠️ verificar el tipo diario", "<140", ">160", "Mercado diario"],
        ["Maíz CBOT (diciembre)", "Bajista por la cosecha de EE. UU. (jul-26)", "<4,5 USD/bu", ">5,5 USD/bu", "CBOT diario"],
        ["Precio de referencia Zen-Noh", "+3.700 JPY/t (jul-sep 26)", "Subidas trasladadas", "Bajadas con coste al alza", "Trimestral"],
        ["P/B de la acción", "0,32x", ">0,40x (objetivo base)", "<0,28x", "Diario"],
        ["Participación de Jumonji Chicken", "8,70% (mar-26)", "Aumenta / informe de participación significativa", "Vende", "EDINET (大量保有報告書)"],
    ], size=7.5)
    D.src(Q1 + "; " + YUHO[2026])
    D.calc("Circulante operativo a jun-2026 = clientes 11.360 + existencias 3.168 − proveedores 6.659 = 7.869 M JPY.")

    D.h1("11.2 Catalizadores Positivos (12 meses)")
    D.table(["#", "Catalizador", "Fecha estimada", "Probabilidad", "Impacto en precio"], [
        ["1", "**Revisión al alza de la previsión de FY3/2027** (el 1T ya cubre el 76% del BO y el 100% del BN previstos)", "Resultados del 1S: ≈mediados de nov-2026", "🟢 Alta (60-70%)", "+5-15%"],
        ["2", "**Plan de mejora de P/B / política de capital** (petición de la TSE): recompra, amortización de autocartera, mayor payout", "Resultados anuales may-2027 / junta jun-2027", "🟡 Media-baja (20-25%)", "+20-50%"],
        ["3", "**Operación corporativa**: aumento de Jumonji Chicken por encima del 10%, OPA o integración con un accionista estratégico (Toyota Tsusho, Cargill) o un consolidador del sector", "Indeterminado", "🔴 Baja (5-10%) ⚠️", "+60-120%"],
        ["4", "**Entrada de un inversor activista** (tendencia en microcaps japonesas con P/B<0,5 y caja neta)", "Indeterminado", "🟡 Baja-media (10-15%)", "+15-40%"],
        ["5", "**Saneamiento definitivo del segmento ganadero** (venta o cierre de granjas, fin de deterioros)", "FY3/2027-28", "🟡 Media (30%)", "+5-10%"],
    ], size=8)

    D.h1("11.3 Eventos Invalidantes (kill switches)")
    D.table(["#", "Evento", "Por qué invalida la tesis", "Acción"], [
        ["1", "**Caja neta < 3.000 M JPY** sin un uso para el accionista (por shock de circulante o inversión no rentable)", "Elimina el margen de seguridad (precio < NNWC)", "Vender / reducir"],
        ["2", "**Adquisición o gran CapEx con caja** fuera del negocio principal o en ganadería", "Riesgo de destrucción del activo principal de la tesis", "Vender"],
        ["3", "**Pérdida operativa en dos trimestres consecutivos** del segmento piensos", "Indica un deterioro competitivo, no solo cíclico", "Revisar / reducir"],
        ["4", "**Dotaciones por insolvencias >500 M JPY** en un año o salvedad del auditor", "El riesgo de crédito oculto sería mayor de lo provisionado", "Vender"],
        ["5", "**Ningún cambio de política de capital tras la junta de jun-2027** y P/B <0,35x", "Confirma la trampa de valor en el horizonte de 18 meses", "Salir al cumplir el horizonte"],
    ], size=8)

    D.h1("Calendario de eventos")
    D.table(["Fecha (estimada)", "Evento"], [
        ["≈12-14 nov-2026", "Resultados del 1S FY3/2027 (半期報告書 + Tanshin); posible revisión de la previsión"],
        ["Invierno 2026-27", "Temporada de gripe aviar (riesgo de clientes)"],
        ["Mensual", "Revisión trimestral del precio del pienso Zen-Noh (oct-dic; ene-mar)"],
        ["≈12 feb-2027", "Resultados del 3T FY3/2027"],
        ["≈12 may-2027", "Resultados anuales FY3/2027 + dividendo + previsión FY3/2028"],
        ["≈25 jun-2027", "Junta General / Yuho FY3/2027"],
    ], size=8.5)
    D.src("Calendario estimado a partir de las fechas históricas de publicación (Tanshin 1T 12-ago-2026; Yuho 25-jun-2026; acuerdo de dividendo 12-may-2026)")

    D.h1("CONCLUSIÓN FINAL Y RECOMENDACIÓN")
    D.box("**¿Es Nichiwa Sangyo una buena inversión a 6-18 meses al precio de 346 JPY?**\n\n"
          "**Respuesta: SÍ, con matices → 🟢 COMPRA ESPECULATIVA «VALUE» / ACUMULAR con tamaño de posición pequeño (≤2-3% de la cartera), precio objetivo base de 440 JPY (+27%) y valor intrínseco central de ≈505 JPY.**\n\n"
          "**Por qué sí:**\n"
          "• Cotiza por debajo del capital circulante neto de Graham (NNWC ≈416 JPY) y a la mitad de su NCAV (≈688 JPY). La caja neta (≈319 JPY/acción) cubre el 92% del precio.\n"
          "• EV ≈490-1.240 M JPY frente a un EBITDA normalizado de ≈1.150 M JPY y un FCF normalizado de ≈330 M JPY (FCF yield sobre EV del ≈27%).\n"
          "• El 1T FY3/2027 es fuerte (BO +39%) y deja la previsión anual muy superable, lo que hace probable una revisión al alza en noviembre de 2026.\n"
          "• Riesgo de pérdida permanente bajo; el escenario bajista razonable es ≈−12%.\n\n"
          "**Por qué con matices:**\n"
          "• Negocio sin moat, ROE de 1-3%, beneficio en pico de ciclo y previsión de BO −66%.\n"
          "• Gobierno corporativo pasivo: sin plan de P/B, sin recompras e incentivos fijos. El descuento puede persistir (trampa de valor).\n"
          "• Muy ilíquida (capitalización de ≈42 M USD): hay que usar órdenes limitadas.\n\n"
          "**Gestión de la posición:** comprar escalonadamente por debajo de 360 JPY; reforzar en 300-320; recoger beneficios parciales en 440-480; mantener el resto si hay catalizadores de capital. Revisar la tesis tras los resultados de nov-2026 y tras la junta de jun-2027 (kill switch #5).", fill="E8F5E9")
    return D.save(out, "Factores_a_Monitorear")
