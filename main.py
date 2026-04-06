from fastapi import FastAPI

app = FastAPI()

# Sample data
users = [
    {"id": 1, "name": "Admin", "role": "admin"},
    {"id": 2, "name": "User", "role": "viewer"}
]

records = []

# Home API
@app.get("/")
def home():
    return {"message": "Finance Backend Running"}

# Get users
@app.get("/users")
def get_users():
    return users

# Add record
@app.post("/records")
def add_record(record: dict):
    records.append(record)
    return {"message": "Record added"}

# Get records
@app.get("/records")
def get_records():
    return records

# Summary API
@app.get("/summary")
def get_summary():
    income = sum(r["amount"] for r in records if r["type"] == "income")
    expense = sum(r["amount"] for r in records if r["type"] == "expense")

    return {
        "total_income": income,
        "total_expense": expense,
        "balance": income - expense
    }
