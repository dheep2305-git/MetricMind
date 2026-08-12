METRICS = {

    "total_sales": {
        "name": "Total Sales",
        "description": "Total revenue generated",
        "formula": "SUM(Sales)",
        "column": "Sales"
    },

    "total_profit": {
        "name": "Total Profit",
        "description": "Total profit generated",
        "formula": "SUM(Profit)",
        "column": "Profit"
    },

    "profit_margin": {
        "name": "Profit Margin",
        "description": "Profit percentage",
        "formula": "(SUM(Profit)/SUM(Sales))*100"
    },

    "total_orders": {
        "name": "Total Orders",
        "description": "Number of unique orders",
        "formula": "COUNT(Order ID)",
        "column": "Order ID"
    }
}