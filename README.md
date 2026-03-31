# 🛍️ Dashboard E-commerce Analytics

## 📊 Description
Dashboard interactif d'analyse de données e-commerce développé avec Python, Streamlit et Plotly.

Analyse de **397,884 transactions** sur 1 an (2010-2011) avec :
- 4,338 clients uniques
- 3,665 produits
- 37 pays

L'objectif était de transformer des données brutes en insights exploitables pour la prise de décision.

## Structure du projet
```
├── app.py              # Dashboard principal
├── nettoyage.py        # Pipeline de nettoyage des données
├── exploration.py      # Analyse exploratoire initiale
├── data.csv            # Données brutes
├── data_clean.csv      # Données nettoyées
└── requirements.txt    # Dépendances Python

## Analyses réalisées

Le dashboard présente plusieurs analyses clés :

**Indicateurs de performance**
- Chiffre d'affaires total et évolution mensuelle
- Volume de transactions et panier moyen
- Répartition géographique des ventes

**Analyses produits**
- Identification des best-sellers
- Analyse de la saisonnalité des ventes
- Comportements d'achat par jour et par heure

**Visualisations interactives**
- Graphiques temporels pour suivre les tendances
- Tableaux filtrables pour l'exploration détaillée
- Comparaisons entre pays et produits


## 🎯 Fonctionnalités
- ✅ KPIs clés (CA, transactions, panier moyen)
- ✅ Analyses temporelles (mensuel, jour, heure)
- ✅ Top produits et pays
- ✅ Tableau de données filtrable
- ✅ Graphiques interactifs

## Perspectives d'évolution

- Ajout de prédictions de ventes avec Machine Learning (ARIMA, Prophet)
- Segmentation clients avancée (RFM Analysis, clustering K-means)
- Analyse de la rétention et du churn
- Calcul de la Customer Lifetime Value (CLV)

## Auteur

**Kadidiatou Ibrahima Bagayoko**  
Étudiante en B2 Informatique - Spécialisation Data  
LinkedIn :  in/kadi-bagayoko

*Projet réalisé en janvier 2026 dans le cadre de la recherche de stage en Data Analytics*


| Technologie | Usage |
|------------|-------|
| Python 3.13 | Langage principal |
| Pandas  Manipulation et nettoyage des données |
| Plotly | Visualisations interactives |
| Streamlit | Interface web du dashboard |
| Git/GitHub | Versioning du code |

## 📁 Structure du projet
```
├── app.py                 # Dashboard principal
├── nettoyage.py          # Script de nettoyage
├── exploration.py        # Exploration initiale
├── data.csv              # Données brutes
├── data_clean.csv        # Données nettoyées
└── requirements.txt      # Dépendances


## Résultats clés

- **CA total** : £9,8M sur la période
- **Panier moyen** : £459
- **Pic de ventes** : Jeudi (£2M) vs autres jours (£1,5M en moyenne)
- **Top marché** : Royaume-Uni (83% du CA)
- **Best-seller** : Paper Craft Little Birdie (80k unités)


## 🚀 Lancer localement
```bash
pip install -r requirements.txt
streamlit run app.py
```

## 👨‍💻 Auteur
Kadidiatou Ibrahima Bagayoko - Étudiante en B2 - Spécialisation Data & IA 

Projet Data Analytics - Janvier 2026
