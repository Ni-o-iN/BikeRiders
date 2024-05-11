# DSA - Team BikeRiders, Thema Fahrradroutenoptimierung
Projekt für die Vorlesung Data Science and Analytics (DSA) zur Überprüfung von guten Routen für Fahrradfahrer in Bezug auf Sicherheit und Vermeidung von langen Ampelwartezeiten.

# Mitglieder:
Emil Gäng 2012346
Nico Ohler 2024457
Kai Winnemann 2021106
Kim Mennemann 2011879

# Ziel des Projekts
Ziel des Projektes ist die Bewertung verschiedener Fahrradrouten von der Hochschule Mannheim zum Mannheimer Hauptbahnhof anhand von Ampelschaltungen.
Die Daten der Ampelschaltungen wurden freundlicherweise von der Verkehrsleitzentrale der Stadt Mannheim zur Verfügung gestellt.
Es soll festgestellt werden, welche der vier ausgewählten Strecken die Optimale ist.
Hierfür werden die kürztmöglichsten Rotphasen für Fahrradfaher ermittelt. Es werden die minimalen und maximalen Längen der Grün- und Rotphasen ermittelt, um einen Mittelwert der Ampelzyklen zu ermitteln.

Weiterhin werden Gefahren auf dem Weg (zB. Fahrradweg in entgegengesetzte Richtung, Überquerung von Straßenbahnschienen), sowie ausgewiesene Fahrradwege berücksichtigt. Diese spielen in der Bewertung der Fahrradrouten einen Rolle.

Ergebnis:
- Eingabe der Durchschnittsgeschwindigkeit
- Eingabe der Tageszeit der Reise
- Ausgabe der optimalen der vier Routen mit Berücksichtigung von folgenden Metadaten:
  - Streckenlänge der Route, z.B. 12km
  - Dauer pro Strecke, z.B. 6 min +- 34s
  - Geschwindigkeit des Fahrradfahrers, z.B. 10km/h oder 30km/h
  - Gefahren auf dem Weg, bzw. Merkmale des Weges, z.B. 300m gegen die Einbahnstraße fahren, vorhandener Fahrradweg

# Hintergrund

Es gibt viele Navigationssysteme, die Routenplanung für Fahrradfahrer ermöglichen. Dabei gibt es für Fahrradfahrer oft ein Problem bei Ampeln, die auf andere Geschwindigkeiten optimiert sind. Eine Grüne Welle ist meist für Autofahrer ausgelegt und nicht für Fahrradfahrer nutzbar. Das führt bei Fahrradfahrern zu längeren Wegzeiten bei kürzerer Strecke. Das Problem besteht hauptsächlich bei erlaubten Geschwindigkeiten von über 30 km/h (meist 50km/h), da Fahrradfahrer diese Geschwindigkeiten meist nicht über längere Zeit halten können.

# Mögliche Datenquellen

|   | Negativ  | Positiv | Bias | Link |
|---|---|---|---|---|
| Fahrradzähler der Stadt (Eco Counter)  |  Wenige Messpunkte (ca.10),  weit verteilt, teiweise geringe Zahlen | Viele Daten über langen Zeitraum  | Es werden nicht alle Fahrradfahrer erfasst, Richtung kann nicht unterschieden werden | https://mannheim.opendatasoft.com/explore/?sort=modified&q=eco+counter |
|  Ampeldaten der Stadt |  PDFs, Daten müssen jedoch händisch übertragen werden | korrekt, vollständig  | Es sagt nichts über die aktuelle Verkehrslage aus, ist nur die Darstellung eines Optimalzustands | https://github.com/eg-00/dsa/tree/main/daten |
| Verkehrszähler der Stadt | 	Hauptsächlich PKW/LKW, nur an einzelnen Kreuzungen |	Stündliche Messpunkte, ungenaue Fahrradzahlen | Fokus auf Autofahrer, Fahrradfahrer nur ein Nebenprodukt | https://opendata.smartmannheim.de/dataset/?organization=smart-mannheim |

# Verwendete Datenquelle
Unter Berücksichtigung unserer Bedürfnisse und Ziele haben wir uns entschieden, ausschließlich die Daten der Verkehrsleitzentrale zu nutzen. Durch direkte Kooperation und Kommunikation mit der Leitzentrale haben wir Zugang zu den gewünschten Informationen über die Ampelsysteme erhalten.

