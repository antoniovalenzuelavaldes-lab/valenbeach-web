"""Genera la web estatica de Valenbeach en site/ (ES y EN). Uso: python build.py
Sin dependencias externas, sin cookies, sin recursos de terceros."""
import os, json, html

AQUI = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.join(AQUI, "docs")
BASE = os.environ.get("BASE", "")  # p. ej. /valenbeach-web para la URL de prueba; vacio en el dominio real
ORIGEN = os.path.join(AQUI, "_origen")

DATOS = {
    "nombre": "Valen Beach",
    "titular": "Antonio Valenzuela Valdes",
    "nif": "[[NIF]]",
    "domicilio": "[[DOMICILIO]]",
    "email": "antonio@valenbeach.com",
    "tel_vis": "(+34) 615 174 997",
    "tel_wa": "34615174997",
    "registro": "AT-434842-A",
    "fecha": "28 de octubre de 2026",
    "date_en": "28 October 2026",
    "dominio": "https://valenbeach.com",
}

# Los datos fiscales NO viven en el repositorio: se leen de datos/titular.json (ignorado por git).
_tit = os.path.join(AQUI, "datos", "titular.json")
if os.path.exists(_tit):
    DATOS.update(json.load(open(_tit, encoding="utf8")))
else:
    print("AVISO: falta datos/titular.json (ver datos/titular.ejemplo.json); se usan marcadores.")

