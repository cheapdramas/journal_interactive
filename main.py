from fastapi import FastAPI,Request
from fastapi.templating import Jinja2Templates
import uvicorn
from pathlib import Path
import requests
from get_requests import router as router_get
path_cert = f'{Path(__file__).parent}' +'\cert.pem'
path_key = f'{Path(__file__).parent}' + '\key.pem'
ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
ssl_context.load_cert_chain(path_cert,keyfile=path_key)


app = FastAPI(ssl_keyfile=path_key,ssl_certfile = path_cert)
app.include_router(router_get)







if __name__ == '__main__':
    uvicorn.run('main:app',reload=True)