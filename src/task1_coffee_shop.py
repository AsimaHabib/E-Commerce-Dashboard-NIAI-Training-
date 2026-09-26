"""Task 1 - Coffee shop: which days are busiest? (bar chart + highlight)"""
import matplotlib.pyplot as plt
from utils import save

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
cups = [120, 135, 128, 140, 180, 260, 240]
colors = ['#1f77b4' if d not in ['Sat', 'Sun'] else '#ff7f0e' for d in days]

plt.figure(figsize=(8, 5))
plt.bar(days, cups, color=colors)
plt.title('Weekend Cup Sales Outperform Weekdays Significantly', fontsize=14, fontweight='bold')
plt.xlabel('Day of the Week')
plt.ylabel('Cups Sold')
# So what? The busiest days are Sat and Sun, so the owner should add staff on weekends.
save('task1_coffee_shop')
