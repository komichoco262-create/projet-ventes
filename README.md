# 📊 Analyse Dynamique des Ventes (Pandas & Matplotlib)

Ce projet est une application Python permettant d'automatiser l'analyse de données commerciales à partir de fichiers CSV. Il calcule automatiquement le Chiffre d'Affaires (Brut et Net), la TVA, et génère une visualisation graphique des performances par produit.

## 🚀 Fonctionnalités

* **Lecture Dynamique** : Capacité de lire et de traiter des fichiers CSV de n'importe quelle taille.
* **Calculs Automatisés** : 
    * CA Brut (Prix * Quantité).
    * CA Net (Prise en compte des remises en %).
    * Calcul de la TVA (20%).
* **Analyse de Performance** : Identification automatique du produit le plus rentable.
* **Visualisation de Données** : Génération d'un graphique en barres avec `Matplotlib`.

## 🛠️ Installation

Assurez-vous d'avoir Python installé (version 3.10 ou supérieure recommandée).

1. Clonez ce dépôt ou copiez les fichiers du projet.
2. Installez les bibliothèques nécessaires via le terminal :

```bash
pip install pandas matplotlib