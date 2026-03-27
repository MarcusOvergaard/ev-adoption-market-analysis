# GEMINI.md

## Project Overview

This project is a data analysis initiative focused on the global automotive industry, with a particular emphasis on Electric Vehicle (EV) adoption and its impact on vehicle sales and production. It involves cleaning, reshaping, and analyzing various datasets related to car sales, production, and trade data to identify key trends, correlations, and country-specific insights. The ultimate goal appears to be to understand the market shifts, especially regarding the transition from Internal Combustion Engine (ICE) vehicles to EVs, and to visualize these findings.

## Directory Structure and Key Files

The project directory is organized to support a data analysis workflow, including raw data, processing scripts, and outputs for visualization and reporting.

### Data Files (`.csv`)
The core of this project relies on several CSV files containing various automotive industry data points. These files likely serve as the primary input for analysis:
*   `car_sales_long.csv`: Detailed car sales data, likely in a long format suitable for time-series analysis.
*   `country_car_sales_long.csv`: Car sales aggregated or categorized by country.
*   `ev_2.csv`, `ev_3.csv`: Data specifically related to electric vehicles, possibly different versions or types of EV data.
*   `table_3.csv`: A general table of data, its specific content would require further inspection.
*   `trade_data.csv`: Information regarding vehicle trade (imports/exports) between countries.
*   `vehicle_data_by_country_long.csv`, `vehicle_data_by_country.csv`: General vehicle data organized by country, potentially in different formats.
*   `vehicle_production.csv`: Data on vehicle production volumes.
*   `vehicles_per_capita1.csv`: Data related to vehicle ownership per capita.
*   `vehicles_sold_per_year.csv`: Annual vehicle sales data.

### Python Scripts (`.py`)
These scripts are crucial for data preparation, cleaning, and potentially initial analysis:
*   `check_missing_data.py`: Likely used to identify and report missing values within the datasets.
*   `update_ev_3.py`: Suggests a script designed to process or update the `ev_3.csv` dataset, possibly cleaning it or adding new derived features.

### Documentation and Analysis Blueprints
These files provide critical context on the project's methodology, analytical goals, and expected outputs:
*   `Notebook Structure.txt`: Outlines a standard structure for data analysis notebooks or reports, guiding the organization of findings from introduction to key takeaways. It also provides best practices for showing data cleaning and transformation steps.
*   `Tableau Charts Made.txt`: Details the specific analytical questions being addressed and the types of visualizations (e.g., line charts, slope charts, scatter plots, stacked area charts, maps) intended to answer these questions. This file serves as a blueprint for the visualization phase of the project, specifically mentioning Tableau as a tool.

### Specialized Directories
*   `Cleaned_Tables`: Likely stores processed and cleaned versions of the raw CSV data, ready for analysis.
*   `Electric car use by country`: Could contain data or analyses specific to EV usage patterns.
*   `List of countries and territories by motor vehicles per capita`, `List of countries by motor vehicle production`, `List of countries by vehicle exports`: These directories probably hold more granular or derived data related to specific aspects of the automotive industry.
*   `new-vehicle-sales-top50-assets`: Suggests this directory contains assets (images, reports, etc.) related to top 50 new vehicle sales, possibly for presentations or reports.

## Usage and Workflow

The typical workflow for this data analysis project involves:

1.  **Data Acquisition & Preparation:** Raw CSV data is sourced and then prepared using Python scripts like `check_missing_data.py` and `update_ev_3.py`. This involves cleaning, validating, and potentially transforming data into suitable formats (e.g., long format as suggested by `Notebook Structure.txt`). The `Cleaned_Tables` directory would store the output of this step.
2.  **Analysis & Visualization:** Following the analytical questions and visualization types outlined in `Tableau Charts Made.txt`, data is analyzed. This likely involves using data visualization tools like Tableau (as implied) or Python libraries to create informative charts and graphs. The project aims to understand trends in vehicle sales, EV adoption's correlation with overall sales, and the breakdown between ICE and EV sales.
3.  **Reporting & Documentation:** Findings are structured and presented, potentially in notebooks or reports, adhering to the organizational principles described in `Notebook Structure.txt`. The various specialized directories (e.g., `Electric car use by country`) might contain intermediate analysis results or final reports for specific topics.

This project is geared towards comprehensive insights into the evolving global automotive market.
