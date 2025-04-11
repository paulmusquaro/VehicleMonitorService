from fastapi import FastAPI
from src.routes import company_routes
import uvicorn


app = FastAPI(title="Vehicle Monitor Service")

app.include_router(company_routes.router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
