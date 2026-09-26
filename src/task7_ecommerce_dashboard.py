"""Task 7 - Capstone: 2x2 e-commerce dashboard"""
import matplotlib.pyplot as plt
import pandas as pd
from utils import save

df = pd.DataFrame({
    'Day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
    'Orders': [45, 62, 58, 70, 95, 110, 80],
    'Revenue': [900, 1240, 1160, 1400, 1900, 2200, 1600],
})
cat_names = ['Electronics', 'Clothing', 'Home', 'Books']
cat_revenue = [4200, 3100, 2000, 1100]

fig, axes = plt.subplots(2, 2, figsize=(13, 9))

# Line chart - revenue is a trend over ordered time.
axes[0, 0].plot(df['Day'], df['Revenue'], marker='o', color='darkgreen', linewidth=2)
axes[0, 0].set(title='Daily Revenue Trend', xlabel='Day', ylabel='Revenue ($)')

# Bar chart - comparing discrete categories (days).
axes[0, 1].bar(df['Day'], df['Orders'], color='skyblue', edgecolor='grey')
axes[0, 1].set(title='Orders by Day', xlabel='Day', ylabel='Number of Orders')

# Scatter plot - relationship between two numeric variables.
axes[1, 0].scatter(df['Orders'], df['Revenue'], color='crimson', s=80)
axes[1, 0].set(title='Orders vs Revenue', xlabel='Orders', ylabel='Revenue ($)')

# Pie chart - part-to-whole, and only 4 categories with clear gaps.
axes[1, 1].pie(cat_revenue, labels=cat_names, autopct='%1.1f%%', startangle=140,
               colors=['#ff9999', '#66b3ff', '#99ff99', '#ffcc99'])
axes[1, 1].set_title('Revenue Share by Category')

# So what? Saturday is the peak for both orders and revenue, and revenue rises in step with orders.
# Electronics drives about 40% of revenue, so protect its stock and marketing.
save('task7_ecommerce_dashboard')
