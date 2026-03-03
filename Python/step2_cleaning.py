import pandas as pd

# Step 1: Load dataset
df = pd.read_csv("../data/orders.csv", encoding='latin1')

print("Original Shape:", df.shape)

# Step 2: Remove duplicate rows
df = df.drop_duplicates()
print("After removing duplicates:", df.shape)

# Step 3: Check missing values
print("\nMissing values before cleaning:")
print(df.isnull().sum())

# Step 4: Fill missing Postal Code with 0
if 'Postal Code' in df.columns:
    df['Postal Code'] = df['Postal Code'].fillna(0)

# Step 5: Convert Order Date to datetime
if 'Order Date' in df.columns:
    df['Order Date'] = pd.to_datetime(df['Order Date'])

# Step 6: Create Year and Month columns
df['Year'] = df['Order Date'].dt.year
df['Month'] = df['Order Date'].dt.month

# Step 7: Save cleaned dataset
df.to_csv("../data/orders_cleaned.csv", index=False)

print("\nCleaning completed!")
print("File saved as orders_cleaned.csv")