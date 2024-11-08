# NEREUS: Political & Climate Correlations with Homelessness

A data analysis project examining the relationships between homelessness rates, climate conditions, and political landscapes across US states (2010-2022).

> **Note**: This project is actively under development. Current findings are preliminary as additional features and data points are being incorporated into the analysis.

## Key Categorical Findings

### Political Categories

**Conservative States**
- Mean homelessness rate: 107.89 per 100,000
- Standard deviation: 40.43
- Range: 21.22 to 314.59
- Most consistent rates across all categories

**Liberal States**
- Mean homelessness rate: 194.34 per 100,000
- Standard deviation: 110.38
- Range: 62.71 to 507.94
- Highest variability in rates

### Temperature Categories

**Cold States**
- Mean homelessness rate: 180.35 per 100,000
- Standard deviation: 102.43
- Range: 67.31 to 507.94
- Higher rates across political categories

**Warm States**
- Mean homelessness rate: 124.92 per 100,000
- Less variable than cold states
- Range: 21.22 to 439.34

### CoC Coverage Analysis

**Medium Coverage Areas**
- Mean homelessness rate: 157.82 per 100,000
- Standard deviation: 101.16
- Range: 21.22 to 473.39
- Shows highest variability

## Key Interactions

### Political-Temperature
- Liberal states maintain higher rates regardless of temperature
- Cold + Liberal combination shows highest rates
- Conservative states maintain lower rates across temperatures

### Political-CoC
- CoC coverage is not a strong predictor of rates
- Liberal states show higher rates regardless of CoC coverage
- Medium CoC coverage shows most variability

### Temperature-CoC
- Cold states show higher rates across all CoC levels
- Warm states show more consistent rates
- CoC coverage effect is less significant than temperature

## Data Overview

### Coverage
624 observations across 48 states (2010-2022)

### Sample Data Point
```python
State: AL
Year: 2010
Homeless_Rate: 126.34
Temperature: 62.7°F
Political_Index: 12.6346
CoCs_per_hundredthousands: 0.167174

### Distribution Statistics
```python
Homeless_Rate statistics:
- Mean: 144.76 per 100,000
- Std: 84.31
- Min: 21.22
- Max: 507.94
```

## Methodology

### Political Index Calculation
- State Legislature Control (40% weight)
- Executive Control (30% weight)
- Presidential Election Results (30% weight)

### Analysis Methods
```python
def comprehensive_analysis(homeless_df, climate_df, political_df):
    return {
        'panel': panel_results,
        'time_series': time_trends,
        'spatial': spatial_patterns,
        'clusters': clusters,
        'fixed_effects': fe_results
    }
```

## Data Sources

### Primary Sources
- Population: US Census Bureau
- Homelessness: HUD User Portal
- Political Data: Harvard Dataverse
  - US Governors Dataset
  - Presidential Election Data
  - House Election Data
- Continuums of Care (CoCs): HUD Exchange

### Citations
- Kaplan, Jacob. United States Governors 1775-2020
- MIT Election Data and Science Lab, U.S. President 1976–2020
- MIT Election Data and Science Lab, U.S. House 1976–2022

## Known Limitations

### Data Collection Issues
- Point-in-Time counts are underestimates
- Methodology varies by community
- Inconsistent reporting across states

### Confounding Variables
- Housing costs
- Cost of living
- Local policies
- Economic indicators
- Social services availability

## Repository Structure

```
NEREUS/
├── climate_data/
│   ├── raw_temperature_data.csv
│   ├── processed_climate_data.csv
│   └── climate_analysis.py
├── drafts/
│   └── preliminary_analysis.md
├── homeless_data/
│   ├── HUD_PIT_data.csv
│   ├── processed_homeless_rates.csv
│   └── homeless_analysis.py
├── political_files/
│   ├── governors_data.csv
│   ├── presidential_data.csv
│   ├── house_data.csv
│   └── political_index_calculator.py
├── population_per_state/
│   ├── census_data.csv
│   └── population_processor.py
├── read_mes/
│   ├── data_sources.md
│   ├── methodology.md
│   └── results.md
├── regression_models/
│   ├── basic_ml_models.py
│   ├── time_series.py
│   ├── climate_regression.py
│   ├── model_check.py
│   └── random_forests.py
├── regression_results/
│   ├── model_outputs/
│   ├── visualizations/
│   └── summary_statistics.md
├── .gitignore
├── requirements.txt
└── README.md
```

## Future Development

### Planned Features
- Housing cost analysis
- Economic indicators
- Local policy implementations
- Mental health services availability
- Substance abuse program data
- More granular temperature data
- Urban vs. rural population distribution

### Research Questions
- Is there a stronger correlation between climate and homelessness than political affiliation?
- How does the COC contribute to homelessness rate?
- Do states with similar climates have similar homelessness patterns regardless of political control?

## Contributing

Contributions welcome for:
- Additional data sources
- Improved analysis methods
- Enhanced visualization techniques
- Documentation improvements

## License

MIT License
```
