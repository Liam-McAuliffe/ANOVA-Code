import pandas as pd
from scipy.stats import f_oneway

# Create a DataFrame with the provided data
data = {
    'Transpiration_Rate': [3.36238433, 3.65191987, 2.59667625, 12.1595331, 3.80726121,
                           3.33733814, 1.36617354, 2.63123273, 1.27980888, 3.42691085,
                           1.19920053, 1.54115587, 0.904568069, 1.33401744, 2.47167868,
                           1.6540773, 0.431201759, 1.99435444, 2.10837023, 4.05043674,
                           1.12009259, 3.14603914, 2.65235754, 2.18146427, 1.54078888],
    'Humidity_Level': ['45', '45', '45', '45', '45', '64', '64', '64', '64', '64',
                       '71', '71', '71', '71', '71', '53', '53', '53', '53', '53',
                       '67', '67', '67', '67', '67']
}

df = pd.DataFrame(data)

# Perform one-way ANOVA
f_statistic, p_value = f_oneway(*[df[df['Humidity_Level'] == level]['Transpiration_Rate'] for level in df['Humidity_Level'].unique()])

# Print results
print(f'F-Statistic: {f_statistic}')
print(f'P-Value: {p_value}')
