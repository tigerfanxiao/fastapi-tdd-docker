from fastapi import FastAPI, Depends
from app.config import get_settings, Settings

app = FastAPI()

@app.get("/ping")
async def pong(setting: Settings = Depends(get_settings)):

    return {
        "ping": "pong", 
        "environment": setting.environment,
        "testing": setting.testing,
    }
