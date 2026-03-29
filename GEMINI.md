# GEMINI.md

## Project Overview

This project is a data analysis initiative focused on the global automotive industry, with a particular emphasis on Electric Vehicle (EV) adoption and its impact on vehicle sales and production. It investigates how socio-economic factors and environmental policies influence adoption curves and the resulting shifts in vehicle replacement cycles.

## Directory Structure and Key Files

The project follows a professional data science repository structure, separating raw data, interim manually-enriched data, processed outputs, and reusable source code.

### Data Architecture
*   **`data/raw/`**: Contains original CSV files sourced from public datasets (e.g., Wikipedia).
*   **`data/interim/`**: Stores manually-enriched datasets that include human-researched values and AI-assisted data patching. These files are used to "patch" the automated cleaning outputs.
*   **`data/processed/Cleaned_Tables/`**: The final standardized and enriched datasets used for analysis and Tableau visualizations.
    *   `vehicle_production.csv`
    *   `ev_3.csv` (Historical Market Share)
    *   `vehicles_per_capita1.csv`
    *   `trade_data.csv`

### Source Code (`src/`)
Reorganized into functional sub-modules for clarity and maintainability:
*   **`src/ev_use/`**: Scripts for scraping and cleaning EV-specific adoption tables.
*   **`src/vehicle_production/`**: Utilities for merging annual production datasets.
*   **`src/vehicles_per_capita/`**: Data cleaning and scraping scripts for per-capita metrics.
*   **`src/vehicle_exports/`**: Trade and export data processing scripts.

### Analysis & Reporting
*   **`notebooks/01_data_cleaning_and_preparation.ipynb`**: The primary data pipeline. It performs automated cleaning of raw data and merges it with the `data/interim/` patches using a `combine_first` logic.
*   **`reports/figures/`**: Contains the final Tableau visualizations (e.g., `ChangeSales_EV_Share.png`, `VehicleProduction.png`).
*   **`assets/`**: Supporting documentation including the original `Project.odt`.

## Workflow & Data Lineage

1.  **Extraction**: Python scripts in `src/` scrape raw data into `data/raw/`.
2.  **Enrichment**: Missing or inconsistent values are researched and stored in `data/interim/`.
3.  **Transformation**: The Jupyter Notebook executes the cleaning logic and applies the interim patches to generate the final `data/processed/` tables.
4.  **Visualization**: Final tables are imported into Tableau to generate interactive dashboards on **Tableau Public**, with static figures exported for the repository's reports. These dashboards address the project's hypotheses through high-resolution, interactive analysis.

This repository serves as a showcase for structured data engineering and insightful automotive market analysis.
