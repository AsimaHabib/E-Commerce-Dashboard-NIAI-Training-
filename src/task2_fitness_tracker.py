"""Task 2 - Fitness tracker: which days missed the 8,000-step goal? (line + goal line)"""
import matplotlib.pyplot as plt
from utils import save

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
steps = [6200, 8100, 7400, 9500, 11000, 3200, 5400]

plt.figure(figsize=(8, 5))
plt.plot(days, steps, marker='o', color='purple', linewidth=2, label='Daily Steps')
plt.axhline(y=8000, color='red', linestyle='--', linewidth=2, label='Daily Goal (8k Steps)')
plt.title('Step Progression Over the Week Against 8,000 Step Goal', fontsize=14, fontweight='bold')
plt.xlabel('Day of the Week')
plt.ylabel('Steps Count')
plt.legend()
# So what? Goal missed on Mon, Wed, Sat and Sun; hit on Tue, Thu and Fri.
save('task2_fitness_tracker')
