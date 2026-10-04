# Dashboard e-commerce : analyse de ventes

Dashboard interactif (Streamlit + Plotly) construit sur près de 400 000 lignes de transactions e-commerce : 6 indicateurs, 6 graphiques et un tableau filtrable, pour passer des données brutes à des constats chiffrés sur le chiffre d'affaires, les produits et les pays.

## Contexte

Projet réalisé en janvier 2026, dans le cadre de ma recherche de stage en Data Analytics. L'objectif : transformer des données brutes en indicateurs exploitables pour la prise de décision, de l'exploration du jeu au dashboard.

## Données

- **Jeu de données :** UCI Online Retail, transactions e-commerce du 1er décembre 2010 au 9 décembre 2011.
- **Données brutes (`data.csv`) :** 541 909 lignes, encodage ISO-8859-1.
- **Données nettoyées (`data_clean.csv`) :** 397 884 lignes, 18 532 factures, 4 338 clients, 3 665 produits, 37 pays.

## Démarche

`nettoyage.py` applique ces étapes, dans l'ordre :

| Étape | Lignes supprimées |
|---|---|
| Transactions sans `CustomerID` | 135 080 |
| Produits sans description (après l'étape précédente) | 0 |
| Quantités négatives ou nulles (retours, annulations) | 8 905 |
| Prix unitaires nuls ou négatifs | 40 |

Il crée ensuite `TotalAmount` (quantité × prix unitaire), convertit `InvoiceDate` en date et extrait l'année, le mois, le jour, l'heure et le jour de la semaine. `app.py` lit `data_clean.csv` et affiche :

- **6 indicateurs :** chiffre d'affaires, transactions (factures), clients, produits, panier moyen, quantité moyenne ;
- **6 graphiques :** chiffre d'affaires mensuel, top 10 des pays, top 10 des produits vendus, ventes par jour de la semaine, ventes par heure, distribution du montant des transactions ;
- **un tableau filtrable** par pays, mois et montant minimum (100 premières lignes affichées).

## Résultats et limites

Chiffres recalculés sur `data_clean.csv` :

- **Chiffre d'affaires total :** £8,91 M sur la période.
- **Panier moyen :** £481 par facture.
- **Royaume-Uni :** 82 % du chiffre d'affaires.
- **Mois le plus fort :** novembre 2011, £1,16 M.
- **Jour de la semaine le plus fort :** jeudi, £1,98 M (aucune vente enregistrée le samedi).
- **Produit le plus vendu en quantité :** « PAPER CRAFT , LITTLE BIRDIE », 80 995 unités.

Limites :

- Décembre 2011 est **partiel** : les données s'arrêtent au 9 décembre (8 jours de vente). Le dernier point de la courbe mensuelle n'est pas comparable aux autres.
- Le nettoyage retire les retours et annulations, et les lignes sans `CustomerID` (près de 25 % des lignes brutes) : le chiffre d'affaires porte sur les ventes avec client identifié et ne tient pas compte des retours.
- Le panier moyen est la moyenne des montants par facture, sans retrait des commandes exceptionnelles.
- Aucun test automatisé ni outil de contrôle de code n'est configuré.

## Structure du dépôt

```
├── .devcontainer/        Configuration Codespaces (lance app.py)
├── app.py                Dashboard principal (lit data_clean.csv)
├── nettoyage.py          Nettoyage : data.csv -> data_clean.csv
├── exploration.py        Exploration initiale des données brutes
├── dashboard.py          Première version du dashboard (lit data.csv)
├── data.csv              Données brutes
├── data_clean.csv        Données nettoyées
└── requirements.txt      Dépendances Python
```

## Reproduire

Depuis le dossier du dépôt (les scripts utilisent des chemins relatifs) :

```bash
pip install -r requirements.txt
python nettoyage.py        # facultatif : régénère data_clean.csv
streamlit run app.py       # dashboard sur http://localhost:8501
```

## Stack

| Technologie | Usage |
|---|---|
| Python, pandas | Nettoyage et calculs |
| Streamlit | Interface du dashboard |
| Plotly | Graphiques interactifs |
| Git / GitHub | Versioning |

## Autrice

**Kadidiatou Ibrahima Bagayoko**, étudiante en Bachelor en Intelligence Artificielle (grade Licence), ECE Paris, spécialisation Data & IA (2024–2027). [LinkedIn](https://linkedin.com/in/kadi-bagayoko)
