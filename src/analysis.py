import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Create outputs folder if not exists
os.makedirs('../outputs', exist_ok=True)

# Load dataset
df = pd.read_csv('../data/placement_data.csv')

# Basic info
print("First 5 rows:")
print(df.head())

print("\nDataset Info:")
print(df.info())

print("\nStatistics:")
print(df.describe())

# Placement count
print("\nPlacement Count:")
print(df['PlacementStatus'].value_counts())

# -------------------------
# Plot 1: Placement Status
# -------------------------
sns.countplot(x='PlacementStatus', data=df)
plt.title("Placement Status Count")
plt.savefig('../outputs/placement_status.png')
plt.show()

# -------------------------
# Plot 2: CGPA vs Salary
# -------------------------
sns.scatterplot(x='CGPA', y='Salary', hue='PlacementStatus', data=df)
plt.title("CGPA vs Salary")
plt.savefig('../outputs/cgpa_salary.png')
plt.show()

# -------------------------
# Plot 3: Branch-wise placement
# -------------------------
sns.countplot(x='Branch', hue='PlacementStatus', data=df)
plt.title("Branch-wise Placement")
plt.savefig('../outputs/branch_placement.png')
plt.show()

# -------------------------
# Plot 4: Correlation Heatmap
# -------------------------
numeric_df = df.select_dtypes(include=['float64', 'int64'])

sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.savefig('../outputs/heatmap.png')
plt.show()

print("\nAnalysis Completed Successfully ✅")