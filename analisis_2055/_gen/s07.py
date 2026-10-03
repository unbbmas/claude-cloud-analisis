from helpers import *
from data import *


def build(out):
    D = Doc(7, "Management y Governance")
    D.h1("7.1 Historia de la Compañía")
    D.table(["Periodo", "Hito", "Relevancia para el inversor"], [
        ["1924-1961", "Fundación en Kobe; cambio de nombre en 1948; salida a bolsa en Osaka en 1961", "Más de 100 años de historia; supervivencia demostrada"],
        ["1963-1995", "Red de 5 fábricas portuarias (Mihara, Kobe, Kagoshima, Hachinohe, Sakaide)", "La base de activos actual es de esta época"],
        ["1975-1999", "Entrada en la ganadería (Towa Chikusan, granjas)", "🔴 Origen del segmento deficitario"],
        ["1999-2017", "Masatoshi Nakahashi, presidente", "Gestión familiar y conservadora"],
        ["2017-2024", "Masatoshi Nakahashi, presidente del consejo; Taichiro Nakahashi, director general de ventas", "Transición familiar"],
        ["feb-2022", "Recompra del 5,8% del capital", "🟢 La única recompra significativa"],
        ["jun-2024", "**Taichiro Nakahashi (hijo), presidente y consejero delegado**", "Segunda generación"],
        ["jun-2025", "Paso a sociedad con comité de auditoría y supervisión", "🟡 Mejora formal de gobierno"],
        ["2024-2026", "Deterioros en ganadería por 1.277 M JPY", "Señal de reconocimiento de problemas por la nueva dirección"],
    ], size=8.5)
    D.src(YUHO[2026] + ", p.4 y p.22-23")

    D.h1("7.2 Equipo Directivo")
    D.table(["Nombre", "Cargo", "Nacimiento", "Trayectoria", "Acciones (miles)", "% capital*"], [
        ["Taichiro Nakahashi", "Presidente y consejero delegado (desde jun-2024)", "1979", "Entra en 2007; director de administración (2011), director general de ventas (2018)", "24", "0,13%"],
        ["Masatoshi Nakahashi", "Consejero y asesor (相談役); padre del presidente", "1945", "Presidente 1999-2017; presidente del consejo 2017-2024", "411", "2,27%"],
        ["Yukihisa Matsumoto", "Consejero, director de la fábrica de Mihara", "1952", "En la empresa desde 1975", "3", "0,02%"],
        ["Hideo Yasui", "Consejero, director de administración y asuntos generales", "1956", "En la empresa desde 1978", "25", "0,14%"],
        ["Satoshi Higashimokuhino", "Consejero, director de la fábrica de Kagoshima", "1961", "En la empresa desde 1984", "—", "0%"],
        ["Tsuneo Wakimura", "Consejero miembro del comité de auditoría (interno)", "1952", "Ex director de administración; auditor desde 2008", "211", "1,16%"],
        ["Shiro Kawasaki", "Consejero externo independiente (comité de auditoría)", "1953", "Ex Sanwa/MUFG; EY ShinNihon; consejero desde 2017", "—", "0%"],
        ["Kenji Yoshida", "Consejero externo independiente (comité de auditoría)", "1972", "Auditor (CPA, ex Tohmatsu); consejero en Monstar Lab", "—", "0%"],
        ["**Total consejo**", "", "", "", "**674**", "**3,72%**"],
    ], size=7.5)
    D.src(YUHO[2026] + ", p.22-23 «役員の状況». *% sobre 18.111.793 acciones en circulación")
    D.p("🔴 **Consejo de 8 hombres, sin mujeres**, con edad media elevada (cuatro consejeros nacidos antes de 1957), 6 internos de carrera y solo **2 independientes (25%)**. El código de gobierno corporativo japonés pide al menos 1/3 de independientes en Prime; en Standard se pide un mínimo de 2. 🟡 Cumple el mínimo.")

    D.h1("7.3 Estructura de Propiedad")
    D.table(["Accionista (31-mar-2026)", "Acciones (miles)", "%", "Naturaleza", "Evolución"], [
        ["Jumonji Chicken Company", "1.576", "8,70%", "Cliente (integradora avícola, Iwate)", "🟢↑ 733 (2021) → 991 → 1.139 → 1.385 → 1.576"],
        ["Toyota Tsusho", "1.362", "7,52%", "Proveedor de grano; participación cruzada", "Estable"],
        ["Tohoku Grain Terminal", "1.153", "6,37%", "Terminal de grano de Hachinohe", "Estable"],
        ["Cargill Japan", "1.000", "5,52%", "Trading de grano", "Estable"],
        ["Minato Bank", "903", "4,99%", "Banco local (Kobe)", "Estable"],
        ["MUFG Bank", "873", "4,82%", "Banco", "↓ desde 923 (2021)"],
        ["SMBC", "873", "4,82%", "Banco", "↓ desde 923 (2021)"],
        ["Hyogo Shinren (JA Hyogo)", "849", "4,69%", "Cooperativa agrícola", "Estable"],
        ["Japan Securities Finance", "767", "4,24%", "Financiación de valores (préstamo de margen)", "🟡 Nuevo en el top 10"],
        ["Seigo Naito", "601", "3,32%", "Particular", "🟡 Nuevo en el top 10"],
        ["**Top 10**", "**9.958**", "**54,98%**", "", ""],
        ["Autocartera", "2.719", "13,05% del total emitido", "", "Sin amortizar"],
    ], size=8)
    D.src(YUHO[2026] + " p.15; " + YUHO[2021] + " p.17; " + YUHO[2022] + " p.17; " + YUHO[2023] + " p.17; " + YUHO[2024] + " p.16")
    D.table(["Tipo de accionista (% acciones)", "FY3/2021", "FY3/2026"], [
        ["Instituciones financieras", "28,29%", "27,32%"], ["Sociedades de valores", "1,25%", "0,72%"],
        ["Otras sociedades", "31,18%", "34,36%"], ["Extranjeros", "9,84%", "3,60%"],
        ["Particulares y otros (incl. autocartera)", "29,44%", "34,00%"], ["Número de accionistas", "1.970", "1.596"],
    ])
    D.src(YUHO[2021] + " p.17 y " + YUHO[2026] + " p.15 «所有者別状況»")
    D.p("**Lectura:** ≈62% del capital está en manos de bancos, tradings, clientes y cooperativas (accionistas «estables» o de relación). 🔴 El free float real es pequeño y la acción es **muy ilíquida**. 🟢 La **acumulación continuada de Jumonji Chicken** (+115% en acciones desde 2021) es la señal de propiedad más relevante: un cliente estratégico que aumenta posición cada año. ⚠️ ESPECULACIÓN: podría anticipar una integración vertical o una operación corporativa. No hay ningún anuncio al respecto. 🟡 La salida de los extranjeros (9,8% → 3,6%) coincide con la recompra de feb-2022 a 355 JPY, probablemente a Unearth International (Seychelles, 4,95% en 2021).")

    D.h1("7.4 Situación Financiera del Controlador")
    D.p("No hay accionista de control ni matriz (la empresa declara «no tener sociedad matriz»). La familia Nakahashi, con ≈2,4% directo, controla la gestión pero no la propiedad. Los accionistas industriales relevantes (Toyota Tsusho, Cargill) son solventes; Jumonji Chicken es una empresa privada de Iwate de tamaño medio. ⚠️ No hay datos públicos verificados de su situación financiera.")
    D.src(YUHO[2026] + ", p.76 «提出会社の親会社等の情報»")

    D.h1("7.5 Track Record del Management")
    D.table(["Métrica", "Masatoshi Nakahashi como presidente del consejo (FY3/2018-24, media)", "Taichiro Nakahashi como presidente (FY3/2025-26, media)", "Comentario"], [
        ["Ventas (M JPY)", "≈45.000", "47.078", "Efecto precio del grano"],
        ["BO (M JPY)", "≈300 (FY3/2020-24)", "1.181", "🟢 Coincide con el grano a la baja"],
        ["Margen operativo", "≈0,7%", "2,5%", ""],
        ["ROE", "≈1,6%", "1,9%", "🔴 Los deterioros anulan la mejora operativa"],
        ["Deterioros", "168 (FY3/2024)", "1.277", "🟡 Saneamiento de la ganadería"],
        ["Dividendo por acción", "5-8 JPY", "6 JPY", "Sin cambios"],
        ["Recompras", "426 M JPY (2022)", "0", "🔴"],
    ], size=8)
    D.calc("BO medio FY3/2020-24 = (528+283+118−200+905)/5 = 327; FY3/2025-26 = (906+1.456)/2 = 1.181. ROE FY3/2018-24 a partir de los Yuho (3,08 / 1,46 / 2,12 / 0,79 / 0,67 / 0,90 / 3,04) → media 1,72%; FY3/2025-26: (1,70+2,03)/2 = 1,87%.")
    D.p("🟡 Es demasiado pronto para juzgar al nuevo presidente: la mejora del BO se explica por el ciclo del grano. Lo positivo: ha reconocido deterioros (limpieza contable) y ha reforzado formalmente el gobierno (comité de auditoría). Lo negativo: **ningún cambio en la política de capital** con P/B de 0,33x.")

    D.h1("7.6 Insider Ownership y transacciones")
    D.table(["Consejero", "Acciones FY3/2025 (miles)", "Acciones FY3/2026 (miles)", "Variación"], [
        ["Taichiro Nakahashi", "24", "24", "0"], ["Masatoshi Nakahashi", "411", "411", "0"],
        ["Yukihisa Matsumoto", "3", "3", "0"], ["Hideo Yasui", "25", "25", "0"], ["Tsuneo Wakimura", "211", "211", "0"],
    ])
    D.src(YUHO[2025] + " p.24 y " + YUHO[2026] + " p.22")
    D.p("🟡 **Sin compras ni ventas de directivos en el último año.** Con un 3,7% en manos del consejo, la alineación con el minoritario es baja. Japón no tiene un registro tipo «Form 4» de fácil acceso; los cambios se ven en el Yuho anual y en los informes de participaciones significativas (≥5%) de EDINET. No se han localizado informes de participación relevantes de directivos.")

    D.h1("7.7 Incentivos")
    D.table(["Elemento", "Situación", "Alineación"], [
        ["Retribución total de consejeros ejecutivos (6)", "79 M JPY (≈13 M por persona)", "—"],
        ["Retribución variable ligada a resultados", "**Ninguna** (solo salario fijo mensual)", "🔴"],
        ["Stock options / acciones restringidas", "**Ninguna**", "🔴"],
        ["Indemnización por jubilación", "Ninguna en el ejercicio", "🟡"],
        ["Quién fija la retribución individual", "El presidente, por delegación del consejo, oído un comité voluntario (presidente + 2 externos)", "🔴 Autorreferencial"],
        ["Límite aprobado por la junta", "160 M JPY/año (ejecutivos); 40 M JPY (comité de auditoría)", ""],
    ], size=8.5)
    D.src(YUHO[2026] + ", p.26 «役員の報酬等»")
    D.p("🔴 **Incentivos desalineados**: nada en la remuneración premia el ROE, el valor contable por acción ni el precio de la acción. La gestión no tiene motivos económicos para corregir el descuento de valoración.")

    D.h1("7.8 Red Flags de Governance")
    D.table(["Señal de alerta", "¿Presente?", "Comentario"], [
        ["Auditor con mandato excesivo", "🔴 Sí", "EY ShinNihon audita a la empresa desde hace **66 años** (rotación de socios correcta)"],
        ["Participaciones cruzadas con proveedores (政策保有株式)", "🔴 Sí", "5 valores cotizados por 1.153 M JPY; el valor de Toyota Tsusho se ha multiplicado (430 → 1.028) sin desinversión"],
        ["Remuneración sin variable", "🔴 Sí", "Solo salario fijo"],
        ["Gestión familiar sin control de capital", "🟡 Sí", "Sucesión padre-hijo; el padre sigue en el consejo como 相談役"],
        ["Consejo sin diversidad y con pocos independientes", "🔴 Sí", "0% mujeres; 25% independientes"],
        ["Plan de acción sobre el P/B (petición de la TSE para Prime y Standard)", "🔴 No localizado", "No aparece en el Yuho; no se ha encontrado publicación"],
        ["Caja excesiva sin plan de uso", "🔴 Sí", "Caja neta del 80% de la capitalización y sin programa de recompra"],
        ["Préstamos a filial insolvente", "🟡 Sí", "2.163 M JPY a Towa Chikusan, provisionados en 1.604"],
        ["Transacciones con partes vinculadas", "🟢 No", "«該当事項はありません»"],
        ["Salvedades del auditor / control interno", "🟢 No", "Opinión favorable sin salvedades; control interno efectivo"],
        ["Cambios de auditor o reexpresiones", "🟢 No", ""],
        ["Ampliaciones de capital dilutivas", "🟢 No", "Número de acciones sin cambios desde 1998"],
    ], size=8)
    D.src(YUHO[2026] + ", p.24, p.27, p.59, p.78-81")

    D.h1("7.9 Calidad de la Información")
    D.table(["Aspecto", "Evaluación", "Nota"], [
        ["Informes anuales y trimestrales", "🟢 Completos y auditados (J-GAAP)", "Yuho y Tanshin en plazo"],
        ["Presentación de resultados / conferencia", "🔴 No", "El Tanshin indica: material complementario «無» y reunión informativa «無»"],
        ["Información en inglés", "🔴 Muy limitada", "⚠️ No se ha encontrado IR en inglés"],
        ["KPIs operativos (toneladas, cuota)", "🔴 No publicados", ""],
        ["Plan a medio plazo", "🔴 No", "Solo la previsión anual"],
        ["Política de capital / objetivo de ROE", "🔴 No", ""],
        ["Cobertura de analistas", "🔴 Nula", "⚠️ Ningún informe de bróker localizado"],
        ["**Puntuación global**", "**🔴 2/10 en transparencia para el inversor**", "Cumple lo legal, nada más"],
    ], size=8.5)
    D.src(Q1 + ", p.1")

    D.h1("7.10 Guidance y Cumplimiento")
    D.table(["Ejercicio", "Ventas previstas → reales", "BO previsto → real", "Bº ordinario previsto → real", "BN previsto → real", "Resultado"], [
        ["FY3/2022", "40.000 → 44.906", "400 → 118", "500 → 217", "300 → 116", "🔴 Incumple (grano ↑)"],
        ["FY3/2023", "48.000 → 54.659", "300 → −200", "400 → −99", "200 → 157", "🔴 Incumple (grano ↑↑)"],
        ["FY3/2024", "50.000 → 52.887", "200 → 905", "300 → 915", "200 → 541", "🟢 Supera ampliamente"],
        ["FY3/2025", "50.000 → 48.577", "400 → 906", "400 → 1.143", "300 → 310", "🟢 BO x2,3; BN en línea"],
        ["FY3/2026", "50.000 → 45.579", "400 → 1.456", "400 → 1.440", "300 → 378", "🟢 BO x3,6"],
        ["FY3/2027", "50.000 → 1T: 11.764", "500 → 1T: 382", "500 → 1T: 413", "300 → 1T: 300", "🟢 1T ya cubre el 76% del BO y el 100% del BN"],
    ], size=8)
    D.src("Previsiones del apartado «経営戦略等» de cada Yuho: " + YUHO[2021] + " p.7; " + YUHO[2022] + " p.7; " + YUHO[2023] + " p.7; " + YUHO[2024] + " p.7; " + YUHO[2025] + " p.7; " + YUHO[2026] + " p.6. Resultados reales de cada Yuho siguiente")
    D.p("🟡 La previsión de la dirección es **mecánica y conservadora**: repite 50.000 M JPY de ventas cuatro años seguidos y una cifra «redonda» de beneficio. Falla en las dos direcciones según el ciclo del grano. 🟢 Desde FY3/2024 ha sido superada de forma sistemática. **La previsión de FY3/2027 (BN 300) ya se ha alcanzado en el 1T**, lo que hace probable una revisión al alza en el informe del 2T (noviembre 2026).")

    D.h1("Conclusión de la Sección 7")
    D.box("🔴 **Gobierno corporativo débil para el accionista minoritario**: gestión familiar con un 3,7% del capital, retribución fija sin incentivos, auditor desde hace 66 años, participaciones cruzadas, caja ociosa y ningún plan sobre el P/B. 🟢 Contabilidad limpia, sin salvedades ni transacciones vinculadas, y saneamiento reciente del segmento ganadero. 🟢 Accionista industrial (Jumonji Chicken) acumulando año tras año. **La gobernanza es la principal razón del descuento y, a la vez, su principal palanca de revalorización si cambia.**", fill="FDECEA")
    return D.save(out, "Management_y_Governance")
