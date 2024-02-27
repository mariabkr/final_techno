from fastapi import FastAPI
from app.routes.lib import router as librairie_router

app=FastAPI(title="Bibliothéque Universitaire Moretus Plantin")
app.include_router(librairie_router)

@app.on_event('start')
def starting():
    print('serveur started.')

def sleep ():
    print('thank you !')
    
