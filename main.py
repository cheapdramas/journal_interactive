from fastapi import FastAPI,Request
from fastapi.templating import Jinja2Templates
import uvicorn
from pathlib import Path
import requests
from get_requests import router as router_get



app = FastAPI()
app.include_router(router_get)







if __name__ == '__main__':
    uvicorn.run('main:app',reload=True)