"""Sube el Worker `valenbeach-reserva` a Cloudflare (API oficial) y activa su direccion workers.dev.
Uso:  python desplegar.py <destino verificado> [nombre] [remitente] [origenes separados por comas] [sitio] [asunto]
Sin argumentos extra despliega el Worker de valenbeach.com.
El token se lee de C:\\Users\\AntonioVV\\.cloudflare_token y nunca se imprime. El destino NO se guarda en el repositorio."""
import json, os, sys, uuid, urllib.request

AQUI = os.path.dirname(os.path.abspath(__file__))
token = open(os.path.expanduser(r"~\.cloudflare_token")).read().strip()
destino = sys.argv[1]
NOMBRE = sys.argv[2] if len(sys.argv) > 2 else "valenbeach-reserva"
DESDE = sys.argv[3] if len(sys.argv) > 3 else "reservas@valenbeach.com"
ORIGENES = sys.argv[4] if len(sys.argv) > 4 else "https://valenbeach.com,https://www.valenbeach.com"
SITIO = sys.argv[5] if len(sys.argv) > 5 else "valenbeach.com"
ASUNTO = sys.argv[6] if len(sys.argv) > 6 else "Solicitud de reserva"


def api(ruta, metodo="GET", cuerpo=None, cabeceras=None):
    h = {"Authorization": "Bearer " + token, **(cabeceras or {})}
    req = urllib.request.Request("https://api.cloudflare.com/client/v4" + ruta, data=cuerpo, method=metodo, headers=h)
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return json.loads(r.read())
    except urllib.error.HTTPError as e:
        return json.loads(e.read())


cuenta = api("/accounts")["result"][0]["id"]
meta = {"main_module": "worker.js", "compatibility_date": "2025-01-01", "bindings": [
    {"type": "send_email", "name": "EMAIL", "destination_address": destino},
    {"type": "plain_text", "name": "DESTINO", "text": destino},
    {"type": "plain_text", "name": "DESDE", "text": DESDE},
    {"type": "plain_text", "name": "ORIGENES", "text": ORIGENES},
    {"type": "plain_text", "name": "SITIO", "text": SITIO},
    {"type": "plain_text", "name": "ASUNTO", "text": ASUNTO}]}
codigo = open(os.path.join(AQUI, "worker.js"), "rb").read()
b = "----" + uuid.uuid4().hex
partes = [(b'Content-Disposition: form-data; name="metadata"\r\nContent-Type: application/json', json.dumps(meta).encode()),
          (b'Content-Disposition: form-data; name="worker.js"; filename="worker.js"\r\nContent-Type: application/javascript+module', codigo)]
cuerpo = b"".join(b"--" + b.encode() + b"\r\n" + h + b"\r\n\r\n" + c + b"\r\n" for h, c in partes) + b"--" + b.encode() + b"--\r\n"
r = api(f"/accounts/{cuenta}/workers/scripts/{NOMBRE}", "PUT", cuerpo, {"Content-Type": "multipart/form-data; boundary=" + b})
print("subida:", r.get("success"), [e.get("message") for e in r.get("errors", [])])
r = api(f"/accounts/{cuenta}/workers/scripts/{NOMBRE}/subdomain", "POST", json.dumps({"enabled": True}).encode(), {"Content-Type": "application/json"})
print("workers.dev:", r.get("success"), [e.get("message") for e in r.get("errors", [])])
sub = api(f"/accounts/{cuenta}/workers/subdomain")["result"]["subdomain"]
print(f"URL: https://{NOMBRE}.{sub}.workers.dev")