T = {
 "es": {
  "lang": "es", "base": "", "otro": "/en/", "otro_nombre": "English",
  "title": "Valen Beach · Apartamento a pie de playa en Torrox Costa, Málaga",
  "meta": "Apartamento vacacional de 4 dormitorios para 10 personas, a 50 m de la playa de las Dunas, en Torrox Costa (Málaga). Piscina comunitaria, terraza y parking privado.",
  "nav": [("#descripcion", "Descripción"), ("#comodidades", "Comodidades"), ("#fotos", "Fotos"),
          ("#disponibilidad", "Disponibilidad"), ("#tarifas", "Tarifas"), ("#donde", "Dónde"), ("el-apartamento/", "El apartamento")],
  "eyebrow": "Tus vacaciones en la Torrox Costa", "h1": "Valen Beach", "cta": "Solicitar reserva por WhatsApp",
  "intro_h": "Relájate a pie de playa",
  "intro": ["Disfruta de este apartamento vacacional en Torrox Costa, Málaga, a pie de playa y junto a la zona protegida de las Dunas de la Carraca. Tiene capacidad para 10 personas y todas las comodidades de la moderna urbanización Duna Beach, con piscina comunitaria.",
            "Cuatro dormitorios y dos cuartos de baño en una sola planta baja con una gran terraza. Habitaciones espaciosas, un complejo residencial cuidado, la playa a pocos metros, sitios donde salir y actividades deportivas: un alojamiento ideal para pasar las vacaciones con familia o amigos."],
  "datos_h": "Datos",
  "contacto_h": "Contacto", "disp": "Disponible 24/7",
  "desc_h": "Descripción",
  "desc": ["Apartamento en Torrox Costa (Málaga, España) con piscina comunitaria, en una zona de playa y residencial, a unos 50 m de la playa de las Dunas.",
           "Cuatro dormitorios y dos cuartos de baño, en planta única."],
  "bloques": [
    ("Interior", ["Apartamento en planta única", "Salón con aire acondicionado, TV de 60″, wifi y TDT", "Antena satélite (TDT)", "Completamente equipado de electrodomésticos"]),
    ("Cocina", ["Cocina eléctrica, horno eléctrico, microondas, lavavajillas, frigorífico, cafetera, calentador de agua, batidora, tostador y exprimidor"]),
    ("Dormitorios y baños", ["1 dormitorio con cama de matrimonio, aire acondicionado y baño en suite", "1 dormitorio con cama de matrimonio, aire acondicionado y ventilador", "1 dormitorio con cama de matrimonio y una cama adicional tipo litera", "1 dormitorio con 3 camas individuales (200 × 105 cm), aire acondicionado y ventilador", "Baño en suite con lavabo, ducha-bañera, bidé e inodoro", "Cuarto de baño con lavabo, ducha-bañera, bidé e inodoro"]),
    ("Exterior", ["Piscina comunitaria", "Jardín comunitario con césped y árboles", "Zona exterior para sentarse", "Plaza de parking privada"]),
    ("Más información", ["Playa más cercana: Las Dunas (a menos de 100 m)", "Aeropuerto más cercano: Málaga (a menos de 60 km)", "No se admiten mascotas", "Muy apto para familias con niños"]),
    ("Incluido en el precio", ["Wifi", "Aspiradora, plancha y tabla de planchar", "Ropa de cama y toallas", "Entrada autónoma mediante llave electrónica", "Calefacción y aire acondicionado por bomba de calor"]),
    ("Con suplemento", ["Cuna", "Late check-in / check-out", "Reserva de taxis"]),
    ("Deporte", ["Tenis (a menos de 1000 m)", "Golf (a menos de 10 km)"]),
  ],
  "reg": "Número de identificación oficial de alojamiento",
  "com_h": "Comodidades",
  "com": ["Aire acondicionado (todas las habitaciones)", "Alojamiento en planta única", "Capacidad para 10 personas", "Bares y restaurantes a menos de 500 m", "Calefacción", "Pista de tenis a menos de 1 km", "Conexión a Internet", "Edificio con 3 plantas", "Jardín comunitario", "Lavadora", "Lavavajillas", "Microondas", "Parking privado", "Piscina comunitaria", "Playa a menos de 100 m", "Ropa de cama incluida en el precio", "Supermercado a menos de 500 m", "Televisión por cable/satélite", "Toallas"],
  "com_nota": "Las comodidades indicadas son orientativas. Se hace lo posible por mantener la información actualizada, pero pueden producirse cambios.",
  "fotos_h": "Fotos",
  "fotos": [("salon1.jpg", "Salón-comedor y cocina"), ("salon2.jpg", "Salón con zona de estar"), ("terraza.jpg", "Terraza"),
            ("dormitorio-suite.jpg", "Dormitorio con baño en suite"), ("dormitorio2.jpg", "Dormitorio con cama de matrimonio"),
            ("litera.jpg", "Dormitorio con litera"), ("dormitorio-individuales.jpg", "Dormitorio con tres camas individuales"), ("bano.jpg", "Cuarto de baño")],
  "disp_h": "Disponibilidad",
  "disp_nota": "Las fechas ocupadas proceden de nuestro calendario y se actualizan cada pocas horas; puede haber un pequeño desfase. La reserva se confirma siempre por WhatsApp.",
  "disp_sin": "El calendario no está disponible en este momento. Consúltanos las fechas por WhatsApp.",
  "meses": ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"],
  "dias": ["L", "M", "X", "J", "V", "S", "D"],
  "ocupado": "Ocupado", "libre": "Libre",
  "noche": "€/noche", "est": "Importe estimado de las noches: {t} € (a confirmar)", "estmsg": " Importe estimado: {t} €.",
  "solo": "Calendario de ocupación pendiente de conectar: de momento se muestran solo los precios orientativos por noche.",
  "tar_h": "Tarifas",
  "tar": [("Temporada baja", "desde 150 € por noche"), ("Temporada alta", "desde 200 € por noche")],
  "tar_nota": "Precios orientativos por noche; el importe final depende de las fechas y del número de personas. Consúltalo por WhatsApp.",
  "res_h": "Solicitar reserva",
  "res_p": "Dinos las fechas y cuántos sois, y te abrimos WhatsApp con el mensaje ya escrito. No hace falta registrarse y no se envía nada hasta que pulses «Enviar» en WhatsApp.",
  "f_in": "Entrada", "f_out": "Salida", "f_pers": "Personas", "f_btn": "Abrir WhatsApp",
  "wa_msg": "Hola, quisiera solicitar una reserva en Valen Beach (Torrox Costa)",
  "wa_msg_f": "Hola, quisiera solicitar una reserva en Valen Beach (Torrox Costa) del {a} al {b} para {n} personas. ¿Está disponible?",
  "donde_h": "Dónde está",
  "donde": "Urbanización Duna Beach 2 · Carretera de Almería 23b, 29770 Torrox (Málaga)",
  "mapa": "Ver en el mapa",
  "cita": "«Disfruta de unas vacaciones inolvidables en nuestra casa frente al mar, donde cada amanecer y atardecer se convierten en un espectáculo único de tranquilidad y belleza.»",
  "cita_a": "Antonio Valenzuela, propietario",
  "torrox_h": "Torrox Costa y El Morche",
  "torrox": ["Disfruta del mejor clima de Europa y de multitud de actividades en Torrox y alrededores.", "La playa de las Dunas, a pocos metros, es la mejor playa de la zona."],
  "res_hh": "Opiniones de huéspedes",
  "res_src": "Opiniones de huéspedes recogidas en Booking.com",
  "opiniones": [("Vanessa", "2024", "Un apartamento muy bonito y grande, al lado de la playa. Todo muy bien. Nos ha gustado mucho. Es tal cual las fotos. Lo recomiendo."),
                ("Irene (España)", "2024", "El apartamento es perfecto para una familia grande: cuatro habitaciones amplias y dos baños. El salón-cocina es muy grande y cómodo y la terraza es enorme. Nos encantó el apartamento y su ubicación frente al mar, en una zona tranquila. Repetiría sin duda."),
                ("Ana (España)", "2023", "Espacioso, con todo lo necesario para una estancia muy agradable. Está en una zona muy tranquila, pero a 5 minutos andando tienes restaurantes y servicios. La playa está al pie de la urbanización.")],
  "foot_leg": "Aviso legal", "foot_pri": "Privacidad", "foot_con": "Condiciones de reserva",
  "foot_tit": "Titular", "foot_reg": "Registro",
  "ap_title": "El apartamento · Valen Beach",
  "ap_desc": "Habitaciones, salón-cocina, terraza y baños del apartamento Valen Beach en Torrox Costa.",
  "ap_h": "El apartamento",
  "ap": [("Salón-cocina", "Amplio salón-comedor abierto a la cocina, de unos 40 m², con la cocina completamente equipada y menaje incluido. El salón cuenta con mobiliario para descansar y televisor."),
         ("Dormitorios", "Cuatro dormitorios amplios con armarios y escritorios. Todos cuentan con aire acondicionado y calefacción; uno de ellos con baño en suite."),
         ("Terraza", "Gran terraza de unos 30 m² para disfrutar del aire libre."),
         ("Baños", "Dos cuartos de baño completamente equipados."),
         ("Climatización", "Aire acondicionado por aerotermia con control bizonal de temperatura."),
         ("Ropa de cama y toallas", "Se proporciona ropa de cama y toallas para uso personal.")],
  "volver": "← Volver al inicio",
 },
 "en": {
  "lang": "en", "base": "/en", "otro": "/", "otro_nombre": "Español",
  "title": "Valen Beach · Beachfront apartment in Torrox Costa, Málaga",
  "meta": "Holiday apartment with 4 bedrooms for up to 10 guests, 50 m from Las Dunas beach in Torrox Costa (Málaga, Spain). Shared pool, terrace and private parking.",
  "nav": [("#descripcion", "Description"), ("#comodidades", "Amenities"), ("#fotos", "Photos"),
          ("#disponibilidad", "Availability"), ("#tarifas", "Rates"), ("#donde", "Location"), ("el-apartamento/", "The apartment")],
  "eyebrow": "Your holiday on the Torrox Costa", "h1": "Valen Beach", "cta": "Request a booking on WhatsApp",
  "intro_h": "Relax right by the beach",
  "intro": ["Enjoy this holiday apartment in Torrox Costa, Málaga, steps from the beach and next to the protected area of Dunas de la Carraca. It sleeps 10 and has all the comforts of the modern Duna Beach development, with a shared swimming pool.",
            "Four bedrooms and two bathrooms on a single ground floor with a large terrace. Spacious rooms, a well-kept residential complex, the beach a few metres away, places to go out and sports activities: an ideal place for a holiday with family or friends."],
  "datos_h": "Details",
  "contacto_h": "Contact", "disp": "Available 24/7",
  "desc_h": "Description",
  "desc": ["Apartment in Torrox Costa (Málaga, Spain) with a shared swimming pool, in a residential beach area about 50 m from Las Dunas beach.",
           "Four bedrooms and two bathrooms, all on one floor."],
  "bloques": [
    ("Inside", ["Single-floor apartment", "Living room with air conditioning, 60″ TV, wifi and digital TV", "Satellite antenna", "Fully equipped with appliances"]),
    ("Kitchen", ["Electric hob, electric oven, microwave, dishwasher, fridge, coffee maker, water heater, blender, toaster and juicer"]),
    ("Bedrooms and bathrooms", ["1 bedroom with a double bed, air conditioning and en-suite bathroom", "1 bedroom with a double bed, air conditioning and a fan", "1 bedroom with a double bed and an extra bunk-style bed", "1 bedroom with 3 single beds (200 × 105 cm), air conditioning and a fan", "En-suite bathroom with washbasin, bath-shower, bidet and toilet", "Bathroom with washbasin, bath-shower, bidet and toilet"]),
    ("Outside", ["Shared swimming pool", "Shared garden with lawn and trees", "Outdoor seating area", "Private parking space"]),
    ("More information", ["Nearest beach: Las Dunas (less than 100 m)", "Nearest airport: Málaga (less than 60 km)", "No pets allowed", "Very suitable for families with children"]),
    ("Included in the price", ["Wifi", "Vacuum cleaner, iron and ironing board", "Bed linen and towels", "Self check-in with an electronic key", "Heating and air conditioning by heat pump"]),
    ("Extra charge", ["Cot", "Late check-in / check-out", "Taxi booking"]),
    ("Sports", ["Tennis (less than 1000 m)", "Golf (less than 10 km)"]),
  ],
  "reg": "Official accommodation registration number",
  "com_h": "Amenities",
  "com": ["Air conditioning (all bedrooms)", "Single-floor accommodation", "Sleeps 10", "Bars and restaurants within 500 m", "Heating", "Tennis court within 1 km", "Internet connection", "3-storey building", "Shared garden", "Washing machine", "Dishwasher", "Microwave", "Private parking", "Shared swimming pool", "Beach within 100 m", "Bed linen included in the price", "Supermarket within 500 m", "Cable/satellite TV", "Towels"],
  "com_nota": "The amenities listed are for guidance. We do our best to keep the information up to date, but changes may occur.",
  "fotos_h": "Photos",
  "fotos": [("salon1.jpg", "Living-dining room and kitchen"), ("salon2.jpg", "Living room seating area"), ("terraza.jpg", "Terrace"),
            ("dormitorio-suite.jpg", "Bedroom with en-suite bathroom"), ("dormitorio2.jpg", "Bedroom with double bed"),
            ("litera.jpg", "Bedroom with bunk bed"), ("dormitorio-individuales.jpg", "Bedroom with three single beds"), ("bano.jpg", "Bathroom")],
  "disp_h": "Availability",
  "disp_nota": "Occupied dates come from our calendar and are refreshed every few hours, so there may be a short delay. Bookings are always confirmed by WhatsApp.",
  "disp_sin": "The calendar is not available right now. Ask us about dates on WhatsApp.",
  "meses": ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
  "dias": ["M", "T", "W", "T", "F", "S", "S"],
  "ocupado": "Booked", "libre": "Available",
  "noche": "€/night", "est": "Estimated total for the nights: €{t} (to be confirmed)", "estmsg": " Estimated total: €{t}.",
  "solo": "The occupancy calendar is not connected yet: for now only indicative nightly prices are shown.",
  "tar_h": "Rates",
  "tar": [("Low season", "from €150 per night"), ("High season", "from €200 per night")],
  "tar_nota": "Indicative prices per night; the final amount depends on dates and number of guests. Ask us on WhatsApp.",
  "res_h": "Request a booking",
  "res_p": "Tell us the dates and how many of you there are, and we open WhatsApp with the message already written. No registration needed and nothing is sent until you press “Send” in WhatsApp.",
  "f_in": "Check-in", "f_out": "Check-out", "f_pers": "Guests", "f_btn": "Open WhatsApp",
  "wa_msg": "Hello, I would like to request a booking at Valen Beach (Torrox Costa)",
  "wa_msg_f": "Hello, I would like to request a booking at Valen Beach (Torrox Costa) from {a} to {b} for {n} guests. Is it available?",
  "donde_h": "Location",
  "donde": "Urbanización Duna Beach 2 · Carretera de Almería 23b, 29770 Torrox (Málaga, Spain)",
  "mapa": "View on the map",
  "cita": "“Enjoy an unforgettable holiday in our house facing the sea, where every sunrise and sunset becomes a unique show of tranquillity and beauty.”",
  "cita_a": "Antonio Valenzuela, owner",
  "torrox_h": "Torrox Costa and El Morche",
  "torrox": ["Enjoy one of the best climates in Europe and plenty of activities in Torrox and the surrounding area.", "Las Dunas beach, just a few metres away, is the best beach in the area."],
  "res_hh": "Guest reviews",
  "res_src": "Guest reviews collected on Booking.com",
  "opiniones": [("Vanessa", "2024", "A very nice, big apartment right next to the beach. Everything was great. We loved it. It is just like the photos. I recommend it."),
                ("Irene (Spain)", "2024", "The apartment is perfect for a big family, it has 4 spacious rooms and two bathrooms. The living room/kitchen is very large and comfortable and the terrace is huge. Overall we found the apartment and the beach front location in a quiet area great. I would definitely repeat."),
                ("Ana (Spain)", "2023", "Spacious, with everything you need for a very pleasant stay. It is in a very quiet area, but a 5 min walk away you have restaurants and services. The beach at the foot of the urbanization.")],
  "foot_leg": "Legal notice (Spanish)", "foot_pri": "Privacy (Spanish)", "foot_con": "Booking conditions (Spanish)",
  "foot_tit": "Owner", "foot_reg": "Registration",
  "ap_title": "The apartment · Valen Beach",
  "ap_desc": "Bedrooms, living-kitchen, terrace and bathrooms of the Valen Beach apartment in Torrox Costa.",
  "ap_h": "The apartment",
  "ap": [("Living-kitchen", "A spacious living-dining room of about 40 m² open to the kitchen, which is fully equipped with kitchenware included. The living room has comfortable furniture and a TV."),
         ("Bedrooms", "Four spacious bedrooms with wardrobes and desks. All have air conditioning and heating; one has an en-suite bathroom."),
         ("Terrace", "A large terrace of about 30 m² to enjoy the outdoors."),
         ("Bathrooms", "Two fully equipped bathrooms."),
         ("Climate control", "Air conditioning by aerothermal heat pump with two-zone temperature control."),
         ("Bed linen and towels", "Bed linen and towels for personal use are provided.")],
  "volver": "← Back to home",
 },
}

