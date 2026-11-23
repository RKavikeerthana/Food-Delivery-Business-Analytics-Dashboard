
def analyze_orders(df):
    print("\n" + "=" * 55)
    print("FOOD DELIVERY BUSINESS ANALYSIS")
    print("=" * 55)

    total_orders = len(df)

    delivered_df = df[df["order_status"] == "Delivered"].copy()
    cancelled_df = df[df["order_status"] == "Cancelled"].copy()

    # 1. Order summary
    delivered_orders = len(delivered_df)
    cancelled_orders = len(cancelled_df)

    delivery_rate = (
        delivered_orders / total_orders * 100 if total_orders else 0
    )
    cancellation_rate = (
        cancelled_orders / total_orders * 100 if total_orders else 0
    )

    print("\n1. ORDER SUMMARY")
    print("Total Orders:", total_orders)
    print("Delivered Orders:", delivered_orders)
    print("Cancelled Orders:", cancelled_orders)
    print("Delivery Rate:", round(delivery_rate, 2), "%")
    print("Cancellation Rate:", round(cancellation_rate, 2), "%")

    # 2. Order value and revenue
    print("\n2. ORDER VALUE AND REVENUE")

    total_order_value = df["order_value"].sum()
    delivered_revenue = delivered_df["order_value"].sum()
    average_order_value = df["order_value"].mean()
    average_delivered_order_value = delivered_df["order_value"].mean()

    print("Total Order Value (including cancellations):", total_order_value)
    print("Delivered Order Value:", delivered_revenue)
    print("Average Order Value:", round(average_order_value, 2))
    print(
        "Average Delivered Order Value:",
        round(average_delivered_order_value, 2)
    )

    # 3. Delivery time
    print("\n3. DELIVERY PERFORMANCE")

    if not delivered_df.empty:
        average_delivery_time = delivered_df["delivery_time"].mean()

        print(
            "Average Delivery Time:",
            round(average_delivery_time, 2),
            "minutes"
        )
        print("Fastest Delivery:", delivered_df["delivery_time"].min(), "minutes")
        print("Longest Delivery:", delivered_df["delivery_time"].max(), "minutes")
    else:
        print("No delivered orders available.")

    # 4. Customer ratings
    print("\n4. CUSTOMER SATISFACTION")

    valid_ratings = delivered_df["rating"].dropna()

    if not valid_ratings.empty:
        print("Average Delivered-Order Rating:", round(valid_ratings.mean(), 2))
        print("Highest Rating:", valid_ratings.max())
        print("Lowest Rating:", valid_ratings.min())
    else:
        print("No ratings available for delivered orders.")

    # 5. Restaurant performance
    print("\n5. RESTAURANT PERFORMANCE")

    restaurant_summary = df.groupby("restaurant").agg(
        total_orders=("order_id", "count"),
        delivered_orders=("order_status", lambda s: (s == "Delivered").sum()),
        cancelled_orders=("order_status", lambda s: (s == "Cancelled").sum()),
        total_order_value=("order_value", "sum")
    )

    delivered_by_restaurant = delivered_df.groupby("restaurant").agg(
        delivered_revenue=("order_value", "sum"),
        average_delivery_time=("delivery_time", "mean"),
        average_rating=("rating", "mean")
    )

    restaurant_summary = restaurant_summary.join(
        delivered_by_restaurant, how="left"
    ).round(2)

    print(restaurant_summary)

    # 6. Cancellation rate by restaurant
    print("\n6. CANCELLATION RATE BY RESTAURANT")

    restaurant_cancellations = (
        df.groupby("restaurant")
        .agg(
            total_orders=("order_id", "count"),
            cancelled_orders=("order_status", lambda s: (s == "Cancelled").sum())
        )
    )

    restaurant_cancellations["cancellation_rate_pct"] = (
        restaurant_cancellations["cancelled_orders"]
        / restaurant_cancellations["total_orders"]
        * 100
    ).round(2)

    print(restaurant_cancellations)

    # 7. Business insights
    print("\n7. KEY BUSINESS INSIGHTS")

    if not restaurant_summary.empty:
        top_restaurant = restaurant_summary["total_orders"].idxmax()
        print("Restaurant with the Most Orders:", top_restaurant)

    if not delivered_by_restaurant.empty:
        avg_times = delivered_by_restaurant["average_delivery_time"].dropna()

        if not avg_times.empty:
            slowest_restaurant = avg_times.idxmax()
            print("Longest Average Delivery Time:", slowest_restaurant)

        avg_ratings = delivered_by_restaurant["average_rating"].dropna()

        if not avg_ratings.empty:
            highest_rated_restaurant = avg_ratings.idxmax()
            print("Highest Average Rating:", highest_rated_restaurant)

    if total_orders:
        print(
            "Business Recommendation:",
            "Investigate cancellations and review delivery performance."
        )

    
    # 8. Monthly business analysis
    print("\n8. MONTHLY BUSINESS ANALYSIS")

    monthly_df = df.copy()

    monthly_df["month"] = (
        monthly_df["order_date"].dt.to_period("M")
    )

    monthly_summary = monthly_df.groupby("month").agg(
        total_orders=("order_id", "count"),
        cancelled_orders=(
            "order_status",
            lambda s: (s == "Cancelled").sum()
        )
    )

    monthly_revenue = (
        monthly_df[monthly_df["order_status"] == "Delivered"]
        .groupby("month")["order_value"]
        .sum()
        .rename("delivered_revenue")
    )

    monthly_summary = monthly_summary.join(
        monthly_revenue,
        how="left"
    )

    monthly_summary["delivered_revenue"] = (
        monthly_summary["delivered_revenue"].fillna(0)
    )

    print(monthly_summary)

        


    return restaurant_summary
