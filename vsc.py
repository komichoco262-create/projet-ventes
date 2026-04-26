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
# 6. GRAPHIQUE 
# =========================
plt.bar(df["ID"], df["CA_Net"])
plt.xlabel("Produit ID")
plt.ylabel("CA Net")
plt.title("Chiffre d'affaires par produit")
plt.show()
# Charger les données et créer le graphique
df = pd.read_csv("ventes.csv")
plt.bar(df['ID'].astype(str), df['Prix'], color='skyblue')
plt.title("Chiffre d'Affaires Net par Produit")
plt.xlabel("ID Produit")
plt.ylabel("CA Net (€)")

# Sauvegarder l'image
plt.savefig("graphique.png")
print("Graphique généré avec succès !")