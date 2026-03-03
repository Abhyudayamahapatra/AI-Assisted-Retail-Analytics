import pandas as pd

# Load cleaned data
df = pd.read_csv(r"C:\AI Assisted Retail sales Analytics\data\orders_cleaned.csv")
print("AI Assistant Ready!")
print("You can ask:")
print("- total sales")
print("- total profit")
print("- sales by category")
print("- profit by region")
print("- top products")
print("- type 'exit' to stop\n")

while True:
    query = input("Ask a question: ").lower()

    if query == "exit":
        print("Assistant closed.")
        break

    elif "total sales" in query:
        print("Total Sales:", df['Sales'].sum())

    elif "total profit" in query:
        print("Total Profit:", df['Profit'].sum())

    elif "sales by category" in query:
        print(df.groupby('Category')['Sales'].sum())

    elif "profit by region" in query:
        print(df.groupby('Region')['Profit'].sum())

    elif "top products" in query:
        top_products = (
            df.groupby('Product Name')['Sales']
            .sum()
            .sort_values(ascending=False)
            .head(5)
        )
        print(top_products)

    else:
        print("Sorry, I don't understand that question.")