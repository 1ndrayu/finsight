import pandas as pd
import matplotlib.pyplot as plt
import io
import base64

def get_monthly_summary():
    df = pd.read_csv("data/transactions.csv", parse_dates=["date"])

    summary = {
        "total_income": df[df["type"] == "credit"]["amount"].sum(),
        "total_expense": df[df["type"] == "debit"]["amount"].sum(),
        "net_savings": df["amount"].sum()
    }

    category_expense = df[df["type"] == "debit"].groupby("category")["amount"].sum().abs().to_dict()
    summary["category_breakdown"] = category_expense

    return summary

def get_trend():
    df = pd.read_csv("data/transactions.csv", parse_dates=["date"])
    df["month"] = df["date"].dt.to_period("M")

    trend = df.groupby(["month", "type"])["amount"].sum().unstack(fill_value=0)
    trend["net"] = trend.get("credit", 0) + trend.get("debit", 0)

    trend = trend.reset_index()
    trend["month"] = trend["month"].astype(str)
    return trend.to_dict(orient="records")

def get_alerts(threshold=500):
    df = pd.read_csv("data/transactions.csv", parse_dates=["date"])
    df = df[df["type"] == "debit"]
    alerts = df[df["amount"].abs() > threshold]

    return alerts[["date", "amount", "category", "description"]].to_dict(orient="records")

def generate_trend_graph():
    df = pd.read_csv("data/transactions.csv", parse_dates=["date"])
    df["month"] = df["date"].dt.to_period("M")

    grouped = df.groupby(["month", "type"])["amount"].sum().unstack(fill_value=0)
    grouped["net"] = grouped.get("credit", 0) + grouped.get("debit", 0)

    # Plot
    plt.figure(figsize=(10, 6))
    grouped[["credit", "debit", "net"]].plot(kind="bar")
    plt.title("Monthly Financial Trends")
    plt.xlabel("Month")
    plt.ylabel("Amount")
    plt.tight_layout()

    # Save to buffer
    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    img_bytes = base64.b64encode(buf.read()).decode("utf-8")
    buf.close()
    plt.close()

    return {"image_base64": img_bytes}
