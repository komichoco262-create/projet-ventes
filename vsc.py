import csv
import pandas as pd
import matplotlib.pyplot as plt
import os

# =========================
# 1. CREATION DU CSV
# =========================
donnees = [
    ["ID", "Prix", "Quantite", "Remise"],
    [101, 15.0, 3, 10],
    [102, 25.0, 2, 5],
    [103, 10.0, 5, 0]
]

with open("ventes.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(donnees)

print("ventes.csv créé !")

# =========================
# 2. LECTURE DU FICHIER
# =========================
if os.path.exists("ventes.csv"):
    df = pd.read_csv("ventes.csv")
else:
    print("Fichier introuvable")
    exit()

# =========================
# 3. CALCULS
# =========================
df["CA_Brut"] = df["Prix"] * df["Quantite"]
df["CA_Net"] = df["CA_Brut"] * (1 - df["Remise"] / 100)
df["TVA"] = df["CA_Net"] * 0.2

# =========================
# 4. ANALYSE
# =========================
ca_total = df["CA_Net"].sum()
print("CA Total =", ca_total)

max_id = df.loc[df["CA_Net"].idxmax(), "ID"]
print("Produit le plus rentable ID =", max_id)

# =========================
# 5. EXPORT FINAL
# =========================
df.to_csv("resultats_final.csv", index=False)
print("resultats_final.csv créé !")

# =========================
# 6. CRÉATION DU GRAPHIQUE
# =========================
# 1. Charger les données depuis le fichier CSV que tu viens de créer
df = pd.read_csv("ventes.csv")

# 2. Configurer le graphique (on utilise astype(str) pour que les ID soient bien espacés)
plt.bar(df['ID'].astype(str), df['Prix'], color='skyblue')

# 3. Ajouter les textes (Titres et légendes)
plt.title("Chiffre d'Affaires Net par Produit")
plt.xlabel("ID Produit")
plt.ylabel("CA Net (€)")

# 4. SAUVEGARDER l'image pour GitHub (C'est l'étape cruciale)
plt.savefig("graphique.png")

# 5. Optionnel : Afficher à l'écran si tu veux le voir sur ton PC
plt.show()

print("Fichier graphique.png généré !")

# Sauvegarder l'image
plt.savefig("diagramecsv.png")
print("Graphique généré avec succès !")