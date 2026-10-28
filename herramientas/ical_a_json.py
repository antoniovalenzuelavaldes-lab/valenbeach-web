"""Convierte el calendario iCal de Booking en datos/disponibilidad.json (solo fechas ocupadas).
La URL del calendario es PRIVADA: se lee de la variable de entorno BOOKING_ICAL y nunca se guarda en ficheros.
Uso:  BOOKING_ICAL="https://ical.booking.com/v1/export?t=..." python herramientas/ical_a_json.py"""
import os, re, sys, json, urllib.request, datetime

url = os.environ.get("BOOKING_ICAL")
if not url:
    sys.exit("Falta la variable de entorno BOOKING_ICAL")
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
txt = urllib.request.urlopen(req, timeout=30).read().decode("utf8", "replace")
txt = re.sub(r"\r?\n[ \t]", "", txt)  # unir lineas plegadas
rangos = []
for ev in re.findall(r"BEGIN:VEVENT(.*?)END:VEVENT", txt, re.S):
    a = re.search(r"DTSTART(?:;[^:]*)?:(\d{8})", ev)
    b = re.search(r"DTEND(?:;[^:]*)?:(\d{8})", ev)
    if a and b:
        f = lambda s: f"{s[:4]}-{s[4:6]}-{s[6:]}"
        rangos.append([f(a.group(1)), f(b.group(1))])  # [entrada, salida): la noche de salida queda libre
rangos.sort()
ahora = datetime.datetime.now(datetime.timezone.utc).strftime("%d/%m/%Y %H:%M UTC")
dest = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "datos", "disponibilidad.json")
json.dump({"actualizado": ahora, "ocupado": rangos}, open(dest, "w", encoding="utf8"), ensure_ascii=False, indent=1)
pub = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "docs", "disponibilidad.json")
if os.path.isdir(os.path.dirname(pub)):  # copia publicada, para no tener que reconstruir toda la web
    json.dump({"actualizado": ahora, "ocupado": rangos}, open(pub, "w", encoding="utf8"), ensure_ascii=False, indent=1)
print(len(rangos), "rangos ocupados:", rangos)
