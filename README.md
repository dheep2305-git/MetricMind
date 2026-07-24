# MetricMind

## Project Overview

MetricMind is an AI-powered Business Intelligence platform that allows users to ask business questions in natural language. The system uses an LLM to understand user queries, a semantic layer to ensure consistent business metrics, and a cloud data warehouse to retrieve enterprise data before presenting insights through an interactive dashboard.

## Technologies

- Snowflake
- Cube.dev
- LangChain
- LLM
- FastAPI
- Next.js
- GitHub

## Project Status

### Day 1
- Created GitHub repository.
- Initialized project structure.
- Added README.md, .gitignore, and requirements.txt.
- Organized folders for backend, frontend, API, LLM, semantic layer, docs, and data.

### Day 2
- Created backend, frontend, API, LLM, and semantic layer modules.
- Added project documentation.
- Added Superstore dataset to the project.
- Prepared the initial backend structure.

### Day 3
- Configured backend settings.
- Created dataset loading module.
- Added API route structure.
- Connected backend with the dataset.

### Day 4
- Added utility functions.
- Implemented dataset preview endpoint.
- Improved backend organization.
- Added basic error handling.

### Day 5
- Loaded the Superstore dataset using Pandas.
- Explored dataset structure and columns.
- Checked data types and missing values.
- Generated summary statistics for data understanding.

### Day 6
- Cleaned the Superstore dataset.
- Checked and handled duplicate records.
- Verified missing values.
- Converted date columns to datetime format.
- Created Year and Month columns.
- Saved the cleaned dataset for analysis.

### Day 7
- Performed exploratory data analysis (EDA).
- Calculated total sales, profit, and orders.
- Analyzed sales and profit by region.
- Analyzed sales by category.
- Identified top customers.
- Generated monthly sales insights.

### Day 8
- Configured the FastAPI backend.
- Started the backend server using Uvicorn.
- Verified backend functionality using Swagger UI.
- Tested the Home, Dataset Info, and Dataset Preview APIs.
- Prepared the backend for business analytics endpoints.

### Day 9
- Added business analytics API endpoints using FastAPI.
- Implemented total sales, total profit, and total orders calculations.
- Developed sales by region and sales by category APIs.
- Integrated dataset loading using Pandas.
- Tested all APIs using Swagger UI.
- Fixed backend routing and dataset loading issues.

### Day 10
- Added Monthly Sales API.
- Implemented Top Products API.
- Added Profit by Category API.
- Prepared backend data for dashboard visualizations.
- Tested all APIs successfully using Swagger UI.

### Day 11
- Created frontend project structure.
- Designed the initial dashboard layout.
- Added HTML, CSS, and JavaScript files.
- Prepared frontend for backend API integration.

## Day 12
- Connected the frontend dashboard with the FastAPI backend.
- Used JavaScript `fetch()` to retrieve live data from backend APIs.
- Displayed Total Sales on the dashboard.
- Displayed Total Profit on the dashboard.
- Displayed Total Orders on the dashboard.
- Verified communication between the frontend and backend.

## Day 13
- Connected frontend to backend APIs.
- Displayed Total Sales, Total Profit, and Total Orders dynamically.
- Fixed CORS issue between frontend and backend.
- Started building the Top Products section.

# Frontend - Day 14
### Dashboard Cards
- Display Total Sales
- Display Total Profit
- Display Total Orders
- Data fetched from FastAPI backend

### Sales by Region Chart
- Added Chart.js library
- Created a bar chart for regional sales
- Chart data fetched dynamically from backend API