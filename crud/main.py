from fastapi import FastAPI
from models.DBmodels import ProductBase
from models.PydanticSchemas import Product

app = FastAPI()

@app.post('/product/')
async def create_item():
    pass

@app.get('//')
async def get_item():
    pass

@app.delete('//')
async def delete_item():
    pass

@app.put('//')
async def edit_item():
    pass