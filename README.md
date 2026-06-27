# Global Automotive Industry Analysis: EV Adoption & Vehicle Sales

This project explores whether higher EV adoption is associated with weaker vehicle sales in mature markets. Using public data on EV adoption, vehicle sales, production, ownership, and trade, it compares trends across countries to identify broader patterns in the automotive industry.

## Project Overview

The analysis compares EV adoption, vehicle sales, production, ownership, and trade across countries to identify broader patterns in the automotive industry.

## Skills Demonstrated

- Data collection and web scraping
- Data cleaning and transformation with pandas
- Combining multiple public datasets
- Exploratory data analysis
- Tableau dashboard development
- Geographic and time-series analysis
- Data validation and manual quality checks

## Dataset

Public datasets include:

- Wikipedia country-level tables
- OICA vehicle production data
- Manually verified corrections where needed

## Methodology

1. Collect public automotive datasets.
2. Clean and standardize the data with Python.
3. Combine datasets into country-level tables.
4. Analyze the results in Jupyter.
5. Visualize the findings in Tableau.

## Figures

Interactive Tableau dashboard: (https://public.tableau.com/app/profile/marcus.timm).

### Sales Trends vs. EV Market Share

![Change in Sales vs EV Share](reports/figures/ChangeSales_EV_Share.png)

### Global Production Snapshots

![Vehicle Production](reports/figures/VehicleProduction.png)

### Total Sales & EV Growth

<p align="center">
  <img src="reports/figures/SALES.png" width="45%" />
  <img src="reports/figures/EVs_sold.png" width="45%" />
</p>

## Results Summary

- EV adoption is highest in wealthier markets.
- Vehicle sales have generally weakened in countries with high EV adoption.
- Conventional vehicles still dominate in many markets.
- Vehicle demand is likely influenced by factors beyond EV adoption.

## Getting Started

### Prerequisites

- Python 3.8+
- Jupyter Notebook or JupyterLab

### Installation

```bash
git clone ...
cd ...
pip install -r requirements.txt
```

Open `notebooks/01_data_cleaning_and_preparation.ipynb` and run the notebook from top to bottom.

## Limitations

- The analysis is exploratory and does not establish causation.
- Public datasets required manual cleaning and validation.
- Macroeconomic factors such as inflation and interest rates were not modeled.
- Country-specific policies were not modeled.

## Future Improvements

- Expand the analysis to additional countries.
- Include manufacturer-level sales data.
- Add more years as new data becomes available.
- Build additional interactive dashboards.

## License

The code and original project materials are released under the [MIT License](LICENSE).

Third-party data sources remain subject to their own licenses and terms of use.
