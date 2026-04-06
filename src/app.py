import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Title
st.title("📊 Student Placement Analysis Dashboard")

# Load data
df = pd.read_csv('data/placement_data.csv')

# Show dataset
st.subheader("Dataset")
st.dataframe(df)

# Placement count
st.subheader("Placement Status Count")
fig1, ax1 = plt.subplots()
sns.countplot(x='PlacementStatus', data=df, ax=ax1)
st.pyplot(fig1)

# CGPA vs Salary
st.subheader("CGPA vs Salary")
fig2, ax2 = plt.subplots()
sns.scatterplot(x='CGPA', y='Salary', hue='PlacementStatus', data=df, ax=ax2)
st.pyplot(fig2)

# Branch-wise placement
st.subheader("Branch-wise Placement")
fig3, ax3 = plt.subplots()
sns.countplot(x='Branch', hue='PlacementStatus', data=df, ax=ax3)
st.pyplot(fig3)

# Heatmap
st.subheader("Correlation Heatmap")
numeric_df = df.select_dtypes(include=['int64', 'float64'])
fig4, ax4 = plt.subplots()
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', ax=ax4)
st.pyplot(fig4)