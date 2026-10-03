import os, zipfile, importlib
OUT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
paths = []
for i in range(1, 13):
    m = importlib.import_module(f"s{i:02d}")
    paths.append(m.build(OUT))
    print("OK", paths[-1])
zp = os.path.join(OUT, "Analisis_Inversion_Nichiwa_Sangyo_2055_12_secciones.zip")
with zipfile.ZipFile(zp, "w", zipfile.ZIP_DEFLATED) as z:
    for p in paths:
        z.write(p, os.path.basename(p))
print("ZIP", zp, os.path.getsize(zp))
