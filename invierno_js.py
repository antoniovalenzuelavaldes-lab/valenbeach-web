# -*- coding: utf-8 -*-
"""Textos del calendario interactivo y de los descuentos por estancia larga (los usa el JS de la web).
Los porcentajes, las noches y las fechas de los descuentos NO van aqui: vienen del panel de administracion.
EN/DE/FR/NL traducidos por Claude, sin revisar por nativos."""

JS_TXT = {
    "es": {"hint0": "Pulsa en el calendario el día de entrada y luego el de salida para solicitar tu reserva.",
           "hint1": "Entrada: {a}. Ahora pulsa el día de salida.",
           "hint2": "Del {a} al {b}: {n} noches. Completa la solicitud en el formulario de abajo.",
           "ocup": "Hay noches ocupadas entre esas fechas. Elige otro periodo.",
           "dto": "Descuento por estancia larga incluido: {p} %.",
           "dtoLinea": "Más de {n} noches: {p} % de descuento (del {a} al {b})."},
    "en": {"hint0": "Click the arrival day in the calendar, then the departure day, to request your booking.",
           "hint1": "Arrival: {a}. Now click the departure day.",
           "hint2": "From {a} to {b}: {n} nights. Complete your request in the form below.",
           "ocup": "Some nights between those dates are taken. Please choose another period.",
           "dto": "Long-stay discount included: {p}%.",
           "dtoLinea": "More than {n} nights: {p}% off (from {a} to {b})."},
    "de": {"hint0": "Klicken Sie im Kalender auf den Anreisetag und dann auf den Abreisetag, um Ihre Buchung anzufragen.",
           "hint1": "Anreise: {a}. Klicken Sie jetzt auf den Abreisetag.",
           "hint2": "Vom {a} bis {b}: {n} Nächte. Vervollständigen Sie die Anfrage im Formular unten.",
           "ocup": "Zwischen diesen Terminen sind einzelne Nächte belegt. Bitte wählen Sie einen anderen Zeitraum.",
           "dto": "Langzeitrabatt eingerechnet: {p} %.",
           "dtoLinea": "Mehr als {n} Nächte: {p} % Rabatt (vom {a} bis {b})."},
    "fr": {"hint0": "Cliquez dans le calendrier sur le jour d'arrivée, puis sur le jour de départ, pour demander votre réservation.",
           "hint1": "Arrivée : {a}. Cliquez maintenant sur le jour de départ.",
           "hint2": "Du {a} au {b} : {n} nuits. Complétez votre demande dans le formulaire ci-dessous.",
           "ocup": "Certaines nuits entre ces dates sont occupées. Choisissez une autre période.",
           "dto": "Réduction long séjour incluse : {p} %.",
           "dtoLinea": "Plus de {n} nuits : {p} % de réduction (du {a} au {b})."},
    "nl": {"hint0": "Klik in de kalender op de aankomstdag en daarna op de vertrekdag om uw boeking aan te vragen.",
           "hint1": "Aankomst: {a}. Klik nu op de vertrekdag.",
           "hint2": "Van {a} tot {b}: {n} nachten. Vul uw aanvraag in het formulier hieronder aan.",
           "ocup": "Enkele nachten tussen die data zijn bezet. Kies een andere periode.",
           "dto": "Korting voor langer verblijf inbegrepen: {p} %.",
           "dtoLinea": "Meer dan {n} nachten: {p} % korting (van {a} tot {b})."},
}
