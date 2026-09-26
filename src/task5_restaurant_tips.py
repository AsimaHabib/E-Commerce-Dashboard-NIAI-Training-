"""Task 5 - Restaurant manager: when do customers tip best? (heatmap)"""
import matplotlib.pyplot as plt
import seaborn as sns
from utils import save

tips = sns.load_dataset('tips')
pivot = tips.pivot_table(index='day', columns='time', values='tip', aggfunc='mean', observed=True)
print(pivot.round(3))

plt.figure(figsize=(8, 5))
sns.heatmap(pivot, annot=True, cmap='YlGnBu', fmt='.2f', cbar_kws={'label': 'Average Tip ($)'})
plt.title('Average Tip Amount by Day and Time', fontsize=14, fontweight='bold')
# So what? Sunday dinner has the highest average tip - schedule your best servers then.
save('task5_restaurant_tips')
