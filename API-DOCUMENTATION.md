# Food Management API Documentation

Version: 1.0.0  
Last Updated: May 22, 2025

## Overview

The Food Management API provides a comprehensive solution for managing various aspects of food service operations, including inventory management, food safety, sales forecasting, profit and loss analysis, food wastage tracking, and more.

## Base URL

All API endpoints are relative to the base URL of your deployment.

Example: `http://localhost:5000`

## Authentication

Some endpoints require authentication using JWT (JSON Web Token). For authenticated endpoints, include the JWT token in the Authorization header:

```
Authorization: Bearer <your_jwt_token>
```

## Response Format

All responses are returned in JSON format. Successful responses typically include a `success: true` flag and a `data` object containing the response data.

Error responses include a `success: false` flag and an `error` message.

## Error Codes

The API uses standard HTTP status codes:

- `200 OK`: Request succeeded
- `400 Bad Request`: Invalid request parameters
- `404 Not Found`: Resource not found
- `500 Internal Server Error`: Server-side error

## Available Endpoints

### Root
- [Get API Information](#get-api-information)

### Dashboard
- [Get Dashboard Statistics](#get-dashboard-statistics)

### Food Safety
- [Get Inspection Details](#get-inspection-details)
- [Update Inspection Records](#update-inspection-records)
- [Get Food Safety Statistics](#get-food-safety-statistics)

### Forecast
- [Get Forecast Information](#get-forecast-information)

### Inventory
- [Get All Inventory Items](#get-all-inventory-items)
- [Update Inventory Items](#update-inventory-items)
- [Delete Inventory Items](#delete-inventory-items)
- [Get Inventory Statistics](#get-inventory-statistics)
- [Export Inventory Data](#export-inventory-data)

### Profit & Loss
- [Get Profit & Loss Statistics](#get-profit--loss-statistics)
- [Get Revenue Details](#get-revenue-details)
- [Get Expense Details](#get-expense-details)
- [Get Financial Insights](#get-financial-insights)
- [Get Revenue & Expenses by Period](#get-revenue--expenses-by-period)

### About
- [Get About Information](#get-about-information)
- [Update About Information](#update-about-information)

### Food Fall (Wastage)
- [Get Food Wastage Statistics](#get-food-wastage-statistics)
- [Get Detailed Wastage by Period](#get-detailed-wastage-by-period)
- [Get Wasted Food Items](#get-wasted-food-items)
- [Get Wastage by Category](#get-wastage-by-category)
- [Get Wastage by Reason](#get-wastage-by-reason)
- [Get AI-driven Wastage Insights](#get-ai-driven-wastage-insights)

---

## Detailed Endpoint Documentation

### Get API Information

Provides general information about the API and available endpoints.

**URL**: `/`  
**Method**: `GET`  
**Authentication**: None

**Response Example**:
```json
{
    "name": "Food Management API",
    "version": "1.0.0",
    "description": "API for food management system with multiple modules",
    "endpoints": {
        "dashboard": "/dashboard",
        "foodsafety": "/foodsafety",
        "forecast": "/forecast",
        "inventory": "/inventory",
        "profitloss": "/profitloss",
        "about": "/about",
        "foodfall": "/foodfall"
    }
}
```

---

### Get Dashboard Statistics

Provides an overview of key metrics across all system modules.

**URL**: `/dashboard/stats`  
**Method**: `GET`  
**Authentication**: None

**Response Example**:
```json
{
    "success": true,
    "data": {
        "total_inventory": 1250,
        "low_stock_items": 15,
        "revenue_this_month": 45000,
        "expenses_this_month": 32000,
        "profit_this_month": 13000,
        "food_wastage_percentage": 4.2,
        "upcoming_inspections": 2
    }
}
```

---

### Get Inspection Details

Retrieves details about food safety inspections.

**URL**: `/foodsafety/inspection`  
**Method**: `GET`  
**Authentication**: None

**Response Example**:
```json
{
    "success": true,
    "data": {
        "last_inspection": "2025-04-15",
        "score": 96,
        "inspector": "Jane Smith",
        "issues": [
            {
                "id": 1,
                "description": "Temperature control in refrigerator #3",
                "severity": "minor"
            },
            {
                "id": 2, 
                "description": "Employee handwashing logs incomplete", 
                "severity": "minor"
            }
        ],
        "next_inspection_due": "2025-07-15"
    }
}
```

---

### Update Inspection Records

Updates food safety inspection records.

**URL**: `/foodsafety/inspection`  
**Method**: `PUT`  
**Authentication**: None

**Request Body**:
```json
{
    "date": "2025-05-22",
    "score": 98,
    "inspector": "John Doe",
    "issues": [
        {
            "description": "Missing temperature log for May 21",
            "severity": "minor"
        }
    ]
}
```

**Response Example**:
```json
{
    "success": true,
    "message": "Inspection data updated successfully",
    "updated_data": {
        "date": "2025-05-22",
        "score": 98,
        "inspector": "John Doe",
        "issues": [
            {
                "description": "Missing temperature log for May 21",
                "severity": "minor"
            }
        ]
    }
}
```

---

### Get Food Safety Statistics

Retrieves statistics related to food safety compliance.

**URL**: `/foodsafety/stats`  
**Method**: `GET`  
**Authentication**: None

**Response Example**:
```json
{
    "success": true,
    "data": {
        "inspection_score_trend": [92, 94, 96, 95, 96],
        "critical_violations_ytd": 0,
        "minor_violations_ytd": 5,
        "staff_certification_percentage": 100,
        "temperature_log_compliance": 98.5
    }
}
```

---

### Get Forecast Information

Provides forecasting data for sales, inventory, and demand trends.

**URL**: `/forecast/`  
**Method**: `GET`  
**Authentication**: None

**Response Example**:
```json
{
    "success": true,
    "data": {
        "sales_forecast": {
            "next_week": 35000,
            "next_month": 150000
        },
        "inventory_forecast": {
            "items_to_reorder": 12,
            "estimated_restock_cost": 4500
        },
        "demand_trends": {
            "increasing": ["organic produce", "plant-based alternatives"],
            "decreasing": ["canned goods", "frozen meals"]
        }
    }
}
```

---

### Get All Inventory Items

Retrieves all items in the inventory.

**URL**: `/inventory/`  
**Method**: `GET`  
**Authentication**: None

**Response Example**:
```json
{
    "ItemsCount": 3,
    "Items": [
        {
            "Name": "Milk",
            "Category": "Dairy",
            "Quantity": 100,
            "Quantity Type": "Liters",
            "Expiry Date": "30-05-2025"
        },
        {
            "Name": "Apples",
            "Category": "Produce",
            "Quantity": 250,
            "Quantity Type": "Kg",
            "Expiry Date": "10-06-2025"
        },
        {
            "Name": "Bread",
            "Category": "Bakery",
            "Quantity": 80,
            "Quantity Type": "Loaves",
            "Expiry Date": "25-05-2025"
        }
    ]
}
```

---

### Update Inventory Items

Adds or updates items in the inventory.

**URL**: `/inventory/`  
**Method**: `PUT`  
**Authentication**: None

**Request Body**:
```json
{
    "Name": "Rice",
    "Category": "Grains",
    "Quantity": 50,
    "Quantity Type": "Kg",
    "InDate": "20-05-2025",
    "Expiry Date": "20-11-2025"
}
```

**Response Example**:
```json
{
    "success": true,
    "message": "Inventory item added/updated successfully",
    "item": {
        "Name": "Rice",
        "Category": "Grains",
        "Quantity": 50,
        "Quantity Type": "Kg",
        "InDate": "20-05-2025",
        "Expiry Date": "20-11-2025"
    }
}
```

---

### Delete Inventory Items

Removes items from the inventory.

**URL**: `/inventory/`  
**Method**: `DELETE`  
**Authentication**: None

**Request Body**:
```json
{
    "items": [
        {
            "Name": "Expired Yogurt",
            "Category": "Dairy"
        }
    ]
}
```

**Response Example**:
```json
{
    "success": true,
    "message": "Inventory items deleted successfully",
    "deleted_items": {
        "items": [
            {
                "Name": "Expired Yogurt",
                "Category": "Dairy"
            }
        ]
    }
}
```

---

### Get Inventory Statistics

Retrieves statistics about the inventory.

**URL**: `/inventory/stats`  
**Method**: `GET`  
**Authentication**: None

**Response Example**:
```json
{
    "success": true,
    "data": {
        "total_items": 1250,
        "total_value": 187500,
        "categories": {
            "dairy": 120,
            "produce": 350,
            "meat": 95,
            "bakery": 175,
            "frozen": 210,
            "dry_goods": 300
        },
        "low_stock_items": 15,
        "expiring_soon": 28
    }
}
```

---

### Export Inventory Data

Provides a link to export inventory data in various formats.

**URL**: `/inventory/export`  
**Method**: `GET`  
**Authentication**: None

**Response Example**:
```json
{
    "success": true,
    "data": {
        "export_url": "https://example.com/exports/inventory_2025_05_22.csv",
        "export_date": "2025-05-22",
        "item_count": 1250,
        "formats_available": ["CSV", "JSON", "XLSX"]
    }
}
```

---

### Get Profit & Loss Statistics

Retrieves a summary of profit and loss figures.

**URL**: `/profitloss/stats`  
**Method**: `GET`  
**Authentication**: None

**Response Example**:
```json
{
    "Total Revanue": 45000,
    "Total Expenses": 32000,
    "Net Profit": 13000,
    "Profit Margin": 29
}
```

---

### Get Revenue Details

Provides detailed information about revenue sources.

**URL**: `/profitloss/revenue`  
**Method**: `GET`  
**Authentication**: None

**Response Example**:
```json
{
    "success": true,
    "data": {
        "revenue_by_category": {
            "dairy": 8500,
            "produce": 12000,
            "meat": 15000,
            "bakery": 5500,
            "frozen": 4000
        },
        "top_selling_items": [
            {"name": "Organic Eggs", "revenue": 2200},
            {"name": "Premium Beef", "revenue": 1800},
            {"name": "Fresh Bread", "revenue": 1500}
        ],
        "revenue_trend": [42000, 43500, 41000, 44500, 45000]
    }
}
```

---

### Get Expense Details

Provides detailed information about expense categories.

**URL**: `/profitloss/expenses`  
**Method**: `GET`  
**Authentication**: None

**Response Example**:
```json
{
    "success": true,
    "data": {
        "expenses_by_category": {
            "inventory": 22000,
            "labor": 6500,
            "utilities": 1800,
            "rent": 1500,
            "equipment": 200
        },
        "expense_trend": [30000, 31200, 30500, 31800, 32000],
        "highest_expense_items": [
            {"name": "Meat Products", "cost": 8500},
            {"name": "Staff Wages", "cost": 6500},
            {"name": "Dairy Products", "cost": 5000}
        ]
    }
}
```

---

### Get Financial Insights

Retrieves AI-generated financial insights and recommendations.

**URL**: `/profitloss/financialinsight`  
**Method**: `GET`  
**Authentication**: None

**Response Example**:
```json
{
    "Revenue Growth": "5.9%",
    "Profit Margin Trend": "Increasing at 0.7% per month",
    "Cost Reduction Opportunities": [
        "Optimize inventory management to reduce waste",
        "Consider bulk purchasing for high-volume ingredients",
        "Review utility usage patterns for potential savings"
    ],
    "Forecasted Growth": "7.2% increase expected next quarter",
    "Market Comparison": "Performing 3.7% above industry average",
    "Risk Factors": [
        "Seasonal fluctuations may impact Q3 revenue",
        "Rising ingredient costs could affect profit margins",
        "Labor market changes may increase staffing costs"
    ],
    "Recommendations": [
        "Introduce seasonal menu items to boost sales",
        "Implement inventory tracking system to reduce waste",
        "Consider loyalty program to increase customer retention"
    ]
}
```

---

### Get Revenue & Expenses by Period

Provides revenue and expense data for specified time periods.

**URL**: `/profitloss/revenue-expenses`  
**Method**: `GET`, `POST`  
**Authentication**: None

**Request Body (POST)**:
```json
{
    "BaseType": "M",
    "BaseCount": 3
}
```

Where:
- `BaseType`: Time period type (W = Weekly, M = Monthly, Y = Yearly, D = Daily)
- `BaseCount`: Number of periods to retrieve

**Response Example**:
```json
{
    "Revenue": {
        "Amount": [45000, 42500, 41000],
        "Category": [
            {"Food Items": 25000},
            {"Beverages": 15000},
            {"Other": 5000}
        ]
    },
    "Expenses": {
        "Amount": [32000, 30500, 29000],
        "Category": [
            {"Employee": 15000},
            {"Ingrediants": 12000},
            {"Other": 5000}
        ]
    }
}
```

---

### Get About Information

Retrieves information about the company or user, with different responses based on authentication level.

**URL**: `/about/`  
**Method**: `GET`  
**Authentication**: Optional (JWT)

**Response Example (Public)**:
```json
{
    "name": "FoodTech Solutions",
    "mobile_number": "555-987-6543",
    "Address": "123 Food Street, Delhi, India",
    "Description": "Authentic Indian cuisine with a modern twist."
}
```

**Response Example (Authenticated - Admin)**:
```json
{
    "user": {
        "name": "Admin User",
        "email": "admin@example.com",
        "mobile_number": "555-123-4567"
    },
    "company_data": {
        "company_name": "FoodTech Solutions",
        "Opening_Hours": "08:00",
        "Address": "123 Food Street, Delhi, India",
        "Description": "Authentic Indian cuisine with a modern twist."
    }
}
```

---

### Update About Information

Updates company or user information based on authentication level.

**URL**: `/about/`  
**Method**: `PUT`  
**Authentication**: Optional (JWT)

**Request Body (Public)**:
```json
{
    "name": "FoodTech Solutions",
    "mobile_number": "555-987-6543",
    "Address": "456 Cuisine Avenue, Delhi, India",
    "Description": "Authentic Indian cuisine with a modern twist."
}
```

**Request Body (Admin)**:
```json
{
    "user": {
        "name": "Admin User",
        "email": "admin@example.com",
        "mobile_number": "555-123-4567"
    },
    "company_data": {
        "company_name": "FoodTech Solutions",
        "Opening_Hours": "08:30",
        "Address": "456 Cuisine Avenue, Delhi, India",
        "Description": "Authentic Indian cuisine with a modern twist."
    }
}
```

**Response Example (Admin)**:
```json
{
    "success": true,
    "message": "Admin and company information updated successfully",
    "updated_data": {
        "user": {
            "name": "Admin User",
            "email": "admin@example.com",
            "mobile_number": "555-123-4567"
        },
        "company_data": {
            "company_name": "FoodTech Solutions",
            "Opening_Hours": "08:30",
            "Address": "456 Cuisine Avenue, Delhi, India",
            "Description": "Authentic Indian cuisine with a modern twist."
        },
        "role": "admin"
    }
}
```

---

### Get Food Wastage Statistics

Retrieves a summary of food wastage metrics.

**URL**: `/foodfall/stats`  
**Method**: `GET`  
**Authentication**: None

**Response Example**:
```json
{
    "Total Wastage": 1250,
    "Cost Impact": 1875,
    "Environmental Impact": 320
}
```

---

### Get Detailed Wastage by Period

Provides detailed food wastage data for specified time periods.

**URL**: `/foodfall/wastage`  
**Method**: `GET`, `POST`  
**Authentication**: None

**Request Body (POST)**:
```json
{
    "BaseType": "M",
    "BaseCount": 3
}
```

Where:
- `BaseType`: Time period type (W = Weekly, M = Monthly, Y = Yearly, D = Daily)
- `BaseCount`: Number of periods to retrieve

**Response Example**:
```json
{
    "Wastage": [980, 1050, 1250]
}
```

---

### Get Wasted Food Items

Retrieves the most wasted food items for specified time periods.

**URL**: `/foodfall/items`  
**Method**: `GET`, `POST`  
**Authentication**: None

**Request Body (POST)**:
```json
{
    "BaseType": "M",
    "BaseCount": 3
}
```

**Response Example**:
```json
{
    "Items": [
        {"Fried Rice": 32},
        {"Biryani": 28},
        {"Noodles": 22},
        {"Dosa": 18},
        {"Idly": 15}
    ]
}
```

---

### Get Wastage by Category

Retrieves food wastage data grouped by category.

**URL**: `/foodfall/category`  
**Method**: `GET`, `POST`  
**Authentication**: None

**Request Body (POST)**:
```json
{
    "BaseType": "M",
    "BaseCount": 3
}
```

**Response Example**:
```json
{
    "Category": [
        {"Rice Items": 450},
        {"Breakfast Items": 320},
        {"Side Dishes": 280},
        {"Beverages": 120},
        {"Desserts": 80}
    ]
}
```

---

### Get Wastage by Reason

Retrieves food wastage data grouped by reason for wastage.

**URL**: `/foodfall/reason`  
**Method**: `GET`, `POST`  
**Authentication**: None

**Request Body (POST)**:
```json
{
    "BaseType": "M",
    "BaseCount": 3
}
```

**Response Example**:
```json
{
    "Reason": [
        {"OverProduction": 625},
        {"Customer Returns": 300},
        {"Expired": 200},
        {"Quality Issues": 125}
    ]
}
```

---

### Get AI-driven Wastage Insights

Retrieves AI-generated insights and recommendations for reducing food wastage.

**URL**: `/foodfall/aiinsight`  
**Method**: `GET`  
**Authentication**: None

**Response Example**:
```json
{
    "Wastage Patterns": [
        "Fried Rice wastage increases by 18% during weekends",
        "Items prepared on Monday mornings have 12% higher wastage rate",
        "Reducing production quantities for dosas on Thursdays could save approximately ₹1,500 per month"
    ],
    "Recommendations": [
        "Adjust production for rice items to reduce by 15% on weekends",
        "Implement better forecasting for breakfast items to avoid overproduction",
        "Consider special offers for items that typically have higher wastage",
        "Review portion sizes for biryani as it shows consistent wastage"
    ],
    "Predicted Savings": {
        "Next Month": 8500,
        "Six Months": 60000,
        "Annual": 135000
    }
}
```

## Time Period Types

For endpoints that accept time period parameters:

- `W`: Weekly
- `M`: Monthly
- `Y`: Yearly
- `D`: Daily

## Authentication Notes

The API uses JWT (JSON Web Token) authentication for certain endpoints. To authenticate:

1. Include the JWT token in the Authorization header:
   ```
   Authorization: Bearer <your_jwt_token>
   ```

2. The token contains user role information which determines access levels:
   - `admin`: Full access to all endpoints and data
   - `manager`: Access to operational data but limited administrative functions
   - `employee`: Limited access based on role
   - Public (no token): Access to publicly available data only
