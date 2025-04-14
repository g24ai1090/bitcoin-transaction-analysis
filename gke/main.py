from fastapi import FastAPI

app = FastAPI()

# This is where you define the endpoint for "/api/"
@app.get("/api/")
async def root():
    return {"message": "API Root"}

# Add any other routes you have here
@app.get("/top-transactions")
async def get_top_transactions():
    # Logic for handling top transactions goes here
    return {"top_transactions": "data"}