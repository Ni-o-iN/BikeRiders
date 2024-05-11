# DSA - Team BikeRiders, Thema Fahrradroutenoptimierung
Projekt für die Vorlesung Data Science and Analytics (DSA) zur Überprüfung von guten Routen für Fahrradfahrer in Bezug auf Sicherheit und Vermeidung von langen Ampelwartezeiten zu unterschiedlichen Tageszeiten.

# Table of Contents  
[Mitglieder](#mitglieder)  
[Ziel des Projekts](#ziel-des-projekts)
[Hintergrund](#hintergrund)  
[Mögliche Datenquellen](#mögliche-datenquellen)
[Verwendete Datenquelle](#verwendete-datenquelle)
[Geplante Routen](#geplante-routen)  
[Datensammlung für Ampelschaltungen](#datensammlung-für-ampelschaltungen)
[Ablaufdiagram](#ablaufdiagramm)  
[Auswahl der Programmiersprache](#auswahl-der-programmiersprache)

# Mitglieder:
- Emil Gäng 2012346
- Nico Ohler 2024457
- Kai Winnemann 2021106
- Kim Mennemann 2011879

# Ziel des Projekts
Ziel des Projektes ist die Bewertung verschiedener Fahrradrouten von der Hochschule Mannheim zum Mannheimer Hauptbahnhof anhand von Ampelschaltungen.
Die Daten der Ampelschaltungen wurden freundlicherweise von der Verkehrsleitzentrale der Stadt Mannheim zur Verfügung gestellt.
Es soll festgestellt werden, welche der vier ausgewählten Strecken die Optimale zu einer bestimmten Tageszeit ist.
Hierfür werden die kürztmöglichsten Rotphasen für Fahrradfahrer ermittelt. Es werden die minimalen und maximalen Längen der Grün- und Rotphasen ermittelt, um einen Mittelwert der Ampelzyklen zu erhalten.

Weiterhin werden Gefahren auf dem Weg (z. B. Fahrradweg in entgegengesetzte Richtung, Überquerung von Straßenbahnschienen), sowie ausgewiesene Fahrradwege berücksichtigt. Diese spielen in der Bewertung der Fahrradrouten einen Rolle.

Erwünschtes Ergebnis:
- Eingabe der Durchschnittsgeschwindigkeit des Fahrradfahrers
- Eingabe der Tageszeit der Reise
- Ausgabe der Optimalen der vier Routen mit Berücksichtigung von folgenden Metadaten:
  - Streckenlänge der Route, z.B. 12km
  - Dauer pro Strecke, z.B. 6 min +- 34s
  - Geschwindigkeit des Fahrradfahrers, z.B. 10km/h oder 30km/h
  - Gefahren auf dem Weg, bzw. Merkmale des Weges, z.B. 300m gegen die Einbahnstraße fahren, vorhandene Fahrradwege

# Hintergrund

Es gibt viele Navigationssysteme, die Routenplanung für Fahrradfahrer ermöglichen. Dabei gibt es für Fahrradfahrer oft ein Problem bei Ampeln, die auf andere Geschwindigkeiten optimiert sind. Eine "Grüne Welle" ist meist für Autofahrer ausgelegt und nicht für Fahrradfahrer nutzbar. Das führt bei Fahrradfahrern zu längeren Wegzeiten bei kürzerer Strecke. Das Problem besteht hauptsächlich bei erlaubten Geschwindigkeiten von über 30 km/h (meist 50km/h), da Fahrradfahrer diese Geschwindigkeiten meist nicht über längere Zeit halten können.

Unsere Arbeit zielt darauf ab, für einen beispielhaften Start- und Zielpunkt die optimale Route zu finden. Insbesondere sind hierbei die Ampelphasen von Interesse, da diese der Grund für längere Warte- und Stoppzeiten auf der Strecke sind.

# Mögliche Datenquellen

|   | Negativ  | Positiv | Bias | Link |
|---|---|---|---|---|
| Fahrradzähler der Stadt (Eco Counter)  |  Wenige Messpunkte (12),  weit verteilt, teilweise geringe Zahlen | Viele Daten über langen Zeitraum (2018-2022), stündliche Messungen  | Es werden nicht alle Fahrradfahrer erfasst (Mess-Bias, Selektionsbias), Richtung kann nicht unterschieden werden | https://mannheim.opendatasoft.com/explore/?sort=modified&q=eco+counter |
|  Ampeldaten der Stadt |  PDFs, Daten müssen jedoch händisch übertragen werden | korrekt, vollständig  | Es sagt nichts über die aktuelle Verkehrslage aus, ist nur die Darstellung eines Optimalzustands (Temporaler Bias) | https://github.com/eg-00/dsa/tree/main/daten |
| Verkehrszähler der Stadt (Traffic Counter) | 	Hauptsächlich PKW/LKW, nur an einzelnen Kreuzungen, ungenaue Fahrradzahlen |	Stündliche Messpunkte (Seit 01/2023, täglich aktualisiert) | Fokus auf Autofahrer, Fahrradfahrer nur ein Nebenprodukt (Stichproben-/Selektionsbias) | https://opendata.smartmannheim.de/dataset/?organization=smart-mannheim |

# Verwendete Datenquelle
Unter Berücksichtigung unserer Bedürfnisse und Ziele haben wir uns entschieden, ausschließlich die Daten der Verkehrsleitzentrale zu nutzen. Durch direkte Kooperation und Kommunikation mit der Leitzentrale haben wir Zugang zu den gewünschten Informationen über die Ampelsysteme erhalten.

Die Entscheidung, die anderen zwei Datenquellen nicht zu nutzen, basiert auf ihrer Unzuverlässigkeit. Diese Quellen liefern zu ungenaue Daten, da sie teilweise auch Autos mitzählen können und die genaue Zusammensetzung der erfassten Daten ist nicht transparent. Zudem stellten wir fest, dass die Daten von Kreuzungen, die zu weit voneinander entfernt liegen, keine kohärenten Informationen bieten. An diesen Kreuzungen waren nur eine Handvoll Fahrradfahrer unterwegs, was die Datensätze für unsere Zwecke als nicht besonders relevant erscheinen ließ. Daher haben wir uns entschieden, uns voll und ganz auf die präzisen und relevanten Daten der Verkehrsleitzentrale zu konzentrieren, um die Qualität und Genauigkeit unserer Analysen sicherzustellen.

# Geplante Routen
![Bild mit den 4 zu betrachtenden Routen](/bilder/Routen.png)

Hellgrüne Route: Verläuft südlich an den Bahnschienen, beinhaltet einen Abschnitt, an dem das Fahrrad die Treppen der Bahnhofsunterführung heruntergetragen werden muss. Hat in großen Teilen des Wegs einen markierten Fahrradweg.

Dunkelgrüne Route: Verläuft nördlich der Bahnschienen, beinhaltet einen Umweg, ist dafür im Vergleich zur lila Route eine "legale" Route, mit markierten Fahrradwegen.

Lila Route: Verläuft nördlich der Bahnschienen, "illegale" Route, da ca. 200m gegen die Fahrtrichtung des Fahrradweges über die Brücke gefahren werden muss. Da viele Fahrradfahrer in Realität diese statt der dunkelgrünen Route fahren, wird diese Route als schnelle Route mit betrachtet.

Rote Route: Zusammengesetzt aus der hell- und dunkelgrünen Route. Verläuft zuerst auf der südlichen Seite der Bahnschienen, dann Seitenwechsel über die Fahrrad- und Fußgängerbrücke zur nördlichen Seite der Bahnschienen. Hat ebenfalls in großen Teilen des Wegs einen markierten Fahrradweg.

# Datensammlung für Ampelschaltungen
In folgender Google Spreadsheet Datei sind die Schaltdaten aller relevanten Ampeln der unterschiedlichen festgelegten Routen zu finden. Diese wurden händisch aus der Datenquelle "Ampeldaten der Stadt" extrahiert.

https://docs.google.com/spreadsheets/d/1XgsFw8Fynec__njbpKFC4uT_02T9ustbVmKGRoTAr60/edit?usp=sharing

# Ablaufdiagramm

![Ablauf](/bilder/Ablaufdiagram.png)

Ein Ablaufdiagramm für unsere Analyse.

# Auswahl der Programmiersprache
Unser Team hat sich nach eingehender Analyse dafür entschieden, Python als Hauptprogrammiersprache für unser DSA-Projekt  zu verwenden, da wir in der Gruppe die meiste Erfahrung mit dieser Sprache haben. Wir sind mit den Python-Bibliotheken, die häufig für Datenverarbeitung und Analyse verwendet werden (bspw. Pandas und NumPy), vertraut. Zudem bietet Python eine ausgezeichnete Balance zwischen Leistung, Flexibilität und Benutzerfreundlichkeit.

Wir haben auch Alternativen wie R und MATLAB in Betracht gezogen. R bietet beispielsweise eine robuste statistische Unterstützung, während MATLAB für seine leistungsstarke numerische Berechnungsumgebung bekannt ist. Dennoch haben wir uns aufgrund unserer Vertrautheit und Projektexpertise mit Python für diese Sprache entschieden. 

Daher planen wir, Python zusammen mit den Bibliotheken Pandas und NumPy zu verwenden, um eine gründliche Analyse der Fahrradrouten durchzuführen und Inputangepasste Entscheidungen zu treffen.
  
# Aufgabenstellung

|Abgabe|Frist|Erwartungen|
|---|---|---|
|Projektskizze|15.05.2024|Projektskizze, Beschreibung der Problematik, Hintergrund, Projektziele, erste technische Dokumentation (Architektur-Diagramme, mögliche Datenquellen, Auswahl der Quellen)|
|Codeprojekt + Dokumentation|12.06.2024|Link zu Github-Repository, Dokumentation kann in der ReadMe aufgeführt und aktualisiert werden oder auch in einem zusätzlichen Dokument (PDF)|
|Codeprojekt + Dokumentation + Abschlusspräsentation|03.07.2024|Link zu Github-Repository, Dokumentation entweder finalisiert in der ReadMe oder in einem zusätzlichen Dokument (PDF) Powerpoint, (10 Minuten Präsentation)|
