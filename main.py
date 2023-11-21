from fastapi import FastAPI
import uvicorn

app = FastAPI(title = 'Prueba de fast api',
              description='API creada con FastAPI',
              version='1.0.1')


@app.get('/')
async def index():
    return 'Hola a mi api con Fast API'


@app.get('/about')
async def index():
    return 'Acerca de este servicio web'

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)