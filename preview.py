"""Genera preview/valenbeach_preview.html: la portada en un solo fichero (imagenes incrustadas),
con NIF y domicilio completo ocultos, para revisarla en privado sin publicar nada."""
import base64, json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build

AQUI = build.AQUI
idioma = sys.argv[1] if len(sys.argv) > 1 else "es"
h = build.pagina_inicio(build.T[idioma])


def datauri(m):
    ruta = os.path.join(build.SITE, m.group(2).lstrip("/"))
    b = base64.b64encode(open(ruta, "rb").read()).decode()
    return f'{m.group(1)}data:image/jpeg;base64,{b}'


h = re.sub(r'(src=")(/img/[^"]+)"', lambda m: datauri(m) + '"', h)
h = re.sub(r'(url\()(/img/[^)]+)\)', lambda m: datauri(m) + ')', h)
h = h.replace('href="/#', 'href="#').replace('href="/en/#', 'href="#')
h = h.replace(build.DATOS["nif"], "[oculto en la versión de prueba]").replace(build.DATOS["domicilio"], "Carretera de Almería 23b, 29770 Torrox (Málaga)")
tarifas = json.load(open(os.path.join(AQUI, "datos", "tarifas.json"), encoding="utf8"))
dd = os.path.join(AQUI, "datos", "disponibilidad.json")
disp = json.load(open(dd, encoding="utf8")) if os.path.exists(dd) else {"actualizado": None, "ocupado": []}
shim = ("<script>(function(){var D=" + json.dumps({"/tarifas.json": tarifas, "/disponibilidad.json": disp}) +
        ";var of=window.fetch;window.fetch=function(u){u=String(u);if(D[u])return Promise.resolve(new Response(JSON.stringify(D[u]),{status:200}));return of.apply(this,arguments)}})();</script>")
h = h.replace("<script>window.VB_BASE", shim + "<script>window.VB_BASE", 1)
banner = ('<div style="background:#fff4d6;color:#4a3b00;border-bottom:1px solid #e0b94a;padding:8px 16px;text-align:center;font-size:.9rem">'
          'Versión de prueba (solo portada): precios y calendario provisionales; datos fiscales ocultos; los enlaces a otras páginas no funcionan aquí.</div>')
h = h.replace("</header>", "</header>" + banner, 1)
os.makedirs(os.path.join(AQUI, "preview"), exist_ok=True)
out = os.path.join(AQUI, "preview", f"valenbeach_preview_{idioma}.html")
open(out, "w", encoding="utf8").write(h)
print(out, round(os.path.getsize(out) / 1024), "KB")
