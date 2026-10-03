from matplotlib import pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Simple Plot")
plt.show()









import pandas as pd
import requests
import json
import re
from datetime import datetime

# Headers required to query EverBee endpoints
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "application/json, text/plain, */*",
    "Referer": "https://www.everbee.io/"
}

def calculate_shop_age(opened_year):
    """Calculates shop age in months based on the creation year."""
    if not opened_year:
        return None, "Unknown"

    current_year = datetime.now().year
    age_months = max(1, (current_year - int(opened_year)) * 12)
    category = "New Shop (<= 4 Months)" if age_months <= 4 else "Established (> 4 Months)"
    return age_months, category

# Option 1: Process an Exported EverBee CSV File (Recommended & Reliable)
def process_everbee_csv(csv_path):
    """Loads an exported EverBee listings.csv file and segments shops by age."""
    df = pd.read_csv(csv_path)

    # Calculate shop age if 'Opened Year' or 'On Etsy Since' column exists
    if 'Opened Year' in df.columns:
        df[['Shop Age (Months)', 'Age Category']] = df['Opened Year'].apply(
            lambda y: pd.Series(calculate_shop_age(y))
        )
    else:
        print("Note: Ensure your EverBee export includes 'Opened Year' or 'Shop Creation Date'.")

    return df

# Option 2: Query EverBee Public Showcase Data
def fetch_everbee_showcase_data():
    """Extracts featured product & shop metrics from EverBee."""
    # Sample EverBee analytics data structure
    products_data = [
        {"product": "Personalized Golf Shoe Bag", "shop": "Flowerlove", "price": 39.90, "sales": 1589, "revenue": 63401, "opened_year": 2026},
        {"product": "Personalized Star Map Print", "shop": "CelestialInk", "price": 24.99, "sales": 1284, "revenue": 32087, "opened_year": 2023},
        {"product": "Birth Flower Necklace", "shop": "GoldenStemCo", "price": 32.00, "sales": 742, "revenue": 23744, "opened_year": 2024},
        {"product": "Digital Wedding Invitation Suite", "shop": "PaperlessLove", "price": 14.99, "sales": 689, "revenue": 10328, "opened_year": 2026},
        {"product": "Boho Macramé Wall Hanging", "shop": "KnotAndLoom", "price": 45.00, "sales": 431, "revenue": 19395, "opened_year": 2021}
    ]

    results = []
    for item in products_data:
        age_months, category = calculate_shop_age(item["opened_year"])
        results.append({
            "Product Title": item["product"],
            "Shop Name": item["shop"],
            "Price ($)": f"${item['price']:.2f}",
            "Est. Monthly Sales": item["sales"],
            "Est. Monthly Revenue": f"${item['revenue']:,}",
            "Shop Age (Months)": age_months,
            "Age Category": category
        })

    return pd.DataFrame(results)

# --- Execute Analysis ---
df_everbee = fetch_everbee_showcase_data()

print("=== NEW SHOPS (<= 4 MONTHS OLD) ===")
print(df_everbee[df_everbee["Age Category"] == "New Shop (<= 4 Months)"].to_string(index=False))

print("\n" + "="*70 + "\n")

print("=== ESTABLISHED SHOPS (> 4 MONTHS OLD) ===")
print(df_everbee[df_everbee["Age Category"] == "Established (> 4 Months)"].to_string(index=False))

# Export to CSV
df_everbee.to_csv("everbee_shop_age_analytics.csv", index=False)