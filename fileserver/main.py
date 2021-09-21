from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from routes import router

app = FastAPI()

app.include_router(router)

@app.get('/')
def home():
    return HTMLResponse()