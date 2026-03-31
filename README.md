# Global Automotive Industry Analysis: EV Adoption & Market Shifts

This project is a comprehensive data analysis initiative focused on the global automotive industry, specifically exploring the adoption of **Plug-in Electric Vehicles (PEVs)** and their impact on long-term and short-term vehicle sales and production.

---

## Table of Contents
1.  [Project Overview](#project-overview)
2.  [Getting Started](#getting-started)
    *   [Prerequisites](#prerequisites)
    *   [Installation](#installation)
3.  [Project Structure](#project-structure)
4.  [Data Analysis Plan](#data-analysis-plan)
5.  [Hypotheses and Conclusions](#hypotheses-and-conclusions)
6.  [Contributing](#contributing)
7.  [License](#license)

---

## 1. Project Overview
The goal of this project is to analyze market sentiment towards electric vehicles and determine how adoption patterns affect global car cycles. We investigate whether developed markets are experiencing a "reboot" in their vehicle replacement cycles due to early EV adoption, potentially leading to a near-term slowdown in total sales.

## 2. Getting Started

### Prerequisites
*   Python 3.8+
*   Jupyter Notebook / JupyterLab
*   Tableau Desktop or Tableau Public (for interacting with dashboards)

### Installation
1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/cars_data_analysis.git
    cd cars_data_analysis
    ```
2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate
    ```
3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## 3. Project Structure
The repository is organized into a modular, professional data science structure:
*   `data/`: Contains raw, interim (manually enriched), and processed datasets.
*   `notebooks/`: Jupyter Notebooks for data cleaning and preparation.
*   `src/`: Modular Python scripts for scraping and initial data processing.
*   `reports/figures/`: Exported static visualizations for the README.
*   `assets/`: Supporting project documentation and original files.

## 4. Data Analysis Plan
This project utilizes a **Hybrid Data Engineering approach** to ensure both reproducibility and high data quality:
1.  **Automated Cleaning**: Python scripts in `src/` perform initial scraping and standardization.
2.  **Manual & AI Enrichment**: Missing information is manually researched and patched using AI-assisted verification in the `data/interim/` folder.
3.  **The "Patch" Logic**: The analysis notebook (`notebooks/01_data_cleaning_and_preparation.ipynb`) uses `combine_first` logic to merge automated results with manual patches.
4.  **Tableau Integration**: Processed data is fed into interactive dashboards for structural trend analysis.

## 5. Hypotheses and Conclusions

### Testable Hypotheses
*   **Socio-Economic Adoption Curve**: Higher economic means and pro-environmental attitudes lead to earlier PEV adoption.
*   **Market Saturation & Cycle Reset**: Rapid early adoption in developed markets creates a "reboot" in buying cycles, potentially slowing near-term future sales.

### Visual Findings
> **Interactive Dashboard**: You can view and interact with the full high-resolution analysis on [Tableau Public here](https://public.tableau.com/app/profile/marcus.timm).

#### Sales Trends vs. EV Market Share
![Change in Sales vs EV Share](reports/figures/ChangeSales_EV_Share.png)
*Developed countries with higher EV adoption rates show a decrease in sales since 2018 compared to developing markets.*

#### Global Production Snapshots
![Vehicle Production](reports/figures/VehicleProduction.png)
*Comparison of total production volumes across the World, China, Europe, and the USA (2023-2024).*

#### Total Sales & EV Growth
<p align="center">
  <img src="reports/figures/SALES.png" width="45%" />
  <img src="reports/figures/EVs_sold.png" width="45%" />
</p>

### Final Conclusions
*   **Replacement Cycles**: The transition to EVs in wealthier markets has front-loaded demand, leading to a deferral of replacements and slowing near-term growth.
*   **Bifurcated Market**: The majority of consumers globally remain committed to conventional vehicles, creating a split adoption curve based on income and regional environmental policy.
*   **Investment Perspective**: Short-term growth may appear muted due to market saturation, but long-term demand for EV infrastructure and battery supply chains remains on a steady expansion path.
*   **Critical Context**: Final results must be interpreted alongside **Pandemic Effects**, **Inflation/Interest Rates**, and **Policy Cycles**.

## 6. Contributing
This is a personal analysis project. Suggestions and feedback are welcome! Please open an issue or submit a pull request if you have ideas for improving the data enrichment or analysis.

## 7. License
This project is for educational and showcase purposes. Data sources (Wikipedia, OICA) remain the property of their respective owners.
