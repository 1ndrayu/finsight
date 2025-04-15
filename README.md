# FinSight API

**FinSight** is a lightweight financial insights API that parses personal transaction data (CSV) and delivers smart, structured analytics — from monthly summaries to spending alerts and trend visualizations.

Built using **FastAPI** and **Pandas**
---

## 🚀 Features

- ✅ **Monthly Summary** – income, expense, savings breakdown
- 📈 **Trend Analysis** – income vs. expenses over time
- ⚠️ **Spending Alerts** – flag unusually high transactions
- 🖼 **Graph API** – base64-encoded monthly financial chart
- 💡 Designed for easy expansion (e.g., budget goals, categories, AI tagging)

---

## 📦 Project Structure
structure.txt

---

## 🔌 API Endpoints

| Method | Route                | Description                                |
|--------|----------------------|--------------------------------------------|
| GET    | `/`                  | Welcome message                            |
| GET    | `/insights/monthly`  | Monthly summary of income, expense, net    |
| GET    | `/insights/trends`   | Monthly trend data                         |
| GET    | `/insights/alerts`   | Spending alerts (threshold parameter)      |
| GET    | `/insights/graph`    | Financial trend chart as base64 image      |

---

## 🧪 Sample Response

`GET /insights/monthly`

```json
{
  "total_income": 15000,
  "total_expense": 8000,
  "net_savings": 7000,
  "category_breakdown": {
    "Food": 2500,
    "Transport": 1200,
    "Rent": 3000
  }
}
```
---
# Clone this repo
git clone https://github.com/your-username/FinSight.git
cd FinSight

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use venv\Scripts\activate

# Install requirements
pip install -r requirements.txt

# Run the server
uvicorn app.main:app --reload

Then visit 👉 http://127.0.0.1:8000/docs

---

# Future Improvements
- CSV upload support
- Auth via API token
- Budget tracking
- Category insights (AI-powered)
- Streamlit or React frontend

---

# License
MIT – feel free to use, extend, and credit!