CSS = """
:root{--bg:#fbfaf6;--fg:#1c2a33;--mut:#5a6a74;--acc:#0e6f9c;--acc2:#0a4f72;--sand:#efe7d6;--line:#dcd6c8;--card:#fff;--wa:#1f9d55}
@media (prefers-color-scheme:dark){:root:not([data-theme=light]){--bg:#10181d;--fg:#e8ecee;--mut:#9fb0ba;--acc:#6cc0e8;--acc2:#a5dcf5;--sand:#1c262c;--line:#2a3943;--card:#17222a;--wa:#35c076;color-scheme:dark}}
*{box-sizing:border-box}html{scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--fg);font:17px/1.65 system-ui,-apple-system,'Segoe UI',Roboto,sans-serif;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px))}
img{max-width:100%;display:block}
.wrap{max-width:1040px;margin:0 auto}
header.top{position:sticky;top:0;z-index:10;background:color-mix(in srgb,var(--bg) 92%,transparent);backdrop-filter:blur(8px);border-bottom:1px solid var(--line);margin:0 calc(-1*max(16px,env(safe-area-inset-left,0px)));padding:8px max(16px,env(safe-area-inset-left,0px))}
header.top .wrap{display:flex;gap:14px;align-items:center;justify-content:space-between;flex-wrap:wrap}
.logo{font:600 1.15rem Georgia,'Times New Roman',serif;letter-spacing:.03em;color:var(--fg);text-decoration:none}
nav{display:flex;gap:6px 16px;flex-wrap:wrap;font-size:.86rem;text-transform:uppercase;letter-spacing:.06em}
nav a{color:var(--mut);text-decoration:none;padding:4px 0}nav a:hover{color:var(--acc)}
.hero{position:relative;margin:0 calc(-1*max(16px,env(safe-area-inset-left,0px)));min-height:min(62vh,540px);display:grid;place-items:center;text-align:center;color:#fff;background:#0a3a52 url(/img/hero.jpg) center 55%/cover no-repeat}
.hero::before{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(5,30,45,.35),rgba(5,30,45,.5))}
.hero>div{position:relative;padding:40px 16px}
.eyebrow{text-transform:uppercase;letter-spacing:.3em;font-size:.8rem;opacity:.95}
h1{font:400 clamp(2.6rem,9vw,5rem)/1.05 Georgia,'Times New Roman',serif;margin:.2em 0 .5em;text-wrap:balance}
.btn{display:inline-block;background:var(--wa);color:#fff;text-decoration:none;padding:12px 22px;border-radius:999px;font-weight:600;border:0;cursor:pointer;font-size:1rem}
.btn:hover{filter:brightness(1.07)}
section{padding:56px 0 8px}
h2{font:400 clamp(1.7rem,4.5vw,2.4rem)/1.2 Georgia,'Times New Roman',serif;margin:0 0 .6em;text-wrap:balance}
h3{font-size:1rem;text-transform:uppercase;letter-spacing:.08em;color:var(--acc2);margin:1.4em 0 .3em}
.cols{display:grid;grid-template-columns:minmax(0,3fr) minmax(0,2fr);gap:36px}
@media(max-width:760px){.cols{grid-template-columns:minmax(0,1fr)}}
.card{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:16px 20px}
ul.ticks{list-style:none;margin:0;padding:0}ul.ticks li{padding:3px 0 3px 22px;position:relative}ul.ticks li::before{content:"✓";position:absolute;left:0;color:var(--acc)}
.grid2{columns:2 260px;column-gap:32px}.grid2 li{break-inside:avoid}
.gal{display:grid;grid-template-columns:repeat(auto-fill,minmax(230px,1fr));gap:10px}
.gal figure{margin:0}.gal img{width:100%;height:auto;aspect-ratio:4/3;object-fit:cover;border-radius:10px;background:var(--sand)}
.gal figcaption{font-size:.85rem;color:var(--mut);padding:4px 2px}
.band{background:var(--sand);margin:56px calc(-1*max(16px,env(safe-area-inset-left,0px))) 0;padding:48px max(16px,env(safe-area-inset-left,0px))}
.cita{display:grid;grid-template-columns:96px 1fr;gap:24px;align-items:center}
.cita img{width:96px;height:96px!important;border-radius:50%;object-fit:cover}
.cita p{font:italic 1.3rem/1.5 Georgia,serif;margin:0}.cita small{color:var(--mut)}
.rev{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:14px}
.rev .card p{margin:.2em 0 .6em}.rev small{color:var(--mut)}
.tarifas{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:14px}
.tarifas b{font:400 1.5rem Georgia,serif;display:block}
.meta{color:var(--mut);font-size:.88rem}
form.res{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:12px;align-items:end;margin-top:14px}
form.res label{font-size:.85rem;color:var(--mut);display:grid;gap:4px}
form.res input{font:inherit;padding:10px;border:1px solid var(--line);border-radius:8px;background:var(--card);color:var(--fg);width:100%}
.cal{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:16px}
.mes{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:10px 12px}
.mes h4{margin:0 0 6px;font-size:.95rem;text-transform:capitalize}
.dias{display:grid;grid-template-columns:repeat(7,1fr);gap:2px;text-align:center;font-size:.82rem}
.dias span{padding:5px 0;border-radius:4px}.dias .h{color:var(--mut);font-size:.72rem}
.dias .l{background:color-mix(in srgb,var(--wa) 18%,transparent)}.dias .o{background:color-mix(in srgb,#c0392b 28%,transparent);text-decoration:line-through;color:var(--mut)}
.dias .p{opacity:.35}.dias small{display:block;font-size:.62rem;color:var(--mut);line-height:1}.dias .n{background:color-mix(in srgb,var(--acc) 8%,transparent)}
footer{border-top:1px solid var(--line);margin-top:64px;padding:26px 0 40px;font-size:.88rem;color:var(--mut)}
footer a{color:var(--mut)}
a{color:var(--acc)}
.legal main{max-width:760px;margin:0 auto;padding:30px 0}
.legal h1{font-size:2rem}.legal h2{font-size:1.3rem;margin-top:1.6em}
.legal table{border-collapse:collapse;width:100%;display:block;overflow-x:auto}.legal td,.legal th{border:1px solid var(--line);padding:6px 10px;text-align:left;vertical-align:top}
"""

