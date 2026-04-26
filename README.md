# 📊 Analyse Dynamique des Ventes (Pandas & Matplotlib)

**👥 Équipe : Kadi – Tes – Yas**

Ce projet est une application Python permettant d'automatiser l'analyse de données commerciales à partir de fichiers CSV.  
Il calcule automatiquement le chiffre d'affaires (brut et net), la TVA, et génère une visualisation graphique des performances par produit.

---

## 🚀 Fonctionnalités

* **Lecture Dynamique** : Capacité de lire et de traiter des fichiers CSV de n'importe quelle taille.  

* **Calculs Automatisés** :  
  * CA Brut (Prix × Quantité)  
  * CA Net (prise en compte des remises en %)  
  * Calcul de la TVA (20%)  

* **Analyse de Performance** :  
  * Identification automatique du produit le plus rentable  

* **Visualisation de Données** :  
  * Génération d'un graphique en barres avec `Matplotlib`  

---

## 📁 Structure des données

Le fichier CSV doit contenir les colonnes suivantes :

```bash
ID, Prix, Quantite, Remise
101, 15.0, 3, 10
102, 25.0, 2, 5
103, 10.0, 5, 0
* **Lecture Dynamique** : Capacité de lire et de traiter des fichiers CSV de n'importe quelle taille.
* **Calculs Automatisés** : 
    * CA Brut (Prix * Quantité).
    * CA Net (Prise en compte des remises en %).
    * Calcul de la TVA (20%).

## 🛠️ Installation

Assurez-vous d'avoir Python installé (version 3.10 ou supérieure recommandée).

1. Clonez ce dépôt ou copiez les fichiers du projet.
2. Installez les bibliothèques nécessaires via le terminal :

```bash
pip install pandas matplotlib