"""Shared helpers: headless matplotlib + a save() that writes to docs/assets."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")
ASSETS = Path(__file__).resolve().parent.parent / "docs" / "assets"
ASSETS.mkdir(parents=True, exist_ok=True)


def save(name):
    plt.tight_layout()
    plt.savefig(ASSETS / f"{name}.png", dpi=150, bbox_inches="tight")
    plt.close()
