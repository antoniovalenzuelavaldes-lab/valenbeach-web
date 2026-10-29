// Worker de Cloudflare: recibe la solicitud de reserva del formulario de valenbeach.com y la envia por correo al titular
// (Email Routing, binding send_email). No guarda nada. El destino y el remitente vienen de variables del Worker, no del codigo.
import { EmailMessage } from "cloudflare:email";

const MAX = { nombre: 80, email: 120, tel: 30, mensaje: 1500 };

const cors = (origen) => ({
  "Access-Control-Allow-Origin": origen,
  "Access-Control-Allow-Methods": "POST, OPTIONS",
  "Access-Control-Allow-Headers": "Content-Type",
  "Vary": "Origin",
});
const json = (obj, status, origen) => new Response(JSON.stringify(obj), { status, headers: { "Content-Type": "application/json", ...(origen ? cors(origen) : {}) } });
const limpia = (s, n) => String(s ?? "").replace(/[\r\n\t]+/g, " ").trim().slice(0, n);
const b64 = (txt) => { let s = ""; new TextEncoder().encode(txt).forEach((b) => (s += String.fromCharCode(b))); return btoa(s); };
const encabezado = (txt) => `=?UTF-8?B?${b64(txt)}?=`;
const fechaOk = (s) => /^\d{4}-\d{2}-\d{2}$/.test(s) && !isNaN(Date.parse(s));

export default {
  async fetch(req, env) {
    const origen = req.headers.get("Origin") || "";
    const ORIGENES = (env.ORIGENES || "https://valenbeach.com,https://www.valenbeach.com").split(",");   // webs autorizadas a usar este formulario
    if (!ORIGENES.includes(origen)) return new Response("Forbidden", { status: 403 });
    if (req.method === "OPTIONS") return new Response(null, { status: 204, headers: cors(origen) });
    if (req.method !== "POST") return json({ ok: false, error: "metodo" }, 405, origen);

    let d;
    try { d = await req.json(); } catch { return json({ ok: false, error: "formato" }, 400, origen); }
    if (d.web) return json({ ok: true }, 200, origen);                                   // campo trampa para robots: se ignora en silencio
    if (!d.t || Date.now() - Number(d.t) < 3000) return json({ ok: false, error: "rapido" }, 400, origen);   // enviado demasiado deprisa: robot

    const nombre = limpia(d.nombre, MAX.nombre), email = limpia(d.email, MAX.email), tel = limpia(d.tel, MAX.tel);
    const mensaje = String(d.mensaje ?? "").replace(/\r/g, "").trim().slice(0, MAX.mensaje);
    const entrada = limpia(d.entrada, 10), salida = limpia(d.salida, 10), personas = parseInt(d.personas, 10);
    if (!nombre || !/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(email)) return json({ ok: false, error: "datos" }, 400, origen);
    if ((entrada && !fechaOk(entrada)) || (salida && !fechaOk(salida)) || (entrada && salida && salida <= entrada)) return json({ ok: false, error: "fechas" }, 400, origen);

    const idioma = limpia(d.idioma, 5), estimado = limpia(d.estimado, 20), tema = limpia(d.asunto, 100);
    const cuerpo = [
      `Nuevo mensaje desde ${env.SITIO || "valenbeach.com"}`, "",
      `Nombre: ${nombre}`, `Correo: ${email}`, tel ? `Teléfono: ${tel}` : null,
      tema ? `Asunto: ${tema}` : null,
      entrada || salida ? `Entrada: ${entrada || "(sin indicar)"}` : null, entrada || salida ? `Salida: ${salida || "(sin indicar)"}` : null,
      isNaN(personas) ? null : `Personas: ${personas}`, estimado ? `Importe estimado de las noches: ${estimado} €` : null,
      `Idioma de la web: ${idioma || "?"}`, "", mensaje ? "Mensaje:\n" + mensaje : "(sin mensaje)", "",
      "— Para responder, usa «Responder»: el correo del cliente está en «Reply-To».",
    ].filter((x) => x !== null).join("\r\n");

    const asunto = `${env.ASUNTO || "Solicitud de reserva"}: ${nombre}${entrada && salida ? ` (${entrada} → ${salida})` : tema ? ` · ${tema}` : ""}`;
    const raw = [
      `From: ${encabezado(env.SITIO || "Valen Beach")} <${env.DESDE}>`, `To: ${env.DESTINO}`, `Reply-To: ${encabezado(nombre)} <${email}>`,
      `Subject: ${encabezado(asunto)}`, `Message-ID: <${crypto.randomUUID()}@valenbeach.com>`, `Date: ${new Date().toUTCString()}`,
      "MIME-Version: 1.0", "Content-Type: text/plain; charset=UTF-8", "Content-Transfer-Encoding: base64", "",
      b64(cuerpo).replace(/(.{76})/g, "$1\r\n"),
    ].join("\r\n");
    try {
      await env.EMAIL.send(new EmailMessage(env.DESDE, env.DESTINO, raw));
    } catch (e) {
      return json({ ok: false, error: "envio" }, 502, origen);
    }
    return json({ ok: true }, 200, origen);
  },
};
