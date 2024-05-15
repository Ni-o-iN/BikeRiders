import pandas as pd

# Stelle sicher, dass der Dateipfad korrekt ist
# Zum Beispiel, wenn die Datei "data.csv" im aktuellen Verzeichnis ist:
# df = pd.read_csv("data.csv")

# Wenn sich die Datei in einem anderen Verzeichnis befindet, gib den vollständigen Pfad an:
# df = pd.read_csv("/Pfad/zur/Datei/data.csv")

# Ersetze "data.csv" durch den tatsächlichen Namen deiner CSV-Datei
df = pd.read_csv("data.csv")

#print(df)
filtered_df = df[(df['KreuzungsID'] == 111) & (df['AmpelID'] == 35) & (df['Uhrzeit_start'] == '02:00')]
filter = df[(df['KreuzungsID'] == 111)]
filter = filter[(filter['KreuzungsID'] == 35)]
print(filter)