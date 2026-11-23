
from data import create_dataset
from data_cleaning import clean_dataset
from analysis import analyze_orders
from visualization import create_charts

# Step 1: Create dataset
df = create_dataset()

print("FOOD DELIVERY DATASET")
print(df)

# Step 2: Clean dataset
clean_df = clean_dataset(df)
clean_df.to_csv("outputs/cleaned_food_delivery_data.csv", index=False)

print("Cleaned dataset exported for Power BI.")

# Step 3: Analyze dataset
restaurant_summary = analyze_orders(clean_df)

# Step 4: Generate charts
create_charts(clean_df)

print("\nPROJECT COMPLETED SUCCESSFULLY")
