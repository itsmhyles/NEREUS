## Proposed Political Index Components

1. **Legislative Control (40% weight)**
- Senate representation (20%)
  - Democrat_Percentage ranges from 0-100
  - Already normalized in dataset
- House representation (20%)
  - Democrat_Percentage ranges from 0-100
  - Already normalized in dataset

2. **Executive Control (35% weight)**
- Gubernatorial party control
  - Democrat = 100
  - Republican = 0
  - Independent = 50

3. **Presidential Elections (25% weight)**
- Democrat_Percentage from presidential results
- Interpolate between election years since elections occur every 4 years

## Index Calculation Formula

```python
def calculate_political_index(year, state, senate_df, house_df, pres_df, gov_df):
    # Legislative Score (40%)
    senate_score = senate_df.loc[(senate_df['Year'] == year) & 
                                (senate_df['State'] == state), 'Democrat_Percentage'].iloc[0] * 0.20
    
    house_score = house_df.loc[(house_df['Year'] == year) & 
                              (house_df['State'] == state), 'Democrat_Percentage'].iloc[0] * 0.20
    
    # Executive Score (35%)
    gov_party = gov_df.loc[(gov_df['year'] == year) & 
                          (gov_df['state'] == state), 'party'].iloc[0]
    gov_score = 100 if gov_party == 'Democrat' else (50 if gov_party == 'Independent' else 0)
    gov_score = gov_score * 0.35
    
    # Presidential Score (25%)
    pres_score = pres_df.loc[(pres_df['Year'] == year) & 
                            (pres_df['State'] == state), 'Democrat_Percentage'].iloc[0] * 0.25
    
    # Total Political Index (0-100 scale)
    total_score = senate_score + house_score + gov_score + pres_score
    
    return total_score
```

## Interpretation

- **Scale**: 0-100
  - 0 = Strongly Republican
  - 50 = Perfect balance
  - 100 = Strongly Democratic

- **Thresholds**:
  - 0-40: Strong Republican control
  - 40-45: Lean Republican
  - 45-55: Competitive/Mixed
  - 55-60: Lean Democratic
  - 60-100: Strong Democratic control

## Rationale for Weights

1. **Legislature (40%)**
- Highest weight due to direct policy control
- Split between chambers to reflect bicameral influence
- Continuous measure captures strength of control

2. **Governor (35%)**
- Significant executive power
- Veto authority
- Policy implementation control

3. **Presidential (25%)**
- Indicator of overall state political preferences
- Lower weight due to national vs. state focus
- Helps smooth temporal variations

## Implementation Considerations

1. **Data Preprocessing**
- Handle missing values
- Standardize state names
- Ensure consistent party coding

2. **Temporal Consistency**
- Interpolate presidential data between elections
- Account for special elections/appointments
- Handle mid-year changes in control

3. **Validation**
- Cross-reference with historical analyses
- Check against known political shifts
- Verify index sensitivity to changes

This methodology provides a balanced approach to measuring state political leanings while accounting for different aspects of political control and their relative importance in state governance.
