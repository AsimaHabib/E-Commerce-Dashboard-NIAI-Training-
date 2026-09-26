"""Task 4 - Does studying help? (scatter + regression line)"""
import matplotlib.pyplot as plt
import seaborn as sns
from utils import save

study_hours = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
exam_score = [52, 58, 61, 65, 70, 72, 78, 80, 83, 88]

plt.figure(figsize=(8, 5))
sns.regplot(x=study_hours, y=exam_score, scatter_kws={'s': 50, 'color': 'darkblue'}, line_kws={'color': 'red'})
plt.title('Strong Positive Relationship Between Study Time and Test Scores', fontsize=14, fontweight='bold')
plt.xlabel('Hours Studied')
plt.ylabel('Exam Score (%)')
# So what? Positive relationship: more study hours go with higher scores.
save('task4_study_vs_score')
