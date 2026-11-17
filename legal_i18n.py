# -*- coding: utf-8 -*-
"""Paginas legales (aviso legal, privacidad, condiciones de reserva) en EN, DE, FR y NL.
Son traducciones de cortesia del original en español (que prevalece en caso de discrepancia), hechas por Claude y SIN revision de un jurista ni de un nativo.
Los datos del titular se rellenan al generar la web (marcadores @...@); los datos fiscales no viven en el repositorio."""

RUTAS_LEGAL = {
    "aviso": {"es": "/aviso-legal-y-exencion-de-responsabilidad/", "en": "/en/legal-notice/", "de": "/de/impressum/", "fr": "/fr/mentions-legales/", "nl": "/nl/juridische-kennisgeving/"},
    "priv": {"es": "/politica-de-privacidad/", "en": "/en/privacy-policy/", "de": "/de/datenschutz/", "fr": "/fr/politique-de-confidentialite/", "nl": "/nl/privacybeleid/"},
    "cond": {"es": "/condiciones/", "en": "/en/booking-conditions/", "de": "/de/buchungsbedingungen/", "fr": "/fr/conditions-de-reservation/", "nl": "/nl/boekingsvoorwaarden/"},
}

FECHAS = {"es": "17 de noviembre de 2026", "en": "17 November 2026", "de": "17. November 2026", "fr": "17 novembre 2026", "nl": "17 november 2026"}

NOTA = {
    "en": 'Courtesy translation of the <a href="@orig@">Spanish original</a>. In case of any discrepancy, the Spanish version prevails. Last updated: @fecha@.',
    "de": 'Unverbindliche Übersetzung des <a href="@orig@">spanischen Originals</a>. Bei Abweichungen gilt die spanische Fassung. Letzte Aktualisierung: @fecha@.',
    "fr": 'Traduction de courtoisie de l\'<a href="@orig@">original en espagnol</a>. En cas de divergence, la version espagnole prévaut. Dernière mise à jour : @fecha@.',
    "nl": 'Vrijblijvende vertaling van het <a href="@orig@">Spaanse origineel</a>. Bij verschillen prevaleert de Spaanse versie. Laatst bijgewerkt: @fecha@.',
}

