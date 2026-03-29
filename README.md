# Global Automotive Industry Analysis: EV Adoption & Market Shifts

This project is a comprehensive data analysis initiative focused on the global automotive industry, specifically exploring the adoption of **Plug-in Electric Vehicles (PEVs)** and their impact on long-term and short-term vehicle sales and production.

## Project Overview
The goal of this project is to analyze market sentiment towards electric vehicles and determine how adoption patterns affect global car cycles. We investigate whether developed markets are experiencing a "reboot" in their vehicle replacement cycles due to early EV adoption, potentially leading to a near-term slowdown in total sales.

## Testable Hypotheses
1.  **Socio-Economic Adoption Curve**: In countries with strong cultural support for green energy, individuals with pro-environmental attitudes and higher economic means adopt PEVs earlier. Those with lower economic means adopt them more gradually, maintaining a preference for conventional internal combustion engine (ICE) vehicles.
2.  **Market Saturation & Cycle Reset**: Rapid adoption in wealthy, pro-environmental markets has modified the vehicle buying cycle. This "reboot" resulted in a surge of recent purchases, which may lead to a subsequent slowdown in future sales as the need for new vehicles is deferred.

## Visual Findings & Analysis
> **Interactive Dashboard**: You can view and interact with the full high-resolution analysis on [Tableau Public here](https://public.tableau.com/app/profile/marcus.timm).

The following charts highlight the structural transition of the market:

### 1. Sales Trends vs. EV Market Share
![Change in Sales vs EV Share](reports/figures/ChangeSales_EV_Share.png)
*Observations show that developed countries with higher EV adoption rates have seen a decrease in car sales since 2018, while developing countries with lower EV adoption are seeing sales growth.*

### 2. Global Production: Long-Term Trends & Regional Snapshots
![Vehicle Production](reports/figures/VehicleProduction.png)
*This composite visualization analyzes the structural shift in global manufacturing across three key dimensions:*
*   **ICE vs. EV Production**: A long-term comparison of total Internal Combustion Engine vs. Electric Vehicle production volumes.
*   **2023 & 2024 Regional Breakdowns**: Side-by-side snapshots of total production for the **World, China, Europe, and the USA**, illustrating how major economies are navigating the transition at different speeds.

### 3. Total Sales & EV Growth
<p align="center">
  <img src="reports/figures/SALES.png" width="45%" />
  <img src="reports/figures/EVs_sold.png" width="45%" />
</p>
*While total car sales have seen fluctuations, EV sales growth suggests a bifurcated market where wealthier consumers are front-loading their vehicle replacements.*

## Key Insights
*   **Replacement Cycles**: The transition to EVs in wealthier markets has accelerated replacement cycles. Once these fleets are upgraded, demand for further replacements is deferred for years, slowing near-term growth.
*   **Bifurcated Market**: The majority of consumers globally remain committed to conventional vehicles, creating a split adoption curve based on income and regional environmental policy.
*   **Investment Perspective**: Short-term growth may appear muted due to market saturation, but long-term demand for EV infrastructure and battery supply chains remains on a steady expansion path.

## Critical Context & Caveats
When interpreting these trends, it is essential to consider confounding variables that impact the car cycle:
*   **Pandemic Effects**: Significant distortion in supply chains and consumer behavior (2020-2022).
*   **Economic Factors**: High inflation and rising interest rates reducing purchasing power.
*   **Policy Cycles**: Changes in government subsidies and environmental regulations.

---

## Technical Workflow: The Hybrid Data Pipeline
This project utilizes a **Hybrid Data Engineering approach** to ensure both reproducibility and high data quality:
1.  **Automated Cleaning**: Python scripts (located in `src/`) perform the initial scraping, standardization, and reshaping of raw Wikipedia data.
2.  **Manual & AI Enrichment**: To address gaps in public data, missing information was manually researched and patched using AI-assisted verification.
3.  **The "Patch" Logic**: The analysis notebook (`notebooks/01_data_cleaning_and_preparation.ipynb`) uses a `combine_first` logic to merge automated results with the manually enriched interim data (`data/interim/`), ensuring manual fixes take precedence.

## Setup & Usage
1.  **Environment**: Create a virtual environment and install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
2.  **Data Processing**: Run the Jupyter Notebook in `notebooks/` to regenerate the final `Cleaned_Tables`.
3.  **Visualization**: Use the CSVs in `data/processed/Cleaned_Tables/` to power the Tableau visualizations.
