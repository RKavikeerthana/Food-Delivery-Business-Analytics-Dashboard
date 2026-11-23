
import os
import matplotlib.pyplot as plt


def create_charts(df, output_dir="outputs"):
    # Create the output folder if it does not exist
    os.makedirs(output_dir, exist_ok=True)

    # Select delivered orders
    delivered_df = df[df["order_status"] == "Delivered"].copy()

    # Ensure order_date is in datetime format when available
    if "order_date" in df.columns:
        df = df.copy()
        df["order_date"] = __import__("pandas").to_datetime(
            df["order_date"], errors="coerce"
        )

    # --------------------------------------------------
    # Chart 1: Total Orders by Restaurant
    # --------------------------------------------------
    orders = df.groupby("restaurant")["order_id"].count().sort_index()

    plt.figure(figsize=(8, 5))
    orders.plot(kind="bar", edgecolor="black")
    plt.title("Total Orders by Restaurant")
    plt.xlabel("Restaurant")
    plt.ylabel("Number of Orders")
    plt.xticks(rotation=0)
    plt.grid(axis="y", linestyle="--", alpha=0.4)
    plt.tight_layout()
    plt.savefig(
        os.path.join(output_dir, "orders_by_restaurant.png"),
        dpi=150
    )
    plt.close()

    # --------------------------------------------------
    # Chart 2: Delivered Revenue by Restaurant
    # --------------------------------------------------
    revenue = (
        delivered_df.groupby("restaurant")["order_value"]
        .sum()
        .sort_index()
    )

    plt.figure(figsize=(8, 5))
    revenue.plot(kind="bar", edgecolor="black")
    plt.title("Delivered Revenue by Restaurant")
    plt.xlabel("Restaurant")
    plt.ylabel("Delivered Order Value")
    plt.xticks(rotation=0)
    plt.grid(axis="y", linestyle="--", alpha=0.4)
    plt.tight_layout()
    plt.savefig(
        os.path.join(output_dir, "delivered_revenue_by_restaurant.png"),
        dpi=150
    )
    plt.close()

    # --------------------------------------------------
    # Chart 3: Average Delivery Time by Restaurant
    # --------------------------------------------------
    if not delivered_df.empty:
        delivery_time = (
            delivered_df.groupby("restaurant")["delivery_time"]
            .mean()
            .sort_index()
        )

        plt.figure(figsize=(8, 5))
        delivery_time.plot(kind="bar", edgecolor="black")
        plt.title("Average Delivery Time by Restaurant")
        plt.xlabel("Restaurant")
        plt.ylabel("Average Delivery Time (minutes)")
        plt.xticks(rotation=0)
        plt.grid(axis="y", linestyle="--", alpha=0.4)
        plt.tight_layout()
        plt.savefig(
            os.path.join(output_dir, "delivery_time_by_restaurant.png"),
            dpi=150
        )
        plt.close()

    # --------------------------------------------------
    # Chart 4: Cancellation Rate by Restaurant
    # --------------------------------------------------
    restaurant_total = df.groupby("restaurant")["order_id"].count()

    restaurant_cancelled = (
        df[df["order_status"] == "Cancelled"]
        .groupby("restaurant")["order_id"]
        .count()
        .reindex(restaurant_total.index, fill_value=0)
    )

    cancellation_rate = (
        restaurant_cancelled / restaurant_total * 100
    )

    plt.figure(figsize=(8, 5))
    cancellation_rate.plot(kind="bar", edgecolor="black")
    plt.title("Cancellation Rate by Restaurant")
    plt.xlabel("Restaurant")
    plt.ylabel("Cancellation Rate (%)")
    plt.xticks(rotation=0)
    plt.grid(axis="y", linestyle="--", alpha=0.4)
    plt.tight_layout()
    plt.savefig(
        os.path.join(output_dir, "cancellation_rate_by_restaurant.png"),
        dpi=150
    )
    plt.close()

    # --------------------------------------------------
    # Chart 5: Order Status Distribution
    # --------------------------------------------------
    status_counts = df["order_status"].value_counts()

    plt.figure(figsize=(7, 7))
    status_counts.plot(
        kind="pie",
        autopct="%1.1f%%",
        startangle=90
    )
    plt.title("Order Status Distribution")
    plt.ylabel("")
    plt.tight_layout()
    plt.savefig(
        os.path.join(output_dir, "order_status_distribution.png"),
        dpi=150
    )
    plt.close()

    # --------------------------------------------------
    # Chart 6: Order Value Distribution
    # --------------------------------------------------
    plt.figure(figsize=(8, 5))
    df["order_value"].plot(
        kind="hist",
        bins=6,
        edgecolor="black"
    )
    plt.title("Distribution of Order Values")
    plt.xlabel("Order Value")
    plt.ylabel("Number of Orders")
    plt.grid(axis="y", linestyle="--", alpha=0.4)
    plt.tight_layout()
    plt.savefig(
        os.path.join(output_dir, "order_value_distribution.png"),
        dpi=150
    )
    plt.close()

    # --------------------------------------------------
    # Chart 7: Monthly Delivered Revenue Trend
    # --------------------------------------------------
    if "order_date" in df.columns and not delivered_df.empty:
        monthly_revenue = (
            delivered_df.dropna(subset=["order_date"])
            .groupby(
                delivered_df.loc[
                    delivered_df["order_status"] == "Delivered",
                    "order_date"
                ].dt.to_period("M")
            )["order_value"]
            .sum()
        )

        if not monthly_revenue.empty:
            monthly_revenue.index = monthly_revenue.index.astype(str)

            plt.figure(figsize=(9, 5))
            monthly_revenue.plot(kind="line", marker="o")
            plt.title("Monthly Delivered Revenue Trend")
            plt.xlabel("Month")
            plt.ylabel("Delivered Revenue")
            plt.xticks(rotation=0)
            plt.grid(True, linestyle="--", alpha=0.4)
            plt.tight_layout()
            plt.savefig(
                os.path.join(output_dir, "monthly_revenue_trend.png"),
                dpi=150
            )
            plt.close()

    print("\nBusiness charts saved successfully in the outputs folder.")
