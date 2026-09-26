# Data Visualization: Real-World Scenarios

Seven real-world scenarios, each solved by picking the **right chart for the question** and stating the insight in one sentence. Built with Python, pandas, Matplotlib, Seaborn and Plotly.

**Live page:** https://github.com/AsimaHabib/E-Commerce-Dashboard-NIAI-Training-/upload

## Tasks

| # | Scenario | Chart | Script |
|---|----------|-------|--------|
| 1 | Coffee shop: busiest days | Bar chart with highlight | `src/task1_coffee_shop.py` |
| 2 | Fitness tracker: 8,000-step goal | Line plot with goal line | `src/task2_fitness_tracker.py` |
| 3 | Streaming report: pie vs bar | Pie vs sorted horizontal bar | `src/task3_streaming_report.py` |
| 4 | Does studying help? | Scatter plot with trend line | `src/task4_study_vs_score.py` |
| 5 | Restaurant tips by day and time | Heatmap | `src/task5_restaurant_tips.py` |
| 6 | Wealth and health over time | Interactive animated Plotly scatter | `src/task6_gapminder_interactive.py` |
| 7 | E-commerce dashboard | 2x2 dashboard | `src/task7_ecommerce_dashboard.py` |

## Project structure

```
data-visualization-worksheet/
├── docs/                # GitHub Pages landing page
│   ├── index.html
│   └── assets/          # generated charts
├── notebook/            # original Jupyter notebook
├── src/                 # one script per task + run_all.py
├── requirements.txt
└── README.md
```

## Run it

```bash
pip install -r requirements.txt
python src/run_all.py            # regenerates every chart in docs/assets/
python src/task1_coffee_shop.py  # or run a single task
```

Task 5 downloads the `tips` dataset through Seaborn, so it needs an internet connection the first time.

## Publish the landing page

1. Push the repo to GitHub.
2. Go to **Settings > Pages**.
3. Set the source to **Deploy from a branch**, branch `main`, folder `/docs`.
4. Your page will be live at `https://github.com/AsimaHabib/E-Commerce-Dashboard-NIAI-Training-/upload`.

