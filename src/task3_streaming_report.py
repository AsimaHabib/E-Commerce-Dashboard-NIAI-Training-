"""Task 3 - Streaming report: pie (bad) vs sorted horizontal bar (good)"""
import matplotlib.pyplot as plt
import pandas as pd
from utils import save

genres = ['Drama', 'Comedy', 'Action', 'Docs', 'Horror', 'Sci-Fi']
hours = [42, 39, 36, 30, 28, 25]

fig, axes = plt.subplots(1, 2, figsize=(14, 6))
axes[0].pie(hours, labels=genres, autopct='%1.1f%%', startangle=90)
axes[0].set_title('Pie Chart: Hard to Rank', fontsize=12, fontweight='bold')

df = pd.DataFrame({'Genre': genres, 'Hours': hours}).sort_values('Hours')
axes[1].barh(df['Genre'], df['Hours'], color='teal')
axes[1].set_title('Sorted Bar: Ranking Is Obvious', fontsize=12, fontweight='bold')
axes[1].set_xlabel('Hours Watched')
axes[1].set_ylabel('Genre')
# So what? The sorted bar chart answers "which genre is #1?" instantly (Drama).
save('task3_streaming_report')
