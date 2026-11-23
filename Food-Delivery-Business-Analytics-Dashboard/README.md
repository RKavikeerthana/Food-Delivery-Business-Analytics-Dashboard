# Food Delivery Business Analytics Dashboard (Power BI)

## Overview
This project analyzes food delivery order data to explore sales performance, restaurant-level metrics, order status, cancellations, delivery times, and trends. It combines Python data preparation/analysis with a Power BI dashboard.

## Project Contents
- `food.pbix` — Power BI report file
- `orders.csv` — source dataset
- `data.py`, `data_cleaning.py` — data-related helpers/cleaning scripts
- `analysis.py` — analysis routines
- `visualization.py` — visualization code
- `main.py` — project entry point (if applicable)
- `outputs/` — generated charts and cleaned/summary CSVs

## Insights Covered
- Orders by restaurant
- Delivered revenue by restaurant
- Monthly revenue trend
- Cancellation rate by restaurant
- Delivery time by restaurant
- Order status distribution
- Order value distribution

## Tools & Technologies
- Power BI
- Python
- Pandas (if used in scripts)
- Data visualization

## How to Use
1. Open `food.pbix` in Power BI Desktop to view the dashboard.
2. Review `orders.csv` as the input dataset.
3. If using the Python scripts, open this folder in VS Code and review `main.py` and related modules.
4. Generated files are available under `outputs/`.

## Note
The dashboard and analysis are for learning and portfolio demonstration. Ensure any shared dataset is anonymized and contains no sensitive or personal data.
