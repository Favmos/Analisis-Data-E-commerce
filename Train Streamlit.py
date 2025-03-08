import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Set title
st.title("E-Commerce Data Dashboard")

st.markdown(
    """
    Nama      : Abdul Rezak
     <br>
    Cohort ID : A452YBF004
    """, unsafe_allow_html=True
)

# Load datasets
dataset_path = r"C:\Users\MSI GAMING\Downloads\Dicoding\E-commerce-public-dataset\E-Commerce Public Dataset"

order_items = pd.read_csv(os.path.join(dataset_path, "order_items_dataset.csv"))
products = pd.read_csv(os.path.join(dataset_path, "products_dataset.csv"))
category_translation = pd.read_csv(os.path.join(dataset_path, "product_category_name_translation.csv"))
orders = pd.read_csv(os.path.join(dataset_path, "orders_dataset.csv"))

# Data preprocessing
orders['order_purchase_timestamp'] = pd.to_datetime(orders['order_purchase_timestamp'])
orders['order_delivered_customer_date'] = pd.to_datetime(orders['order_delivered_customer_date'])
orders['delivery_time_days'] = (orders['order_delivered_customer_date'] - orders['order_purchase_timestamp']).dt.days

# Merging datasets for category analysis
merged_data = order_items.merge(products, on="product_id", how="left")
merged_data = merged_data.merge(category_translation, on="product_category_name", how="left")
category_counts = merged_data['product_category_name_english'].value_counts().reset_index()
category_counts.columns = ['Product Category', 'Total Sold']

# Sidebar navigation
st.sidebar.header("Navigation")
page = st.sidebar.radio("Go to", ["Product Analysis", "Delivery Time Analysis"])

if page == "Product Analysis":
    st.subheader("Top 10 Best Selling Product Categories")
    fig, ax = plt.subplots(figsize=(10,5))
    sns.barplot(data=category_counts.head(10), x='Total Sold', y='Product Category', palette='viridis', ax=ax)
    ax.set_xlabel("Total Sold")
    ax.set_ylabel("Product Category")
    ax.set_title("Top 10 Best Selling Product Categories")
    st.pyplot(fig)

elif page == "Delivery Time Analysis":
    st.subheader("Distribution of Delivery Time")
    fig, ax = plt.subplots(figsize=(10,5))
    sns.histplot(orders['delivery_time_days'].dropna(), bins=30, kde=True, color='blue', ax=ax)
    ax.set_xlabel("Delivery Time (Days)")
    ax.set_ylabel("Frequency")
    ax.set_title("Distribution of Delivery Time")
    st.pyplot(fig)
    
    st.write("### Delivery Time Statistics")
    st.write(orders['delivery_time_days'].describe())
