import pandas as pd
import numpy as np
import os

df = pd.read_csv('uber.csv')
print(df.head())

print("Shape of dataset:", df.shape)
print("\nNumber of duplicated rows:", df.duplicated().sum())
print("\nData types:")
print(df.dtypes)
print("\nSummary statistics (numerical):")
print(df.describe())
print("\nSummary statistics (categorical):")
print(df.describe(include='object'))

print("\nMissing values per column:")
print(df.isnull().sum())
print("\nPercentage of missing values per column:")
print((df.isnull().sum() / len(df) * 100).round(2))

print("\nNumber of unique values per column:")
print(df.nunique())

numeric_columns = df.select_dtypes(include=['number']).columns
df[numeric_columns] = df[numeric_columns].fillna(df[numeric_columns].mean())
df.fillna(df.mode().iloc[0], inplace=True)

df.drop_duplicates(inplace=True)

print("=== MEAN VALUES ===")
print()
numerical_cols = df.select_dtypes(include=[np.number]).columns
print("Mean for numerical columns:")
for col in numerical_cols:
    mean_value = df[col].mean()
    print(f"{col}: {mean_value:.4f}")

print()
print("All means at once:")
print(df.mean())

print("\nMedian for specific columns:")
if 'fare_amount' in df.columns:
    print(f"Fare Amount Median: {df['fare_amount'].median():.4f}")
if 'passenger_count' in df.columns:
    print(f"Passenger Count Median: {df['passenger_count'].median():.4f}")

print("=== MODE VALUES ===")
print("Mode for all columns:")
modes = df.mode()
for column in df.columns:
    mode_values = df[column].mode()
    if len(mode_values) > 0:
        print(f"{column}: {mode_values.iloc[0]}")
    else:
        print(f"{column}: No mode found")

print("\nAll modes at once (first row):")
print(df.mode().iloc[0])

print("\nSpecific column modes:")
if 'fare_amount' in df.columns:
    print(f"fare_amount: {df['fare_amount'].mode().iloc[0] if len(df['fare_amount'].mode()) > 0 else 'No mode'}")
if 'pickup_longitude' in df.columns:
    print(f"pickup_longitude: {df['pickup_longitude'].mode().iloc[0] if len(df['pickup_longitude'].mode()) > 0 else 'No mode'}")
if 'pickup_latitude' in df.columns:
    print(f"pickup_latitude: {df['pickup_latitude'].mode().iloc[0] if len(df['pickup_latitude'].mode()) > 0 else 'No mode'}")
if 'dropoff_longitude' in df.columns:
    print(f"dropoff_longitude: {df['dropoff_longitude'].mode().iloc[0] if len(df['dropoff_longitude'].mode()) > 0 else 'No mode'}")
if 'dropoff_latitude' in df.columns:
    print(f"dropoff_latitude: {df['dropoff_latitude'].mode().iloc[0] if len(df['dropoff_latitude'].mode()) > 0 else 'No mode'}")
if 'passenger_count' in df.columns:
    print(f"passenger_count: {df['passenger_count'].mode().iloc[0] if len(df['passenger_count'].mode()) > 0 else 'No mode'}")

print("=== STANDARD DEVIATION VALUES ===")
std_devs = df.std(numeric_only=True)
for column, std_val in std_devs.items():
    print(f"{column}: {std_val}")

print("\nAll standard deviations at once:")
print(df.std(numeric_only=True))

print("\nSample standard deviation (default, ddof=1):")
print(df.std(numeric_only=True))

print("\nPopulation standard deviation (ddof=0):")
print(df.std(numeric_only=True, ddof=0))

print("\nStandard deviation with mean for context:")
for column in df.select_dtypes(include=[np.number]).columns:
    mean_val = df[column].mean()
    std_val = df[column].std()
    print(f"{column}: mean={mean_val:.4f}, std={std_val:.4f}")

print("\nCoefficient of Variation (std/mean):")
for column in df.select_dtypes(include=[np.number]).columns:
    mean_val = df[column].mean()
    std_val = df[column].std()
    if mean_val != 0:
        cv = std_val / abs(mean_val)
        print(f"{column}: {cv:.4f}")
    else:
        print(f"{column}: Cannot calculate CV (mean is zero)")

print("\n=== QUARTILES & RANGE ===")
if 'fare_amount' in df.columns:
    print(f"Q1: {df['fare_amount'].quantile(0.25)}")
    print(f"Q2 (Median): {df['fare_amount'].quantile(0.50)}")
    print(f"Q3: {df['fare_amount'].quantile(0.75)}")
    print(df['fare_amount'].describe())

print("OUTLIERS IDENTIFICATION")
def identify_outliers(data):
    Q1 = data['fare_amount'].quantile(0.25)
    Q3 = data['fare_amount'].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = df[(df['fare_amount'] < lower_bound) | (df['fare_amount'] > upper_bound)]
    return outliers

if 'fare_amount' in df.columns:
    outlier_data = identify_outliers(df)
    print("Outliers:", outlier_data)

print("=== SAVING ENHANCED DATASET FOR POWER BI ===")
output_dir = "enhanced_data_for_powerbi"
os.makedirs(output_dir, exist_ok=True)

csv_path = os.path.join(output_dir, "enhanced_dataset.csv")
df.to_csv(csv_path, index=False, encoding='utf-8')
print("SUCCESS: CSV saved - enhanced_dataset.csv")

excel_path = os.path.join(output_dir, "enhanced_dataset.xlsx")
df.to_excel(excel_path, index=False, engine='openpyxl')
print("SUCCESS: Excel saved - enhanced_dataset.xlsx")

parquet_path = os.path.join(output_dir, "enhanced_dataset.parquet")
df.to_parquet(parquet_path, index=False)
print("SUCCESS: Parquet saved - enhanced_dataset.parquet")

print(f"\n=== SAVE SUMMARY ===")
print(f"Dataset shape: {df.shape}")
print(f"Files saved in: {os.path.abspath(output_dir)}")
print(f"Records: {len(df):,}")
print(f"Columns: {len(df.columns)}")

print(f"\n=== POWER BI IMPORT STEPS ===")
print("1. Open Power BI Desktop")
print("2. Click 'Get Data' → 'Text/CSV'")
print(f"3. Navigate to: {os.path.abspath(output_dir)}")
print("4. Select 'enhanced_dataset.csv'")
print("5. Click 'Load'")

print("\nREADY FOR POWER BI IMPORT!")