JS = """
(function(){
var L=window.VB||{},T=null;
function iso(d){return d.toISOString().slice(0,10);}
function precio(k){if(!T)return null;
 if(T.excepciones&&T.excepciones[k]!=null)return T.excepciones[k];
 var md=k.slice(5),ts=T.temporadas||[];
 for(var i=0;i<ts.length;i++){var rs=ts[i].rangos||[];for(var j=0;j<rs.length;j++){var r=rs[j];
  if(r[0]<=r[1]?(md>=r[0]&&md<=r[1]):(md>=r[0]||md<=r[1]))return ts[i].precio;}}
 return T.precio_base_noche;}
function total(a,b){if(!T||!a||!b)return null;var s=new Date(a+'T00:00:00Z'),e=new Date(b+'T00:00:00Z'),t=0;
 if(!(e>s))return null;for(var x=new Date(s);x<e;x.setUTCDate(x.getUTCDate()+1))t+=precio(iso(x));return t;}
function fmt(s){var p=s.split('-');return p[2]+'/'+p[1]+'/'+p[0];}
var B=window.VB_BASE||'';
var f=document.getElementById('resform');
var pT=fetch(B+'/tarifas.json',{cache:'no-store'}).then(function(r){return r.ok?r.json():null}).catch(function(){return null});
if(f){var est=document.getElementById('estimado');
 pT.then(function(t){T=t;});
 function act(){var t=total(f.a.value,f.b.value);if(est)est.textContent=t==null?'':L.est.replace('{t}',t);}
 f.a.addEventListener('change',act);f.b.addEventListener('change',act);
 f.addEventListener('submit',function(e){e.preventDefault();
  var a=f.a.value,b=f.b.value,n=f.n.value,m=(a&&b)?L.msgf.replace('{a}',fmt(a)).replace('{b}',fmt(b)).replace('{n}',n||'?'):L.msg,t=total(a,b);
  if(t!=null)m+=L.estmsg.replace('{t}',t);
  window.open('https://wa.me/'+L.tel+'?text='+encodeURIComponent(m),'_blank','noopener');});
 var hoy0=new Date().toISOString().slice(0,10);f.a.min=hoy0;f.b.min=hoy0;
 f.a.addEventListener('change',function(){f.b.min=f.a.value||hoy0;});}
var cal=document.getElementById('cal');
if(cal){
 Promise.all([fetch(B+'/disponibilidad.json',{cache:'no-store'}).then(function(r){return r.ok?r.json():null}).catch(function(){return null}),pT]).then(function(rs){
 var d=rs[0];T=rs[1];var hay=d&&d.actualizado&&Array.isArray(d.ocupado),oc={};
 var nn=document.getElementById('calnota');
 if(!hay&&!T){cal.textContent=L.sin;if(nn)nn.hidden=true;return;}
 if(!hay){if(nn)nn.textContent=L.solo;}
 if(hay)d.ocupado.forEach(function(r){var s=new Date(r[0]+'T00:00:00Z'),e=new Date(r[1]+'T00:00:00Z');
  for(var x=new Date(s);x<e;x.setUTCDate(x.getUTCDate()+1))oc[iso(x)]=1;});
 var hoy=new Date();hoy=new Date(Date.UTC(hoy.getFullYear(),hoy.getMonth(),hoy.getDate()));
 cal.innerHTML='';cal.className='cal';
 for(var i=0;i<12;i++){var m=new Date(Date.UTC(hoy.getUTCFullYear(),hoy.getUTCMonth()+i,1));
  var box=document.createElement('div');box.className='mes';
  box.innerHTML='<h4>'+L.meses[m.getUTCMonth()]+' '+m.getUTCFullYear()+'</h4>';
  var g=document.createElement('div');g.className='dias';
  L.dias.forEach(function(x){g.insertAdjacentHTML('beforeend','<span class="h">'+x+'</span>');});
  var off=(m.getUTCDay()+6)%7;for(var k=0;k<off;k++)g.insertAdjacentHTML('beforeend','<span></span>');
  var dm=new Date(Date.UTC(m.getUTCFullYear(),m.getUTCMonth()+1,0)).getUTCDate();
  for(var dd=1;dd<=dm;dd++){var dt=new Date(Date.UTC(m.getUTCFullYear(),m.getUTCMonth(),dd)),key=iso(dt);
   var c=dt<hoy?'p':(hay?(oc[key]?'o':'l'):'n'),p=precio(key);
   g.insertAdjacentHTML('beforeend','<span class="'+c+'" title="'+(c=='o'?L.oc:'')+'">'+dd+(p!=null&&c!='p'&&c!='o'?'<small>'+p+'€</small>':'')+'</span>');}
  box.appendChild(g);cal.appendChild(box);}
 });}
})();
"""


