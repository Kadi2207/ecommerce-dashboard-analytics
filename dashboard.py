import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="E-commerce Analytics", layout="wide", page_icon="📊")

# Titre principal
st.title("🛍️ Dashboard E-commerce Analytics")
st.markdown("---")

# Charger données (mise en cache pour performance)
@st.cache_data
def load_data():
    df = pd.read_csv('data.csv', encoding='ISO-8859-1')
    return df

df = load_data()

# SECTION 1 : Métriques clés (KPIs)
st.header("📊 Indicateurs Clés")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Transactions", f"{len(df):,}")
with col2:
    st.metric("Clients Uniques", f"{df['CustomerID'].nunique():,}")
with col3:
    st.metric("Produits Uniques", f"{df['StockCode'].nunique():,}")
with col4:
    st.metric("Pays", f"{df['Country'].nunique()}")

st.markdown("---")

# SECTION 2 : Aperçu des données
st.header("👀 Aperçu des Données")
st.dataframe(df.head(100), use_container_width=True, height=300)

st.markdown("---")

# SECTION 3 : Statistiques descriptives
st.header("📈 Statistiques Descriptives")
st.dataframe(df.describe(), use_container_width=True)

st.markdown("---")

# SECTION 4 : Qualité des données
st.header("🔍 Qualité des Données")
col1, col2 = st.columns(2)

with col1:
    st.subheader("Valeurs Manquantes")
    missing = df.isnull().sum()
    missing_df = pd.DataFrame({
        'Colonne': missing.index, 
        'Valeurs Manquantes': missing.values,
        'Pourcentage': (missing.values / len(df) * 100).round(2)
    })
    missing_df = missing_df[missing_df['Valeurs Manquantes'] > 0]
    st.dataframe(missing_df, use_container_width=True)

with col2:
    st.subheader("Types de Données")
    types_df = pd.DataFrame({
        'Colonne': df.dtypes.index,
        'Type': df.dtypes.values.astype(str)
    })
    st.dataframe(types_df, use_container_width=True)

st.markdown("---")
st.success("✅ Dashboard chargé avec succès!")