LEGAL = {
    # ------------------------------------------------------------------ ENGLISH
    "en": {
        "aviso": ("Legal notice", """
<h2>1. Identification details</h2>
<p>In compliance with Article 10 of Spanish Law 34/2002 on information society services and electronic commerce, this website is owned by:</p>
<p><b>Owner:</b> @titular@<br><b>Tax ID (NIF):</b> @nif@<br><b>Address:</b> @domicilio@<br><b>Email:</b> @email@<br><b>Telephone:</b> @tel@<br><b>Trade name:</b> @nombre@<br><b>Activity:</b> holiday accommodation rental<br><b>Official accommodation registration number:</b> @registro@</p>
<h2>2. Purpose and terms of use</h2>
<p>This notice governs access to and use of the website. Accessing it means accepting this notice. The terms of booking are set out in the <a href="@r_cond@">General booking conditions</a>.</p>
<h2>3. Intellectual property</h2>
<p>The texts, photographs and design of the site belong to the owner. They may not be reproduced or communicated to the public without authorisation, except as permitted by law.</p>
<h2>4. Liability</h2>
<p>The information about the accommodation (amenities, services, rates, availability) is indicative and is kept up to date as far as possible, but it may change. A booking is only formalised when the owner confirms it. The owner is not responsible for the content of third-party sites that may be linked to.</p>
<h2>5. Applicable law and jurisdiction</h2>
<p>This notice is governed by Spanish law. If you are a consumer, the courts of your place of residence have jurisdiction.</p>
"""),
        "priv": ("Privacy policy", """
<h2>1. Controller</h2>
<p><b>@titular@</b>, tax ID (NIF) @nif@, with address at @domicilio@. Contact: @email@.</p>
<h2>2. What data we process and why</h2>
<table><tr><th>Data</th><th>Purpose</th><th>Legal basis</th></tr>
<tr><td>What you give us when you contact us (name, telephone, email, dates and number of guests) by WhatsApp, telephone or email</td><td>To answer your enquiry and handle your booking request</td><td>Pre-contractual measures at your request (Art. 6(1)(b) GDPR)</td></tr>
<tr><td>Guest data required by the traveller registration rules (name, ID document and vehicle registration number)</td><td>To comply with the legal obligation to keep a guest register and report to the authorities</td><td>Legal obligation (Art. 6(1)(c))</td></tr>
<tr><td>Payment and invoicing data, if any</td><td>To collect payment for the stay and meet tax obligations</td><td>Performance of the contract and legal obligation (Art. 6(1)(b) and 6(1)(c))</td></tr><tr><td>What you give us in the email request form (name, email, optional telephone, dates and message)</td><td>To answer your booking request</td><td>Pre-contractual measures at your request (Art. 6(1)(b) GDPR)</td></tr>
<tr><td>Technical data about your visit (page, referring site, country, browser and screen size), without IP address or cookies</td><td>To measure how the website is used and improve it</td><td>Legitimate interest (Art. 6(1)(f) GDPR)</td></tr></table>
<p>This website <b>has no forms that store data</b> and <b>does not use cookies</b>. To know how many people visit it we use <b>GoatCounter</b>, a cookie-free statistics service that does not store your IP address or identify you, and that is not activated if your browser sends a "do not track" signal. The "Request a booking" form only prepares a message and opens WhatsApp on your device: we receive nothing until you send it through WhatsApp.</p>
<h2>3. Recipients</h2>
<p>We do not share your data with third parties except where legally required (for example, with the authorities responsible for traveller registration or taxation). We use WhatsApp (Meta) as a communication channel if you write to us that way, and the web hosting provider to serve this page, which may record your IP address for technical and security reasons.</p>
<p>For visit statistics we use GoatCounter, which does not receive your email or any data you give us by WhatsApp or email.</p>
<p>The availability calendar and the rates are loaded from our own service hosted on Cloudflare, which may record your IP address for technical and security reasons; it receives no personal data from you.</p>
<p>The email request form sends your message to our mailbox through a Cloudflare service (which only forwards it and does not store it); we receive it in our inbox, where it is kept like any other email.</p>
<h2>4. Retention</h2>
<p>We keep conversations and request data for as long as needed to deal with the request and, if a booking is made, for the periods required by registration, tax and commercial rules.</p>
<h2>5. Your rights</h2>
<p>You can exercise your rights of access, rectification, erasure, objection, restriction and portability by writing to @email@. If you believe your data is not being handled correctly, you can lodge a complaint with the Spanish Data Protection Agency (<a href="https://www.aepd.es">www.aepd.es</a>).</p>
<h2>6. Cookies</h2>
<p>This site does not install cookies. Visits are measured with GoatCounter, without cookies, without advertising and without storing the IP address; for that reason it does not show a cookie banner. If your browser sends a "do not track" signal, your visit is not even counted.</p>
"""),
        "cond": ("General booking conditions", """
<p>These conditions govern the short-stay rental of the apartment <b>@nombre@</b> in Torrox Costa (Málaga), official accommodation registration number <b>@registro@</b>. They are complemented by the <a href="@r_aviso@">legal notice</a> and the <a href="@r_priv@">privacy policy</a>.</p>
<h2>1. Who rents</h2>
<p>@titular@, tax ID (NIF) @nif@, with address at @domicilio@. Contact: @email@ · @tel@ (also by WhatsApp).</p>
<h2>2. Request and confirmation of the booking</h2>
<p>Requests are made by WhatsApp, email or telephone. <b>A request is not a booking</b>: the booking is confirmed when the owner accepts it in writing and the deposit indicated below is received. The maximum capacity of the accommodation is <b>10 people</b>. Pets are not allowed.</p>
<h2>3. Price</h2>
<ul><li>The price is per night and <b>includes VAT</b>. Current rates are shown on the <a href="@r_tarifas@">home page</a>.</li>
<li>The <b>minimum stay</b> is 2 nights.</li>
<li><b>Final cleaning</b> is included in the price, as are bed linen, towels and wifi.</li>
<li>An electricity allowance of <b>50 kWh per week</b> is included.</li></ul>
<h2>4. Deposit and payment</h2>
<p>To confirm the booking, a <b>deposit of €50</b> is paid, which is <b>deducted from the final price</b>. The rest of the price is paid in the way and on the date agreed when the booking is confirmed. Payment methods are communicated on confirmation; they are not published on this website.</p>
<h2>5. Security deposit</h2>
<p>Before arrival the guest hands over a <b>security deposit of €400</b> as a guarantee. It is returned <b>after checking the condition of the apartment</b>, on the day of departure or at the latest within the following 3 days. Any damage or additional charges under section 10 will be deducted from the security deposit where applicable.</p>
<h2>6. Cancellation</h2>
<p>The cancellation policy is <b>flexible</b>: you can cancel <b>up to 1 week (7 days) before the arrival date</b>. To cancel, just notify us by WhatsApp or email. If you cancel within that week, what was agreed when the booking was confirmed applies.</p>
<h2>7. Right of withdrawal</h2>
<p>As this is an accommodation service with a specific date of performance, the <b>14-day statutory right of withdrawal does not apply</b> (Article 103(l) of the Spanish consolidated text of the General Law for the Protection of Consumers and Users). The cancellation policy in section 6 applies.</p>
<h2>8. Arrival and departure</h2>
<ul><li><b>Arrival</b>: from 4:00 pm to 9:00 pm on the day of arrival. Earlier or later arrival must be agreed in advance and may carry an extra charge.</li>
<li><b>Departure</b>: by 11:00 am at the latest on the day of departure. A later departure must be agreed in advance and may carry an extra charge.</li>
<li>Check-in is self-service: the arrival instructions are sent to the guest once the booking is confirmed.</li>
<li>On leaving, the guest leaves the apartment locked with the keys inside, and notifies us by WhatsApp.</li></ul>
<h2>9. Guest data</h2>
<p>Before arrival the guest must send the <b>name and ID document of all occupants</b>, and the <b>registration number of the vehicle</b> using the parking space. This is a legal traveller-registration obligation; see the <a href="@r_priv@">privacy policy</a>.</p>
<h2>10. Additional charges</h2>
<ul><li><b>Electricity</b>: consumption above 50 kWh per week is charged at <b>€0.45 per kWh</b>. The meter can be read next to the front door.</li>
<li><b>Arrival or departure outside the agreed hours</b>: on request.</li>
<li><b>Cot</b>: €1 per day.</li>
<li><b>Lost keys</b>: the physical key is copy-protected and losing it means replacing the whole lock (<b>€150</b>). Losing a magnetic key costs <b>€20</b>.</li>
<li>Additional services, with price and availability on request: bicycle hire, and hire of parasol and beach chairs.</li></ul>
<h2>11. Rules of use</h2>
<ul><li><b>Smoking</b> is not allowed in the apartment.</li>
<li><b>Parties are strictly forbidden</b> in the community. If a dinner runs past midnight, it must continue inside the apartment.</li>
<li>Rubbish must be put in the bin outside the residential complex before departure.</li>
<li>The <b>rules of the owners' community</b> must be followed; they are given to the guest.</li>
<li>Air conditioning must be used in moderation and only when you are at home.</li>
<li>The towel sets are for indoor use and must not be taken to the beach.</li></ul>
<h2>12. Guest's responsibility</h2>
<p>The guest is responsible for any damage caused to the apartment, the furniture or the common areas, and for breaches of the community rules. The owner may terminate the stay if the rules of use are seriously breached.</p>
<h2>13. Applicable law and complaints</h2>
<p>Spanish law. For any complaint, write to @email@. If you are a consumer, the courts of your place of residence have jurisdiction.</p>
"""),
    },
    # ------------------------------------------------------------------ DEUTSCH
    "de": {
        "aviso": ("Impressum und rechtliche Hinweise", """
<h2>1. Angaben zum Anbieter</h2>
<p>In Erfüllung von Artikel 10 des spanischen Gesetzes 34/2002 über Dienste der Informationsgesellschaft und den elektronischen Geschäftsverkehr wird mitgeteilt, dass diese Website betrieben wird von:</p>
<p><b>Inhaber:</b> @titular@<br><b>Steuernummer (NIF):</b> @nif@<br><b>Anschrift:</b> @domicilio@<br><b>E-Mail:</b> @email@<br><b>Telefon:</b> @tel@<br><b>Handelsname:</b> @nombre@<br><b>Tätigkeit:</b> Vermietung von Ferienunterkünften<br><b>Amtliche Registriernummer der Unterkunft:</b> @registro@</p>
<h2>2. Gegenstand und Nutzungsbedingungen</h2>
<p>Dieser Hinweis regelt den Zugang zur Website und ihre Nutzung. Mit dem Aufruf der Website akzeptieren Sie diesen Hinweis. Die Buchungsbedingungen finden Sie in den <a href="@r_cond@">Allgemeinen Buchungsbedingungen</a>.</p>
<h2>3. Geistiges Eigentum</h2>
<p>Die Texte, Fotografien und das Design der Website gehören dem Inhaber. Ihre Vervielfältigung oder öffentliche Wiedergabe ist ohne Genehmigung nicht gestattet, soweit das Gesetz nichts anderes erlaubt.</p>
<h2>4. Haftung</h2>
<p>Die Angaben zur Unterkunft (Ausstattung, Leistungen, Preise, Verfügbarkeit) sind unverbindlich und werden nach Möglichkeit aktuell gehalten, können sich aber ändern. Eine Buchung kommt erst zustande, wenn der Inhaber sie bestätigt. Der Inhaber haftet nicht für Inhalte verlinkter Seiten Dritter.</p>
<h2>5. Anwendbares Recht und Gerichtsstand</h2>
<p>Dieser Hinweis unterliegt spanischem Recht. Sind Sie Verbraucher, sind die Gerichte an Ihrem Wohnsitz zuständig.</p>
"""),
        "priv": ("Datenschutzerklärung", """
<h2>1. Verantwortlicher</h2>
<p><b>@titular@</b>, Steuernummer (NIF) @nif@, mit Anschrift @domicilio@. Kontakt: @email@.</p>
<h2>2. Welche Daten wir verarbeiten und wozu</h2>
<table><tr><th>Daten</th><th>Zweck</th><th>Rechtsgrundlage</th></tr>
<tr><td>Angaben, die Sie uns bei der Kontaktaufnahme (Name, Telefon, E-Mail, Daten und Personenzahl) per WhatsApp, Telefon oder E-Mail mitteilen</td><td>Beantwortung Ihrer Anfrage und Bearbeitung Ihrer Buchungsanfrage</td><td>Vorvertragliche Maßnahmen auf Ihre Anfrage (Art. 6 Abs. 1 lit. b DSGVO)</td></tr>
<tr><td>Gästedaten, die die Meldevorschriften für Reisende verlangen (Name, Ausweisdokument und Kfz-Kennzeichen)</td><td>Erfüllung der gesetzlichen Pflicht zur Gästeregistrierung und Mitteilung an die Behörden</td><td>Rechtliche Verpflichtung (Art. 6 Abs. 1 lit. c)</td></tr>
<tr><td>Zahlungs- und Rechnungsdaten, falls vorhanden</td><td>Einzug des Aufenthaltspreises und Erfüllung steuerlicher Pflichten</td><td>Vertragserfüllung und rechtliche Verpflichtung (Art. 6 Abs. 1 lit. b und c)</td></tr><tr><td>Angaben, die Sie uns im Formular für die Anfrage per E-Mail mitteilen (Name, E-Mail, optional Telefon, Daten und Nachricht)</td><td>Beantwortung Ihrer Buchungsanfrage</td><td>Vorvertragliche Maßnahmen auf Ihre Anfrage (Art. 6 Abs. 1 lit. b DSGVO)</td></tr>
<tr><td>Technische Daten Ihres Besuchs (Seite, Herkunftswebsite, Land, Browser und Bildschirmgröße), ohne IP-Adresse und ohne Cookies</td><td>Messung der Nutzung der Website, um sie zu verbessern</td><td>Berechtigtes Interesse (Art. 6 Abs. 1 lit. f DSGVO)</td></tr></table>
<p>Diese Website <b>hat keine Formulare, die Daten speichern</b>, und <b>verwendet keine Cookies</b>. Um zu wissen, wie viele Personen sie besuchen, nutzen wir <b>GoatCounter</b>, einen Statistikdienst ohne Cookies, der Ihre IP-Adresse nicht speichert und Sie nicht identifiziert und der nicht aktiviert wird, wenn Ihr Browser „Do Not Track“ signalisiert. Das Formular „Buchung anfragen“ bereitet nur eine Nachricht vor und öffnet WhatsApp auf Ihrem Gerät: Wir erhalten nichts, bis Sie sie über WhatsApp senden.</p>
<h2>3. Empfänger</h2>
<p>Wir geben Ihre Daten nicht an Dritte weiter, außer bei gesetzlicher Verpflichtung (zum Beispiel an die für die Gästeregistrierung oder das Steuerwesen zuständigen Behörden). Wir nutzen WhatsApp (Meta) als Kommunikationskanal, wenn Sie uns darüber schreiben, sowie den Hosting-Anbieter, um diese Seite auszuliefern; dieser kann Ihre IP-Adresse aus technischen und Sicherheitsgründen protokollieren.</p>
<p>Für die Besucherstatistik nutzen wir GoatCounter, das weder Ihre E-Mail-Adresse noch Daten erhält, die Sie uns per WhatsApp oder E-Mail mitteilen.</p>
<p>Der Verfügbarkeitskalender und die Preise werden von einem eigenen, bei Cloudflare gehosteten Dienst geladen, der Ihre IP-Adresse aus technischen und Sicherheitsgründen protokollieren kann; er erhält keine personenbezogenen Daten von Ihnen.</p>
<p>Das Formular für die Anfrage per E-Mail sendet Ihre Nachricht über einen Cloudflare-Dienst (der sie nur weiterleitet und nicht speichert) an unser Postfach; wir erhalten sie in unserem Posteingang, wo sie wie jede andere E-Mail aufbewahrt wird.</p>
<h2>4. Speicherdauer</h2>
<p>Wir bewahren die Unterhaltungen und die Daten der Anfrage so lange auf, wie es zur Bearbeitung erforderlich ist, und, falls eine Buchung zustande kommt, für die nach Melde-, Steuer- und Handelsvorschriften vorgeschriebenen Fristen.</p>
<h2>5. Ihre Rechte</h2>
<p>Sie können Ihre Rechte auf Auskunft, Berichtigung, Löschung, Widerspruch, Einschränkung und Datenübertragbarkeit ausüben, indem Sie an @email@ schreiben. Wenn Sie der Ansicht sind, dass Ihre Daten nicht ordnungsgemäß verarbeitet werden, können Sie sich bei der spanischen Datenschutzbehörde (Agencia Española de Protección de Datos, <a href="https://www.aepd.es">www.aepd.es</a>) beschweren.</p>
<h2>6. Cookies</h2>
<p>Diese Website setzt keine Cookies. Besuche werden mit GoatCounter gemessen, ohne Cookies, ohne Werbung und ohne Speicherung der IP-Adresse; deshalb zeigt sie kein Cookie-Banner. Wenn Ihr Browser „Do Not Track“ signalisiert, wird Ihr Besuch nicht einmal gezählt.</p>
"""),
        "cond": ("Allgemeine Buchungsbedingungen", """
<p>Diese Bedingungen regeln die Kurzzeitvermietung der Wohnung <b>@nombre@</b> in Torrox Costa (Málaga) mit der amtlichen Registriernummer <b>@registro@</b>. Sie werden ergänzt durch das <a href="@r_aviso@">Impressum</a> und die <a href="@r_priv@">Datenschutzerklärung</a>.</p>
<h2>1. Vermieter</h2>
<p>@titular@, Steuernummer (NIF) @nif@, mit Anschrift @domicilio@. Kontakt: @email@ · @tel@ (auch per WhatsApp).</p>
<h2>2. Anfrage und Bestätigung der Buchung</h2>
<p>Die Anfrage erfolgt per WhatsApp, E-Mail oder Telefon. <b>Eine Anfrage ist keine Buchung</b>: Die Buchung ist bestätigt, wenn der Inhaber sie schriftlich annimmt und die unten genannte Anzahlung eingegangen ist. Die maximale Belegung der Unterkunft beträgt <b>10 Personen</b>. Haustiere sind nicht erlaubt.</p>
<h2>3. Preis</h2>
<ul><li>Der Preis gilt pro Nacht und <b>enthält die Mehrwertsteuer</b>. Die aktuellen Preise finden Sie auf der <a href="@r_tarifas@">Startseite</a>.</li>
<li>Der <b>Mindestaufenthalt</b> beträgt 2 Nächte.</li>
<li>Die <b>Endreinigung</b> ist im Preis enthalten, ebenso Bettwäsche, Handtücher und WLAN.</li>
<li>Enthalten ist ein Stromverbrauch von <b>50 kWh pro Woche</b>.</li></ul>
<h2>4. Anzahlung und Zahlungsweise</h2>
<p>Zur Bestätigung der Buchung wird eine <b>Anzahlung von 50 €</b> geleistet, die <b>vom Endpreis abgezogen</b> wird. Der Restbetrag wird in der Form und zu dem Termin gezahlt, die bei der Bestätigung der Buchung vereinbart werden. Die Zahlungsmöglichkeiten werden bei der Bestätigung mitgeteilt; sie werden auf dieser Website nicht veröffentlicht.</p>
<h2>5. Kaution</h2>
<p>Vor der Anreise hinterlegt der Gast eine <b>Kaution von 400 €</b> als Sicherheit. Sie wird <b>nach Prüfung des Zustands der Wohnung</b> am Abreisetag oder spätestens innerhalb der folgenden 3 Tage zurückgezahlt. Von der Kaution werden gegebenenfalls Schäden oder zusätzliche Kosten gemäß Abschnitt 10 abgezogen.</p>
<h2>6. Stornierung</h2>
<p>Die Stornierungsbedingungen sind <b>flexibel</b>: Sie können <b>bis 1 Woche (7 Tage) vor dem Anreisetag</b> stornieren. Zum Stornieren genügt eine Mitteilung per WhatsApp oder E-Mail. Bei einer Stornierung innerhalb dieser Woche gilt, was bei der Bestätigung der Buchung vereinbart wurde.</p>
<h2>7. Widerrufsrecht</h2>
<p>Da es sich um eine Beherbergungsleistung mit einem bestimmten Leistungstermin handelt, <b>besteht das gesetzliche 14-tägige Widerrufsrecht nicht</b> (Artikel 103 Buchst. l des spanischen Gesetzestextes zum allgemeinen Verbraucherschutzgesetz). Es gelten die Stornierungsbedingungen in Abschnitt 6.</p>
<h2>8. An- und Abreise</h2>
<ul><li><b>Anreise</b>: von 16:00 bis 21:00 Uhr am Anreisetag. Eine frühere oder spätere Anreise muss angefragt werden und kann zusätzliche Kosten verursachen.</li>
<li><b>Abreise</b>: spätestens um 11:00 Uhr am Abreisetag. Eine spätere Abreise muss angefragt werden und kann zusätzliche Kosten verursachen.</li>
<li>Der Zugang erfolgt selbstständig: Die Anreiseinformationen werden dem Gast nach der Buchungsbestätigung zugesandt.</li>
<li>Bei der Abreise lässt der Gast die Wohnung verschlossen und die Schlüssel in der Wohnung und meldet sich per WhatsApp.</li></ul>
<h2>9. Daten der Gäste</h2>
<p>Vor der Anreise muss der Gast <b>Name und Ausweisdokument aller Personen</b> sowie das <b>Kfz-Kennzeichen</b> des Fahrzeugs, das den Stellplatz nutzt, mitteilen. Dies ist eine gesetzliche Meldepflicht für Reisende; siehe die <a href="@r_priv@">Datenschutzerklärung</a>.</p>
<h2>10. Zusätzliche Kosten</h2>
<ul><li><b>Strom</b>: Verbrauch über 50 kWh pro Woche wird mit <b>0,45 € pro kWh</b> berechnet. Der Zähler kann neben der Eingangstür abgelesen werden.</li>
<li><b>An- oder Abreise außerhalb der Zeiten</b>: auf Anfrage.</li>
<li><b>Kinderbett</b>: 1 € pro Tag.</li>
<li><b>Schlüsselverlust</b>: Der physische Schlüssel ist kopiergeschützt; sein Verlust erfordert den Austausch des gesamten Schlosses (<b>150 €</b>). Der Verlust eines Magnetschlüssels kostet <b>20 €</b>.</li>
<li>Zusatzleistungen mit Preis und Verfügbarkeit auf Anfrage: Fahrradverleih sowie Verleih von Sonnenschirm und Strandstühlen.</li></ul>
<h2>11. Nutzungsregeln</h2>
<ul><li>In der Wohnung ist das <b>Rauchen</b> nicht erlaubt.</li>
<li><b>Partys sind in der Wohnanlage streng verboten.</b> Zieht sich ein Abendessen über Mitternacht hinaus, muss es in der Wohnung fortgesetzt werden.</li>
<li>Der Müll wird vor der Abreise in den Container außerhalb der Wohnanlage gebracht.</li>
<li>Die <b>Regeln der Eigentümergemeinschaft</b> sind verbindlich; sie werden dem Gast ausgehändigt.</li>
<li>Die Klimaanlage ist sparsam und nur bei Anwesenheit zu nutzen.</li>
<li>Die Handtuchsets sind für die Nutzung im Haus bestimmt und dürfen nicht an den Strand mitgenommen werden.</li></ul>
<h2>12. Verantwortung des Gastes</h2>
<p>Der Gast haftet für Schäden, die er an der Wohnung, der Einrichtung oder den Gemeinschaftsbereichen verursacht, sowie für Verstöße gegen die Regeln der Eigentümergemeinschaft. Der Inhaber kann den Aufenthalt beenden, wenn die Nutzungsregeln schwerwiegend verletzt werden.</p>
<h2>13. Anwendbares Recht und Beschwerden</h2>
<p>Spanisches Recht. Für Beschwerden schreiben Sie an @email@. Sind Sie Verbraucher, sind die Gerichte an Ihrem Wohnsitz zuständig.</p>
"""),
    },
    # ------------------------------------------------------------------ FRANÇAIS
    "fr": {
        "aviso": ("Mentions légales", """
<h2>1. Informations d'identification</h2>
<p>Conformément à l'article 10 de la loi espagnole 34/2002 sur les services de la société de l'information et le commerce électronique, il est indiqué que ce site web appartient à :</p>
<p><b>Titulaire :</b> @titular@<br><b>Numéro fiscal (NIF) :</b> @nif@<br><b>Adresse :</b> @domicilio@<br><b>E-mail :</b> @email@<br><b>Téléphone :</b> @tel@<br><b>Nom commercial :</b> @nombre@<br><b>Activité :</b> location d'hébergement de vacances<br><b>Numéro officiel d'enregistrement du logement :</b> @registro@</p>
<h2>2. Objet et conditions d'utilisation</h2>
<p>Ces mentions régissent l'accès au site et son utilisation. Y accéder implique de les accepter. Les conditions de réservation figurent dans les <a href="@r_cond@">Conditions générales de réservation</a>.</p>
<h2>3. Propriété intellectuelle</h2>
<p>Les textes, photographies et la conception du site appartiennent au titulaire. Leur reproduction ou communication au public n'est pas autorisée sans accord, sauf dans les limites permises par la loi.</p>
<h2>4. Responsabilité</h2>
<p>Les informations sur le logement (équipements, services, tarifs, disponibilités) sont données à titre indicatif et mises à jour autant que possible, mais elles peuvent changer. Une réservation n'est formalisée que lorsque le titulaire la confirme. Le titulaire n'est pas responsable du contenu des sites tiers vers lesquels des liens peuvent renvoyer.</p>
<h2>5. Droit applicable et juridiction</h2>
<p>Ces mentions sont régies par le droit espagnol. Si vous êtes consommateur, les tribunaux de votre domicile sont compétents.</p>
"""),
        "priv": ("Politique de confidentialité", """
<h2>1. Responsable du traitement</h2>
<p><b>@titular@</b>, numéro fiscal (NIF) @nif@, domicilié à @domicilio@. Contact : @email@.</p>
<h2>2. Quelles données nous traitons et pourquoi</h2>
<table><tr><th>Données</th><th>Finalité</th><th>Base juridique</th></tr>
<tr><td>Celles que vous nous communiquez en nous contactant (nom, téléphone, e-mail, dates et nombre de personnes) par WhatsApp, téléphone ou e-mail</td><td>Répondre à votre demande et gérer votre demande de réservation</td><td>Mesures précontractuelles à votre demande (art. 6, par. 1, point b) du RGPD)</td></tr>
<tr><td>Données des voyageurs exigées par la réglementation sur le registre des voyageurs (nom, pièce d'identité et immatriculation du véhicule)</td><td>Respecter l'obligation légale d'enregistrement et d'information des autorités</td><td>Obligation légale (art. 6, par. 1, point c))</td></tr>
<tr><td>Données de paiement et de facturation, le cas échéant</td><td>Encaisser le séjour et respecter les obligations fiscales</td><td>Exécution du contrat et obligation légale (art. 6, par. 1, points b) et c))</td></tr><tr><td>Celles que vous nous communiquez dans le formulaire de demande par e-mail (nom, e-mail, téléphone facultatif, dates et message)</td><td>Répondre à votre demande de réservation</td><td>Mesures précontractuelles à votre demande (art. 6, par. 1, point b) du RGPD)</td></tr>
<tr><td>Données techniques de la visite (page, site d'origine, pays, navigateur et taille d'écran), sans adresse IP ni cookies</td><td>Mesurer l'utilisation du site pour l'améliorer</td><td>Intérêt légitime (art. 6, par. 1, point f) du RGPD)</td></tr></table>
<p>Ce site <b>n'a aucun formulaire qui conserve des données</b> et <b>n'utilise pas de cookies</b>. Pour savoir combien de personnes le visitent, nous utilisons <b>GoatCounter</b>, un service de statistiques sans cookies qui ne conserve pas votre adresse IP, ne vous identifie pas et ne s'active pas si votre navigateur indique « ne pas suivre ». Le formulaire « Demander une réservation » prépare seulement un message et ouvre WhatsApp sur votre appareil : nous ne recevons rien tant que vous ne l'envoyez pas par WhatsApp.</p>
<h2>3. Destinataires</h2>
<p>Nous ne cédons pas vos données à des tiers, sauf obligation légale (par exemple, aux administrations compétentes en matière de registre des voyageurs ou de fiscalité). Nous utilisons WhatsApp (Meta) comme canal de communication si vous nous écrivez par ce moyen, ainsi que l'hébergeur du site pour servir cette page, qui peut enregistrer votre adresse IP pour des raisons techniques et de sécurité.</p>
<p>Pour les statistiques de visites, nous utilisons GoatCounter, qui ne reçoit ni votre e-mail ni aucune donnée que vous nous communiquez par WhatsApp ou par e-mail.</p>
<p>Le calendrier de disponibilités et les tarifs sont chargés depuis un service propre hébergé chez Cloudflare, qui peut enregistrer votre adresse IP pour des raisons techniques et de sécurité ; il ne reçoit aucune donnée personnelle de votre part.</p>
<p>Le formulaire de demande par e-mail envoie votre message à notre boîte par un service de Cloudflare (qui ne fait que le transmettre et ne le conserve pas) ; nous le recevons dans notre messagerie, où il est conservé comme n'importe quel autre e-mail.</p>
<h2>4. Conservation</h2>
<p>Nous conservons les conversations et les données de la demande le temps nécessaire pour la traiter et, en cas de réservation, pendant les durées exigées par les règles d'enregistrement, fiscales et commerciales.</p>
<h2>5. Vos droits</h2>
<p>Vous pouvez exercer vos droits d'accès, de rectification, d'effacement, d'opposition, de limitation et de portabilité en écrivant à @email@. Si vous estimez que vos données ne sont pas traitées correctement, vous pouvez déposer une réclamation auprès de l'Agence espagnole de protection des données (Agencia Española de Protección de Datos, <a href="https://www.aepd.es">www.aepd.es</a>).</p>
<h2>6. Cookies</h2>
<p>Ce site n'installe pas de cookies. Les visites sont mesurées avec GoatCounter, sans cookies, sans publicité et sans conserver l'adresse IP ; c'est pourquoi il n'affiche pas de bandeau de cookies. Si votre navigateur indique « ne pas suivre », votre visite n'est même pas comptée.</p>
"""),
        "cond": ("Conditions générales de réservation", """
<p>Ces conditions régissent la location de courte durée de l'appartement <b>@nombre@</b>, à Torrox Costa (Málaga), numéro officiel d'enregistrement du logement <b>@registro@</b>. Elles sont complétées par les <a href="@r_aviso@">mentions légales</a> et la <a href="@r_priv@">politique de confidentialité</a>.</p>
<h2>1. Qui loue</h2>
<p>@titular@, numéro fiscal (NIF) @nif@, domicilié à @domicilio@. Contact : @email@ · @tel@ (aussi par WhatsApp).</p>
<h2>2. Demande et confirmation de la réservation</h2>
<p>La demande se fait par WhatsApp, par e-mail ou par téléphone. <b>La demande n'est pas une réservation</b> : la réservation est confirmée lorsque le titulaire l'accepte par écrit et que l'acompte indiqué ci-dessous est reçu. La capacité maximale du logement est de <b>10 personnes</b>. Les animaux ne sont pas admis.</p>
<h2>3. Prix</h2>
<ul><li>Le prix est par nuit et <b>TVA incluse</b>. Les tarifs en vigueur figurent sur la <a href="@r_tarifas@">page d'accueil</a>.</li>
<li>Le <b>séjour minimum</b> est de 2 nuits.</li>
<li>Le <b>ménage de fin de séjour</b> est inclus dans le prix, ainsi que le linge de lit, les serviettes et le wifi.</li>
<li>Une consommation d'électricité de <b>50 kWh par semaine</b> est incluse.</li></ul>
<h2>4. Acompte et mode de paiement</h2>
<p>Pour confirmer la réservation, un <b>acompte de 50 €</b> est versé ; il est <b>déduit du prix final</b>. Le reste du prix se paie selon les modalités et à la date convenues lors de la confirmation de la réservation. Les moyens de paiement sont communiqués à la confirmation ; ils ne sont pas publiés sur ce site.</p>
<h2>5. Caution</h2>
<p>Avant l'arrivée, le client remet une <b>caution de 400 €</b> en garantie. Elle est restituée <b>après vérification de l'état de l'appartement</b>, le jour du départ ou, au plus tard, dans les 3 jours suivants. Les dégâts ou frais supplémentaires de la section 10 seront, le cas échéant, déduits de la caution.</p>
<h2>6. Annulation</h2>
<p>La politique d'annulation est <b>flexible</b> : vous pouvez annuler <b>jusqu'à 1 semaine (7 jours) avant la date d'arrivée</b>. Pour annuler, il suffit de nous prévenir par WhatsApp ou par e-mail. En cas d'annulation dans cette semaine, ce qui a été convenu lors de la confirmation de la réservation s'applique.</p>
<h2>7. Droit de rétractation</h2>
<p>S'agissant d'un service d'hébergement à date d'exécution déterminée, <b>le droit légal de rétractation de 14 jours ne s'applique pas</b> (article 103, point l) du texte refondu de la loi générale espagnole pour la défense des consommateurs et des usagers). La politique d'annulation de la section 6 s'applique.</p>
<h2>8. Arrivée et départ</h2>
<ul><li><b>Arrivée</b> : de 16 h 00 à 21 h 00 le jour de l'arrivée. Une arrivée plus tôt ou plus tard doit être demandée et peut entraîner un coût supplémentaire.</li>
<li><b>Départ</b> : au plus tard à 11 h 00 le jour du départ. Un départ plus tard doit être demandé et peut entraîner un coût supplémentaire.</li>
<li>L'accès est autonome : les instructions d'arrivée sont envoyées au client après confirmation de la réservation.</li>
<li>En partant, le client laisse l'appartement fermé, les clés à l'intérieur, et prévient par WhatsApp.</li></ul>
<h2>9. Données des voyageurs</h2>
<p>Avant l'arrivée, le client doit envoyer le <b>nom et la pièce d'identité de tous les occupants</b>, ainsi que l'<b>immatriculation du véhicule</b> qui utilise la place de parking. C'est une obligation légale d'enregistrement des voyageurs ; consultez la <a href="@r_priv@">politique de confidentialité</a>.</p>
<h2>10. Frais supplémentaires</h2>
<ul><li><b>Électricité</b> : la consommation supérieure à 50 kWh par semaine est facturée <b>0,45 € par kWh</b>. Le compteur peut être consulté près de la porte d'entrée.</li>
<li><b>Arrivée ou départ hors horaires</b> : sur demande.</li>
<li><b>Lit bébé</b> : 1 € par jour.</li>
<li><b>Perte de clés</b> : la clé physique est anticopie et sa perte oblige à changer toute la serrure (<b>150 €</b>). La perte d'une clé magnétique coûte <b>20 €</b>.</li>
<li>Services supplémentaires, prix et disponibilité sur demande : location de vélos, de parasol et de chaises de plage.</li></ul>
<h2>11. Règles d'usage</h2>
<ul><li>Il est interdit de <b>fumer</b> dans l'appartement.</li>
<li>Les <b>fêtes sont strictement interdites</b> dans la copropriété. Si un dîner se prolonge après minuit, il doit continuer à l'intérieur de l'appartement.</li>
<li>Les ordures sont déposées dans le conteneur, à l'extérieur de la résidence, avant le départ.</li>
<li>Les <b>règles de la copropriété</b> sont obligatoires ; elles sont remises au client.</li>
<li>La climatisation doit être utilisée avec modération et seulement lorsque l'on est présent.</li>
<li>Les jeux de serviettes sont destinés à l'intérieur et ne peuvent pas être utilisés à la plage.</li></ul>
<h2>12. Responsabilité du client</h2>
<p>Le client répond des dommages causés à l'appartement, au mobilier ou aux parties communes, et du non-respect des règles de la copropriété. Le titulaire peut mettre fin au séjour en cas de manquement grave aux règles d'usage.</p>
<h2>13. Droit applicable et réclamations</h2>
<p>Droit espagnol. Pour toute réclamation, écrivez à @email@. Si vous êtes consommateur, les tribunaux de votre domicile sont compétents.</p>
"""),
    },
    # ------------------------------------------------------------------ NEDERLANDS
    "nl": {
        "aviso": ("Juridische kennisgeving", """
<h2>1. Identificatiegegevens</h2>
<p>In overeenstemming met artikel 10 van de Spaanse wet 34/2002 over diensten van de informatiemaatschappij en elektronische handel wordt meegedeeld dat deze website eigendom is van:</p>
<p><b>Eigenaar:</b> @titular@<br><b>Belastingnummer (NIF):</b> @nif@<br><b>Adres:</b> @domicilio@<br><b>E-mail:</b> @email@<br><b>Telefoon:</b> @tel@<br><b>Handelsnaam:</b> @nombre@<br><b>Activiteit:</b> verhuur van vakantieaccommodatie<br><b>Officieel registratienummer van de accommodatie:</b> @registro@</p>
<h2>2. Doel en gebruiksvoorwaarden</h2>
<p>Deze kennisgeving regelt de toegang tot en het gebruik van de website. Door de website te openen, aanvaardt u deze kennisgeving. De boekingsvoorwaarden staan in de <a href="@r_cond@">Algemene boekingsvoorwaarden</a>.</p>
<h2>3. Intellectuele eigendom</h2>
<p>De teksten, foto's en het ontwerp van de website behoren toe aan de eigenaar. Zonder toestemming mogen ze niet worden vermenigvuldigd of openbaar gemaakt, behalve voor zover de wet dat toestaat.</p>
<h2>4. Aansprakelijkheid</h2>
<p>De informatie over de accommodatie (voorzieningen, diensten, tarieven, beschikbaarheid) is indicatief en wordt zoveel mogelijk actueel gehouden, maar kan veranderen. Een boeking wordt pas definitief wanneer de eigenaar haar bevestigt. De eigenaar is niet verantwoordelijk voor de inhoud van websites van derden waarnaar wordt verwezen.</p>
<h2>5. Toepasselijk recht en bevoegde rechter</h2>
<p>Deze kennisgeving wordt beheerst door het Spaanse recht. Bent u consument, dan zijn de rechtbanken van uw woonplaats bevoegd.</p>
"""),
        "priv": ("Privacybeleid", """
<h2>1. Verwerkingsverantwoordelijke</h2>
<p><b>@titular@</b>, belastingnummer (NIF) @nif@, gevestigd te @domicilio@. Contact: @email@.</p>
<h2>2. Welke gegevens we verwerken en waarom</h2>
<table><tr><th>Gegevens</th><th>Doel</th><th>Rechtsgrond</th></tr>
<tr><td>Wat u ons meedeelt wanneer u contact opneemt (naam, telefoon, e-mail, data en aantal personen) via WhatsApp, telefoon of e-mail</td><td>Uw vraag beantwoorden en uw boekingsaanvraag behandelen</td><td>Precontractuele maatregelen op uw verzoek (art. 6, lid 1, onder b AVG)</td></tr>
<tr><td>Gegevens van gasten die de regels voor de reizigersregistratie vereisen (naam, identiteitsbewijs en kenteken van het voertuig)</td><td>Voldoen aan de wettelijke verplichting tot registratie en informatieverstrekking aan de autoriteiten</td><td>Wettelijke verplichting (art. 6, lid 1, onder c)</td></tr>
<tr><td>Betalings- en factuurgegevens, indien van toepassing</td><td>Het verblijf in rekening brengen en voldoen aan de fiscale verplichtingen</td><td>Uitvoering van de overeenkomst en wettelijke verplichting (art. 6, lid 1, onder b en c)</td></tr><tr><td>Wat u ons meedeelt in het aanvraagformulier per e-mail (naam, e-mail, optioneel telefoon, data en bericht)</td><td>Uw boekingsaanvraag beantwoorden</td><td>Precontractuele maatregelen op uw verzoek (art. 6, lid 1, onder b AVG)</td></tr>
<tr><td>Technische gegevens van uw bezoek (pagina, herkomstwebsite, land, browser en schermgrootte), zonder IP-adres en zonder cookies</td><td>Het gebruik van de website meten om haar te verbeteren</td><td>Gerechtvaardigd belang (art. 6, lid 1, onder f AVG)</td></tr></table>
<p>Deze website <b>heeft geen formulieren die gegevens opslaan</b> en <b>gebruikt geen cookies</b>. Om te weten hoeveel mensen haar bezoeken, gebruiken we <b>GoatCounter</b>, een statistiekdienst zonder cookies die uw IP-adres niet opslaat, u niet identificeert en niet wordt geactiveerd als uw browser „niet volgen” aangeeft. Het formulier „Boeking aanvragen” stelt alleen een bericht op en opent WhatsApp op uw apparaat: wij ontvangen niets totdat u het via WhatsApp verstuurt.</p>
<h2>3. Ontvangers</h2>
<p>We verstrekken uw gegevens niet aan derden, tenzij de wet dat verplicht (bijvoorbeeld aan de autoriteiten die bevoegd zijn voor reizigersregistratie of belastingen). We gebruiken WhatsApp (Meta) als communicatiekanaal als u ons daarop schrijft, en de hostingprovider om deze pagina te leveren, die uw IP-adres om technische en veiligheidsredenen kan vastleggen.</p>
<p>Voor de bezoekstatistieken gebruiken we GoatCounter, dat noch uw e-mailadres noch gegevens ontvangt die u ons via WhatsApp of e-mail meedeelt.</p>
<p>De beschikbaarheidskalender en de tarieven worden geladen vanuit een eigen dienst die bij Cloudflare wordt gehost en die uw IP-adres om technische en veiligheidsredenen kan vastleggen; zij ontvangt geen persoonsgegevens van u.</p>
<p>Het aanvraagformulier per e-mail stuurt uw bericht via een dienst van Cloudflare (die het alleen doorgeeft en niet opslaat) naar onze mailbox; wij ontvangen het in onze inbox, waar het wordt bewaard zoals elke andere e-mail.</p>
<h2>4. Bewaartermijn</h2>
<p>We bewaren de gesprekken en de gegevens van de aanvraag zolang nodig is om de aanvraag te behandelen en, bij een boeking, gedurende de termijnen die de registratie-, fiscale en handelsregels voorschrijven.</p>
<h2>5. Uw rechten</h2>
<p>U kunt uw rechten van inzage, rectificatie, wissing, bezwaar, beperking en overdraagbaarheid uitoefenen door te schrijven naar @email@. Als u van mening bent dat uw gegevens niet correct worden verwerkt, kunt u een klacht indienen bij de Spaanse gegevensbeschermingsautoriteit (Agencia Española de Protección de Datos, <a href="https://www.aepd.es">www.aepd.es</a>).</p>
<h2>6. Cookies</h2>
<p>Deze website plaatst geen cookies. Bezoeken worden gemeten met GoatCounter, zonder cookies, zonder reclame en zonder het IP-adres op te slaan; daarom toont zij geen cookiemelding. Als uw browser „niet volgen” aangeeft, wordt uw bezoek niet eens geteld.</p>
"""),
        "cond": ("Algemene boekingsvoorwaarden", """
<p>Deze voorwaarden regelen de kortetermijnverhuur van het appartement <b>@nombre@</b> in Torrox Costa (Málaga), met officieel registratienummer van de accommodatie <b>@registro@</b>. Ze worden aangevuld door de <a href="@r_aviso@">juridische kennisgeving</a> en het <a href="@r_priv@">privacybeleid</a>.</p>
<h2>1. Wie verhuurt</h2>
<p>@titular@, belastingnummer (NIF) @nif@, gevestigd te @domicilio@. Contact: @email@ · @tel@ (ook via WhatsApp).</p>
<h2>2. Aanvraag en bevestiging van de boeking</h2>
<p>De aanvraag gebeurt via WhatsApp, e-mail of telefoon. <b>Een aanvraag is geen boeking</b>: de boeking is bevestigd wanneer de eigenaar haar schriftelijk aanvaardt en de hieronder vermelde aanbetaling is ontvangen. De maximale capaciteit van de accommodatie is <b>10 personen</b>. Huisdieren zijn niet toegestaan.</p>
<h2>3. Prijs</h2>
<ul><li>De prijs geldt per nacht en is <b>inclusief btw</b>. De geldende tarieven staan op de <a href="@r_tarifas@">startpagina</a>.</li>
<li>Het <b>minimumverblijf</b> is 2 nachten.</li>
<li>De <b>eindschoonmaak</b> is in de prijs inbegrepen, evenals beddengoed, handdoeken en wifi.</li>
<li>Inbegrepen is een stroomverbruik van <b>50 kWh per week</b>.</li></ul>
<h2>4. Aanbetaling en betaalwijze</h2>
<p>Om de boeking te bevestigen wordt een <b>aanbetaling van € 50</b> voldaan, die wordt <b>afgetrokken van de eindprijs</b>. De rest van de prijs wordt betaald op de manier en datum die bij de bevestiging van de boeking worden afgesproken. De betaalmethoden worden bij de bevestiging meegedeeld; ze worden niet op deze website gepubliceerd.</p>
<h2>5. Waarborgsom</h2>
<p>Voor aankomst overhandigt de gast een <b>waarborgsom van € 400</b> als zekerheid. Die wordt <b>na controle van de staat van het appartement</b> teruggegeven, op de dag van vertrek of uiterlijk binnen 3 dagen daarna. Eventuele schade of extra kosten uit sectie 10 worden van de waarborgsom afgetrokken.</p>
<h2>6. Annulering</h2>
<p>Het annuleringsbeleid is <b>flexibel</b>: u kunt <b>tot 1 week (7 dagen) vóór de aankomstdatum</b> annuleren. Om te annuleren volstaat een bericht via WhatsApp of e-mail. Bij annulering binnen die week geldt wat bij de bevestiging van de boeking is afgesproken.</p>
<h2>7. Herroepingsrecht</h2>
<p>Omdat het gaat om een accommodatiedienst met een bepaalde uitvoeringsdatum, <b>geldt het wettelijke herroepingsrecht van 14 dagen niet</b> (artikel 103, onder l van de Spaanse geconsolideerde tekst van de algemene wet ter bescherming van consumenten en gebruikers). Het annuleringsbeleid van sectie 6 is van toepassing.</p>
<h2>8. Aankomst en vertrek</h2>
<ul><li><b>Aankomst</b>: van 16:00 tot 21:00 uur op de dag van aankomst. Een eerdere of latere aankomst moet vooraf worden aangevraagd en kan extra kosten meebrengen.</li>
<li><b>Vertrek</b>: uiterlijk om 11:00 uur op de dag van vertrek. Een later vertrek moet vooraf worden aangevraagd en kan extra kosten meebrengen.</li>
<li>De toegang is zelfstandig: de aankomstinstructies worden naar de gast gestuurd nadat de boeking is bevestigd.</li>
<li>Bij vertrek laat de gast het appartement afgesloten achter, met de sleutels binnen, en meldt dat via WhatsApp.</li></ul>
<h2>9. Gegevens van de gasten</h2>
<p>Voor aankomst moet de gast de <b>naam en het identiteitsbewijs van alle gebruikers</b> sturen, evenals het <b>kenteken van het voertuig</b> dat de parkeerplaats gebruikt. Dit is een wettelijke verplichting voor de reizigersregistratie; zie het <a href="@r_priv@">privacybeleid</a>.</p>
<h2>10. Extra kosten</h2>
<ul><li><b>Elektriciteit</b>: verbruik boven 50 kWh per week wordt in rekening gebracht tegen <b>€ 0,45 per kWh</b>. De meter kan naast de voordeur worden afgelezen.</li>
<li><b>Aankomst of vertrek buiten de uren</b>: op aanvraag.</li>
<li><b>Babybedje</b>: € 1 per dag.</li>
<li><b>Verlies van sleutels</b>: de fysieke sleutel is kopieerbeveiligd en bij verlies moet het hele slot worden vervangen (<b>€ 150</b>). Het verlies van een magnetische sleutel kost <b>€ 20</b>.</li>
<li>Extra diensten, met prijs en beschikbaarheid op aanvraag: verhuur van fietsen, parasol en strandstoelen.</li></ul>
<h2>11. Gebruiksregels</h2>
<ul><li><b>Roken</b> is in het appartement niet toegestaan.</li>
<li><b>Feesten zijn in het complex strikt verboden.</b> Als een diner na middernacht doorloopt, moet het binnen in het appartement worden voortgezet.</li>
<li>Het afval wordt voor vertrek in de container buiten het complex gedeponeerd.</li>
<li>De <b>regels van de vereniging van eigenaren</b> moeten worden nageleefd; ze worden aan de gast overhandigd.</li>
<li>De airconditioning moet met mate worden gebruikt en alleen als u thuis bent.</li>
<li>De handdoekensets zijn voor gebruik binnen en mogen niet mee naar het strand.</li></ul>
<h2>12. Verantwoordelijkheid van de gast</h2>
<p>De gast is verantwoordelijk voor schade aan het appartement, het meubilair of de gemeenschappelijke ruimtes en voor schending van de regels van de vereniging van eigenaren. De eigenaar kan het verblijf beëindigen als de gebruiksregels ernstig worden overtreden.</p>
<h2>13. Toepasselijk recht en klachten</h2>
<p>Spaans recht. Voor klachten schrijft u naar @email@. Bent u consument, dan zijn de rechtbanken van uw woonplaats bevoegd.</p>
"""),
    },
}
