from helpers import *
from data import *


def build(out):
    D = Doc(4, "Análisis Financiero Detallado")
    D.h1("4.1 Revenue Analysis")
    D.h2("Evolución trimestral / semestral (periodos disponibles)")
    D.p("Echo publica Tanshin trimestrales y semestrales; los informes anuales solo incluyen información semestral desde 2024. La tabla combina datos 🔍 verificados (Tanshin 1T FY2/2027) y 💡 derivados de las variaciones porcentuales publicadas en Tanshin y noticias (Kabutan).")
    D.table(["Periodo", "Ventas", "Var. a/a", "BO", "Var. a/a", "Margen operativo", "Fuente"], [
        ["1T FY2/2025 (mar-may 24)", "≈26.722 💡", "n.d.", "≈320 💡", "n.d.", "≈1,20%", "Derivado de la variación del 1T FY2/2026 (−0,8%; −35,6%)"],
        ["1S FY2/2025 (mar-ago 24)", "n.d.", "n.d.", "≈848 💡", "n.d.", "n.d.", "Derivado (1S FY2/2026 = −20,2%)"],
        ["2S FY2/2025 (sep-24 a feb-25)", "n.d.", "n.d.", "≈512 💡", "n.d.", "n.d.", "1.360 − 848"],
        ["1T FY2/2026 (mar-may 25)", "26.508", "−0,8%", "206", "−35,6%", "0,78%", "🔍 Q1_2026 p.1"],
        ["2T FY2/2026 (jun-ago 25)", "≈26.353 💡", "n.d.", "≈471 💡", "≈−10% (Bº ord.)", "≈1,79%", "1S − 1T (Kabutan: «jun-ago −10%»)"],
        ["2S FY2/2026 (sep-25 a feb-26)", "≈52.950 💡", "n.d.", "≈433 💡", "≈−15%", "≈0,82%", "Año − 1S"],
        ["**1T FY2/2027 (mar-may 26)**", "**27.285**", "**+2,9%**", "**8**", "**−96,1%**", "**0,03%**", "🔍 Q1_2026 p.1"],
    ], size=7.5)
    D.calc("1S FY2/2026: ventas = 54.500/1,031 = 52.861 y BO = 555/(1 − 0,18) = 677 (a partir de la previsión del 1S FY2/2027 y de su variación publicada). 1S FY2/2025: BO = 677/(1 − 0,202) = 848. 1T FY2/2025: ventas = 26.508/0,992 = 26.722 y BO = 206/0,644 = 320.")
    D.src(Q1 + " p.1; Kabutan «上期経常が20％減益で着地・6-8月期も10％減益» (10-oct-2025) y «今期経常は4％増益へ» (10-abr-2026), vía búsqueda web")
    D.p("🔴 **Tendencia del BO claramente bajista**: el margen operativo pasa de ≈1,2% (1T FY2/2025) a 0,78% (1T FY2/2026) y a **0,03% (1T FY2/2027)**. Las ventas se recuperan (+2,9%), pero el margen bruto cae 0,74 pp y el SG&A sube +3,0% (fletes).")
    D.h2("Evolución anual (8 años)")
    rows = []
    for y in YA:
        g = "" if y == 2019 else pct((sales[y] / sales[y - 1] - 1) * 100)
        rows.append([f"FY2/{y}", n(sales[y]), g, n(gp[y]), n(op[y]), n(ordinary[y]), n(ni[y]), n(eps[y], 2)])
    rows.append(["LTM may-2026", "106.588", "", "11.669", "912", "908", "641", "105,77"])
    D.table(["Ejercicio", "Ventas", "Δ%", "Bº bruto", "BO", "Bº ordinario", "BN", "BPA (JPY)"], rows, size=8)
    D.src(TIKR + "; Yuho FY2/2022-26 p.2")
    D.h2("CAGR")
    D.table(["Métrica", "Inicio", "Fin", "Años", "CAGR"], [
        ["Ventas FY2/2019→FY2/2026", "81.054", "105.811", "7", "+3,9%"],
        ["Ventas FY2/2022→FY2/2026", "91.930", "105.811", "4", "+3,6%"],
        ["Ventas FY2/2024→FY2/2026", "107.406", "105.811", "2", "−0,7%"],
        ["BO FY2/2022→FY2/2026", "467", "1.110", "4", "+24,2%"],
        ["BO FY2/2024→FY2/2026 (desde el máximo)", "1.720", "1.110", "2", "−19,7%"],
        ["BPA FY2/2022→FY2/2026", "47,82", "128,63", "4", "+28,1%"],
        ["Valor contable por acción FY2/2022→FY2/2026", "1.510,58", "2.005,33", "4", "+7,3%"],
    ], size=8.5)
    D.calc("Ej.: (1.110/467)^(1/4) − 1 = 24,2%; (1.110/1.720)^(1/2) − 1 = −19,7%.")

    D.h1("4.2 Recurrencia de Ingresos")
    D.p("🟢 **Alta recurrencia de facto (≈95%+)**: la comida y los consumibles (arena, empapadores) se reponen semanalmente en los mismos puntos de venta. 🔴 **Sin contratos plurianuales**: las condiciones se renegocian y las cuentas pueden cambiar de mayorista, como muestra el 1T FY2/2027.")
    D.table(["Tipo", "Peso FY2/2026", "Naturaleza"], [
        ["Comida para mascotas", "78,4%", "Recurrente, consumo diario"],
        ["Accesorios perro/gato (arena, empapadores, higiene, juguetes)", "19,1%", "Mayoritariamente consumible, recurrente"],
        ["Otros accesorios", "2,1%", "Duradero, puntual"],
        ["Otros (servicios, formación, eventos)", "0,4%", "Puntual (escuela traspasada en abr-2026)"],
    ], size=8.5)
    D.src(YUHO[2026] + ", p.20")

    D.h1("4.3 Crecimiento Orgánico vs Adquisiciones")
    D.table(["Ejercicio", "Δ Ventas", "Orgánico", "Adquisiciones", "💡 Precio", "💡 Volumen/mix"], [
        ["FY2/2022", "+6.276", "100%", "0", "+2 a +4%", "+3 a +5% (demanda por COVID)"],
        ["FY2/2023", "+5.025", "100%", "0", "+5 a +8%", "−2 a 0%"],
        ["FY2/2024", "+10.451", "100%", "0", "+10 a +12% (subidas de fabricantes)", "−1 a +1%"],
        ["FY2/2025", "−1.018", "100%", "0", "+1 a +2%", "−2 a −3%"],
        ["FY2/2026", "−577", "100%", "0", "≈0% («efecto agotado»)", "≈−0,5% (cambios de clientes; Rakuten +)"],
    ], size=8.5)
    D.p("⚠️ El reparto precio/volumen es una **estimación propia** basada en el comentario de la dirección y en la tendencia de volumen del mercado (valor +, volumen −). La empresa no publica volúmenes. 🔍 **Todo el crecimiento es orgánico.**")

    D.h1("4.4 Análisis M&A")
    D.table(["Operación", "Año", "Resultado"], [
        ["Compra de PetPet (portal de información)", "2013", "🔴 Cerrado en sep-2025 (no rentable)"],
        ["Venta de Kokoro K.K.", "2016", "🟡 Desinversión"],
        ["Alianza de capital con Kokubu (18,31%)", "2013", "🟡 Estabilidad accionarial y canal alimentario; no ha evitado la erosión del margen"],
        ["Compra de los minoritarios de I&I y PetPet", "2025-2026", "🟡 Simplificación (16 M JPY pagados)"],
        ["Marca GOODISH (procedente de Fancl)", "2026", "⚠️ Términos no publicados; relanzamiento en otoño de 2026"],
        ["Traspaso de la escuela Echo Pet Business a Yashima Gakuen", "abr-2026", "🟢 Salida de una actividad no estratégica (coste de reestructuración de 8 M JPY)"],
    ], size=8)
    D.src(YUHO[2026] + " p.4-7, p.18, p.58; " + Q1 + " p.2")
    D.p("🟡 Las operaciones son pequeñas y de simplificación de cartera («selección y concentración»), sin destrucción relevante de valor. 🔴 Las diversificaciones (portal, escuela, tiendas) no han generado valor medible.")

    D.h1("4.5 Backlog y Pipeline")
    D.p("🔴 **Sin cartera de pedidos** (no hay producción ni pedidos registrados: «受注実績 該当なし»). La visibilidad se limita a la **previsión de la dirección para FY2/2027**: ventas de 110.000 M JPY (+4,0%), BO de 1.150 (+3,6%), Bº ordinario de 1.147 (+3,6%), BN de 758 (−2,6%) y BPA de 124,81 JPY. Para el 1S: ventas de 54.500, BO de 555, BN de 371.")
    D.src(Q1 + ", p.1")
    D.calc("Avance del 1T sobre la previsión del 1S: BO 8/555 = **1,4%**; ventas 27.285/54.500 = 50,1%. Para cumplir el 1S, el 2T tendría que generar un BO de 547 M JPY, frente a ≈471 en el 2T FY2/2025 y un margen de 2,0% nunca visto en un 2T reciente. 🔴 **Es muy probable una revisión a la baja con los resultados del 1S (≈9-10 oct-2026)**, que sería la tercera vez seguida que no se cumple la previsión.")

    D.h1("4.6 Drivers de Crecimiento")
    D.table(["Driver", "Descripción", "Impacto potencial", "Probabilidad 6-18m"], [
        ["1. Recuperación del margen bruto", "Renegociación de condiciones, marcas propias (ShareZ, GOODISH), rappels", "±300-600 M JPY de BO", "🟡 Media-baja (30%)"],
        ["2. Comercio electrónico (Rakuten) y nuevos canales", "Volumen +; margen −", "+2-4% de ventas", "🟢 Alta (60%)"],
        ["3. Eficiencia logística (IA, entregas conjuntas, nuevos centros)", "Compensa la inflación de fletes", "+100-200 M JPY", "🟡 Media (40%)"],
        ["4. Subidas de precio de fabricantes", "Inflación de materias primas y yen débil", "+3-5% de ventas", "🟡 Media (50%)"],
        ["5. Operación corporativa (Kokubu/Itochu u otro)", "Integración o exclusión de bolsa en un sector en consolidación", "Prima del 30-60%", "🔴 Baja (10-15%) ⚠️"],
    ], size=8)

    D.h1("Conclusión de la Sección 4")
    D.box("🔴 **Deterioro operativo en curso**: ventas planas (CAGR de 2 años −0,7%), BO −35% desde el máximo y un 1T FY2/2027 prácticamente en equilibrio (BO de 8 M JPY). 🟡 Crecimiento 100% orgánico y recurrente, pero muy dependiente de precios de fabricantes. 🔴 La previsión de FY2/2027 parece **inalcanzable** a la luz del 1T: es un riesgo de corto plazo para la cotización.", fill="FDECEA")
    return D.save(out, "Analisis_Financiero")
