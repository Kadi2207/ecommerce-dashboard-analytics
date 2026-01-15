# 📊 EXPLORATION DES DONNÉES E-COMMERCE
# découverte de notre dataset

import pandas as pd

# 1. Chargement des données
print("🔄 Chargement des données...")
df = pd.read_csv('data.csv', encoding='ISO-8859-1')
print("✅ Données chargées avec succès!\n")

# 2. Informations générales
print("=" * 50)
print("📋 INFORMATIONS GÉNÉRALES")
print("=" * 50)
print(f"Nombre de lignes : {len(df)}")
print(f"Nombre de colonnes : {len(df.columns)}")
print(f"\nNom des colonnes :")
for i, col in enumerate(df.columns, 1):
    print(f"  {i}. {col}")

# 3. Aperçu des premières lignes
print("\n" + "=" * 50)
print("👀 APERÇU DES 5 PREMIÈRES LIGNES")
print("=" * 50)
print(df.head())

# 4. Types de données
print("\n" + "=" * 50)
print("🔢 TYPES DE DONNÉES")
print("=" * 50)
print(df.dtypes)

# 5. Statistiques de base
print("\n" + "=" * 50)
print("📊 STATISTIQUES DE BASE")
print("=" * 50)
print(df.describe())

# 6. Valeurs manquantes
print("\n" + "=" * 50)
print("❓ VALEURS MANQUANTES")
print("=" * 50)
missing = df.isnull().sum()
print(missing[missing > 0])

print("\n✅ Exploration terminée!")