def e(s):
    return html.escape(s, quote=True)


def lista(items):
    return "<ul class='ticks'>" + "".join(f"<li>{e(i)}</li>" for i in items) + "</ul>"


def cabecera(t, titulo, desc, ruta_rel, canon, alt, legal=False):
    base = t["base"]
    nav = "".join(f'<a href="{(base + "/" if base else "/") + h if not h.startswith("#") else (base + "/" if base else "/") + h}">{e(n)}</a>' for h, n in t["nav"])
    return f"""<!doctype html><html lang="{t['lang']}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{e(titulo)}</title><meta name="description" content="{e(desc)}">
<link rel="canonical" href="{DATOS['dominio']}{canon}"><link rel="alternate" hreflang="es" href="{DATOS['dominio']}{alt['es']}"><link rel="alternate" hreflang="en" href="{DATOS['dominio']}{alt['en']}"><link rel="alternate" hreflang="x-default" href="{DATOS['dominio']}{alt['es']}">
<meta property="og:title" content="{e(titulo)}"><meta property="og:description" content="{e(desc)}"><meta property="og:image" content="{DATOS['dominio']}/img/hero.jpg"><meta property="og:type" content="website">
<style>{CSS}</style></head><body class="{'legal' if legal else ''}"><header class="top"><div class="wrap"><a class="logo" href="{base or ''}/">{DATOS['nombre']}</a><nav>{nav}<a href="{t['otro']}" hreflang="{'en' if t['lang']=='es' else 'es'}" lang="{'en' if t['lang']=='es' else 'es'}">{t['otro_nombre']}</a></nav></div></header>"""


