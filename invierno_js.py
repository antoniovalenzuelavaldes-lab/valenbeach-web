# -*- coding: utf-8 -*-
"""Textos del calendario interactivo y de los descuentos por estancia larga (los usa el JS de la web).
Los porcentajes, las noches y las fechas de los descuentos NO van aqui: vienen del panel de administracion.
EN/DE/FR/NL traducidos por Claude, sin revisar por nativos."""

JS_TXT = {
    "es": {"hint0": "Pulsa en el calendario el día de entrada y luego el de salida para solicitar tu reserva.",
           "hint1": "Entrada: {a}. Ahora pulsa el día de salida.",
           "hint2": "Del {a} al {b}: {n} noches.",
           "resBtn": "Reservar estas fechas", "resClear": "Borrar selección",
           "ocup": "Hay noches ocupadas entre esas fechas. Elige otro periodo.",
           "dto": "Descuento por estancia larga incluido: {p} %.",
           "dtoLinea": "A partir de {n} noches: {p} % de descuento (del {a} al {b}).",
           "dtoAviso": "Aprovecha nuestros descuentos: con estancias de {n} noches o más tienes un {p} % de descuento."},
    "en": {"hint0": "Click the arrival day in the calendar, then the departure day, to request your booking.",
           "hint1": "Arrival: {a}. Now click the departure day.",
           "hint2": "From {a} to {b}: {n} nights.",
           "resBtn": "Book these dates", "resClear": "Clear selection",
           "ocup": "Some nights between those dates are taken. Please choose another period.",
           "dto": "Long-stay discount included: {p}%.",
           "dtoLinea": "{n} nights or more: {p}% off (from {a} to {b}).",
           "dtoAviso": "Take advantage of our discounts: stay {n} nights or more and get {p}% off."},
    "de": {"hint0": "Klicken Sie im Kalender auf den Anreisetag und dann auf den Abreisetag, um Ihre Buchung anzufragen.",
           "hint1": "Anreise: {a}. Klicken Sie jetzt auf den Abreisetag.",
           "hint2": "Vom {a} bis {b}: {n} Nächte.",
           "resBtn": "Diese Termine anfragen", "resClear": "Auswahl löschen",
           "ocup": "Zwischen diesen Terminen sind einzelne Nächte belegt. Bitte wählen Sie einen anderen Zeitraum.",
           "dto": "Langzeitrabatt eingerechnet: {p} %.",
           "dtoLinea": "Ab {n} Nächten: {p} % Rabatt (vom {a} bis {b}).",
           "dtoAviso": "Nutzen Sie unsere Rabatte: ab {n} Nächten erhalten Sie {p} % Rabatt."},
    "fr": {"hint0": "Cliquez dans le calendrier sur le jour d'arrivée, puis sur le jour de départ, pour demander votre réservation.",
           "hint1": "Arrivée : {a}. Cliquez maintenant sur le jour de départ.",
           "hint2": "Du {a} au {b} : {n} nuits.",
           "resBtn": "Réserver ces dates", "resClear": "Effacer la sélection",
           "ocup": "Certaines nuits entre ces dates sont occupées. Choisissez une autre période.",
           "dto": "Réduction long séjour incluse : {p} %.",
           "dtoLinea": "À partir de {n} nuits : {p} % de réduction (du {a} au {b}).",
           "dtoAviso": "Profitez de nos réductions : à partir de {n} nuits, {p} % de réduction."},
    "nl": {"hint0": "Klik in de kalender op de aankomstdag en daarna op de vertrekdag om uw boeking aan te vragen.",
           "hint1": "Aankomst: {a}. Klik nu op de vertrekdag.",
           "hint2": "Van {a} tot {b}: {n} nachten.",
           "resBtn": "Deze data aanvragen", "resClear": "Selectie wissen",
           "ocup": "Enkele nachten tussen die data zijn bezet. Kies een andere periode.",
           "dto": "Korting voor langer verblijf inbegrepen: {p} %.",
           "dtoLinea": "Vanaf {n} nachten: {p} % korting (van {a} tot {b}).",
           "dtoAviso": "Profiteer van onze kortingen: vanaf {n} nachten krijgt u {p} % korting."},
}


# Enlace directo al anuncio en Booking (sin parametros de seguimiento). El sufijo de idioma de la URL es el que usa Booking.
_BK = "https://www.booking.com/hotel/es/espectacular-apartamento-en-primera-linea-de-playa-torrox"
BOOKING = {
    "es": {"url": _BK + ".es.html", "texto": "¿Prefieres reservar en Booking? No hay problema.", "boton": "Ver el apartamento en Booking"},
    "en": {"url": _BK + ".en-gb.html", "texto": "Prefer to book on Booking.com? No problem.", "boton": "See the apartment on Booking.com"},
    "de": {"url": _BK + ".de.html", "texto": "Möchten Sie lieber über Booking.com buchen? Kein Problem.", "boton": "Unterkunft auf Booking.com ansehen"},
    "fr": {"url": _BK + ".fr.html", "texto": "Vous préférez réserver sur Booking.com ? Pas de problème.", "boton": "Voir l'appartement sur Booking.com"},
    "nl": {"url": _BK + ".nl.html", "texto": "Liever boeken via Booking.com? Geen probleem.", "boton": "Bekijk het appartement op Booking.com"},
}
