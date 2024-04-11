# DSA
Projekt für die Vorlesung Data Science and Analytics (DSA) zur Überprüfung von guten Routen für Fahrradfahrer in Bezug auf Sicherheit und Vermeidung von langen Ampelwartezeiten.


# Ziel des Projekts
Ziel des Projektes ist die Bewertung verschiedener Fahrradrouten von der Hochschule Mannheim zum Mannheimer Hauptbahnhof anhand von Ampelschaltungen.
Die Daten der Ampelschaltungen wurden freundlicherweise von der Verkehrsleitzentrale der Stadt Mannheim zur Verfügung gestellt.
Es soll festgestellt werden, welche der vier ausgewählten Strecken die Optimale ist.
Hierfür werden die kürztmöglichsten Rotphasen für Fahrradfaher ermittelt. Es werden die minimalen und maximalen Längen der Grün- und Rotphasen ermittelt, um einen Mittelwert der Ampelzyklen zu ermitteln.

Weiterhin werden Gefahren auf dem Weg (zB. Fahrradweg in entgegengesetzte Richtung, Überquerung von Straßenbahnschienen), sowie ausgewiesene Fahrradwege berücksichtigt. Diese spielen einen Rolle in der Bewertung der Fahrradrouten.

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

# mögliche Datenquellen

|   | negativ  | positiv |  kommentar |   |
|---|---|---|---|---|
| Fahrradzähler der Stadt  |  wenige messpunkte (ca.10),  weit verteilt, teiweise geringe zahlen | viele Daten über langen zeitraum  |   |   |
|  Ampeldaten der Stadt |  PDFs | korrekt, vollständig  |   |   |
|   |   |   |   |   |
  
# Aufgabenstellung

|Abgabe|Frist|Erwartungen|
|---|---|---|
|Projektskizze|15.05.2024|Projektskizze, Beschreibung der Problematik, Hintergrund, Projektziele, erste technische Dokumentation (Architektur-Diagramme, mögliche Datenquellen, Auswahl der Quellen)|
|Codeprojekt + Dokumentation|12.06.2024|Link zu Github-Repository, Dokumentation kann in der ReadMe aufgeführt und aktualisiert werden oder auch in einem zusätzlichen Dokument (PDF)|
|Codeprojekt + Dokumentation + Abschlusspräsentation|03.07.2024|Link zu Github-Repository, Dokumentation entweder finalisiert in der ReadMe oder in einem zusätzlichen Dokument (PDF) Powerpoint, (10 Minuten Präsentation)|