def pie(t):
    es = t["lang"] == "es"
    return f"""<footer><div class="wrap"><p>{e(DATOS['nombre'])} · {t['foot_tit']}: {e(DATOS['titular'])} · NIF {DATOS['nif']} · {t['foot_reg']}: {DATOS['registro']}<br>{e(DATOS['domicilio'])} · <a href="mailto:{DATOS['email']}">{DATOS['email']}</a></p>
<p><a href="/aviso-legal-y-exencion-de-responsabilidad/">{t['foot_leg']}</a> · <a href="/politica-de-privacidad/">{t['foot_pri']}</a> · <a href="/condiciones/">{t['foot_con']}</a></p></div></footer>"""


def script(t):
    v = {"msg": t["wa_msg"], "msgf": t["wa_msg_f"], "tel": DATOS["tel_wa"], "meses": t["meses"], "dias": t["dias"],
         "oc": t["ocupado"], "li": t["libre"], "sin": t["disp_sin"], "est": t["est"], "estmsg": t["estmsg"], "solo": t["solo"]}
    return "<script>window.VB_BASE=" + json.dumps(BASE) + ";window.VB=" + json.dumps(v, ensure_ascii=False) + ";" + JS + "</script>"


def pagina_inicio(t):
    base = t["base"]
    wa = f"https://wa.me/{DATOS['tel_wa']}?text=" + __import__("urllib.parse", fromlist=["quote"]).quote(t["wa_msg"])
    bloques = "".join(f"<h3>{e(h)}</h3>{lista(l)}" for h, l in t["bloques"])
    fotos = "".join(f'<figure><img src="/img/{f}" alt="{e(c)}" loading="lazy" width="1600" height="1200"><figcaption>{e(c)}</figcaption></figure>' for f, c in t["fotos"])
    tar = "".join(f'<div class="card"><h3 style="margin-top:0">{e(a)}</h3><b>{e(b)}</b></div>' for a, b in t["tar"])
    ops = "".join(f'<div class="card"><p>{e(x)}</p><small>{e(a)} · {b}</small></div>' for a, b, x in t["opiniones"])
    es = t["lang"] == "es"
    alt = {"es": "/", "en": "/en/"}
    h = cabecera(t, t["title"], t["meta"], "", "/" if es else "/en/", alt)
    h += f"""<div class="hero"><div><div class="eyebrow">{e(t['eyebrow'])}</div><h1>{t['h1']}</h1><a class="btn" href="#reservar">{e(t['cta'])}</a></div></div>
<main class="wrap"><section id="inicio"><div class="cols"><div><h2>{e(t['intro_h'])}</h2>{''.join(f'<p>{e(p)}</p>' for p in t['intro'])}</div>
<div class="card"><h3 style="margin-top:0">{e(DATOS['nombre'])}</h3><p style="margin:.2em 0 1em">{e(DATOS['domicilio'])}</p><h3>{e(t['contacto_h'])}</h3><p style="margin:.2em 0">{t['disp']}<br><a href="tel:+{DATOS['tel_wa']}">{DATOS['tel_vis']}</a><br><a href="mailto:{DATOS['email']}">{DATOS['email']}</a><br><a href="{wa}" rel="noopener" target="_blank">WhatsApp</a></p></div></div></section>
<section id="descripcion"><h2>{e(t['desc_h'])}</h2>{''.join(f'<p>{e(p)}</p>' for p in t['desc'])}<div class="grid2">{bloques}</div><p class="meta"><b>{e(t['reg'])}:</b> {DATOS['registro']}</p></section>
<section id="comodidades"><h2>{e(t['com_h'])}</h2><ul class="ticks grid2">{''.join(f'<li>{e(c)}</li>' for c in t['com'])}</ul><p class="meta">{e(t['com_nota'])}</p></section>
<section id="fotos"><h2>{e(t['fotos_h'])}</h2><div class="gal">{fotos}</div></section>
<section id="disponibilidad"><h2>{e(t['disp_h'])}</h2><div id="cal" class="meta">…</div><p class="meta" id="calnota">{e(t['disp_nota'])}</p></section>
<section id="tarifas"><h2>{e(t['tar_h'])}</h2><div class="tarifas">{tar}</div><p class="meta">{e(t['tar_nota'])}</p></section>
<section id="reservar"><h2>{e(t['res_h'])}</h2><p>{e(t['res_p'])}</p>
<form class="res" id="resform"><label>{t['f_in']}<input type="date" name="a"></label><label>{t['f_out']}<input type="date" name="b"></label><label>{t['f_pers']}<input type="number" name="n" min="1" max="10" value="2"></label><button class="btn" type="submit">{t['f_btn']}</button></form><p class="meta" id="estimado"></p></section></main>
<div class="band"><div class="wrap cita"><img src="/img/antonio.jpg" alt="{e(DATOS['titular'])}" width="96" height="96"><div><p>{e(t['cita'])}</p><small>{e(t['cita_a'])}</small></div></div></div>
<main class="wrap"><section id="donde"><h2>{e(t['donde_h'])}</h2><div class="cols"><div><p>{e(t['donde'])}</p><p><a class="btn" style="background:var(--acc)" href="https://www.openstreetmap.org/search?query=Carretera%20de%20Almer%C3%ADa%2023%2C%20Torrox" target="_blank" rel="noopener">{e(t['mapa'])}</a></p><h3>{e(t['torrox_h'])}</h3>{''.join(f'<p>{e(p)}</p>' for p in t['torrox'])}</div><img src="/img/atardecer.jpg" alt="" loading="lazy" style="border-radius:12px"></div></section>
<section><h2>{e(t['res_hh'])}</h2><div class="rev">{ops}</div><p class="meta">{e(t['res_src'])}</p></section></main>"""
    h += pie(t) + script(t) + "</body></html>"
    return h


