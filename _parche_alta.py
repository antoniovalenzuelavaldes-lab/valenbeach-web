import json
s = open('build.py', encoding='utf8').read()
# 1) bug de enlaces/imagenes en la version de prueba: se perdia el nombre del atributo
viejo = '''re.sub(r'(href|src)="/(?!/)', r'="' + BASE + '/', contenido)'''
assert viejo in s
s = s.replace(viejo, '''re.sub(r'(href|src)="/(?!/)', lambda m: m.group(1) + '="' + BASE + '/', contenido)''')
# 2) tarjetas de tarifas
s = s.replace('"tar": [("Temporada baja", "desde 150 € por noche"), ("Temporada alta", "desde 200 € por noche")],',
              '"tar": [("Temporada alta (julio)", "450 € por noche"), ("Resto del año", "desde 150 € por noche")],')
s = s.replace('"tar": [("Low season", "from €150 per night"), ("High season", "from €200 per night")],',
              '"tar": [("High season (July)", "€450 per night"), ("Rest of the year", "from €150 per night")],')
open('build.py', 'w', encoding='utf8').write(s)
# 3) tarifas.json
p = 'datos/tarifas.json'
d = json.load(open(p, encoding='utf8'))
for t in d['temporadas']:
    if t['nombre'] == 'Temporada alta':
        t['precio'] = 450
        t['rangos'] = [["07-01", "07-31"]]
        t['_origen'] = "Indicado por el titular el 28/10/2026: temporada alta = julio, 450 EUR/noche"
d['_nota'] = ("Datos de la web antigua (Pinpoint) y confirmaciones del titular (28/10/2026): limpieza incluida, estancia minima 2 noches, "
              "temporada alta = julio a 450 EUR/noche. PENDIENTE: precio y fechas de la temporada baja (hoy el calendario usa 200 EUR/noche fuera de julio) e IVA.")
d['iva_incluido'] = True
d['_nota'] = d['_nota'].replace(' e IVA.', '.') + " IVA incluido en los precios (confirmado por el titular)."
json.dump(d, open(p, 'w', encoding='utf8'), ensure_ascii=False, indent=2)
s = open('build.py', encoding='utf8').read()
a = 'Estancia mínima: 2 noches. Limpieza final incluida en el precio.",'
assert a in s
s = s.replace(a, 'Precios con IVA incluido. Estancia mínima: 2 noches. Limpieza final incluida en el precio.",', 1)
b = 'Minimum stay: 2 nights. Final cleaning included in the price.",'
assert b in s
s = s.replace(b, 'Prices include VAT. Minimum stay: 2 nights. Final cleaning included in the price.",', 1)
s = s.replace('"est": "Importe estimado de las noches: {t} € (a confirmar)"', '"est": "Importe estimado de las noches: {t} € (IVA incluido, a confirmar)"', 1)
s = s.replace('"est": "Estimated total for the nights: €{t} (to be confirmed)"', '"est": "Estimated total for the nights: €{t} (VAT included, to be confirmed)"', 1)
open('build.py', 'w', encoding='utf8').write(s)
print('ok')
