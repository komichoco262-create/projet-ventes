import csv
import pandas as pd
import matplotlib.pyplot as plt
import os
import random


# 1. CREATION DU CSV 

donnees = [["ID", "Prix", "Quantite", "Remise"]]

for i in range(1, 100000): 
    prix = round(random.uniform(5, 100), 2)       # prix entre 5 et 100
    quantite = random.randint(1, 20)              # quantité entre 1 et 20
    remise = random.choice([0, 5, 10, 15, 20])    # remise possible
    
    donnees.append([100 + i, prix, quantite, remise])

with open("ventes.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(donnees)

print("ventes.csv (100000 lignes) créé !")


# 2. LECTURE DU FICHIER

if os.path.exists("ventes.csv"):
    df = pd.read_csv("ventes.csv")
else:
    print("Fichier introuvable")
    exit()


# 3. CALCULS

df["CA_Brut"] = df["Prix"] * df["Quantite"]
df["CA_Net"] = df["CA_Brut"] * (1 - df["Remise"] / 100)
df["TVA"] = df["CA_Net"] * 0.2

# 4. ANALYSE

ca_total = df["CA_Net"].sum()
print("CA Total =", ca_total)

max_id = df.loc[df["CA_Net"].idxmax(), "ID"]
print("Produit le plus rentable ID =", max_id)


# 5. EXPORT FINAL

df.to_csv("resultats_final.csv", index=False)
print("resultats_final.csv créé !")

# 6.**** CRÉATION DU GRAPHIQUE****


plt.figure(figsize=(10,5))

plt.hist(df["CA_Net"], bins=30)

plt.title("Distribution du CA Net")
plt.xlabel("CA Net")
plt.ylabel("Frequence")

plt.savefig("graphique.png")

plt.show()

