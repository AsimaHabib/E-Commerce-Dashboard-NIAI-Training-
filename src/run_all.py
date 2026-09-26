"""Run every task and regenerate all charts in docs/assets."""
import runpy
from pathlib import Path

for script in sorted(Path(__file__).parent.glob('task*.py')):
    print('Running', script.name)
    runpy.run_path(str(script))
print('Done - charts saved to docs/assets/')
