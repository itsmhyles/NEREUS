# NEREUS: Political & Climate Correlations with Homelessness

A data analysis project examining the relationships between homelessness rates, climate conditions, and political landscapes across US states (2010-2022).

> **Note**: This project is actively under development. Current findings are preliminary as additional features and data points are being incorporated into the analysis. Future updates will include more comprehensive variables such as housing costs, economic indicators, and local policy implementations.

## Key Findings

### Political Correlations
- Moderate positive correlation (0.418) between Democratic-leaning states and homelessness rates
- Democratic states show higher reported rates, potentially due to:
  - More comprehensive counting systems
  - Better-funded social services
  - More systematic documentation

### Climate Correlations
- Weak negative correlation (-0.215) between temperature and homelessness
- Counterintuitive finding: Colder states show slightly higher homelessness rates
- Urban concentration in colder states may influence this pattern

## Data Overview

**Coverage**: 624 observations across 48 states (2010-2022)

**Variables**:
- State
- Year
- Homeless_Rate
- Temperature
- Political_Index

## Methodology

### Data Sources
- Population: US Census Bureau
- Homelessness: HUD User Portal
- Political Data: Harvard Dataverse

### Analysis Methods

```python
# Core analysis components
import pandas as pd
from linearmodels import PanelOLS
from statsmodels.tsa.seasonal import seasonal_decompose
import geopandas as gpd
from sklearn.cluster import KMeans

## Future Development Plans

Currently working on incorporating:
- Housing cost analysis
- Economic indicators
- Local policy implementations
- Substance abuse program data
- More granular temperature data
- Seasonal migration patterns
- Urban vs. rural population distribution

## Contributing

As this project is actively evolving, contributions are welcome for:
- Additional data sources
- Improved analysis methods
- Enhanced visualization techniques
- Documentation improvements

## License

MIT License
