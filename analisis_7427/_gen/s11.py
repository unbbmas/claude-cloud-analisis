from helpers import *
from data import *


def build(out):
    D = Doc(11, "Factores a Monitorear")
    D.h1("11.1 KPIs Críticos")
    D.table(["KPI", "Último dato", "Umbral 🟢", "Umbral 🔴", "Fuente / frecuencia"], [
        ["Margen bruto trimestral", "10,18% (1T FY2/2027)", ">11,0%", "<10,3%", "Tanshin trimestral"],
        ["SG&A / ventas", "10,16% (1T)", "<10,0%", ">10,3%", "Tanshin"],
        ["BO del 1S FY2/2027", "1T: 8 M JPY", "≥450", "<300", "Tanshin 1S (≈9-10 oct-2026)"],
        ["Previsión anual de BO", "1.150 M JPY", "Mantenida o recorte <15%", "Recorte a <800", "TDnet"],
        ["Crecimiento de ventas", "+2,9% (1T)", ">+2%", "<−2%", "Tanshin"],
        ["Peso de Rakuten / cambios de clientes", "10,5% / «cambios de condiciones»", "Sin nuevas pérdidas", "Nuevas menciones a pérdida de cuentas", "Yuho / MD&A"],
        ["Fletes / ventas", "5,0% (FY2/2026)", "<4,9%", ">5,2%", "Yuho anual"],
        ["Rappels pendientes / BO", "2.199 / 1.110 = 2,0x", "<2,0x", ">2,5x", "Yuho (KAM)"],
        ["Caja neta normalizada", "≈1.500 M JPY", ">1.000", "<0 (deuda neta estructural)", "Balance (atención al calendario)"],
        ["P/B", "0,42x", ">0,50x", "<0,36x", "Diario"],
        ["Participaciones de Kokubu e Itochu", "18,2% / 3,6%", "Aumento o informe de participación significativa", "Venta", "EDINET (大量保有報告書)"],
        ["Dividendo", "30 JPY", "≥30 JPY", "Recorte", "Tanshin"],
    ], size=7.5)
    D.src(Q1 + "; " + YUHO[2026])

    D.h1("11.2 Catalizadores Positivos (12 meses)")
    D.table(["#", "Catalizador", "Fecha estimada", "Probabilidad", "Impacto"], [
        ["1", "**Operación corporativa**: Kokubu (18,2%) y/o Itochu (3,6%) integran o excluyen a Echo de bolsa, siguiendo a Mitsubishi Shokuhin (2025), Itochu Shokuhin (2026) y PALTAC (2026)", "Indeterminado", "🔴 Baja (10-15%) ⚠️", "+60-130%"],
        ["2", "**Recuperación del margen en el 2S FY2/2027** tras los cambios con clientes del 1T (efecto comparativo favorable y subidas de precio)", "Resultados 3T (≈ene-2027) y anuales (≈abr-2027)", "🟡 Media (40%)", "+10-25%"],
        ["3", "**Política de capital**: plan de P/B (petición de la TSE), subida del payout al ≥30% prometido, recompras", "Resultados anuales / junta (abr-may 2027)", "🟡 Baja-media (20-25%)", "+10-30%"],
        ["4", "**Nuevos productos y marcas propias** (GOODISH en otoño de 2026; ShareZ «Magokoro Gohan») con más margen", "Otoño 2026 - 2027", "🟡 Media (35%)", "+5%"],
        ["5", "**Previsión de FY2/2028 creíble** con el nuevo plan y el bonus ligado al BO", "abr-2027", "🟡 Media (40%)", "+5-15%"],
    ], size=8)

    D.h1("11.3 Eventos Invalidantes (kill switches)")
    D.table(["#", "Evento", "Por qué invalida la tesis", "Acción"], [
        ["1", "**Pérdida operativa en el 1S o el 2S de FY2/2027**", "El margen normalizado de ≈1% deja de ser válido", "Vender / reducir"],
        ["2", "**Recorte del dividendo**", "Señal de deterioro estructural y rompe el «suelo» de rentabilidad del 3,6%", "Vender"],
        ["3", "**Venta de la participación de Kokubu** a un tercero sin oferta a los minoritarios, o reducción de su peso", "Elimina el catalizador corporativo", "Revisar"],
        ["4", "**Deuda neta estructural** (no explicada por el calendario) o adquisición relevante", "Erosión del margen de seguridad", "Revisar / vender"],
        ["5", "**Ventas <−3% dos trimestres seguidos** con nuevas pérdidas de clientes", "Pérdida de posición competitiva", "Vender"],
    ], size=8)

    D.h1("Calendario de eventos")
    D.table(["Fecha (estimada)", "Evento"], [
        ["≈9-10 oct-2026", "**Resultados del 1S FY2/2027** (probable revisión de la previsión)"],
        ["Otoño 2026", "Relanzamiento de la marca GOODISH"],
        ["≈9 ene-2027", "Resultados del 3T FY2/2027"],
        ["≈9 abr-2027", "Resultados anuales FY2/2027 + previsión FY2/2028 + dividendo"],
        ["≈inicio de may-2027", "Feria «Minna Daisuki!! Pet Kingdom 2027»"],
        ["≈finales de may-2027", "Junta General de Accionistas y Yuho FY2/2027"],
    ], size=8.5)
    D.src("Fechas históricas: Tanshin del 1S el 10-oct-2025, del 3T el 9-ene-2026 y anual el 10-abr-2026; " + Q1 + " (10-jul-2026)")

    D.h1("CONCLUSIÓN FINAL Y RECOMENDACIÓN")
    D.box("**¿Es Echo Trading una buena inversión a 6-18 meses al precio de 835 JPY?**\n\n"
          "**Respuesta: SÍ, CON CONDICIONES → 🟡 MANTENER / ACUMULAR DE FORMA ESCALONADA, preferiblemente DESPUÉS de los resultados del 1S (≈9-10 oct-2026). Posición pequeña (≤2% de la cartera). Precio objetivo base a 12 meses ≈930 JPY (+15% con dividendo), valor esperado ≈983 JPY (+21%), valor intrínseco central ≈1.235 JPY.**\n\n"
          "**A favor:**\n"
          "• Valoración muy baja: P/B de 0,42x, ≈0,52x el NCAV, PER de FY2/2026 de 6,5x y EV/EBITDA normalizado de ≈3x, con dividendo del 3,6% nunca recortado.\n"
          "• Negocio asset-light, sin deuda a largo y con clientes de calidad; FCF yield normalizado del ≈8%.\n"
          "• Opción estratégica: Kokubu (18,2%) e Itochu (3,6%) en un sector donde los accionistas de referencia están excluyendo de bolsa a sus mayoristas con primas del 30-45%.\n\n"
          "**En contra:**\n"
          "• Deterioro operativo: el 1T FY2/2027 tuvo un BO de 8 M JPY y el margen bruto baja en 3 de los últimos 4 años.\n"
          "• Dos incumplimientos de la previsión (≈−24%) y un tercero probable: credibilidad baja y riesgo de caída a corto plazo.\n"
          "• Sin moat, pérdida de terreno frente a Japell y presión de Rakuten y de los costes logísticos.\n\n"
          "**Gestión de la posición:** primera compra por debajo de 800 JPY tras la publicación del 1S; segunda en 700-750 si hay una revisión fuerte sin pérdidas operativas; recoger beneficios parciales en 950-1.000; mantener el resto como opción de operación corporativa. Revisar la tesis tras los resultados anuales de abr-2027 y aplicar los kill switches.", fill="E8F5E9")
    return D.save(out, "Factores_a_Monitorear")
