# Retail Performance Analysis
import matplotlib.pyplot as plt
import numpy as np

# Data
quarters = ['Q1', 'Q2', 'Q3', 'Q4']
turnover_ratios = [3.4, 7.7, 5.41, 6.31]
average_ratio = 5.7
industry_target = 8

# Create the plot
plt.figure(figsize=(10, 6))
bar_colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']
plt.bar(quarters, turnover_ratios, color=bar_colors, label='Quarterly Turnover Ratio')

# Add a line for the average
plt.axhline(y=average_ratio, color='blue', linestyle='--', label=f'Average Ratio ({average_ratio:.2f})')

# Add a line for the industry target
plt.axhline(y=industry_target, color='red', linestyle='-', label=f'Industry Target ({industry_target})')

# Add titles and labels
plt.title('Inventory Turnover Ratio Analysis (2024)', fontsize=16)
plt.xlabel('Quarter', fontsize=12)
plt.ylabel('Turnover Ratio', fontsize=12)
plt.ylim(0, 10)
plt.legend()
plt.grid(axis='y', linestyle='--')

# Save the plot as a PNG file
plt.savefig('inventory_turnover.png')