Die Entscheidung, die anderen zwei Datenquellen nicht zu nutzen, basiert auf ihrer Unzuverlässigkeit. Diese Quellen liefern zu ungenaue Daten, da sie teilweise auch Autos mitzählen könnten, und die genaue Zusammensetzung der erfassten Daten nicht transparent ist. Zudem stellten wir fest, dass die Daten von Kreuzungen, die zu weit voneinander entfernt liegen, keine kohärenten Informationen bieten. An diesen Kreuzungen waren nur eine Handvoll Fahrradfahrer unterwegs, was die Datensätze für unsere Zwecke als nicht besonders relevant erscheinen ließ. Daher haben wir uns entschieden, uns voll und ganz auf die präzisen und relevanten Daten der Verkehrsleitzentrale zu konzentrieren, um die Qualität und Genauigkeit unserer Analysen sicherzustellen.

# Geplante Routen
![Bild mit den 4 zu betrachtenden Routen](/bilder/Routen.png)

Hellgrüne Route: Verläuft südlich an den Bahnschienen, beinhaltet einen Abschnitt, an dem das Fahrrad die Treppen der Bahnhofsunterführung heruntergetragen werden muss 

Dunkelgrüne Route: "legale" Route, nördlich der Bahnschienen, beinhaltet einen Umweg

Lila Route: "illegale" Route, da ca. 200m gegen die Fahrtrichtung über die Brücke gefahren werden muss. Da viele Fahrradfahrer dies machen, kommt diese Route als schnelle Route mit in Frage

Rote Route: Zusammengesetzt aus der hell- und dunkelgrünen Route. Verläuft zuerst auf der südlichen Seite der Bahnschienen, dann Seitenwechsel über die Fahrrad- und Fußgängerbrücke

# Datensammlung für Ampelschaltungen
In folgender Google Spreadsheet Datei sind die Schaltdaten aller relevanten Ampeln der unterschiedlichen festgelegten Routen zu finden. Diese wurden extrahiert aus der Datenquelle "Ampeldaten der Stadt".

https://docs.google.com/spreadsheets/d/1XgsFw8Fynec__njbpKFC4uT_02T9ustbVmKGRoTAr60/edit?usp=sharing

# Auswahl der Programmiersprache
Unser Team hat sich nach eingehender Analyse dafür entschieden, Python als Hauptprogrammiersprache für unser Data Science and Analytics (DSA)  zu verwenden, da wir in der Gruppe die meiste Erfahrung mit dieser Sprache haben. Wir sind mit den Python-Bibliotheken, unteranderem Pandas und NumPy, vertraut, die sich gut für die Datenverarbeitung und Analyse eignen. Zudem bietet Python eine ausgezeichnete Balance zwischen Leistung, Flexibilität und Benutzerfreundlichkeit.

Wir haben auch Alternativen wie R und MATLAB in Betracht gezogen. R bietet beispielsweise eine robuste statistische Unterstützung, während MATLAB für seine leistungsstarke numerische Berechnungsumgebung bekannt ist. Dennoch haben wir uns aufgrund unserer Vertrautheit und Projektexpertiese der Vergangenheit mit Python für diese Sprache entschieden. 

Daher planen wir, Python zusammen mit den Bibliotheken Pandas und NumPy zu verwenden, um eine gründliche Analyse der Fahrradrouten durchzuführen und Inputangepasste Entscheidungen zu treffen.
  
# Aufgabenstellung

|Abgabe|Frist|Erwartungen|
|---|---|---|
|Projektskizze|15.05.2024|Projektskizze, Beschreibung der Problematik, Hintergrund, Projektziele, erste technische Dokumentation (Architektur-Diagramme, mögliche Datenquellen, Auswahl der Quellen)|
|Codeprojekt + Dokumentation|12.06.2024|Link zu Github-Repository, Dokumentation kann in der ReadMe aufgeführt und aktualisiert werden oder auch in einem zusätzlichen Dokument (PDF)|
|Codeprojekt + Dokumentation + Abschlusspräsentation|03.07.2024|Link zu Github-Repository, Dokumentation entweder finalisiert in der ReadMe oder in einem zusätzlichen Dokument (PDF) Powerpoint, (10 Minuten Präsentation)|
