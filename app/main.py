from fastapi import FastAPI
from fastapi import Query
from app.insights import get_monthly_summary, get_trend
from fastapi.responses import JSONResponse

app = FastAPI(title="FinSight API")

@app.get("/")
def read_root():
    return {"message": "Welcome to FinSight API"}

@app.get("/insights/monthly")
def monthly_summary():
    return get_monthly_summary()

@app.get("/insights/trends")
def monthly_trends():
    return get_trend()

@app.get("/insights/alerts")
def spending_alerts(threshold: int = Query(500)):
    return get_alerts(threshold)

@app.get("/insights/graph")
def show_trend_graph():
    graph = generate_trend_graph()
    return JSONResponse(content=graph)
