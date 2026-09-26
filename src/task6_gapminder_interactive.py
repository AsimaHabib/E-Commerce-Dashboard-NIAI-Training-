"""Task 6 - Startup pitch: interactive animated Plotly scatter (writes an HTML file)"""
import plotly.express as px
from utils import ASSETS

fig = px.scatter(
    px.data.gapminder(), x='gdpPercap', y='lifeExp',
    animation_frame='year', animation_group='country',
    size='pop', color='continent', hover_name='country',
    log_x=True, size_max=55, range_x=[100, 100000], range_y=[25, 90],
    title='Global Health and Wealth Progression Over the Decades',
    labels={'gdpPercap': 'GDP Per Capita (Log Scale)', 'lifeExp': 'Life Expectancy (Years)'},
)
# So what? Countries move up and to the right: richer and longer-lived over time.
fig.write_html(ASSETS / 'task6_gapminder.html', include_plotlyjs='cdn')
