# Email: 23f1001296@ds.study.iitm.ac.in
# This Marimo notebook demonstrates variable dependencies, interactivity,
# dynamic markdown, and data flow between cells.

import marimo

app = marimo.App()

# ---------------------------------------------------------
# Cell 1: Load dataset
# Output is used by Cell 3
# ---------------------------------------------------------
@app.cell
def _():
    import numpy as np
    import pandas as pd

    df = pd.DataFrame({
        "x": np.linspace(0, 10, 100),
        "y": np.linspace(0, 10, 100)**2
    })

    df
    return df


# ---------------------------------------------------------
# Cell 2: Interactive slider
# Slider value is used by Cell 3 and Cell 4
# ---------------------------------------------------------
@app.cell
def _(mo):
    slider = mo.ui.slider(start=1, stop=10, step=1, value=5, label="Scale Factor")
    slider
    return slider


# ---------------------------------------------------------
# Cell 3: Data transformation
# Depends on df (Cell 1) and slider (Cell 2)
# ---------------------------------------------------------
@app.cell
def _(df, slider):
    df_scaled = df.copy()
    df_scaled["scaled_y"] = df_scaled["y"] * slider.value
    df_scaled
    return df_scaled


# ---------------------------------------------------------
# Cell 4: Dynamic markdown
# Reacts to slider's current value
# ---------------------------------------------------------
@app.cell
def _(mo, slider):
    mo.md(f"""
    ## 📊 Dynamic Analysis Report

    **Current scale factor:** `{slider.value}`

    Changing the slider updates the scaled values in real-time.
    """)
    return


# ---------------------------------------------------------
# Cell 5: Visualization (depends on Cell 3)
# ---------------------------------------------------------
@app.cell
def _(df_scaled):
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots()
    ax.plot(df_scaled["x"], df_scaled["scaled_y"])
    ax.set_title("Scaled Y vs X")
    ax.set_xlabel("x")
    ax.set_ylabel("scaled_y")

    fig
    return fig


app.run()
