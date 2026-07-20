import plotly.express as px
import pandas as pd


def category_chart(counter):

    df = pd.DataFrame(
        {
            "Category": list(counter.keys()),
            "Count": list(counter.values())
        }
    )

    fig = px.bar(
        df,
        x="Category",
        y="Count",
        title="Skill Distribution"
    )

    return fig