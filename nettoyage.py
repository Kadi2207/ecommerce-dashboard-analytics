# 🧹 NETTOYAGE DES DONNÉES E-COMMERCE

import pandas as pd
import numpy as np

print("🔄 Chargement des données brutes...")
df = pd.read_csv('data.csv', encoding='ISO-8859-1')
print(f"✅ Données chargées : {len(df)} lignes\n")

# ========================================
# ÉTAPE 1 : Supprimer les lignes sans CustomerID
# ========================================
print("=" * 60)
print("ÉTAPE 1 : Supprimer les transactions sans CustomerID")
print("=" * 60)
avant = len(df)
df = df[df['CustomerID'].notna()]
apres = len(df)
print(f"Avant : {avant} lignes")
print(f"Après : {apres} lignes")
print(f"❌ Supprimées : {avant - apres} lignes ({((avant-apres)/avant*100):.2f}%)\n")

# ========================================
# ÉTAPE 2 : Supprimer les lignes avec Description manquante
# ========================================
print("=" * 60)
print("ÉTAPE 2 : Supprimer les produits sans description")
print("=" * 60)
avant = len(df)
df = df[df['Description'].notna()]
apres = len(df)
print(f"Avant : {avant} lignes")
print(f"Après : {apres} lignes")
print(f"❌ Supprimées : {avant - apres} lignes\n")

# ========================================
# ÉTAPE 3 : Supprimer les quantités négatives et nulles
# ========================================
print("=" * 60)
print("ÉTAPE 3 : Supprimer les retours/annulations (Quantity <= 0)")
print("=" * 60)
avant = len(df)
df = df[df['Quantity'] > 0]
apres = len(df)
print(f"Avant : {avant} lignes")
print(f"Après : {apres} lignes")
print(f"❌ Supprimées : {avant - apres} lignes\n")

# ========================================
# ÉTAPE 4 : Supprimer les prix négatifs ou nuls
# ========================================
print("=" * 60)
print("ÉTAPE 4 : Supprimer les prix <= 0")
print("=" * 60)
avant = len(df)
df = df[df['UnitPrice'] > 0]
apres = len(df)
print(f"Avant : {avant} lignes")
print(f"Après : {apres} lignes")
print(f"❌ Supprimées : {avant - apres} lignes\n")

# ========================================
# ÉTAPE 5 : Créer la colonne Montant Total
# ========================================
print("=" * 60)
print("ÉTAPE 5 : Créer la colonne 'TotalAmount' (Quantity × UnitPrice)")
print("=" * 60)
df['TotalAmount'] = df['Quantity'] * df['UnitPrice']
print(f"✅ Colonne 'TotalAmount' créée")
print(f"Exemple : {df['TotalAmount'].head(3).values}\n")

# ========================================
# ÉTAPE 6 : Convertir InvoiceDate en format date
# ========================================
print("=" * 60)
print("ÉTAPE 6 : Convertir InvoiceDate en format datetime")
print("=" * 60)
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
print(f"✅ Type avant : object → Type après : {df['InvoiceDate'].dtype}")
print(f"Exemple : {df['InvoiceDate'].iloc[0]}\n")

# ========================================
# ÉTAPE 7 : Créer des colonnes temporelles
# ========================================
print("=" * 60)
print("ÉTAPE 7 : Extraire Année, Mois, Jour, Heure")
print("=" * 60)
df['Year'] = df['InvoiceDate'].dt.year
df['Month'] = df['InvoiceDate'].dt.month
df['Day'] = df['InvoiceDate'].dt.day
df['Hour'] = df['InvoiceDate'].dt.hour
df['DayOfWeek'] = df['InvoiceDate'].dt.day_name()
print("✅ Colonnes créées : Year, Month, Day, Hour, DayOfWeek\n")

# ========================================
# RÉSUMÉ FINAL
# ========================================
print("=" * 60)
print("📊 RÉSUMÉ DU NETTOYAGE")
print("=" * 60)
print(f"✅ Données finales : {len(df)} lignes")
print(f"✅ Colonnes : {len(df.columns)}")
print(f"✅ Période : {df['InvoiceDate'].min()} → {df['InvoiceDate'].max()}")
print(f"✅ Clients uniques : {df['CustomerID'].nunique()}")
print(f"✅ Produits uniques : {df['StockCode'].nunique()}")
print(f"✅ Pays : {df['Country'].nunique()}")

# ========================================
# SAUVEGARDER LES DONNÉES NETTOYÉES
# ========================================
print("\n" + "=" * 60)
print("💾 Sauvegarde des données nettoyées...")
print("=" * 60)
df.to_csv('data_clean.csv', index=False, encoding='utf-8')
print("✅ Fichier sauvegardé : data_clean.csv")
print("\n🎉 NETTOYAGE TERMINÉ AVEC SUCCÈS!")