def pagina_apto(t):
    es = t["lang"] == "es"
    base = t["base"]
    alt = {"es": "/el-apartamento/", "en": "/en/el-apartamento/"}
    h = cabecera(t, t["ap_title"], t["ap_desc"], "", alt["es"] if es else alt["en"], alt)
    items = "".join(f"<h3>{e(a)}</h3><p>{e(b)}</p>" for a, b in t["ap"])
    fotos = "".join(f'<figure><img src="/img/{f}" alt="{e(c)}" loading="lazy" width="1600" height="1200"><figcaption>{e(c)}</figcaption></figure>' for f, c in t["fotos"])
    h += f"""<main class="wrap" style="padding-top:36px"><p><a href="{base or ''}/">{t['volver']}</a></p><h1 style="font-size:2.4rem;color:var(--fg)">{e(t['ap_h'])}</h1><div class="cols"><div>{items}</div><div class="card"><h3 style="margin-top:0">{e(t['tar_h'])}</h3>{''.join(f'<p style="margin:.3em 0"><b>{e(a)}</b>: {e(b)}</p>' for a, b in t['tar'])}<p class="meta">{e(t['tar_nota'])}</p><p><a class="btn" href="https://wa.me/{DATOS['tel_wa']}?text={__import__('urllib.parse', fromlist=['quote']).quote(t['wa_msg'])}" target="_blank" rel="noopener">{e(t['cta'])}</a></p></div></div><section><div class="gal">{fotos}</div></section></main>"""
    h += pie(t) + "</body></html>"
    return h


def legal(titulo, cuerpo, ruta):
    t = T["es"]
    alt = {"es": ruta, "en": ruta}
    h = cabecera(t, f"{titulo} · {DATOS['nombre']}", titulo, "", ruta, alt, legal=True)
    h += f"<main><h1>{e(titulo)}</h1>{cuerpo}</main>" + pie(t) + "</body></html>"
    return h


AVISO = f"""
<p class="meta">Última actualización: {DATOS['fecha']}.</p>
<h2>1. Datos identificativos</h2>
<p>En cumplimiento del artículo 10 de la Ley 34/2002, de servicios de la sociedad de la información y de comercio electrónico, se informa de que este sitio web es titularidad de:</p>
<p><b>Titular:</b> {DATOS['titular']}<br><b>NIF:</b> {DATOS['nif']}<br><b>Domicilio:</b> {DATOS['domicilio']}<br><b>Correo electrónico:</b> {DATOS['email']}<br><b>Teléfono:</b> {DATOS['tel_vis']}<br><b>Nombre comercial:</b> {DATOS['nombre']}<br><b>Actividad:</b> alquiler de alojamiento vacacional<br><b>Número de identificación oficial de alojamiento:</b> {DATOS['registro']}</p>
<h2>2. Objeto y condiciones de uso</h2>
<p>Este aviso regula el acceso y uso del sitio web. Acceder a él implica aceptar este aviso. Las condiciones de la reserva se recogen en las <a href="/condiciones/">Condiciones generales de reserva</a>.</p>
<h2>3. Propiedad intelectual</h2>
<p>Los textos, fotografías y diseño del sitio pertenecen al titular. No se permite su reproducción o comunicación pública sin autorización, salvo lo permitido por la ley.</p>
<h2>4. Responsabilidad</h2>
<p>La información sobre el alojamiento (comodidades, servicios, tarifas, disponibilidad) es orientativa y se mantiene actualizada en la medida de lo posible, pero puede cambiar. La reserva se formaliza únicamente cuando el titular la confirma. El titular no responde de los contenidos de sitios de terceros a los que se pueda enlazar.</p>
<h2>5. Legislación y jurisdicción</h2>
<p>Este aviso se rige por la legislación española. Si eres consumidor, son competentes los juzgados y tribunales de tu domicilio.</p>
"""

