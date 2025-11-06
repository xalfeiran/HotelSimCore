from fastapi import FastAPI
from api import router as api_router
from simulation import start_simulation
import uvicorn

app = FastAPI(title="Hotel Simulation Core")

app.include_router(api_router, prefix="/api")

@app.on_event("startup")
async def startup_event():
    await start_simulation()

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
