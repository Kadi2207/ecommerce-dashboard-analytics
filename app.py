import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Configuration de la page
st.set_page_config(
    page_title="E-commerce Analytics Dashboard",
    page_icon="🛍️",
    layout="wide"
)

# Charger les données nettoyées
@st.cache_data
def load_data():
    df = pd.read_csv('data_clean.csv')
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    return df

df = load_data()

# ========================================
# HEADER
# ========================================
st.title("🛍️ Dashboard E-commerce Analytics")
st.markdown("**Analyse des ventes et comportements clients | Période : Déc 2010 - Déc 2011**")
st.markdown("---")

# ========================================
# KPIs PRINCIPAUX
# ========================================
st.header("📊 Indicateurs Clés de Performance (KPIs)")

# Calculs
total_revenue = df['TotalAmount'].sum()
total_transactions = df['InvoiceNo'].nunique()
total_customers = df['CustomerID'].nunique()
total_products = df['StockCode'].nunique()
avg_basket = df.groupby('InvoiceNo')['TotalAmount'].sum().mean()
avg_quantity = df['Quantity'].mean()

# Affichage en colonnes
col1, col2, col3, col4, col5, col6 = st.columns(6)

with col1:
    st.metric("💰 Chiffre d'Affaires", f"£{total_revenue:,.0f}")
with col2:
    st.metric("🧾 Transactions", f"{total_transactions:,}")
with col3:
    st.metric("👥 Clients", f"{total_customers:,}")
with col4:
    st.metric("📦 Produits", f"{total_products:,}")
with col5:
    st.metric("🛒 Panier Moyen", f"£{avg_basket:,.2f}")
with col6:
    st.metric("📊 Qté Moyenne", f"{avg_quantity:.1f}")

st.markdown("---")

# ========================================
# GRAPHIQUES - LIGNE 1
# ========================================
st.header("📈 Analyses des Ventes")

col1, col2 = st.columns(2)

with col1:
    # Évolution du CA mensuel
    st.subheader("💹 Évolution du Chiffre d'Affaires Mensuel")
    monthly_revenue = df.groupby(df['InvoiceDate'].dt.to_period('M'))['TotalAmount'].sum().reset_index()
    monthly_revenue['InvoiceDate'] = monthly_revenue['InvoiceDate'].astype(str)
    
    fig = px.line(monthly_revenue, x='InvoiceDate', y='TotalAmount',
                  labels={'InvoiceDate': 'Mois', 'TotalAmount': 'CA (£)'},
                  markers=True)
    fig.update_traces(line_color='#1f77b4', line_width=3)
    fig.update_layout(height=400, hovermode='x unified')
    st.plotly_chart(fig, use_container_width=True)

with col2:
    # Top 10 pays par CA
    st.subheader("🌍 Top 10 Pays par Chiffre d'Affaires")
    top_countries = df.groupby('Country')['TotalAmount'].sum().sort_values(ascending=False).head(10)
    
    fig = px.bar(x=top_countries.values, y=top_countries.index, orientation='h',
                 labels={'x': 'CA (£)', 'y': 'Pays'},
                 color=top_countries.values, color_continuous_scale='Blues')
    fig.update_layout(height=400, showlegend=False)
    st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# ========================================
# GRAPHIQUES - LIGNE 2
# ========================================
col1, col2 = st.columns(2)

with col1:
    # Top 10 produits les plus vendus
    st.subheader("🏆 Top 10 Produits les Plus Vendus")
    top_products = df.groupby('Description')['Quantity'].sum().sort_values(ascending=False).head(10)
    
    fig = px.bar(x=top_products.values, y=top_products.index, orientation='h',
                 labels={'x': 'Quantité Vendue', 'y': 'Produit'},
                 color=top_products.values, color_continuous_scale='Greens')
    fig.update_layout(height=400, showlegend=False)
    st.plotly_chart(fig, use_container_width=True)

with col2:
    # Ventes par jour de la semaine
    st.subheader("📅 Ventes par Jour de la Semaine")
    day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    day_sales = df.groupby('DayOfWeek')['TotalAmount'].sum().reindex(day_order)
    
    fig = px.bar(x=day_sales.index, y=day_sales.values,
                 labels={'x': 'Jour', 'y': 'CA (£)'},
                 color=day_sales.values, color_continuous_scale='Oranges')
    fig.update_layout(height=400, showlegend=False)
    st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# ========================================
# GRAPHIQUES - LIGNE 3
# ========================================
col1, col2 = st.columns(2)

with col1:
    # Ventes par heure de la journée
    st.subheader("⏰ Ventes par Heure de la Journée")
    hourly_sales = df.groupby('Hour')['TotalAmount'].sum()
    
    fig = px.line(x=hourly_sales.index, y=hourly_sales.values,
                  labels={'x': 'Heure', 'y': 'CA (£)'},
                  markers=True)
    fig.update_traces(line_color='#d62728', line_width=3)
    fig.update_layout(height=400)
    st.plotly_chart(fig, use_container_width=True)

with col2:
    # Distribution du panier moyen
    st.subheader("💰 Distribution du Montant des Transactions")
    basket_amounts = df.groupby('InvoiceNo')['TotalAmount'].sum()
    basket_amounts_filtered = basket_amounts[basket_amounts < 1000]  # Filtrer les outliers
    
    fig = px.histogram(basket_amounts_filtered, nbins=50,
                       labels={'value': 'Montant (£)', 'count': 'Nombre de transactions'},
                       color_discrete_sequence=['#9467bd'])
    fig.update_layout(height=400, showlegend=False)
    st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# ========================================
# TABLEAU DE DONNÉES
# ========================================
st.header("📋 Données Détaillées")

# Filtres
col1, col2, col3 = st.columns(3)
with col1:
    countries = ['Tous'] + sorted(df['Country'].unique().tolist())
    selected_country = st.selectbox("🌍 Filtrer par Pays", countries)
with col2:
    months = ['Tous'] + sorted(df['Month'].unique().tolist())
    selected_month = st.selectbox("📅 Filtrer par Mois", months)
with col3:
    min_amount = st.number_input("💰 Montant minimum", min_value=0, value=0)

# Appliquer les filtres
df_filtered = df.copy()
if selected_country != 'Tous':
    df_filtered = df_filtered[df_filtered['Country'] == selected_country]
if selected_month != 'Tous':
    df_filtered = df_filtered[df_filtered['Month'] == selected_month]
df_filtered = df_filtered[df_filtered['TotalAmount'] >= min_amount]

# Afficher le tableau
st.dataframe(
    df_filtered[['InvoiceNo', 'InvoiceDate', 'Description', 'Quantity', 
                 'UnitPrice', 'TotalAmount', 'Country']].head(100),
    use_container_width=True,
    height=400
)

st.markdown("---")

# ========================================
# FOOTER
# ========================================
st.success("✅ Dashboard créé avec Streamlit & Plotly | Projet Data Analytics E-commerce")