PRIVACIDAD = f"""
<p class="meta">Última actualización: {DATOS['fecha']}.</p>
<h2>1. Responsable</h2>
<p><b>{DATOS['titular']}</b>, NIF {DATOS['nif']}, con domicilio en {DATOS['domicilio']}. Contacto: {DATOS['email']}.</p>
<h2>2. Qué datos tratamos y para qué</h2>
<table><tr><th>Datos</th><th>Finalidad</th><th>Base jurídica</th></tr>
<tr><td>Los que nos facilites al contactar (nombre, teléfono, correo, fechas y número de personas) por WhatsApp, teléfono o correo electrónico</td><td>Responder a tu consulta y gestionar tu solicitud de reserva</td><td>Medidas precontractuales a petición tuya (art. 6.1.b RGPD)</td></tr>
<tr><td>Datos de los huéspedes que exige la normativa de registro de viajeros</td><td>Cumplir la obligación de registro documental e información a las autoridades</td><td>Obligación legal (art. 6.1.c)</td></tr>
<tr><td>Datos de pago y facturación, si los hay</td><td>Cobrar la estancia y cumplir las obligaciones fiscales</td><td>Ejecución del contrato y obligación legal (art. 6.1.b y 6.1.c)</td></tr></table>
<p>Esta web <b>no tiene formularios que guarden datos</b>, no usa cookies de seguimiento ni cargas de servicios de terceros. El formulario de «Solicitar reserva» solo prepara un mensaje y abre WhatsApp en tu dispositivo: no recibimos nada hasta que tú lo envías por WhatsApp.</p>
<h2>3. Destinatarios</h2>
<p>No cedemos tus datos a terceros salvo obligación legal (por ejemplo, a las administraciones competentes en materia de registro de viajeros o tributaria). Usamos WhatsApp (Meta) como canal de comunicación si tú nos escribes por ese medio, y el proveedor de alojamiento web para servir esta página, que puede registrar tu dirección IP por motivos técnicos y de seguridad.</p>
<h2>4. Conservación</h2>
<p>Conservamos las conversaciones y los datos de la solicitud el tiempo necesario para atenderla y, si hay reserva, durante los plazos que exijan las normas de registro, fiscales y mercantiles.</p>
<h2>5. Tus derechos</h2>
<p>Puedes ejercer los derechos de acceso, rectificación, supresión, oposición, limitación y portabilidad escribiendo a {DATOS['email']}. Si consideras que tus datos no se tratan correctamente, puedes reclamar ante la Agencia Española de Protección de Datos (<a href="https://www.aepd.es">www.aepd.es</a>).</p>
<h2>6. Cookies</h2>
<p>Este sitio no instala cookies ni usa herramientas de analítica o publicidad. Por eso no muestra un aviso de cookies.</p>
"""

if __name__ == "__main__":
    os.makedirs(SITE, exist_ok=True)

    def w(ruta, contenido):
        p = os.path.join(SITE, ruta.strip("/"), "index.html") if ruta != "/" else os.path.join(SITE, "index.html")
        os.makedirs(os.path.dirname(p), exist_ok=True)
        if BASE:
            import re
            contenido = re.sub(r'(href|src)="/(?!/)', r'="' + BASE + '/', contenido)
            contenido = contenido.replace("url(/img/", "url(" + BASE + "/img/").replace("fetch('/disponibilidad.json'", "fetch('" + BASE + "/disponibilidad.json'")
            contenido = contenido.replace('<meta charset="utf-8">', '<meta charset="utf-8"><meta name="robots" content="noindex,nofollow">', 1)
            contenido = contenido.replace(DATOS["nif"], "[oculto en la versión de prueba]").replace(DATOS["domicilio"], "Carretera de Almería 23b, 29770 Torrox (Málaga)")
            contenido = contenido.replace("</header>", '</header><div style="background:#fff4d6;color:#4a3b00;border-bottom:1px solid #e0b94a;padding:8px 16px;text-align:center;font-size:.9rem">Versión de prueba: precios y calendario provisionales; datos fiscales ocultos.</div>', 1)
        open(p, "w", encoding="utf8").write(contenido)

    w("/", pagina_inicio(T["es"]))
    w("/en/", pagina_inicio(T["en"]))
    w("/el-apartamento/", pagina_apto(T["es"]))
    w("/en/el-apartamento/", pagina_apto(T["en"]))
    w("/aviso-legal-y-exencion-de-responsabilidad/", legal("Aviso legal", AVISO, "/aviso-legal-y-exencion-de-responsabilidad/"))
    w("/politica-de-privacidad/", legal("Política de privacidad", PRIVACIDAD, "/politica-de-privacidad/"))
    # Condiciones: texto original del titular, conservado tal cual para su revision
    orig = open(os.path.join(ORIGEN, "condiciones.txt"), encoding="utf8").read().split("\n")
    cuerpo = ""
    for ln in orig[2:]:
        cuerpo += ("<h2>" + e(ln) + "</h2>") if (len(ln) < 60 and not ln.endswith(".")) else ("<p>" + e(ln) + "</p>")
    w("/condiciones/", legal("Condiciones generales de reserva", "<p class='meta'>Texto conservado de la web anterior; pendiente de revisión.</p>" + cuerpo, "/condiciones/"))
    import shutil
    shutil.copy(os.path.join(AQUI, "datos", "tarifas.json"), os.path.join(SITE, "tarifas.json"))
    dd = os.path.join(AQUI, "datos", "disponibilidad.json")
    if os.path.exists(dd):
        shutil.copy(dd, os.path.join(SITE, "disponibilidad.json"))
    else:
        open(os.path.join(SITE, "disponibilidad.json"), "w", encoding="utf8").write(json.dumps({"actualizado": None, "ocupado": []}))
    open(os.path.join(SITE, "robots.txt"), "w").write("User-agent: *\nAllow: /\nSitemap: https://valenbeach.com/sitemap.xml\n")
    urls = ["/", "/en/", "/el-apartamento/", "/en/el-apartamento/", "/aviso-legal-y-exencion-de-responsabilidad/", "/politica-de-privacidad/", "/condiciones/"]
    open(os.path.join(SITE, "sitemap.xml"), "w").write('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + "".join(f"<url><loc>https://valenbeach.com{u}</loc></url>" for u in urls) + "</urlset>")
    print("docs/ generado:", len(urls), "paginas")
