from helpers import *
from data import *


def build(out):
    D = Doc(7, "Management y Governance")
    D.h1("7.1 Historia de la Compañía")
    D.table(["Periodo", "Hito", "Relevancia"], [
        ["1971-1992", "Fundación (Echo Hanbai) y red nacional; fusión de 1992 y nuevo nombre", "Empresa fundada por emprendedores de Osaka; la familia Takahashi sigue entre los principales accionistas ⚠️"],
        ["1995-2005", "Salida a bolsa en Osaka y Tokio; 1.ª sección en 2005", "Etapa de expansión logística"],
        ["2013", "Kokubu entra como primer accionista (18,31%)", "Ancla estratégica; consejero de Kokubu en el consejo"],
        ["2016", "Minoru Toyoda (ex Nisshin Seifun Premix) es nombrado presidente tras un año como responsable de la «reforma de gestión»", "Gestor profesional externo"],
        ["2016-2026", "BO de ≈70-100 M JPY (FY2/2019-20) → máximo de 1.720 (FY2/2024) → 1.110 (FY2/2026)", "Recuperación y nueva erosión"],
        ["2026", "Nuevo plan a medio plazo y nueva retribución variable ligada al BO", "Inicio de un nuevo ciclo estratégico"],
    ], size=8.5)
    D.src(YUHO[2026] + ", p.4-5 y p.34-36")

    D.h1("7.2 Equipo Directivo")
    D.table(["Nombre", "Cargo", "Nacimiento", "Trayectoria", "Acciones (miles)", "% capital"], [
        ["Minoru Toyoda", "Presidente y consejero delegado (desde mar-2016); presidente de Pets Value e I&I", "1955", "Nisshin Seifun Premix (2012); en Echo desde 2015", "94", "1,56%"],
        ["Koji Umezawa", "Consejero ejecutivo, director comercial", "1971", "En la empresa desde 1994", "20", "0,33%"],
        ["Yoshiharu Ono", "Consejero ejecutivo: estrategia, contabilidad, sistemas y finanzas", "1975", "En la empresa desde 2003 (antes, notario)", "15", "0,25%"],
        ["Yukihisa Kato", "Consejero ejecutivo: personas, asuntos generales y formación", "1976", "En la empresa desde 1999", "14", "0,23%"],
        ["Fumitaka Shinada", "Consejero externo (**directivo de Kokubu**)", "1964", "Kokubu desde 1988; director ejecutivo de Kokubu Group", "—", "—"],
        ["Takemasa Hirafuji", "Consejero, miembro permanente del comité de auditoría", "1958", "Sugi Yakkyoku; Echo desde 2005", "1", "0,02%"],
        ["Yutaka Konishi", "Consejero externo, comité de auditoría (CPA)", "1968", "**Auditor de Echo desde 2004** (22 años)", "—", "—"],
        ["Yukinori Furukawa", "Consejero externo, comité de auditoría (abogado)", "1974", "**Auditor de Echo desde 2009** (17 años)", "—", "—"],
        ["**Total consejo**", "", "", "", "**145**", "**2,4%**"],
    ], size=7.5)
    D.src(YUHO[2026] + ", p.30 y p.34-36")
    D.p("🟡 Consejo de 8 hombres (0% mujeres), con 3 externos de los que **solo 2 son independientes**, y ambos con una antigüedad muy larga (17-22 años). Esto **debilita su independencia real** según los criterios internacionales. 🟢 El consejo se reúne mensualmente y existen comités de sostenibilidad y de riesgos. 🔴 El departamento de auditoría interna tiene **una sola persona**.")
    D.src(YUHO[2026] + ", p.30 y p.42")

    D.h1("7.3 Estructura de Propiedad")
    D.table(["Accionista (28-feb-2026)", "Miles de acciones", "%", "Naturaleza", "Evolución"], [
        ["Kokubu Group Honsha", "1.105", "18,20%", "Socio estratégico, proveedor (sociedad vinculada)", "Estable desde 2013"],
        ["Kazuhiko Takahashi", "380", "6,26%", "Particular (Ashiya) ⚠️ probable familia fundadora", "↓ desde 480 (feb-2022)"],
        ["Echo Trading Kyoeikai", "342", "5,63%", "Asociación de proveedores-accionistas", "↑ desde 325"],
        ["Itochu Corp.", "220", "3,62%", "Trading general", "Estable"],
        ["Kenta Iwami", "143", "2,36%", "Particular (Tokio)", "🟡 Nuevo en el top 10"],
        ["TR K.K.", "129", "2,13%", "Sociedad patrimonial (Ashiya) ⚠️ vinculada a la familia Takahashi", "Estable"],
        ["Plan de accionariado de empleados", "116", "1,92%", "Empleados", "↑ desde 76"],
        ["Akihiro Takahashi", "100", "1,65%", "Particular (Ashiya) ⚠️", "Estable"],
        ["Minoru Toyoda (presidente)", "94", "1,56%", "Directivo", "↑ desde 64 (acciones restringidas)"],
        ["Akira Kasahara", "78", "1,29%", "Particular", "Nuevo"],
        ["**Top 10**", "**2.709**", "**44,61%**", "", ""],
    ], size=8)
    D.src(YUHO[2026] + " p.26; " + YUHO[2022] + " p.19; " + YUHO[2024] + " p.27")
    D.table(["Tipo de accionista", "% feb-2026"], [
        ["Instituciones financieras", "0,39%"], ["Sociedades de valores", "2,93%"], ["Otras sociedades", "30,54%"],
        ["Extranjeros", "2,97%"], ["Particulares y otros", "62,95%"], ["N.º de accionistas", "3.698 (+922 con menos de 100 acciones)"],
    ])
    D.p("**Lectura:** 🟡 base accionarial de **particulares (63%)** y socios estratégicos (Kokubu + Itochu + Kyoeikai ≈ 27%), con casi nula presencia institucional (0,4%) y extranjera (3%). 🔴 Iliquidez y nula cobertura de analistas. 🟢 **Kokubu (18,2%) + Itochu (3,6%) suman ≈22%**. En un sector donde Mitsubishi Corp, Itochu y Medipal han comprado el resto de sus filiales cotizadas (2025-2026), es un **catalizador potencial** ⚠️ (no hay ningún anuncio).")

    D.h1("7.4 Situación Financiera del Controlador")
    D.p("No hay sociedad matriz. **Kokubu Group Honsha** (privada, Tokio, capital de 3.500 M JPY) es el mayor distribuidor independiente de alimentación y bebidas de Japón, con ventas de ≈2 billones de JPY ⚠️. Su capacidad financiera para comprar el resto de Echo (≈4.100 M JPY a precio de mercado por el 81,8% restante) es holgada. ⚠️ No hay datos financieros auditados de Kokubu en los documentos adjuntos.")
    D.src(YUHO[2026] + ", p.77 (関連当事者情報)")

    D.h1("7.5 Track Record del Management")
    D.table(["Métrica", "Antes / inicio (FY2/2019-20)", "Máximo (FY2/2024)", "Actual (FY2/2026)", "1T FY2/2027"], [
        ["Ventas (M JPY)", "81.054-81.387", "107.406", "105.811", "27.285"],
        ["BO (M JPY)", "69-94", "1.720", "1.110", "8"],
        ["Margen operativo", "0,1%", "1,6%", "1,05%", "0,03%"],
        ["ROE", "≈−0,2% a 0,5%", "12,0%", "6,6%", "≈0%"],
        ["Dividendo por acción (JPY)", "20", "33 (incl. 5 extra)", "30", "30 (prev.)"],
        ["Valor contable por acción (JPY)", "≈1.448-1.465", "1.780", "2.005", "1.977"],
    ], size=8)
    D.src(TIKR + "; Yuho FY2/2024 y FY2/2026; " + Q1)
    D.p("🟢 Bajo Toyoda (2016-), la empresa pasó de un beneficio casi nulo a un máximo de 1.720 M JPY (con ayuda de las subidas de precio de 2022-24) y el valor contable por acción creció ≈+4,6% anual. 🔴 Desde FY2/2024 el beneficio cae (−35%) y el plan «I3☆55» terminó con incumplimientos de la previsión en FY2/2025 y FY2/2026. 🟡 Con 71 años, **la sucesión del presidente** es un tema abierto.")

    D.h1("7.6 Insider Ownership y transacciones")
    D.table(["Persona", "Acciones FY2/2024", "Acciones FY2/2026", "Cambio", "Origen"], [
        ["Minoru Toyoda (presidente)", "64.000", "94.000", "+30.000", "Acciones restringidas (2024: 15.000 a 1.263 JPY; 2025: 15.000 a 928 JPY)"],
        ["Kazuhiko Takahashi", "380.000", "380.000", "0", "(−100.000 entre feb-2022 y feb-2024)"],
        ["Consejeros ejecutivos (conjunto)", "n.d.", "≈143.000", "+", "Acciones restringidas de 39.000 por año (2024 y 2025)"],
    ], size=8)
    D.src(YUHO[2026] + " p.25 (emisión de acciones restringidas) y p.77 (Toyoda: 18,9 M JPY en 2024 y 13,9 M JPY en 2025); " + YUHO[2024] + " p.27")
    D.p("🟡 **No hay compras en mercado** de los consejeros: el aumento viene de las acciones restringidas. 🔴 La venta de 100.000 acciones por el probable accionista fundador (2022-24, a precios de ≈600-1.600 JPY) no es una señal positiva, aunque puede responder a planificación patrimonial.")

    D.h1("7.7 Incentivos")
    D.table(["Elemento", "Situación FY2/2026", "Cambio previsto (junta de 27-may-2026)", "Alineación"], [
        ["Retribución de 4 consejeros ejecutivos", "127,7 M JPY (fijo 91,7 + acciones restringidas 36,1); bonus 0", "Límite de 400 M JPY/año (antes 360)", "—"],
        ["Bonus ligado a resultados", "No había en FY2/2026", "**Nuevo bonus**: 10-50% del fijo si el BO alcanza el 85-120% de la **previsión publicada a principio de año**", "🔴 Incentiva previsiones conservadoras"],
        ["Acciones restringidas (RS)", "39.000 acciones/año; restricción de **50 años** (hasta la salida)", "Límite de 70 M JPY/año", "🟢 Alineación a largo plazo con el accionista"],
        ["Stock options", "Ninguna", "—", "🟡"],
        ["Quién decide la retribución individual", "El presidente, por delegación del consejo", "—", "🔴 Autorreferencial"],
    ], size=8)
    D.src(YUHO[2026] + ", p.44-46")
    D.p("🔴 **Red flag de diseño**: ligar el bonus a la **propia previsión** de la dirección (y no a un objetivo externo o al ROE/ROIC) incentiva a fijar previsiones bajas. 🟢 Las acciones restringidas a 50 años sí alinean con el precio a largo plazo: el presidente ya tiene ≈78 M JPY en acciones (94.000 × 835).")

    D.h1("7.8 Red Flags de Governance")
    D.table(["Señal de alerta", "¿Presente?", "Comentario"], [
        ["Incumplimiento repetido de previsiones sin revisión previa", "🔴 Sí", "FY2/2026: Bº ordinario previsto de 1.459 mantenido el 9-ene-2026; real de 1.107 (−24%); no se localizó revisión antes del cierre"],
        ["Auditor con mandato excesivo", "🔴 Sí", "Deloitte Tohmatsu, **33 años**"],
        ["Independientes con antigüedad excesiva", "🔴 Sí", "17 y 22 años de vinculación"],
        ["Accionista-proveedor con consejero en el consejo", "🟡 Sí", "Kokubu: compras de 10.822 M JPY «a condiciones de mercado»"],
        ["Participaciones en clientes (政策保有株式)", "🔴 Sí", "14 cotizadas por 785 M JPY, y en aumento vía asociaciones de proveedores"],
        ["Auditoría interna insuficiente", "🔴 Sí", "1 persona"],
        ["Bonus ligado a la previsión propia", "🔴 Sí (desde 2026)", "Ver 7.7"],
        ["Salvedades del auditor", "🟢 No", "Opinión limpia; KAM sobre rappels"],
        ["Dilución", "🟢 Mínima", "+0,65% por año en acciones restringidas"],
        ["Transacciones vinculadas relevantes", "🟡 Kokubu", "Divulgadas"],
    ], size=8)
    D.src(YUHO[2026] + ", p.42, p.47, p.77, p.94; búsquedas Kabutan/Monex del 3-oct-2026 (previsión y su mantenimiento el 9-ene-2026)")

    D.h1("7.9 Calidad de la Información")
    D.table(["Aspecto", "Evaluación"], [
        ["Informes legales (Yuho y Tanshin)", "🟢 Completos y en plazo"],
        ["Presentación de resultados / conferencia", "🔴 No («補足説明資料 無 / 説明会 無»)"],
        ["Objetivos cuantitativos del plan a medio plazo", "🔴 No figuran en el Yuho; solo una referencia genérica a «objetivos numéricos»"],
        ["Desglose por canal y cliente", "🟡 Solo producto y clientes >10%"],
        ["Explicación del efecto festivo en el balance", "🟢 Sí (buena práctica)"],
        ["Información en inglés", "🔴 Muy limitada ⚠️"],
        ["**Puntuación global**", "**🟡 4/10**"],
    ], size=8.5)

    D.h1("7.10 Guidance y Cumplimiento")
    D.table(["Ejercicio", "Previsión inicial", "Revisión", "Real", "Desviación", "Resultado"], [
        ["FY2/2024", "«Menor crecimiento del beneficio» (cifra no localizada)", "n.d.", "BO 1.720 / Bº ord. 1.745", "Muy por encima", "🟢 Supera"],
        ["FY2/2025", "Bº ordinario 1.780 (+2,5%)", "No localizada", "1.370", "**−23%**", "🔴 Incumple"],
        ["FY2/2026", "BO ≈1.450 / Bº ordinario 1.459 (+6,6%)", "Mantenida el 9-ene-2026", "BO 1.110 / Bº ord. 1.107", "**−24%**", "🔴 Incumple"],
        ["FY2/2027", "Ventas 110.000 / BO 1.150 / BN 758 (1S: BO 555)", "Mantenida el 10-jul-2026", "1T: BO 8 (1,4% del 1S)", "—", "🔴 Riesgo muy alto"],
    ], size=8)
    D.src("Kabutan: «今期経常は3％増で2期連続最高益更新へ» (5-abr-2024), «今期経常は7％増益へ» (11-abr-2025), «今期経常は4％増益へ» (10-abr-2026); Monex Scouter (9-ene-2026); " + Q1)
    D.p("🔴 **Credibilidad baja de la previsión**: dos incumplimientos seguidos de ≈−24% y un 1T FY2/2027 que deja la nueva previsión en entredicho. La norma de la TSE exige revisar la previsión cuando el beneficio se desvía ≥30%. Las desviaciones de ≈24% han quedado **justo por debajo** de ese umbral, lo que permitió no revisar.")

    D.h1("Conclusión de la Sección 7")
    D.box("🟡/🔴 **Gobierno corporativo mejorable**: dirección profesional con un buen recorrido 2016-2024, pero previsiones poco fiables, independientes con antigüedad excesiva, auditoría interna mínima y un nuevo bonus que premia batir la propia previsión. 🟢 Las acciones restringidas a 50 años alinean al equipo, y la presencia de Kokubu (18,2%) e Itochu (3,6%) abre la puerta a una **operación corporativa** en un sector en plena consolidación.", fill="FFF4E5")
    return D.save(out, "Management_y_Governance")
